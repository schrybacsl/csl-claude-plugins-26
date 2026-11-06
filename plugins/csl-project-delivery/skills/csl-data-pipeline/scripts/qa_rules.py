#!/usr/bin/env python3
"""
qa_rules.py — data-QA findings on a pull snapshot, each with its tier and rule ID
(csl-data-pipeline SKILL.md Section 3.5; rules from csl-schedule-risk/references/tier-rules.md).

Tests
  schema drift     columns missing or renamed since the previous pull        -> STOP (exit 2)
  silent lapse     END passed, not closed, % and status unchanged vs previous,
                   no constraint or comment recorded                          -> RED (R4)
                   same but a constraint is recorded                          -> AMBER (A3)
                   END passed, not closed, but % or status moved              -> AMBER (A2)
                   END passed, not closed, no previous pull to test against   -> AMBER (A2), R4 untested
  inverted dates   START after END                                            -> AMBER (A6)
  mixed ID formats IDs matching and not matching --id-regex in one sheet      -> AMBER (A6), population
  missing baseline blank baseline column                                      -> AMBER (A6), population
  duplicates       repeated --dup-key                                         -> AMBER (A6)
  RPN arithmetic   RPN C not equal to SEV x Occ x Det                         -> AMBER (A6)
  missing dates    blank START or END (only with --require-dates)             -> AMBER (A6)

Population findings (mixed IDs, missing baseline) are one finding each with the
count and examples, because tiering every row for one data condition buries the
report (tier-rules.md, rule of use 3). Rows carrying a defect are excluded from
roll-ups with a footnote; the fix goes on the docket with the sheet owner.

Examples
  python3 qa_rules.py --current outputs/W77/pulls/2026-09-18/2158727850315652.csv \
      --previous outputs/W77/pulls/2026-09-11/2158727850315652.csv \
      --id-col "WS #" --id-regex "^WS-\\d{2}\\.\\d{2}(\\.\\d{2})?$" --baseline-col "Baseline Status" \
      --end-col "Target Date" --as-of 2026-09-18 --out findings.csv
  python3 qa_rules.py --current permits.csv --start-col START --end-col END --dup-key "Permit #"

Exit codes: 0 no findings; 1 findings; 2 schema drift (stop and confirm the column map before reporting).
"""
from __future__ import annotations

import argparse
import re
import signal
import sys
from datetime import date
from pathlib import Path

import pandas as pd

if hasattr(signal, "SIGPIPE"):  # let `| head` close the pipe quietly
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import (  # noqa: E402
    META_COLS, normalize_frame, now_et, parent_mask, pick_label_col, read_snapshot, to_iso_date, to_number,
)

STATUS_CANDIDATES = ["Status", "Status Type", "State", "Health", "Lifecycle Step", "Step"]
CONSTRAINT_CANDIDATES = ["Constraints", "Constraint", "Blocker"]
COMMENT_CANDIDATES = ["General Comments", "Comments", "Comment", "Notes", "Update"]
BASELINE_CANDIDATES = ["Baseline Status", "Baseline Start", "Baseline Finish"]


def _first_present(df: pd.DataFrame, explicit: str | None, candidates: list[str]) -> str | None:
    if explicit:
        return explicit if explicit in df.columns else None
    for c in candidates:
        if c in df.columns:
            return c
    return None


def _pct_series(df: pd.DataFrame, col: str | None) -> pd.Series:
    if not col or col not in df.columns:
        return pd.Series([None] * len(df), index=df.index, dtype="object")
    vals = df[col].map(to_number)
    numeric = pd.to_numeric(vals, errors="coerce")
    if numeric.notna().any() and numeric.max() <= 1.0:
        numeric = numeric * 100.0
    return numeric


def _date_series(df: pd.DataFrame, col: str | None) -> pd.Series:
    if not col or col not in df.columns:
        return pd.Series([None] * len(df), index=df.index, dtype="object")
    return df[col].map(to_iso_date)


def finding(rule: str, tier: str, scope: str, key: str, label: str, detail: str, evidence: str = "") -> dict:
    return {"rule_id": rule, "tier": tier, "scope": scope, "row_key": key, "label": label, "detail": detail, "evidence": evidence}


def run_rules(cur: pd.DataFrame, prev: pd.DataFrame | None, *, key: str, label_col: str | None, as_of: date,
              start_col: str | None, end_col: str | None, pct_col: str | None, status_col: str | None,
              constraint_col: str | None, comment_col: str | None, id_col: str | None, id_regex: str | None,
              baseline_col: str | None, baseline_scope: str, dup_key: list[str], require_dates: bool,
              closed_values: set[str]) -> tuple[list[dict], bool]:
    """Return (findings, schema_drift_stop)."""
    out: list[dict] = []
    stop = False
    labels = cur[label_col].astype(str) if label_col and label_col in cur.columns else cur[key].astype(str)

    # 1. Schema drift
    if prev is not None:
        only_prev = sorted(set(prev.columns) - set(cur.columns) - set(META_COLS))
        only_cur = sorted(set(cur.columns) - set(prev.columns) - set(META_COLS))
        if only_prev or only_cur:
            stop = True
            out.append(finding("SCHEMA", "STOP", "sheet", "", "column map",
                               f"columns missing since previous pull {only_prev}; new columns {only_cur}",
                               "confirm renames with the sheet owner and update the report config before computing anything"))

    starts, ends, pct = _date_series(cur, start_col), _date_series(cur, end_col), _pct_series(cur, pct_col)
    status = cur[status_col].astype(str) if status_col and status_col in cur.columns else pd.Series([""] * len(cur), index=cur.index)
    constraint = cur[constraint_col].astype(str) if constraint_col and constraint_col in cur.columns else pd.Series([""] * len(cur), index=cur.index)
    comment = cur[comment_col].astype(str) if comment_col and comment_col in cur.columns else pd.Series([""] * len(cur), index=cur.index)

    prev_idx = None
    if prev is not None and key in prev.columns:
        prev_idx = prev.drop_duplicates(key).set_index(key)

    # 2. Silent lapse / past END
    for i in cur.index:
        e = ends.loc[i]
        if not e:
            continue
        end_d = date.fromisoformat(e)
        if end_d >= as_of:
            continue
        p = pct.loc[i]
        closed = (p is not None and pd.notna(p) and p >= 100) or status.loc[i].strip().lower() in closed_values
        if closed:
            continue
        days = (as_of - end_d).days
        k = str(cur.loc[i, key])
        lab = labels.loc[i]
        pct_txt = "blank" if p is None or pd.isna(p) else f"{p:g}%"
        if prev_idx is None or k not in prev_idx.index:
            out.append(finding("A2", "AMBER (A2)", "row", k, lab,
                               f"END {e} passed {days} days ago; not closed ({pct_txt}); R4 untested, no previous pull for this row",
                               f"{end_col}={e}; {pct_col or '%'}={pct_txt}"))
            continue
        pr = prev_idx.loc[k]
        prev_p = to_number(pr[pct_col]) if pct_col and pct_col in prev_idx.columns else None
        if prev_p is not None and prev_p <= 1.0 and p is not None and pd.notna(p) and p > 1.0:
            prev_p *= 100.0
        prev_status = str(pr[status_col]) if status_col and status_col in prev_idx.columns else ""
        moved = (prev_p is not None and p is not None and pd.notna(p) and abs(prev_p - p) > 1e-9) or (prev_status != status.loc[i])
        has_reason = bool(constraint.loc[i].strip()) or bool(comment.loc[i].strip())
        if moved:
            out.append(finding("A2", "AMBER (A2)", "row", k, lab,
                               f"END {e} passed {days} days ago; progress moved ({prev_p if prev_p is not None else 'blank'} to {pct_txt}; status {prev_status!r} to {status.loc[i]!r}) but not closed",
                               f"{end_col}={e}"))
        elif constraint.loc[i].strip():
            out.append(finding("A3", "AMBER (A3)", "row", k, lab,
                               f"END {e} passed {days} days ago; no status change; constraint recorded: {constraint.loc[i].strip()} (check its age; >2 weeks stays A3 with the enabling owner named)",
                               f"{end_col}={e}; {pct_col or '%'}={pct_txt}"))
        elif has_reason:
            out.append(finding("A2", "AMBER (A2)", "row", k, lab,
                               f"END {e} passed {days} days ago; no status change; comment recorded, no constraint picklist value",
                               f"comment: {comment.loc[i].strip()[:80]}"))
        else:
            out.append(finding("R4", "RED (R4)", "row", k, lab,
                               f"silent lapse: END {e} passed {days} days ago; % ({pct_txt}) and status unchanged since previous pull; no constraint or comment",
                               f"{end_col}={e}; previous {pct_col or '%'}={prev_p if prev_p is not None else 'blank'}"))

    # 3. Inverted dates
    for i in cur.index:
        s, e = starts.loc[i], ends.loc[i]
        if s and e and s > e:
            out.append(finding("A6", "AMBER (A6)", "row", str(cur.loc[i, key]), labels.loc[i],
                               f"dates inverted: {start_col} {s} is after {end_col} {e}; correction requested from the sheet owner",
                               f"{start_col}={s}; {end_col}={e}"))

    # 4. Missing dates (optional)
    if require_dates:
        for i in cur.index:
            miss = [c for c, v in ((start_col, starts.loc[i]), (end_col, ends.loc[i])) if c and not v]
            if miss:
                out.append(finding("A6", "AMBER (A6)", "row", str(cur.loc[i, key]), labels.loc[i],
                                   f"missing {', '.join(miss)}; row cannot be scheduled or aged", ""))

    # 5. Mixed ID formats (population)
    if id_col and id_col in cur.columns and id_regex:
        rx = re.compile(id_regex)
        ids = cur[id_col].astype(str).str.strip()
        nonblank = ids[ids != ""]
        ok = nonblank[nonblank.map(lambda v: bool(rx.match(v)))]
        bad = nonblank[~nonblank.index.isin(ok.index)]
        if len(ok) and len(bad):
            out.append(finding("A6", "AMBER (A6)", "population", "", id_col,
                               f"mixed ID formats: {len(ok)} rows match {id_regex!r}, {len(bad)} do not (e.g. {', '.join(bad.head(5))}); "
                               f"nonconforming rows excluded from roll-ups with a footnote; fix on the docket with the sheet owner",
                               "csl-document-control 1.2: one format per tracker"))

    # 6. Missing baseline (population)
    if baseline_col and baseline_col in cur.columns:
        scope_mask = pd.Series([True] * len(cur), index=cur.index)
        if baseline_scope == "children":
            scope_mask = ~parent_mask(cur)
        elif baseline_scope == "parents":
            scope_mask = parent_mask(cur)
        blank = cur.loc[scope_mask, baseline_col].astype(str).str.strip() == ""
        if int(blank.sum()):
            ex = labels[scope_mask][blank].head(5).tolist()
            out.append(finding("A6", "AMBER (A6)", "population", "", baseline_col,
                               f"{int(blank.sum())} of {int(scope_mask.sum())} rows (scope: {baseline_scope}) have no {baseline_col}; "
                               f"they cannot roll up against baseline (e.g. {', '.join(ex)})", ""))

    # 7. Duplicates
    if dup_key:
        cols = [c for c in dup_key if c in cur.columns]
        if cols:
            k = cur[cols].astype(str).agg("|".join, axis=1)
            dups = k[k.duplicated(keep=False) & (k.str.strip("|") != "")]
            for val in sorted(dups.unique()):
                rows = cur.index[k == val]
                out.append(finding("A6", "AMBER (A6)", "population", val, val,
                                   f"duplicate {'+'.join(cols)} on {len(rows)} rows", ""))

    # 8. RPN arithmetic
    if {"SEV", "Occ", "Det", "RPN C"} <= set(cur.columns):
        for i in cur.index:
            s, o, d, r = (to_number(cur.loc[i, c]) for c in ("SEV", "Occ", "Det", "RPN C"))
            if None in (s, o, d, r):
                continue
            if abs(s * o * d - r) > 0.5:
                out.append(finding("A6", "AMBER (A6)", "row", str(cur.loc[i, key]), labels.loc[i],
                                   f"RPN C {r:g} does not equal SEV x Occ x Det = {s:g} x {o:g} x {d:g} = {s * o * d:g}",
                                   "tracker entry conflicting with itself"))
    return out, stop


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--current", required=True, help="current snapshot CSV")
    p.add_argument("--previous", help="previous snapshot CSV (enables schema drift and silent-lapse tests)")
    p.add_argument("--key", default="_row_id", help="row key column")
    p.add_argument("--label-col", help="human label column")
    p.add_argument("--as-of", help="YYYY-MM-DD; default today (ET)")
    p.add_argument("--start-col", default="START")
    p.add_argument("--end-col", default="END")
    p.add_argument("--pct-col", default="%")
    p.add_argument("--status-col", help="status column (auto: Status, Status Type, State, Health)")
    p.add_argument("--constraint-col", help="constraint column (auto: Constraints)")
    p.add_argument("--comment-col", help="comment column (auto: General Comments, Comments)")
    p.add_argument("--closed-values", default="closed,complete,completed,done,cancelled,canceled",
                   help="status values that count as closed")
    p.add_argument("--id-col", help="ID column for the mixed-format test")
    p.add_argument("--id-regex", help="regex a conforming ID must match, e.g. ^WS-\\d{2}\\.\\d{2}(\\.\\d{2})?$")
    p.add_argument("--baseline-col", help="baseline column (auto: Baseline Status, Baseline Start)")
    p.add_argument("--baseline-scope", choices=["all", "children", "parents"], default="all")
    p.add_argument("--dup-key", action="append", default=[], help="column(s) that must be unique; repeat for composite")
    p.add_argument("--require-dates", action="store_true", help="flag blank START/END")
    p.add_argument("--parents-only", action="store_true", help="test parent rows only")
    p.add_argument("--out", help="write findings CSV here")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cur = normalize_frame(read_snapshot(args.current))
    prev = normalize_frame(read_snapshot(args.previous)) if args.previous else None
    if args.parents_only:
        cur = cur[parent_mask(cur)].copy()
        if prev is not None:
            prev = prev[parent_mask(prev)].copy()
    if args.key not in cur.columns:
        print(f"key column {args.key!r} not in current file; pass --key", file=sys.stderr)
        return 2
    as_of = date.fromisoformat(args.as_of) if args.as_of else now_et().date()
    label_col = pick_label_col(cur, args.label_col)
    findings, stop = run_rules(
        cur, prev, key=args.key, label_col=label_col, as_of=as_of,
        start_col=args.start_col if args.start_col in cur.columns else None,
        end_col=args.end_col if args.end_col in cur.columns else None,
        pct_col=args.pct_col if args.pct_col in cur.columns else None,
        status_col=_first_present(cur, args.status_col, STATUS_CANDIDATES),
        constraint_col=_first_present(cur, args.constraint_col, CONSTRAINT_CANDIDATES),
        comment_col=_first_present(cur, args.comment_col, COMMENT_CANDIDATES),
        id_col=args.id_col, id_regex=args.id_regex,
        baseline_col=_first_present(cur, args.baseline_col, BASELINE_CANDIDATES), baseline_scope=args.baseline_scope,
        dup_key=args.dup_key, require_dates=args.require_dates,
        closed_values={v.strip().lower() for v in args.closed_values.split(",") if v.strip()},
    )
    df = pd.DataFrame(findings, columns=["rule_id", "tier", "scope", "row_key", "label", "detail", "evidence"])
    order = {"STOP": 0, "RED (R4)": 1, "AMBER (A3)": 2, "AMBER (A2)": 3, "AMBER (A6)": 4}
    if len(df):
        df = df.assign(_o=df["tier"].map(lambda t: order.get(t, 9))).sort_values(["_o", "label"]).drop(columns="_o")
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(args.out, index=False, lineterminator="\n")

    print(f"QA findings: {Path(args.current).name} as of {as_of.isoformat()}; rows tested {len(cur)}"
          f"{'; previous ' + Path(args.previous).name if args.previous else ''}")
    counts = df["tier"].value_counts().to_dict() if len(df) else {}
    print("Counts: " + (", ".join(f"{k} {v}" for k, v in counts.items()) if counts else "none"))
    print()
    print("| Tier (rule) | Scope | Row / ID | Detail | Evidence |")
    print("|---|---|---|---|---|")
    for _, r in df.iterrows():
        print(f"| {r['tier']} | {r['scope']} | {r['label'] or r['row_key']} | {r['detail']} | {r['evidence']} |")
    if stop:
        print("\nSTOP: schema drift; confirm the column map before any roll-up.", file=sys.stderr)
        return 2
    return 1 if len(df) else 0


if __name__ == "__main__":
    raise SystemExit(main())

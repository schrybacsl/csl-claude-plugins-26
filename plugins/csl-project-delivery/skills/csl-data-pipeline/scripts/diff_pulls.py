#!/usr/bin/env python3
"""
diff_pulls.py — row-level diff between two pull snapshots: what was added, removed,
and changed (per cell, old -> new), written as CSVs plus the Markdown "what moved"
table that csl-schedule-risk and csl-weekly-reporting consume (SKILL.md Section 3.4).

Both files are normalized with the same rules as the pull (pipeline_common), so a
formatting difference never shows as a change and a real change always does.
Rows are keyed by _row_id (stable Smartsheet row ID); pass --key for exports that
lack it (a composite key is formed when --key is repeated).

Examples
  python3 diff_pulls.py --old outputs/W77/pulls/2026-09-11/1059284113641348.csv \
      --new outputs/W77/pulls/2026-09-18/1059284113641348.csv --parents-only \
      --sheet-name "W77 Roadmap Master" --sheet-id 1059284113641348
  python3 diff_pulls.py --old last_week.csv --new this_week.csv --key "Task Name" --key START

Outputs (in --out-dir, default <new dir>/diff_<old>_to_<new>/):
  added.csv, removed.csv, changed_cells.csv, what_moved.md, diff_summary.json
and one appended line in the running change log (--changelog, default
<pulls root>/changelog_<sheet-id>.csv when the sheet id is known).

Exit codes: 0 no differences; 1 differences found; 2 input error.
"""
from __future__ import annotations

import argparse
import json
import signal
import sys
from datetime import date
from pathlib import Path

import pandas as pd

if hasattr(signal, "SIGPIPE"):  # let `| head` close the pipe quietly
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import (  # noqa: E402
    META_COLS, fmt_et, frame_md5, load_sidecar, normalize_frame, now_et, parent_mask,
    pick_label_col, read_snapshot, short_md5, to_iso_date, to_number,
)


def _pull_label(csv_path: Path, sidecar: dict) -> str:
    """Pull timestamp from the sidecar, else the date folder, else the file name."""
    if sidecar.get("pulled_at_display"):
        return sidecar["pulled_at_display"]
    parent = csv_path.resolve().parent.name
    return parent if parent and parent[:4].isdigit() else csv_path.name


def _sidecar_for(csv_path: Path) -> dict:
    j = csv_path.with_suffix(".json")
    if j.exists():
        try:
            return load_sidecar(j)
        except (OSError, json.JSONDecodeError):
            pass
    return {}


def _keyed(df: pd.DataFrame, key_cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    out["_key"] = out[key_cols].astype(str).agg("|".join, axis=1) if len(key_cols) > 1 else out[key_cols[0]].astype(str)
    return out


def _delta(old: str, new: str) -> str:
    """Numeric difference, or day difference for dates, else blank."""
    a, b = to_number(old), to_number(new)
    if a is not None and b is not None:
        d = b - a
        return f"{d:+g}"
    da, db = to_iso_date(old), to_iso_date(new)
    if da and db:
        days = (date.fromisoformat(db) - date.fromisoformat(da)).days
        return f"{days:+d} days"
    return ""


def diff_frames(old: pd.DataFrame, new: pd.DataFrame, key_cols: list[str], ignore_cols: set[str],
                label_col: str | None) -> dict:
    """Core diff. Returns dict with added/removed/changed frames and summary counts."""
    o, n = _keyed(old, key_cols), _keyed(new, key_cols)
    dup_old = int(o["_key"].duplicated().sum())
    dup_new = int(n["_key"].duplicated().sum())
    o = o.drop_duplicates("_key", keep="first").set_index("_key")
    n = n.drop_duplicates("_key", keep="first").set_index("_key")

    cols_old, cols_new = set(old.columns), set(new.columns)
    only_old = sorted(cols_old - cols_new)
    only_new = sorted(cols_new - cols_old)
    compare_cols = [c for c in new.columns if c in cols_old and c not in ignore_cols
                    and c not in ("_key", "_row_number") and c not in key_cols]

    added_keys = [k for k in n.index if k not in o.index]
    removed_keys = [k for k in o.index if k not in n.index]
    common = [k for k in n.index if k in o.index]

    records = []
    for k in common:
        ro, rn = o.loc[k], n.loc[k]
        for c in compare_cols:
            vo, vn = str(ro[c]), str(rn[c])
            if vo != vn:
                label = str(rn[label_col]) if label_col and label_col in n.columns else k
                records.append({"key": k, "label": label, "column": c, "old": vo, "new": vn, "delta": _delta(vo, vn)})
    changed = pd.DataFrame(records, columns=["key", "label", "column", "old", "new", "delta"])
    return {
        "added": n.loc[added_keys].reset_index(),
        "removed": o.loc[removed_keys].reset_index(),
        "changed_cells": changed,
        "changed_rows": int(changed["key"].nunique()) if len(changed) else 0,
        "compared_rows": len(common),
        "only_in_old_cols": only_old,
        "only_in_new_cols": only_new,
        "duplicate_keys": {"old": dup_old, "new": dup_new},
        "compare_cols": compare_cols,
    }


def what_moved_markdown(res: dict, meta: dict, top: int) -> str:
    """The one-page 'what moved' table: Row / ID | Field | Last pull | This pull | Delta | Tier (rule) | Cause | Owner | Next action."""
    lines = []
    ident = "identical" if meta["identical"] else "changed"
    lines.append(f"# What moved: {meta['sheet_name']} ({meta['sheet_id']})")
    lines.append("")
    lines.append(f"Last pull {meta['old_label']} (md5 {short_md5(meta['old_md5'])}); this pull {meta['new_label']} "
                 f"(md5 {short_md5(meta['new_md5'])}); hash {ident}. Rows compared {res['compared_rows']}; "
                 f"added {len(res['added'])}; removed {len(res['removed'])}; changed {res['changed_rows']} rows / "
                 f"{len(res['changed_cells'])} cells. Generated {meta['generated']}.")
    if res["only_in_old_cols"] or res["only_in_new_cols"]:
        lines.append("")
        lines.append(f"**Schema drift, stop and confirm before reporting:** columns only in last pull {res['only_in_old_cols']}; "
                     f"only in this pull {res['only_in_new_cols']}.")
    if res["duplicate_keys"]["old"] or res["duplicate_keys"]["new"]:
        lines.append("")
        lines.append(f"Duplicate keys (data defect, AMBER (A6) candidate): last pull {res['duplicate_keys']['old']}, this pull {res['duplicate_keys']['new']}.")
    lines.append("")
    lines.append("Tier, cause, owner, and next action are filled by the analyst per csl-schedule-risk; the script fills the evidence columns only.")
    lines.append("")
    lines.append("| Row / ID | Field | Last pull | This pull | Delta | Tier (rule) | Cause | Owner | Next action, date |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    cc = res["changed_cells"]
    shown = 0
    for _, r in cc.head(top).iterrows():
        lines.append(f"| {r['label']} | {r['column']} | {r['old']} | {r['new']} | {r['delta']} |  |  |  |  |")
        shown += 1
    for _, r in res["added"].head(max(0, top - shown)).iterrows():
        lab = r.get(meta["label_col"], r["_key"]) if meta["label_col"] else r["_key"]
        lines.append(f"| {lab} | (row added) |  | new row |  |  |  |  |  |")
    for _, r in res["removed"].head(max(0, top - shown)).iterrows():
        lab = r.get(meta["label_col"], r["_key"]) if meta["label_col"] else r["_key"]
        lines.append(f"| {lab} | (row removed) | present |  |  |  |  |  |  |")
    if len(cc) > top:
        lines.append("")
        lines.append(f"Table truncated to {top} changed cells; changed_cells.csv holds all {len(cc)}.")
    lines.append("")
    lines.append(f"Source: {meta['sheet_name']} (ID {meta['sheet_id']}) pulled {meta['old_label']} and {meta['new_label']}; "
                 f"key {meta['key']}; columns compared {len(res['compare_cols'])}.")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--old", required=True, help="previous snapshot CSV")
    p.add_argument("--new", required=True, help="current snapshot CSV")
    p.add_argument("--key", action="append", default=[], help="key column(s); default _row_id; repeat for a composite key")
    p.add_argument("--label-col", help="column used to name rows in the table (default: first sensible title column)")
    p.add_argument("--ignore-cols", default="", help="comma list of columns to ignore (e.g. Modified,Modified By)")
    p.add_argument("--parents-only", action="store_true", help="compare parent rows only (_indent == 0)")
    p.add_argument("--out-dir", help="where to write outputs")
    p.add_argument("--changelog", help="running change log CSV to append to")
    p.add_argument("--sheet-name", default="", help="for the table header (falls back to the sidecar)")
    p.add_argument("--sheet-id", default="", help="for the table header and change log name (falls back to the sidecar)")
    p.add_argument("--top", type=int, default=200, help="max changed cells shown in the Markdown table")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    old_path, new_path = Path(args.old), Path(args.new)
    for p in (old_path, new_path):
        if not p.exists():
            print(f"missing file: {p}", file=sys.stderr)
            return 2
    old = normalize_frame(read_snapshot(old_path))
    new = normalize_frame(read_snapshot(new_path))
    if args.parents_only:
        old, new = old[parent_mask(old)].copy(), new[parent_mask(new)].copy()

    key_cols = args.key or (["_row_id"] if "_row_id" in old.columns and "_row_id" in new.columns else [])
    if not key_cols:
        print("no _row_id in both files; pass --key <column> (repeat for a composite key)", file=sys.stderr)
        return 2
    for k in key_cols:
        if k not in old.columns or k not in new.columns:
            print(f"key column {k!r} missing from one of the files", file=sys.stderr)
            return 2
    ignore = {c.strip() for c in args.ignore_cols.split(",") if c.strip()}
    label_col = pick_label_col(new, args.label_col)

    res = diff_frames(old, new, key_cols, ignore, label_col)
    sc_old, sc_new = _sidecar_for(old_path), _sidecar_for(new_path)
    old_md5 = sc_old.get("md5") or frame_md5(old)
    new_md5 = sc_new.get("md5") or frame_md5(new)
    meta = {
        "sheet_name": args.sheet_name or sc_new.get("sheet_name") or new_path.stem,
        "sheet_id": args.sheet_id or sc_new.get("sheet_id") or new_path.stem,
        "old_label": _pull_label(old_path, sc_old),
        "new_label": _pull_label(new_path, sc_new),
        "old_md5": old_md5, "new_md5": new_md5, "identical": old_md5 == new_md5,
        "generated": fmt_et(now_et()), "key": "+".join(key_cols), "label_col": label_col,
    }

    out_dir = Path(args.out_dir) if args.out_dir else new_path.parent / f"diff_{old_path.stem}_to_{new_path.stem}"
    out_dir.mkdir(parents=True, exist_ok=True)
    res["added"].to_csv(out_dir / "added.csv", index=False, lineterminator="\n")
    res["removed"].to_csv(out_dir / "removed.csv", index=False, lineterminator="\n")
    res["changed_cells"].to_csv(out_dir / "changed_cells.csv", index=False, lineterminator="\n")
    md = what_moved_markdown(res, meta, args.top)
    (out_dir / "what_moved.md").write_text(md, encoding="utf-8")
    summary = {
        **{k: v for k, v in meta.items()},
        "rows_old": int(len(old)), "rows_new": int(len(new)), "compared_rows": res["compared_rows"],
        "added": int(len(res["added"])), "removed": int(len(res["removed"])),
        "changed_rows": res["changed_rows"], "changed_cells": int(len(res["changed_cells"])),
        "only_in_old_cols": res["only_in_old_cols"], "only_in_new_cols": res["only_in_new_cols"],
        "duplicate_keys": res["duplicate_keys"], "parents_only": bool(args.parents_only),
        "old_file": str(old_path), "new_file": str(new_path),
    }
    (out_dir / "diff_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")

    changelog = Path(args.changelog) if args.changelog else (
        new_path.parent.parent / f"changelog_{meta['sheet_id']}.csv" if meta["sheet_id"] else None)
    if changelog:
        row = pd.DataFrame([{
            "old_snapshot": meta["old_label"], "new_snapshot": meta["new_label"],
            "old_md5": old_md5, "new_md5": new_md5, "identical": meta["identical"],
            "rows_old": len(old), "rows_new": len(new), "added": len(res["added"]), "removed": len(res["removed"]),
            "changed_rows": res["changed_rows"], "changed_cells": len(res["changed_cells"]),
            "schema_drift": bool(res["only_in_old_cols"] or res["only_in_new_cols"]), "generated_at": meta["generated"],
        }])
        changelog.parent.mkdir(parents=True, exist_ok=True)
        row.to_csv(changelog, mode="a", header=not changelog.exists(), index=False, lineterminator="\n")

    print(md)
    print(f"written: {out_dir}")
    differences = summary["added"] + summary["removed"] + summary["changed_cells"]
    return 1 if differences else 0


if __name__ == "__main__":
    raise SystemExit(main())

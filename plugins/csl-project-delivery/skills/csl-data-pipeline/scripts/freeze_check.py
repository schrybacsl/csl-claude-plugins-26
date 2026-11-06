#!/usr/bin/env python3
"""
freeze_check.py — compare the md5 of the last N snapshots of one sheet and report the
frozen streak with its tier (csl-data-pipeline SKILL.md Section 3.5; tier rules A4 and
R5 in csl-schedule-risk/references/tier-rules.md).

A sheet whose normalized CSV hashes identically to the previous pull is frozen one
pull: AMBER (A4). Frozen across two or more consecutive weekly pulls while field
witnesses (permits started or closed, deliveries, minuted closures) show movement:
RED (R5). Frozen two or more pulls with no witness of movement: AMBER (A4) held
open, witnesses sought. The script computes the streak; the analyst supplies the
witnesses with --field-movement, because the sheet cannot testify about the field.

Examples
  python3 freeze_check.py --sheet-id 1059284113641348 --pulls-dir outputs/W77/pulls --last 6 \
      --field-movement "SIPP 53782 started 09/16/26; SIPP 51718 closed 09/18/26"
  python3 freeze_check.py --files w1.csv w2.csv w3.csv          # offline: order = chronological

Exit codes: 0 always (the tier is the finding, not a failure).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import find_snapshots, frame_md5, normalize_frame, read_snapshot, short_md5  # noqa: E402


def chain(snaps: list[dict]) -> list[dict]:
    """Mark each snapshot identical/changed against the one before it."""
    out = []
    prev = None
    for s in snaps:
        identical = prev is not None and prev["md5"] == s["md5"]
        out.append({**s, "identical_to_previous": identical})
        prev = s
    return out


def streak(rows: list[dict]) -> int:
    """Consecutive identical pulls counted back from the latest."""
    n = 0
    for r in reversed(rows):
        if r["identical_to_previous"]:
            n += 1
        else:
            break
    return n


def tier_for(frozen: int, field_movement: str) -> tuple[str, str]:
    if frozen == 0:
        return "GREEN (G)", "hash changed against the previous pull; the byte-identity test does not fire"
    if frozen == 1:
        return "AMBER (A4)", "byte-identical to the previous pull; name the rows expected to move"
    if field_movement.strip():
        return "RED (R5)", f"byte-identical across {frozen} consecutive pulls while the field moved: {field_movement.strip()}"
    return "AMBER (A4) held open", f"byte-identical across {frozen} consecutive pulls; no field witness supplied, witnesses sought"


def sentence(sheet: str, rows: list[dict], frozen: int, tier: str, field_movement: str) -> str:
    latest = rows[-1]
    through = latest.get("pulled_at_display") or latest["date"]
    base = f"{sheet} unchanged for {frozen} consecutive pull{'s' if frozen != 1 else ''} through {through}, {tier}"
    if frozen == 0:
        return f"{sheet} changed between the last two pulls (md5 {short_md5(rows[-2]['md5']) if len(rows) > 1 else 'n/a'} to {short_md5(latest['md5'])}), {tier}."
    if field_movement.strip():
        return f"{base}; milestones lapsed inside the window: <name rows>; field movement in the same window: {field_movement.strip()}."
    return f"{base}; rows expected to move: <name rows>; field witnesses sought before R5 applies."


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--sheet-id", help="sheet ID; snapshots are read from --pulls-dir sidecars")
    src.add_argument("--files", nargs="+", help="offline: snapshot CSVs in chronological order (md5 computed here)")
    p.add_argument("--pulls-dir", help="pulls root, e.g. outputs/W77/pulls (with --sheet-id)")
    p.add_argument("--last", type=int, default=6, help="how many most-recent snapshots to compare")
    p.add_argument("--field-movement", default="", help="witnesses of field movement inside the frozen window (permits, deliveries, minuted closures)")
    p.add_argument("--hash-ignore", default="", help="with --files: comma list of columns excluded from the md5")
    p.add_argument("--sheet-name", default="", help="name for the sentence form")
    p.add_argument("--json", action="store_true", help="emit JSON instead of the table")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.sheet_id:
        if not args.pulls_dir:
            print("--pulls-dir is required with --sheet-id", file=sys.stderr)
            return 0
        found = find_snapshots(args.pulls_dir, args.sheet_id)
        snaps = [{"date": s["date"], "pulled_at_display": s["sidecar"].get("pulled_at_display", s["date"]),
                  "md5": s["md5"], "rows": s["row_count"], "cols": s["column_count"], "file": s["csv"]} for s in found]
        sheet = args.sheet_name or (found[-1]["sidecar"].get("sheet_name") if found else "") or f"sheet {args.sheet_id}"
    else:
        ignore = [c.strip() for c in args.hash_ignore.split(",") if c.strip()]
        snaps = []
        for f in args.files:
            df = normalize_frame(read_snapshot(f))
            snaps.append({"date": Path(f).parent.name or Path(f).stem, "pulled_at_display": Path(f).name,
                          "md5": frame_md5(df, ignore), "rows": len(df),
                          "cols": len([c for c in df.columns if not str(c).startswith("_")]), "file": f})
        sheet = args.sheet_name or Path(args.files[-1]).stem

    if not snaps:
        print("no snapshots found", file=sys.stderr)
        return 0
    rows = chain(snaps[-args.last:])
    frozen = streak(rows)
    tier, why = tier_for(frozen, args.field_movement)
    result = {"sheet": sheet, "pulls_compared": len(rows), "frozen_streak": frozen, "tier": tier, "reason": why,
              "sentence": sentence(sheet, rows, frozen, tier, args.field_movement),
              "chain": [{k: v for k, v in r.items() if k != "sidecar"} for r in rows]}
    if args.json:
        print(json.dumps(result, indent=2, default=str))
        return 0
    print(f"Freeze check: {sheet}  ({len(rows)} pulls compared)")
    print(f"{'pull':<22}{'md5':<16}{'rows':>7}{'cols':>6}  identical to previous")
    for r in rows:
        print(f"{str(r.get('pulled_at_display') or r['date']):<22}{short_md5(r['md5']):<16}{str(r.get('rows') or ''):>7}"
              f"{str(r.get('cols') or ''):>6}  {'yes' if r['identical_to_previous'] else 'no'}")
    print(f"\nFrozen streak: {frozen} consecutive identical pull(s) -> {tier}: {why}")
    print(f"Sentence form: {result['sentence']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

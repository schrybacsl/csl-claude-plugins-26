#!/usr/bin/env python3
"""
smartsheet_pull.py — full-sheet pull with column map, indent, display values, and a
timestamped snapshot plus JSON sidecar (csl-data-pipeline SKILL.md, Sections 3.1–3.3).

Why a full pull: the Smartsheet connector's server-side date filter is defective on
the W77 workspace, so every pull takes the whole sheet and filters locally. Why a
sidecar: the report's source note and the freeze check need sheet name, ID, pull
timestamp (ET), row count, column count, and the md5 of the normalized CSV, and
those must be recorded at pull time, not reconstructed later.

Modes
  sdk   smartsheet-python-sdk (optional import; pip install smartsheet-python-sdk)
  rest  requests against https://api.smartsheet.com/2.0 with pagination (>500 rows)
  csv   --from-csv <export or prior snapshot>: offline ingestion of an xlsx/csv export

Token: environment variable named by --token-env (default ASMLW77). Never printed.

Examples
  python3 smartsheet_pull.py --sheet-id 1059284113641348 --out-dir outputs/W77/pulls \
      --program W77 --sheet-name "W77 Roadmap Master 2025-2032"
  python3 smartsheet_pull.py --sheet-id 7673437876080516 --out-dir outputs/W77/pulls \
      --from-csv exports/Sheet_-_J_2026_CSL_Tasks.csv --key "Task Name" --program W77
  python3 smartsheet_pull.py --sheet-id 289677048237956 --out-dir outputs/W77/pulls \
      --mode rest --include attachments,discussions

Exit codes: 0 pulled; 2 configuration error (no token, bad file); 3 API failure after retries.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys
import time
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import (  # noqa: E402
    META_COLS, fmt_et, frame_md5, iso_et, normalize_frame, now_et, parent_mask,
    previous_snapshot, read_snapshot, short_md5, write_snapshot,
)

BASE_URL = "https://api.smartsheet.com/2.0"
RETRY_STATUS = {429, 500, 502, 503, 504}


# --------------------------------------------------------------------------- #
# Retry
# --------------------------------------------------------------------------- #
def _retry(fn, attempts: int = 5, base_sleep: float = 1.5):
    """Call fn(); on a rate-limit or 5xx style failure back off and retry.

    Smartsheet allows roughly 300 requests per minute per token; a 429 carries a
    Retry-After header, which is honored when present.
    """
    last = None
    for i in range(attempts):
        try:
            return fn()
        except _RetryableError as exc:  # raised by the REST path
            last = exc
            sleep = exc.retry_after or base_sleep * (2 ** i)
        except Exception as exc:  # SDK exceptions carry a status code attribute
            last = exc
            code = getattr(getattr(exc, "message", None), "status_code", None) or getattr(exc, "status_code", None)
            if code not in RETRY_STATUS:
                raise
            sleep = base_sleep * (2 ** i)
        time.sleep(sleep)
    raise RuntimeError(f"gave up after {attempts} attempts: {last}")


class _RetryableError(Exception):
    def __init__(self, msg: str, retry_after: float | None = None):
        super().__init__(msg)
        self.retry_after = retry_after


# --------------------------------------------------------------------------- #
# Row assembly shared by SDK and REST
# --------------------------------------------------------------------------- #
def _indent_from_parents(rows: list[dict]) -> None:
    """Fill _indent as depth in the parentId chain (0 = parent / top level).

    The GET response does not reliably populate `indent`; parentId is reliable.
    """
    parent_of = {r["_row_id"]: r.get("_parent_id") for r in rows}
    cache: dict = {}

    def depth(rid):
        if rid in cache:
            return cache[rid]
        pid = parent_of.get(rid)
        d = 0 if not pid else 1 + depth(pid)
        cache[rid] = d
        return d

    for r in rows:
        r["_indent"] = depth(r["_row_id"])


def _frame_from_rows(rows: list[dict], column_titles: list[str]) -> pd.DataFrame:
    cols = META_COLS + [c for c in column_titles if c not in META_COLS]
    extra = sorted({k for r in rows for k in r.keys()} - set(cols))
    df = pd.DataFrame(rows, columns=cols + extra)
    return df


def pull_via_sdk(sheet_id: int, token: str, values: str = "display", include: tuple[str, ...] = ()) -> tuple[pd.DataFrame, str]:
    """Full pull through smartsheet-python-sdk. Returns (frame, sheet name)."""
    import smartsheet  # optional dependency; imported only when used

    client = smartsheet.Smartsheet(token)
    client.errors_as_exceptions(True)
    page, page_size, rows, col_map, titles, name = 1, 500, [], {}, [], None
    while True:
        kwargs = {"page_size": page_size, "page": page}
        if include:
            kwargs["include"] = list(include)
        sheet = _retry(lambda: client.Sheets.get_sheet(sheet_id, **kwargs))
        if not col_map:
            for col in sheet.columns:
                col_map[col.id] = col.title
                titles.append(col.title)
            name = sheet.name
        for row in sheet.rows:
            rec = {
                "_row_id": str(row.id),
                "_row_number": row.row_number,
                "_parent_id": str(row.parent_id) if getattr(row, "parent_id", None) else "",
                "_indent": 0,
            }
            for cell in row.cells:
                title = col_map.get(cell.column_id, f"Col_{cell.column_id}")
                disp = getattr(cell, "display_value", None)
                raw = getattr(cell, "value", None)
                rec[title] = raw if values == "raw" else (disp if disp not in (None, "") else raw)
            if "attachments" in include:
                rec["_attachment_count"] = len(getattr(row, "attachments", None) or [])
            if "discussions" in include:
                rec["_discussion_count"] = len(getattr(row, "discussions", None) or [])
            rows.append(rec)
        total = getattr(sheet, "total_row_count", None) or len(rows)
        if len(rows) >= total or not sheet.rows:
            break
        page += 1
    _indent_from_parents(rows)
    return _frame_from_rows(rows, titles), name or str(sheet_id)


def pull_via_rest(sheet_id: int, token: str, values: str = "display", include: tuple[str, ...] = (), page_size: int = 500) -> tuple[pd.DataFrame, str]:
    """Full pull through the REST API with pagination. Returns (frame, sheet name)."""
    import requests

    headers = {"Authorization": f"Bearer {token}"}
    page, rows, col_map, titles, name = 1, [], {}, [], None

    def get(params):
        resp = requests.get(f"{BASE_URL}/sheets/{sheet_id}", headers=headers, params=params, timeout=90)
        if resp.status_code in RETRY_STATUS:
            ra = resp.headers.get("Retry-After")
            raise _RetryableError(f"HTTP {resp.status_code}", float(ra) if ra else None)
        resp.raise_for_status()
        return resp.json()

    while True:
        params = {"pageSize": page_size, "page": page}
        if include:
            params["include"] = ",".join(include)
        data = _retry(lambda: get(params))
        if not col_map:
            for col in sorted(data["columns"], key=lambda c: c.get("index", 0)):
                col_map[col["id"]] = col["title"]
                titles.append(col["title"])
            name = data.get("name")
        for row in data.get("rows", []):
            rec = {
                "_row_id": str(row["id"]),
                "_row_number": row.get("rowNumber"),
                "_parent_id": str(row["parentId"]) if row.get("parentId") else "",
                "_indent": row.get("indent", 0) or 0,
            }
            for cell in row.get("cells", []):
                title = col_map.get(cell.get("columnId"), f"Col_{cell.get('columnId')}")
                disp, raw = cell.get("displayValue"), cell.get("value")
                rec[title] = raw if values == "raw" else (disp if disp not in (None, "") else raw)
            if "attachments" in include:
                rec["_attachment_count"] = len(row.get("attachments") or [])
            if "discussions" in include:
                rec["_discussion_count"] = len(row.get("discussions") or [])
            rows.append(rec)
        if page >= int(data.get("totalPages", 1) or 1):
            break
        page += 1
    _indent_from_parents(rows)
    return _frame_from_rows(rows, titles), name or str(sheet_id)


def load_from_csv(path: str, key_cols: list[str], indent_col: str | None) -> tuple[pd.DataFrame, dict]:
    """Offline ingestion of an export or a prior snapshot; synthesizes meta columns when absent."""
    df = read_snapshot(path)
    df.columns = [str(c).strip() for c in df.columns]
    notes: dict = {"source_file": str(path)}
    if "_row_id" not in df.columns:
        if key_cols:
            missing = [k for k in key_cols if k not in df.columns]
            if missing:
                raise SystemExit(f"--key column(s) not in file: {missing}")
            df.insert(0, "_row_id", df[key_cols].astype(str).agg("|".join, axis=1)
                      .map(lambda s: hashlib.md5(s.encode("utf-8")).hexdigest()[:16]))
            notes["synthetic_row_id"] = f"md5 of {key_cols}"
        else:
            df.insert(0, "_row_id", [str(i + 1) for i in range(len(df))])
            notes["synthetic_row_id"] = "row position (pass --key for a stable key)"
    if "_row_number" not in df.columns:
        df.insert(1, "_row_number", [i + 1 for i in range(len(df))])
    if "_parent_id" not in df.columns:
        df.insert(2, "_parent_id", "")
    if "_indent" not in df.columns:
        if indent_col and indent_col in df.columns:
            df.insert(3, "_indent", pd.to_numeric(df[indent_col], errors="coerce").fillna(0).astype(int))
            notes["indent_from"] = indent_col
        else:
            df.insert(3, "_indent", 0)
            notes["indent_from"] = "none (all rows treated as parents)"
    return df, notes


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--sheet-id", required=True, help="Smartsheet sheet ID (recorded even for --from-csv)")
    p.add_argument("--out-dir", required=True, help="pulls root, e.g. outputs/W77/pulls")
    p.add_argument("--program", default="", help="program code for the sidecar, e.g. W77")
    p.add_argument("--sheet-name", default="", help="sheet name for the sidecar when the API does not supply it")
    p.add_argument("--mode", choices=["auto", "sdk", "rest"], default="auto", help="API path; auto = sdk if importable else rest")
    p.add_argument("--token-env", default="ASMLW77", help="environment variable holding the API token")
    p.add_argument("--values", choices=["display", "raw"], default="display", help="display_value (as seen) or raw value")
    p.add_argument("--include", default="", help="comma list: attachments,discussions (adds count columns)")
    p.add_argument("--from-csv", help="offline: ingest this csv/xlsx export or prior snapshot instead of calling the API")
    p.add_argument("--key", action="append", default=[], help="with --from-csv: column(s) to synthesize a stable _row_id")
    p.add_argument("--indent-col", help="with --from-csv: column carrying indent level")
    p.add_argument("--hash-ignore", default="", help="comma list of columns excluded from the md5 (e.g. Modified,Modified By)")
    p.add_argument("--overwrite", action="store_true", help="overwrite a same-day snapshot instead of suffixing _HHMM")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    include = tuple(x.strip() for x in args.include.split(",") if x.strip())
    hash_ignore = [x.strip() for x in args.hash_ignore.split(",") if x.strip()]
    pulled_at = now_et()
    notes: dict = {}

    if args.from_csv:
        raw, notes = load_from_csv(args.from_csv, args.key, args.indent_col)
        sheet_name, source = args.sheet_name or Path(args.from_csv).stem, f"csv:{args.from_csv}"
    else:
        token = os.environ.get(args.token_env)
        if not token:
            print(f"no token in ${args.token_env}; use --from-csv for offline work", file=sys.stderr)
            return 2
        mode = args.mode
        if mode == "auto":
            try:
                import smartsheet  # noqa: F401
                mode = "sdk"
            except ImportError:
                mode = "rest"
        try:
            if mode == "sdk":
                raw, sheet_name = pull_via_sdk(int(args.sheet_id), token, args.values, include)
            else:
                raw, sheet_name = pull_via_rest(int(args.sheet_id), token, args.values, include)
        except Exception as exc:  # network / API failure after retries
            print(f"pull failed ({mode}): {exc}", file=sys.stderr)
            return 3
        sheet_name = args.sheet_name or sheet_name
        source = f"smartsheet-{mode}"

    df = normalize_frame(raw)
    md5 = frame_md5(df, hash_ignore)
    parents = int(parent_mask(df).sum())
    prev = previous_snapshot(args.out_dir, args.sheet_id, iso_et(pulled_at))
    prev_block = None
    if prev:
        prev_block = {"date": prev["date"], "pulled_at": prev["pulled_at"], "md5": prev["md5"],
                      "identical": prev["md5"] == md5}

    sidecar = {
        "program": args.program,
        "sheet_name": sheet_name,
        "sheet_id": str(args.sheet_id),
        "pulled_at": iso_et(pulled_at),
        "pulled_at_display": fmt_et(pulled_at),
        "source": source,
        "values": args.values,
        "row_count": int(len(df)),
        "column_count": int(len([c for c in df.columns if c not in META_COLS])),
        "parent_rows": parents,
        "child_rows": int(len(df) - parents),
        "md5": md5,
        "md5_ignore_cols": hash_ignore,
        "columns": [c for c in df.columns if c not in META_COLS],
        "server_side_filters": "none (connector date filter defective; filter locally)",
        "previous": prev_block,
        "notes": notes,
    }
    csv_path, json_path = write_snapshot(df, args.out_dir, str(args.sheet_id), sidecar, pulled_at, args.overwrite)

    # Pull log block (SKILL.md Section 4.1) — paste into the source note as-is.
    prev_line = "previous  none on file"
    if prev_block:
        prev_line = (f"previous  {prev_block['date']} md5 {short_md5(prev_block['md5'])}  "
                     f"{'IDENTICAL' if prev_block['identical'] else 'changed'}")
    print(f"PULL      {sheet_name} ({args.sheet_id})")
    print(f"pulled_at {fmt_et(pulled_at)}   source {source}")
    print(f"rows      {len(df)} (parents {parents}, children {len(df) - parents})   columns {sidecar['column_count']}")
    print(f"md5       {md5} (normalized CSV{', ignoring ' + ','.join(hash_ignore) if hash_ignore else ''})")
    print(prev_line)
    print(f"snapshot  {csv_path} (+ {json_path.name})")
    if notes:
        print(f"notes     {notes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

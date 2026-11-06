#!/usr/bin/env python3
"""
Shared helpers for the csl-data-pipeline scripts.

Every script in this folder imports from here so that normalization, hashing,
snapshot layout, and timestamps are identical across pulls, diffs, freeze checks,
and QA. Nothing in this module touches the network.

Snapshot layout (csl-data-pipeline SKILL.md, Section 3.1):

    <pulls-dir>/<yyyy-mm-dd>/<sheet-id>.csv     normalized full pull
    <pulls-dir>/<yyyy-mm-dd>/<sheet-id>.json    sidecar: sheet name, id, pull
                                                timestamp (ET), rows, cols, md5,
                                                column list, source

Normalization rules (NORMALIZATION_VERSION 1): strip whitespace; blanks and
NaN-like tokens become ""; US dates M/D/YY or M/D/YYYY become ISO YYYY-MM-DD;
currency and thousands-separated numbers become plain decimals; percentages
drop the sign ("45%" -> "45"). Two pulls that differ only in formatting hash the
same, so a changed md5 always means a changed value, and an unchanged md5 across
pulls is the byte-identity evidence behind AMBER (A4) and RED (R5).

Usage from a sibling script:

    import sys; from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from pipeline_common import normalize_frame, frame_md5, write_snapshot
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Iterable
from zoneinfo import ZoneInfo

import pandas as pd

ET = ZoneInfo("America/New_York")
NORMALIZATION_VERSION = "1"
META_COLS = ["_row_id", "_row_number", "_parent_id", "_indent"]
NA_TOKENS = {"", "nan", "none", "nat", "null", "n/a"}

_CURRENCY = re.compile(r"^\(?-?\$\s?-?[\d,]*\.?\d+\)?$")
_PERCENT = re.compile(r"^-?[\d,]*\.?\d+\s?%$")
_NUMBER = re.compile(r"^-?[\d,]*\.?\d+$")
_DATE_US = re.compile(r"^(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})$")
_DATE_ISO = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
_DATETIME_ISO = re.compile(r"^(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2})(:\d{2})?")


# --------------------------------------------------------------------------- #
# Time
# --------------------------------------------------------------------------- #
def now_et() -> datetime:
    """Current time in Eastern Time (W77 and the northeast programs report in ET)."""
    return datetime.now(ET)


def fmt_et(dt: datetime) -> str:
    """Source-note form: MM/DD/YY HH:MM ET (csl-document-control Section 4)."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ET)
    return dt.astimezone(ET).strftime("%m/%d/%y %H:%M ET")


def iso_et(dt: datetime) -> str:
    """Sidecar form: ISO 8601 with offset, second precision."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ET)
    return dt.astimezone(ET).isoformat(timespec="seconds")


def date_folder(dt: datetime) -> str:
    """Folder name for a pull: the ET calendar date, yyyy-mm-dd."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ET)
    return dt.astimezone(ET).strftime("%Y-%m-%d")


# --------------------------------------------------------------------------- #
# Cell and frame normalization
# --------------------------------------------------------------------------- #
def _fmt_number(x: float) -> str:
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return f"{x:.6f}".rstrip("0").rstrip(".")


def to_number(s) -> float | None:
    """Parse a currency, percent, or plain number string; None when it is not one."""
    if s is None:
        return None
    t = str(s).strip()
    if not t:
        return None
    neg = t.startswith("(") and t.endswith(")")
    t = t.strip("()").replace("$", "").replace(",", "").replace("%", "").strip()
    if not _NUMBER.match(t):
        return None
    try:
        v = float(t)
    except ValueError:
        return None
    return -v if neg else v


def to_iso_date(s) -> str | None:
    """Return YYYY-MM-DD for a US or ISO date string; None when it is not a date."""
    if s is None:
        return None
    t = str(s).strip()
    m = _DATE_US.match(t)
    if m:
        mm, dd, yy = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if yy < 100:
            yy += 2000
        try:
            return date(yy, mm, dd).isoformat()
        except ValueError:
            return None
    m = _DATE_ISO.match(t)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3))).isoformat()
        except ValueError:
            return None
    m = _DATETIME_ISO.match(t)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3))).isoformat()
        except ValueError:
            return None
    return None


def normalize_cell(v) -> str:
    """Normalize one cell to its canonical string (see module docstring)."""
    if v is None:
        return ""
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, float):
        if v != v:  # NaN
            return ""
        return _fmt_number(v)
    if isinstance(v, int):
        return str(v)
    s = str(v).strip()
    if s.lower() in NA_TOKENS:
        return ""
    if _DATE_US.match(s) or _DATE_ISO.match(s):
        d = to_iso_date(s)
        return d if d else s
    if _CURRENCY.match(s) or _PERCENT.match(s) or _NUMBER.match(s):
        n = to_number(s)
        return _fmt_number(n) if n is not None else s
    return s


def normalize_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with every cell normalized and every column named as a string."""
    out = df.copy()
    out.columns = [str(c).strip() for c in out.columns]
    mapper = getattr(out, "map", None) or getattr(out, "applymap")
    out = mapper(normalize_cell)
    return out.astype(str)


def frame_md5(df: pd.DataFrame, ignore_cols: Iterable[str] = ()) -> str:
    """md5 of the normalized CSV text (LF line endings, no index, sheet column order)."""
    ignore = set(ignore_cols)
    cols = [c for c in df.columns if c not in ignore]
    text = df[cols].to_csv(index=False, lineterminator="\n")
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def file_md5(path: str | Path) -> str:
    """md5 of a file's bytes (byte-identical re-send test for exports and zips)."""
    h = hashlib.md5()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def short_md5(h: str) -> str:
    return f"{h[:8]}…{h[-4:]}" if h and len(h) >= 12 else (h or "")


# --------------------------------------------------------------------------- #
# Snapshots
# --------------------------------------------------------------------------- #
def read_snapshot(path: str | Path) -> pd.DataFrame:
    """Read a snapshot or export CSV as strings with no NaN coercion."""
    p = Path(path)
    if p.suffix.lower() in {".xlsx", ".xlsm", ".xls"}:
        return pd.read_excel(p, dtype=str).fillna("")
    return pd.read_csv(p, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def load_sidecar(path: str | Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def snapshot_paths(pulls_dir: str | Path, date_str: str, sheet_id: str, suffix: str = "") -> tuple[Path, Path]:
    folder = Path(pulls_dir) / date_str
    stem = f"{sheet_id}{suffix}"
    return folder / f"{stem}.csv", folder / f"{stem}.json"


def write_snapshot(df: pd.DataFrame, pulls_dir: str | Path, sheet_id: str, sidecar: dict,
                   pulled_at: datetime | None = None, overwrite: bool = False) -> tuple[Path, Path]:
    """Write <pulls-dir>/<yyyy-mm-dd>/<sheet-id>.csv and .json; never overwrite unless told.

    A second pull on the same day gets a _HHMM suffix so both snapshots survive
    (csl-document-control Section 8: pull data is retained with the report).
    """
    pulled_at = pulled_at or now_et()
    day = date_folder(pulled_at)
    csv_path, json_path = snapshot_paths(pulls_dir, day, sheet_id)
    if csv_path.exists() and not overwrite:
        suffix = "_" + pulled_at.astimezone(ET).strftime("%H%M%S")
        csv_path, json_path = snapshot_paths(pulls_dir, day, sheet_id, suffix)
        n = 2
        while csv_path.exists():
            csv_path, json_path = snapshot_paths(pulls_dir, day, sheet_id, f"{suffix}-{n}")
            n += 1
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path, index=False, lineterminator="\n")
    sidecar = dict(sidecar)
    sidecar.setdefault("snapshot_csv", str(csv_path))
    sidecar.setdefault("normalization_version", NORMALIZATION_VERSION)
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(sidecar, fh, indent=2, sort_keys=True, default=str)
    return csv_path, json_path


def find_snapshots(pulls_dir: str | Path, sheet_id: str) -> list[dict]:
    """All sidecars for a sheet under pulls_dir, oldest first.

    Each item: {"date", "pulled_at", "md5", "row_count", "column_count", "csv", "json", "sidecar"}.
    """
    root = Path(pulls_dir)
    items: list[dict] = []
    if not root.exists():
        return items
    for json_path in sorted(root.glob(f"*/{sheet_id}*.json")):
        try:
            sc = load_sidecar(json_path)
        except (OSError, json.JSONDecodeError):
            continue
        if str(sc.get("sheet_id", "")) != str(sheet_id):
            continue
        csv_path = json_path.with_suffix(".csv")
        items.append({
            "date": json_path.parent.name,
            "pulled_at": sc.get("pulled_at", json_path.parent.name),
            "md5": sc.get("md5", ""),
            "row_count": sc.get("row_count"),
            "column_count": sc.get("column_count"),
            "csv": str(csv_path),
            "json": str(json_path),
            "sidecar": sc,
        })
    items.sort(key=lambda d: str(d["pulled_at"]))
    return items


def previous_snapshot(pulls_dir: str | Path, sheet_id: str, before_iso: str) -> dict | None:
    """The most recent snapshot already on file at `before_iso` (ISO timestamp); the new pull is not yet written."""
    earlier = [s for s in find_snapshots(pulls_dir, sheet_id) if str(s["pulled_at"]) <= before_iso]
    return earlier[-1] if earlier else None


# --------------------------------------------------------------------------- #
# Frame conveniences
# --------------------------------------------------------------------------- #
LABEL_CANDIDATES = [
    "Roadmap + Equipment + Task", "Task Name", "Task", "Primary", "Name", "Title",
    "Permit", "Permit #", "Project", "Description", "WS #", "WS", "ID",
]


def pick_label_col(df: pd.DataFrame, preferred: str | None = None) -> str | None:
    """Choose the column that names a row for humans (tables, what-moved output)."""
    if preferred and preferred in df.columns:
        return preferred
    for c in LABEL_CANDIDATES:
        if c in df.columns:
            return c
    for c in df.columns:
        if c not in META_COLS:
            return c
    return None


def parent_mask(df: pd.DataFrame) -> pd.Series:
    """True for parent (top-level) rows: _indent == 0 or blank. Child rows are phases and double count."""
    if "_indent" not in df.columns:
        return pd.Series([True] * len(df), index=df.index)
    ind = pd.to_numeric(df["_indent"], errors="coerce").fillna(0)
    return ind <= 0


def parse_iso(ts: str) -> datetime | None:
    try:
        return datetime.fromisoformat(str(ts))
    except (TypeError, ValueError):
        return None

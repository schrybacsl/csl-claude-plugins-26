#!/usr/bin/env python3
"""
ctrw_pipeline_skeleton.py — skeleton of the CTRW test-rig telemetry pipeline
(csl-data-pipeline SKILL.md Section 3.7): parse / merge / classify / metrics, with the
dark-window classifier and the reservoir drawdown regression implemented against a
generic timestamp / volume / flow / valve CSV so the logic can be tested offline.

Production layout (two modules; this file carries both layers for portability):
  ctrw_lib.py   parse_log (channel-count-aware), merge_paths (dual path, zero overlap),
                detect_resends (md5), classify_dark_windows, drawdown_regression,
                uptime_minutes, valve_saturation, zero_flow_events, compute_metrics
  pipeline.py   orchestrator: unzip RE__<date>_TR7__TR2__TR5_Data_.zip -> resend check ->
                parse both logger paths per rig -> merge -> classify -> metrics ->
                formula-driven xlsx + branded PDF CSL-W77-CTRW-<rig>-<yymmdd> (report factory)

Program facts encoded in RIGS: TR7 logger m4535 (35 channels), TR2 logger m8357
(35 channels), TR5 logger m5794 (25 channels, no bath instrumentation). One logger per
rig alternates between a CT share path and a disk3 path with zero timestamp overlap, so
both paths are pulled and merged; cadence is mixed 30/60 s.

Dark-window classes
  true_dark              no data on either path; not explained by a file boundary or midnight cut
  export_artifact        gap at a file boundary shorter than the boundary tolerance, or a gap in
                         one path that the other path covers
  midnight_cut_artifact  short gap that straddles 00:00 (daily export cut)
  byte_identical_resend  a file whose md5 matches one already processed; not new data

Examples
  python3 ctrw_pipeline_skeleton.py --demo --out-dir /tmp/ctrw_demo
  python3 ctrw_pipeline_skeleton.py --rig TR7 --from-csv ct_share=ct/TR7_0820.csv \
      --from-csv disk3=disk3/TR7_0824.csv --min-volume 6.0 --as-of 2026-08-27 --out-dir outputs/W77/CTRW/2026

PDF-export logs: convert with `pdftotext -layout` first and map the columns in parse_log
(parse_pdf_export is a stub by design; the layout is site specific).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import fmt_et, now_et  # noqa: E402

RIGS = {
    "TR7": {"logger": "m4535", "channels": 35, "bath_instrumented": True},
    "TR2": {"logger": "m8357", "channels": 35, "bath_instrumented": True},
    "TR5": {"logger": "m5794", "channels": 25, "bath_instrumented": False},
}
PATH_LABELS = ("ct_share", "disk3")
ZIP_NAME_PATTERN = "RE__<date>_TR7__TR2__TR5_Data_.zip"
PROGRAM = "W77"


# --------------------------------------------------------------------------- #
# 1. Parse
# --------------------------------------------------------------------------- #
def detect_resends(files: list[str | Path], registry_path: str | Path | None = None) -> pd.DataFrame:
    """md5 every incoming file; flag files identical to a previously processed one or to each other.

    A re-sent file with an identical hash is not a new export, whatever the email says
    (csl-document-control Section 7.3). The registry JSON maps md5 -> first file name seen.
    """
    registry: dict = {}
    if registry_path and Path(registry_path).exists():
        registry = json.loads(Path(registry_path).read_text(encoding="utf-8"))
    rows = []
    seen_batch: dict = {}
    for f in files:
        p = Path(f)
        h = hashlib.md5(p.read_bytes()).hexdigest()
        resend_of = registry.get(h) or seen_batch.get(h) or ""
        rows.append({"file": p.name, "md5": h, "bytes": p.stat().st_size,
                     "class": "byte_identical_resend" if resend_of else "new",
                     "resend_of": resend_of})
        seen_batch.setdefault(h, p.name)
        registry.setdefault(h, p.name)
    if registry_path:
        Path(registry_path).parent.mkdir(parents=True, exist_ok=True)
        Path(registry_path).write_text(json.dumps(registry, indent=2, sort_keys=True), encoding="utf-8")
    return pd.DataFrame(rows, columns=["file", "md5", "bytes", "class", "resend_of"])


def parse_pdf_export(path: str | Path, rig: str) -> pd.DataFrame:
    """Stub: the logger's PDF export is converted with `pdftotext -layout <pdf> -` and the
    fixed-width table is mapped to channel columns per the rig's channel list. Site specific."""
    raise NotImplementedError("PDF-export parsing is site specific: run pdftotext -layout and map columns here")


def parse_log(path: str | Path, rig: str, *, ts_col: str = "timestamp", source: str = "ct_share") -> pd.DataFrame:
    """Read one logger file (CSV) into a timestamp-indexed frame; channel-count-aware.

    Validates the non-timestamp column count against RIGS[rig]["channels"] and records a
    warning column instead of failing, because a short channel set is itself a finding
    (TR5 has no bath channels; TR2 bath instrumentation was electrically faulted).
    """
    p = Path(path)
    if p.suffix.lower() == ".pdf":
        return parse_pdf_export(p, rig)
    df = pd.read_csv(p)
    if ts_col not in df.columns:
        raise ValueError(f"{p.name}: timestamp column {ts_col!r} not found; columns are {list(df.columns)[:8]}...")
    df[ts_col] = pd.to_datetime(df[ts_col], errors="coerce")
    df = df.dropna(subset=[ts_col]).sort_values(ts_col).drop_duplicates(ts_col, keep="first")
    expected = RIGS.get(rig, {}).get("channels")
    got = len([c for c in df.columns if c != ts_col])
    df["_source"] = source
    df["_file"] = p.name
    df.attrs["channel_check"] = {"rig": rig, "expected": expected, "found": got,
                                 "ok": expected is None or got == expected}
    return df.reset_index(drop=True)


# --------------------------------------------------------------------------- #
# 2. Merge
# --------------------------------------------------------------------------- #
def file_spans(frames: list[pd.DataFrame], ts_col: str = "timestamp") -> pd.DataFrame:
    rows = []
    for f in frames:
        if len(f):
            rows.append({"source": f["_source"].iloc[0], "file": f["_file"].iloc[0],
                         "start": f[ts_col].iloc[0], "end": f[ts_col].iloc[-1], "rows": len(f)})
    return pd.DataFrame(rows, columns=["source", "file", "start", "end", "rows"]).sort_values("start").reset_index(drop=True)


def merge_paths(frames: list[pd.DataFrame], ts_col: str = "timestamp") -> tuple[pd.DataFrame, dict]:
    """Concatenate every file from both logger paths, report overlap, keep one row per timestamp.

    The program's loggers alternate paths with zero overlap; a non-zero overlap count is
    reported, not silently averaged, and the first source in PATH_LABELS order wins.
    """
    if not frames:
        return pd.DataFrame(), {"overlap_timestamps": 0, "sources": {}}
    order = {lab: i for i, lab in enumerate(PATH_LABELS)}
    allf = pd.concat(frames, ignore_index=True)
    allf["_rank"] = allf["_source"].map(lambda s: order.get(s, 99))
    allf = allf.sort_values([ts_col, "_rank"])
    dup = allf.duplicated(ts_col, keep=False)
    overlap = int(allf.loc[dup, ts_col].nunique())
    merged = allf.drop_duplicates(ts_col, keep="first").drop(columns="_rank").reset_index(drop=True)
    report = {
        "overlap_timestamps": overlap,
        "sources": {s: {"rows": int((merged["_source"] == s).sum()),
                        "start": str(merged.loc[merged["_source"] == s, ts_col].min()),
                        "end": str(merged.loc[merged["_source"] == s, ts_col].max())}
                    for s in merged["_source"].unique()},
        "rows": int(len(merged)),
        "window": {"start": str(merged[ts_col].iloc[0]), "end": str(merged[ts_col].iloc[-1])},
    }
    return merged, report


# --------------------------------------------------------------------------- #
# 3. Classify
# --------------------------------------------------------------------------- #
def infer_cadence(ts: pd.Series, top: int = 2) -> dict[int, float]:
    """Modal sample intervals in seconds with their share of intervals (mixed 30/60 s is normal)."""
    d = ts.sort_values().diff().dt.total_seconds().dropna().round()
    if d.empty:
        return {}
    vc = d.value_counts(normalize=True)
    out = {int(k): round(float(v), 3) for k, v in vc.head(top).items() if v >= 0.10}
    return out or {int(vc.index[0]): round(float(vc.iloc[0]), 3)}


def find_gaps(ts: pd.Series, threshold_s: float) -> pd.DataFrame:
    t = ts.sort_values().reset_index(drop=True)
    d = t.diff().dt.total_seconds()
    idx = d.index[d > threshold_s]
    rows = [{"start": t[i - 1], "end": t[i], "duration_min": round(d[i] / 60.0, 1)} for i in idx]
    return pd.DataFrame(rows, columns=["start", "end", "duration_min"])


def classify_dark_windows(merged: pd.DataFrame, spans: pd.DataFrame, single_frames: list[pd.DataFrame], *,
                          ts_col: str = "timestamp", cadence_s: dict[int, float] | None = None, min_gap_min: float = 5.0,
                          midnight_tol_min: float = 30.0, boundary_tol_h: float = 6.0) -> pd.DataFrame:
    """Classify every gap above threshold as true_dark, export_artifact, or midnight_cut_artifact.

    Order of tests: midnight cut (short gap straddling 00:00) -> file boundary (gap ends
    where the next file starts, within tolerance) -> covered by the other path -> true dark.
    Gaps that exist in a single path but are covered after the merge are reported as
    export artifacts so the weekly summary can say how many "dark" hours were not dark.
    """
    cadence_s = cadence_s or infer_cadence(merged[ts_col])
    cad_max = max(cadence_s) if cadence_s else 60
    threshold = max(min_gap_min * 60.0, 3.0 * cad_max)
    rows = []
    merged_gaps = find_gaps(merged[ts_col], threshold)
    ends = {pd.Timestamp(e): (s, f) for s, f, e in zip(spans["source"], spans["file"], spans["end"])} if len(spans) else {}
    starts = {pd.Timestamp(s0): (s, f) for s, f, s0 in zip(spans["source"], spans["file"], spans["start"])} if len(spans) else {}
    for _, g in merged_gaps.iterrows():
        start, end, dur = pd.Timestamp(g["start"]), pd.Timestamp(g["end"]), float(g["duration_min"])
        straddles_midnight = start.normalize() != end.normalize()
        if straddles_midnight and dur <= midnight_tol_min:
            rows.append({"start": start, "end": end, "duration_min": dur, "class": "midnight_cut_artifact",
                         "evidence": f"gap straddles 00:00 and lasts {dur:g} min (daily export cut)"})
            continue
        at_end = ends.get(start)
        at_start = starts.get(end)
        if at_end and at_start and dur <= boundary_tol_h * 60:
            rows.append({"start": start, "end": end, "duration_min": dur, "class": "export_artifact",
                         "evidence": f"file boundary: {at_end[1]} ({at_end[0]}) ends, {at_start[1]} ({at_start[0]}) starts"})
            continue
        rows.append({"start": start, "end": end, "duration_min": dur, "class": "true_dark",
                     "evidence": "no data on either logger path; not a file boundary or midnight cut"})
    # Gaps visible in one path that the merged frame covers: export artifacts of that path.
    merged_ts = set(merged[ts_col])
    for f in single_frames:
        if len(f) < 2:
            continue
        for _, g in find_gaps(f[ts_col], threshold).iterrows():
            inside = merged[(merged[ts_col] > g["start"]) & (merged[ts_col] < g["end"])]
            if len(inside):
                other = ", ".join(sorted(set(inside["_source"]) - {f["_source"].iloc[0]})) or "other file"
                rows.append({"start": g["start"], "end": g["end"], "duration_min": g["duration_min"], "class": "export_artifact",
                             "evidence": f"{f['_source'].iloc[0]} gap covered by {other} ({len(inside)} rows)"})
    out = pd.DataFrame(rows, columns=["start", "end", "duration_min", "class", "evidence"])
    if len(out):
        out = out.drop_duplicates(["start", "end", "class"]).sort_values("start").reset_index(drop=True)
    _ = merged_ts  # retained for future per-timestamp coverage checks
    return out


# --------------------------------------------------------------------------- #
# 4. Metrics
# --------------------------------------------------------------------------- #
def detect_refills(df: pd.DataFrame, *, ts_col: str = "timestamp", vol_col: str = "volume_l", step_l: float = 0.5,
                   collapse_min: float = 30.0) -> list[pd.Timestamp]:
    """Timestamps where volume steps up by more than step_l between consecutive samples (refills)."""
    v = df[vol_col].astype(float)
    dv = v.diff()
    hits = list(df.loc[dv > step_l, ts_col])
    events: list[pd.Timestamp] = []
    for t in hits:
        if not events or (t - events[-1]) > timedelta(minutes=collapse_min):
            events.append(pd.Timestamp(t))
    return events


def drawdown_regression(df: pd.DataFrame, *, ts_col: str = "timestamp", vol_col: str = "volume_l",
                        refills: list | None = None, min_points: int = 20, min_volume_l: float | None = None,
                        tail_n: int = 10) -> dict:
    """OLS of reservoir volume on time (days) since the last refill: L/day, R², runway days, tier.

    Runway = (current volume - minimum safe volume) / loss per day. Tier per tier-rules.md:
    runway < 90 days RED (R9); falling but >= 90 days AMBER (A1); not falling GREEN (G).
    """
    refills = refills if refills is not None else detect_refills(df, ts_col=ts_col, vol_col=vol_col)
    seg = df[[ts_col, vol_col]].dropna().sort_values(ts_col)
    if refills:
        seg = seg[seg[ts_col] > max(refills)]
    if len(seg) < min_points:
        return {"n": int(len(seg)), "fit_start": None, "slope_l_per_day": None, "r2": None, "runway_days": None,
                "tier": "GREY (no data)", "note": f"fewer than {min_points} points after the last refill"}
    t0 = seg[ts_col].iloc[0]
    x = ((seg[ts_col] - t0).dt.total_seconds() / 86400.0).to_numpy()
    y = seg[vol_col].astype(float).to_numpy()
    slope, intercept = np.polyfit(x, y, 1)
    pred = slope * x + intercept
    ss_res = float(((y - pred) ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    current = float(np.median(y[-tail_n:]))
    floor = float(min_volume_l) if min_volume_l is not None else 0.0
    loss = -slope if slope < 0 else 0.0
    runway = (current - floor) / loss if loss > 0 else float("inf")
    if loss > 0 and runway < 90:
        tier = "RED (R9)"
    elif loss > 0:
        tier = "AMBER (A1)"
    else:
        tier = "GREEN (G)"
    return {"n": int(len(seg)), "fit_start": str(t0), "fit_end": str(seg[ts_col].iloc[-1]), "span_days": round(float(x[-1]), 2),
            "slope_l_per_day": round(float(slope), 4), "intercept_l": round(float(intercept), 4), "r2": round(r2, 3),
            "loss_l_per_day": round(loss, 4), "current_volume_l": round(current, 3), "min_volume_l": floor,
            "runway_days": None if runway == float("inf") else round(runway, 1), "tier": tier,
            "refills": [str(r) for r in refills], "note": "" if min_volume_l is not None else "minimum safe volume not supplied; runway to empty"}


def uptime_minutes(df: pd.DataFrame, *, ts_col: str = "timestamp", window: tuple | None = None) -> dict:
    """Uptime as minutes with at least one sample over the window (default: first to last sample)."""
    ts = pd.to_datetime(df[ts_col])
    start, end = (pd.Timestamp(window[0]), pd.Timestamp(window[1])) if window else (ts.min(), ts.max())
    minutes_with_data = int(ts[(ts >= start) & (ts <= end)].dt.floor("min").nunique())
    window_minutes = int((end - start).total_seconds() // 60) + 1
    return {"window_start": str(start), "window_end": str(end), "window_minutes": window_minutes,
            "minutes_with_data": minutes_with_data,
            "uptime_pct": round(100.0 * minutes_with_data / window_minutes, 2) if window_minutes > 0 else None}


def valve_saturation(df: pd.DataFrame, *, ts_col: str = "timestamp", valve_col: str = "valve_pct", hi: float = 95.0, lo: float = 5.0) -> dict:
    """Share of samples at or beyond the saturation bands and the longest saturated run (minutes)."""
    v = df[valve_col].astype(float)
    sat = (v >= hi) | (v <= lo)
    longest, run, run_start, best = 0.0, 0, None, None
    ts = pd.to_datetime(df[ts_col]).reset_index(drop=True)
    s = sat.reset_index(drop=True)
    for i, flag in enumerate(s):
        if flag:
            run_start = run_start if run_start is not None else ts[i]
            run = (ts[i] - run_start).total_seconds() / 60.0
            if run >= longest:
                longest, best = run, (str(run_start), str(ts[i]))
        else:
            run_start = None
    return {"samples": int(len(v)), "saturated_pct": round(100.0 * float(sat.mean()), 2) if len(v) else None,
            "high_pct": round(100.0 * float((v >= hi).mean()), 2) if len(v) else None,
            "low_pct": round(100.0 * float((v <= lo).mean()), 2) if len(v) else None,
            "longest_saturated_min": round(longest, 1), "longest_window": best,
            "watch": bool(longest >= 60) or bool(len(v) and float(sat.mean()) >= 0.10)}


def zero_flow_events(df: pd.DataFrame, *, ts_col: str = "timestamp", flow_col: str = "flow_lpm", tol: float = 0.05) -> dict:
    """Zero-flow readings (tool-down signature, RED (R9) when confirmed on a live circuit)."""
    f = df[flow_col].astype(float)
    z = f <= tol
    return {"zero_flow_samples": int(z.sum()), "first": str(df.loc[z, ts_col].min()) if z.any() else None,
            "last": str(df.loc[z, ts_col].max()) if z.any() else None, "tier": "RED (R9) candidate" if z.any() else "GREEN (G)"}


def compute_metrics(merged: pd.DataFrame, rig: str, dark: pd.DataFrame, *, ts_col: str, vol_col: str | None,
                    flow_col: str | None, valve_col: str | None, min_volume_l: float | None) -> dict:
    m: dict = {"rig": rig, **RIGS.get(rig, {}), "rows": int(len(merged)), "cadence_s": infer_cadence(merged[ts_col]),
               "uptime": uptime_minutes(merged, ts_col=ts_col)}
    if len(dark):
        by = dark.groupby("class")["duration_min"].agg(["count", "sum"])
        m["dark_windows"] = {k: {"count": int(v["count"]), "hours": round(float(v["sum"]) / 60.0, 2)} for k, v in by.iterrows()}
        td = dark[dark["class"] == "true_dark"]
        m["true_dark_days"] = round(float(td["duration_min"].sum()) / 1440.0, 2) if len(td) else 0.0
    else:
        m["dark_windows"], m["true_dark_days"] = {}, 0.0
    if vol_col and vol_col in merged.columns:
        m["drawdown"] = drawdown_regression(merged, ts_col=ts_col, vol_col=vol_col, min_volume_l=min_volume_l)
    if flow_col and flow_col in merged.columns:
        m["zero_flow"] = zero_flow_events(merged, ts_col=ts_col, flow_col=flow_col)
        m["flow_mean_lpm"] = round(float(merged[flow_col].astype(float).mean()), 3)
    if valve_col and valve_col in merged.columns:
        m["valve"] = valve_saturation(merged, ts_col=ts_col, valve_col=valve_col)
    return m


# --------------------------------------------------------------------------- #
# 5. Outputs
# --------------------------------------------------------------------------- #
def deliverable_names(rig: str, as_of: datetime) -> dict:
    stem = f"CSL-{PROGRAM}-CTRW-{rig}-{as_of.strftime('%y%m%d')}"
    return {"stem": stem, "xlsx": f"{stem}.xlsx", "pdf": f"{stem}.pdf"}


def workbook_spec(metrics: dict, cols: dict) -> dict:
    """Formula layout for the per-rig xlsx (rendered by the report factory with openpyxl per csl-brand Section 5).

    Data rows stay raw; the Metrics sheet computes slope, R², runway, uptime with live formulas so
    a reviewer can audit the arithmetic in the workbook itself.
    """
    n = metrics.get("drawdown", {}).get("n") or 0
    return {
        "sheets": [
            {"name": "Control", "rows": ["document number", "rig / logger / channels", "sources and file md5s",
                                          "window", "pull timestamp (ET)", "column dictionary", "change log"]},
            {"name": "Data", "columns": [cols["ts"], cols.get("vol"), cols.get("flow"), cols.get("valve"), "_source", "_file", "days_since_fit_start"]},
            {"name": "DarkWindows", "columns": ["start", "end", "duration_min", "class", "evidence"]},
            {"name": "Metrics", "formulas": {
                "slope_l_per_day": f"=SLOPE(Data!B2:B{n + 1},Data!G2:G{n + 1})",
                "r_squared": f"=RSQ(Data!B2:B{n + 1},Data!G2:G{n + 1})",
                "current_volume_l": f"=MEDIAN(OFFSET(Data!B{n + 1},-9,0,10,1))",
                "runway_days": "=(current_volume_l-min_volume_l)/-slope_l_per_day",
                "uptime_pct": "=minutes_with_data/window_minutes",
            }},
        ],
        "tier_rules": "runway < 90 days RED (R9); falling >= 90 AMBER (A1); zero flow RED (R9)",
    }


def summary_markdown(metrics: dict, dark: pd.DataFrame, names: dict, sources: dict) -> str:
    dd = metrics.get("drawdown", {})
    up = metrics.get("uptime", {})
    checks = [c for c in metrics.get("channel_checks", []) if c]
    channel_txt = ", ".join("{}/{}{}".format(c["expected"], c["found"], "" if c["ok"] else " SHORT") for c in checks) or "n/a"
    resend_n = sum(1 for r in metrics.get("resends", []) if r["class"] == "byte_identical_resend")
    lines = [f"# {names['stem']} telemetry summary (skeleton output)", ""]
    tier = dd.get("tier", "GREY (no data)")
    if dd.get("loss_l_per_day"):
        lines.append(f"**Bottom line.** {metrics['rig']} reservoir losing {dd['loss_l_per_day']:.3f} L/day (R² {dd['r2']}, n {dd['n']}); "
                     f"runway {dd['runway_days']} days to {dd['min_volume_l']} L, {tier}. Uptime {up.get('uptime_pct')}% of window minutes; "
                     f"true dark {metrics.get('true_dark_days', 0)} days.")
    else:
        lines.append(f"**Bottom line.** {metrics['rig']}: no measurable drawdown in the window, {tier}. Uptime {up.get('uptime_pct')}%.")
    lines += ["", "| Metric | Value |", "|---|---|",
              f"| Rig / logger / channels | {metrics['rig']} / {metrics.get('logger')} / {metrics.get('channels')} |",
              f"| Window | {up.get('window_start')} to {up.get('window_end')} |",
              f"| Cadence (s: share) | {metrics.get('cadence_s')} |",
              f"| Minutes with data / window minutes | {up.get('minutes_with_data')} / {up.get('window_minutes')} ({up.get('uptime_pct')}%) |",
              f"| Dark windows by class | {metrics.get('dark_windows')} |",
              f"| Drawdown | {dd.get('slope_l_per_day')} L/day, R² {dd.get('r2')}, runway {dd.get('runway_days')} days, {tier} |",
              f"| Refills detected | {len(dd.get('refills', []))} |",
              f"| Zero-flow samples | {metrics.get('zero_flow', {}).get('zero_flow_samples')} ({metrics.get('zero_flow', {}).get('tier')}) |",
              f"| Valve saturation | {metrics.get('valve', {}).get('saturated_pct')}% of samples; longest run {metrics.get('valve', {}).get('longest_saturated_min')} min |",
              f"| Channel check (expected / found per file) | {channel_txt} |",
              f"| Files flagged byte-identical re-send | {resend_n} of {len(metrics.get('resends', []))} |",
              "", "| Source path | Rows | Start | End |", "|---|---|---|---|"]
    for s, v in sources.items():
        lines.append(f"| {s} | {v['rows']} | {v['start']} | {v['end']} |")
    if len(dark):
        lines += ["", "| Dark window start | End | Minutes | Class | Evidence |", "|---|---|---|---|---|"]
        for _, r in dark.iterrows():
            lines.append(f"| {r['start']} | {r['end']} | {r['duration_min']} | {r['class']} | {r['evidence']} |")
    lines += ["", f"Deliverables: {names['xlsx']} (formula-driven) and {names['pdf']} (branded, report factory). Generated {fmt_et(now_et())}."]
    return "\n".join(lines) + "\n"


def run_pipeline(files_by_source: dict[str, list[str]], rig: str, cols: dict, out_dir: Path, as_of: datetime,
                 min_volume_l: float | None, registry: str | None = None) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    all_files = [f for fs in files_by_source.values() for f in fs]
    resends = detect_resends(all_files, registry)
    frames = []
    for source, fs in files_by_source.items():
        for f in fs:
            if resends.loc[resends["file"] == Path(f).name, "class"].eq("byte_identical_resend").any():
                continue
            frames.append(parse_log(f, rig, ts_col=cols["ts"], source=source))
    spans = file_spans(frames, cols["ts"])
    merged, merge_report = merge_paths(frames, cols["ts"])
    dark = classify_dark_windows(merged, spans, frames, ts_col=cols["ts"])
    metrics = compute_metrics(merged, rig, dark, ts_col=cols["ts"], vol_col=cols.get("vol"), flow_col=cols.get("flow"),
                              valve_col=cols.get("valve"), min_volume_l=min_volume_l)
    metrics["merge"] = merge_report
    metrics["channel_checks"] = [f.attrs.get("channel_check") for f in frames]
    metrics["resends"] = resends.to_dict(orient="records")
    names = deliverable_names(rig, as_of)
    merged.to_csv(out_dir / f"{names['stem']}_merged.csv", index=False, lineterminator="\n")
    dark.to_csv(out_dir / f"{names['stem']}_dark-windows.csv", index=False, lineterminator="\n")
    (out_dir / f"{names['stem']}_metrics.json").write_text(json.dumps(metrics, indent=2, default=str), encoding="utf-8")
    (out_dir / f"{names['stem']}_workbook-spec.json").write_text(json.dumps(workbook_spec(metrics, cols), indent=2), encoding="utf-8")
    md = summary_markdown(metrics, dark, names, merge_report.get("sources", {}))
    (out_dir / f"{names['stem']}_summary.md").write_text(md, encoding="utf-8")
    print(md)
    print(f"written to {out_dir}: merged csv, dark-windows csv, metrics json, workbook spec, summary md")
    return metrics


# --------------------------------------------------------------------------- #
# Demo data
# --------------------------------------------------------------------------- #
def make_demo_data(out_dir: Path) -> dict[str, list[str]]:
    """Two weeks of synthetic TR7-like data across both paths with every dark-window class present."""
    rng = np.random.default_rng(11)
    out_dir.mkdir(parents=True, exist_ok=True)
    t0 = pd.Timestamp("2026-08-13 00:00:00")

    def series(start: pd.Timestamp, end: pd.Timestamp, cadence_s: int) -> pd.DataFrame:
        ts = pd.date_range(start, end, freq=f"{cadence_s}s")
        days = (ts - t0).total_seconds() / 86400.0
        vol = 18.0 - 0.14 * days + rng.normal(0, 0.02, len(ts))
        vol = np.where(days >= 9.0, vol + 2.0, vol)  # refill on day 9
        flow = 4.2 + rng.normal(0, 0.04, len(ts))
        valve = np.clip(65 + rng.normal(0, 2.0, len(ts)), 40, 100)
        df = pd.DataFrame({"timestamp": ts, "volume_l": vol.round(3), "flow_lpm": flow.round(3), "valve_pct": valve.round(1)})
        return df

    files: dict[str, list[str]] = {"ct_share": [], "disk3": []}
    # ct_share file 1: day 0 to day 3 12:00 (30 s cadence)
    a = series(t0, t0 + pd.Timedelta(days=3, hours=12), 30)
    # ct_share file 2: starts 20 minutes later (export artifact at the file boundary), 60 s cadence, to end of day 6
    b = series(t0 + pd.Timedelta(days=3, hours=12, minutes=20), t0 + pd.Timedelta(days=6, hours=23, minutes=59), 60)
    # disk3 file 1: day 7 00:00 to day 13, 30 s cadence, with a 4-hour true dark on day 10 and a 12-minute midnight cut day 11->12
    c = series(t0 + pd.Timedelta(days=7), t0 + pd.Timedelta(days=13, hours=23, minutes=59), 30)
    dark_start, dark_end = t0 + pd.Timedelta(days=10, hours=9), t0 + pd.Timedelta(days=10, hours=13)
    c = c[~((c["timestamp"] > dark_start) & (c["timestamp"] < dark_end))]
    mid_s, mid_e = t0 + pd.Timedelta(days=11, hours=23, minutes=55), t0 + pd.Timedelta(days=12, hours=0, minutes=7)
    c = c[~((c["timestamp"] > mid_s) & (c["timestamp"] < mid_e))]
    # valve saturated for 3 hours on day 12
    sat = (c["timestamp"] >= t0 + pd.Timedelta(days=12, hours=14)) & (c["timestamp"] < t0 + pd.Timedelta(days=12, hours=17))
    c.loc[sat, "valve_pct"] = 100.0
    for name, df, src in (("TR7_m4535_ct_0813.csv", a, "ct_share"), ("TR7_m4535_ct_0816.csv", b, "ct_share"),
                          ("TR7_m4535_disk3_0820.csv", c, "disk3")):
        p = out_dir / name
        df.to_csv(p, index=False, lineterminator="\n")
        files[src].append(str(p))
    # a byte-identical re-send of the first file
    dup = out_dir / "TR7_m4535_ct_0813_RESEND.csv"
    dup.write_bytes((out_dir / "TR7_m4535_ct_0813.csv").read_bytes())
    files["ct_share"].append(str(dup))
    return files


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--rig", default="TR7", choices=sorted(RIGS), help="rig code")
    p.add_argument("--from-csv", action="append", default=[], metavar="LABEL=PATH",
                   help="logger file as label=path (labels ct_share / disk3); repeat per file")
    p.add_argument("--ts-col", default="timestamp")
    p.add_argument("--volume-col", default="volume_l")
    p.add_argument("--flow-col", default="flow_lpm")
    p.add_argument("--valve-col", default="valve_pct")
    p.add_argument("--min-volume", type=float, help="minimum safe reservoir volume (L) for the runway")
    p.add_argument("--as-of", help="YYYY-MM-DD for the document number; default today")
    p.add_argument("--out-dir", default="ctrw_out")
    p.add_argument("--resend-registry", help="JSON registry of processed file md5s")
    p.add_argument("--demo", action="store_true", help="generate synthetic dual-path data and run the pipeline on it")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    out_dir = Path(args.out_dir)
    as_of = datetime.fromisoformat(args.as_of) if args.as_of else now_et().replace(tzinfo=None)
    cols = {"ts": args.ts_col, "vol": args.volume_col, "flow": args.flow_col, "valve": args.valve_col}
    if args.demo:
        files = make_demo_data(out_dir / "demo_data")
        print(f"DEMO synthetic data: {sum(len(v) for v in files.values())} files under {out_dir / 'demo_data'}")
        run_pipeline(files, args.rig, cols, out_dir, as_of, args.min_volume if args.min_volume is not None else 6.0,
                     registry=str(out_dir / "demo_registry.json"))
        return 0
    if not args.from_csv:
        build_parser().print_help()
        return 2
    files: dict[str, list[str]] = {}
    for item in args.from_csv:
        label, _, path = item.rpartition("=")
        label = label or "ct_share"
        files.setdefault(label, []).append(path)
    run_pipeline(files, args.rig, cols, out_dir, as_of, args.min_volume, args.resend_registry)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

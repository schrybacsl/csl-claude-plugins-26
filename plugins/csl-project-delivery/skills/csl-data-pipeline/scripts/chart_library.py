#!/usr/bin/env python3
"""
chart_library.py — the standard CSL report figures, rendered with the brand tokens
(csl-data-pipeline SKILL.md Section 3.9; colors and rules from csl-brand Sections 1 and 6;
form and interaction rules from the dataviz skill).

Every function takes a tidy DataFrame with the columns named in its docstring (the data
contract), a finding-style title ("Mitigation past-target rows rose to 17 with no
closures", never "Past-target trend"), and a source string that is stamped under the
figure ("ST CHW/PCW System Mitigation Plan (ID 2158727850315652) pulled 09/18/26 06:41 ET").
Series colors follow the fixed brand order navy, dark teal, teal, olive; tier-coded marks
use the package status colors, never CSL Red; every tier color is paired with its word.
One axis per panel: measures in different units get stacked panels, not a twin axis.

Figures
  fig_permit_gates_weekly          permit gates cleared in time vs permits started, per week
  fig_mitigation_open_past_target  open vs past-target rows over weeks, closures as bars
  fig_closures_per_week            closures per week
  fig_health_distribution          roadmap health distribution (Green / Yellow / Active / Pending)
  fig_rpn_watchlist                RPN watchlist bars, >= 700 highlighted, threshold hairline
  fig_frozen_weeks                 frozen-weeks indicator strip from the freeze chain
  fig_csl_board_reds_anchors       CSL board: Reds and anchors closed per week
  fig_forecast_vs_budget_egrp      forecast vs budget by E-GRP with variance % and tier marks
  fig_quarterly_cash_flow          quarterly cash flow vs plan with cumulative lines
  fig_rig_timeseries               rig flow and valve position, stacked panels, dark windows shaded
  fig_reservoir_drawdown           reservoir volume with regression line, refills, runway annotation

Usage
  from chart_library import fig_rpn_watchlist, save_figure
  fig = fig_rpn_watchlist(df, title="Six rows sit at or above RPN 700; two have no dated mitigation",
                          source="W77 Roadmap Master (ID 1059284113641348) pulled 09/18/26 06:40 ET")
  save_figure(fig, "WKR-38C_fig02_rpn-watchlist.png")

  python3 chart_library.py --demo --out-dir /tmp/chart_demo      # renders every figure from synthetic data, labeled DEMO
  python3 chart_library.py --list                                # prints the data contracts
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

# --------------------------------------------------------------------------- #
# Brand tokens: import from skills/csl-brand/assets; fall back to the same values
# so the module still imports when copied out of the package. Keep in sync.
# --------------------------------------------------------------------------- #
HERE = Path(__file__).resolve().parent
_candidates = []
if os.environ.get("CSL_BRAND_ASSETS"):
    _candidates.append(Path(os.environ["CSL_BRAND_ASSETS"]))
_candidates.append(HERE.parents[1] / "csl-brand" / "assets")  # flat package layout
# Plugin layout: plugins/csl-project-delivery/skills/csl-data-pipeline/scripts -> plugins/csl-core/skills/csl-brand/assets
_candidates.append(HERE.parents[3] / "csl-core" / "skills" / "csl-brand" / "assets")
# Claude environments mount plugin skills under /mnt/skills; search there last.
for _root in (Path("/mnt/skills"),):
    if _root.exists():
        _candidates.extend(sorted(_root.glob("**/csl-brand/assets")))
for _c in _candidates:
    if (_c / "brand_tokens.py").exists():
        sys.path.insert(0, str(_c))
        break
try:
    from brand_tokens import CHART_SERIES, CSL, TIER, add_source_note, apply_matplotlib_style  # type: ignore
    BRAND_SOURCE = "brand_tokens.py"
except ImportError:  # pragma: no cover - fallback mirrors csl-brand SKILL.md Section 1
    BRAND_SOURCE = "fallback constants (brand_tokens.py not found)"

    class _P:  # minimal stand-in for brand_tokens.CSL
        red, black, white = "#BF311A", "#000000", "#FFFFFF"
        navy, teal_dark, teal, olive = "#0A3173", "#056873", "#1AA8BF", "#BFAD2E"
        ink, slate, grey, mist, paper = "#1F2933", "#52606D", "#9AA5B1", "#E4E7EB", "#F5F7FA"

    CSL = _P()
    TIER = {"RED": {"fill": "#C62828", "text": "#FFFFFF"}, "AMBER": {"fill": "#E09B1A", "text": "#1F2933"},
            "GREEN": {"fill": "#2E7D32", "text": "#FFFFFF"}, "BLUE": {"fill": "#0A3173", "text": "#FFFFFF"},
            "GREY": {"fill": "#9AA5B1", "text": "#1F2933"}}
    CHART_SERIES = ["#0A3173", "#056873", "#1AA8BF", "#BFAD2E", "#6C83AB", "#69A4AB", "#76CBD9", "#D9CE82"]

    def apply_matplotlib_style(font=None):
        from cycler import cycler
        matplotlib.rcParams.update({"axes.prop_cycle": cycler(color=CHART_SERIES), "axes.spines.top": False,
                                    "axes.spines.right": False, "axes.grid": True, "axes.grid.axis": "y",
                                    "grid.color": CSL.mist, "axes.edgecolor": CSL.grey, "axes.titlelocation": "left",
                                    "axes.titleweight": "bold", "savefig.dpi": 200, "savefig.bbox": "tight"})

    def add_source_note(fig, text):
        fig.text(0.01, -0.02, text, ha="left", va="top", fontsize=7, color=CSL.slate)

_STYLED = False
HEALTH_TIER = {"green": "GREEN", "yellow": "AMBER", "amber": "AMBER", "red": "RED", "active": "BLUE",
               "blue": "BLUE", "pending": "GREY", "grey": "GREY", "gray": "GREY", "not started": "BLUE"}


def _style() -> None:
    global _STYLED
    if not _STYLED:
        apply_matplotlib_style()
        _STYLED = True


def _finish(fig, title: str, source: str, demo: bool = False) -> None:
    """Title as the finding, source line stamped, DEMO watermark when synthetic."""
    if not getattr(fig, "_csl_top_reserved", False):
        fig.subplots_adjust(top=1 - 0.40 / fig.get_figheight())
    fig.suptitle(title, x=0.01, y=0.995, ha="left", va="top", fontsize=11, fontweight="bold", color=CSL.ink)
    add_source_note(fig, f"Source: {source}")
    if demo:
        fig.text(0.5, 0.5, "DEMO — synthetic data", ha="center", va="center", fontsize=28,
                 color=CSL.grey, alpha=0.25, rotation=20, transform=fig.transFigure)


def save_figure(fig, path: str | Path, dpi: int = 200) -> Path:
    """Save at 2x for PDF embedding (PNG) or as SVG for HTML, then close the figure."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(p, dpi=dpi, bbox_inches="tight", facecolor=CSL.white)
    plt.close(fig)
    return p


def _bar_labels(ax, bars, fmt="{:g}", max_bars: int = 8, orient: str = "v") -> None:
    """Data labels on bars when there are eight or fewer (csl-brand Section 6); zero bars stay unlabeled."""
    if len(bars) <= max_bars:
        vals = [b.get_height() if orient == "v" else b.get_width() for b in bars]
        ax.bar_label(bars, labels=[fmt.format(v) if v else "" for v in vals], padding=2, fontsize=7, color=CSL.ink)


def _legend_top(ax, ncol: int = 3) -> None:
    """Legend in one row above the plot area, under the finding title, so it never covers a mark."""
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=ncol, frameon=False, fontsize=7.5,
              handlelength=1.6, columnspacing=1.2, borderaxespad=0.2)
    fig = ax.figure
    fig.subplots_adjust(top=1 - 0.62 / fig.get_figheight())  # room for title + legend row in inches
    fig._csl_top_reserved = True


def _money(v: float) -> str:
    sign, a = ("-" if v < 0 else ""), abs(v)
    if a >= 1e6:
        return f"{sign}${a / 1e6:,.1f}M"
    if a >= 1e3:
        return f"{sign}${a / 1e3:,.0f}K"
    return f"{sign}${a:,.0f}"


# --------------------------------------------------------------------------- #
# Figures
# --------------------------------------------------------------------------- #
def fig_permit_gates_weekly(df: pd.DataFrame, *, title: str, source: str, demo: bool = False):
    """Contract: week (label), started (int), gated_in_time (int). Perfect weeks are marked in words."""
    _style()
    fig, ax = plt.subplots(figsize=(7.0, 3.2))
    x = np.arange(len(df))
    w = 0.38
    b1 = ax.bar(x - w / 2, df["started"], w, color=CSL.navy, label="Permits started")
    b2 = ax.bar(x + w / 2, df["gated_in_time"], w, color=CSL.teal_dark, label="Gated in time before start")
    _bar_labels(ax, b1)
    _bar_labels(ax, b2)
    for i, (s, g) in enumerate(zip(df["started"], df["gated_in_time"])):
        if s > 0 and g == s:
            ax.text(i, max(s, g) + 0.6, "perfect week", ha="center", fontsize=6.5, color=CSL.slate, style="italic")
    ax.set_xticks(x, df["week"].astype(str), fontsize=8)
    ax.set_ylabel("Permits")
    ax.set_ylim(0, max(1, float(df[["started", "gated_in_time"]].to_numpy().max()) * 1.35))
    _legend_top(ax, 2)
    _finish(fig, title, source, demo)
    return fig


def fig_mitigation_open_past_target(df: pd.DataFrame, *, title: str, source: str, demo: bool = False):
    """Contract: week (label), open (int), past_target (int), closures (int). One axis: rows."""
    _style()
    fig, ax = plt.subplots(figsize=(7.0, 3.2))
    x = np.arange(len(df))
    bars = ax.bar(x, df["closures"], 0.5, color=CHART_SERIES[6], label="Closures in week")
    _bar_labels(ax, bars)
    ax.plot(x, df["open"], marker="o", ms=4, lw=2, color=CSL.navy, label="Open rows")
    ax.plot(x, df["past_target"], marker="o", ms=4, lw=2, color=CSL.teal_dark, label="Past-target rows")
    ax.annotate(f"{int(df['past_target'].iloc[-1])} past target", (x[-1], df["past_target"].iloc[-1]),
                textcoords="offset points", xytext=(6, 0), fontsize=7.5, color=CSL.teal_dark, va="center")
    ax.set_xticks(x, df["week"].astype(str), fontsize=8)
    ax.set_ylabel("Rows")
    _legend_top(ax, 3)
    _finish(fig, title, source, demo)
    return fig


def fig_closures_per_week(df: pd.DataFrame, *, title: str, source: str, demo: bool = False):
    """Contract: week (label), closures (int)."""
    _style()
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    bars = ax.bar(np.arange(len(df)), df["closures"], 0.55, color=CSL.navy)
    _bar_labels(ax, bars)
    ax.set_xticks(np.arange(len(df)), df["week"].astype(str), fontsize=8)
    ax.set_ylabel("Rows closed")
    _finish(fig, title, source, demo)
    return fig


def fig_health_distribution(counts: dict | pd.Series, *, title: str, source: str, demo: bool = False):
    """Contract: mapping health label -> count (Green, Yellow, Active, Pending, ...). Tier colors with the word."""
    _style()
    s = pd.Series(counts).astype(float)
    total = float(s.sum()) or 1.0
    fig, ax = plt.subplots(figsize=(6.5, 0.6 + 0.45 * len(s)))
    colors = [TIER[HEALTH_TIER.get(str(k).strip().lower(), "GREY")]["fill"] for k in s.index]
    y = np.arange(len(s))[::-1]
    bars = ax.barh(y, s.values, color=colors, height=0.6)
    for yi, (k, v) in zip(y, s.items()):
        ax.text(v + total * 0.01, yi, f"{k}: {int(v)} ({v / total:.0%})", va="center", fontsize=8, color=CSL.ink)
    ax.set_yticks(y, [str(k) for k in s.index], fontsize=8)
    ax.set_xlim(0, s.max() * 1.45)
    ax.grid(False, axis="y")
    ax.grid(True, axis="x")
    ax.set_xlabel(f"Rows (n = {int(total)})")
    _finish(fig, title, source, demo)
    return fig


def fig_rpn_watchlist(df: pd.DataFrame, *, title: str, source: str, threshold: int = 700, top: int = 12, demo: bool = False):
    """Contract: item (str), rpn (number), optional mitigation (bool: active dated mitigation on the row).
    Bars >= threshold in the RED status color with the word; rows without mitigation flagged (R1)."""
    _style()
    d = df.sort_values("rpn", ascending=False).head(top).copy()
    fig, ax = plt.subplots(figsize=(7.0, 0.8 + 0.38 * len(d)))
    y = np.arange(len(d))[::-1]
    colors = [TIER["RED"]["fill"] if r >= threshold else CSL.navy for r in d["rpn"]]
    ax.barh(y, d["rpn"], color=colors, height=0.62)
    ax.axvline(threshold, color=CSL.slate, lw=0.8, ls="--")
    ax.text(threshold, len(d) - 0.3, f"critical threshold {threshold}", fontsize=7, color=CSL.slate, ha="center")
    for yi, (_, r) in zip(y, d.iterrows()):
        tag = ""
        if r["rpn"] >= threshold:
            tag = "  RED, no mitigation (R1)" if ("mitigation" in d.columns and not bool(r["mitigation"])) else "  RED band"
        ax.text(r["rpn"] + 8, yi, f"{int(r['rpn'])}{tag}", va="center", fontsize=7.5, color=CSL.ink)
    ax.set_yticks(y, d["item"].astype(str), fontsize=8)
    ax.set_xlim(0, 1000 * 1.25)
    ax.grid(False, axis="y")
    ax.grid(True, axis="x")
    ax.set_xlabel("RPN C (SEV x Occ x Det)")
    _finish(fig, title, source, demo)
    return fig


def fig_frozen_weeks(pulls: list[dict], *, title: str, source: str, demo: bool = False):
    """Contract: list of {date: str, identical: bool} in chronological order (freeze_check chain).
    Identical pulls draw as grey '=' squares, changed pulls as navy; the streak is written in words."""
    _style()
    n = len(pulls)
    fig, ax = plt.subplots(figsize=(max(4.0, 0.7 * n + 1.5), 1.6))
    streak = 0
    for p in reversed(pulls):
        if p.get("identical"):
            streak += 1
        else:
            break
    for i, p in enumerate(pulls):
        ident = bool(p.get("identical"))
        ax.add_patch(plt.Rectangle((i, 0), 0.9, 0.9, facecolor=CSL.mist if ident else CSL.navy,
                                   edgecolor=CSL.grey if ident else CSL.navy))
        ax.text(i + 0.45, 0.45, "=" if ident else "Δ", ha="center", va="center", fontsize=10,
                color=CSL.slate if ident else CSL.white, fontweight="bold")
        ax.text(i + 0.45, -0.25, str(p.get("date", "")), ha="center", va="top", fontsize=6.5, color=CSL.slate, rotation=0)
    ax.set_xlim(-0.2, n + 0.2)
    ax.set_ylim(-0.9, 1.4)
    ax.axis("off")
    word = "no frozen pulls" if streak == 0 else f"{streak} consecutive identical pull(s) through {pulls[-1].get('date', '')}"
    ax.text(0, 1.15, word, fontsize=8, color=CSL.ink)
    _finish(fig, title, source, demo)
    return fig


def fig_csl_board_reds_anchors(df: pd.DataFrame, *, title: str, source: str, demo: bool = False):
    """Contract: week (label), reds (int), anchors_closed (int). Reds use the RED status color with the word."""
    _style()
    fig, ax = plt.subplots(figsize=(7.0, 3.0))
    x = np.arange(len(df))
    w = 0.38
    b1 = ax.bar(x - w / 2, df["reds"], w, color=TIER["RED"]["fill"], label="RED items on the board")
    b2 = ax.bar(x + w / 2, df["anchors_closed"], w, color=CSL.navy, label="Anchor rows closed")
    _bar_labels(ax, b1)
    _bar_labels(ax, b2)
    ax.set_xticks(x, df["week"].astype(str), fontsize=8)
    ax.set_ylabel("Rows")
    _legend_top(ax, 2)
    _finish(fig, title, source, demo)
    return fig


def fig_forecast_vs_budget_egrp(df: pd.DataFrame, *, title: str, source: str, demo: bool = False, top: int = 12):
    """Contract: egrp (str), budget (number), forecast (number). Variance % annotated; >10% marked R2, 5-10% A2."""
    _style()
    d = df.copy()
    d["var_pct"] = np.where(d["budget"] > 0, (d["forecast"] - d["budget"]) / d["budget"] * 100.0, np.nan)
    d = d.reindex(d["var_pct"].abs().sort_values(ascending=False).index).head(top)
    fig, ax = plt.subplots(figsize=(7.2, 0.9 + 0.42 * len(d)))
    y = np.arange(len(d))[::-1]
    h = 0.36
    ax.barh(y + h / 2, d["budget"], h, color=CSL.navy, label="Budget")
    ax.barh(y - h / 2, d["forecast"], h, color=CSL.teal_dark, label="Forecast")
    xmax = float(d[["budget", "forecast"]].to_numpy().max()) if len(d) else 1.0
    for yi, (_, r) in zip(y, d.iterrows()):
        v = r["var_pct"]
        if pd.isna(v):
            note = "no budget"
        else:
            rule = "RED (R2)" if abs(v) > 10 else ("AMBER (A2)" if abs(v) >= 5 else "GREEN (G)")
            note = f"{v:+.1f}%  {rule}"
        ax.text(max(r["budget"], r["forecast"]) + xmax * 0.02, yi, note, va="center", fontsize=7.5, color=CSL.ink)
    ax.set_yticks(y, d["egrp"].astype(str), fontsize=8)
    ax.set_xlim(0, xmax * 1.45)
    ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: _money(v)))
    ax.grid(False, axis="y")
    ax.grid(True, axis="x")
    _legend_top(ax, 2)
    _finish(fig, title, source, demo)
    return fig


def fig_quarterly_cash_flow(df: pd.DataFrame, *, title: str, source: str, demo: bool = False):
    """Contract: quarter (label), plan (number), actual (number, NaN for future quarters). Cumulative lines share the dollar axis."""
    _style()
    fig, ax = plt.subplots(figsize=(7.0, 3.4))
    x = np.arange(len(df))
    w = 0.38
    ax.bar(x - w / 2, df["plan"], w, color=CHART_SERIES[4], label="Plan (quarter)")
    ax.bar(x + w / 2, df["actual"].fillna(0), w, color=CSL.navy, label="Actual (quarter)")
    ax.plot(x, df["plan"].cumsum(), color=CSL.teal_dark, lw=2, ls="--", marker="o", ms=3, label="Plan cumulative")
    act_cum = df["actual"].cumsum()
    ax.plot(x, act_cum, color=CSL.teal, lw=2, marker="o", ms=3, label="Actual cumulative")
    last = act_cum.last_valid_index()
    if last is not None:
        gap = act_cum.loc[last] - df["plan"].cumsum().loc[last]
        ax.annotate(f"{_money(gap)} vs plan to date", (x[list(df.index).index(last)], act_cum.loc[last]),
                    textcoords="offset points", xytext=(6, 6), fontsize=7.5, color=CSL.ink)
    ax.set_xticks(x, df["quarter"].astype(str), fontsize=8)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: _money(v)))
    _legend_top(ax, 4)
    _finish(fig, title, source, demo)
    return fig


def fig_rig_timeseries(df: pd.DataFrame, *, title: str, source: str, ts_col: str = "timestamp", flow_col: str = "flow_lpm",
                       valve_col: str = "valve_pct", dark_windows: list[dict] | None = None, sat_hi: float = 95.0,
                       demo: bool = False):
    """Contract: ts_col (datetime), flow_col (L/min), valve_col (%); dark_windows = [{start, end, class}].
    Two stacked panels (different units), shared time axis; dark windows shaded grey (true dark) or olive (artifact)."""
    _style()
    d = df.copy()
    d[ts_col] = pd.to_datetime(d[ts_col])
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.2, 4.2), sharex=True, gridspec_kw={"hspace": 0.12})
    a1.plot(d[ts_col], d[flow_col], color=CSL.navy, lw=1.0)
    a1.set_ylabel("Flow (L/min)")
    a2.plot(d[ts_col], d[valve_col], color=CSL.teal_dark, lw=1.0)
    a2.axhspan(sat_hi, 100, color=CSL.mist, alpha=0.8, lw=0)
    a2.text(d[ts_col].iloc[0], sat_hi + 0.5, f"saturation watch >= {sat_hi:g}%", fontsize=6.5, color=CSL.slate, va="bottom")
    a2.set_ylabel("Valve position (%)")
    a2.set_ylim(0, 105)
    for wnd in dark_windows or []:
        col = CSL.grey if str(wnd.get("class", "")).startswith("true") else "#F7F5E6"
        for a in (a1, a2):
            a.axvspan(pd.to_datetime(wnd["start"]), pd.to_datetime(wnd["end"]), color=col, alpha=0.5, lw=0)
        a1.text(pd.to_datetime(wnd["start"]), a1.get_ylim()[1], str(wnd.get("class", "")), fontsize=6, color=CSL.slate,
                va="bottom", ha="left", clip_on=False)
    fig.autofmt_xdate()
    _finish(fig, title, source, demo)
    return fig


def fig_reservoir_drawdown(df: pd.DataFrame, fit: dict, *, title: str, source: str, ts_col: str = "timestamp",
                           vol_col: str = "volume_l", refills: list | None = None, min_volume_l: float | None = None,
                           demo: bool = False):
    """Contract: ts_col (datetime), vol_col (liters); fit = {slope_l_per_day, intercept_l, r2, fit_start, runway_days, tier}
    from ctrw_pipeline_skeleton.drawdown_regression; refills = list of timestamps (step increases)."""
    _style()
    d = df.copy()
    d[ts_col] = pd.to_datetime(d[ts_col])
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    ax.plot(d[ts_col], d[vol_col], ".", ms=2.5, color=CSL.navy, alpha=0.6, label="Reservoir volume")
    if fit and fit.get("fit_start") is not None:
        t0 = pd.to_datetime(fit["fit_start"])
        seg = d[d[ts_col] >= t0]
        if len(seg):
            days = (seg[ts_col] - t0).dt.total_seconds() / 86400.0
            ax.plot(seg[ts_col], fit["intercept_l"] + fit["slope_l_per_day"] * days, color=CSL.teal_dark, lw=2,
                    label=f"Regression {fit['slope_l_per_day']:+.3f} L/day, R² {fit.get('r2', float('nan')):.2f}")
            rw = fit.get("runway_days")
            rw_txt = "runway not falling" if rw is None or rw == float("inf") else f"runway {rw:.0f} days"
            ax.annotate(f"{rw_txt}  {fit.get('tier', '')}", (seg[ts_col].iloc[-1], seg[vol_col].iloc[-1]),
                        textcoords="offset points", xytext=(-6, -16), ha="right", va="top", fontsize=7.5, color=CSL.ink)
    for r in refills or []:
        ax.axvline(pd.to_datetime(r), color=CSL.olive, lw=1.2, ls="-")
    if refills:
        ax.plot([], [], color=CSL.olive, lw=1.2, label="Refill (step increase)")
    if min_volume_l is not None:
        ax.axhline(min_volume_l, color=CSL.slate, lw=0.8, ls="--")
        ax.text(d[ts_col].iloc[0], min_volume_l, f" minimum safe volume {min_volume_l:g} L", fontsize=6.5, color=CSL.slate, va="bottom")
    ax.set_ylabel("Volume (L)")
    _legend_top(ax, 3)
    fig.autofmt_xdate()
    _finish(fig, title, source, demo)
    return fig


FIGURES = {
    "fig_permit_gates_weekly": fig_permit_gates_weekly,
    "fig_mitigation_open_past_target": fig_mitigation_open_past_target,
    "fig_closures_per_week": fig_closures_per_week,
    "fig_health_distribution": fig_health_distribution,
    "fig_rpn_watchlist": fig_rpn_watchlist,
    "fig_frozen_weeks": fig_frozen_weeks,
    "fig_csl_board_reds_anchors": fig_csl_board_reds_anchors,
    "fig_forecast_vs_budget_egrp": fig_forecast_vs_budget_egrp,
    "fig_quarterly_cash_flow": fig_quarterly_cash_flow,
    "fig_rig_timeseries": fig_rig_timeseries,
    "fig_reservoir_drawdown": fig_reservoir_drawdown,
}


# --------------------------------------------------------------------------- #
# Demo (synthetic data, clearly labeled)
# --------------------------------------------------------------------------- #
def render_demo(out_dir: Path) -> list[Path]:
    """Render every figure from synthetic data; titles and watermark say DEMO."""
    rng = np.random.default_rng(7)
    src = "DEMO synthetic data; no sheet pulled"
    weeks = [f"W{n}" for n in range(33, 41)]
    out: list[Path] = []

    started = rng.integers(2, 7, len(weeks))
    gated = started.copy()
    gated[:4] = np.maximum(0, started[:4] - 1)  # one late gate a week, then four perfect weeks
    fig = fig_permit_gates_weekly(pd.DataFrame({"week": weeks, "started": started, "gated_in_time": gated}),
                                  title="DEMO: Fourth consecutive perfect week; every permit gated before start", source=src, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig01_permit-gates.png"))

    mit = pd.DataFrame({"week": weeks, "open": [22, 24, 26, 27, 20, 20, 21, 20], "past_target": [12, 20, 35, 54, 15, 17, 17, 17],
                        "closures": [0, 0, 0, 0, 43, 0, 0, 0]})
    fig = fig_mitigation_open_past_target(mit, title="DEMO: Past-target fell 54 to 15 on a 43-row closure sweep, then rose to 17", source=src, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig02_mitigation-open-past-target.png"))

    fig = fig_closures_per_week(mit[["week", "closures"]], title="DEMO: One closure sweep in eight weeks; zero closures in seven", source=src, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig03_closures.png"))

    fig = fig_health_distribution({"Green": 32, "Yellow": 42, "Active": 13, "Pending": 10},
                                  title="DEMO: Yellow is the largest health class at 43% of 97 parent rows", source=src, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig04_health.png"))

    rpn = pd.DataFrame({"item": ["Electrical Distribution MV & LV", "Roof Zone 02", "Mechanical Piping Project D", "Roof Zones 01/04/10",
                                 "PCW Isolating PPCW 17 Loops", "Chiller plant sequencing", "CDA dryer redundancy", "AHU-22N fan wall"],
                        "rpn": [1000, 810, 810, 810, 800, 560, 448, 320],
                        "mitigation": [False, True, True, True, True, True, True, True]})
    fig = fig_rpn_watchlist(rpn, title="DEMO: Five rows at or above RPN 700; one carries no dated mitigation", source=src, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig05_rpn-watchlist.png"))

    pulls = [{"date": d, "identical": i} for d, i in zip(
        ["08/07", "08/14", "08/21", "08/28", "09/04", "09/11", "09/18"], [False, False, True, True, True, True, True])]
    fig = fig_frozen_weeks(pulls, title="DEMO: Roadmap hash unchanged for five consecutive pulls", source=src, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig06_frozen-weeks.png"))

    board = pd.DataFrame({"week": weeks, "reds": [3, 3, 2, 2, 2, 1, 1, 1], "anchors_closed": [1, 0, 2, 1, 0, 1, 2, 1]})
    fig = fig_csl_board_reds_anchors(board, title="DEMO: Board Reds down to one; two anchors closed in the week", source=src, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig07_board.png"))

    egrp = pd.DataFrame({"egrp": ["Facility", "AHU", "Roof", "Electrical", "Chillers", "Mechanical Piping", "CDA", "Boiler"],
                         "budget": [85e6, 61e6, 51.3e6, 40e6, 22e6, 12e6, 9e6, 7e6]})
    egrp["forecast"] = egrp["budget"] * np.array([1.02, 1.07, 1.12, 0.96, 1.00, 1.18, 1.04, 0.99])
    fig = fig_forecast_vs_budget_egrp(egrp, title="DEMO: Two E-GRPs exceed budget by more than 10% (R2)", source=src, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig08_forecast-vs-budget.png"))

    cash = pd.DataFrame({"quarter": ["2026 Q1", "2026 Q2", "2026 Q3", "2026 Q4"], "plan": [42.5e6, 41.6e6, 76.7e6, 32.9e6],
                         "actual": [38.1e6, 40.2e6, 61.0e6, np.nan]})
    fig = fig_quarterly_cash_flow(cash, title="DEMO: Cumulative actuals trail plan by $21.5M through Q3", source=src, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig09_cash-flow.png"))

    ts = pd.date_range("2026-08-20", periods=7 * 24 * 60, freq="min")
    flow = 4.2 + rng.normal(0, 0.05, len(ts))
    valve = np.clip(65 + np.cumsum(rng.normal(0, 0.3, len(ts))) * 0.05, 40, 100)
    valve[3000:3180] = 100.0
    rig = pd.DataFrame({"timestamp": ts, "flow_lpm": flow, "valve_pct": valve})
    dark = [{"start": ts[2000], "end": ts[2240], "class": "true_dark"}, {"start": ts[6000], "end": ts[6030], "class": "export_artifact"}]
    fig = fig_rig_timeseries(rig, title="DEMO: TR7 held 4.2 L/min; one 4-hour true dark window; valve saturated 3 hours", source=src,
                             dark_windows=dark, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig10_rig-timeseries.png"))

    days = np.arange(0, 21, 0.25)
    vol = 18.0 - 0.14 * days + rng.normal(0, 0.03, len(days))
    vol[days >= 14] += 2.0
    res = pd.DataFrame({"timestamp": pd.Timestamp("2026-08-01") + pd.to_timedelta(days, unit="D"), "volume_l": vol})
    fit = {"slope_l_per_day": -0.14, "intercept_l": 18.0 - 0.14 * 14 + 2.0, "r2": 0.96, "fit_start": res["timestamp"].iloc[int(np.argmax(days >= 14))],
           "runway_days": (vol[-1] - 6.0) / 0.14, "tier": "AMBER (A1)"}
    fig = fig_reservoir_drawdown(res, fit, title=f"DEMO: Reservoir losing 0.14 L/day; runway {fit['runway_days']:.0f} days after the refill", source=src,
                                 refills=[res["timestamp"].iloc[int(np.argmax(days >= 14))]], min_volume_l=6.0, demo=True)
    out.append(save_figure(fig, out_dir / "demo_fig11_reservoir-drawdown.png"))
    return out


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--demo", action="store_true", help="render every figure from synthetic data labeled DEMO")
    p.add_argument("--out-dir", default="chart_demo", help="output folder for --demo")
    p.add_argument("--list", action="store_true", help="print figure names and data contracts")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.list:
        for name, fn in FIGURES.items():
            print(f"{name}\n    {(fn.__doc__ or '').strip().splitlines()[0]}")
        print(f"\nbrand tokens: {BRAND_SOURCE}")
        return 0
    if args.demo:
        paths = render_demo(Path(args.out_dir))
        for p in paths:
            print(p)
        print(f"rendered {len(paths)} DEMO figures with {BRAND_SOURCE}")
        return 0
    build_parser().print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

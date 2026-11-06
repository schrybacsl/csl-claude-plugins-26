"""
CSL Consulting brand tokens for Python rendering stacks.

Import this module wherever a chart, PDF, workbook, deck, or document is
rendered so hex values are never retyped:

    from brand_tokens import CSL, TIER, CHART_SERIES, apply_matplotlib_style
    from brand_tokens import reportlab_colors, openpyxl_fills, tint

Source: CSL Brand Guidelines (Summer 2023) + csl-work-agent package conventions.
Keep in sync with brand-tokens.json and skills/csl-brand/SKILL.md.
"""
from __future__ import annotations

from dataclasses import dataclass


# --------------------------------------------------------------------------- #
# Core palette
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class _Palette:
    # Primary
    red: str = "#BF311A"        # logo + hairline accents only; never a fill
    black: str = "#000000"
    white: str = "#FFFFFF"
    # Accent
    navy: str = "#0A3173"
    teal_dark: str = "#056873"
    teal: str = "#1AA8BF"
    olive: str = "#BFAD2E"
    # Neutrals (package convention)
    ink: str = "#1F2933"
    slate: str = "#52606D"
    grey: str = "#9AA5B1"
    mist: str = "#E4E7EB"
    paper: str = "#F5F7FA"


CSL = _Palette()

LEGACY_FORBIDDEN = {"#C8102E", "#c8102e"}

# Tier / status signal colors (deliberately distinct from CSL Red)
TIER = {
    "RED": {"fill": "#C62828", "text": "#FFFFFF"},
    "AMBER": {"fill": "#E09B1A", "text": "#1F2933"},
    "GREEN": {"fill": "#2E7D32", "text": "#FFFFFF"},
    "BLUE": {"fill": "#0A3173", "text": "#FFFFFF"},
    "GREY": {"fill": "#9AA5B1", "text": "#1F2933"},
}

# Aliases commonly found in trackers
TIER_ALIASES = {
    "red": "RED", "critical": "RED", "overdue": "RED", "open": "RED",
    "amber": "AMBER", "yellow": "AMBER", "watch": "AMBER", "at risk": "AMBER",
    "green": "GREEN", "on track": "GREEN", "closed": "GREEN", "complete": "GREEN",
    "blue": "BLUE", "not started": "BLUE", "pending": "BLUE", "info": "BLUE",
    "grey": "GREY", "gray": "GREY", "n/a": "GREY", "no data": "GREY",
}


def tier_for(value: str | None) -> str:
    """Map a tracker health/status string onto a package tier key."""
    if not value:
        return "GREY"
    return TIER_ALIASES.get(str(value).strip().lower(), "GREY")


# --------------------------------------------------------------------------- #
# Tints
# --------------------------------------------------------------------------- #
def _hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#%02X%02X%02X" % rgb


def tint(hex_color: str, strength: float) -> str:
    """Mix a color with white. strength=0.6 keeps 60% of the color."""
    r, g, b = _hex_to_rgb(hex_color)
    k = max(0.0, min(1.0, strength))
    return _rgb_to_hex(tuple(round(c * k + 255 * (1 - k)) for c in (r, g, b)))


TINTS = {
    name: {"60": tint(hexv, 0.60), "30": tint(hexv, 0.30), "12": tint(hexv, 0.12)}
    for name, hexv in {
        "navy": CSL.navy, "teal_dark": CSL.teal_dark, "teal": CSL.teal, "olive": CSL.olive
    }.items()
}

# Fixed chart series order: navy, dark teal, teal, olive, then 60% tints
CHART_SERIES = [
    CSL.navy, CSL.teal_dark, CSL.teal, CSL.olive,
    TINTS["navy"]["60"], TINTS["teal_dark"]["60"], TINTS["teal"]["60"], TINTS["olive"]["60"],
]


# --------------------------------------------------------------------------- #
# Typography
# --------------------------------------------------------------------------- #
FONT_PRINT = "Avenir Medium"
FONT_OFFICE = "Avenir Next LT Pro"
FONT_FALLBACK = "Arial Narrow"
FONT_MONO = "Consolas"

FONT_STACK = [FONT_OFFICE, "Avenir", "Avenir Next", FONT_FALLBACK, "Arial"]

SCALE_PDF = {"title": 22, "h1": 14, "h2": 11, "body": 10, "table": 8.5, "caption": 7.5}
SCALE_DECK = {"title": 32, "section": 24, "body": 16, "table": 12, "footnote": 10}


def installed_brand_font() -> str:
    """Return the first brand-approved font installed on this machine.

    Uses matplotlib's font manager when available; falls back to fc-list.
    The caller should report the fallback in the delivery note if Arial Narrow
    (or Arial) is what actually rendered.
    """
    try:
        from matplotlib import font_manager
        names = {f.name for f in font_manager.fontManager.ttflist}
        for candidate in FONT_STACK:
            if candidate in names:
                return candidate
    except Exception:
        pass
    try:
        import subprocess
        out = subprocess.run(["fc-list", ":", "family"], capture_output=True, text=True).stdout
        for candidate in FONT_STACK:
            if candidate.lower() in out.lower():
                return candidate
    except Exception:
        pass
    return "DejaVu Sans"  # last resort; flag it


# --------------------------------------------------------------------------- #
# Matplotlib
# --------------------------------------------------------------------------- #
def apply_matplotlib_style(font: str | None = None) -> None:
    """Apply the CSL chart style globally. Call once before plotting."""
    import matplotlib as mpl
    from cycler import cycler

    face = font or installed_brand_font()
    mpl.rcParams.update({
        "font.family": face,
        "font.size": 9,
        "axes.titlesize": 11,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelsize": 9,
        "axes.edgecolor": CSL.grey,
        "axes.linewidth": 0.5,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": CSL.mist,
        "grid.linewidth": 0.5,
        "axes.prop_cycle": cycler(color=CHART_SERIES),
        "xtick.color": CSL.slate,
        "ytick.color": CSL.slate,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "text.color": CSL.ink,
        "axes.labelcolor": CSL.ink,
        "legend.frameon": False,
        "legend.fontsize": 8,
        "figure.facecolor": CSL.white,
        "axes.facecolor": CSL.white,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.facecolor": CSL.white,
    })


def add_source_note(fig, text: str) -> None:
    """Stamp the mandatory source line under a matplotlib figure."""
    fig.text(0.01, -0.02, text, ha="left", va="top", fontsize=7, color=CSL.slate)


# --------------------------------------------------------------------------- #
# ReportLab
# --------------------------------------------------------------------------- #
def reportlab_colors():
    """Return a dict of reportlab Color objects keyed like the palette."""
    from reportlab.lib import colors
    out = {
        "red": colors.HexColor(CSL.red),
        "black": colors.HexColor(CSL.black),
        "white": colors.HexColor(CSL.white),
        "navy": colors.HexColor(CSL.navy),
        "teal_dark": colors.HexColor(CSL.teal_dark),
        "teal": colors.HexColor(CSL.teal),
        "olive": colors.HexColor(CSL.olive),
        "ink": colors.HexColor(CSL.ink),
        "slate": colors.HexColor(CSL.slate),
        "grey": colors.HexColor(CSL.grey),
        "mist": colors.HexColor(CSL.mist),
        "paper": colors.HexColor(CSL.paper),
    }
    for k, v in TIER.items():
        out[f"tier_{k.lower()}"] = colors.HexColor(v["fill"])
    for name, t in TINTS.items():
        for pct, hexv in t.items():
            out[f"{name}_{pct}"] = colors.HexColor(hexv)
    return out


def reportlab_table_style(header_rows: int = 1):
    """Standard CSL table: navy header, white bold text, zebra rows, hairline rules."""
    from reportlab.lib import colors
    from reportlab.platypus import TableStyle
    c = reportlab_colors()
    return TableStyle([
        ("BACKGROUND", (0, 0), (-1, header_rows - 1), c["navy"]),
        ("TEXTCOLOR", (0, 0), (-1, header_rows - 1), c["white"]),
        ("FONTSIZE", (0, 0), (-1, -1), SCALE_PDF["table"]),
        ("LEADING", (0, 0), (-1, -1), SCALE_PDF["table"] * 1.25),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, c["mist"]),
        ("ROWBACKGROUNDS", (0, header_rows), (-1, -1), [c["white"], c["paper"]]),
        ("TEXTCOLOR", (0, header_rows), (-1, -1), c["ink"]),
    ])


# --------------------------------------------------------------------------- #
# openpyxl
# --------------------------------------------------------------------------- #
def openpyxl_fills():
    """Header fill, zebra fill, and tier fills for openpyxl."""
    from openpyxl.styles import PatternFill, Font, Alignment
    solid = lambda h: PatternFill("solid", fgColor=h.lstrip("#"))  # noqa: E731
    return {
        "header_fill": solid(CSL.navy),
        "header_font": Font(name=FONT_OFFICE, bold=True, color="FFFFFF", size=10),
        "body_font": Font(name=FONT_OFFICE, size=10, color=CSL.ink.lstrip("#")),
        "zebra_fill": solid(CSL.paper),
        "header_align": Alignment(vertical="center", wrap_text=True),
        "tier": {k: (solid(v["fill"]), Font(name=FONT_OFFICE, bold=True, color=v["text"].lstrip("#"), size=10))
                 for k, v in TIER.items()},
    }


def style_openpyxl_header(ws, header_row: int = 1, freeze: bool = True, autofilter: bool = True) -> None:
    """Apply the CSL header standard to a worksheet in place."""
    f = openpyxl_fills()
    for cell in ws[header_row]:
        cell.fill = f["header_fill"]
        cell.font = f["header_font"]
        cell.alignment = f["header_align"]
    if freeze:
        ws.freeze_panes = ws.cell(row=header_row + 1, column=1)
    if autofilter and ws.max_column and ws.max_row:
        ws.auto_filter.ref = ws.dimensions


# --------------------------------------------------------------------------- #
# Guard
# --------------------------------------------------------------------------- #
def assert_no_legacy_red(text: str) -> None:
    """Raise if the superseded CSL Red hex appears in generated source/markup."""
    for bad in LEGACY_FORBIDDEN:
        if bad in text:
            raise ValueError(f"Legacy CSL Red {bad} found; use {CSL.red} for the logo only.")


if __name__ == "__main__":
    print("CSL palette:", CSL)
    print("Tints:", TINTS)
    print("Chart series:", CHART_SERIES)
    print("Installed brand font:", installed_brand_font())

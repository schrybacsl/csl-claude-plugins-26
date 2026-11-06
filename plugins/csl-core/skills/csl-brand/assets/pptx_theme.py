"""
python-pptx helpers that apply the CSL deck standard (16:9).

Usage:
    from pptx import Presentation
    from pptx_theme import new_deck, add_title_slide, add_content_slide, add_kpi_strip, add_table, add_footer

    prs = new_deck()
    add_title_slide(prs, "Mid-Week Executive Update", "Week 40 | Mon 09/28/26 to Fri 10/02/26",
                    doc_number="CSL-W77-WKR-40B", prepared_by="S. Schryba", prepared_for="S. Kazantzidis",
                    logo_path="/path/to/csl_logo.png")
    s = add_content_slide(prs, "Executive summary")
    add_kpi_strip(prs, s, [("Permits gated", "40/40", "+0"), ("Mitigation past target", "17", "+2"),
                           ("Roadmap frozen", "6 wks", "RED")])
    ...
    prs.save("CSL-W77-WKR-40B.pptx")

Color and font values come from brand_tokens.py; nothing is hard-coded here.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from brand_tokens import CSL, TIER, SCALE_DECK, FONT_OFFICE, tier_for  # noqa: E402

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt, Emu

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN = Inches(0.5)


def _rgb(hexv: str) -> RGBColor:
    return RGBColor.from_string(hexv.lstrip("#"))


def _set_font(run, size_pt: float, bold=False, italic=False, color=CSL.ink, name=FONT_OFFICE):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = _rgb(color)


def new_deck() -> Presentation:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs


def _blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def _rect(slide, x, y, w, h, fill_hex, line=False):
    from pptx.enum.shapes import MSO_SHAPE
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = _rgb(fill_hex)
    if line:
        shp.line.color.rgb = _rgb(CSL.mist)
        shp.line.width = Pt(0.5)
    else:
        shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def _text(slide, x, y, w, h, text, size, bold=False, italic=False, color=CSL.ink, align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.05)
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = text
    _set_font(r, size, bold, italic, color)
    return tb


def add_title_slide(prs, title, subtitle, doc_number, prepared_by, prepared_for,
                    logo_path=None, cover_hex=CSL.navy, distribution=None, date_issued=None):
    """Cover: full-bleed cover field, white type, logo on a white block.

    cover_hex defaults to CSL navy. An engagement that has adopted a client cover
    color (W77 royal-blue from WKR-40A on) passes it explicitly.
    """
    s = _blank(prs)
    _rect(s, 0, 0, SLIDE_W, SLIDE_H, cover_hex)
    # Logo block (white) top-left
    if logo_path and os.path.exists(logo_path):
        _rect(s, MARGIN, MARGIN, Inches(1.9), Inches(0.9), CSL.white)
        s.shapes.add_picture(logo_path, MARGIN + Inches(0.15), MARGIN + Inches(0.12), width=Inches(1.6))
    _text(s, MARGIN, Inches(2.2), Inches(11), Inches(0.5), "CSL CONSULTING | OWNER'S REPRESENTATIVE",
          SCALE_DECK["footnote"] + 2, color=CSL.white)
    _text(s, MARGIN, Inches(2.7), Inches(12), Inches(1.2), title, SCALE_DECK["title"], bold=True, color=CSL.white)
    _text(s, MARGIN, Inches(3.9), Inches(12), Inches(0.6), subtitle, SCALE_DECK["section"] - 4, italic=True, color=CSL.white)
    meta = [
        ("Document", doc_number),
        ("Prepared by", prepared_by),
        ("Prepared for", prepared_for),
        ("Date issued", date_issued or ""),
        ("Distribution", distribution or ""),
    ]
    y = Inches(5.0)
    for k, v in meta:
        if not v:
            continue
        _text(s, MARGIN, y, Inches(2.0), Inches(0.35), k.upper(), SCALE_DECK["footnote"], color=CSL.white)
        _text(s, MARGIN + Inches(2.0), y, Inches(9), Inches(0.35), v, SCALE_DECK["footnote"] + 2, color=CSL.white)
        y += Inches(0.34)
    return s


def add_content_slide(prs, title, doc_number="", page_label="", logo_path=None):
    s = _blank(prs)
    _text(s, MARGIN, Inches(0.35), Inches(12), Inches(0.6), title, SCALE_DECK["section"], bold=True, color=CSL.navy)
    # navy rule under title
    _rect(s, MARGIN, Inches(0.95), SLIDE_W - 2 * MARGIN, Pt(1.5), CSL.navy)
    add_footer(s, doc_number, page_label, logo_path)
    return s


def add_footer(slide, doc_number="", page_label="", logo_path=None):
    y = SLIDE_H - Inches(0.45)
    _rect(slide, MARGIN, y - Inches(0.05), SLIDE_W - 2 * MARGIN, Pt(0.5), CSL.grey)
    if logo_path and os.path.exists(logo_path):
        slide.shapes.add_picture(logo_path, MARGIN, y, width=Inches(0.9))
    _text(slide, Inches(5.0), y, Inches(3.3), Inches(0.3), doc_number, SCALE_DECK["footnote"], color=CSL.slate, align=PP_ALIGN.CENTER)
    _text(slide, SLIDE_W - MARGIN - Inches(2.0), y, Inches(2.0), Inches(0.3), page_label, SCALE_DECK["footnote"], color=CSL.slate, align=PP_ALIGN.RIGHT)


def add_kpi_strip(prs, slide, kpis, top=Inches(1.2), height=Inches(1.25)):
    """kpis: list of (label, value, delta_or_tier). Tier words color the card's top bar."""
    n = max(1, len(kpis))
    gap = Inches(0.15)
    w = (SLIDE_W - 2 * MARGIN - gap * (n - 1)) / n
    x = MARGIN
    for label, value, delta in kpis:
        card = _rect(slide, x, top, w, height, CSL.white, line=True)
        bar_hex = TIER[tier_for(delta)]["fill"] if tier_for(delta) in ("RED", "AMBER", "GREEN") else CSL.navy
        _rect(slide, x, top, w, Pt(3), bar_hex)
        _text(slide, x, top + Inches(0.1), w, Inches(0.3), str(label).upper(), SCALE_DECK["footnote"], color=CSL.slate)
        _text(slide, x, top + Inches(0.38), w, Inches(0.55), str(value), 26, bold=True, color=CSL.navy)
        _text(slide, x, top + Inches(0.9), w, Inches(0.3), str(delta), SCALE_DECK["footnote"], color=CSL.slate)
        x += w + gap


def add_table(slide, rows, left=MARGIN, top=Inches(2.7), width=None, col_widths_in=None, font_pt=None):
    """rows: list of lists; first row is the header. Tier cells (RED/AMBER/GREEN) are auto-colored."""
    width = width or (SLIDE_W - 2 * MARGIN)
    font_pt = font_pt or SCALE_DECK["table"]
    nrows, ncols = len(rows), len(rows[0])
    shape = slide.shapes.add_table(nrows, ncols, left, top, width, Inches(0.3) * nrows)
    tbl = shape.table
    if col_widths_in:
        for i, w in enumerate(col_widths_in):
            tbl.columns[i].width = Inches(w)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = tbl.cell(r, c)
            cell.text = "" if val is None else str(val)
            para = cell.text_frame.paragraphs[0]
            run = para.runs[0] if para.runs else para.add_run()
            if r == 0:
                cell.fill.solid(); cell.fill.fore_color.rgb = _rgb(CSL.navy)
                _set_font(run, font_pt, bold=True, color=CSL.white)
            else:
                cell.fill.solid(); cell.fill.fore_color.rgb = _rgb(CSL.white if r % 2 else CSL.paper)
                t = tier_for(val) if isinstance(val, str) and val.strip().upper() in ("RED", "AMBER", "GREEN") else None
                if t:
                    cell.fill.fore_color.rgb = _rgb(TIER[t]["fill"])
                    _set_font(run, font_pt, bold=True, color=TIER[t]["text"])
                    para.alignment = PP_ALIGN.CENTER
                else:
                    _set_font(run, font_pt, color=CSL.ink)
            cell.margin_left = cell.margin_right = Inches(0.06)
            cell.margin_top = cell.margin_bottom = Inches(0.03)
    return shape


def add_source_note(slide, text):
    _text(slide, MARGIN, SLIDE_H - Inches(0.85), SLIDE_W - 2 * MARGIN, Inches(0.3), text, SCALE_DECK["footnote"] - 1, italic=True, color=CSL.slate)

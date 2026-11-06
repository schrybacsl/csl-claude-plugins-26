"""
python-docx helpers that apply the CSL Word standard (Letter, 0.75 in margins).

Usage:
    from docx import Document
    from docx_styles import new_document, add_document_control_block, add_heading, add_table, add_footer

    doc = new_document()
    add_document_control_block(doc, {
        "Document No.": "W77-SOP-PCW-040", "Revision": "0", "Title": "40-inch PCW System Filter Changeout",
        "Author": "S. Schryba / D. Wolf, CSL Consulting", "Technical Reviewer": "P. Gorman, ASML",
        "Approver": "B. Gannon, ASML", "Date Issued": "08/04/26", "Supersedes": "Legacy 10-inch procedure",
    })
    add_heading(doc, "1. Purpose", level=1)
    doc.add_paragraph("...", style="CSL Body")
    add_table(doc, [["Step", "Action", "Verification"], ["1", "...", "..."]])
    add_footer(doc, "W77-SOP-PCW-040 Rev 0 | CSL Consulting | Owner's Representative")
    doc.save("W77-SOP-PCW-040_Rev0.docx")
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from brand_tokens import CSL, TIER, SCALE_PDF, FONT_OFFICE, tier_for  # noqa: E402

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Inches


def _rgb(hexv: str) -> RGBColor:
    return RGBColor.from_string(hexv.lstrip("#"))


def _shade(cell, hexv: str) -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexv.lstrip("#"))
    tcPr.append(shd)


def _style(doc, name, base, size, bold=False, italic=False, color=CSL.ink, space_after=6, keep_next=False):
    styles = doc.styles
    try:
        st = styles[name]
    except KeyError:
        from docx.enum.style import WD_STYLE_TYPE
        st = styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        st.base_style = styles[base]
    st.font.name = FONT_OFFICE
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT_OFFICE)
    st.font.size = Pt(size)
    st.font.bold = bold
    st.font.italic = italic
    st.font.color.rgb = _rgb(color)
    st.paragraph_format.space_after = Pt(space_after)
    st.paragraph_format.line_spacing = 1.15
    st.paragraph_format.keep_with_next = keep_next
    return st


def new_document() -> Document:
    doc = Document()
    for s in doc.sections:
        s.page_width, s.page_height = Inches(8.5), Inches(11)
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Inches(0.75)
    _style(doc, "CSL Title", "Title", SCALE_PDF["title"], bold=True, color=CSL.navy, space_after=4)
    _style(doc, "CSL Subtitle", "Normal", SCALE_PDF["h2"], italic=True, color=CSL.teal_dark, space_after=12)
    _style(doc, "CSL H1", "Heading 1", SCALE_PDF["h1"], bold=True, color=CSL.navy, space_after=4, keep_next=True)
    _style(doc, "CSL H2", "Heading 2", SCALE_PDF["h2"], italic=True, color=CSL.teal_dark, space_after=3, keep_next=True)
    _style(doc, "CSL Body", "Normal", SCALE_PDF["body"], color=CSL.ink, space_after=6)
    _style(doc, "CSL Caption", "Normal", SCALE_PDF["caption"], italic=True, color=CSL.slate, space_after=8)
    _style(doc, "CSL Table", "Normal", SCALE_PDF["table"], color=CSL.ink, space_after=0)
    # Also retarget the built-in Normal so stray paragraphs comply
    normal = doc.styles["Normal"]
    normal.font.name = FONT_OFFICE
    normal.font.size = Pt(SCALE_PDF["body"])
    normal.font.color.rgb = _rgb(CSL.ink)
    return doc


def add_heading(doc, text, level=1):
    return doc.add_paragraph(text, style="CSL H1" if level == 1 else "CSL H2")


def add_table(doc, rows, col_widths_in=None, header_rows=1, tier_column=None):
    """rows: list of lists; first `header_rows` rows are headers. tier_column: index to auto-color RED/AMBER/GREEN."""
    nrows, ncols = len(rows), len(rows[0])
    t = doc.add_table(rows=nrows, cols=ncols)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = "Table Grid"
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = t.cell(r, c)
            cell.text = ""
            p = cell.paragraphs[0]
            p.style = doc.styles["CSL Table"]
            run = p.add_run("" if val is None else str(val))
            run.font.name = FONT_OFFICE
            run.font.size = Pt(SCALE_PDF["table"])
            if r < header_rows:
                _shade(cell, CSL.navy)
                run.font.bold = True
                run.font.color.rgb = _rgb(CSL.white)
            else:
                if (r - header_rows) % 2 == 1:
                    _shade(cell, CSL.paper)
                if tier_column is not None and c == tier_column:
                    tier = tier_for(val)
                    if tier in ("RED", "AMBER", "GREEN"):
                        _shade(cell, TIER[tier]["fill"])
                        run.font.bold = True
                        run.font.color.rgb = _rgb(TIER[tier]["text"])
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if col_widths_in:
        for row in t.rows:
            for i, w in enumerate(col_widths_in):
                row.cells[i].width = Inches(w)
    # thin light borders
    tbl = t._tbl
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single"); el.set(qn("w:sz"), "4"); el.set(qn("w:color"), CSL.mist.lstrip("#"))
        borders.append(el)
    tbl.tblPr.append(borders)
    doc.add_paragraph("", style="CSL Body")
    return t


def add_document_control_block(doc, fields: dict):
    """First table in SOPs, scope packages, assessments: the document control block."""
    rows = [["Field", "Value"]] + [[k, v] for k, v in fields.items()]
    return add_table(doc, rows, col_widths_in=[1.8, 5.2])


def add_revision_history(doc, history):
    """history: list of (rev, date, author, description)."""
    rows = [["Rev", "Date", "Author", "Description of change"]] + [list(map(str, h)) for h in history]
    add_heading(doc, "Revision history", level=2)
    return add_table(doc, rows, col_widths_in=[0.6, 0.9, 1.6, 3.9])


def add_footer(doc, text):
    for s in doc.sections:
        p = s.footer.paragraphs[0]
        p.text = text
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs:
            r.font.name = FONT_OFFICE
            r.font.size = Pt(SCALE_PDF["caption"])
            r.font.color.rgb = _rgb(CSL.slate)
        # page number field on the right
        p2 = s.footer.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p2.add_run()
        for tag, txt in (("begin", None), (None, "PAGE"), ("end", None)):
            if tag:
                fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), tag); run._r.append(fc)
            else:
                it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; run._r.append(it)
        run.font.size = Pt(SCALE_PDF["caption"]); run.font.color.rgb = _rgb(CSL.slate)

---
name: csl-brand
description: >
  CSL Consulting visual identity for every file Claude makes: palette (CSL Red #BF311A for logo and
  hairlines only; navy, dark teal, teal, olive for everything else), status colors, Avenir type with
  fallbacks, logo lockup, page anatomy for PDF, Word, PowerPoint, Excel, HTML, and email, and the
  pre-issue brand QA checklist, with token files in CSS, JSON, and Python. Use it whenever a CSL
  file, chart, or table is created or revised, when someone asks for "CSL branded", "our template",
  "house style", brand colors, fonts, or logo placement, and to audit an existing file for brand
  compliance. Load it before rendering anything visual, even one chart.
---

# CSL Brand Standard for Agent-Produced Deliverables

Source of authority: CSL Consulting Brand Guidelines, Summer 2023 edition (user-provided). Where this skill adds conventions the guidelines do not cover (status colors, chart sequences, page maps), they are marked **package convention** and were derived from CSL deliverables issued on the ASML W77 engagement in 2026. The guidelines win over this skill if they ever conflict; update this skill rather than deviating silently.

Machine-readable tokens for everything below live in `assets/` (CSS, JSON, Python). Use them instead of retyping hex values.

---

## 1. Color

### 1.1 Primary

| Token | Name | Hex | RGB | Use |
|---|---|---|---|---|
| `csl-red` | CSL Red | `#BF311A` | 191, 49, 26 | Logo. Hairline rules and small accent marks only, in sparing doses. Never a fill, background, chart series, table header, or body-text color. Supersedes the legacy `#C8102E`, which must not appear in new files. |
| `csl-black` | Black | `#000000` | 0, 0, 0 | Wordmark "CONSULTING", body text in print. |
| `csl-white` | White | `#FFFFFF` | 255, 255, 255 | Page ground. Reports are white-background documents. |

### 1.2 Accent palette (color the document with these)

| Token | Name | Hex | RGB | Typical role |
|---|---|---|---|---|
| `csl-navy` | Navy | `#0A3173` | 10, 49, 115 | Covers, section headers, primary chart series, table header fills, KPI values |
| `csl-teal-dark` | Dark Teal | `#056873` | 5, 104, 115 | Secondary headers, second chart series, callout borders |
| `csl-teal` | Teal | `#1AA8BF` | 26, 168, 191 | Highlights, third chart series, links in HTML, progress fills |
| `csl-olive` | Olive | `#BFAD2E` | 191, 173, 46 | Fourth chart series, annotation, "watch" emphasis |

Chart series order is fixed: navy → dark teal → teal → olive → then 60% tints of the same four in the same order. Do not introduce other hues into a chart. Single-series charts use navy.

### 1.3 Neutrals (package convention)

| Token | Hex | Use |
|---|---|---|
| `csl-ink` | `#1F2933` | Body text on screen and in PDF reports (softer than pure black for long reading) |
| `csl-slate` | `#52606D` | Secondary text, captions, source notes |
| `csl-grey` | `#9AA5B1` | Hairlines, axis lines, disabled |
| `csl-mist` | `#E4E7EB` | Table zebra rows, panel backgrounds |
| `csl-paper` | `#F5F7FA` | Page-section backgrounds in HTML dashboards |

### 1.4 Status colors (package convention; not from the brand guide)

RED / AMBER / GREEN tiers need signal colors that are visibly not CSL Red. Use these and only these for status badges, health cells, and RAG dots:

| Tier | Hex | Text on it |
|---|---|---|
| RED | `#C62828` | white |
| AMBER | `#E09B1A` | `csl-ink` |
| GREEN | `#2E7D32` | white |
| BLUE (informational / not started) | `#0A3173` (navy) | white |
| GREY (no data / not applicable) | `#9AA5B1` | `csl-ink` |

Status color is never the only carrier of meaning: pair it with the word (RED, AMBER, GREEN) or a symbol, so the document survives greyscale printing and color-blind readers.

### 1.5 Tints

When a fill lighter than the base is needed (table bands, area-chart fills, KPI card backgrounds), use these fixed tints rather than ad-hoc opacity:

| Base | 60% | 30% | 12% |
|---|---|---|---|
| Navy | `#6C83AB` | `#B6C1D5` | `#E2E6EE` |
| Dark Teal | `#69A4AB` | `#B4D2D5` | `#E1EDEE` |
| Teal | `#76CBD9` | `#BAE5EC` | `#E4F5F7` |
| Olive | `#D9CE82` | `#ECE6C0` | `#F7F5E6` |

(Tints are computed as base × k + white × (1 − k), rounded; `assets/brand_tokens.py` regenerates them.)

### 1.6 Client co-branding

Client marks (for example the ASML mark on W77 covers) may appear on the cover and running footer of a client-facing report when the engagement has adopted that look. The client's brand color may be used as the **cover field** for that engagement's report family only (W77 adopted a royal-blue cover with the 9/28/26 Look-Ahead, WKR-40A; reuse the cover hex from the last issued edition's report-factory config rather than re-deriving it). Inside the document, the CSL accent palette governs. CSL Red never touches the client color; keep the logo on a white block.

---

## 2. Typography

| Context | Face | Weight / style |
|---|---|---|
| Print and PDF (report factory, InDesign, HTML→PDF) | **Avenir Medium** | Headers bold, subheaders italic, body Medium |
| Microsoft Office (Word, PowerPoint, Excel, Outlook) | **Avenir Next LT Pro** | Same weights; Demi for headers if Bold is unavailable |
| Fallback when Avenir is not installed | **Arial Narrow** | Same weights; keep the same size scale |
| Code, IDs, sheet cell references inside a document | Consolas / Menlo | Regular, one size down |

Rules that hold across media:

- Headers are **bold**, subheaders are *italic*. Do not underline. Do not set headers in all caps except the document type line on a cover ("MEETING MINUTES", "END-OF-WEEK EXECUTIVE REPORT").
- Body text is never smaller than 9 pt in print or 13 px on screen. Tables may drop to 8 pt / 12 px. Source notes 7.5 pt.
- Size scale for Letter-size PDF reports (package convention): title 22 pt, section header 14 pt bold, subheader 11 pt italic, body 10 pt, table 8.5 pt, caption 7.5 pt.
- Size scale for 16:9 decks: title 32 pt, section 24 pt, body 16 pt, table 12 pt, footnote 10 pt.
- Left-align everything. Justified text is not used. Numbers in tables right-align; text left-aligns; dates and IDs center.
- Line spacing 1.15 in Office; 1.35 in HTML.
- Never embed Avenir in an artifact that will be distributed outside CSL without confirming license coverage; PDFs produced by the report factory embed subsets, which is permitted for CSL's licensed seats.

Font availability check (run before rendering): if `fc-list | grep -i avenir` returns nothing, render with Arial Narrow and say so in the delivery note. Do not substitute Helvetica, Calibri, or a Google font.

---

## 3. Logo

The official logo files are the CSL brand package assets (PNG and SVG; horizontal lockup). They are not yet committed to this repository: Marketing adds them under `assets/logo/` by pull request (repository `GOVERNANCE.md`). Until then, read them from the CSL brand library on SharePoint through the Microsoft 365 connector, or ask the operator to attach them.

Lockup: red box (`#BF311A`) with white "C | S | L" letters, and the word **CONSULTING** in black, letter-spaced, set beneath. Only the official file may be used in an issued document. The CSS/HTML approximation in `assets/logo-fallback.html` exists for previews and internal drafts when the file is not reachable; replace it before issue.

| Rule | Value |
|---|---|
| Clear space | Height of the red box on all four sides |
| Minimum size | 0.9 in wide in print; 120 px on screen |
| Placement, report cover | Top left, on white |
| Placement, running header | Top left, 0.6 in wide, page number and document number top right |
| Placement, deck | Bottom left of every content slide at 0.9 in; top left on title slide |
| Placement, minutes and letters | Centered top of page 1 (matches the CSL minutes template) |
| Never | Recolor, outline, stretch, place on red, place on a photo, add a drop shadow, rebuild the letters in a different typeface |

---

## 4. Company naming and boilerplate

| Context | Form |
|---|---|
| First reference in any document | CSL Consulting |
| Subsequent references | CSL |
| Legal / contractual | CSL Consulting, LLC |
| Never | "CSL LLC", "CSL Consulting LLC" without the comma, "C.S.L." |
| Headquarters line | 152 Middlesex Turnpike, Burlington, MA 01803 |
| Role descriptor | Owner's Representative / Owner's Project Manager (OPM) / Capital Program Management, as the engagement defines it |

Boilerplate footer for client-facing reports: `CSL Consulting | Owner's Representative | [Program name] | [Document number] Rev [n] | Page X of Y`.

Confidentiality line (when the audience is external to the client team): `Prepared for [Client] by CSL Consulting. Contains program information intended for the distribution list only.`

---

## 5. Page anatomy by medium

Full page maps with measurements are in `references/document-anatomy.md`. The essentials:

**PDF report (Letter portrait, 0.75 in margins).** Cover: logo top left, document type line in caps, title, subtitle with the reporting window, metadata block (document number, revision, date issued, prepared by, prepared for, distribution), optional client mark bottom right. Pages 2+: running header (logo, document number, page X of Y), section header band in navy text with a 1 pt navy rule, body, source note at page foot in slate 7.5 pt. Last page: docket / next actions table, then the source note listing every pull.

**PowerPoint (16:9).** Title slide: cover field (navy, or the engagement's adopted cover color), white title, logo on a white block. Content slides: white ground, slide title in navy 24 pt bold, thin navy rule, content, footer strip with logo left / document number center / page right in slate 10 pt. Use `assets/pptx_theme.py` to apply.

**Word (Letter).** Styles Title / Heading 1 / Heading 2 / Body / Caption mapped in `assets/docx_styles.py`. Heading 1 navy bold 14 pt; Heading 2 dark teal italic 11 pt; body ink 10 pt; tables with navy header row and white text, zebra rows in mist. Document control block (number, revision, author, reviewer, approver, dates) as the first table in SOPs and technical documents.

**Excel.** Header row: navy fill, white bold text, frozen; filters on; column widths set; numbers formatted; a `README` or `Control` sheet first with document number, source, pull date, and column dictionary. Conditional formatting for tiers uses the status colors in 1.4. Never fill cells CSL Red.

**HTML dashboard / artifact.** Tokens from `assets/brand-tokens.css` on `:root`. Paper ground, navy header bar with white type, cards on white with mist borders, status dots per 1.4, charts per 1.2 series order. Dark mode is permitted only if every token is redefined; otherwise force light.

**Email.** Plain text or minimal HTML. No banner images. Signature block per `skills/csl-client-comms/templates/signature-block.md`. Never paste brand colors into email body text.

---

## 6. Charts (with `dataviz` conventions)

- One message per chart; the title states the finding ("Mitigation past-target rows doubled to 20"), not the metric name.
- Series colors in the fixed order (1.2). Tier-coded charts (health, RAG) use the status colors (1.4), never the accent palette.
- Axis lines and gridlines in `csl-grey` at 0.5 pt; no chart borders; no 3-D; no gradients.
- Data labels on bars when there are eight or fewer bars; otherwise a table beside the chart.
- Source line under every chart: sheet name, sheet ID, pull timestamp.
- Save at 2× for PDF embedding; PNG for reports, SVG for HTML.
- Matplotlib style sheet and ReportLab color registry are in `assets/brand_tokens.py`.

---

## 7. Voice in branded documents

The brand is also how the writing sounds. Client-executive documents use a plain human voice: short sentences, active verbs, numbers with units, no jargon a non-engineer would have to look up, and no dash constructions in running prose (use a period or a comma). Records (minutes, notices) are third person, past tense, formal. Correspondence is first person plural. See `skills/csl-client-comms` for tone by audience and `skills/csl-weekly-reporting` for the report-family voice rules.

---

## 8. Pre-issue brand QA

Run `references/brand-qa-checklist.md` on every file before it is called done. The five checks that catch most defects:

1. Grep the file (or its source) for `C8102E` and for any use of `BF311A` outside the logo and hairlines.
2. Confirm the typeface actually rendered (open the PDF and inspect fonts; `pdffonts file.pdf`), not just the CSS declaration.
3. Confirm the cover metadata block is complete and the document number matches `csl-document-control`.
4. Confirm every chart has the source line and follows the series order.
5. Print-preview one page in greyscale and confirm tiers are still readable by their labels.

---

## Files in this skill

- `assets/brand-tokens.css` — CSS custom properties for HTML artifacts and HTML→PDF.
- `assets/brand-tokens.json` — same tokens for JavaScript, Replit apps, and config files.
- `assets/brand_tokens.py` — Python constants, matplotlib rcParams, ReportLab color registry, openpyxl fills.
- `assets/pptx_theme.py` — python-pptx helpers that apply the deck standard.
- `assets/docx_styles.py` — python-docx helpers that apply the Word standard.
- `assets/logo-fallback.html` — CSS lockup for previews only.
- `references/document-anatomy.md` — page maps and measurements per medium.
- `references/brand-qa-checklist.md` — the pre-issue checklist.

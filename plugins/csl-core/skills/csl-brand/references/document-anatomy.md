# Document Anatomy by Medium

Measurements and page maps for CSL deliverables. Package convention derived from the CSL-W77 report families issued in 2026; the brand guide governs color and type, this file governs layout.

## 1. PDF report family (WKR-A / WKR-B / WKR-C, program summaries, assessments)

**Page:** US Letter portrait, 8.5 × 11 in, margins 0.75 in all sides (text block 7.0 × 9.5 in). Rendered by the project report factory (ReportLab or HTML → Chromium). Not tabloid; the 11 × 17 landscape executive format is retired except where a client has explicitly asked for it.

**Cover (page 1).**
- Cover field: full page. Default CSL navy `#0A3173`; an engagement's adopted client cover color is permitted (W77: royal-blue field from WKR-40A, 09/28/26, onward; take the hex from the last issued edition's factory config).
- Logo: white block 1.9 × 0.9 in at top left containing the official CSL logo at 1.6 in wide.
- Document type line: caps, letter-spaced, 11 pt, white at 85% opacity, 2.2 in from top. Examples: `ONE-WEEK LOOK-AHEAD`, `MID-WEEK EXECUTIVE UPDATE`, `END-OF-WEEK EXECUTIVE REPORT`.
- Title: 30 pt bold white. Program name.
- Subtitle: 20 pt italic white. Reporting window written as `Week 40 | Monday 09/28/26 to Friday 10/02/26`.
- Metadata block (from 5.0 in): two-column, label caps 10 pt / value 12 pt, white. Rows: Document, Revision, Date issued, Prepared by, Prepared for, Distribution. Cover blocks read `Prepared by <operator> for <client recipient>` when the edition's direction calls for a single line.
- Client mark (optional): bottom right, no larger than the CSL logo block, on its own white block.
- No source note on the cover.

**Content pages (2 to n).**
- Running header: logo at 0.6 in wide left; `Document number | Rev` center; `Page X of Y` right; 7.5 pt slate; 0.5 pt grey rule beneath.
- Section header: 14 pt bold navy, 1 pt navy rule under it, 10 pt space after.
- Subheader: 11 pt italic dark teal.
- Body: 10 pt ink, 1.35 leading, single column. Two columns are allowed for a KPI strip or a chart-plus-commentary pair; never for running prose.
- KPI strip: up to six cards across the text block, each with a 3 pt top bar in the tier color (or navy when untiered), label caps 7.5 pt slate, value 20 pt bold navy, delta 7.5 pt slate.
- Tables: navy header row, white bold 8.5 pt; zebra rows paper/white; 0.4 pt mist rules; tier cells filled per status colors with the word inside.
- Charts: full text-block width or half-width paired with commentary; title is the finding; source line 7.5 pt slate under the chart.
- Page foot source note: `Source: [Sheet name] (ID [id]) pulled [MM/DD/YY HH:MM ET]; ...` 7.5 pt slate, above the footer rule.
- Running footer: `CSL Consulting | Owner's Representative | [Program] | [Doc no.] Rev [n]` left; page right.

**Last page.** Docket / next-actions table (Item, Owner, Due, Tier), then the consolidated source note listing every pull with timestamps, then the standing statement: `This report reflects tracker data as of the pull timestamps listed. Field conditions may have changed after the pull.`

**Standard page counts (2026 practice).** WKR-A 10 pp; WKR-B 5 pp; WKR-C 8 to 11 pp; program critical summary 1 to 2 pp; EWO 1 to 2 pp.

## 2. Meeting minutes and agendas

Follow the CSL minutes template exactly (it predates this package and is the firm standard): Letter portrait, margins 0.65 in top / 0.6 in bottom / 0.75 in left and right; logo centered at top of each page; document title underlined caps (`MEETING MINUTES #016`); metadata table with 1 pt black borders; black header rows in the attendee and action tables (this is the one place a black table header is standard); item numbering `[meeting]-[item]` zero-padded to three digits; status vocabulary Open / Closed / In Progress / Record; footer `[Meeting description] | [Meeting date]` centered 8 pt on every page; legal disclaimer on the last page. Status colors: Open in tier red `#C62828`, Closed in tier green `#2E7D32`, Record in slate. Date format MM/DD/YY. Body Avenir Next LT Pro 9 pt (Arial fallback in the legacy HTML template is acceptable when regenerating from that template).

Agenda: single page, same header, timed items table (Time, Item, Lead, Purpose: Decide / Inform / Discuss), "Carried items" block listing open action IDs, "Pre-reads" block with document numbers.

## 3. Executive memo / notice / gap analysis

- Memo: Letter portrait, 1 to 2 pages. Header block: logo left; `MEMORANDUM` caps right; rule. To / From / Date / Re / Document number / Distribution lines. Bottom line paragraph first, then Findings (numbered), then Recommended actions (table: Action, Owner, Due), then Basis (documents relied on, with numbers and dates). Signature line for the CSL author.
- Notice (engineering / facilities notice, e.g., `FM-W77-UTM-0903 R1`): same header; adds a Status line (Information / Action Required / Escalation) and an Affected systems line; body organized as Condition, Evidence, Risk, Recommended actions, Next review date.
- Gap-analysis one-pager: Letter landscape, single page. Left column: timeline of events with dates and document numbers. Right column: the gap statement, impact, and the record request. Footer carries the document number and "Program record".

## 4. PowerPoint deck (16:9)

- 13.333 × 7.5 in. Margins 0.5 in.
- Title slide: cover field (navy or engagement cover color), logo on white block top left, org line, title 32 pt bold white, subtitle 20 pt italic white, metadata rows from 5.0 in.
- Content slide: title 24 pt bold navy at 0.35 in, 1.5 pt navy rule at 0.95 in, content from 1.2 in, footer strip at 7.05 in with 0.5 pt grey rule, logo 0.9 in left, document number center, page label right, all 10 pt slate.
- Section divider: navy field, section title 28 pt bold white, no logo.
- Chart slide: one chart, title is the finding, source note 9 pt italic slate above the footer.
- Standard executive deck: 3 slides (cover, KPI strip + executive summary, critical path + risk) when a deck is requested in place of the PDF B edition; the chart library slides are appended as needed.

## 5. Word documents (SOPs, scope packages, assessments, proposals)

- Letter portrait, 0.75 in margins.
- First table: document control block (Document No., Revision, Title, Author, Technical reviewer, Approver, Date issued, Supersedes, Distribution).
- Styles: CSL Title 22 pt bold navy; CSL Subtitle 11 pt italic dark teal; CSL H1 14 pt bold navy; CSL H2 11 pt italic dark teal; CSL Body 10 pt ink; CSL Caption 7.5 pt italic slate; CSL Table 8.5 pt.
- Numbered headings (1., 1.1) for SOPs and assessments; unnumbered for proposals.
- Footer: `[Doc no.] Rev [n] | CSL Consulting | Owner's Representative` left, page number right.
- Revision history table at the end of SOPs and any document expected to revise.
- File properties (Title, Subject, Author, Company) set to the document, not inherited from a Save-As source. A stale title in file properties is a brand defect.

## 6. Excel workbooks (trackers, upload sheets, extractions)

- Sheet 1 `Control` (or `README`): document number, revision, purpose, source sheets with IDs and pull timestamps, column dictionary, change log.
- Data sheets: header row navy fill / white bold / frozen; autofilter; widths set; number formats applied (currency `$#,##0.00`, dates `MM/DD/YY`, percentages `0.0%`); tier columns with conditional formatting per status colors; no merged cells in data regions; no CSL Red fills anywhere.
- Formula-driven roll-ups stay live (no pasted values) unless the deliverable is an import file, in which case values only, and the Control sheet says so.
- Tab colors: navy for data, dark teal for roll-ups, olive for reference lists, grey for archive.

## 7. HTML dashboards and artifacts

- Load `assets/brand-tokens.css`. Paper page ground, navy header bar (logo on white block, program name, last-pull timestamp), white cards with mist borders and 3 pt tier top bars, tables per the CSS, charts per series order.
- Every card shows its source and pull time on hover or in a footer line.
- Force light theme unless every token is redefined for dark.
- Command / executive header views: a KPI strip of at most eight tiles, then the RED list, then the docket, then drill-downs. The header view is what an executive reads in ninety seconds; nothing scrolls above the RED list.

## 8. Email

- Plain text or minimal HTML. No banners, no colored text, no embedded logo images.
- Subject line pattern: `[Program] | [Topic] | [Doc no. or date]`, e.g., `W77 | WKR-40B Mid-Week Executive Update | 09/30/26`.
- Signature block per `skills/csl-client-comms/templates/signature-block.md`.

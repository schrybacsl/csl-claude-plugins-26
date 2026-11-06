# Brand QA Checklist (run before any file is called done)

Record the result in the delivery note as `Brand QA: pass` or list the items that failed and were fixed. A failed item that cannot be fixed (font not installed, logo file unavailable) is stated in the delivery note; the file is issued as a draft, not a release.

## A. Color

- [ ] No occurrence of legacy `#C8102E` (grep the source, the CSS, the pptx XML: `unzip -p file.pptx | grep -i c8102e`).
- [ ] `#BF311A` appears only in the logo and in hairline rules; never as a fill, background, table header, chart series, badge, or text color.
- [ ] Table headers are navy `#0A3173` (black is permitted only in the legacy minutes template).
- [ ] Chart series follow the fixed order navy → dark teal → teal → olive → 60% tints; no other hues.
- [ ] RED / AMBER / GREEN cells use the package status colors and carry the word, not just the color.
- [ ] A greyscale print preview of one content page still communicates tiers and hierarchy.

## B. Typography

- [ ] Font that actually rendered is Avenir Medium / Avenir Next LT Pro / Arial Narrow (`pdffonts file.pdf`; in pptx/docx check `theme1.xml` and run properties). Not Calibri, Helvetica, Times, or a web font.
- [ ] Headers bold, subheaders italic, no underlines except the minutes title.
- [ ] Body ≥ 9 pt print / 13 px screen; tables ≥ 8 pt; captions 7.5 pt.
- [ ] All caps used only for the document type line and the minutes title.
- [ ] Left-aligned text; right-aligned numbers; no justified paragraphs.

## C. Logo

- [ ] Official logo file used (not the CSS fallback) in any issued document.
- [ ] Clear space equal to the box height on all sides; not stretched; on white; not on the client cover color directly.
- [ ] Minimum 0.9 in print / 120 px screen.
- [ ] Present on cover and every running header or footer where the anatomy calls for it.

## D. Identity and provenance

- [ ] "CSL Consulting" on first reference, "CSL" after; legal form "CSL Consulting, LLC" only in contractual context; no "CSL LLC".
- [ ] Document number present and formed per `skills/csl-document-control` (family, sequence, edition letter or revision).
- [ ] Cover metadata complete: Document, Revision, Date issued, Prepared by, Prepared for, Distribution (unless the edition's standing direction omits a line, e.g., no sources note on a specific cover).
- [ ] Source note lists every data pull with sheet name, ID, and timestamp; the "as of" statement is on the last page.
- [ ] Footer carries program name, document number, revision, and page X of Y.
- [ ] File properties (Title, Author, Company, Subject) match the document; no inherited title from a Save-As source.
- [ ] File name matches the naming convention (`csl-document-control`), e.g., `CSL-W77-WKR-40B_2026-09-30.pdf`.

## E. Layout

- [ ] Page size and margins per `document-anatomy.md` for the medium.
- [ ] Section headers have their rule; no orphaned headers at page bottom.
- [ ] Tables do not split a single row across pages; header rows repeat.
- [ ] Charts have finding-style titles and source lines; labels legible at 100%.
- [ ] KPI strip ≤ 6 cards (PDF) / ≤ 8 tiles (dashboard header view).
- [ ] Page count matches the family standard or the deviation is intentional and noted.

## F. Voice (client-executive documents)

- [ ] Bottom line up front on page 2 (first content page).
- [ ] No dash constructions in running prose of the WKR-B / WKR-C families; acronyms spelled out on first use per page.
- [ ] Every finding has item, tier, exposure, owner, action, date.
- [ ] No contractor or vendor explanation stated as fact; positions attributed.
- [ ] Numbers carry units and denominators; dates carry the year where any ambiguity exists.

## G. Accessibility and delivery

- [ ] PDF has a title in metadata and is text-selectable (not an image-only render).
- [ ] Color contrast of text on tier fills meets 4.5:1 (white on RED and GREEN; ink on AMBER and GREY).
- [ ] File size reasonable for email (< 10 MB; compress images at 200 dpi if not).
- [ ] Delivered with: document number, two-sentence summary, next action, and any QA exceptions.

---
name: csl-technical-docs
description: >
  Authoring and auditing controlled technical documents: SOPs in the site convention, CMMS PM task
  packages, multi-party scope packages, engineering assessment reports with a verdict per failure
  mode, facilities and engineering notices (FM- format), equipment watchlists, options menus, and
  naming and turnover conventions; plus audits of others' SOPs (Save-As inheritance, dictionary
  conflicts, RACI gaps, missing appendices). Use it whenever someone says "write an SOP", "PM
  package", "scope this out", "assessment report", "issue a notice", "review this SOP", "Rev 0", or
  "watchlist", or hands over a procedure or report to check.
---

# CSL Technical Documents

A controlled technical document is the owner's instruction to the people who will touch the equipment, price the work, or act on a finding, and it outlives the person who wrote it. This skill defines how CSL, as owner's representative, writes SOPs, PM task packages, scope packages, assessment reports, engineering notices, watchlist workbooks, and options menus so that a technician can execute them without interpretation, a vendor can price them without a call, and a reader eighteen months later can see who approved what and on what basis. It also defines how CSL audits a technical document someone else issued. Numbering per `csl-document-control`; page anatomy and Word styles per `csl-brand` (`references/document-anatomy.md` Section 5, `assets/docx_styles.py`); tiers per `csl-schedule-risk/references/tier-rules.md`; permit content per the installed `sipp` skill and `csl-permits-shutdowns`; the memo that carries an audit finding per `csl-executive-memo`; asset codes and PM record identity per `csl-asset-data-cmms`.

---

## 1. Bottom line / when this runs

| Product | Number form | Runs when | Reviewer and approver |
|---|---|---|---|
| SOP (site convention) | `W77-SOP-PCW-040 Rev 0` | A procedure is new, replaces a legacy one, or a mitigation workstream releases a maintainable state | Client technical reviewer (W77: P. Gorman); client owner approves (W77: B. Gannon) |
| PM task package | `CSL-W77-PM-TRC-001 Rev 0` | An SOP is released and the CMMS needs its PM record | Client data owner for the CMMS record; maintenance provider for craft and duration |
| Scope package | `CSL-W77-SCP-WS04.01 Rev 0` | One piece of work must be priced or executed by more than one party | Client program lead; PMO for the PDS dependency |
| Assessment / technical report | `CSL-W77-ASM-WS02.02 Rev 0` | A workstream needs a verdict on failure modes before it spends money | Client engineering lead; CSL MEP for technical backing |
| Equipment watchlist workbook | Workstream ID and date (`WS-02.01`, 08/06/26) | A population must be ranked before corrective work is planned | Workstream owner |
| Engineering / facilities notice | `FM-W77-UTM-0903 R1` | A condition needs to be on record with evidence and owners (RED (R9) telemetry fires this same day) | Client engineering lead; the CSL PM on site authors |
| Options menu / intake checklist | `CSL-W77-OPT-KPI v1.1` | A stakeholder selects modules for a custom view or intake | Named recipient |
| Audit of a received document | `CSL-<PROG>-MEM-<yymmdd>` | A counterpart's SOP, scope, or report arrives for review or for CSL's signature | Operator; then the document's author in writing |

Which anatomy a request maps to:

| Request as spoken | Product | Section |
|---|---|---|
| "procedure for filter changeout", "write an SOP", "Rev 0" | SOP | 4.2 |
| "PM package", "put it in Planon as a PM", "what does the PM record need" | PM task package | 4.3 |
| "scope this out", "who does what on the boiler copper", "split the scope" | Scope package | 4.4 |
| "assessment report", "is the delta-T problem real", "verdict on the failure modes" | Assessment report | 4.5 |
| "watchlist", "rank the coils", "which units first" | Watchlist workbook | 4.6 |
| "issue a notice", "put the UT results on record" | Engineering / facilities notice | 4.7 |
| "options menu", "intake checklist", "v1.1" | Options menu | 4.8 |
| "review this SOP", "does this draft hold up", "check their procedure" | Audit | 4.9 |
| "turnover naming", "what do we call the O&M files" | Naming and turnover | 4.10 |

Two rules hold across every product: the document control block is the first table and the revision history is the last, and nothing that prints on a label, tag, or contract exhibit is taught in a document before the governing code is confirmed in writing (RED (R8)).

---

## 2. Inputs and pulls

| Input | Where it comes from | QA before use |
|---|---|---|
| Basis documents (vendor letters, test reports, OEM manuals, prior SOPs) | Tracker row attachments (mitigation sheet 2158727850315652), client SharePoint, OEM portals | Dated, numbered, current revision; a letter cited in a scope package is attached to the row it governs (WS-04.01: the water-treatment vendor's 05/14/26 recommendations letter) |
| Drawings and specifications | Client document system; `csl-design-construction-oversight` drawing log | Referenced by number and revision, never by title alone |
| Asset identity | CMMS extract and the delivered code sets (`csl-asset-data-cmms`) | Code confirmed in writing before it appears in a procedure; a provisional code is marked provisional |
| Workstream scope and done-definition | Mitigation sheet row (WS-02.02 defined eight failure modes; WS-12.01 / 12.02 / 12.03 the filter SOPs and PMs) | Pull the row in this session; state the pull time in the References section |
| Permits and isolation | SIPP permit record (`sipp`; sheet 289677048237956) | Permit type, gates, and LOTO points named, not "as required" |
| Measurements | Test reports (MTI UT S-1000, 07/17/26), CTRW telemetry, BMS trends | Instrument, method standard, point count, baseline period, and units stated with every table |
| Roles | `csl-people` for CSL staff; stakeholder register for client and vendor staff | One RACI per document; every R has a role that exists on the project |
| Prior revisions and legacy procedures | `_superseded/` folder; client document system | Supersession named on the new document's face; the legacy number is cited, not reused |

Verbal rulings are recorded as "stated on the call by [name], [date]; written confirmation requested [date]" and never become the baseline of a procedure (csl-operating-rules Section 8).

---

## 3. Method

1. **Fix the number and the control block before writing a sentence.** Reserve the number per `csl-document-control` (grep the outputs folder), then fill Document No., Revision, Title, Author, Technical reviewer, Approver, Date issued (blank until issue), Supersedes, Distribution. Writing into a numbered shell prevents the Save-As defect in 4.1, because the properties and header are set for this document from the start.
2. **Write the done-definition.** One sentence naming the reader (technician, vendor estimator, client executive) and the action the document enables (change a filter, price a scope, approve an action list). Every section either serves that action or is cut.
3. **Collect the basis and list it first.** References with numbers, revisions, and dates; the prior SOPs being superseded; the drawings; the tracker row and its pull time. A reference that cannot be produced is not a reference; it becomes a data gap.
4. **Draft in the anatomy for the type (Section 4).** Keep the section numbers fixed across documents of one type so that reviewers compare like with like and so the PM record can cite "SOP steps 8.4 to 8.9".
5. **Verify every value.** Units, tolerances, part numbers, torque values, set points, valve tags, and durations come from a named source or are labeled illustrative in the draft; illustrative values are removed or sourced before issue. Re-run arithmetic (fill volumes, wall-loss percentages, rates per year) in code.
6. **Route for review and approval and record the dates.** Technical reviewer first, approver second; their names and dates go in the control block, and the review comments are filed with the document. An approver field filled without approval is corrected the same day (`csl-document-control` 7.5).
7. **Render.** Build the Word file with `csl-brand/assets/docx_styles.py` (`new_document`, `add_document_control_block`, `add_heading`, `add_table`, `add_revision_history`, `add_footer`), set the file properties (Title, Subject, Author, Company) to this document, export the PDF alongside, and name both per `csl-document-control` Section 3.
8. **Link the document to the systems it feeds.** An SOP release creates or updates the PM record (W77 filter SOPs: PMs created under WS-12.03 on release); a scope package is attached to its tracker row; a notice is logged and its next review date goes on the docket; an assessment's actions A1 to An become tracker rows with owners.
9. **For a received document, audit before responding.** Run the checklist in 4.9 and `templates/doc-audit-checklist.md`, then write the findings as a memo (`csl-executive-memo`) with dates and document numbers, never as an opinion about the author.

---

## 4. Output specification

### 4.1 Document control block, revision history, file properties (all types)

The first table in the document, in this order: Document No. | Revision | Title | Author | Technical reviewer | Approver | Date issued | Supersedes | Distribution. The revision history is the last table: Rev | Date | Author | Description of change; `Rev 0` reads "First issue" with the supersession named. Footer: `[Doc no.] Rev [n] | CSL Consulting | Owner's Representative` left, page number right.

File properties are part of the record. Set Title, Subject, Author, and Company to this document at creation; a Word file whose properties still carry another document's title and number was made by Save-As and may have inherited headers, definitions, and numbering. Real case: the draft `W77-SOP-GFC-001 Rev 0` (GFC naming SOP) was built by Save-As from `W77-SOP-PCW-040 Rev 0`; its file properties still carried PCW-040's title and number, and its definitions taught the code structure superseded by the 08/24/26 format rulings (Functional Code Structure v1.1). Report such a finding as a record discrepancy, AMBER (A6), in this form: "Draft W77-SOP-GFC-001 Rev 0, received [date]: file properties Title and Subject = W77-SOP-PCW-040 (Save-As inheritance); Section 4 Definitions describes the structure superseded 08/24/26; correction requested in writing [date]; logged in the GFC structure record (CSL-W77-MEM-260919)." If the document would put a superseded code on a label, the tier is RED (R8) until the code is corrected.

### 4.2 SOP anatomy (site convention `<SITE>-SOP-<SYS>-<nnn> Rev <n>`)

Template: `templates/sop.md`. Real examples: `W77-SOP-PCW-040 Rev 0` (40-inch PCW system-filter changeout, cleanroom sections 1 to 4, WS-12.01) and `W77-SOP-PCW-024 Rev 0` (TR7 24-inch point-of-use filter changeout, WS-12.02), both authored S. Schryba / D. Wolf, CSL Consulting, issued 08/04/26 to P. Gorman (ASML) as technical reviewer with B. Gannon (ASML) as approver, superseding the legacy 10-inch procedures, with CMMS PMs to be created under WS-12.03 on release. The legacy format `W77-IRO-SOP-014 Rev 1.0` (cabinet PM / backflushing) stays in circulation under its own number; new SOPs never start in that format (`csl-document-control` 1.2).

| § | Section | Content that makes it complete |
|---|---|---|
| 1 | Purpose | One paragraph: what the procedure achieves and the condition it returns the system to |
| 2 | Scope and applicability | Systems, assets by code, locations (cleanroom sections, rig), and what the SOP does not cover |
| 3 | References | Drawings (number, revision), specifications, OEM manuals (title, document number, date), prior SOPs superseded, the workstream row and pull time |
| 4 | Definitions | Terms and abbreviations used in this SOP only; must agree with the delivered corpus (glossary, code scheme record) |
| 5 | Roles and RACI | One RACI table for the whole document; Engineering present as a role; every step's "who" is a role in this table |
| 6 | Safety | Hazards by step group, PPE, LOTO points by tag, permits required with the SIPP permit type and reference (`sipp`), stop-work conditions |
| 7 | Prerequisites, materials, tools, parts | Part numbers, quantities, consumables, calibrated instruments with ranges, spares-on-hand check, communications to the rig or area owner |
| 8 | Procedure | Numbered steps; each step = action, expected result, verification or hold point, who; one instruction per step |
| 9 | Acceptance criteria and return to service | Measurable criteria (differential pressure, leak check duration, flow), who signs, what "in service" means |
| 10 | Records | What is logged, where (checklist appendix, CMMS PM record), and the PM linkage (record fields, SOP number and steps cited) |
| 11 | Appendices | A checklist, B drawings and P&ID excerpts by number and revision, C photos with asset codes and dates |
| — | Revision history | Last table |

Section 5 RACI shape (one table; assignments below are illustrative for a point-of-use filter changeout):

| Activity | Client system owner | Engineering | FM lead | FM technician | Owner's rep (CSL) | Rig or area owner |
|---|---|---|---|---|---|---|
| Release the window and permit | A | C | R | I | C | R |
| Isolate and verify zero energy | I | I | A | R | C | I |
| Changeout steps 8.3 to 8.6 | I | C | A | R | I | I |
| Leak check and return to service | A | C | R | R | C (witness) | I |
| Records and PM closure | A | I | R | R | C | I |

Section 6 Safety shape:

| Hazard (step group) | Control | PPE | Permit / LOTO | Reference |
|---|---|---|---|---|
| Pressurized housing (8.1 to 8.3) | Isolate, vent, and read 0 psig before opening | Safety glasses, gloves, face shield at the vent | SIPP permit (type per `sipp`); locks on V-101 / V-102 (illustrative tags) | Site LOTO procedure number and revision |
| Water release in a cleanroom section (8.3, 8.7) | Containment and approved drain; spill kit staged | Per site cleanroom protocol | Area owner notified in step 8.1 | Cleanroom protocol number |

### 4.3 PM task package anatomy (`CSL-<PROG>-PM-<sys>-<nnn> Rev <n>`)

Template: `templates/pm-task-package.md`; W77 series `CSL-W77-PM-TRC-001`, `-002`. One package per PM, in this order: asset(s) and functional codes | PM title | frequency or trigger (calendar, run-hours, condition) | craft and headcount | estimated duration | safety and permits | parts and consumables with part numbers | tools and instruments | procedure reference (SOP number, revision, and step range) | acceptance and record fields | CMMS PM record fields | go-live checklist.

CMMS PM record fields for Planon, with the values a package carries (TR7 filter PM under WS-12.03; frequency and duration illustrative until the OEM interval and the first timed changeout are on record):

| Planon field | Value in the package |
|---|---|
| PM name | TR7 24-inch POU filter changeout |
| Asset | Functional code of the TR7 POU filter housing, as confirmed in writing by the client data owner; "provisional" until then, and no record created while provisional |
| Frequency | Quarterly, or on differential pressure at 8.0 psid, whichever first (illustrative) |
| Standard duration | 2.0 hours, two technicians (illustrative) |
| Instructions | "Execute W77-SOP-PCW-024 Rev 0, steps 8.1 to 8.8; record dP, part number, lot" |
| Linked SOP document number | W77-SOP-PCW-024 Rev 0 |

Go-live checklist: SOP at issued revision and linked; asset code confirmed in the CMMS, not a placeholder; PM record created with first due date; parts in stores or on order with part numbers; craft and provider assigned (IFM 2.0 transition noted where the provider is changing); permit template referenced; record fields defined; handover to the maintenance provider recorded with a date. A PM created against a provisional code is a RED (R8) item because the code will print on the label and the work order.

### 4.4 Scope package anatomy (`CSL-<PROG>-SCP-<WS> Rev <n>`)

Template: `templates/scope-package.md`. Real example: `CSL-W77-SCP-WS04.01 Rev 0`, issued 08/14/26, boiler copper replacement for Boilers 3 and 5. Basis document: the water-treatment vendor's 05/14/26 recommendations letter, attached to the tracker row. Standing direction recorded in the package: the named valve vendor is not to be used on this scope; Vanderweil specifies. Dependency: PMO approval of the PDS before pricing is committed.

| § | Section | Content |
|---|---|---|
| 1 | Bottom line and decision requested | What is being scoped, who is asked to decide what, by when |
| 2 | Basis documents | Number, date, author, where attached |
| 3 | Background and condition | The condition and its evidence in one page |
| 4 | Scope by party | Table: party, scope, deliverable, exclusions, pricing basis (lump sum, T&M, OPEX) |
| 5 | Interfaces and sequencing | Who hands what to whom, in what order, with the hold points |
| 6 | Constraints | Shutdown windows, permits, long-lead items, standing directions (vendor exclusions) |
| 7 | Deliverables and acceptance | Per party: what is delivered, who accepts, criteria |
| 8 | Schedule assumptions | Dates the pricing assumes; what moves them |
| 9 | Commercial path | CAAR / PO route, proposal-to-PO step, tracker row (`csl-cost-change-control`) |
| 10 | Open items and approvals | Open-confirm rows with asked dates; approval block |

Section 4 as issued for WS-04.01 (exclusions and pricing basis columns as the package framed them):

| Party | Scope | Deliverable | Exclusions | Pricing basis |
|---|---|---|---|---|
| Water-treatment vendor | Chemistry program for Boilers 3 and 5 through and after the replacement | Chemistry recommendations and monitoring plan | Materials and installation | OPEX, existing service agreement |
| Vanderweil (engineering) | Specify the replacement copper; piping connection details | Specification and connection sketches by drawing number | Installation, chemistry | Engineering proposal against the PDS |
| MMI (installation) | Install per the Vanderweil specification | Installation pricing; schedule with shutdown windows | Design, chemistry, sampling | Lump sum against the specification |
| FM contractor | Sampling before and after | Sample results to the water-treatment vendor and CSL | Design, installation | Existing FM scope |

### 4.5 Assessment report anatomy (`CSL-<PROG>-ASM-<WS> Rev <n>`)

Template: `templates/assessment-report.md`. Real example: `CSL-W77-ASM-WS02.02 Rev 0`, 20 pages, issued 08/06/26. Verdict vocabulary per failure mode, fixed: **CONFIRMED PRESENT** / **PROBABLE, unverified** / **NOT SUPPORTED**.

| § | Section | Content |
|---|---|---|
| 1 | Bottom line | One table: failure mode, verdict, confidence, the one action it drives |
| 2 | Scope and done-definition | The eight failure modes the workstream defined; what "assessed" means for each |
| 3 | Method and evidence sources | Walk-downs, trends, CMMS history, interviews by role, drawings; pull times |
| 4 | Findings per failure mode | Evidence, confidence, what data would change the verdict |
| 5 | Principal finding | WS-02.02: low delta-T as the common pathway, produced by air binding, waterside fouling, 3-way mixing valves, and sub-2-fps branch velocity |
| 6 | Triage rule for the field | Record coil delta-T, CHW supply temperature at the coil, and zone flow before assigning a complaint to a cause |
| 7 | Actions | A1 to A6: action, owner, due date, data-dependency flag ("needs no CMMS data, can start now" separates actions from the migration) |
| 8 | Data gaps | What was not available, from which source, and what closes it |
| 9 | References | Numbers, revisions, dates |
| — | Appendices | Trend plots, walk-down sheets, photos with asset codes |

Verdict row form (values illustrative): `3-way mixing valves at terminal coils | CONFIRMED PRESENT | High (drawings + walk-down) | A3: HX replacement scope (WS-22.08)`. Every action becomes a tracker row that cites the report number.

### 4.6 Equipment watchlist workbook (WS-02.01, 08/06/26)

Excel, six tabs, Control sheet first per `csl-brand` Section 5:

| Tab | Columns | Purpose |
|---|---|---|
| Control | Document number, source pulls with IDs and timestamps, column dictionary, change log | Provenance |
| Ranked watchlist | Asset, functional code, zone, RPN (S × O × D), tier with rule ID, failure modes flagged, next action, owner | What gets looked at first |
| Full population by zone | Every asset in scope, zone, service, age, last corrective WO | Denominator for every percentage |
| Failure-mode matrix | Assets × the eight failure modes; cell = evidence code (observed / trend / history / none) | Traceability from verdict to asset |
| Corrective-WO query spec | CMMS fields, filters, date range, export format the maintenance provider runs | Repeatable pull |
| Data gaps | Missing nameplate, trend, or history per asset; source; owner | Feeds the walk-down list |

Tier cells use the status colors (`csl-brand` 1.4), never CSL Red; RPN arithmetic is re-run in code before issue.

### 4.7 Engineering / facilities notice (`FM-<AREA>-<TOPIC>-<mmdd> R<n>`)

Template: `templates/engineering-notice.md`. `mmdd` is the condition date, not the issue date; `R<n>` updates the same notice; a new notice states what it supersedes on its face. Real examples: `FM-W77-UTM-0903 R1` (full UT data set) and `R2` (adds the communication timeline and Q&A), superseding `FM-W77-UTM-0819`; `FM-DUV-LOG-0828`. Authored by the CSL PM on site (D. Wolf).

| Element | Rule |
|---|---|
| Status line | One of Information / Action Required / Escalation; Escalation when a RED rule fired |
| Affected systems | System tags and areas served |
| Condition | What was found, when, by whom, by what method |
| Evidence | Measurement tables with instrument, standard, point count, baseline period, units |
| Risk statement | What the data supports and what it does not; no inferred failure date |
| Codes and standards | The evaluation basis by number |
| Recommended actions | Action, owner, due date |
| Next review date | On the face |
| Supersedes | The earlier notice number |

UTM-0903 evidence as issued: ASTM E797 ultrasonic thickness, 16 points, 297-day baseline (MTI report S-1000, 07/17/26); 11 of 15 carbon-steel locations below lower manufacturing tolerance; worst location 0.38 mm/yr; 18-inch mains 36 to 37% below nominal if schedule 40 is confirmed (open data gap). Risk statement as issued: no failure date is assignable from the data; a credible short-term leakage risk exists. Codes: ASME B31.9; API 579-1/FFS-1. A wall-loss reading below manufacturer lower tolerance is RED (R9) and the notice goes out the same day; client direction to de-escalate is recorded and the item is held at AMBER with the R9 rule still cited and a review date on the face (`tier-rules.md` 2.5).

### 4.8 Options menu / intake checklist (`CSL-<PROG>-OPT-<topic> v<n.n>`)

Two pages: page 1 the checklist (modules coded A1…E6, one line each with a tick box), page 2 the build sheet (selected modules, data sources, refresh cadence, recipient). Version strings, not revisions, because the document iterates weekly; every version change is recorded on the build sheet ("v1.1: G3 corrected from CARR to CAAR", `csl-document-control` 2.7). Module content is owned by `csl-dashboard-kpi`; this skill governs the document form.

### 4.9 Audit of a received technical document

Checklist (`templates/doc-audit-checklist.md`), run in this order because each check scopes the next:

| Check | Test | Finding form |
|---|---|---|
| File properties | Title, Subject, Author, Company, created and modified dates against the control block | "Properties carry [other doc]; Save-As inheritance" |
| Supersession | States what it supersedes; the superseded document is the one actually in circulation | "Supersedes line absent; legacy [number] still circulating" |
| Dictionary versus delivered corpus | Definitions and examples against the glossary, the code scheme record, and issued SOPs | "Section 4 defines [term] contrary to [ruling, date]" |
| RACI | Exactly one; every step's "who" appears in it; Engineering present | "Two RACIs (§5 and §8) disagree on [activity]" |
| Appendices and references | Every cited appendix, drawing, form exists at the stated revision | "Appendix B cited, not attached" |
| Examples versus current ruling | Worked examples produce the structure the written ruling produces | "Example code [x] follows the pre-08/24/26 structure" |
| Review and approval evidence | Names, dates, comments on file | "Approver field filled; no approval on record" |

Findings go in a memo per `csl-executive-memo` (`CSL-<PROG>-MEM-<yymmdd>`): Bottom line, Findings numbered with tier and rule (AMBER (A6) for record discrepancies; RED (R8) when a label or work order would inherit the defect), Recommended actions with owner and date, Basis. Describe every finding as a record discrepancy with documents and dates.

### 4.10 Naming and turnover conventions

- Document numbers and file names per `csl-document-control` Sections 1 and 3; the CSL number stays inside the document when a client tenant convention names the file (W77: `Enterprise_Site_Building` + project + discipline + document type).
- SOP system codes (`PCW`, `GFC`) are assigned once per system family and reused; sequence numbers are never reused after supersession.
- Turnover packages carry data and drawings, not only PDFs: the asset list with confirmed functional codes, the drawings by number and revision, the O&M manuals named `<Doc no.>_<yyyy-mm-dd>_<descriptor>`, and the SOPs and PM packages at issued revision. Index per `csl-design-construction-oversight/templates/turnover-package-index.md`.
- Every turnover file states which naming convention it was built to and the date of that convention, because W77's client-side convention is still being written into future contracts.

---

## 5. Voice and formatting rules

- Numbered headings (1., 1.1) in SOPs, packages, and assessments; the section numbers in Section 4 are fixed per type.
- One instruction per step; imperative verb first ("Close V-101"); expected result and verification on every step; a hold point is a row, not an adjective.
- Units and tolerances on every value ("0 psig ± gauge tolerance", "≤ 2.0 psid clean"); part numbers for every part; drawings by number and revision.
- No "as required", "as needed", "periodically", or "appropriate PPE"; write the quantity, interval, or item.
- Plain voice for anything a technician reads: short sentences, no shorthand a new hire would have to decode; spell out on first use.
- Roles, not names, inside procedure steps; names in the control block and RACI.
- Tables for steps, parts, RACI, evidence, actions; prose for purpose, condition, and reasoning.
- Photos and figures carry the asset code, date, and orientation; drawing excerpts carry number and revision.
- Render Word with `docx_styles.py` (CSL H1 navy bold, CSL H2 dark teal italic, navy table headers, zebra rows in mist); PDF alongside; both named per `csl-document-control` Section 3; file properties set.
- Dates MM/DD/YY in the body; ISO in file names; time zone stated once (ET on W77).
- Illustrative values in a draft are labeled "(illustrative)" and removed or sourced before issue.

Rendering recipe (the helper sets Letter, 0.75 in margins, and the CSL styles; the properties block is what defeats Save-As inheritance):

```python
from docx_styles import new_document, add_document_control_block, add_heading, add_table, add_revision_history, add_footer
doc = new_document()
add_document_control_block(doc, {"Document No.": "W77-SOP-PCW-024", "Revision": "0",
    "Title": "TR7 24-inch Point-of-Use Filter Changeout (WS-12.02)",
    "Author": "S. Schryba / D. Wolf, CSL Consulting", "Technical reviewer": "P. Gorman, ASML",
    "Approver": "B. Gannon, ASML", "Date issued": "08/04/26",
    "Supersedes": "Legacy 10-inch point-of-use filter procedure", "Distribution": "per transmittal"})
add_heading(doc, "8. Procedure", level=1)
add_table(doc, [["Step", "Action", "Expected result", "Verification / hold point", "Who"], ["8.1", "...", "...", "HOLD: ...", "FM technician"]])
add_revision_history(doc, [("0", "08/04/26", "S. Schryba / D. Wolf", "First issue; supersedes the legacy 10-inch procedure")])
add_footer(doc, "W77-SOP-PCW-024 Rev 0 | CSL Consulting | Owner's Representative")
cp = doc.core_properties; cp.title = "W77-SOP-PCW-024 Rev 0 TR7 24-inch POU Filter Changeout"
cp.subject = "W77-SOP-PCW-024"; cp.author = "S. Schryba, CSL Consulting"; cp.keywords = "SOP; PCW; WS-12.02"
# Company is an app property (docProps/app.xml), not a core property: set it in Word or patch app.xml after save
doc.save("W77-SOP-PCW-024_Rev0_2026-08-04.docx")   # then export the PDF with the same stem
```

---

## 6. Worked example: SOP excerpt

Document control block, `W77-SOP-PCW-024 Rev 0`, as issued (Distribution row illustrative):

| Field | Value |
|---|---|
| Document No. | W77-SOP-PCW-024 |
| Revision | 0 |
| Title | TR7 24-inch Point-of-Use Filter Changeout (WS-12.02) |
| Author | S. Schryba / D. Wolf, CSL Consulting |
| Technical reviewer | P. Gorman, ASML |
| Approver | B. Gannon, ASML |
| Date issued | 08/04/26 |
| Supersedes | Legacy 10-inch point-of-use filter procedure |
| Distribution | B. Gannon, P. Gorman (ASML); D. Wolf, N. Grubler, E. Hubert (CSL); FM maintenance lead (illustrative) |

Section 8 Procedure, steps 8.1 to 8.8 (valve tags, part number, torque, and pressure values are illustrative; the issued SOP carries the values from the OEM manual and the P&ID):

| Step | Action | Expected result | Verification / hold point | Who |
|---|---|---|---|---|
| 8.1 | Confirm the SIPP permit is active and the rig owner has released TR7 for the window; close inlet valve V-101 and outlet valve V-102; apply locks and tags | Both valves closed, locked, tagged; permit number on the checklist | HOLD: FM lead and CSL witness initial the checklist | FM technician; FM lead; CSL witness |
| 8.2 | Open vent valve V-103; read housing gauge PI-101 | 0 psig ± gauge tolerance within 2 minutes | Record PI-101 reading and time | FM technician |
| 8.3 | Open drain valve V-104 to the approved floor drain; capture volume | Housing drains fully; approximately 40 L (illustrative) | Record volume; confirm no water outside the containment | FM technician |
| 8.4 | Remove housing bolts in a star pattern; lift the bowl; remove the spent element; bag and label it with asset code, date, and technician initials | Element removed intact; bag labeled | Photo of the spent element (Appendix C) | FM technician |
| 8.5 | Inspect the housing O-ring and seat; replace the O-ring; install the new element, part no. PCW-24-POU-E1 (illustrative), oriented per the OEM arrow | New element seated; new O-ring in place | Part number and lot recorded on the checklist | FM technician |
| 8.6 | Reinstall the bowl; torque bolts to 25 ft·lb (illustrative) in a star pattern in two passes | All bolts at torque | Torque wrench serial and reading recorded | FM technician |
| 8.7 | Close V-104; crack V-101 to fill; vent through V-103 until a steady stream shows; close V-103; hold 5 minutes | No air; no visible leak at the housing joint after 5 minutes | HOLD: leak check witnessed and initialed | FM technician; CSL witness |
| 8.8 | Open V-102; return TR7 to service; read differential pressure across the housing at steady flow | ≤ 2.0 psid clean-filter baseline (illustrative) | Record dP, flow, time; enter the PM record fields in Section 10 | FM technician; rig owner notified |

Records (Section 10): checklist Appendix A retained with the permit; CMMS PM record (created under WS-12.03 on release) closed with dP, part number, lot, technician, and the SOP number and revision cited. Revision history: `0 | 08/04/26 | S. Schryba / D. Wolf | First issue; supersedes the legacy 10-inch point-of-use procedure`.

---

## 7. Failure modes and how to avoid them

| Failure | What it looks like | Avoidance |
|---|---|---|
| Save-As inheritance | Properties, header, or definitions from the source document survive in the new one | Number and control block first; set properties at creation; check `Title` and `Subject` before issue |
| Verbal ruling taught as standard | An SOP or naming guide fixes a structure that was only stated on a call | Cite the written ruling by document and date; mark anything verbal as "written confirmation requested [date]" |
| Two RACIs | A document-level RACI and a step-level one that disagree | One RACI; steps cite roles from it |
| "As required" steps | Steps with no quantity, interval, or verification | Every step carries action, expected result, verification, who |
| Unsourced values | Torque, pressure, or part number typed from memory | Named source per value; illustrative label in drafts; strip before issue |
| Missing appendix | The procedure cites a checklist or drawing that is not attached | Appendix list checked against citations before issue |
| Scope package without a decision | A description of the problem with no request | Section 1 names the decision, the decider, and the date |
| Assessment without verdicts | Findings prose with no per-failure-mode call | Verdict table first, fixed vocabulary |
| Notice without owners or review date | A condition reported and left | Every recommended action has an owner and a date; next review date on the face |
| Notice dated by issue | `mmdd` in the number is the day it was sent | `mmdd` is the condition date; the issue date sits in the body |
| PM created on a provisional code | Work orders and labels carry a code that later changes | Code confirmed in writing first (RED (R8) otherwise) |
| Version and revision confused | An SOP at "v1.1" or an options menu at "Rev 2" | `Rev <n>` for controlled documents; `v<n.n>` for living documents |
| Superseded document still circulating | Two procedures for one task on the floor | Supersession on the new face; old file moved to `_superseded/`; distribution list told |
| PDF missing | Word file issued alone; reviewers see reflowed tables | PDF alongside, both named per `csl-document-control` |
| Audit written as opinion | "Sloppy draft" | Record discrepancies with document numbers and dates; memo form |

---

## 8. Pre-issue checklist

- Number reserved and formed per `csl-document-control`; revision marker present; supersession named.
- Document control block first, complete; revision history last; footer correct.
- File properties (Title, Subject, Author, Company) set to this document; checked, not assumed.
- Section numbering matches the type's anatomy; one RACI; Engineering present as a role.
- Every step: action, expected result, verification or hold point, who; no "as required".
- Every value sourced; units and tolerances present; part numbers present; illustrative labels removed.
- References by number and revision; every cited appendix, drawing, and form attached.
- Permits and LOTO named with the SIPP reference; safety section reviewed against `sipp`.
- Tiers carry rule IDs; RED (R8) and RED (R9) items flagged in the delivery note.
- CMMS or tracker linkage stated (PM record fields; tracker row; docket entry for the next review date).
- Reviewer and approver names and dates recorded; comments filed.
- Rendered with `docx_styles.py`; PDF alongside; file names per Section 3 of `csl-document-control`; brand QA run (`csl-brand`).
- No health, HR, or personal content; disputes described as record discrepancies with dates.

---

## Files in this skill

- `templates/sop.md` — SOP skeleton in the site convention with the eleven numbered sections, control block, RACI, safety table, step table, and revision history.
- `templates/pm-task-package.md` — PM task package skeleton with the Planon PM record fields and the go-live checklist.
- `templates/scope-package.md` — scope package skeleton with the scope-by-party table and the WS-04.01 example rows.
- `templates/assessment-report.md` — assessment report skeleton with the verdict table, per-failure-mode finding block, triage rule, and action register.
- `templates/engineering-notice.md` — FM-format notice skeleton with the evidence table, risk statement, and supersedes line.
- `templates/doc-audit-checklist.md` — the received-document audit checklist and the memo form for findings.

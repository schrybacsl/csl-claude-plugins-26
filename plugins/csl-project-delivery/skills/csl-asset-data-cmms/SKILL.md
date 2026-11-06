---
name: csl-asset-data-cmms
description: >
  Asset register building and CMMS migration (Planon, CHAMPS, Maximo): functional and asset code
  schemes, parent master lists and hierarchies, upload sheets on the client's unaltered templates,
  reconciliation to legacy extracts, New Asset Form intake, QR tagging gates, open-confirm
  registers, the weekly program summary and gate register, data-quality metrics, and import-failure
  triage. Use it whenever someone says "upload sheet", "asset list", "functional code", "PML",
  "Planon", "CHAMPS", "QR tags", "walk-down", "reconcile to the extract", "why did the import fail",
  or "can we print the tags yet", and every Friday for the program summary.
---

# CSL Asset Data and CMMS Migration

An asset register migration decides what the maintenance provider will see, route, and print for the next decade, and the owner pays for every code that changes after it goes live or onto a label. This skill defines how CSL builds asset registers and code sets, populates the client's import templates without altering them, reconciles to the legacy system, controls revisions, delivers with evidence, verifies what went live, gates physical tagging, and reports the program weekly. The W77 Planon / CHAMPS migration (about 2,000 active assets across six buildings; CSL scope mechanical/HVAC and loops since 08/24/26; hard deadline 10/30/26 for the Loops and AHS hierarchy ahead of the IFM 2.0 maintenance-provider transition) is the worked case; the method is general. Numbering and client-mandated import names per `csl-document-control`; workbook anatomy per `csl-brand` Section 5; tiers per `csl-schedule-risk/references/tier-rules.md`; SOP and PM linkage per `csl-technical-docs`; the Friday editions feed `csl-weekly-reporting`; record corrections per `csl-client-comms`; Planon record packaging per the installed `planon-doc-generator` skill.

---

## 1. Bottom line / when this runs

| Product | Number or name | Cadence | Reader |
|---|---|---|---|
| Populated client import template (xlsx) + copy-paste-ready CSV | Client template name + date + `_R<n>` (`ASML_W77_..._August_24_2026_R3.csv`); CSL reference `CSL-<PROG>-UPL-<yymmdd> R<n>` on the companion Control sheet | Per delivery | Client data owner (imports) |
| Segment-builder workbook (code set) | `v_<n>` living version with Control sheet | Per revision | Client data owner; CSL team |
| Reconciliation workbook | Same delivery, `Reconciliation` tab | Per delivery | Client data owner |
| New Asset Form batch | One sheet per upload + master; IN number cited | Per intake | Client data owner; loops owner |
| Weekly program critical summary | `CSL-<PROG>-PLN-SUM-<yymmdd> R<n>` | Friday | Client program lead; CSL Project Director |
| End-of-week gate register edition | `CSL-<PROG>-PLN-EWO-<yymmdd>` | Friday | Same |
| Open-confirm register | Section of PLN-SUM; standalone when asked | Weekly | Client data owner |
| Code scheme record | `references/code-scheme-record.md` maintained as a dated record | On every ruling | Anyone coding |

Which product a request maps to:

| Request as spoken | Product | Section |
|---|---|---|
| "upload sheet", "populate the template", "the CHAMPS file" | Client template + Control sheet | 3.5, 4.1 |
| "functional code", "GFC", "what's the code for", "segment builder" | Code set and scheme record | 3.4, 4.2 |
| "reconcile to the extract", "is it in CHAMPS", "double-listed" | Reconciliation | 3.3 |
| "New Asset Form", "IN 12491", "intake" | Intake batch | 4.5 |
| "loops hierarchy", "PML", "parent list" | Loop / system hierarchy | 4.4 |
| "QR tags", "can we print", "walk-down" | Tagging gates | 3.9 |
| "why did the import fail", "rejected" | Import triage | 4.10 |
| "how many have we delivered", "Friday summary", "EWO" | PLN-SUM / PLN-EWO | 4.6, 4.7 |

Absolute rules (csl-operating-rules Section 6, trigger 9): nothing prints on a label or tag before its governing code and structure are confirmed in writing, RED (R8) otherwise; and a client template is never renamed, re-columned, or "cleaned", because the stated import root cause on W77 (09/29/26) was "any change and they will not upload".

---

## 2. Inputs and pulls

| Source | What it gives | QA before use |
|---|---|---|
| Roadmap Master (W77: Smartsheet 1059284113641348) | Equipment rows by E-GRP; the 335-row mechanical pull behind v_4 | Full-sheet pull, filter locally; parent/child rows separated; pull time recorded |
| Panel lists, drawings extractions, mitigation trackers | Electrical (426 panels, Panel List Rev2), single-line extractions, WS rows naming assets | Source, revision, and date on every row carried in |
| Legacy CMMS extract (W77: CHAMPS Total Combined Assets, 2,645 records) | Active records, legacy codes, status, placeholders | Hash the file; record extract date; never edit the extract, join to it |
| Client templates (W77: six CHAMPS templates: Process / Multi-Asset / Standard Asset, each IMP and Update; CSL held one) | Column set, required fields, auto-populate machinery | Kept byte-identical except for data rows; which template a file was built on is stated on the Control sheet |
| Written rulings (format, scope, structure) | The convention in force by date | Verbal rulings marked as such with the written-confirmation request date |
| Cooling Loop Utility Matrix | 16 numbered systems across 18 loop columns; sub-loops; POU segments | Version and date; tower and condenser circuits outside the closed-loop matrix noted |
| New Asset Forms via the client DMS | Assets outside the bulk upload (IN 12366, 12491, 12548 batches) | IN number as issued; nameplate fields counted before coding |
| Walk-down sheets and photos | Nameplate data, field tags, collisions | Asset code, date, and location on every sheet |
| Share log, transmittals, import rejection logs | Evidence of delivery and of what the importer rejected | Timestamps kept; rejection log requested for every failed import |

---

## 3. Method

Ten phases; each ends in something the owner learns or must decide.

### 3.1 Scope ruling in writing

Get the scope in a dated written ruling before coding: which taxonomies and systems are in (W77, 08/24/26: mechanical/HVAC plus loops; electrical done in-house by the client; roof PML already in Planon), which are excluded (hot-water and potable loops: the Loops PML covers 17 of 18 loops, excluding HW heat), and which families are deferred (doors, taxonomy 13, and the board taxonomies 13-down after gases and plumbing). A scope ruling given on a call is recorded as verbal with the confirmation request date; coding to it is a failure mode (Section 7). The owner learns what the deliverable will and will not contain.

### 3.2 Source census

List every source that names an asset in scope, with row counts, dates, and hashes. The census is the denominator for every later percentage and the answer to "where did this record come from".

| Source (W77 mechanical) | Rows | Date / pull | Used for |
|---|---|---|---|
| Roadmap Master 1059284113641348, equipment rows by E-GRP | 335 (mechanical pull) | Pull time on the Control sheet | Unit population behind v_4 and v_5 |
| CHAMPS Total Combined Assets extract | 2,645 | Extract date and hash on the Control sheet | Legacy join; Active / placeholder status |
| MEP list R0 | 672 | 08/06/26 | First census product; the 672 line of the delivered total |
| Panel List Rev2 (3077374458417028) | 426 panels | Per pull | Electrical, done in-house by the client; census only |
| Mitigation sheet 2158727850315652 | WS rows naming assets | Per pull | Assets a workstream touches (WS-22.08 valves, WS-12 filters) |
| Cooling Loop Utility Matrix | 16 systems / 18 loop columns | Version and date | Loop parents and associations |

### 3.3 Reconciliation

Join the census to the legacy extract on the legacy code, then on name, then on location, and classify every row (method in `references/reconciliation-method.md`): Active with code | Active without code | Not in legacy | Double-listed | Code defect. W77 patterns and their dispositions:

| Pattern | W77 instance | Disposition |
|---|---|---|
| Double-listing originating in the source | SE05–10 versus Smoke Exhaust 05–10; AHU15ERV / AHUERV15 resolved to a single CHAMPS record | One record kept; the other listed as a merge on the confirm register |
| Tag collision | Two pumps both field-tagged TCWP-1 at W59; provisionally TCWP01 / TCWP02 | Must resolve in writing before QR prints (RED (R8) if a print is scheduled) |
| Placeholder record | BFP01 (Watts LF009 RPZ) versus DCW_BFP01 NEW-Placeholder in CHAMPS | Code-path ruling plus merge; placeholder never counted as Active |
| Code defect | SCHWP06 record carrying CHW01_PMP05, duplicating SCHWP05 | Corrected in the code set; defect reported to the data owner with the record IDs |
| Dangling parent | HEX3 / HEX4 condenser-water pumps coded under HEX3 / HEX4 with no HEX records | Parent records added (v_5: HEX03 / HEX04, CDP03 / CDP05) |
| Nameplate gap | 21 of 32 slurry-machine rows lacking nameplate data; forms with zero commissioning dates | Walk-down items list with the IN number; row held, not guessed |

Each pattern becomes an open-confirm row or a walk-down item. The owner learns how much of the register is clean and what blocks the rest.

### 3.4 Code scheme application

Build a segment-builder sheet: one column per level of the scheme, an assembled-code column built by formula, then validation columns (format pass, uniqueness, instance padding, parent exists, child token in the allowed list). The W77 scheme and every dated ruling are in `references/code-scheme-record.md`; the elements in force:

| Element | Ruling | Date and status |
|---|---|---|
| Published scheme | Six-level V1.0 `Enterprise_Site_Bldg_System_Equipment_Device` | Published; depth since ruled four ways |
| Prefix and separators | `ASML_WLT_077_` with underscores; no building letter | 08/24/26, written (Functional Code Structure v1.1) |
| Reset point | Code resets at the unit: `ASML_WLT_077_AHU22N` | 08/24/26, written |
| Children | `<unit>_PUM01`, `<unit>_sensor01` | 08/24/26, written; pump token open |
| Loop association | A column on the record, not a code segment or parent prefix | 08/24/26, written |
| Legacy grouping codes | Numeric grouping codes dropped | 08/24/26, written |
| Spaces | Required on every record for work-order routing | 08/24/26, written |
| Fan-family child tokens | EXF (exhaust) / RDF (redundant) / SEF (smoke exhaust) | Recorded with the v_3 R2 fan recodes |
| Structure depth | Six levels 08/24/26; extended past six 09/10/26; eight levels verbal 09/22/26; "up to seven" 09/29/26; no versioned spec | OPEN |
| Open tokens | PUM versus PMP / CWP; FAN as a level-2 code; 2-digit versus 3/4-digit instance padding | OPEN |

Treat depth as OPEN, build every code set to the convention in force on its issue date, and state that convention on the file's Control sheet. The owner learns which codes are stable and which are exposed to the next ruling.

### 3.5 Client template population, template unaltered

| Do | Do not |
|---|---|
| Keep the client's file name pattern and append `_R<n>` | Rename the file to a CSL number (the CSL number goes on the companion Control sheet) |
| Paste values into the data rows only | Add helper columns, notes columns, or a Control sheet inside the client file |
| Leave headers, column order, sheet names, hidden columns, and auto-populate (standard-asset, taxonomy) machinery as received | "Clean" headers, unhide and delete, or overwrite formula columns with values |
| Work in the segment builder; paste at the end | Build the code set inside the template |
| State which of the client's templates (Process / Multi-Asset / Standard Asset; IMP or Update) the file uses | Assume the one template CSL holds fits every record class |
| Byte-compare the template structure (headers, sheet names) against the pristine copy before delivery | Deliver from memory |

Root cause on record for the W77 import failures, stated 09/29/26: "any change and they will not upload" (attribute to the speaker in that day's record). The owner learns that the file will import, or why it did not.

### 3.6 Revision control

`R0` is the first issue; every reissue increments and the Control sheet change log states what changed and the delta in rows. W77 delivered sets (record in 4.3): MEP list R0 → R3 (08/06/26 to 08/24/26); mechanical R4 → v_5 (08/24/26 to 08/26/26). Never overwrite an issued file; move it to `_superseded/` (`csl-document-control` Section 2). The owner learns which file is current and what the last revision fixed.

### 3.7 Delivery with evidence

Share with edit access from the client tenant, email the transmittal, and keep the share log entry (timestamp, recipients) with the transmittal register: W77 mechanical template delivered Wed 08/26/26 3:22 PM ET to B. Gannon and T. Dube (ASML) and N. Grubler and E. Hubert (CSL) with a copy-paste-ready CSV alongside the xlsx (`CSL-W77-TRN-260826-01`). The evidence is what settles "we never got it" and "that was work in progress" (`csl-document-control` Section 5). The owner learns the delivery is provable.

### 3.8 Post-import verification

After the client imports, pull what went live and compare it to what was delivered; once a record is live its primary key is untouchable, so every later change is an Update-template transaction, never a re-import.

| Check | Delivered versus live | Finding form |
|---|---|---|
| Record count | Rows delivered against records created | "237 delivered; <n> live; <n> rejected per the log of <date>" |
| Codes | Assembled code string-equal on every record | "<n> records live with a code differing from the delivered set (list)" |
| Status values | Status vocabulary as expected | W77: "completed" versus "tested complete" on imported records, reported as a status-vocabulary finding, AMBER (A6) |
| Space and cost center | Present on every live record | "<n> live records without space; work-order routing blocked" |
| Parents and associations | Parent exists; loop column populated | "<n> children live with no parent record" |
| Standard asset / taxonomy | Auto-populated fields filled | "<n> records with blank standard asset after import" |

The owner learns what is actually in the CMMS.

### 3.9 Gates before physical tagging

All of the following in writing before a single label prints, RED (R8) if breached:

| Gate | Evidence required | Why |
|---|---|---|
| Functional code will not change when system relationships are layered in later | Written confirmation from the client data owner citing the structure spec version | The code prints on the label; a change means reprinting and re-walking, and that cost is stated in the hold request |
| Tag collisions resolved | Ruling on TCWP-1 at W59 (TCWP01 / TCWP02) | Two assets, one tag, no routing |
| Placeholder merges ruled | BFP01 / DCW_BFP01 disposition | A merged record after printing orphans a label |
| Label stock and printer readiness | Stock count and test print (a ribbon logjam stopped a run once) | Readiness is a gate, not an assumption |
| Tagging sequence and split of responsibility | Central plant → roof → tool areas; CSL / FM PMs by area | Crews and escorts scheduled to the sequence |
| Provider cycle alignment | Direction on whether tagging rides the maintenance provider's PM cycles | Avoids a second walk when the client so directs |

The owner learns whether printing is safe this week.

### 3.10 Weekly program summary and gate register

Every Friday: PLN-SUM (bottom line, delivered-to-date by file, open-confirm register, import status, intake line, next deliveries, risks) and PLN-EWO (gate register G-nn). Counts come from this session's files, never from last week's edition or from a counterpart's recap. The owner learns the program state in two pages.

---

## 4. Output specification

### 4.1 Upload sheet and Control sheet

Client template files carry data rows only. The CSL companion workbook (segment builder or reconciliation) opens with a `Control` sheet (spec and validation rules in `references/upload-sheet-qa.md`):

| Control field | Content |
|---|---|
| CSL reference | `CSL-<PROG>-UPL-<yymmdd> R<n>` |
| Client file delivered | Exact client file name with `_R<n>`; CSV alongside |
| Client template used | Which of the client's templates; IMP or Update; "unaltered" statement |
| Convention built to | Scheme version and ruling dates; depth status |
| Sources | Sheet or extract name, ID, extract date, hash, pull time |
| Record counts | Rows; resolved to Active; Not in legacy; hold; review |
| Validation results | Format, uniqueness, padding, parents, required fields, encoding |
| Delta versus previous revision | Rows added, removed, recoded, with the reason |
| Change log | Revision, date, change, by |
| Qualifying confirms | Open-confirm numbers that hold rows in this file |
| Transmittal | Number, date and time, share-log recipients |

### 4.2 Code scheme record

Maintained in `references/code-scheme-record.md` as a dated table: ruling, date, who stated it, written or verbal, document, what it changed, which delivered files it governs. Open items carried at the end of that file: child pump token (PUM versus PMP / CWP), FAN as a level-2 code, instance padding (2-digit versus 3/4-digit), and structure depth (OPEN). A ruling enters the record the day it is made; a verbal ruling is marked verbal until the written confirmation arrives.

### 4.3 Delivered code sets, W77 record (for reconciling counts)

| File | Revision / version | Date | Records | Built to | Note |
|---|---|---|---|---|---|
| MEP list (672 records) | R0 | 08/06/26 | 672 | Pre-ruling census | First census product |
| MEP list | R1 | 08/19/26 | 672 | Pre-ruling | Reissue; change per its change log |
| MEP list | R2 | 08/24/26 | 672 | All rows flagged INCLUDE | Scope flags complete |
| MEP list | R3 | 08/24/26 | 672 | Six-level codes (V1.0) | Six-level codes applied |
| Mechanical | R4 | 08/24/26 | 214 | Unit-as-process | Mechanical set on the unit-as-process basis |
| Mechanical segment builder | v_3 | 08/26/26 | 213 | 08/24/26 rulings | Segment builder introduced |
| Mechanical segment builder | v_3 R2 | 08/26/26* | 213 | 08/24/26 rulings | Fan recodes |
| Mechanical segment builder | v_4 | 08/26/26* | 235 | 08/24/26 rulings | Full mechanical from the 335-row roadmap master pull |
| Mechanical segment builder | v_5 | 08/26/26* | 239 | 08/24/26 rulings | Added CDP03 / CDP05 and HEX03 / HEX04 parent records (+4) |
| Client template, mechanical, POPULATED | R0 | 08/26/26 | 237 named assets: 216 resolved to Active CHAMPS records, 21 Not in CHAMPS | 08/24/26 rulings | Delivered 3:22 PM ET with CSV |
| New Asset Forms | Batch | 08/27/26 | 61 assets (IN 12366 Sentek shaker W59; IN 12491 slurry machine W77; IN 12548 LIMMS W59; Watts LF009 RPZ coded BFP01) | 08/24/26 rulings | 21 of 32 slurry rows lack nameplate data |
| Loops PML | R0 | 09/23/26 | 18 loops with sub-assets; 17 of 18 in scope (HW heat excluded) | Convention in force 09/23/26 (depth OPEN) | Loop codes as MainAsset_Parent records |

Dates marked * are placed in the 08/26/26 delivery sequence; confirm each from the file's own Control sheet before citing. Delivered-to-date total: 672 + 239 + 61 = 972 records. CSL's own 09/11/26 reply-all itemized 962 assets across 5 upload sheets; the file-level sum is 972. Reconcile the 10-record difference by file before the count is next cited, so a counterpart's dispute of the figure cannot stand on an arithmetic gap (csl-operating-rules Section 6, trigger 7).

### 4.4 Loop and system hierarchy

The authoritative loop enumeration is the Cooling Loop Utility Matrix: 16 numbered systems across 18 loop columns, with sub-loops and point-of-use segments beneath them; tower and condenser circuits sit outside the closed-loop matrix and are coded as their own parents. Loop codes are MainAsset_Parent records (`ASML_WLT_077_CHWMAIN` … `PCWWFL` as proposed) and the loop association of every unit is a column on the unit's record, not a code segment or a parent prefix (08/24/26 ruling).

| Record type | Example | Relationship carried |
|---|---|---|
| Loop parent (MainAsset_Parent) | `ASML_WLT_077_CHWMAIN` | Top of the loop hierarchy; one per matrix column in scope |
| Sub-loop | Secondary or process branch under a loop parent | Parent = loop parent |
| POU segment | Point-of-use filter or cabinet segment | Parent = sub-loop or loop parent |
| Unit | `ASML_WLT_077_AHU22N` | Loop association as a column; parent per the structure spec in force |
| Child device | `ASML_WLT_077_AHU22N_PUM01` | Parent = unit |
| Tower / condenser circuit | Own parent record outside the closed-loop matrix | Associated by column to the chillers it serves |

Utility data encountered while building the hierarchy is an engineering finding, not a data note: the matrix's mixing columns read grossly over iron specification (580 ppm against a 0.1 total-Fe specification) while isolated and treated loops read in specification; that goes to the client engineering lead as a finding (`csl-executive-memo`, or a notice per `csl-technical-docs` 4.7), with a one-line pointer in PLN-SUM, and is never buried in the asset file.

### 4.5 New Asset Form intake

| Step | Actor | Record | Age clock |
|---|---|---|---|
| Form arrives in the client DMS | Requester | IN number, date received | Starts |
| Logged on the intake tracker | APM (N. Grubler) | Asset count, nameplate fields present, loop involvement | Day 0 |
| Code drafted in the segment builder | APM | Draft code, convention built to | Target 2 business days |
| Code approved | Client data owner | Approval date | A5 after 5 business days unanswered |
| Loops owner notified | APM | Notification date, where a loop association exists | Same day as approval |
| Upload sheet issued | S. Schryba / APM | One sheet per upload plus the master; transmittal | Per delivery |

Visibility problem on record: requests sat two to three weeks unseen; the fix is a shared tracker view with edit access for the data owner and a weekly intake line in PLN-SUM (received, coded, approved, uploaded, waiting, with ages). Forms with zero commissioning dates or missing nameplate data go to the walk-down items list with the IN number.

### 4.6 Weekly program critical summary (`CSL-<PROG>-PLN-SUM-<yymmdd> R<n>`)

One to two pages (template: `templates/program-summary.md`): 1 Bottom line (three sentences: state, what changed, what is asked) | 2 Delivered to date, table by file with record counts and the convention built to (4.3) | 3 Open-confirm register (4.8) | 4 Import status (what went live, rejected, pending; rejection log received or requested) | 5 Intake line (New Asset Forms) | 6 Next deliveries with dates | 7 Risks, tiered with rule IDs (RED (R8) tagging gate; AMBER (A5) confirms over five business days; AMBER (A6) recap discrepancies). `CSL-W77-PLN-SUM-260828 R1` superseded R0 the same day; a substantive same-day change increments the revision.

Bottom-line form: "Delivered to date 972 records across three files (list); the mechanical set awaits re-import on an unaltered CHAMPS template after the 09/29/26 root cause; structure depth remains OPEN (four rulings, no versioned spec), so no QR print is scheduled. Asked this week: the versioned structure spec (G-13) and the template class ruling for process and multi-asset records."

### 4.7 Gate register edition (`CSL-<PROG>-PLN-EWO-<yymmdd>`)

One to two pages (template: `templates/gate-register.md`): gates G-nn with condition, owner, opened date, status (Open / Evidence received / Closed), evidence needed, and what the gate blocks. W77 standing gates: G-13 versioned structure spec (blocks tagging and all code sets beyond mechanical); G-16 walk-through questionnaire completeness; G-17 SOP review; G-18 sensor calibration batch (350 points / 123 nodes; the PDF arrived truncated at exactly 2 MiB in every copy, so the action is a re-send, not a review of the partial); G-19 process/systems master list before the associated uploads. A gate closes on evidence, never on a statement that it will be met.

### 4.8 Open-confirm register

Columns: # | Question | Asked (date) | To whom (role and name) | Blocks | Status | Tier (rule). A confirm unanswered more than five business days is AMBER (A5); one that gates a print is RED (R8) once the print is scheduled. Standalone template: `templates/open-confirm-register.md`; W77 carried eight standing confirms at PLN-SUM-260828.

### 4.9 Data-quality metrics (per file, on the Control sheet and in PLN-SUM)

| Metric | Definition |
|---|---|
| Records ready / hold / review | Ready = passes all validations and resolved to a legacy record or ruled Not in legacy; hold = blocked by an open confirm; review = data defect found |
| % with nameplate data | Manufacturer, model, serial present; base = records in the file |
| % with space and cost center | Both fields present (required for work-order routing) |
| Duplicate rate | Double-listings found ÷ records, with the list |
| Code format validity | Rows passing the format rule for the convention built to |
| Unique-code check | Zero duplicates in the assembled-code column; collisions listed |
| Delta versus previous revision | Rows added, removed, recoded, with the reason |

Validation rules as run in code (`references/upload-sheet-qa.md` has the full set): format `^ASML_WLT_077_[A-Z]{2,4}[0-9]{2,4}[A-Z]?(_[A-Za-z]{3,6}[0-9]{2,4})?$` for the 08/24/26 convention (adjust the padding group when the padding ruling lands); uniqueness on the assembled code; parent exists for every child; child token in the allowed list; space and cost center non-blank; legacy join class assigned on every row.

### 4.10 Import failure triage

| Order | Test | Evidence | If it fails |
|---|---|---|---|
| 0 | Rejection log obtained | The importer's log or screenshot | Ask before testing anything; record the stated root cause with date and speaker |
| 1 | Template altered | Diff of file name, sheet names, headers, column order against the pristine template | Rebuild on the pristine template; data rows only |
| 2 | Primary key changed on a live record | Compare keys to the live pull | Revert; submit as an Update transaction |
| 3 | Auto-populate machinery stripped | Formula columns, hidden columns, standard-asset and taxonomy fields present | Restore from the pristine template |
| 4 | Required fields blank | Space, cost center non-blank on every row | Fill from the source or hold the row |
| 5 | Encoding and format | UTF-8 / BOM, delimiter, date format, leading zeros preserved | Re-export from the workbook, not from a text editor |
| 6 | Code validity | Format and uniqueness rules pass | Fix in the segment builder; re-paste |

W77 stated root cause, 09/29/26: unaltered CHAMPS templates required. A failed import is never fixed by editing the live system.

### 4.11 Walk-down items list

One sheet, kept with the master intake workbook and carried in PLN-SUM as a count: # | Asset (draft code) | IN or source file | Building / area | What is missing (nameplate fields, commissioning date, field tag, location) | Photo required | Owner (CSL / FM PM) | Walk date | Result. Items come from the reconciliation (nameplate gaps: 21 of 32 slurry-machine rows; forms with zero commissioning dates) and from tag collisions (TCWP-1 at W59); a row leaves the list only when the field data is on the sheet and in the code set, and the walk follows the tagging sequence (central plant → roof → tool areas) so that one visit serves both.

### 4.12 Weekly rhythm

| Day | Work | Output |
|---|---|---|
| Monday | Pull the intake tracker and the live CMMS extract; age every open confirm | Confirm ages; intake line |
| Tuesday | Planon weekly (3 PM ET): put the confirms and gates on the agenda; record rulings the same day as written or verbal | Code scheme record updated; minutes audit per `csl-meeting-records` |
| Wednesday / Thursday | Code set work, template population, reconciliation, walk-down items | Segment builder v_n; transmittals |
| Friday | Counts re-derived from the files; PLN-SUM and PLN-EWO issued; transmittal register updated | `PLN-SUM-<yymmdd>`, `PLN-EWO-<yymmdd>` into WKR-nnC |

---

## 5. Voice and formatting rules

- Counts always with the file, revision, date, and convention: "239 records, v_5, 08/26/26, built to the 08/24/26 rulings", never "about 240 assets".
- Codes in monospace in prose; assembled codes exactly as the file carries them (case, underscores, padding).
- Rulings cited by date and document; verbal rulings labeled verbal with the confirmation request date.
- Findings in the fixed order: item, tier with rule, exposure (records, reprints, days), owner, action, date.
- Counterparts by role and name as the record names them; discrepancies as record discrepancies with dates and documents.
- Workbooks per `csl-brand` Section 5: Control sheet first, navy header rows, autofilter, no merged cells, no CSL Red fills, tier cells in status colors with the tier word.
- Client template files carry none of the CSL formatting; the CSL look lives in the companion workbook.
- Dates MM/DD/YY in documents; ISO in CSL file names; the client's own date pattern inside client-mandated names.

Sentence forms:

- Count: "Delivered to date: 972 records (MEP list R3, 672, 08/24/26; mechanical v_5, 239, 08/26/26; New Asset Forms, 61, 08/27/26); the 962-record itemization of 09/11/26 is being reconciled to this file-level total."
- Verbal ruling: "Structure depth stated as eight levels on the call by [name], 09/22/26; written confirmation requested 09/22/26; code sets continue on the 08/24/26 written convention until the spec issues."
- Tagging hold: "No QR print is scheduled: G-13 (versioned structure spec) open since [date]; RED (R8) applies if a print date is set; reprint and re-walk cost stated in the hold request of [date]."
- Discrepancy: "Recap of [date] states the mechanical upload was work in progress; transmittal CSL-W77-TRN-260826-01 shows delivery 08/26/26 3:22 PM ET with edit access; correction requested same day (AMBER (A6))."

---

## 6. Worked example

Control-sheet block, mechanical segment builder v_5 (values from the record; field names per `references/upload-sheet-qa.md`):

| Field | Value |
|---|---|
| CSL reference | CSL-W77-UPL-260826 R0 (companion workbook; the client file keeps its own name) |
| Client file delivered | ASML_WLT_077_Mechanical Asset Upload Sheet August 26 2026 CSL-Consulting.xlsx + copy-paste-ready CSV |
| Client template used | CHAMPS asset template held by CSL (one of six: Process / Multi-Asset / Standard Asset, IMP / Update); template unaltered |
| Convention built to | Functional Code Structure v1.1 with the 08/24/26 format rulings; six-level scheme V1.0 as published; depth OPEN |
| Sources | Roadmap Master 1059284113641348, 335-row mechanical pull; CHAMPS Total Combined Assets extract, 2,645 records; walk-down sheets |
| Records | 239 rows in v_5; client template 237 named assets: 216 resolved to Active CHAMPS records, 21 Not in CHAMPS |
| Delta versus previous | v_4 235 → v_5 239: +4 parent records added (CDP03, CDP05, HEX03, HEX04) |
| Validation | Format pass 239/239; unique assembled codes 239/239; parents present after the +4; open tokens flagged on the rows shown below |
| Transmittal | CSL-W77-TRN-260826-01, 08/26/26 3:22 PM ET, edit-access share to B. Gannon, T. Dube, N. Grubler, E. Hubert |

Segment-builder excerpt, six rows (assembled codes follow the 08/24/26 rulings; the RDF01 instance and the loop-column values are illustrative):

| Enterprise | Site | Bldg | Unit | Child | Loop (column, not a segment) | Assembled code | Flag |
|---|---|---|---|---|---|---|---|
| ASML | WLT | 077 | AHU22N | — | CHW01 (illustrative) | `ASML_WLT_077_AHU22N` | Ready |
| ASML | WLT | 077 | AHU22N | PUM01 | CHW01 (illustrative) | `ASML_WLT_077_AHU22N_PUM01` | Hold: child token PUM vs PMP / CWP open |
| ASML | WLT | 077 | AHU22N | RDF01 | — | `ASML_WLT_077_AHU22N_RDF01` | Ready (fan-family token RDF; instance illustrative) |
| ASML | WLT | 077 | HEX03 | — | CDW (illustrative) | `ASML_WLT_077_HEX03` | Ready; parent added in v_5 |
| ASML | WLT | 077 | HEX03 | CWP01 | CDW (illustrative) | `ASML_WLT_077_HEX03_CWP01` | Hold: child token open; parent now exists |
| ASML | WLT | 077 | BFP01 | — | DCW | `ASML_WLT_077_BFP01` | Hold: code path vs DCW_BFP01 placeholder in CHAMPS; merge ruling needed |

Open-confirm register, five rows (asked dates marked * are illustrative; the rest are from the record):

| # | Question | Asked | To whom | Blocks | Status / tier |
|---|---|---|---|---|---|
| 1 | Issue a versioned structure spec fixing depth (six / seven / eight levels) | 09/22/26 (verbal ruling; written confirmation requested) | Client data owner (T. Dube) | QR label prints; every code set beyond mechanical | Open; RED (R8) if a print is scheduled; AMBER (A5) |
| 2 | Child pump token: PUM, PMP, or CWP | 08/24/26 | Client data owner | Final child codes; PM records | Open; AMBER (A5) |
| 3 | TCWP-1 tag collision at W59: TCWP01 / TCWP02 provisional | 08/28/26* | Client data owner; FM PM | QR prints at W59 | Open; RED (R8) before prints |
| 4 | BFP01 versus DCW_BFP01 NEW-Placeholder: code path and merge | 08/27/26* | Client data owner | New Asset Form batch upload | Open; AMBER (A5) |
| 5 | Which of the six CHAMPS templates applies to process and multi-asset records | 09/29/26 | Client import owner | Re-import of the mechanical set | Open |

---

## 7. Failure modes and how to avoid them

| Failure | What it looks like | Avoidance |
|---|---|---|
| Coding to a verbal ruling | A code set built to "eight levels" stated on a call | Build to the last written convention; mark the verbal one on the Control sheet with the confirmation request date |
| Renaming or reshaping a client template | Added helper column, renamed sheet, "cleaned" headers; import rejected | Data rows only; CSL work in the companion workbook; byte-compare the template structure before delivery |
| Recoding a live primary key | A re-import to change a code already in the CMMS | Update-template transaction; code changes after go-live are a decision with a cost, not an edit |
| Printing tags before confirmation | Labels ordered while depth or a token is open | Gates in 3.9 in writing; RED (R8) hold request |
| Letting a counterpart's recap redefine delivered scope | A recap calls delivered files "work in progress" or states only 3 assets uploaded; the next report repeats it | Report both figures with the file list; same-day record correction with the transmittal evidence (`csl-client-comms`) |
| Burying engineering findings in a data file | Iron at 580 ppm noted in a cell comment | Finding to the engineering lead as a memo or notice; one-line pointer in PLN-SUM |
| Counting records without stating the convention | "972 delivered" with no file list | Table by file with revision, date, count, convention |
| Carrying last week's counts | PLN-SUM figures copied forward | Counts re-derived from this session's files; pull times on the page |
| Placeholder treated as a record | DCW_BFP01 NEW-Placeholder counted as Active | Placeholder class in the reconciliation; merge ruling on the confirm register |
| Intake invisible | New Asset Forms unseen for two to three weeks | Shared tracker view; weekly intake line with ages |
| Reviewing a truncated file | Sensor calibration PDF cut at exactly 2 MiB reviewed as complete | Size check against the sender's; re-send requested; gate stays open |
| Guessing nameplate data | Model or serial typed to fill a required field | Row held; walk-down item with the IN number |

---

## 8. Pre-issue checklist

- Scope ruling cited by date and document; exclusions and deferrals listed on the Control sheet.
- Client template unaltered: file name pattern kept with `_R<n>`, sheets, headers, column order, hidden columns, auto-populate machinery intact; data rows only.
- Convention built to stated on the Control sheet with ruling dates; depth marked OPEN where it is.
- Validations run in code and recorded: format, uniqueness, padding, parent exists, required fields (space, cost center), encoding.
- Reconciliation classes counted with the legacy extract's date and hash; double-listings, collisions, placeholders, code defects, dangling parents listed.
- Record counts by file, revision, date; delta versus previous revision with reason; totals re-added in code.
- Open-confirm register current; every hold row points at a confirm; A5 and R8 tiers applied with rule IDs.
- Engineering findings routed to the engineering lead, not left in the data file.
- Transmittal drafted; share with edit access; CSV alongside xlsx; share-log timestamp captured.
- Tagging gates checked; no print scheduled on an unconfirmed code.
- PLN-SUM and PLN-EWO numbered per `csl-document-control`; counts from this session; brand QA per `csl-brand` on the CSL workbook and PDFs.
- Planon record packaging (CSV / XML / JSON) via the installed `planon-doc-generator` skill; nothing invented to fill a template.

---

## Files in this skill

- `references/code-scheme-record.md` — the W77 functional code scheme and every dated ruling, with the open-items table and the "convention in force by date" ledger.
- `references/upload-sheet-qa.md` — validation rules for segment builders and client templates, and the Control sheet specification.
- `references/reconciliation-method.md` — join order, classification classes, findings patterns, and the reconciliation tab layout.
- `templates/program-summary.md` — PLN-SUM skeleton with populated W77 rows.
- `templates/gate-register.md` — PLN-EWO skeleton with the G-13 to G-19 gates.
- `templates/open-confirm-register.md` — standalone open-confirm register with tiering rules.

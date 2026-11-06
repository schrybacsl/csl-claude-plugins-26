# Upload Sheet QA: Validation Rules and Control Sheet Specification

Read this before populating a client import template or issuing a segment-builder revision (`csl-asset-data-cmms` 3.4, 3.5, 4.1, 4.9). Two artifacts leave CSL for every delivery: the client's template with data rows only, and the CSL companion workbook whose first sheet is `Control`. The rules below are run in code (openpyxl / pandas) and their results are written to the Control sheet; a rule that cannot be run is reported as not run, never as passed. Workbook anatomy per `csl-brand` Section 5 applies to the companion workbook only; the client template carries none of it.

---

## 1. Template integrity (client file)

| Rule | Test | Pass | On failure |
|---|---|---|---|
| T1 File name pattern | Client pattern kept; only `_R<n>` appended | `ASML_W77_..._August_24_2026_R3.csv` | Rename back; the CSL number lives on the Control sheet |
| T2 Sheet names | Identical to the pristine template | Set equality | Restore |
| T3 Header row | Cell-by-cell string equality with the pristine template, same order | 100% | Restore; no added or renamed columns |
| T4 Hidden columns and formula columns | Present and unchanged (standard-asset and taxonomy auto-populate) | Unchanged | Restore from the pristine copy; re-paste data rows |
| T5 Data region | Values only in data rows; no formulas, comments, fills, merged cells, or filters left on | Clean | Paste values; clear formats |
| T6 Template class | Which of the client's templates (W77: Process / Multi-Asset / Standard Asset; IMP or Update) is stated on the Control sheet and in the transmittal | Stated | Ask the import owner which class applies before delivery |
| T7 Encoding (CSV) | UTF-8 (BOM per the importer's requirement), delimiter as the template's export produces, dates in the template's format, leading zeros preserved (`077`) | Round-trips through the importer's reader | Re-export from the workbook |

Reference: W77 root cause stated 09/29/26, "any change and they will not upload".

## 2. Code validation (segment builder)

| Rule | Test | Notes |
|---|---|---|
| C1 Format | Regex for the convention built to. 08/24/26 convention, 2-digit padding: `^ASML_WLT_077_[A-Z]{2,4}[0-9]{2,4}[A-Z]?(_[A-Za-z]{3,6}[0-9]{2,4})?$` | Loosen or tighten the padding group when the padding ruling lands (open item 4); keep the regex text on the Control sheet |
| C2 Assembly | Assembled code equals the segments joined by `_`, no blanks inside, no trailing separator | Formula column; recomputed in code |
| C3 Uniqueness | Zero duplicate assembled codes; list every collision with both rows | TCWP01 / TCWP02 provisional split is recorded here |
| C4 Parent exists | Every child's unit token resolves to a unit row in the same set | v_5 added HEX03 / HEX04, CDP03 / CDP05 to pass this |
| C5 Child token allowed | Child token in the allowed list for the convention (PUM pending; EXF / RDF / SEF; sensor) | Open tokens flagged Hold, not failed |
| C6 Padding | Instance digits consistent within a family | Open item 4; report the distribution (2-digit versus 3/4-digit) |
| C7 Loop column | Loop association present where the unit sits on a loop; never inside the code | Cross-check against the Cooling Loop Utility Matrix |
| C8 Prefix | `ASML_WLT_077_`; no building letter; underscores | Superseded forms listed in `code-scheme-record.md` Section 6 |

## 3. Record completeness

| Rule | Field(s) | Pass | Hold or review |
|---|---|---|---|
| R1 Space | Space code present (work-order routing) | Non-blank | Hold; source the space from drawings or walk-down |
| R2 Cost center | Present | Non-blank | Hold |
| R3 Nameplate | Manufacturer, model, serial | All present or the gap listed | Review; walk-down item (21 of 32 slurry-machine rows lacked nameplate data) |
| R4 Commissioning date | Present or explicitly unknown | Not zero, not 01/01/1900 | Review; walk-down item |
| R5 Legacy join class | One of Active with code / Active without code / Not in legacy / Double-listed / Code defect / Placeholder | Assigned | Review until assigned |
| R6 Status vocabulary | Values from the importer's list | Valid | Review ("completed" versus "tested complete" reported as a finding) |

## 4. Control sheet specification (companion workbook, first sheet)

| Row | Field | Content and example |
|---|---|---|
| 1 | CSL reference | `CSL-W77-UPL-260826 R0` |
| 2 | Client file delivered | `ASML_WLT_077_Mechanical Asset Upload Sheet August 26 2026 CSL-Consulting.xlsx`; CSV alongside |
| 3 | Client template used | Class (Process / Multi-Asset / Standard Asset), IMP or Update; "template unaltered; T1 to T7 pass" |
| 4 | Convention built to | "Functional Code Structure v1.1 with the 08/24/26 format rulings; six-level scheme V1.0; depth OPEN (09/10, 09/22 verbal, 09/29)"; regex text used for C1 |
| 5 | Sources | Sheet or extract, ID, extract date, MD5, pull time ET (Roadmap Master 1059284113641348, 335-row mechanical pull; CHAMPS Total Combined Assets, 2,645 records) |
| 6 | Record counts | Rows; resolved to Active; Not in legacy; hold; review (237 named assets: 216 Active, 21 Not in CHAMPS) |
| 7 | Validation results | Each rule ID with pass / fail counts or "not run: reason" |
| 8 | Data-quality metrics | Ready / hold / review; % nameplate; % space and cost center; duplicate rate; format validity; unique-code check |
| 9 | Delta versus previous revision | "v_4 235 → v_5 239: +4 parents (CDP03, CDP05, HEX03, HEX04)" |
| 10 | Change log | Revision, date, change, by (one line per revision, oldest first) |
| 11 | Qualifying confirms | Open-confirm numbers holding rows in this file, with asked dates |
| 12 | Engineering findings routed | Any finding found while building (utility data, defects) and the memo or notice it went to |
| 13 | Transmittal | Number, date and time ET, recipients, share method (edit access) |
| 14 | Column dictionary | Every column in the companion sheets: name, meaning, source, allowed values |

Tab order after Control: data sheet(s) (navy tabs), roll-ups (dark teal), reference lists such as allowed tokens and the loop matrix (olive), archive (grey). Header rows navy with white bold text, frozen, autofilter on; tier cells in status colors with the tier word; no CSL Red fills; no merged cells in data regions.

## 5. Delivery bundle

| Item | Rule |
|---|---|
| Client template (xlsx) | Data rows only; T1 to T7 pass |
| Copy-paste-ready CSV | Same rows; T7 pass; same `_R<n>` |
| Companion workbook | Control sheet per Section 4; segment builder; reconciliation tab |
| Transmittal | `CSL-<PROG>-TRN-<yymmdd>-<seq>`; purpose For import; recipients; response requested by |
| Share log evidence | Edit-access share from the client tenant; timestamp captured |
| Superseded revision | Moved to `_superseded/` with its revision intact |

## 6. Run order (script outline)

1. Load the pristine template and the candidate; run T1 to T5 (structure diff) before touching data.
2. Load the segment builder; recompute C2; run C1, C3 to C8; write results to Control row 7.
3. Run R1 to R6; assign Ready / Hold / Review; compute Section 4 row 8 metrics.
4. Diff against the previous revision by assembled code; write row 9.
5. Paste values into the template data region; re-run T1 to T5 on the result; export CSV; run T7.
6. Fill rows 11 to 13; hash all delivered files; save the pull snapshot alongside (`csl-document-control` Section 8).

A file with any T-rule failure is not delivered. A file with C or R holds is delivered with the holds listed on the Control sheet and in the transmittal, because the client decides whether held rows wait or import as-is.

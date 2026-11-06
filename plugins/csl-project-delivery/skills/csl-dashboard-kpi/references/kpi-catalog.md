# KPI Catalog

Read this whenever a tile, table, or chart is about to show a number: every KPI here has one owner, a stated formula and denominator, a named source column, a threshold tied to a rule ID in `csl-schedule-risk/references/tier-rules.md`, and a refresh cadence. A tile that cannot cite a catalog ID is not built. Values come from this session's pulls (`csl-data-pipeline`); "not available at <pull time>, source <name>" is shown honestly when a source is missing. Owner means the role accountable for the underlying record; CSL computes and reports.

Conventions: W77 sources are named with their Smartsheet IDs because that is where the program lives today; after the Graph repoint the IDs become `SheetRef` keys and nothing else changes. Cadence F = Friday pull, W = Wednesday, S = Sunday/Monday, D = daily when a program is in a shutdown or print window.

## 1. Permits (source: SIPP Permits 289677048237956; `csl-permits-shutdowns`)

| ID | KPI | Definition and formula | Denominator | Source columns | Threshold -> tier (rule) | Cadence | Owner |
|---|---|---|---|---|---|---|---|
| KPI-PRM-01 | Permits started this week | count(START within Mon–Fri of the reporting week) | none (count) | START, Status | informational | F, S (next week) | Permit coordinator (client) |
| KPI-PRM-02 | Gated in time % | count(started permits with every gate timestamped before START) / started x 100 | permits started | gate columns with timestamps, START | < 100% names the permit and gate; a start with no permit at all is RED (R6) | F | Permit coordinator; contractor PM |
| KPI-PRM-03 | Perfect-week streak | consecutive weeks with KPI-PRM-02 = 100% and zero work-done-no-record | none (count of weeks) | derived from KPI-PRM-02, KPI-PRM-07 | reset to 0 by any R6; the resetting permit is named | F | CSL reporter |
| KPI-PRM-04 | Permits closed with duration | count(closed in week); median and max days open = close date - START | closed in week | START, close date | informational; a close with open gates is a record defect AMBER (A6) | F | Permit coordinator |
| KPI-PRM-05 | New permits next month | count(START within the next 30 days) with systems named | none | START, System | informational; feeds WKR-A look-ahead | S | CSL reporter |
| KPI-PRM-06 | Inverted-date flags | count(START > END) | rows on board | START, END | >= 1 -> AMBER (A6) per row; correction requested | F | Permit coordinator |
| KPI-PRM-07 | Work done, no record | count(field activity in daily or field reports with no permit row) | none | field reports x permit board | >= 1 -> RED (R6) until backfilled | D during active work, F | Contractor PM; site EH&S |

## 2. Roadmap (source: W77 Roadmap Master 1059284113641348, parent rows only; `csl-schedule-risk`)

| ID | KPI | Definition and formula | Denominator | Source columns | Threshold -> tier (rule) | Cadence | Owner |
|---|---|---|---|---|---|---|---|
| KPI-RDM-01 | Rows changed since last pull | count(parent rows with any compared cell changed) from `diff_pulls.py` | parent rows compared | all compared columns | 0 with identical md5 -> frozen (see KPI-RDM-02) | S, W, F | Roadmap owner (client) |
| KPI-RDM-02 | Frozen weeks | frozen streak from `freeze_check.py` | none (count of pulls) | normalized md5 | 1 -> AMBER (A4); >= 2 with field witnesses -> RED (R5); >= 2 without -> A4 held open | every pull | Roadmap owner |
| KPI-RDM-03 | RPN >= 700 count | count(RPN C >= 700) | parent rows with RPN C | RPN C | informational; list sorted descending | F | Risk owner (client) |
| KPI-RDM-04 | RPN >= 700 without active mitigation | count(RPN C >= 700 and (Owner blank or no dated action or action date passed with no status change)) | KPI-RDM-03 | RPN C, Owner, mitigation action and date (register) | >= 1 -> RED (R1); rows named | F, and same day when observed | Client program lead |
| KPI-RDM-05 | Health distribution | count by Health (Green, Yellow, Active, Pending) | parent rows | Health | informational; a class that changes without row changes is a data finding | F | Roadmap owner |
| KPI-RDM-06 | % behind baseline | count(Variance2 < 0) / count(Baseline Finish present) x 100 | rows carrying a baseline | Variance2, Baseline Finish | reported; per-row slip tiers per A2/R3 | F | Roadmap owner; scheduler |
| KPI-RDM-07 | 0% past start quarter without constraint | count(YR. = current year, % = 0, START quarter passed, Constraints blank) | rows dated this year | YR., %, START, Constraints | one population finding AMBER (A2); RED (R4) if any row is anchor, critical path, or >= 700 | F | Roadmap owner |
| KPI-RDM-08 | Bow-wave count | count(END in the final program year) and delta vs last pull | parent rows | END | growth reported with rows named; shrinkage with deletions is a data finding | F, monthly | Client program lead |
| KPI-RDM-09 | Forecast vs budget variance by E-GRP | (sum Forecast - sum Budget) / sum Budget x 100 per E-GRP | budget per E-GRP | Budget, Forecast <year>, E-GRP | > 10% -> RED (R2); 5–10% -> AMBER (A2) | F, quarter close | Budget owner (client); D. Wolf tracker for WS lines |
| KPI-RDM-10 | Quarterly cash flow vs plan | actual per quarter vs plan; cumulative gap $ and % of plan to date | plan to date | quarterly columns, paid ledger or client actuals | line variance per R2/A2; annual not equal to quarterly sum -> AMBER (A6) | quarter close | Budget owner |

## 3. Mitigation workstreams (source: ST CHW/PCW System Mitigation Plan 2158727850315652 joined to the Containment Budget Tracker Rev 4 on WS number; `csl-schedule-risk` 3.7, `csl-cost-change-control`)

| ID | KPI | Definition and formula | Denominator | Source columns | Threshold -> tier (rule) | Cadence | Owner |
|---|---|---|---|---|---|---|---|
| KPI-MIT-01 | Open rows | count(rows not closed or cancelled) | none | Status | informational | F | Sheet owner (client program lead); CSL co-owns WS-08 and WS-22 |
| KPI-MIT-02 | Past-target count and trend | count(open rows with Target Date < pull date); series by week | open rows | Target Date, Status | row tiers per A2; anchors or minuted dates per R4; always printed with KPI-MIT-03 | F | Row owners |
| KPI-MIT-03 | Closures per week | count(rows closed since previous snapshot) | none | Status (diff) | a bulk sweep is reported as a sweep with its count | F | Row owners |
| KPI-MIT-04 | Steps complete of 10 | per project: completed lifecycle steps of 10; block median | 10 | Lifecycle Step, In Place (PO) | past step 9 with no PO number -> exception row | F | Project owners |
| KPI-MIT-05 | Committed $ vs planning budget | sum(PO amounts) vs sum(planning budget) per project and block; variance % | planning budget | tracker Rev 4 columns | > 10% -> RED (R2); 5–10% -> AMBER (A2) | F | D. Wolf (tracker); client budget owner |
| KPI-MIT-06 | Rows per owner | count(open rows) by Owner; concentration = max share | open rows | Owner | > 50% on one owner -> throughput risk on the sheet, rows listed | F | Sheet owner |
| KPI-MIT-07 | Data-defect counts | count(mixed-format IDs), count(blank Baseline Status), count(blank E-Group) | rows | WS #, Baseline Status, E-Group | >= 1 -> AMBER (A6) population; rows footnoted out of roll-ups | F | Sheet owner |

## 4. CSL action board (source: CSL Tasks 7673437876080516)

| ID | KPI | Definition and formula | Denominator | Source columns | Threshold -> tier (rule) | Cadence | Owner |
|---|---|---|---|---|---|---|---|
| KPI-BRD-01 | Reds | count(rows with Health red, or End Date passed and State not Complete) | open rows | Health, State, End Date | each named with its rule (A2 or R4) | F | CSL PMs (assigned) |
| KPI-BRD-02 | Anchors closed | count(anchor rows moved to Complete this week) of anchors planned | anchors planned for the week | State (diff), anchor list from WKR-A | shortfall named with cause | F | CSL owner of the row |
| KPI-BRD-03 | Byte-identical flag | md5 identical to previous pull (the board was identical 08/28/26 to 09/04/26) | none | normalized md5 | identical -> AMBER (A4); rows expected to move named | every pull | S. Schryba (board admin) |

## 5. Asset program (sources: delivered upload files, open-confirm register, gate register, client import log; `csl-asset-data-cmms`)

| ID | KPI | Definition and formula | Denominator | Source | Threshold -> tier (rule) | Cadence | Owner |
|---|---|---|---|---|---|---|---|
| KPI-AST-01 | Records delivered by file and convention | count(rows) per delivered file with the convention version built to (Functional Code Structure v1.1) and delivery timestamp | none | Control sheet of each file; transmittal register | informational; a convention change re-opens delivered rows and is stated | F | S. Schryba |
| KPI-AST-02 | Ready / hold / review | count per class per file (ready = passes validations; hold = blocked by an open confirm; review = data defect) | rows in file | Reconciliation tab | hold rows tie to a confirm ID | F | S. Schryba; client data owner for confirms |
| KPI-AST-03 | Open confirms | count(open) and age in business days per confirm | none | open-confirm register | > 5 business days -> AMBER (A5); one that gates a scheduled print -> RED (R8) | F, S | Client data owner |
| KPI-AST-04 | Open gates | count(G-nn open) with what each blocks | gates on register | PLN-EWO gate register | a gate open > 2 weeks against a dated deliverable -> AMBER (A3) | F | Gate owners |
| KPI-AST-05 | Days to hard deadline 10/30/26 | business days from pull date to 10/30/26 (Loops + AHS hierarchy) with open gates counted against it | none | calendar; KPI-AST-04 | fewer than 20 business days with any blocking gate open -> headline item | W, F | Client program lead; S. Schryba |
| KPI-AST-06 | Import status | count(live / rejected / pending) per delivered file; rejection log received yes/no | rows delivered | client import log | rejected with no log received -> AMBER (A5) after 5 business days | F | Client data owner |

## 6. Telemetry (source: CTRW pipeline outputs per rig; `csl-data-pipeline` 3.6)

| ID | KPI | Definition and formula | Denominator | Source | Threshold -> tier (rule) | Cadence | Owner |
|---|---|---|---|---|---|---|---|
| KPI-TEL-01 | Runway days | (current median volume - minimum safe volume) / loss L/day from the drawdown regression since the last refill | none | `_metrics.json` drawdown | < 90 -> RED (R9); falling >= 90 -> AMBER (A1); not falling -> GREEN (G) | F (weekly zip) | Client engineering lead; D. Wolf notices |
| KPI-TEL-02 | Uptime % | minutes with at least one sample / window minutes x 100 | window minutes | `_metrics.json` uptime | < 95% named with the dark classes | F | Logger owner (client FM) |
| KPI-TEL-03 | Dark days | sum(true_dark minutes) / 1440; artifacts (export, midnight cut, re-send) stated separately | none | dark-window table | any true dark on TR2-type faults reported with the fault | F | Logger owner |
| KPI-TEL-04 | Valve saturation % | samples at >= 95% or <= 5% / samples; longest saturated run | samples | valve channel | >= 10% or a run >= 60 min -> watch item AMBER (A1) | F | Controls / BMS |
| KPI-TEL-05 | Zero-flow events | count(samples at or below tolerance) with first and last time | none | flow channel | >= 1 confirmed on a live circuit -> RED (R9) | F, D when live | Client engineering lead |

## 7. Program governance (sources: minutes and agendas, correction log; `csl-meeting-records`, `csl-client-comms`)

| ID | KPI | Definition and formula | Denominator | Source | Threshold -> tier (rule) | Cadence | Owner |
|---|---|---|---|---|---|---|---|
| KPI-GOV-01 | Minutes issued within 2 business days | count(minutes issued <= 2 business days after the meeting) / meetings held | meetings in the month | minutes issue dates | < 100% names the meeting number | monthly, F | Meeting issuer (N. Grubler for the Planon weekly) |
| KPI-GOV-02 | Open action items aged | count(open items) in buckets 0–7, 8–14, > 14 days from the minutes item date | open items | action registers | > 14 days with no update -> AMBER (A3) per item | F | Item owners |
| KPI-GOV-03 | Record discrepancies open | count(correction requests outstanding: counterpart minutes or recaps conflicting with the transcript or CSL's record) | none | correction log | >= 1 -> AMBER (A6); reversal of a minuted decision -> RED (R7) | F | Meeting issuer; counterpart named in the log |
| KPI-GOV-04 | CAAR status | per CAPEX project: design and execution CAAR state (not started / submitted / approved) with dates | CAPEX projects | CARR tracker 4463394158497668; intake replies | a project at lifecycle step 8 with no CAAR submitted -> docket item | F | Client project manager of record |

## 8. How a KPI enters a dashboard

1. Cite the catalog ID in the tile's config; the tile label is the KPI name, the hover shows formula, denominator, source, and pull time.
2. The value comes from `metrics.json` of the same pull the report used, so the dashboard and the PDF never disagree on a number they share.
3. The tier bar and word come from the threshold column, never from a stylist's choice.
4. A KPI added or changed here bumps the catalog version noted in the options menu build sheet and the dashboard's about panel.

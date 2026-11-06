# KPI and Reporting Options Menu

Read this when a stakeholder asks for "their own view", when the client program lead asks CSL to build command dashboards for team members, or when an intake session must be run and its result turned into a build sheet. The menu is a two-page branded document (`CSL-<PROG>-OPT-<topic> v<n.n>`; form per `csl-technical-docs` 4.8; numbering per `csl-document-control` 2.7): page 1 the checklist, page 2 the build sheet. Module content is owned here; every module maps to catalog IDs in `kpi-catalog.md`.

## 1. The W77 case this method comes from

The client program lead asked CSL to build personal command dashboards for several team members, modeled on the executive header view of the Roadmap Insight Dashboard. CSL prepared `CSL-W77-OPT-KPI` (2 pages: checklist plus build sheet) and ran intake sessions from it. One recipient, the CRE engineering counterpart, selected six modules (A1, A6, A7, B7, E2, E6) and corrected a typo on the governance line (CAAR, not CARR); the menu was reissued as v1.1 with the correction recorded on the build sheet ("v1.1: G3 corrected from CARR to CAAR"), file `CSL-W77-OPT-KPI_Koning_v1.1.pdf`. The new view was built beside the executive view, access-gated with its own codes, and reads the same pulls. The taxonomy below is the package's generic superset so the codes stay stable across programs and recipients.

## 2. Module taxonomy

Codes are stable; a program menu shows only the modules its sources support. Effort: S = existing KPI and figure, hours; M = new join or figure, one to two days; L = new source or connector, a week or more.

| Code | Module | KPI(s) | Source | Refresh | Drill-down | Effort |
|---|---|---|---|---|---|---|
| **A** | **Schedule and look-ahead** | | | | | |
| A1 | Week look-ahead: anchor rows with END dates and any verbally named outer frame | KPI-BRD-02, minuted dates | CSL Tasks; minutes | Sunday pull | Row -> transmittal or minutes item | S |
| A2 | Rows changed since last pull ("what moved") | KPI-RDM-01 | Roadmap Master diff | every pull | Cell-level old -> new | S |
| A3 | Frozen-weeks indicator with witnesses | KPI-RDM-02 | freeze chain; permit board | every pull | Rows expected to move | S |
| A4 | % behind baseline and worst variance rows | KPI-RDM-06 | Roadmap Master | Friday | Row -> baseline vs current | S |
| A5 | 0% past start quarter without constraint | KPI-RDM-07 | Roadmap Master | Friday | Row list sorted by RPN and budget | S |
| A6 | Milestones in the next 30 / 60 / 90 days by system | START and END in window; E-GRP or taxonomy | Roadmap Master, permit board | Friday | System -> rows -> permits | M |
| A7 | Bow wave: rows ending in the final program year, trend | KPI-RDM-08 | Roadmap Master | Friday, monthly | Rows moved into the final year since last pull | S |
| A8 | Constraint register with age and enabling owner | Constraints, A3 aging | Roadmap Master | Friday | Constraint -> rows -> owner | M |
| **B** | **Risk and RPN** | | | | | |
| B1 | RPN watchlist >= 700 with mitigation status | KPI-RDM-03, KPI-RDM-04 | Roadmap Master; risk register | Friday | Row -> register entry | S |
| B2 | RPN >= 700 without active mitigation (R1 count) | KPI-RDM-04 | same | Friday, same day | Row -> owner request date | S |
| B3 | RPN changes since last pull with cause | diff on SEV, Occ, Det, RPN C | Roadmap Master | Friday | Factor moved -> document cited | S |
| B4 | Health distribution | KPI-RDM-05 | Roadmap Master | Friday | Class -> rows | S |
| B5 | Risk register extract (top 10, every RED, tier changes) | register schema | risk register | Friday | Row -> mitigation action | M |
| B6 | Tier changes this week | register diff | risk register | Friday | Row -> rule that changed | M |
| B7 | System risk heat: max RPN and count >= 700 per E-GRP or taxonomy | KPI-RDM-03 grouped | Roadmap Master | Friday | System -> rows | M |
| **C** | **Cost and pipeline** | | | | | |
| C1 | Forecast vs budget by E-GRP with rule marks | KPI-RDM-09 | Roadmap Master | Friday, quarter close | E-GRP -> rows | S |
| C2 | Quarterly cash flow vs plan, cumulative | KPI-RDM-10 | Roadmap Master; paid ledger | quarter close | Quarter -> contributors | M |
| C3 | Proposal-to-PO pipeline: steps of 10, committed vs planning | KPI-MIT-04, KPI-MIT-05 | mitigation sheet + tracker Rev 4 | Friday | Project -> PO record | M |
| C4 | Blocked POs with days blocked | pipeline blockers | tracker; PO records | Friday | PO -> blocker -> owner | S |
| C5 | Change-order log by owner | CO log schema | project workbooks | monthly | CO -> decision record | M |
| C6 | Invoice and payment tracking, single-entry linkage | Paid Ledger, Committed Cost | budget workbooks | monthly | Invoice -> PO -> budget line | L |
| **D** | **Permits and safety** | | | | | |
| D1 | Permits started this week and gated-in-time % | KPI-PRM-01, KPI-PRM-02 | SIPP Permits | Friday | Permit -> gates with timestamps | S |
| D2 | Perfect-week streak | KPI-PRM-03 | derived | Friday | Week that reset it | S |
| D3 | Permits closed with duration | KPI-PRM-04 | SIPP Permits | Friday | Permit -> close record | S |
| D4 | New permits next month by system | KPI-PRM-05 | SIPP Permits | Sunday | Permit -> roadmap row | S |
| D5 | Data-quality flags (inverted dates, missing contractor, duplicates) | KPI-PRM-06 | SIPP Permits | Friday | Row -> correction request | S |
| D6 | Work done, no record (R6) | KPI-PRM-07 | field reports x board | daily during work | Activity -> backfill status | M |
| **E** | **Asset and CMMS** | | | | | |
| E1 | Records delivered by file and convention | KPI-AST-01 | delivery Control sheets | Friday | File -> transmittal | S |
| E2 | Ready / hold / review by file | KPI-AST-02 | reconciliation tabs | Friday | Hold -> confirm ID | S |
| E3 | Open confirms with age | KPI-AST-03 | confirm register | Friday | Confirm -> rows it holds | S |
| E4 | Gate register G-nn status | KPI-AST-04 | PLN-EWO | Friday | Gate -> evidence needed | S |
| E5 | Days to hard deadline 10/30/26 with open gates | KPI-AST-05 | calendar; gates | Wednesday, Friday | Gate -> owner | S |
| E6 | Import status: live / rejected / pending, rejection log status | KPI-AST-06 | client import log | Friday | File -> rejection reasons | M |
| E7 | Tagging gate status (R8) | code stability confirmations | code scheme record | Friday | Gate -> written ruling | S |
| **F** | **Telemetry and engineering** | | | | | |
| F1 | Reservoir runway per rig | KPI-TEL-01 | CTRW metrics | Friday | Rig -> regression detail | S |
| F2 | Uptime % per rig | KPI-TEL-02 | CTRW metrics | Friday | Rig -> dark windows by class | S |
| F3 | Dark days classified | KPI-TEL-03 | dark-window table | Friday | Window -> evidence | S |
| F4 | Valve saturation watch | KPI-TEL-04 | CTRW metrics | Friday | Rig -> longest run | S |
| F5 | Zero-flow events | KPI-TEL-05 | CTRW metrics | Friday, daily when live | Event -> notice | S |
| F6 | Engineering notice register (FM- notices open, review dates) | notice list | `csl-technical-docs` | Friday | Notice -> evidence tables | M |
| **G** | **Governance and appropriation** | | | | | |
| G1 | Minutes issued within 2 business days | KPI-GOV-01 | minutes dates | monthly | Meeting -> issue date | S |
| G2 | Open action items aged | KPI-GOV-02 | action registers | Friday | Item -> owner -> last update | S |
| G3 | CAAR status (design / execution) per CAPEX project | KPI-GOV-04 | CARR tracker; intake replies | Friday | Project -> CAAR document | M |
| G4 | Record discrepancies open | KPI-GOV-03 | correction log | Friday | Discrepancy -> correction reply | S |
| G5 | BGP tollgate position per project | BGP trackers | Tollgate Review Tracker 3843202021805956 | Friday | Project -> checklist items | M |

## 3. Module card format

Each module prints as one card on the checklist page and one row on the build sheet:

```
[ ] A6  Milestones in the next 30 / 60 / 90 days by system
     KPI     START and END inside the window, grouped by E-GRP; count per bucket with the rows named
     Source  W77 Roadmap Master 2025-2032 (1059284113641348), parent rows; SIPP Permits (289677048237956) for permits inside the window
     Refresh Friday pull; Sunday pull for the look-ahead edition
     Drill   system -> rows (START, END, %, Health) -> permits on the row
     Effort  M (new grouping and figure; sources already pulled)
     Tier    rows past END inside the window carry A2 / R4 per csl-schedule-risk
```

## 4. Intake session agenda (30 minutes)

| Minutes | Item | Output |
|---|---|---|
| 0–5 | Role and the decisions this person makes weekly (what they approve, escalate, or schedule) | One sentence on the build sheet: "Decides: ..." |
| 5–15 | Walk the checklist; pick at most 8 modules; say why each | Ticks with a reason phrase each |
| 15–20 | Thresholds they care about that differ from the catalog default (never below the RED rules) | Threshold notes; any tightening recorded, loosening declined with the rule cited |
| 20–24 | Delivery channel (live view, Friday PDF page, both) and refresh expectation | Channel and cadence |
| 24–28 | Access: who else sees this view; access code or SSO group | Access line; codes issued separately, never on the sheet |
| 28–30 | Read back; sign the build sheet | Signed build sheet, version string set |

Corrections raised in the session are made on the menu itself and reissued with a version bump the same day, so the record shows what the recipient actually approved.

## 5. Build sheet (page 2)

| Field | Entry (W77 CRE engineering view, v1.1) |
|---|---|
| Recipient and role | CRE engineering counterpart (Koning view) |
| Decides | Engineering priorities across systems; which risks get an engineering owner; asset-data readiness for the maintenance transition |
| Modules selected | A1 look-ahead; A6 milestones 30/60/90 by system; A7 bow wave; B7 system risk heat; E2 ready/hold/review; E6 import status |
| Thresholds | Catalog defaults; A6 window 30/60/90 days; B7 highlights systems with any row >= 700 |
| Sources and refresh | Roadmap Master 1059284113641348 (Friday, Sunday); SIPP Permits 289677048237956; delivery Control sheets; client import log (Friday) |
| Delivery | Live view beside the executive view; not a PDF page |
| Access | Two access codes for the named view, issued by the CSL author; codes rotate on request |
| Version log | v1.0 issued; v1.1 same week: G3 corrected from CARR to CAAR (recipient's correction) |
| Signed | Recipient and CSL author, date |

## 6. Six module cards as issued (excerpt)

| Code | Name | KPI | Source | Refresh | Drill-down | Effort |
|---|---|---|---|---|---|---|
| A1 | Week look-ahead | Anchor rows with END dates; outer frame with provenance (tracker END versus date stated on a call) | CSL Tasks 7673437876080516; minutes | Sunday | Row -> transmittal or minutes item | S |
| A6 | Milestones next 30/60/90 days by system | Count of START and END per bucket per E-GRP; rows named | Roadmap Master 1059284113641348; SIPP Permits | Friday | System -> rows -> permits | M |
| A7 | Bow wave | Rows with END in the final program year; delta since last pull | Roadmap Master | Friday, monthly | Rows that moved into the final year | S |
| B7 | System risk heat | Max RPN C and count >= 700 per E-GRP; R1 rows marked | Roadmap Master; risk register | Friday | System -> rows -> mitigation | M |
| E2 | Ready / hold / review | Counts per class per delivered file; holds tied to confirm IDs | Reconciliation tabs of delivered files | Friday | Hold -> confirm -> owner | S |
| E6 | Import status | Live / rejected / pending per file; rejection log received or requested | Client import log | Friday | File -> rejection reasons | M |

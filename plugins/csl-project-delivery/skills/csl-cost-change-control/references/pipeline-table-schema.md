# Proposal-to-PO Pipeline Table Schema

The pipeline table is the Friday commercial view of every mitigation workstream that carries money. It is not a second tracker: status comes from the lifecycle step on the ST CHW/PCW System Mitigation Plan (Smartsheet 2158727850315652), dollars come from the CHW/PCW Containment Budget Tracker (Rev 4, D. Wolf), and the two are joined on the WS number at each pull. The lifecycle steps are read as defined in `csl-schedule-risk` 3.7 (pricing = step 9, execution = step 10, PO number written back to the row's "In Place" column).

## 1. Columns

| # | Column | Source | Rule |
|---|---|---|---|
| 1 | WS | Mitigation sheet | Canonical format `WS-<nn>.<nn>[.<nn>]`; rows in any other format (`WS209`) are listed in the defect footnote and excluded |
| 2 | Project IN | BGP / intake reply | Cite as issued (`IN 12896`); blank with "not yet assigned, <n> days since PDS" when intake is open |
| 3 | Scope | Mitigation sheet row title | One line; the row title, not a paraphrase |
| 4 | E-Group | Mitigation sheet | Blank is a defect (child rows missing E-Group) |
| 5 | Steps done of 10 | Mitigation sheet | Count of completed lifecycle steps |
| 6 | Current step | Mitigation sheet | Label as it appears on the sheet header, with the package's stage name in parentheses when they differ |
| 7 | Days at current step | Computed | Pull date − date the current step was entered; unknown entry date is a defect |
| 8 | Planning budget | Tracker Rev 4 | Per WS number; blank means the tracker has no row for this WS, which is itself reported |
| 9 | Proposal amount and date | Tracker / proposal | Latest proposal; earlier proposals in the row history |
| 10 | Vendor | Proposal | |
| 11 | Approval route | BGP / tracker | CAPEX (design CAAR, execution CAAR) or OPEX; the route decides which gates apply |
| 12 | Design CAAR status and date | CARR tracker 4463394158497668 | Not started / Submitted / Approved, with date |
| 13 | Execution CAAR status and date | CARR tracker | Same |
| 14 | Committed (PO) | PO record | PO amount; only an issued PO or executed contract counts |
| 15 | Δ versus planning | Computed | (Committed or latest proposal − Planning budget) / Planning budget; tier per R2 / A2 |
| 16 | PO number in place | Mitigation sheet "In Place" column, checked against the PO record | A PO number on the sheet with no matching PO record is a defect |
| 17 | Invoiced / paid to date | Paid Ledger or client actuals | Where available; otherwise "not available at <pull time>, source <name>" |
| 18 | Blocker | Recorded | One clause; blocked POs get the six-part callout |
| 19 | Owner | Mitigation sheet | One person |
| 20 | Target date | Mitigation sheet | The step target; past target is a `csl-schedule-risk` KPI |
| 21 | Tier (rule) | `csl-schedule-risk/references/tier-rules.md` | Never a tier without the rule |
| 22 | Source and pull time | This session | Sheet, ID, timestamp; tracker revision |

## 2. Join and QA

1. Join mitigation sheet rows to tracker rows on the WS number (column 1 to the tracker's Project ID / WS key). Report the count of rows that fail to join and why (format defect; missing tracker row).
2. Confirm every PO number in column 16 exists in the PO record with the same amount as column 14.
3. Confirm every CAPEX row with an IN has a row on the CARR tracker; a pipeline row with no CARR row is a finding.
4. Recompute column 15 in code; tiers follow from it.
5. Hash both source pulls; a tracker byte-identical to last week while sheet steps advanced is an A4 finding on the tracker.

## 3. Block roll-ups (reported above the table)

| Roll-up | Definition |
|---|---|
| Position | Median steps done; count of rows at each of steps 7, 8, 9, 10 |
| Committed versus planning | Sum of column 14 against sum of column 8 for priced rows; delta in dollars and % |
| Exceptions | Rows past step 9 with no PO number; rows whose committed exceeds planning; rows with a PO number that fails the PO-record check |
| Blocked POs | Count, total dollars, longest days blocked |
| Defects | ID-format failures, blank E-Group, blank baseline status, unknown step-entry dates |

## 4. Blocked-PO record (six parts, every week until released)

| Part | W77 example (WKR-36A R1 first report; 09/18/26 status) |
|---|---|
| Amount | $25,947.71 (WS-06.02 flush) |
| Days blocked | 18 days since first report 08/31/26 (WKR-36A R1) |
| Root cause as recorded | ASML requester of record out of office; PO cannot release without them |
| Exposure | WS-06.02 flush cannot start; TR2 exposure continues (rig telemetry dark since 07/19/26; bath instrumentation electrically faulted) |
| Unblock action | Delegate approver on the requisition path, requested through ASML |
| Owner | D. Wolf (CSL) |

Tier: AMBER (A3) while the block stands; RED (R4) if the flush milestone passes with no status change on the row.

## 5. Friday paragraph pattern

Position (median step, counts at 7 to 10), committed versus planning with the delta, exceptions by name, blocked POs with days, next week's movements with owners and dates. Plain voice for the C edition: no dash constructions, "purchase order" spelled out on first use, denominators on every count. Example text is in `SKILL.md` 3.3.

## 6. Rendering

Table per `csl-brand` Section 5 (Excel or PDF table): navy header, tier cells in the status colors of Section 1.4 with the tier word and rule present, numbers right-aligned with cents where the source has them, source line beneath. Steps-of-10 shown as a segmented bar in dashboards (`csl-dashboard-kpi`), as `7 / 10` in print.

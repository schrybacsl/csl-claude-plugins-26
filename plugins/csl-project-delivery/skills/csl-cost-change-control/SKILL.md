---
name: csl-cost-change-control
description: >
  Owner-side cost and change control: budget trackers and program rollups, forecast versus budget
  variance, the proposal-to-PO pipeline, change order and PCO review, pay application review,
  retainage, contingency, CAPEX gates, EVM S-curves, burn rate, cash flow, PO and invoice linkage,
  and the cost side of LOE proposals. Use it whenever someone asks "where are we on budget", "is
  this CO fair", "review this pay app", "PO status", "committed vs budget", "burn rate",
  "contingency", "what is blocked", or "variance", and whenever a cost figure will appear in a
  deliverable. Figures always need a cited source.
---

# CSL Cost and Change Control

Cost control on an owner's-representative engagement protects the owner's money by keeping three numbers honest at all times: what was approved (budget), what has been promised to others (committed), and what will be spent by the end (forecast). This skill defines the CSL budget-workbook standard, the proposal-to-PO pipeline method used on ASML W77, the CAPEX appropriation gates, the change order and pay application review methods, forecast-versus-budget reporting, earned value where it helps and where it misleads, contingency discipline, and the cost hand-off for level-of-effort proposals. Its outputs feed the Friday End-of-Week report (`csl-weekly-reporting`), stand-alone memos (`csl-executive-memo`), and KPI views (`csl-dashboard-kpi`). Tiers come from `csl-schedule-risk`; R2 (variance above 10%) is the rule this skill fires most.

---

## 1. Bottom line / when this runs

| Product | Cadence | Feeds |
|---|---|---|
| Pipeline status paragraph and table (proposal-to-PO, committed versus planning, blocked POs) | Friday, before the C edition | WKR-nnC mitigation and commercial section |
| Forecast versus budget variance table by E-GRP or workstream, quarterly cash flow versus plan | Friday; quarter close (W77 Q3 closes 09/30/26) | WKR-nnC; memo when R2 fires |
| Change order / PCO review with recommendation | Per submission | Owner decision record; CO log |
| Pay application review | Per requisition, before certification reaches the owner | Payment recommendation; paid ledger |
| CAAR and tollgate status per project | Weekly with the pipeline | Pipeline table; BGP tracker cross-check |
| Contingency and allowance log | Monthly and on every draw | Budget workbook; program master |
| Cost side of an LOE proposal | Per pursuit | `csl-bd-pursuits` |

The agent recommends; a named CSL person approves (csl-operating-rules, Section 9). Every cost figure in a deliverable comes from a pull or a document cited in the same deliverable.

---

## 2. Inputs and pulls

| Source | What this skill reads | QA before use |
|---|---|---|
| ST CHW/PCW System Mitigation Plan (Smartsheet 2158727850315652) | Lifecycle step per WS row, target date, owner, PO number in the "In Place" column | Mixed ID formats (`WS-22-01.01` versus `WS209`) and blank baseline statuses are data defects; count and exclude with a footnote (`csl-schedule-risk` 3.7) |
| CHW/PCW Containment Budget Tracker, Rev 4 (D. Wolf, CSL) | Planning budget, proposal amount, committed (PO) amount per Project ID / WS number | Confirm the revision on the file; key every row to the WS number, never to the title |
| W77 Roadmap Master 2025–2032 (1059284113641348) | Budget, Forecast 2025–2030, 2026–2028 quarterly columns, E-GRP, Constraints | Parent rows only; test the quarterly sum against the annual forecast on the same pull |
| BGP trackers (CARR 4463394158497668; Document Checklist 6755444325306244; Tollgate Review 3843202021805956; Workflow 4721471294230404) | CAAR status, checklist completeness, tollgate dates per IN | Match the IN to the WS row; a project on the pipeline with no CARR row is a finding |
| Client PO and invoice records (ERP extract or SharePoint, as provided) | PO number, date, amount, requester, approval status, invoices against it | Single entry per invoice; PO amount reconciles to committed |
| Contractor and vendor submissions (proposals, PCOs, G702/G703, lien waivers) | Quantum, backup, schedule impact claims | Contract terms first (markup caps, retainage, allowances) |
| Contract (C132 for CSL; A133 / A101 or purchase terms for the owner's vendors) | Markup limits, retainage, allowance and contingency language, notice periods | Installed `aia-contracts-capital-projects` skill for the article-level reading |

Record sheet name, ID, pull timestamp (ET), row count, and hash for every pull. When two fields on the same sheet disagree (annual forecast versus quarterly sum, tracker committed versus PO record), report both, name the discrepancy, and state the likely cause as a hypothesis to check; never reconcile silently.

Pull sequence for the Friday block, in this order so each step has what it needs:

1. Mitigation sheet, then the Containment Budget Tracker; join on WS number; log join failures.
2. PO and invoice records for the WS rows at steps 9 and 10; confirm every PO number in the "In Place" column exists in the PO record with a matching amount.
3. BGP trackers for every row with an IN; confirm the CAAR gates and checklist state.
4. Roadmap Master budget and forecast columns (parent rows) for the variance table; run the quarterly-sum test.
5. Contractor submissions received in the week (PCOs, requisitions) into their review queues with receipt dates.

---

## 3. Method

### 3.1 Owner's advocate stance

Read every proposal, change, and requisition as the owner's representative: the question is what the owner is entitled to under the contract and what protects the owner's budget, schedule, and scope. Contractor and vendor explanations are recorded as their position. Contract mechanics (A201 Article 7 changes, Article 9 payments, G-series forms, GMP negotiation, retainage law, markup ranges) are in the installed `aia-contracts-capital-projects` skill; cite its part numbers rather than restating them. This skill adds the owner's-side workflow and the record.

### 3.2 Budget structure standard (CSL standard from 08/2026)

Per-project budget workbook in six sections, rolling to a program Master. The structure was set by the Brown University Health Planning, Design and Construction requirements of 08/2026 (single-entry PO and invoice linkage was their largest pain point) and is the CSL standard for new programs going forward. Full column lists and roll-up formulas are in `references/budget-workbook-schema.md`.

| Section | Holds | Feeds |
|---|---|---|
| 1. Master | One row per budget line: original budget, adjustments, current budget, committed, invoiced, paid, forecast to complete, estimate at completion, variance | Program Master (one row per project) |
| 2. BA Detail | Budget authorizations funding the project: number, date, amount, phase, funding source, approver | Master original budget and authorized total |
| 3. Paid Ledger | Every invoice once: PO number, invoice number, vendor, amount, retainage, net paid, paid date, cost code | Committed Cost (invoiced and paid to date), Master (paid), cash flow actuals |
| 4. Budget Adjustments | Every movement of budget: transfers, approved COs, contingency draws, authorization changes, with reference numbers | Master current budget; contingency log |
| 5. Committed Cost | Every PO and contract: original value, approved COs, current value, invoiced, paid, remaining commitment, retainage held | Master committed; cash flow forecast (remaining commitment spread by schedule) |
| 6. Project Cost | Cost-code view: budget, committed, invoiced, paid, forecast to complete, EAC, variance, % complete by cost code | Master; EVM inputs where used |

Rules that make the structure work: an invoice is entered once, in the Paid Ledger, keyed to its PO, and flows to Committed Cost and Master by formula; a PO is entered once, in Committed Cost; budget moves only through Budget Adjustments with a reference (CO number, CAAR number, transfer memo); the change-order log and the risk log are kept per project in the same workbook and roll to the program master by union without renumbering (`csl-schedule-risk/references/risk-register-schema.md`, Section 4); cash flow is ledger-driven (actuals from paid dates, forecast from remaining commitments spread against the schedule), never typed.

The program Master carries one row per project with the project's Master totals, its schedule health from `csl-schedule-risk`, its tier, and the date of its last workbook update; a project whose workbook has not been updated in the reporting period shows as stale, not as unchanged. Roll-up identities that are checked in code before any issue:

1. Current budget = original budget + sum of Budget Adjustments for the line.
2. Committed = sum of current PO values (original + approved COs) in Committed Cost.
3. Invoiced and paid = sums from the Paid Ledger by PO; Committed Cost never holds typed invoice figures.
4. Estimate at completion = paid + unpaid invoiced + remaining commitment + forecast for uncommitted scope; variance = current budget − EAC.
5. Program totals = sums of project Master rows; a program figure that does not equal its project sum is a defect, not a rounding note.

Dashboard readings for the pipeline (used by `csl-dashboard-kpi`): each project shows steps complete of 10 as a segmented bar, committed dollars against planning budget as a paired figure, and the tier with its rule; a row past step 9 with no PO number in place shows as an exception, and a row whose committed exceeds planning shows its variance percentage rather than a color alone.

### 3.3 Proposal-to-PO pipeline

The mitigation sheet's 10-step lifecycle drives proposal-to-PO status; nothing is double-tracked. Pricing is step 9 and execution is step 10; when the PO issues, its number is written back to the project row in the "In Place" column, which is what closes step 10. The dashboard reads each project as steps complete of 10 plus committed dollars versus planning budget. D. Wolf maintains the CHW/PCW Containment Budget Tracker (Rev 4) keyed to Project ID / WS number; the pipeline table joins that tracker to the sheet on the WS number. The lifecycle table and the weekly KPIs are in `csl-schedule-risk` 3.7; the pipeline columns are in `references/pipeline-table-schema.md`.

Weekly method:

1. Pull the mitigation sheet and the tracker; join on WS number; list rows that fail to join (ID format defects) and exclude them with a count.
2. For each row: steps complete of 10; current step; days at current step; planning budget; proposal amount and date; committed (PO) amount; PO number in place or not; blocker.
3. Compute block roll-ups: rows at each step; committed total versus planning total; rows past step 9 with no PO number; rows whose committed exceeds planning (variance and tier per R2 / A2).
4. Identify blocked POs and report each in the six-part form below.
5. Write the Friday paragraph: block position (median step, count at each of steps 7 to 10), committed versus planning with the delta, blocked POs with days blocked, what moves next week and who owns it.

Pipeline table columns (full definitions in `references/pipeline-table-schema.md`): WS | Project IN | scope | E-Group | steps done of 10 | current step | days at step | planning budget (tracker Rev 4) | proposal amount and date | committed (PO) | Δ versus planning | PO number in place | CAAR status (design / execution) | blocker | owner | target date | tier (rule) | source and pull time.

The Friday paragraph reads, in the plain voice the C edition uses (values from the worked example in 6.1):

> The WS-22 block stands at a median of 7 steps complete of 10: one project in execution with its purchase order in place, one with its requisition raised and purchase order pending, two at pricing, two at proposal review, one at vendor request, and one at intake. Committed value is $146,730 against $809,200 of planning budget on the seven priced rows. One vendor price (WS-22.06) is 12.4% above planning and goes to a scope check before any requisition. Outside the block, the WS-06.02 flush purchase order of $25,947.71 has been blocked for 18 days; a delegate approver has been requested. Next week: WS-22.03 pricing due 09/25, WS-22.05 quotes due 09/30, and the design CAAR path for IN 12896 to be placed on the CARR tracker.

**Blocked-PO pattern.** A PO that cannot release is a schedule and exposure item, not a bookkeeping note. Report: amount; days blocked (from first report, with the first-report document); root cause as recorded; exposure (what cannot start and what that risks); unblock action; owner. The W77 case: a $25,947.71 flush PO blocked because the ASML requester of record was out of office and the PO could not release without them; root cause of the WS-06.02 delay; exposure on TR2 (rig telemetry dark since 07/19/26 with bath instrumentation electrically faulted); first reported in WKR-36A R1 (08/31/26); 18 days blocked at the 09/18/26 pull; unblock action, a delegate approver on the requisition path; owner, D. Wolf with the ASML requester's organization. Report the days-blocked count every week until the PO number appears in the "In Place" column.

### 3.4 CAPEX appropriation gates

On ASML programs a CAPEX project needs a Capital Asset Appropriation Request (CAAR) for design and a second CAAR for execution; both are required before the corresponding PO can issue. The term is CAAR; "CARR" in the BGP workspace is the Capital Appropriation Request Review tracker, a different thing, and the two are never interchanged (the KPI options menu was reissued as v1.1 to correct exactly that typo). Intake runs through the Project Definition Sheet (PDS) and User Requirements Specification (URS); the Building Governance Process (BGP) then tracks the project across four sheets: CARR tracker, Document Checklist, Tollgate Review, Workflow (`asml-pm-agent`, Part 12).

Track per project: PDS and URS revision and submission date; IN number assigned and date; design CAAR status and date; execution CAAR status and date; tollgate dates; document checklist completeness; the WS row the project belongs to.

Example, IN 12896, W77 Cooling Water Non-Contact Enhancements (WS-22.08): confirmed as a CRE project by intake reply on Mon 08/31/26 to D. Wolf's same-day PDS V2 and URS R1 submission; PM A. Pfordresher (ASML CRE) owns change management. Scope: replace four 3-way mixing valves with plate-and-frame heat exchangers, with a possible fifth in the W77 basement pending field verification. CAPEX, so design and execution CAARs are both required. Open items at 09/18/26: the vendor quote covers three of the four valves; the basement location needs field verification before the count is fixed; the CAAR path (design CAAR first) is not yet on the CARR tracker. Pipeline position: 6 of 10 steps complete; current step 7 (proposal under review); step 8 (funding) waits on the design CAAR. Report those three open items every week until closed, because each one moves the committed figure. The gate status block for the row:

| Gate | Status at 09/18/26 | Date | Document |
|---|---|---|---|
| PDS V2 and URS R1 submitted | Complete | 08/31/26 | D. Wolf submission; intake reply same day |
| IN assigned | Complete: IN 12896 | 08/31/26 | Intake reply |
| Scope count fixed | Open: 4 confirmed, possible 5th pending basement field verification | Verification not yet scheduled at 09/18/26 | Field report on verification |
| Vendor quote covers full scope | Open: 3 of 4 valves quoted | Requote requested | Vendor proposal |
| Design CAAR | Not started; not on CARR tracker | No target on record at 09/18/26; owner A. Pfordresher | CARR tracker 4463394158497668 |
| Execution CAAR | Not started | After design CAAR | CARR tracker |
| Document checklist | Not available at the 09/18/26 pull | Pulled with the next Friday block | Checklist 6755444325306244 |
| Execution PO | Not issued | After execution CAAR | "In Place" column on the WS-22.08 row |

### 3.5 Change order and PCO review

Review every proposed change in this order and write the finding for each; a change that fails an early test does not need the later ones priced, but the record shows all seven were considered. Contract mechanics per `aia-contracts-capital-projects` Part 3.5 (entitlement test, pricing methods, markup ranges) and Part 4.1 (G701, G714, G710). Template: `templates/change-order-review.md`.

| # | Test | Question | Evidence required |
|---|---|---|---|
| 1 | Entitlement | Is the work outside the contract documents and not reasonably inferable? Was notice given inside the contract period? | Drawing and spec references; RFI or notice with date |
| 2 | Causation | What event caused it, when, and who owns that event (owner direction, design omission, differing condition, contractor means and methods)? | Dated direction, RFI response, field report |
| 3 | Quantum | Are labor hours, rates, material quantities, unit prices, and equipment consistent with the backup and the contract rate table? | Itemized backup; quotes; certified rates |
| 4 | Schedule impact | Is a time extension claimed, and is it supported by a fragnet against the current schedule? Concurrent delay? | Schedule analysis with data date |
| 5 | Markup | Do overhead, profit, bond, and insurance percentages match the contract, and are they stacked only where the contract allows? | Contract markup clause; arithmetic re-run |
| 6 | Overlap | Does any part duplicate base scope, an allowance, a prior CO, or work already paid on a requisition? | SOV, CO log, paid ledger cross-check |
| 7 | Documentation | Signed proposal, backup, sub quotes, revised SOV lines, and the correct form (CO, CCD, ASI)? | Submission package |

Markup check, done in code every time: apply the contract percentages in the contract's order to the direct cost, compare to the submitted total, and report the difference as a numbered comment. Where the contract allows sub markup and GC markup on sub cost but not GC profit on GC overhead, a proposal that compounds the two is reduced to the contract arithmetic, and the comment shows both figures. Typical ranges and what to resist are in `aia-contracts-capital-projects` Part 3.5.

Recommendation language is fixed: "CSL is not in a position to recommend approval as submitted" followed by numbered comments, each with the test it failed, the dollar or day effect, and what would resolve it; or "CSL recommends approval in the amount of $X and Y days" when all seven pass. The owner decides. Log the PCO, the review date, the recommendation, and the decision in the project CO log (columns: PCO number, title, date received, requested $, requested days, tests failed, recommended $, recommended days, decision, decision date, CO number, budget adjustment reference), and the approved amount in Budget Adjustments. Schedule effects go to `csl-schedule-risk` for the variance record.

### 3.6 Pay application and requisition review

Review each G702 / G703 before certification reaches the owner, per the checklist in `templates/pay-app-review-checklist.md` and `aia-contracts-capital-projects` Part 4.2 and Part 3.7. The checks that catch money:

1. Continuation sheet arithmetic re-run in code: scheduled value, previous, this period, stored, total to date, %, balance, retainage per line; totals tie to the G702.
2. Previous certified totals reconcile to the last certified application and to the paid ledger; a mismatch stops the review.
3. Work in place verified against the field report for the period (`csl-design-construction-oversight`); % complete claimed above what the field shows is reduced, with the line and the evidence named.
4. Stored materials: invoice, title, insurance, location, and a bill of sale for off-site storage; no documentation, no payment on that line.
5. Retainage: percentage per contract on each line and on stored materials; any reduction only by written owner approval; retainage held reconciles to the ledger.
6. Lien waivers: conditional for this period, unconditional for the prior period, from the contractor and every sub above the contract threshold; missing waivers are a withholding basis.
7. Schedule of values front-loading: early lines (mobilization, general conditions, submittals) billed ahead of physical progress; compare cumulative % billed to cumulative % complete by trade.
8. Change orders: only approved COs appear as new lines; pending PCOs are not billed.

The arithmetic that must tie on the G702, re-run from the G703 lines rather than read from the cover: total completed and stored to date; less retainage (work in place at the contract percentage, stored materials at the contract percentage, which may differ); total earned less retainage; less previous certificates for payment; current payment due; balance to finish including retainage. A cover whose "previous certificates" line does not equal the last certified application is returned before any other check. The tie, with illustrative figures at 10% retainage on work and 10% on stored materials:

| Line | Figure |
|---|---|
| Total completed and stored to date (G703 column G total) | $1,284,500.00 |
| Retainage: 10% of $1,204,500.00 work in place + 10% of $80,000.00 stored | $128,450.00 |
| Total earned less retainage | $1,156,050.00 |
| Less previous certificates for payment (must equal last certified application) | $1,012,300.00 |
| Current payment due | $143,750.00 |
| Balance to finish, including retainage (contract sum to date less total earned less retainage) | Contract sum less $1,156,050.00 |

Any line that does not reproduce from the continuation sheet is a numbered comment; a retainage percentage lower than the contract's without a written owner approval is a withholding basis.

Output: a recommendation of the certified amount, the lines reduced with reasons, retainage held, and the withholding notice text if any (in writing, every time, per A201 §9.5). Enter the certified invoice once in the Paid Ledger when paid.

### 3.7 Forecast versus budget

Compute variance at every level the owner reads: cost line, workstream, E-GRP, program year. Variance = forecast minus budget, in dollars and as a percentage of budget. Tier per `csl-schedule-risk`: R2 above 10%, A2 between 5% and 10%, GREEN below. The March 2026 W77 baseline is the comparison point until the live pull replaces it: 2026 forecast $159.1M; 2026 quarterly plan Q1 $42.5M, Q2 $41.6M, Q3 $76.7M, Q4 $32.9M; peak year 2027 at $181.6M; program $753.4M (`asml-pm-agent`, Part 4).

Test the baseline itself before using it: the four 2026 quarterly figures sum to $193.7M against a Forecast 2026 of $159.1M on the same snapshot, a 21.7% gap between two fields that should agree. Report both figures and the gap; the likely cause is child rows (phases) summed into the quarterly columns while the annual column counts parents only, and the test is to re-sum parent rows on the live pull. Do not carry either figure into a report as "the 2026 plan" without that note.

Quarterly cash flow versus plan: actual (paid ledger by paid date, or the client's actuals extract) against the quarterly plan; cumulative curve; the gap in dollars and as a percentage of the plan to date; the three largest contributors named. Present variance tables with these columns: group | items | budget | forecast | variance $ | variance % | tier (rule) | cause (one clause) | source. Sort by absolute variance descending.

Quarter-close routine (W77 Q3 closes 09/30/26): pull the roadmap on the close date and again on the first Friday after it, hash both; freeze the quarter's forecast columns in the report snapshot; compute actual versus plan for the quarter and cumulative for the year; list every E-GRP and workstream whose forecast moved between the two pulls with the movement and the cause; carry any R2 into the next C edition headline and a memo. A forecast column that changes after the close without a re-baseline entry is reported as an A6 record discrepancy.

### 3.8 Earned value and burn rate

Use the standard quantities and state the data date with every figure:

| Quantity | Definition | Source in the workbook standard |
|---|---|---|
| PV (planned value) | Budgeted cost of work scheduled to date | Project Cost forecast phasing or the capital plan by month |
| EV (earned value) | Budgeted cost of work actually performed to date | % complete per cost code (field-verified) x current budget |
| AC (actual cost) | Cost incurred for the work performed to date | Paid Ledger plus accrued invoices, by period |
| SPI | EV / PV | Below 1.0 means behind plan |
| CPI | EV / AC | Below 1.0 means over cost |
| EAC | BAC / CPI while the cause of variance continues; AC + (BAC − EV) when it is closed | Report which form was used and why |
| Burn rate | AC per month against the plan's PV per month | Bar under the S-curve |

Plot PV, EV, and AC as an S-curve per project and per program with the data date marked; burn rate is AC per month against the capital plan's monthly PV, shown as a bar under the curve.

EVM is meaningful when physical progress is measured independently of cost (an SOV with field-verified % complete, a schedule with a data date) and when PV is a fixed baseline. It misleads on procurement-heavy programs and portfolios like W77 in their design and buyout years: AC jumps at PO or delivery while EV is flat, EV rests on vendor-reported milestones, and the "plan" is a forecast column that moves every quarter, so SPI and CPI describe the forecast, not performance. In those conditions report committed versus planning budget, steps complete of 10, and cash flow versus plan, and reserve SPI / CPI for projects in construction with a certified SOV. Say which regime a chart is in, in its caption.

### 3.9 Contingency, allowances, and scope substitution

Keep one contingency and allowance log per project, rolling to the master. A draw exists only with a documented change; a contingency balance that falls while % complete stands still is a finding. Allowances reconcile at closeout to actual cost with the credit or debit shown.

| Column | Rule |
|---|---|
| Line | Owner contingency, CM contingency, design contingency, and each allowance as its own line; owner and CM contingency are never merged |
| Original amount | From the GMP or budget authorization, with the document cited |
| Draw date, reference, amount, reason | One row per draw; reference is a CO number, CCD number, or Budget Adjustment ID |
| Remaining | Original less draws, by formula |
| Remaining vs work remaining | Remaining contingency as a percentage of forecast to complete; report when it falls below the % of work remaining |
| Allowance reconciliation | Actual cost against allowance at closeout; credit or debit to the owner shown |

Scope substitution rule (csl-operating-rules, Section 8): new scope, supplements, and "while we are in there" items get a new row, a new number, and a budget line, or are declined in writing. Nothing rides an existing row; a row whose scope grew without a new number is reported as a data defect and an exposure until corrected.

### 3.10 LOE proposal hand-off

When a level-of-effort proposal is owed (W77: the BCA + IRO merged, maintained tracker requested by B. Gannon 09/18/26, proof of concept built 09/17/26 with 348 records), this skill produces the cost side and `csl-bd-pursuits` produces the document (`CSL-W77-LOE-yymmdd`). Cost side: hours by role and by task, with the basis for each estimate; the rate table referenced by contract and edition, never retyped; assumptions (data sources, update cadence, client responsibilities); exclusions (scope not priced); fee summary by phase and month; what triggers a change in fee. Rates and fee totals are reviewed by E. Hubert before the document issues.

| LOE cost-side element | Content |
|---|---|
| Task list | Numbered tasks with the deliverable each produces and its cadence (one-time build, weekly maintenance, monthly PMO / IMT update) |
| Hours by role | Per task: Project Manager, Assistant Project Manager, data or dashboard specialist, Project Director review; basis stated (rows, sheets, meetings) |
| Rate reference | Contract and edition that governs the rates; no rates retyped into the memo |
| Assumptions | Client provides source sheets and access; update cadence; number of review cycles |
| Exclusions | Scope not priced (new data sources, software licensing, on-site walk-downs unless listed) |
| Fee summary | By phase and by month; change triggers (scope, cadence, data-source count) |

### 3.11 Weekly routine (Friday, before the C edition)

1. Run the pull sequence in Section 2; log hashes and join failures.
2. Refresh the pipeline table; compute block roll-ups; write the six-part callout for every blocked PO with its days-blocked count.
3. Refresh the variance table by E-GRP and workstream; run the quarterly-sum test; tier every row; any R2 goes to the headline and a memo draft.
4. Review PCOs and requisitions received in the week against 3.5 and 3.6; log recommendations; queue owner decisions.
5. Update the contingency and allowance log for any draw; confirm every draw has its Budget Adjustments row.
6. Update the CAAR and tollgate block for every project with an IN; flag projects on the pipeline with no CARR row.
7. Hand the schedule effects (days, slipped milestones) and the exposure figures to `csl-schedule-risk` for the register.
8. Write the Friday paragraph; file the pull snapshot with the edition per `csl-document-control`.

---

## 4. Output specification

**Friday pipeline block** (WKR-nnC): bottom line first (block position, committed versus planning, blocked POs), then the pipeline table per `references/pipeline-table-schema.md`, then the blocked-PO callouts, then the docket rows. Numbers with denominators: "6 of 8 rows at step 8 or beyond; committed $X of $Y planning".

**Variance table**: columns per 3.7; total row; tier per row; a note on any two-field discrepancy; source line with sheet, ID, pull timestamp.

**CO review memo**: `CSL-<PROG>-MEM-yymmdd`; template in `templates/change-order-review.md`; recommendation sentence first.

**Pay app review**: checklist completed, certified amount recommended, reductions listed, withholding text; filed with the requisition.

**Contingency log extract**: monthly in the C edition; remaining versus % complete in one line.

**Program master status page** (multi-project programs): one row per project with current budget, committed, paid, EAC, variance, tier (rule), schedule health, last workbook update; stale rows flagged; totals row tied to the project sum.

**Blocked-PO callout**: the six parts (amount, days blocked with first-report document, root cause as recorded, exposure, unblock action, owner) as one short paragraph, repeated weekly until the PO number is in place.

**Cash-flow and S-curve charts**: per `csl-brand` Section 6 (navy PV, dark teal EV, teal AC; source line; finding in the title); regime stated in the caption per 3.8.

Document control per `csl-document-control`; all figures in a record carry cents where the source does.

---

## 5. Voice and formatting rules

- Amounts exact in records ("$25,947.71"); rounding in a headline only when the exact figure is in the body. Percentages carry their base ("7.3% of $34.75M").
- Every cost figure carries its source and date in the same table or sentence.
- Contractor and vendor positions are attributed: "MMI claims 6 days of delay; the fragnet supports 2."
- Recommendation language is fixed (3.5); approval is the owner's; CSL "recommends", never "approves".
- Client-executive editions: no dash constructions in running prose; acronyms spelled out on first use per page (Purchase Order, Capital Asset Appropriation Request).
- Discrepancies between two sources are named with both figures, never blended.

---

## 6. Worked example

### 6.1 Pipeline status, WS-22 Tiger Team / BGP block, 09/18/26 pull

Eight BGP projects on identical lifecycles. Row facts for WS-22.04 and WS-22.08 are from the program record; the status and dollar values on the other six rows are illustrative of the format and are refreshed from the mitigation sheet and Containment Budget Tracker Rev 4 before issue.

| WS | Scope | Steps done / 10 | Current step | Planning budget | Committed (PO) | Δ vs planning | PO in place | Blocker / note | Owner | Tier (rule) |
|---|---|---|---|---|---|---|---|---|---|---|
| WS-22.01 | PCW emergency action (Veldhoven list) | 10 | Execution | $148,200 | $146,730 | −1.0% (PO) | Yes | None | D. Wolf | GREEN (G) |
| WS-22.02 | PCW emergency action (Veldhoven list) | 9 | Execution: PO pending | $96,500 | $0 | n/a | No | Requisition raised 09/15; PO not yet issued | D. Wolf | GREEN (G) |
| WS-22.03 | PCW emergency action (Veldhoven list) | 8 | Pricing | $212,000 | $0 | n/a | No | Funding approved; final pricing due from vendor 09/25 | D. Wolf | GREEN (G) |
| WS-22.04 | Ex WS-01.02.01, moved out from under Nalco | 6 | Proposal under review | $74,800 | $0 | n/a | No | Proposal received; CSL review comments due 09/23 | S. Schryba | GREEN (G) |
| WS-22.05 | PCW emergency action (Veldhoven list) | 5 | Vendor request issued | $58,300 | $0 | n/a | No | Quotes due 09/30 | D. Wolf | GREEN (G) |
| WS-22.06 | PCW emergency action (Veldhoven list) | 8 | Pricing | $131,400 | $0 | +12.4% (proposal $147,694) | No | Vendor price above planning; scope check before requisition | D. Wolf | RED (R2) |
| WS-22.07 | PCW emergency action (Veldhoven list) | 4 | Intake | $88,000 | $0 | n/a | No | PDS submitted; IN not yet assigned, 16 days | D. Wolf | AMBER (A3) |
| WS-22.08 | Non-Contact Enhancements: four 3-way mixing valves to plate-and-frame HX; possible fifth pending field verification (IN 12896) | 6 | Proposal under review; design CAAR next | Per tracker Rev 4 | $0 | n/a | No | Quote covers 3 of 4 valves; basement verify open; CAAR path not on CARR tracker | D. Wolf; A. Pfordresher (ASML) | AMBER (A3) |

Block roll-up (steps done = completed steps; current step = the next one): 1 of 8 complete at step 10; 1 of 8 at step 10 with PO pending; 2 of 8 at step 9; 2 of 8 at step 7; median steps done 7.0; committed $146,730 against illustrative planning $809,200 for the seven priced rows. One R2 (WS-22.06, vendor price above planning by more than 10%) goes to the docket with a scope check before any requisition.

**Blocked PO callout (outside the WS-22 block).** WS-06.02 flush PO, $25,947.71. Blocked 18 days at the 09/18/26 pull, first reported WKR-36A R1 (08/31/26). Root cause as recorded: ASML requester of record out of office; PO cannot release without them. Exposure: WS-06.02 flush cannot start; TR2 exposure continues (rig telemetry dark since 07/19/26). Unblock action: delegate approver on the requisition path, requested through ASML. Owner: D. Wolf. Tier: AMBER (A3), becomes RED (R4) if the flush milestone passes with no status change.

### 6.2 Forecast versus budget by E-GRP, March 2026 baseline snapshot

Baseline budgets and item counts are from the March 2026 snapshot (`asml-pm-agent`, Part 4.3). The snapshot carried no per-E-GRP forecast, so the forecast, variance, and tier columns populate only from a live pull of sheet 1059284113641348; they are left blank rather than estimated. The threshold columns are computed from the budgets and tell the reader how large a forecast movement fires each rule.

| E-GRP | Items | Budget ($M) | Share of listed | A2 fires above ($M, 5%) | R2 fires above ($M, 10%) | Forecast ($M, live pull) | Variance $ / % | Tier (rule) |
|---|---|---|---|---|---|---|---|---|
| Facility | 7 | 85.00 | 31.7% | 4.250 | 8.500 | | | |
| AHU | 91 | 60.95 | 22.8% | 3.047 | 6.095 | | | |
| Roof | 19 | 51.25 | 19.1% | 2.563 | 5.125 | | | |
| Mech Piping | 6 | 34.75 | 13.0% | 1.738 | 3.475 | | | |
| Electrical | 35 | 24.50 | 9.2% | 1.225 | 2.450 | | | |
| Fan | 91 | 6.48 | 2.4% | 0.324 | 0.648 | | | |
| Chillers | 8 | 2.08 | 0.8% | 0.104 | 0.208 | | | |
| Nitrogen | 4 | 1.95 | 0.7% | 0.097 | 0.195 | | | |
| Sanitary | 4 | 0.77 | 0.3% | 0.038 | 0.077 | | | |
| Listed total | 265 | 267.73 | 100% | | | | | |

Notes for the reader: nine of 17 E-GRPs carried budgets in the snapshot table (the listed total is 35.5% of the $753.4M program); the remaining eight are pulled live. Program-level check on the same snapshot: Forecast 2026 $159.1M against a 2026 quarterly sum of $193.7M (Q1 $42.5M, Q2 $41.6M, Q3 $76.7M, Q4 $32.9M), a 21.7% two-field discrepancy reported as an A6 data finding until the parent-row re-sum resolves it; peak year 2027 at $181.6M. Live pulls are required before any of these figures are issued as current.

---

## 7. Failure modes and how to avoid them

| Failure | What it looks like | Avoidance |
|---|---|---|
| Double-tracking the pipeline | A separate PO spreadsheet drifts from the mitigation sheet | Lifecycle step on the sheet is the status; the tracker holds dollars; join on WS number |
| Keying on titles | Two rows for one project because the title was retyped | Project ID / WS number is the key everywhere |
| Treating a quote as a commitment | "Committed" includes unissued quotes | Committed = PO or executed contract only; quotes are pipeline |
| Carrying a blocked PO as bookkeeping | The block is a footnote for three weeks | Six-part callout weekly with days blocked, until the PO number is in place |
| "CARR" for CAAR | A CAPEX gate named after a tracker | CAAR is the appropriation; CARR is the BGP review tracker |
| One CAAR for a CAPEX project | Execution PO requested on a design CAAR | Design and execution CAARs tracked as separate dated gates |
| Averaging two sources | A "2026 plan" that is neither the annual nor the quarterly figure | Both figures, the gap, the hypothesis, the test |
| Approving language | "CSL approved the CO" in a report | CSL recommends; the owner approves; the log records both |
| Paying on unverified % complete | Pay app certified from the G703 alone | Field report for the period against every line above threshold |
| Stacked markup | OH&P on sub OH&P on bond | Contract clause cited; arithmetic re-run; excess as a numbered comment |
| Scope riding a row | HX fifth valve priced inside the four-valve row without a change | New row or written change; count fixed by field verification first |
| Contingency without a draw record | Balance falls; no adjustment row | Every draw through Budget Adjustments with a reference |
| EVM in the wrong regime | CPI reported on a buyout-phase portfolio as performance | Regime stated; committed versus planning used instead |

---

## 8. Pre-issue checklist

- Every figure traces to a pull or a cited document from this session; timestamps and sources in the table or source note.
- Arithmetic re-run in code: variances, percentages, continuation-sheet totals, markups.
- Tiers carry rule IDs (`csl-schedule-risk/references/tier-rules.md`); R2 items are in the headline.
- Committed means PO or executed contract; quotes and requisitions are labeled as pipeline.
- Blocked POs reported in six parts with days blocked.
- CAAR spelled correctly; design and execution gates shown separately; IN numbers cited as issued.
- Two-source discrepancies named with both figures.
- Recommendation language fixed; no "approved" attributed to CSL.
- New scope has a new row and number or a written decline.
- Dates calendar-checked; MM/DD/YY in the body; ISO in file names.
- Brand QA run (`csl-brand`); chart series order and status colors correct; document number per `csl-document-control`.

---

## Files in this skill

- `templates/change-order-review.md` — the seven-test review memo skeleton with fixed recommendation language and a populated example.
- `templates/pay-app-review-checklist.md` — requisition review checklist with arithmetic, verification, and withholding sections.
- `references/budget-workbook-schema.md` — the six-section per-project workbook and program master: column lists, keys, and roll-up formulas described.
- `references/pipeline-table-schema.md` — proposal-to-PO pipeline columns, joins, KPIs, and the blocked-PO record.

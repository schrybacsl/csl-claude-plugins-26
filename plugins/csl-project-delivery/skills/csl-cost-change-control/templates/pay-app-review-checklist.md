# Pay Application / Requisition Review Checklist

Complete for every G702 / G703 (or the vendor's equivalent requisition) before certification reaches the owner. File the completed checklist with the requisition; enter the certified invoice once in the Paid Ledger when paid. Contract mechanics per the installed `aia-contracts-capital-projects` skill (Part 3.7 Article 9; Part 4.2 monthly checklist). Example entries are illustrative and are not program records.

---

**Requisition review** | Project <name and ID> | Contractor <name> | Application No. <n> | Period to <MM/DD/YY> | Received <MM/DD/YY> | Reviewer S. Schryba, CSL Consulting | Time zone ET

## A. Before the math

| # | Check | Result | Note |
|---|---|---|---|
| A1 | Correct form (G702 cover, G703 continuation) and signed by the contractor; notarized where the contract requires | Pass | Application 5, signed 09/25/26 |
| A2 | Schedule of values matches the last approved SOV; any new lines are approved COs only | Fail | Line 31 "Coordination" added without a CO; removed from this review |
| A3 | "Previous certificates for payment" equals the last certified application and the Paid Ledger | Pass | $1,012,300.00 both sources |
| A4 | Approved change orders reflected in the contract sum; pending PCOs not billed | Pass | CO-01 and CO-02 included; PCO-007 not billed |
| A5 | Retainage percentage per contract on work and on stored materials | Pass | 10% and 10% per Article 5 |
| A6 | Lien waivers: conditional for this period, unconditional for the prior period, contractor and subs above the contract threshold | Fail | Mechanical sub prior-period unconditional waiver missing |
| A7 | Certified payrolls attached where the project is prevailing wage | n/a | Not a prevailing-wage contract |
| A8 | Insurance certificates current through the period | Pass | Expires 12/31/26 |

## B. Arithmetic (re-run in code from the G703 lines)

| # | Check | Result | Note |
|---|---|---|---|
| B1 | Each line: previous + this period + stored = total to date; % = total / scheduled value; balance = scheduled − total | Pass | 34 lines re-summed |
| B2 | No line above 100% | Pass | |
| B3 | Column totals tie to the G702 lines 4 through 9 | Pass | |
| B4 | Retainage held = contract % x work in place + contract % x stored materials | Pass | $130,325.00 as submitted (10% of $1,223,250.00 work + 10% of $80,000.00 stored) |
| B5 | Current payment due = total earned less retainage − previous certificates | Pass | $1,172,925.00 − $1,012,300.00 = $160,625.00 as submitted |
| B6 | Balance to finish including retainage = contract sum to date − total earned less retainage | Pass | |

## C. Verification against the field

| # | Check | Result | Note |
|---|---|---|---|
| C1 | % complete on every line above the review threshold compared to the field report for the period (`csl-design-construction-oversight`) | Fail | Line 14 insulation ($75,000.00 scheduled) billed 80%; field report FR-15 (09/24/26) shows 55%; reduce by $18,750.00 gross |
| C2 | Front-loading: cumulative % billed on early lines (mobilization, general conditions, submittals) against cumulative % complete by trade | Watch | General conditions at 62% billed against 48% time elapsed; note for next application |
| C3 | Stored materials on site: seen, tagged to the project, protected; invoice attached | Pass | HX skids, $80,000.00, seen 09/24/26 |
| C4 | Stored materials off site: bill of sale, insurance naming the owner, bonded warehouse or owner access, photographs | n/a | None claimed |
| C5 | Work claimed on lines covered by a pending PCO dispute | Pass | None |
| C6 | Defective or rejected work billed as complete | Pass | None open on the deficiency log |

## D. Result

| Item | Figure |
|---|---|
| Amount requested | $160,625.00 |
| Reductions | Line 14 −$18,750.00 gross, −$16,875.00 net of 10% retainage (C1); line 31 removed, no value billed yet (A2) |
| Retainage held after correction | $128,450.00 cumulative (10% of $1,204,500.00 work + 10% of $80,000.00 stored) |
| Amount recommended for certification | $143,750.00 ($1,156,050.00 earned less retainage − $1,012,300.00 previous) |
| Withholding notice required | Yes: line 14 reduction and missing prior-period waiver (A6); text below, issued in writing per A201 §9.5 |
| Owner decision requested by | <MM/DD/YY> |

Withholding notice text (fixed form): "The owner withholds $16,875.00 from Application No. 5 (line 14, insulation, reduced from 80% to 55% complete, $18,750.00 gross less retainage) on the basis of the 09/24/26 observation recorded in field report FR-15, and conditions payment on receipt of the mechanical subcontractor's unconditional lien waiver for Application No. 4. The withheld amount will be released on the next application upon verification."

## E. Record

| Field | Entry |
|---|---|
| Paid Ledger row (on payment) | Invoice Application 5 | PO <number> | $143,750.00 net | paid date <MM/DD/YY> | retainage held $128,450.00 |
| Committed Cost update | Invoiced to date and paid to date roll by formula from the ledger |
| Documents relied on | G702/G703 Application 5 (09/25/26); FR-15 (09/24/26); SOV rev 2; lien waiver register; CO log |
| Next application watch items | Front-loading on general conditions (C2); line 14 re-verification; waiver A6 |

---

Pre-issue: every Fail has a reduction or a condition; arithmetic file saved with the review; withholding text in writing; certified amount stated once; no "approved" attributed to CSL; brand QA per `csl-brand`; filed per `csl-document-control`.

# Budget Workbook Schema (per-project, six sections, rolling to a program Master)

The CSL standard for capital-project budget workbooks from 08/2026, set by the Brown University Health Planning, Design and Construction requirements (E. Frias and Ryan, 08/24/26 feedback round; single-entry PO and invoice linkage was the client's largest pain point) and adopted for new CSL programs going forward. One workbook per project; one program Master workbook that reads the project Masters. Render per `csl-brand` Section 5 (Excel): `Control` sheet first, navy header rows, frozen headers, filters on, live formulas unless the file is an import.

## 0. Control sheet (every workbook)

Document number (`CSL-<PROG>-TRK_<project>_<yyyy-mm-dd>.xlsx` per `csl-document-control`), revision, project ID and name, campus / building, PM, prepared by, source systems and pull dates, column dictionary, change log (`MM/DD/YY: what changed`).

## 1. Master (one row per budget line)

| Column | Type | Rule |
|---|---|---|
| Budget line ID | Text key | `<ProjectID>-<nn>`; never reused |
| Cost code | Picklist | Owner's chart of accounts (or MasterFormat division where the owner has none; `masterformat-2018` skill) |
| Description | Text | |
| Original budget | Currency | = sum of BA Detail allocations to this line at first authorization |
| Adjustments | Currency | = SUMIFS(Budget Adjustments amount, line = this line) |
| Current budget | Currency | = Original budget + Adjustments |
| Committed | Currency | = SUMIFS(Committed Cost current PO value, line = this line) |
| Invoiced to date | Currency | = SUMIFS(Paid Ledger gross amount, line = this line) |
| Paid to date | Currency | = SUMIFS(Paid Ledger net paid, line = this line) |
| Retainage held | Currency | = SUMIFS(Paid Ledger retainage withheld, line) − SUMIFS(Paid Ledger retainage released, line) |
| Remaining commitment | Currency | = Committed − Invoiced to date |
| Forecast, uncommitted scope | Currency | Typed by the PM with a basis note; the only typed forecast figure in the sheet |
| Estimate at completion (EAC) | Currency | = Invoiced to date + Remaining commitment + Forecast, uncommitted scope |
| Variance | Currency and % | = Current budget − EAC; % of Current budget; tier per `csl-schedule-risk` (R2 > 10%, A2 5–10%) |
| % committed / % paid | % | Committed / Current budget; Paid / Current budget |
| Notes | Text | Basis of forecast; open PCOs affecting the line |

Totals row = project totals; these are the figures the program Master reads.

## 2. BA Detail (budget authorizations)

Records the authorizations that fund the project (capital authorization requests, board approvals, CAAR equivalents on other clients). The term "BA" follows the client's usage for budget authorization; where a client uses a different name, keep the sheet name and note the client term on the Control sheet.

| Column | Rule |
|---|---|
| BA number | Client's authorization number as issued; never renumbered |
| Date approved | MM/DD/YY |
| Phase | Planning / Design / Construction / Closeout |
| Amount | Currency |
| Funding source | Capital plan year, grant, operating transfer |
| Approver | Name and title |
| Allocation to budget lines | One row per line allocation; sums to the BA amount |
| Status | Requested / Approved / Amended / Closed |
| Document | Link or file name of the approval |

Authorized total = sum of approved BA amounts; Master original budget = allocations at first authorization; later authorizations enter through Budget Adjustments with the BA number as reference.

## 3. Paid Ledger (every invoice, once)

| Column | Rule |
|---|---|
| Ledger ID | Sequential |
| PO number | Must exist in Committed Cost; validation rejects unknown POs |
| Budget line ID | Inherited from the PO; override only with a note |
| Vendor | From the PO |
| Invoice number | Vendor's number as issued |
| Invoice date; period covered | MM/DD/YY |
| Application number | For G702/G703 requisitions |
| Gross amount | Total earned this period before retainage |
| Retainage withheld | Per contract % (work and stored materials may differ) |
| Retainage released | On reduction or final payment, with the approval document |
| Net paid | = Gross − Retainage withheld + Retainage released |
| Paid date; payment reference | MM/DD/YY; check or ACH reference |
| Reviewed by; review document | Reviewer initials; checklist file name (`templates/pay-app-review-checklist.md`) |
| Status | Received / Under review / Certified / Paid / Withheld (with notice reference) |

An invoice is entered here and nowhere else. Committed Cost and Master read it by formula. Cash-flow actuals are this sheet grouped by paid date.

## 4. Budget Adjustments (every movement of budget)

| Column | Rule |
|---|---|
| Adjustment ID | `BA-<nnn>` |
| Date | MM/DD/YY |
| Type | Transfer between lines / Approved CO / Contingency draw / Authorization change / Allowance reconciliation |
| From line; To line | Budget line IDs; a draw from contingency has From = contingency line |
| Amount | Currency; transfers net to zero across the two rows |
| Reference | CO number, CCD number, BA number, transfer memo number |
| Approved by; date | Name; MM/DD/YY |
| Note | Reason in one clause |

Current budget on Master reads this sheet; the contingency log is a filtered view of it (Type = Contingency draw) plus the original contingency amounts.

## 5. Committed Cost (every PO and contract, once)

| Column | Rule |
|---|---|
| PO / contract number | As issued by the owner's system; the key the Paid Ledger validates against |
| Vendor | |
| Budget line ID | |
| Description | Scope in one line |
| Original value | Currency |
| Approved COs | = SUMIFS(CO log approved amount, PO = this PO) |
| Current value | = Original value + Approved COs |
| Invoiced to date | = SUMIFS(Paid Ledger gross, PO) |
| Paid to date | = SUMIFS(Paid Ledger net paid, PO) |
| Retainage held | = SUMIFS(Paid Ledger withheld, PO) − SUMIFS(Paid Ledger released, PO) |
| Remaining commitment | = Current value − Invoiced to date |
| Expected spend by month | Remaining commitment spread across the PO's schedule (typed curve or linear to the PO end date); feeds cash-flow forecast |
| Status | Issued / In progress / Closed |
| Lifecycle link (W77) | WS number and step; PO number also written to the mitigation sheet "In Place" column |

## 6. Project Cost (cost-code view)

A pivot of Master by cost code with the same columns (budget, adjustments, current, committed, invoiced, paid, forecast to complete, EAC, variance, % complete). % complete by cost code is field-verified where the code is under construction and is the EV input where EVM is used (`SKILL.md` 3.8).

## 7. Logs kept in the same workbook

- **CO log**: PCO number, title, date received, requested $ and days, tests failed (1–7), recommended $ and days, decision, decision date, CO number, Budget Adjustments reference. Rolls to the program CO log by union.
- **Risk log**: the 25-field schema in `csl-schedule-risk/references/risk-register-schema.md` plus Project ID; rolls to the program register by union.
- **Contingency and allowance log**: filtered view of Budget Adjustments plus original amounts; remaining versus % of work remaining.

## 8. Program Master

One row per project, reading each project's Master totals: current budget, committed, invoiced, paid, EAC, variance $ and %, tier (rule), contingency remaining, % complete, schedule health (from `csl-schedule-risk`), last workbook update. Roll-up checks run before issue: program totals equal the sum of project rows; every project row's update date is inside the reporting period or the row is flagged stale; no project Master shows a Paid figure that exceeds Invoiced or an Invoiced figure that exceeds Committed without a note.

## 9. Cash flow (ledger-driven)

- Actuals by month = Paid Ledger net paid grouped by paid date (or gross, if the owner reports on accrual; state which).
- Forecast by month = Committed Cost expected spend by month for remaining commitments + Master forecast for uncommitted scope, phased by the schedule.
- Plan by month = BA Detail phase amounts spread by the approved schedule, or the client's capital plan where one exists.
- Chart: cumulative plan, forecast, and actual as an S-curve; monthly burn as bars; series order and source line per `csl-brand` Section 6; regime note per `SKILL.md` 3.8.

## 10. What is never typed

Committed totals, invoiced totals, paid totals, current budget, EAC, variance, remaining commitment, and any program total. If a figure cannot be derived, the missing source is named on the Control sheet and the cell shows the derivation gap, not a typed number.

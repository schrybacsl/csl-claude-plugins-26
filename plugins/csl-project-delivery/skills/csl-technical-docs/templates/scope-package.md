# Scope Package (CSL-<PROG>-SCP-<WS> Rev <n>)

Skeleton for a scope package that splits one piece of work across several parties, per `csl-technical-docs` 4.4. Ten numbered sections; bottom line and decision requested first. Example values follow `CSL-W77-SCP-WS04.01 Rev 0` (boiler copper replacement, Boilers 3 and 5, issued 08/14/26) where the record supplies them: basis document the water-treatment vendor's 05/14/26 recommendations letter attached to the tracker row; scope split across the water-treatment vendor (chemistry / OPEX), Vanderweil (engineering), MMI (installation pricing), and the FM contractor (sampling); standing direction that the named valve vendor is not used on this scope; dependency on PMO approval of the PDS. Dates, durations, and window assumptions not in the record are illustrative. Commercial path per `csl-cost-change-control`; number and file name per `csl-document-control`.

---

## Document control

| Field | Value |
|---|---|
| Document No. | CSL-W77-SCP-WS04.01 |
| Revision | 0 |
| Title | Boiler Copper Replacement, Boilers 3 and 5: Scope by Party |
| Author | <name>, CSL Consulting |
| Technical reviewer | CSL MEP (S. Dube / D. O'Brien) or the client engineering lead, as the engagement directs |
| Approver | Client program lead (W77: B. Gannon, ASML) |
| Date issued | 08/14/26 |
| Supersedes | None |
| Distribution | Client program lead; PMO; the four parties in Section 4; CSL PM on site |

## 1. Bottom line and decision requested

> Boilers 3 and 5 need their copper replaced per the water-treatment vendor's 05/14/26 recommendations. This package splits the work across four parties so that engineering, pricing, chemistry, and sampling can proceed in parallel. Decision requested from the client program lead by <MM/DD/YY>: approve the scope split and release Vanderweil to specify; pricing is committed only after PMO approval of the PDS.

## 2. Basis documents

| Ref | Document | Author | Date | Where attached |
|---|---|---|---|---|
| B1 | Recommendations letter, Boilers 3 and 5 | Water-treatment vendor | 05/14/26 | Mitigation sheet row WS-04.01 (Smartsheet 2158727850315652), pulled <MM/DD/YY HH:MM ET> |
| B2 | Project Definition Sheet (PDS) | <author> | <MM/DD/YY> | PMO intake; approval pending |

## 3. Background and condition

One page: the condition, its evidence (B1 findings summarized with the vendor's figures and units), what has already been done, and why the work is split rather than issued to one party.

## 4. Scope by party

| Party | Scope | Deliverable | Exclusions | Pricing basis |
|---|---|---|---|---|
| Water-treatment vendor | Chemistry program for Boilers 3 and 5 through and after the replacement | Chemistry recommendations and monitoring plan | Materials and installation | OPEX, existing service agreement |
| Vanderweil (engineering) | Specify the replacement copper; piping connection details | Specification and connection sketches by drawing number and revision | Installation, chemistry | Engineering proposal against the PDS |
| MMI (installation) | Install per the Vanderweil specification | Installation pricing; schedule with shutdown windows | Design, chemistry, sampling | Lump sum against the specification |
| FM contractor | Sampling before and after | Sample results to the water-treatment vendor and CSL | Design, installation | Existing FM scope |

## 5. Interfaces and sequencing

| Step | From | To | Hand-off | Hold point |
|---|---|---|---|---|
| 1 | Water-treatment vendor | Vanderweil | B1 and current chemistry data | Vanderweil confirms receipt in writing |
| 2 | Vanderweil | MMI | Specification and connection details at issued revision | No pricing on a draft specification |
| 3 | MMI | Client program lead via CSL | Installation price and window plan | Proposal review (proposal-to-PO step 7) |
| 4 | FM contractor | Water-treatment vendor and CSL | Pre-work samples | Results on file before the window is set |

## 6. Constraints

| Constraint | Detail | Owner |
|---|---|---|
| Standing direction | The named valve vendor is not to be used on this scope; Vanderweil specifies | Client program lead (direction on record 08/2026) |
| PDS approval | Pricing is not committed before PMO approval of the PDS | PMO |
| Shutdown windows | One boiler at a time; window per the operations calendar (illustrative sequencing) | Operations with CSL PM on site |
| Permits | SIPP permit per window; hot work if brazing is specified | MMI with the permit coordinator |
| Long-lead | Copper sections per the specification; lead time stated in the MMI proposal | MMI |

## 7. Deliverables and acceptance

| Party | Deliverable | Accepted by | Criteria |
|---|---|---|---|
| Vanderweil | Specification, connection details | Client engineering lead with CSL review | Issued revision; drawing numbers assigned |
| MMI | Installed copper, pressure test record, as-builts | Client system owner on CSL recommendation | Test per specification; as-builts by drawing number |
| Water-treatment vendor | Monitoring plan and post-work chemistry report | Client system owner | Parameters within the vendor's stated ranges |
| FM contractor | Sample results | Water-treatment vendor and CSL | Chain of custody complete |

## 8. Schedule assumptions

| Assumption | Date | What moves it |
|---|---|---|
| PDS approved by PMO | <MM/DD/YY> | PMO calendar |
| Vanderweil specification issued | <MM/DD/YY> | PDS approval; data from the vendor |
| MMI pricing received | <MM/DD/YY> | Specification issue |
| First boiler window | <MM/DD/YY> | PO issue; operations calendar; copper lead time |

## 9. Commercial path

| Item | Value |
|---|---|
| Route | CAAR (design, then execution) and PO per `csl-cost-change-control` 3.4; CAAR, not "CARR" |
| Proposal-to-PO step | Current lifecycle step on the WS-04.01 row at the pull; PO number written back to the row on issue |
| Budget line | Containment Budget Tracker (Rev 4), keyed to WS-04.01 |

## 10. Open items and approvals

| # | Open item | Asked | To whom | Blocks | Status |
|---|---|---|---|---|---|
| 1 | Confirm PMO approval date for the PDS | <MM/DD/YY> | PMO | Pricing commitment | Open |
| 2 | Confirm whether the engineering proposal is inside an existing Vanderweil agreement | <MM/DD/YY> | Client program lead | Vanderweil release | Open |

| Approval | Name | Date |
|---|---|---|
| Recommended by | <name>, CSL Consulting | <MM/DD/YY> |
| Approved by | Client program lead | <MM/DD/YY> |

## Revision history

| Rev | Date | Author | Description of change |
|---|---|---|---|
| 0 | 08/14/26 | <name> | First issue |

---

Pre-issue: decision, decider, and date in Section 1; every basis document dated and attached to the tracker row; every party has scope, deliverable, exclusions, and pricing basis; standing directions recorded in Section 6; commercial route stated with CAAR spelled correctly; open items carry asked dates; control block first and revision history last; file properties set; PDF alongside; brand QA per `csl-brand`; number per `csl-document-control`.

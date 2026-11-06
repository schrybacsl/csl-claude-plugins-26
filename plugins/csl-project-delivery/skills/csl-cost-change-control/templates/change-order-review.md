# Change Order / PCO Review Memo

Skeleton for the owner's-representative review of a proposed change order. Number as `CSL-<PROG>-MEM-<yymmdd>` (`csl-document-control`); one memo per PCO, or one memo per batch when several PCOs share a cause. The recommendation sentence comes first. Contract mechanics per the installed `aia-contracts-capital-projects` skill (Part 3.5 entitlement, pricing, markup; Part 4.1 forms). Example values below are illustrative and are not program records; they show the level of specificity expected.

---

**CSL-W77-MEM-<yymmdd>** | Change Order Review | Rev 0 | Date issued <MM/DD/YY> | Prepared by <operator>, CSL Consulting | Prepared for <owner decision-maker> | Distribution <names> | Time zone ET

## 1. Recommendation (bottom line)

One of two fixed forms:

> CSL is not in a position to recommend approval of PCO-007 as submitted. Four comments follow; resolution of comments 2 and 3 would support approval in the amount of $41,860.00 and 3 calendar days.

> CSL recommends approval of PCO-007 in the amount of $41,860.00 and 3 calendar days. All seven review tests pass; backup is complete.

The owner decides. CSL does not approve.

## 2. Submission summary

| Field | Entry |
|---|---|
| PCO number and title | PCO-007, Added isolation valves and supports at HX-2 tie-in |
| Contractor / vendor | MMI |
| Date received | 09/22/26 |
| Requested amount | $48,915.00 |
| Requested time | 6 calendar days |
| Form | Change order proposal (to become G701 on approval) |
| Contract | Purchase order terms, markup clause 7.2 (10% sub OH&P, 5% GC on sub work, no stacking) |
| Related rows | WS-22.08; IN 12896; CO log entry pending |

## 3. Seven tests

| # | Test | Finding | Effect |
|---|---|---|---|
| 1 | Entitlement | Isolation valves are not shown on the issued piping sketch and are not reasonably inferable from the base scope; notice given 09/15/26 within the contract period | Entitled |
| 2 | Causation | Owner-directed addition on the field walk 09/12/26 (recorded in field report FR-14); not a differing site condition | Owner cause; time entitlement follows the schedule test |
| 3 | Quantum | 64 labor hours claimed against a task the contractor's own daily reports show at 46 hours for comparable tie-ins; material quotes attached for valves, none for supports | 18 hours and the support material are unsupported |
| 4 | Schedule impact | 6 days claimed; the fragnet shows the tie-in on a path with 3 days of float consumed by the added work | 3 days supportable |
| 5 | Markup | 10% sub OH&P applied, then 5% GC markup applied to the marked-up sub total, then 5% again as "coordination" | Second 5% not in contract; stacking removed |
| 6 | Overlap | Two pipe supports are already in base scope line 07 of the SOV | Duplicate; remove |
| 7 | Documentation | Sub quote for valves present; support quote missing; revised SOV lines not provided | Incomplete |

## 4. Numbered comments

1. Quantum (test 3): reduce labor to 46 hours per the contractor's daily reports of 09/16 to 09/19/26, or provide time cards supporting 64. Effect: −$1,980.00.
2. Markup (test 5): remove the 5% "coordination" markup not provided in clause 7.2; apply 5% GC markup to sub cost, not to marked-up sub cost. Effect: −$2,415.00.
3. Overlap (test 6): remove the two supports carried in SOV line 07. Effect: −$1,660.00.
4. Documentation (test 7): provide the support material quote and the revised SOV lines before the G701 is prepared. Effect: none on amount; gates issue.

Arithmetic (re-run in code): $48,915.00 − $1,980.00 − $2,415.00 − $1,660.00 = $42,860.00; less $1,000.00 of unsupported support material pending quote = $41,860.00 supportable at this review.

## 5. Budget and schedule effect if approved as recommended

| Item | Figure | Source |
|---|---|---|
| Amount | $41,860.00 | This review |
| Funding line | WS-22.08 planning budget, Containment Budget Tracker Rev 4 | Tracker |
| Contingency draw | Owner contingency, via Budget Adjustments row BA-<nnn> | Workbook |
| Time | 3 calendar days on the HX-2 tie-in; no critical-path effect | Fragnet dated 09/22/26 |
| Tier | AMBER (A2): 1–30 days on a non-critical row; cost variance inside 10% of the WS row | `csl-schedule-risk/references/tier-rules.md` |

## 6. Record

| Field | Entry |
|---|---|
| CO log row | PCO-007 | received 09/22/26 | requested $48,915.00 / 6 d | tests failed 3, 5, 6, 7 | recommended $41,860.00 / 3 d | decision pending |
| Documents relied on | Contractor proposal 09/22/26; FR-14 (09/12/26); daily reports 09/16–09/19/26; clause 7.2; SOV rev 2; fragnet 09/22/26 |
| Next action | Contractor to respond to comments 1 to 4 by <MM/DD/YY>; owner decision at the following weekly |

## 7. Source note

Documents and pulls listed with dates; tracker revision cited; arithmetic file saved with the memo per `csl-document-control` Section 8.

---

Pre-issue: recommendation sentence in the fixed form; all seven tests shown even when an early one fails; arithmetic re-run; markup clause cited; CO log row drafted; tier with rule; brand QA per `csl-brand`.

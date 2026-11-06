# Oversight Log Schemas

Columns and status vocabularies for the seven logs CSL keeps as owner's representative: submittal, RFI, design review comment, decision, nonconformance (NCR), punch, and commissioning issues. CSL keeps its own copy of each log and reconciles it weekly against the CM's and the CxA's; the CM's log is an input, not the record. Status is always a party plus an action. Aging and days-in-court are computed in code from the date history (`SKILL.md` 3.3), never read from a status column. Tiers per `csl-schedule-risk/references/tier-rules.md`.

Common columns on every log: ID, date opened, opened by (organization and person), project phase or area, tier (rule) when a finding attaches, source document, last updated, and a `history` field holding every hand-off as `MM/DD/YY | from | to | action`.

---

## 1. Submittal log

| # | Column | Rule |
|---|---|---|
| 1 | Submittal number | `<spec section>-<seq>` with revision letter (`23 73 13-02 R1`); the CM's number is kept as an alias, never replaced |
| 2 | Spec section and title | MasterFormat 2018 number and title (`masterformat-2018`) |
| 3 | Description | The item as the spec names it |
| 4 | Type | Product data / Shop drawing / Sample / Certificate / Test report / Closeout / Mock-up |
| 5 | Required by | Schedule activity ID and date the item gates; lead time stated |
| 6 | Date received from CM | |
| 7 | Date to A/E | |
| 8 | Date returned by A/E | |
| 9 | A/E action | Vocabulary below |
| 10 | Date to Owner (when an owner decision is required) | Only for items the owner decides (color, standard, operability); most submittals never touch the owner |
| 11 | Owner decision and date | Recommendation form per `SKILL.md` 3.1; decided by the named owner |
| 12 | Workflow status | Vocabulary below |
| 13 | Ball-in-court | CM / A/E / Owner / Vendor / Closed; never blank on an open item |
| 14 | Days-in-court: CM, A/E, Owner, Vendor | Four columns, computed from history |
| 15 | Days open and aged | Days open; aged = days past the Section 01 33 00 period |
| 16 | Resubmittal count | A third revision is a finding on the item, whichever party caused it |
| 17 | Notes | CSL's review notes; conditions attached to a recommendation |

**A/E action vocabulary (the A/E's words, recorded exactly):** No Exceptions Taken | Make Corrections Noted | Revise and Resubmit | Rejected | Submit Specified Item | For Record Only.

**Workflow status vocabulary:** Not Yet Submitted | With CM (preparing or correcting) | With A/E | Pending Owner Decision | Returned to CM | Closed. "Under Review" is not a status; it is one of the four "With" states plus the days.

Header line for an extract: "Submittals: 212 logged; 38 open; 9 aged; oldest 27 days with A/E; 4 pending owner decision, earliest needed 10/09/26."

---

## 2. RFI log

| # | Column | Rule |
|---|---|---|
| 1 | RFI number | The CM's number; CSL never renumbers |
| 2 | Question | One sentence, in CSL's words, so an executive can read it |
| 3 | Drawing and spec reference | Sheet and revision; spec section |
| 4 | Discipline | Arch / Struct / Mech / Elec / Plumb / FP / Civil / Process / Controls |
| 5 | Cost impact | Yes / No / Possible; Yes opens a PCO number the same day |
| 6 | Schedule impact | Yes / No / Possible; Yes names the activity and the date |
| 7 | Date opened | |
| 8 | Response due | Date opened plus the contract response period (business or calendar days as the contract says) |
| 9 | Ball-in-court | CM / A/E / Owner / Consultant / Closed |
| 10 | Days-in-court: CM, A/E, Owner | Computed from history |
| 11 | Days open; aging band | 0–7 / 8–14 / 15–30 / > 30 calendar days |
| 12 | Response summary | The A/E's answer in one sentence; the full response attached |
| 13 | Date answered | |
| 14 | Status | Vocabulary below |
| 15 | Linked PCO / NCR / decision | Numbers only |
| 16 | CSL note | Owner-requirement, budget, schedule, or operability observation; scope-growth flag |

**Status vocabulary:** Open | Answered, pending CM acknowledgement | Closed | Void | Converted to PCO-<nnn>.

An RFI whose answer adds scope is closed and its scope moves to a PCO; the RFI is never the change vehicle (csl-operating-rules, Section 8).

---

## 3. Design review comment log

| # | Column | Rule |
|---|---|---|
| 1 | Comment ID | `DR-<phase>-<seq>` (`DR-CD50-014`) |
| 2 | Design phase and set | SD / DD / CD 50 / CD 90 / IFC / Bulletin, with the set date |
| 3 | Discipline | As RFI log |
| 4 | Sheet or spec reference | Sheet and detail, or spec section and paragraph |
| 5 | Comment | CSL's comment, one owner question per comment |
| 6 | Category | Owner requirement / Budget / Schedule / Operability and maintainability / Coordination / Code flag to A/E |
| 7 | OPR or standard reference | The section of the OPR, program, RDD, or owner standard the comment rests on |
| 8 | A/E response | The A/E's words and date |
| 9 | CSL disposition | Open / Responded / Accepted / Not accepted, escalated / Withdrawn |
| 10 | Closed by, date, document | Named person; the drawing issue or letter that closed it |
| 11 | Cost or schedule consequence | Where the comment changes either |

A comment closed only by "incorporated in the next set" is reopened at the next set until the sheet shows it. Code flags are closed by the A/E's written response, never by CSL.

---

## 4. Decision log (with the schedule and cost lever)

| # | Column | Rule |
|---|---|---|
| 1 | Decision ID | `D-<seq>` |
| 2 | Decision needed | One sentence framed as a choice |
| 3 | Options | Each with cost and schedule effect |
| 4 | CSL recommendation | One of the options, with the reason in one clause |
| 5 | Decision owner | One named person on the owner side |
| 6 | Due date | Calendar date |
| 7 | Milestone gated | The activity or event the decision holds, with its date |
| 8 | Schedule consequence if late | Days per day late, or the date that moves |
| 9 | Cost consequence if late | Dollars (expediting, remobilization, rework) with the basis |
| 10 | Escalation at +5 business days | The named person who hears it |
| 11 | Status | Needed / Options issued / Decided / Recorded / Overdue (+n business days) |
| 12 | Decision and date | The decision as made |
| 13 | Recorded in | Minutes number and item |

Columns 7 to 10 are the lever and are mandatory (the OSU Medical Center Expansion Wing lesson, `SKILL.md` 3.3). A row missing any of them is reported as "decision item without a lever" in the extract header.

Equipment decision rows add: equipment item ID, responsibility (OFOI / OFCI / CFCI / VFCI), disposition (new / existing / relocate / dispose), room, RDD status, and the vendor quote or move cost the decision turns on.

---

## 5. Nonconformance report (NCR) log

| # | Column | Rule |
|---|---|---|
| 1 | NCR number | `NCR-<seq>` |
| 2 | Date and location | Room, grid, or system; photo numbers |
| 3 | Spec section and requirement | The requirement not met, quoted |
| 4 | Description | What was found, by whom |
| 5 | Root cause (as determined) | Contractor's stated cause recorded as their position; A/E's finding recorded as the A/E's |
| 6 | Disposition | Rework / Repair / Use-as-is (A/E written acceptance on file) / Reject and replace |
| 7 | Disposition by | The A/E, with date and document |
| 8 | Cost and schedule consequence | Who bears it; change number if any |
| 9 | Corrective action and date | |
| 10 | Verification | CSL verified date and initials; retest or reinspection reference |
| 11 | Status | Open / Dispositioned / Corrected / Verified / Closed |
| 12 | Linked Cx issue / punch item | Numbers |

A use-as-is disposition without the A/E's written acceptance is an open NCR. Repeat NCRs on one trade are a contractor-accountability finding (`SKILL.md` 3.15).

---

## 6. Punch list

| # | Column | Rule |
|---|---|---|
| 1 | Item number | `P<phase>-<seq>` |
| 2 | Area / room | As the room schedule names it |
| 3 | Discipline | |
| 4 | Description | What is wrong and what complete looks like |
| 5 | Identified by | CM / A/E / Owner walk (CSL, facilities, end user), with date |
| 6 | Responsible party | Trade or vendor |
| 7 | Life safety or owner-critical | Yes / No; Yes must reach Owner accepted before substantial completion |
| 8 | Value | Dollar value for the retainage arithmetic |
| 9 | State | Open / CM reports complete / CSL verified / Owner accepted |
| 10 | Dates per state | One date column per state |
| 11 | Photo before / after | Photo log numbers |

Counts by state are the weekly metric: "Phase 2 punch: 146 items; 31 open; 52 CM reports complete; 44 CSL verified; 19 owner accepted; 6 life-safety items, 4 at owner accepted." Items the owner walk adds are the owner's list and stay on it.

---

## 7. Commissioning issues log

| # | Column | Rule |
|---|---|---|
| 1 | Issue number | The CxA's number |
| 2 | System and equipment tag | |
| 3 | Found during | PFC / FPT / IST / Seasonal / Warranty |
| 4 | Test script and revision | |
| 5 | Description | Observed versus required, with the OPR or sequence reference |
| 6 | Severity | High (owner-critical function or life safety) / Medium (performance shortfall) / Low (documentation or cosmetic) |
| 7 | Responsible party | CM, trade, vendor, controls, A/E (design), or Owner |
| 8 | Corrective action and date | |
| 9 | Retest date and result | |
| 10 | Status | Open / Corrected, retest scheduled / Retested, passed / Deferred (seasonal), date / Closed |
| 11 | Linked NCR / punch item | Numbers; an issue in this log and not in the others where it belongs is a record discrepancy |

Deferred tests carry a date and the contract lever (retainage or warranty term) that brings the contractor back. The log is reconciled with the punch list and NCR log before any substantial completion recommendation.

---

## 8. Extract header lines (one per log, in this order in the weekly edition)

- Submittals: logged; open; aged; oldest with party; pending owner decision and earliest needed date.
- RFIs: open; aged; by band; with cost or schedule impact; oldest with party.
- Design comments: open by category; code flags awaiting A/E response.
- Decisions: due this week; overdue with days; rows without a lever.
- NCRs: open by disposition state; repeat NCRs by trade.
- Punch: counts by state; life-safety items by state.
- Cx issues: open by severity; deferred with dates; FPTs failed awaiting retest.

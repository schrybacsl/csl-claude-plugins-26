# Engineering / Facilities Notice (FM-<AREA>-<TOPIC>-<mmdd> R<n>)

Skeleton for a client-convention facilities or engineering notice per `csl-technical-docs` 4.7 and `csl-brand` document anatomy Section 3. `mmdd` is the condition date, not the issue date; `R<n>` updates the same notice; a new notice names what it supersedes on its face. Example values follow `FM-W77-UTM-0903 R1` (full UT data set) and `R2` (communication timeline and Q&A added), which superseded `FM-W77-UTM-0819`, authored by the CSL PM on site (D. Wolf); owners and dates in the actions table are illustrative where the record does not supply them. A wall-loss reading below manufacturer lower tolerance, a zero-flow reading, or reservoir runway under 90 days is RED (R9) and the notice issues the same day (`csl-schedule-risk/references/tier-rules.md`). Memo header per `csl-executive-memo`.

---

**FM-W77-UTM-0903 R2** | Issued <MM/DD/YY> | Prepared by D. Wolf, CSL Consulting | Supersedes FM-W77-UTM-0819 and updates R1

| Line | Value |
|---|---|
| Status | Action Required |
| Affected systems | Chilled-water carbon-steel distribution piping, W77, including the 18-inch mains |
| Condition date | 09/03/26 |
| Next review date | <MM/DD/YY> |

## Condition

> Ultrasonic thickness testing of the carbon-steel chilled-water piping (MTI report S-1000, 07/17/26) shows wall loss below the lower manufacturing tolerance at 11 of 15 carbon-steel locations. The 18-inch mains read 36 to 37% below nominal if schedule 40 is confirmed; the original schedule is an open data gap.

## Evidence

| Parameter | Value | Source |
|---|---|---|
| Method | Ultrasonic thickness, ASTM E797 | MTI report S-1000 |
| Points | 16 | MTI report S-1000 |
| Baseline period | 297 days | MTI report S-1000 |
| Carbon-steel locations below lower manufacturing tolerance | 11 of 15 | MTI report S-1000 |
| Worst location loss rate | 0.38 mm/yr | MTI report S-1000 |
| 18-inch mains versus nominal | 36 to 37% below, if schedule 40 is confirmed | MTI report S-1000; schedule confirmation open |

Measurement tables carry instrument, standard, point count, baseline period, and units; readings by location are in the attachment at the revision cited.

## Risk statement

> No failure date is assignable from the data. A credible short-term leakage risk exists at the locations below tolerance. The statement is limited to what the readings support; it does not infer a remaining life.

Tier: RED (R9), wall loss below manufacturer lower tolerance. Client direction to de-escalate to working level (recorded <MM/DD/YY>) holds the item at AMBER with the R9 rule still cited and the review date above; the direction is recorded, the rule does not change (`tier-rules.md` 2.5).

## Codes and standards

| Standard | Use |
|---|---|
| ASME B31.9 | Building services piping: minimum wall evaluation |
| API 579-1 / ASME FFS-1 | Fitness-for-service assessment method |

## Recommended actions

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Confirm the original pipe schedule for the 18-inch mains from drawings or a direct measurement at a cut-out | Client engineering lead | <MM/DD/YY> |
| 2 | Fitness-for-service evaluation of the 11 locations per API 579-1 | Engineer of record | <MM/DD/YY> |
| 3 | Re-test interval and points for the next UT campaign | Client engineering lead with the UT vendor | <MM/DD/YY> |
| 4 | PDS for piping remediation to ride the IRO strategy to REDM 10/01/26 | CSL PM on site | Before 10/01/26 |

## Communication timeline (R2 addition)

| Date | Communication | From | To | Document |
|---|---|---|---|---|
| 08/19/26 | First notice | D. Wolf | Client engineering lead; client program lead | FM-W77-UTM-0819 |
| 09/03/26 | Full UT data set | D. Wolf | Same | FM-W77-UTM-0903 R1 |

## Questions and answers (R2 addition)

| Question raised | By (role) | Answer on record | Date |
|---|---|---|---|
| Is a failure date assignable? | Client program lead | No; the data supports a leakage risk statement only | <MM/DD/YY> |

## Supersedes

FM-W77-UTM-0819. R2 updates R1 by adding the communication timeline and Q&A; the evidence table is unchanged from R1.

---

Pre-issue: status line one of Information / Action Required / Escalation; condition date in the number, issue date in the body; evidence table with method, points, baseline, units, source; risk statement limited to the data; codes by number; every action with owner and date; next review date on the face; supersedes line present; tier with rule and any de-escalation direction recorded; no CSL Red fills; logged for the docket; number per `csl-document-control` 1.2.

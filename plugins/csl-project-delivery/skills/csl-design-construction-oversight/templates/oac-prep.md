# OAC Prep (one page)

Skeleton for the owner's brief prepared the day before every Owner-Architect-Contractor meeting. It stays on the owner side; the minutes that follow are the record (`csl-meeting-records`). Seven blocks in the order of `csl-design-construction-oversight` 3.2, then the docket and the source note. One populated example row per table; example content is illustrative for a phased healthcare renovation and is not a client record. Variables in `<angle brackets>` change every issue. Carries the OAC meeting number (`OAC #<nnn> Prep`); file `CSL-<PROG>-OAC-<nnn>_prep_<yyyy-mm-dd>.pdf`.

---

**OAC #<nnn> Prep** | <Project name and phase> | OAC <Day MM/DD/YY, time> ET | Prepared by <name>, CSL Consulting, for <Owner PM> | Time zone ET

## Bottom line

Two sentences: what holds the next milestone and what the owner must decide or accept this week.

> Phase 2 substantial completion holds at 12/04/26 only if the A/E answers RFI-087 by 10/12/26 and the Owner decides D-031 by 10/09/26. Two PCOs totaling $20,570 are pending with CSL positions below.

## 1. Look-ahead (next two weeks)

| Activity (schedule ID) | Area | CM date | CSL check | Constraint |
|---|---|---|---|---|
| A2150 Medical gas rough-in and AHJ rough inspection | Procedure rooms 2 and 3 | 10/13 to 10/14 | Inspection booked 10/14; RFI-087 open | Zone valve box location |

## 2. Open RFIs at or past the response period

Response period per the executed contract: <n business days>. Aging computed from the date history (`references/log-schemas.md`).

| RFI | Question | Days open (opened; due) | Ball in court (days-in-court) | Cost / schedule impact | Action, date |
|---|---|---|---|---|---|
| RFI-087 | Zone valve box on M-401 conflicts with casework elevation A-501, procedure room 3 | 12 business days (09/22/26; due 10/06) | A/E (12 of 15 calendar days) | Possible / Yes, gates 10/14 inspection | A/E response by 10/12; CSL notice at 15 business days |

## 3. Submittals pending owner decision

| Submittal | Spec section | Question for the owner | Gates | Decision needed by |
|---|---|---|---|---|
| 26 51 13-04 procedure-room luminaires | 26 51 13 Interior Lighting | 3500 K or 4000 K per the facility lighting standard | Fixture release 10/12 (4-week lead) | 10/09 (D-031) |

## 4. Change orders and PCOs pending

| Number | Description | Amount | CSL position (one of the four forms) | Owner action |
|---|---|---|---|---|
| PCO-014 | Abatement of floor mastic found 09/29/26, Phase 2 area | $18,420 | Recommend the Owner not accept as submitted; quantity exceeds the abatement survey by 340 SF | Revised backup from CM by 10/09 |

Review method and contingency arithmetic per `csl-cost-change-control`.

## 5. Safety, ICRA / ILSM, permits

| Item | Status | Finding (tier, rule) if any |
|---|---|---|
| ICRA Class IV barrier, anteroom with HEPA negative air | Daily checklist 5 of 5; one deficiency 10/05/26, corrected within 10 minutes, photo P2-118 | None; recorded |

In manufacturing facilities this block is the permit board summary: permits starting this week and their gate progress, permits closed, work done with no record (RED (R6)) per `csl-permits-shutdowns`.

## 6. Decision log items due

| ID | Decision | Owner | Needed by | Milestone gated | Lever if late (days / dollars) | Escalation at +5 business days |
|---|---|---|---|---|---|---|
| D-031 | Luminaire color temperature | Owner Facilities | 10/09 | Fixture release 10/12 | 1 day per day after 10/12; $1,800 expediting after 10/16 | Owner Facilities Director |

Every row carries the lever; a row without one is listed under "decision items without a lever" and fixed before the meeting.

## 7. Docket

| Who | What | By |
|---|---|---|
| A/E | RFI-087 and RFI-091 responses | 10/12/26 |

## Source note

> CM RFI and submittal logs exported <MM/DD/YY HH:MM ET>; CSL logs reconciled <date> (<n> count differences, listed); ICRA log through <date>; schedule data date <date>; decision log as of <date>.

---

Pre-issue: bottom line names the milestone and the decisions that hold it; every open item shows a party and days; every decision row has its lever; every CSL position uses one of the four review forms; no personal or health information; brand QA per `csl-brand`; number and file name per `csl-document-control`.

# Tier Rules (stand-alone reference)

Load this file when any deliverable needs to show a RED / AMBER / GREEN tier and the full `csl-schedule-risk` skill is not already loaded. It is the same table as `SKILL.md` Section 3.1; `SKILL.md` is the authority if the two ever differ. Summary copies live in `csl-operating-rules` Section 6 and `references/escalation-matrix.md` Section 1.

## 1. Decision table

Assign the tier by the first rule that fires, top to bottom. Print the rule ID beside the tier every time the tier is shown: `RED (R1)`, `AMBER (A3)`, `GREEN (G)`.

| Tier | Rule | Condition | Response window | First form |
|---|---|---|---|---|
| RED | R1 | Risk at or above the program critical RPN threshold (W77: RPN C >= 700) with no active mitigation: no named owner, or no dated action, or action date passed with no status change | Same day | Flag in the current reply; executive memo; report headline |
| RED | R2 | Forecast versus budget variance > 10% on any cost line, E-GRP, or workstream | Same day | Memo with exposure table |
| RED | R3 | Critical-path slip > 30 days against baseline | Same day | Schedule variance memo |
| RED | R4 | Silent milestone lapse: a dated milestone passed with no status change and no constraint or comment recorded | Same day | Headline; row and date named |
| RED | R5 | Tracker byte-identical across two or more consecutive weekly pulls while its milestones move in the field | Same day | Headline; attributed to the tracker; change list |
| RED | R6 | Work done with no record: field activity with no permit or tracker row | Same day | Notice; RED until backfilled |
| RED | R7 | Minuted decision reversed without a written change decision | Same day | Record-correction reply; ratify-or-correct request |
| RED | R8 | Irreversible step (print, tag, cut, order) about to proceed on an unconfirmed record | Same day | Hold request; gate statement in report and memo |
| RED | R9 | Telemetry showing a tool-down or leakage-risk signature: zero-flow reading, wall loss below manufacturer lower tolerance, reservoir runway under 90 days | Same day | Facilities notice (FM- format) |
| AMBER | A1 | RPN C 400–699; or, where no RPN is scored, a degrading trend still inside tolerance (reservoir runway above 90 days but falling); or an RPN C increase on a row already >= 700 that still has an active mitigation | Within the week | Watchlist row in the weekly report |
| AMBER | A2 | Minor variance: cost variance 5–10% of the line; schedule slip 1–30 days on the critical path; float consumption > 50% on any row | Within the week | Weekly report finding |
| AMBER | A3 | Constraint recorded and unresolved > 2 weeks | Within the week | Docket item with the owner of the enabling action |
| AMBER | A4 | Tracker frozen one pull (byte-identical to the previous pull) | Within the week | Rows expected to move, named |
| AMBER | A5 | Open confirm unanswered > 5 business days | Within the week | Follow-up email; confirm register |
| AMBER | A6 | Record discrepancy unresolved: counterpart minutes or recap conflicting with the transcript or CSL's record; a tracker entry conflicting with itself (inverted dates, RPN not equal to its factors) or with another live source | Within the week | Correction requested; discrepancy logged |
| GREEN | G | On plan: dates inside baseline, no rule above fires, mitigation current | Routine | Reported by exception only |

Thresholds marked as package convention in `SKILL.md` (the 5% lower bound of A2, the 50% float consumption, the 14-day register review) come from CSL practice on W77 and may be tuned per engagement in the engagement context file (`csl-operating-rules` Section 5); the RED rules track csl-operating-rules Section 6 and are not tuned.

## 2. Rules of use

1. Never show a tier without its rule.
2. When more than one rule fires, cite the highest-tier rule and list the others in the finding body.
3. Tier the population, not every row, for portfolio classes; the worst row sets the tier and the top rows by RPN and budget are listed. Individual RED findings are reserved for anchor rows, critical-path rows, RPN >= 700 rows, permits and gates, and minuted commitment dates.
4. A tier changes only on evidence from this session's pull or a dated document.
5. Client-directed de-escalation does not change the rule; the item is held at AMBER with a review date and the direction is recorded.
6. Status colors for tiers are the package status colors in `csl-brand` Section 1.4 (RED `#C62828`, AMBER `#E09B1A`, GREEN `#2E7D32`), never CSL Red, and the tier word always accompanies the color.

## 3. Situation map

| Situation seen in the pull | Rule |
|---|---|
| Roadmap row at RPN C 810 with owner and a dated action still in the future | AMBER (A1) |
| Same row, action date passed, no status change | RED (R1) |
| Roadmap row at RPN C 1,000 with no owner on the row | RED (R1) |
| Mitigation row target date passed 9 days ago, owner named, no update | AMBER (A2); R4 if it is an anchor or minuted date |
| Mitigation row past target 3 weeks with `Dependency Enabler Pending` recorded | AMBER (A3) |
| Client counterpart states a new delivery date on a call; tracker still shows the old END | Report both; AMBER (A5) once the written confirmation request is 5 business days old; RED (R7) if the spoken date reverses a minuted one |
| Sheet hash unchanged one week | AMBER (A4) |
| Sheet hash unchanged two weeks while a permit on one of its rows started | RED (R5) |
| Sheet hash unchanged two weeks, no field witness of movement | AMBER (A4), held open, witnesses sought |
| Contractor reports work performed Saturday; no SIPP permit row | RED (R6) |
| QR label print scheduled while functional-code depth is ruled verbally | RED (R8) |
| Forecast on an E-GRP 7% over budget | AMBER (A2) |
| Forecast on an E-GRP 10.01% over budget | RED (R2) |
| LCWC "Bottom" reading on a DUV cooling circuit | RED (R9) |
| Counterpart minutes mark an absent attendee present | AMBER (A6); correction request same day |
| New permit row with END before START | AMBER (A6); correction request; gate count still reported |
| 2026 rows at 0% past Q1 with no constraint, 31 rows | One population finding; tier set by the worst row (R4 if any is anchor, critical path, or >= 700; otherwise AMBER (A2)) |

## 4. Sentence forms

- Finding: "Electrical Distribution MV & LV, RPN C 1,000, RED (R1): no dated mitigation on the row at the 09/18/26 pull; exposure per FMEA edition on file; owner requested from B. Gannon in writing 09/18/26; response by 09/22/26."
- Population: "<n> of <N> rows dated 2026 remain at 0% past Q1 with no constraint recorded, AMBER (A2); the three highest by RPN are listed below; none is on the critical path."
- Frozen tracker: "Roadmap Master unchanged for six consecutive pulls through 09/18/26, RED (R5); milestones lapsed inside the window: <rows>; field movement in the same window: permits 53782 (started 09/16) and 51718 (closed 09/18)."
- De-escalated item: "Held at AMBER (A3) per client direction of <date> to resolve at working level; review date <date>."

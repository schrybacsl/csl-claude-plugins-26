---
name: csl-schedule-risk
description: >
  Schedule and risk discipline, and the authority for the RED / AMBER / GREEN tier rules (R1 to R9,
  A1 to A6) every csl-* skill cites. Use it whenever someone asks "what slipped", "what moved", "is
  this on track", "look-ahead", "bow wave", "re-baseline", "float", "critical path", "risk
  register", "RPN", "FMEA", "constraint", or "why is this row still at 0%"; whenever a schedule,
  tracker, or mitigation sheet is reviewed against baseline; whenever a milestone lapsed silently;
  whenever a risk needs a severity x occurrence x detection score; and whenever any finding needs a
  tier before issue.
---

# CSL Schedule and Risk

Schedule review and risk rating exist so the owner learns, every week and in one page, what moved against the baseline, what did not move and should have, what the exposure is in dollars, days, and records, and who closes it by when. This skill defines the tier rules for the whole package, the FMEA / RPN method used on ASML W77, the look-ahead framing method, re-baseline discipline, frozen-tracker and silent-lapse detection, mitigation-workstream lifecycle KPIs, the risk register, and the schedule health metrics. Its outputs feed the WKR series (`csl-weekly-reporting`), stand-alone memos (`csl-executive-memo`), and KPI views (`csl-dashboard-kpi`).

---

## 1. Bottom line / when this runs

Run this skill on every Sunday pull before the Monday Look-Ahead, on every Friday pull before the End-of-Week report, and on demand whenever a date, a tier, or a risk score is about to appear in a deliverable. The three products are:

| Product | Cadence | Feeds |
|---|---|---|
| "What moved this week" table with tiers and causes | Sunday and Friday pulls | WKR-nnA framing, WKR-nnC headline and roadmap section |
| Risk register review (RPN watchlist, mitigation status, tier changes) | Weekly, Friday | WKR-nnC risk section; executive memo when a RED stands alone |
| Schedule health metrics and mitigation lifecycle KPIs | Weekly, Friday; monthly roll-up | WKR-nnC; `csl-dashboard-kpi` command views |

A finding without a tier and the rule that produced it is not finished (csl-operating-rules, Section 2). A tier without a rule is a color, not a finding.

---

## 2. Inputs and pulls

Pull every sheet the review depends on in this session and record the timestamp; carry nothing forward. QA rules (byte-identity hash, stale-row detection, the date-filter workaround) are in `csl-data-pipeline`; the sheet IDs are in the W77 engagement context file (`engagement-context-W77.md` in the W77 Claude Project).

| Source (W77) | What this skill reads | QA before use |
|---|---|---|
| W77 Roadmap Master 2025–2032 (1059284113641348) | Parent rows only: START, END, Baseline Start/Finish, Variance2, %, Constraints, Health, SEV / Occ / Det / RPN C, RPN-B, Budget, Forecast, YR., E-GRP, Predecessors | Hash against last pull; filter parents locally (child rows are phases and double-count) |
| Roadmap weekly pull (1390098374414212) | WKR roadmap section rows | Same hash test; compare row count to last edition |
| ST CHW/PCW System Mitigation Plan (2158727850315652) | WS rows: lifecycle step, target date, owner, status, baseline status, E-Group | Flag mixed ID formats and blank baseline statuses before computing anything |
| CSL Tasks (7673437876080516) | Anchor rows, Reds, closures | Byte-identity test (the board was identical 08/28/26 to 09/04/26) |
| SIPP Permits (289677048237956) | Permit start dates and gate counts as field-movement evidence | Inverted-dates flag (`csl-permits-shutdowns`) |
| Equipment Summary RPN (7673299942199172) and BR+A FMEA | Baseline scores and failure-mode text | Note the FMEA edition date on every RPN citation |
| P6 export or schedule narrative (J. Yazici, CSL scheduler) | Critical path, total float, predecessor logic | Data date on the export; never an undated schedule |
| Minutes and agendas (`csl-meeting-records`) | Minuted dates, verbal rulings, re-baseline decisions | Verbal versus written status of every date |

Record for each pull: sheet name, ID, timestamp (ET), row count, hash, and whether the hash matched the previous pull. When two sources give different dates for the same milestone (tracker END versus minuted target), report both; never average and never pick silently.

Pull sequence, in this order so each step has what it needs:

1. Roadmap Master, then the weekly roadmap pull; hash both; diff rows against the previous snapshot saved with the last edition.
2. Mitigation sheet; count open, past-target, closures, owner concentration; list ID-format and blank-baseline defects.
3. CSL Tasks and SIPP Permits; these are the field-movement witnesses for the frozen-tracker test.
4. Minutes, agendas, and notices issued since the last pull; extract every date, ruling, and re-baseline with its verbal or written status.
5. Schedule file (P6 export) only when a critical-path or float question is live; record its data date.

---

## 3. Method

### 3.1 Tier rules (canonical for the package)

Assign the tier by the first rule that fires, top to bottom, and print the rule ID beside the tier every time it is shown (`RED (R1)`, `AMBER (A4)`). The stand-alone copy of this table for other skills to load is `references/tier-rules.md`.

| Tier | Rule | Condition | Response |
|---|---|---|---|
| RED | R1 | Risk at or above the program critical RPN threshold (W77: RPN C >= 700) with no active mitigation (definition in 3.2) | Same day: flag in reply, memo, report headline |
| RED | R2 | Forecast versus budget variance > 10% on any cost line, E-GRP, or workstream | Same day; memo with exposure table (`csl-cost-change-control`) |
| RED | R3 | Critical-path slip > 30 days against baseline | Same day; schedule variance memo with J. Yazici |
| RED | R4 | Silent milestone lapse: a dated milestone passed with no status change and no constraint or comment recorded | Same day; name the row and the date it passed |
| RED | R5 | Tracker byte-identical across >= 2 consecutive weekly pulls while its milestones move in the field | Same day; headline; attribute to the tracker |
| RED | R6 | Work done with no record (field activity with no permit or tracker row) | Same day; RED until backfilled (`csl-permits-shutdowns`) |
| RED | R7 | Minuted decision reversed without a written change decision | Same day; record-correction reply (`csl-client-comms`) |
| RED | R8 | Irreversible step (print, tag, cut, order) about to proceed on an unconfirmed record | Same day; hold request; gate statement |
| RED | R9 | Telemetry showing a tool-down or leakage-risk signature (zero flow, wall loss below lower tolerance, reservoir runway < 90 days) | Same day; facilities notice (FM- format) |
| AMBER | A1 | RPN C 400–699 (or, where no RPN is scored, a degrading trend still inside tolerance, such as a reservoir runway above 90 days but falling); or any RPN C increase on a row already >= 700 that still has an active mitigation | Within the week; watchlist row |
| AMBER | A2 | Minor variance: cost variance 5–10% of the line, or schedule slip 1–30 days on the critical path, or float consumption > 50% on any row (thresholds are package convention) | Within the week; report finding |
| AMBER | A3 | Constraint recorded and unresolved > 2 weeks | Within the week; docket item with owner |
| AMBER | A4 | Tracker frozen one pull (byte-identical to the previous pull) | Within the week; name the rows expected to move |
| AMBER | A5 | Open confirm unanswered > 5 business days | Within the week; follow-up email |
| AMBER | A6 | Record discrepancy unresolved: counterpart minutes or recap conflicting with the transcript or CSL's record; a tracker entry conflicting with itself (inverted dates, RPN not equal to its factors) or with another live source | Within the week; correction requested, logged |
| GREEN | G | On plan: dates inside baseline, no rule above fires, mitigation current | Report by exception only |

Rules of use, because the tier is the part of a report executives read first:

1. Never show a tier without its rule. `RED` alone is rejected at pre-issue.
2. When more than one rule fires, cite the highest-tier rule and list the others in the finding body.
3. Tier the population, not every row, for portfolio classes (for example, 2026 rows at 0% past Q1 with no constraint): one finding, tiered by the worst row in the class, with the top rows by RPN and budget listed. Individual RED findings are reserved for anchor rows, critical-path rows, RPN >= 700 rows, permits and gates, and minuted commitment dates.
4. A tier changes only on evidence from this session's pull or a dated document. Last week's tier is a comparison point, not a default.
5. Client-directed de-escalation ("solve at working level") does not change the rule; record the direction, hold the item at AMBER with a review date, and report it without adjectives (`references/escalation-matrix.md`, Section 3).

How common situations map to rules, so the same condition gets the same tier every week:

| Situation seen in the pull | Rule |
|---|---|
| Roadmap row at RPN C 810 with owner and a dated action that is still in the future | AMBER (A1); it stays off RED only while the date holds |
| Same row, action date passed, no status change | RED (R1) |
| Mitigation row target date passed 9 days ago, owner named, no update | AMBER (A2); becomes R4 if it is an anchor or minuted date |
| Client counterpart states a new delivery date on a call; tracker still shows the old END | Report both; AMBER (A5) once the written confirmation request is 5 business days old; RED (R7) if the spoken date reverses a minuted one |
| Sheet hash unchanged one week | AMBER (A4) |
| Sheet hash unchanged two weeks while a permit on one of its rows started | RED (R5) |
| QR label print scheduled while functional-code depth is still ruled verbally | RED (R8) |
| Forecast on an E-GRP 7% over budget | AMBER (A2); RED (R2) at 10.01% |

### 3.2 FMEA / RPN method

Score every risk row as Severity x Occurrence x Detection, each 1–10, product 1–1,000. W77 carries two scores per row: the baseline `RPN-B` (BR+A FMEA edition on file) and the current `RPN C` (SEV, Occ, Det columns). Scale anchors (package convention; where the BR+A FMEA edition defines its own anchors, the FMEA governs):

| Score | Severity (effect if the failure occurs) | Occurrence (likelihood in the planning horizon) | Detection (chance the failure is caught before effect) |
|---|---|---|---|
| 1–2 | Cosmetic; no production or safety effect | Remote; no history on this asset class | Certain; continuous monitoring with alarm |
| 3–4 | Local nuisance; maintenance work order | Occasional; isolated history | Likely; routine PM or BMS trend would show it |
| 5–6 | Area or system degradation; workaround exists | Moderate; recurring history on site | Possible; found on inspection cadence only |
| 7–8 | Production interruption, tool-down risk, or code violation | Frequent; failing trend documented | Unlikely; no instrument, walk-down only |
| 9–10 | Life safety, environmental release, or site-wide outage | Near certain; failure in progress or imminent | Undetectable before effect |

Work the method in this order:

1. Read RPN-B and RPN C from the sheet; never recompute RPN-B, and recompute RPN C only to check the sheet's arithmetic (a product that does not equal SEV x Occ x Det is a data defect, reported under A6).
2. When RPN C differs from last pull, record which factor moved and why, citing the document or observation that justified it. An unexplained score change is an A6 finding until explained.
3. Sort the watchlist by RPN C descending; ties by Budget descending. The top of the W77 list at the March 2026 baseline was Electrical Distribution MV & LV at 1,000, followed by Roof Zone 02, Mechanical Piping Project D, and Roof Zones 01/04/10 at 810, and PCW Isolating PPCW 17 Loops at 800 (`asml-pm-agent`, Part 4.4). Confirm against the live pull before citing any of them.
4. Test every row >= 700 for active mitigation. **No active mitigation** means any one of: no named owner; no dated action; or the action date has passed without a status change. Any of the three makes the row RED (R1).
5. Record the mitigation in the risk register (3.8) with owner, action, date, and the source document. The register is what turns a score into something the owner can act on.

### 3.3 Constraints

The W77 roadmap Constraints column is a picklist. Use these values exactly, because filters and roll-ups break on variants:

`Seasonal Weather Dependent` | `Access Limitations/Share Corridor` | `CapEx/Funding Gate` | `Long Lead Time` | `Operations Blackout` | `Outage Scheduling Utility Tie-in` | `Safety EH&S Limitation` | `Permit Regulatory` | `Dependency Enabler Pending`

Use constraints to explain, not excuse, a row at 0% past its start quarter. A 2026 row at 0% after 03/31/26 with a constraint recorded is a dated AMBER (A3) item once the constraint has stood more than two weeks, with the owner of the enabling action named (a `CapEx/Funding Gate` row names the CAAR owner; a `Dependency Enabler Pending` row names the enabler and its own date). The same row with no constraint recorded is a start-milestone silent lapse (R4 for anchor, critical-path, or >= 700 rows; otherwise it joins the population finding in 3.9). When a row's comment names a reason that is not in the picklist, report the comment and recommend the nearest picklist value; do not edit the client's sheet.

### 3.4 Look-ahead framing

Frame the commitment week from the Sunday pull, before anyone has moved anything on Monday. Steps:

1. Pull Sunday; hash the sheets; note what changed since Friday's pull (usually nothing, which is itself a data point).
2. Identify the anchor rows: the tracker rows whose closure the week is built around. A row qualifies when its END falls in the week, when a minuted commitment lands in the week, or when another party's start depends on it. Name each by row and END date. The week of 08/24/26 was built around the upload-sheet row with END 08/28/26; the week of 08/31/26 was bookkeeping around flipping those anchor rows after the 08/26/26 delivery.
3. Separate the tracker END from any outer frame a stakeholder named verbally. The W77 case: the upload-sheet row carried END 08/28/26 on CSL Tasks, while T. Dube's 08/05/26 verbal direction set a mid-September (~09/15/26) outer frame for the full-building upload. State both, in that order, with their provenance: "Tracker END 08/28/26 (CSL Tasks row); outer frame ~09/15/26 (stated on the call by T. Dube 08/05/26; carried in Agenda #016 item 016-003 as 'mid-September 2026 full-upload target')."
4. Carry the commitment week's docket: what closes this week, who owns it, the evidence of closure (transmittal number, minutes item), and what starts toward the outer frame.
5. Report any compressed date accepted verbally by a client counterpart in five parts, every time: original baseline; new date; delta in days; resourcing implication; acceptance attributed by name and date. As written in WKR-33A and carried until the #019 re-baseline:

> Original baseline: Planon uploads and asset tagging closing end of Q4 2026 (12/31/26). New date: full-building upload sheet by ~09/15/26. Delta: 107 days of compression on 41 days' notice. Resourcing implication: the mechanical, gases and plumbing, and taxonomy 13-down sequences compress into six weeks, and every functional-code structure change re-opens delivered rows. Acceptance: direction issued by T. Dube (ASML) on 08/05/26, verbal; written confirmation requested; not a CSL baseline change until minuted.

The look-ahead's job is to make Monday's reader see the tracker date, the spoken date, and the gap between them without having to ask. The framing block for the week of 09/28/26 (WKR-40A), built from the recurring calendar in the W77 engagement context file (`engagement-context-W77.md` in the W77 Claude Project), shows the shape:

| Anchor | Date | Source of the date | What closes it |
|---|---|---|---|
| Planon weekly (next in series after #021) | Tue 09/29/26, 3 PM ET | Standing series | Ratify-or-correct on the #020 structure ruling; spec status |
| Q3 roadmap close | Wed 09/30/26 | Roadmap calendar | Q3 forecast columns frozen; variance table for WKR-40C |
| REDM: IRO strategy and CHW piping | Thu 10/01/26 | Client review cadence | Decision recorded; PDS-first direction confirmed or changed in writing |
| Outer frame: Loops + AHS hierarchy | Fri 10/30/26 | Minutes #021 item 021-004 (written, all parties) | 42 days from the 09/18 pull; staged weekly in the docket |

### 3.5 Re-baseline discipline

A baseline changes only by a written, minuted re-baseline that states the delta. Until then the original baseline stands in CSL documents and the new date is reported as "requested" or "stated on the call by <name>, <date>". Record every re-baseline in this form:

| Field | W77 entry (Planon full-building upload) |
|---|---|
| Baseline being replaced | ~09/15/26 outer frame (verbal, T. Dube, 08/05/26; Agenda #016 item 016-003) |
| Re-baselined at | Planon weekly meeting #019, 09/15/26, minuted |
| Cause | Functional-code structure change after delivery of the mechanical upload (08/26/26) |
| Delta | Approximately 1,480 records requiring recode before any relabel; new dates per #019 minutes |
| Conditions | Versioned functional-code spec to be issued; delta review in writing before relabel |
| Owner of the new dates | T. Dube (spec); S. Schryba (recode and reissue) |

Anything less than that (a recap, a chat message, a tracker edit with no minute) is not a re-baseline and is reported as R7 if it reverses a minuted date. When a counterpart's minutes record a re-baseline that the transcript does not support, audit per `csl-meeting-records` and correct at the source the same day.

### 3.6 Frozen tracker and silent lapse detection

A live tracker that does not change while the field does is a data-governance finding, and it is reported as one. Detection:

1. Hash every pull (`csl-data-pipeline` scripts: sheet hash and row-level diff). Byte-identical to the previous pull = AMBER (A4). Byte-identical across two or more consecutive weekly pulls while field milestones move = RED (R5).
2. Establish field movement from witnesses outside the frozen sheet: SIPP permits started or closed, deliveries received, shutdowns executed, minuted actions closed, transmittals issued. A frozen sheet with no witnesses of movement is A4 held open, not R5.
3. Name the rows that should have moved: rows whose START or END fell inside the frozen window, rows whose permits started or closed, rows with minuted actions due in the window.
4. Attribute the frozen state to the tracker, not to the field. Write "the roadmap has not changed in six pulls" and "Roof Zone 10 should have moved," never "no work occurred."
5. Report it in the headline, with the count of consecutive frozen pulls and the count of lapsed milestones. The W77 roadmap was frozen six consecutive weeks through the 09/18/26 pull, with the RPN 1,000 Electrical Distribution item reported nine weeks running and milestones lapsing silently inside the window; WKR-38C carried it as the lead roadmap finding.
6. Escalate per `references/escalation-matrix.md` (operator, then tracker owner, then client program lead). Propose the tracker edits as a change list; never write to the client's sheet.

When R5 fires, the headline sentence follows one pattern so editions compare cleanly: "<Sheet> unchanged for <n> consecutive pulls through <date>; <k> milestones lapsed inside the window (<row>, <row>); field movement in the same window: <witness>, <witness>." The change list that accompanies it has one line per row: row name, field to update, value evidenced, evidence document.

### 3.7 Mitigation-workstream lifecycle tracking

The ST CHW/PCW mitigation sheet runs each workstream row through a 10-step lifecycle; step 9 is pricing and step 10 is execution (PO issued and written back to the row). Read the step labels from the sheet header at pull time; the sheet header governs. The package reads the lifecycle as follows for reporting, and reports position as steps complete of 10 so a reader sees progress without decoding labels:

| Step | Stage as reported | Evidence the step is complete |
|---|---|---|
| 1 | Issue logged | Row with WS ID, system, owner |
| 2 | Scope and done-definition | Scope text and done-definition on the row |
| 3 | Engineering basis | Assessment or concept issued (WS-02.02 assessment Rev 0, 08/06/26, is the model) |
| 4 | Solution selected | Option minuted |
| 5 | Intake and governance route | PDS / URS submitted; IN assigned for CAPEX, or OPEX route confirmed |
| 6 | Vendor request issued | RFQ date and vendors named |
| 7 | Proposal received and reviewed | Proposal date; CSL review comments |
| 8 | Funding approved | CAAR (design, execution) or OPEX approval on record |
| 9 | Pricing | Final price agreed; requisition raised |
| 10 | Execution | PO issued; PO number in the "In Place" column; work proceeds |

The cost side of the same lifecycle (proposal-to-PO pipeline, committed versus planning budget, blocked POs) is in `csl-cost-change-control`. Weekly KPIs, computed from the pull and compared to the previous edition:

| KPI | Definition | Recent W77 readings (cite the edition; re-pull before reuse) |
|---|---|---|
| Open rows | Rows not closed or cancelled | 20 open at the 09/18/26 pull (WKR-38C) |
| Past-target | Open rows whose target date has passed | 20 (08/21) → 35 (08/28) → 54 (09/04) → 15 (09/11) → 17 (09/18) |
| Closures this week | Rows moved to closed since the previous pull | 0, 0, 0 for three weeks, then a 43-closure sweep the week of 09/07/26, then 0 |
| Concentration | Open rows on a single owner | 10 of 20 open rows on the client program lead at 09/18/26 (9 of 20 the week before) |
| Steps complete of 10 | Per row and block median | WS-22 block: eight BGP projects on identical lifecycles |
| Data defects | Rows that cannot roll up | Two ID formats in use (`WS-22-01.01` versus `WS209`); child rows missing E-Group and baseline status |

Treat mixed ID formats and blank baseline statuses as data defects that block roll-ups: report the count, exclude the affected rows from the KPI with a footnote, and put the fix on the docket with the sheet owner. A past-target count that falls because rows were closed in bulk is reported with the closure count beside it, so a 54 → 15 move is read as a sweep, not as progress on 39 separate actions. Concentration above half the open rows on one person is reported as a throughput risk on the sheet, with the rows listed, not as a comment on the person.

### 3.8 Risk register and weekly review

Keep one register per program in the schema in `references/risk-register-schema.md` (ID, title, system / WS, SEV / Occ / Det, RPN-B, RPN C, tier + rule, trigger or leading indicator, exposure quantified in dollars, days, and records, owner, mitigation action and date, status, last review, source document). The weekly routine, Friday before the C edition:

1. Re-pull scores; log every RPN change with its cause.
2. Re-test every row >= 700 for active mitigation (3.2, step 4); re-tier.
3. Advance or expire mitigation actions by date; an action past its date with no update becomes "no active mitigation".
4. Add new risks from the week's minutes, notices, telemetry, and permit board; retire closed ones with the closing document cited.
5. Update exposure figures from the cost skill's pull (committed dollars, blocked PO amounts) and the schedule pull (variance days, records affected).
6. Set the last-review date on every row touched; rows not reviewed in 14 days are flagged in the register header.

### 3.9 Schedule health metrics

Compute these on parent rows at each Friday pull, each with its denominator, and compare to the March 2026 baseline snapshot (`asml-pm-agent`, Part 4) and to last week:

| Metric | Definition | March 2026 baseline (W77) |
|---|---|---|
| % behind baseline | Rows with negative Variance2 / rows with a baseline | 473 (71.6% per the snapshot, which implies 661 rows carrying a baseline) |
| Not started past start | Rows at 0% with START before the pull date | 194 not started (95.6% of tracked) at baseline; the past-start subset is computed per pull |
| Variance days | Sum and median of negative Variance2; worst 10 rows named | Per pull |
| Bow wave | Rows with END in the final program year | 102 projects deferred to 2032 |
| 2026 at 0% past Q1 without constraint | YR. = 2026, % = 0, pull date > 03/31/26, Constraints blank | Per pull; the class is one finding (3.1, rule 3) |
| Health distribution | Green / Yellow / Active / Pending counts | 32 / 42 / 13 / 10 of 97 |

Growth in the bow wave between pulls is a program-level signal: report the delta and the rows that moved into the final year. A shrinking bow wave that coincides with rows disappearing from the sheet is a data finding until the deletions are explained.

### 3.10 Critical path, float, and slip

The roadmap is a portfolio tracker, not a logic-linked schedule; its Predecessors column is sparse. Treat critical path and float as schedule-file facts and get them from the P6 export or the project schedule the contractor is obliged to maintain, through J. Yazici when the question is contested. Rules:

1. Slip is Baseline Finish to current END, in calendar days, on the row's own baseline; Variance2 is the sheet's version of that figure and is checked, not trusted.
2. Float is total float from the schedule file at a stated data date. Report float consumed as a fraction of the float at baseline; above 50% is A2, and a critical-path row (zero float) slipping past 30 days is R3.
3. A contractor's float claim is their position until CSL has recomputed it from the file. Write both figures when they differ.
4. Owner-caused, contractor-caused, and concurrent delay are attributed with dates and documents at the time of the slip, not reconstructed later; the contractual consequences are in the installed `aia-contracts-capital-projects` skill (Article 8).
5. Schedule compression accepted on CSL's behalf is reported in the five-part form of 3.4, step 5, and put on record as the accepting party's.

### 3.11 Escalation

The path (who hears it first, then next) is in `references/escalation-matrix.md`; this skill decides only that a finding must travel and in what form. Every escalation carries, in this order: item and document number; tier and rule; exposure in dollars, days, and records; what has already been done; the decision or action requested; owner and date; attachments (pull snapshot, transmittal evidence, notice). Draft the escalation in the same reply the finding appears in; the operator decides whether it goes. Nothing is sent by the agent.

| Tier | Form | Skill that writes it |
|---|---|---|
| RED, stands alone | Executive or decision memo `CSL-W77-MEM-yymmdd` | `csl-executive-memo` |
| RED, record reversal or misstatement | Same-day record-correction reply | `csl-client-comms` |
| RED, field or telemetry | Facilities notice, FM- format | `csl-technical-docs` with D. Wolf |
| AMBER | Weekly report finding, docket item, follow-up email | `csl-weekly-reporting`, `csl-client-comms` |

---

## 4. Output specification

**"What moved this week" table** (template: `templates/what-moved-table.md`). One page. Bottom line first as a two-sentence headline (what moved, what did not and should have). Then the table, sorted RED, AMBER, GREEN and within tier by exposure: Row / ID | Source | Last pull | This pull | Delta | Tier (rule) | Cause | Owner | Next action and date. Then a three-line source note (sheet, ID, pull timestamp, hash match yes/no).

**Risk register extract** for the C edition: top 10 by RPN C, every RED, every tier change this week. Columns per the schema. A one-line count header: "Register: <n> rows; <r> RED; <a> AMBER; <c> tier changes this week; <p> rows past review date."

**Schedule health block**: the six metrics in 3.9 with baseline, last pull, this pull, delta, and a one-clause cause per metric that moved.

**Mitigation KPI strip**: open, past-target, closures, concentration, data defects, with last-week values in parentheses.

**Look-ahead framing block** for the A edition: anchor rows with END dates; outer frame with provenance; five-part compression statement when one applies; docket for the week.

**Docket**: every open item from the blocks above as one row: item, tier (rule), owner, action, date, evidence of closure expected. Items carried from a previous edition show the edition they first appeared in.

**Charts** (at most two per edition, per `csl-brand` Section 6 and the `dataviz` skill): the past-target trend with closures overlaid, titled by the finding ("Past-target rose to 17 with no closures"); the RPN watchlist as a horizontal bar sorted descending with the 700 threshold drawn as a hairline. Status colors only on tier-coded marks; source line under each chart.

Numbering: these blocks live inside `CSL-W77-WKR-nnA/C`; a stand-alone schedule variance or risk memo is `CSL-W77-MEM-yymmdd` (`csl-document-control`). Rendering and chart rules per `csl-brand` (status colors from Section 1.4; never CSL Red for RED; tier word beside every color).

---

## 5. Voice and formatting rules

- State the row, the dates, the delta, the tier with rule, the owner, the action, the date. In that order.
- Tracker facts are stated as tracker facts: "END 08/28/26 on CSL Tasks", not "due end of August".
- Verbal dates carry their provenance in the same sentence: "stated on the call by T. Dube 08/05/26; written confirmation requested <date>."
- Contractor or vendor float and duration claims are recorded as their position: "MMI states 14 days float; CSL's calculation from the P6 export shows 3."
- Client-executive editions: no dash constructions in running prose; spell out acronyms on first use per page; tables for anything with more than three numbers.
- Numbers with denominators and units: "17 of 20 open rows past target", "~1,480 records", "107 days".
- Interpersonal friction is written as a record discrepancy with documents and dates, never as character.

---

## 6. Worked example: what moved, week ending 09/18/26

Populated from the WKR-38C record (Friday 09/18/26 pull). Live pulls are required before any reissue; the figures below are for shape and standard, not for reuse.

**Headline.** The roadmap did not move for a sixth consecutive pull while the permit board recorded a fourth perfect week and the loops working sessions produced a written re-baseline; the mitigation sheet closed nothing and added two past-target rows. Two items are RED on tracker grounds, not field grounds.

| Row / ID | Source | Last pull (09/11) | This pull (09/18) | Delta | Tier (rule) | Cause | Owner | Next action, date |
|---|---|---|---|---|---|---|---|---|
| Roadmap Master, all parent rows | 1059284113641348 | Hash identical to 09/04 | Hash identical; sixth consecutive frozen pull | 0 rows changed; milestones lapsed inside window | RED (R5) | Tracker not maintained while permits 53782 and 51718 moved in the field | Roadmap owner (ASML) via B. Gannon | Change list of rows to update issued with WKR-38C; review Tue 09/22 |
| Electrical Distribution MV & LV | Roadmap | RPN C 1,000; no dated mitigation | Unchanged; ninth consecutive week reported | 0 | RED (R1) | No dated mitigation on the row at any of nine pulls | B. Gannon | Mitigation owner and date requested in writing 09/18 |
| Planon full-building upload outer frame | Minutes #019 | ~09/15/26 (verbal 08/05) | Re-baselined in writing 09/15 | ~1,480-record recode delta before relabel | AMBER (A5) | Versioned functional-code spec requested in writing 09/10; unanswered 6 business days | T. Dube (spec), S. Schryba (recode) | Spec and written delta review before any relabel; #020 |
| Mitigation sheet, past-target | 2158727850315652 | 15 | 17 | +2; 0 closures | AMBER (A2) | Two targets passed in the week; no closures | Row owners; 10 of 20 open on B. Gannon | Owner-by-owner review at Tue Planon weekly |
| WS-06.02 flush (PO $25,947.71) | Mitigation sheet; PO record | Blocked, 11 days | Blocked, 18 days since first report 08/31 | +7 days | AMBER (A3) | Requester of record out of office; PO cannot release | D. Wolf to unblock via ASML | Delegate approver requested; see `csl-cost-change-control` |
| SIPP permit 54164 REMA pump | 289677048237956 | Not on board | New; dates inverted (START 10/12/26 after END 10/09/26) | New row | AMBER (A6) | Data-entry defect on a new permit | Permit coordinator | Correction requested 09/18; gates 3 of 5 |
| SIPP permit 51718 tie-in | 289677048237956 | Open, 39 days | Closed 09/18 at 46 days | Closed | GREEN (G) | Closed with gates complete | Contractor PM | None; record complete |
| BCA + IRO merged tracker (LOE) | B. Gannon request 09/18 | Not open | Proof of concept built 09/17 (348 records); LOE owed | New commitment | GREEN (G) | New scope, new row, new number | S. Schryba | LOE per `csl-bd-pursuits`, week of 09/21 |

Source note: Roadmap Master 1059284113641348 pulled 09/18/26 06:40 ET, hash identical to 09/11/26; Mitigation Plan 2158727850315652 pulled 09/18/26 06:41 ET; SIPP Permits 289677048237956 pulled 09/18/26 06:42 ET; CSL Tasks 7673437876080516 pulled 09/18/26 06:43 ET. Minutes #019 (09/15/26) for the re-baseline.

What the owner learns from the page: the two REDs are governance conditions that an ASML tracker owner can clear this week; the re-baseline is on record with its delta; the mitigation sheet needs an owner-by-owner review rather than more rows; the permit board is clean.

---

## 7. Failure modes and how to avoid them

| Failure | What it looks like | Avoidance |
|---|---|---|
| Adopting contractor float claims | "14 days float remaining" appears in a CSL report with no calculation | Recompute from the schedule export; record the claim as the contractor's position |
| Averaging conflicting sources | END 08/28 and ~09/15 become "early September" | State both dates with provenance; never blend |
| Carrying last week's numbers | Past-target shows 15 because the sheet was not re-pulled | Every figure from this session's pull; pull timestamp in the source note |
| Treating a verbal ruling as baseline | A call-stated date becomes the END in CSL's own tracker | "Stated on the call by <name>, <date>; written confirmation requested" until minuted |
| Tier without rule | A red cell with no reason | Rule ID beside every tier; pre-issue grep for bare tier words |
| Letting new scope ride an existing row | The BCA + IRO merge tracked under the dashboard row | New row, new number, budget line, or written decline (csl-operating-rules, Section 8) |
| Reading a frozen tracker as an idle field | "No activity on the roadmap" in a headline | Attribute to the tracker; cite the permits and deliveries that moved |
| Reporting a bulk closure as progress | "Past-target fell 54 to 15" with no closure count | Closure count beside every past-target move |
| Double-counting phases | Child rows summed into portfolio metrics | Parent rows only; state the row count used |
| Silent RPN edits | RPN C changes with no reason in the pull | Log the factor that moved and the source; flag unexplained changes |
| Tiering every row in a class | 40 RED rows for one data condition | One population finding, worst row sets the tier, top rows listed |

---

## 8. Pre-issue checklist

- Every figure traces to a pull made in this session; timestamps and hashes in the source note.
- Every tier carries its rule ID; no bare RED / AMBER / GREEN anywhere in the file.
- Every RED has owner, action, and date, or states that one is missing and who was asked for it.
- Every date is checked against a calendar (`date -d`); ISO week numbers computed, not counted.
- Verbal dates carry provenance; written re-baselines cite the minutes number.
- Both dates shown wherever a tracker date and a spoken date differ.
- Contractor and vendor claims are attributed, not adopted.
- Data defects (ID formats, blank baselines, inverted dates) counted and excluded with a footnote.
- Escalation triggers from csl-operating-rules Section 6 checked against this week's findings; anything firing is in the headline.
- Brand QA run (`csl-brand/references/brand-qa-checklist.md`); status colors from Section 1.4, tier word paired with every color.
- Document number and file name per `csl-document-control`.

---

## Files in this skill

- `references/tier-rules.md` — the stand-alone tier decision table (R1–R9, A1–A6, G) with the situation map, for other skills to load when they need to show a tier.
- `references/risk-register-schema.md` — full register schema with field definitions, example rows, and the weekly review routine.
- `templates/what-moved-table.md` — the one-page "what moved this week" skeleton with a populated example row per section.

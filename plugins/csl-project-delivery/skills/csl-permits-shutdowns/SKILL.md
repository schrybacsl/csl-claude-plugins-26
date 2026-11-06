---
name: csl-permits-shutdowns
description: >
  Owner's-rep oversight of contractor work permits (SIPP and equivalents) and shutdowns: the gate
  model, gated-in-time and perfect-week counts, the Friday permit board section, permit-board data-
  quality flags, work-done-no-record reconciliation, shutdown and outage packages with staged gates,
  tie-ins, hot work, LOTO, confined space, crane lifts, and correlating permits with schedule claims
  and telemetry. Use it whenever someone says "permit board", "SIPP", "shutdown package", "outage
  window", "gates", "perfect week", "did they have a permit", "tie-in", or "LOTO", and whenever a
  Friday report needs its permit section.
---

# CSL Permits and Shutdowns

The permit board is the owner's evidence that contractor work in an operating facility happened where, when, and how it was authorized, and the weekly permit section is how the owner learns that without walking the roof. This skill defines the gate model and the perfect-week metric, the weekly pull and its data-quality rules, the Friday permit board section, the work-done-no-record rule, the shutdown and outage package, post-event reconciliation, and how permits are used as the field witness when a contractor claims access limitation, a tracker says complete, or telemetry shows an excursion. The SIPP process itself (Safety in Process Planning: form fields, priority classes, four-approver workflow, daily alignment meeting, 200-#### numbering, Smartsheet automation) is in the installed `sipp` skill and is not repeated here. Outputs feed `csl-weekly-reporting` (the WKR-nnC permit board section and the WKR-nnA look-ahead), `csl-schedule-risk` (field-movement witness for frozen trackers), and `csl-executive-memo` (notices). Tiers per `csl-schedule-risk/references/tier-rules.md`.

---

## 1. Bottom line / when this runs

| Product | Cadence | Feeds |
|---|---|---|
| Weekly permit board section (started, closed, walkthroughs, windows, new for the coming month, data-quality flags, work with no record, perfect-week streak) | Friday, from the Friday pull | WKR-nnC; Monday WKR-nnA carries the permits starting next week |
| Work-done-no-record notice | Same day it is observed | `csl-executive-memo` notice; escalation per `references/escalation-matrix.md` |
| Shutdown or outage package with staged gates | Per event; gate count at T-14, T-7, T-2, T-0 | Alignment meeting; WKR; post-event reconciliation |
| Post-event reconciliation | Within two business days of restoration | WKR; CTRW telemetry summaries (`csl-data-pipeline`) |
| Permit-versus-claim check | On demand when a contractor, tracker, or telemetry makes a claim | Schedule finding (`csl-schedule-risk`); record correction (`csl-client-comms`) |

Two rules are absolute because csl-operating-rules Section 6 makes them so: work executed without its gate record complete is RED (R6) until backfilled, and the backfill is reported when it happens.

---

## 2. Inputs and pulls

| Source | What this skill reads | QA before use |
|---|---|---|
| SIPP Permits sheet (W77: Smartsheet 289677048237956) | One row per permit with the columns in `references/permit-board-schema.md` | Full-sheet pull, filter locally (connector date-filter defect); hash against last pull; QA rules in 3.3 |
| Gate records per permit (approval columns, hazard control confirmations, isolation verification, gas measurements, PPE, JSA, alignment meeting attendance) | Gates cleared of total, with timestamps | A gate with no timestamp is not cleared |
| Alignment meeting log (`sipp`, Part 5) | Permits reviewed, conflicts, attendees by role, closeouts confirmed | Meeting date against permit start dates |
| Contractor daily reports, field reports (`csl-design-construction-oversight`), Clerk of the Works notes | Work reported by date and location | Every reported activity matched to a permit row |
| Shutdown package and isolation list | Scope, isolations, restoration verification | Restoration line for every isolation line |
| CTRW telemetry (TR7 m4535, TR2 m8357, TR5 m5794) and BMS trends | Excursions inside permit windows | Both logger paths pulled; "dark" windows may be export artifacts (`csl-data-pipeline`) |
| Roadmap Master (1059284113641348), CSL Tasks (7673437876080516), P6 export | Rows the permit's work belongs to | Permit start and close dates are the field witness for the frozen-tracker test (`csl-schedule-risk` 3.6) |

Record sheet name, ID, pull timestamp (ET), row count, and hash for every pull. W77's board carries the site's five-digit permit numbers (`53782`, `51718`, `54164`); the `200-####` format in `sipp` is the generic Smartsheet implementation. Cite the number as the board carries it and never renumber (`csl-document-control` 1.2).

---

## 3. Method

### 3.1 What this skill adds to SIPP

`sipp` governs how a permit is requested, reviewed, approved, aligned, executed, and closed. This skill is the owner's reporting and oversight layer on that record: it counts gates, tests timing, finds the rows that contradict themselves, ties permits to schedule and telemetry, and tells the owner every Friday whether the week was clean. When the two overlap (alignment meeting agenda, approval statuses), `sipp` is the authority for the process and this skill for what CSL reports about it.

### 3.2 Gate model, gated in time, perfect week

A permit carries N gates, and N is set by what the permit declares. A pump replacement may carry 5 gates; a building shutdown package aggregates 40 across its constituent permits and isolations. The gate families, what clears each one, and the evidence CSL reads:

| Gate family | Cleared when | Evidence on the board or attached |
|---|---|---|
| Approvals | Each required approver (system owner, project manager, EH&S, manufacturing or operations, per `sipp` Part 4) has recorded Approved or Approved with Conditions | Approval column with date per role; conditions acknowledged by the contractor |
| Hazard controls | Each identified hazard has its named control in place | One gate per hazard; control confirmed by the walk or the alignment meeting |
| Isolation | Every LOTO point locked, tagged, and zero energy proven | Isolation list with lock numbers and verification timestamp |
| Gas measurement | Atmosphere tested inside the required window before entry or hot work | Readings, instrument, time, tester |
| PPE | PPE matrix confirmed for the crew | Toolbox talk record referencing the permit |
| JSA / pre-task plan | Crew-signed JSA attached to the permit | Signed sheet with date and crew count |
| Alignment meeting | Permit reviewed at the daily alignment meeting before start | Meeting log entry citing the permit |

Every gate carries a timestamp; a gate marked cleared with no timestamp is counted as open, because the timing test in the next table cannot be run without it.

| Term | Definition | How it is reported |
|---|---|---|
| Gate progress | Gates cleared of total, each with a timestamp | `3/5`, `37/40`; the count and the names of the open gates |
| Gated in time | Every gate cleared before the permit's start date and time | Yes / No per started permit; No names the gate and the clearance time relative to start |
| Perfect week | Every permit that started in the reporting week was gated in time, and no work was reported without a permit | "Perfect week: yes" or the permits that broke it |
| Streak | Consecutive perfect weeks, counted through the Friday of the current edition | "Fourth consecutive perfect week through 09/18/26"; one ungated start or one RED (R6) item resets the streak to zero and the reset is reported with the permit that caused it |

Package convention: a week with a RED (R6) item is not a perfect week whatever the gate record of the permits that did start, because an unpermitted start is exactly the ungated start the metric exists to catch. W77 recorded four consecutive perfect weeks through 09/18/26 (weeks ending 08/28, 09/04, 09/11, 09/18); the streak is re-derived from the pull every Friday, never carried forward.

### 3.3 Weekly pull and data-quality rules

Pull the full sheet Friday morning before the C edition, hash it, diff it against last Friday's snapshot, and run the QA rules in this order, because the flags decide which rows can be counted:

| Rule | Test | Tier and action |
|---|---|---|
| Date order | Finish date before start date | AMBER (A6); correction requested from the permit coordinator the same day; the row is still counted for gate progress but excluded from duration statistics |
| Status versus dates | Status Closed with no finish date; status Approved or Active with start in the past and no gate timestamps; status Submitted with start already passed | AMBER (A6); named per row; a started row with no gate timestamps is tested as an ungated start |
| Missing contractor | Contractor blank on a submitted or later row | AMBER (A6); the row cannot be attributed and is listed |
| Duplicate numbers | Same permit number on two rows | AMBER (A6); both rows listed; the coordinator states which is the record |
| Aged open | Open more than 30 days with no window or closeout entry (`sipp` KPI: open SIPPs > 30 days) | Listed with days open; multi-window permits state their remaining windows instead |
| Byte-identical sheet | Hash unchanged from last Friday while field reports show permitted work | AMBER (A4) one pull; RED (R5) two pulls |

The W77 case that fixed the date-order rule: permit 54164 (REMA pump) arrived on the board with START 10/12/26 after END 10/09/26; it was reported as AMBER (A6) with the correction requested 09/18/26, and its gate progress (3 of 5) was still reported, because a data defect on the dates does not excuse the owner from knowing whether the permit is ready.

Compute the derived fields in code after the QA pass, and save them with the pull snapshot (`references/permit-board-schema.md`, Section 2):

| Derived field | Formula | Used for |
|---|---|---|
| Days open | Pull date minus start date, open rows only | Aged-open list |
| Days to start | Start date minus pull date, future rows only | New-for-the-coming-month block |
| Gate progress | Gates with a timestamp of total gates declared | Every block |
| Gated in time | All gate timestamps earlier than start date and time | Perfect-week test |
| Duration at close | Finish date minus start date, closed rows only, excluding date-order flags | Closed block; 30-day KPI |
| Window count | Windows executed of windows declared, from the permit's window schedule | Multi-window permits |
| Field witness flag | Start or close inside the current pull window | Frozen-tracker test in `csl-schedule-risk` 3.6 |

### 3.4 Weekly permit board section (Friday report)

Write the section in this order, every week, so editions compare (template: `templates/permit-board-weekly-section.md`):

1. Headline: perfect week yes or no; streak; counts of started, closed, new, flagged, and work-with-no-record items.
2. Permits started this week: number, description and type of work, contractor, start date, gate progress at start, gated in time yes or no.
3. Permits closed this week: number, description, opened, closed, duration in days, windows executed of total, closeout record complete yes or no. A duration above 30 days is stated with the reason the record gives (multi-window, tie-in sequence) rather than left to look like neglect; the tie-in permit 51718 closed 09/18/26 at 46 days with gates complete.
4. Walkthroughs held: date, permits covered, attendees by role, outcome (from the alignment meeting log, not the permit sheet).
5. Windows executed: permit, window k of n, date, outcome; a multi-window permit executing window 2 is reported as window 2 with the remaining windows and dates.
6. New permits opened for the coming month: number, description, start date, days to start, gate progress (`3/5`), approvals outstanding by role.
7. Data-quality flags: each flagged row with the rule, the tier (rule), and the correction request date.
8. Work reported with no record: what, where, when, who reported it, RED (R6), backfill status.
9. Source note: sheet, ID, pull timestamp, row count, hash changed or not, alignment log dates.

A metric that the pull did not carry is written as "not available at <pull time>, source <name>" (csl-operating-rules, Section 9), never filled.

The Monday Look-Ahead (WKR-nnA) carries the forward half of the same record as a strip, so the commitment week opens with the permits it depends on:

| Permits starting in the commitment week | Start | Gate progress at the Sunday pull | Open gates | Owner of the next gate |
|---|---|---|---|---|
| 54164 REMA pump (once dates are corrected) | 10/12/26 | 3/5 | Two, named from the board at the pull | Permit coordinator; contractor PM |

A permit inside the commitment week with gates open at the Sunday pull is a docket item with the gate owner named, because Monday is the last day the owner can act before the alignment meeting decides it.

### 3.5 Work done, no record

Field activity observed or reported with no matching permit row is RED (R6) the same day, whatever the schedule or the tracker says. Method: record what was seen or reported, where, when, and by whom (contractor daily report, field walk, telemetry, a tracker row flipped to complete); search the board for a permit covering that work, location, and window, including permits under a different contractor's name; if none, issue the notice (`csl-executive-memo` notice form; escalation path in `references/escalation-matrix.md`: operator, then site EH&S or permit coordinator and the contractor PM, then the client program lead); log it on the risk register. When the permit is backfilled, report the backfill with the permit number and the date the record was completed, and state that the tier moved from RED (R6) to closed on that date. A backfilled permit does not restore the perfect week it broke.

### 3.6 Event types and what the owner's rep checks

The `sipp` form decides the permit types and PPE; this table is what CSL confirms on the board and in the field for each event type, with the W77 examples on record:

| Event | What CSL checks | W77 example |
|---|---|---|
| Hot work | Hot work permit gate; 35-ft combustible clearance; fire watch during and 60 minutes after; detection impairment coordinated with EH&S and restored | Standard on every welding and grinding row |
| LOTO | Energy sources listed; lock assignment; zero-energy verification timestamp; restoration verified and logged | Isolation gates inside every tie-in and pump permit |
| Confined space | Atmospheric test results before entry and continuous monitoring; attendant named; rescue plan; gas measurement gate timestamped | Gas measurement column on the board |
| Crane lift | Lift plan on the permit; certified rigger; exclusion zone and overhead path cleared; wind limit; alignment meeting the day before | Crane permit 53782 started Wed 09/16/26 fully gated |
| Wall opening for machine delivery | Structural review of the opening; dust and weather containment; security and traffic plan; delivery sequence timed | Wall opening gated in time for a Saturday three-machine delivery |
| Utility tie-in | Outage window agreed with operations; isolation list; pressure test and flush; restoration verification; multi-window sequence stated | Tie-in permit 51718 opened 08/03/26, closed 09/18/26 at 46 days with gates complete |
| Roof work | Roof access permit; weather and lightning rule; load limits; fall protection; drainage protection | Rooftop air-handler work (the 90-unit WS-02 population sits on the roof) |
| Radio / BDA install | Penetrations and firestopping; fire alarm interface and impairment permit where the BDA ties to life safety; AHJ acceptance test | Low-voltage rows reviewed for the life-safety impairment gate |
| Pump replacement | LOTO; isolation and drain; alignment and run test; restoration | REMA pump permit 54164, gates 3/5, dates inverted at the 09/18/26 pull |
| Building shutdown or outage | Shutdown package (3.7); gates staged and counted at T-2; restoration verified | 08/22/26 building shutdown: 37/40 at T-2, closed 40/40 with no incidents |

### 3.7 Shutdown and outage package

A shutdown is a set of permits, isolations, and communications executed in one window, and the owner's rep owns the package that holds them together (template: `templates/shutdown-package.md`). Build it in this order and report the gate count at T-14, T-7, T-2, and T-0:

1. Scope: what is being done, by whom, in which window, and the abort criteria.
2. Affected systems and areas: system tags, areas served, production or tool impact per operations, and the operations sign-off.
3. Sequence: a timed line from pre-shutdown checks through isolation, work, restoration, and verification, with the owner of each step.
4. Isolation plan: every isolation point (valve, breaker, blind) with its lock, the person who applies it, and the restoration line beside it.
5. Communication plan: notifications at T-14, T-7, T-2, T-0, and restoration; who sends them, to whom, on which channel; the alignment meeting date.
6. Permits and gates staged: every constituent permit with its gate progress; the package count is the sum. On W77 the 08/22/26 building shutdown stood at 37 of 40 gates on Thu 08/20/26, two days before start; the three open gates were named with their owners and latest clearance times, and the package closed at 40 of 40 with no incidents.
7. Contingency and restoration: what stops the work, who decides, how systems come back and in what order, and the verification points (pressures, flows, alarms cleared).
8. Post-event reconciliation (3.8) within two business days.
9. Lessons captured in the next look-ahead (WKR-nnA) as dated items with owners, not as a paragraph.

The gate count is reported at four checkpoints, and each checkpoint has its own question, because a count without the question behind it is a number nobody acts on:

| Checkpoint | Question answered | Who confirms | Escalation if the answer is no |
|---|---|---|---|
| T-14 days | Are all constituent permits submitted and the outage window confirmed by operations in writing? | CSL PM; operations | Window not confirmed: the shutdown is not on the look-ahead as a date, only as a request |
| T-7 days | Are approvals complete on every permit; is the isolation list walked and every point found? | Approvers; system owner | Approval past SLA: reviewer role and days named to the client program lead |
| T-2 days | Gate count staged; open gates named with owners and latest clearance times; communications sent | CSL PM; permit coordinator | Any open gate that cannot clear before T-0 by its owner's statement: go / no-go decision recorded in writing |
| T-0 | Alignment meeting held; every gate cleared with a timestamp before the first isolation | Alignment meeting | Work does not start; the window is rescheduled and the reason recorded |

### 3.8 Post-event reconciliation

Close the event on the record, not on the handshake. Within two business days of restoration, confirm and report: every constituent permit closed with its closeout record; every isolation on the plan shows its restoration line completed and verified; telemetry and BMS trends for the affected systems checked across the window for excursions; any excursion inside the window attributed to the planned event with the permit and window cited; any excursion outside the window investigated as a fault. On the 08/22/26 shutdown a test-rig stop in the CTRW telemetry coincident with the shutdown window was attributed to the planned shutdown with the permit and window cited, rather than logged as a rig fault; without this step it would have opened a false RED (R9) inquiry and cost a week of vendor time. Reconciliation findings go into the WKR-nnC and, where they touch the rigs, into the CTRW summaries (`csl-data-pipeline`).

| Reconciliation item | Evidence required | Result form |
|---|---|---|
| Permits closed | Closeout record on every constituent permit | "<k> of <n> permits closed; open: <numbers>" |
| Isolations restored | Restoration line completed and verified per isolation point, with the verifier and time | "<k> of <n> isolations restored and verified" |
| Telemetry checked | Channels and logger paths named; window start and end in ISO 8601 with zone | Excursions listed with time and attribution |
| Excursions attributed | Permit number and window cited for each excursion inside the window | "Attributed to the planned shutdown (permit <n>, window <dates>)" |
| Excursions unexplained | Any excursion outside a permit window | Investigated; tiered per `csl-schedule-risk` (R9 for tool-down or leakage signatures) |
| Incidents and near misses | Count and numbers; conditions only | "No incidents" or the incident numbers |
| Lessons | Dated docket items with owners | Carried into WKR-nnA |

### 3.9 Correlating permits with schedule, trackers, and telemetry

The permit board is the field witness, and it is checked before any claim is adopted:

| Claim | Check the board for | What the owner learns |
|---|---|---|
| Contractor claims access limitation delayed the work | A permit submitted for that work, location, and window; its approval dates against the `sipp` SLA; declines and their reasons | No permit submitted: the claim has no record and is reported as the contractor's position. Permit held past SLA by a reviewer: an owner-side delay, reported honestly with the reviewer role and days |
| Tracker or roadmap row says complete | A closed permit for that work with closeout record | Complete with no permit is RED (R6) or a false tracker entry; either is reported, and the row is not accepted as complete |
| Telemetry shows an excursion | A permit whose window covers the excursion | Covered: attribute and cite. Not covered: investigate; RED (R9) if the signature is tool-down or leakage risk |
| Tracker unchanged for two pulls | Permits started or closed on the tracker's rows | Field moved while the tracker did not: RED (R5), attributed to the tracker (`csl-schedule-risk` 3.6) |
| Requisition claims work in place | Permits closed for that work in the billing period | Billed work with no permit is a payment question (`csl-cost-change-control`) |

The access-limitation check in practice: a contractor states that a roof activity slipped two weeks because access was not granted. The board shows the permit submitted as Routine on a Thursday with a Monday start, inside the 48- to 72-hour SLA in `sipp` Part 4; EH&S approved within the SLA; the system owner approval came six days later. The finding reads: submission was compliant; one approval exceeded the Routine SLA by four days; the remaining ten days of the claimed slip have no permit-side cause. The contractor's statement is recorded as their position; the four days are recorded as an owner-side approval delay with the role named; the schedule finding goes to `csl-schedule-risk` with both figures.

### 3.10 Alignment meetings and pre-task planning

The daily alignment meeting (`sipp`, Part 5) is the last gate before work starts, and CSL facilitates or co-facilitates it. Attendees by role: the CSL or owner PM, facilities or system owner, EH&S, the manufacturing or operations representative, and every contractor starting or continuing work. Confirmed on the record: which permits start today and tomorrow and their gate status; scope or hazard changes since approval (any change sends the permit back for re-review); conflicts between concurrent permits sharing utilities, space, or access routes; closeouts from the previous day with documentation. The output is the meeting log with attendees, permits reviewed, decisions, and actions; the log entry is cited on the permit row as the alignment gate and in the weekly section under walkthroughs. Pre-task planning (JSA or PTP) is the crew's own gate: signed by the crew before start, attached to the permit, and checked on the walk. A permit whose alignment gate is timestamped after the work start is not gated in time, whatever the other gates say.

The minimum log entry per meeting, so the entry can be cited from the permit row and the weekly section:

| Field | Content |
|---|---|
| Meeting date and time | `MM/DD/YY HH:MM ET`; facilitator |
| Attendees by role | CSL/owner PM, facilities, EH&S, operations, contractors present (organization) |
| Permits reviewed | Number, status (starting, active, closing), gate status stated |
| Changes and conflicts | Scope or hazard changes sent back for re-review; concurrent permits sharing utilities, space, or access, and the resolution |
| Closeouts confirmed | Permits closed the previous day with documentation confirmed |
| Actions | Owner, action, date |

### 3.11 Escalation

Work done with no record: same-day notice to the operator, then site EH&S or the permit coordinator and the contractor PM, then the client program lead (`references/escalation-matrix.md`, Section 2). Data-quality flags: correction request to the permit coordinator the same day; AMBER (A6) in the weekly section until corrected. Telemetry excursion with a tool-down or leakage signature: facilities notice in the FM- format with D. Wolf (`csl-technical-docs`). Every escalation carries item and permit number, tier and rule, exposure (gates open, hours of unpermitted work, systems at risk), what has been done, the action requested, owner, and date.

### 3.12 Weekly rhythm

| When | Work | Output |
|---|---|---|
| Sunday / Monday | Pull the board with the other Sunday pulls; compute days to start and gate progress for the commitment week | WKR-nnA permit strip; docket items for open gates |
| Daily | Alignment meeting attended or the log read; field reports matched to permit rows | Log entries; same-day R6 notice if a match fails |
| Per event | Shutdown package staged at T-14, T-7, T-2, T-0; reconciliation within two business days | Package revisions; reconciliation page |
| Friday | Full pull, hash, QA rules, derived fields; section written in the order of 3.4; streak recomputed | WKR-nnC permit board section; pull snapshot filed |

---

## 4. Output specification

**Weekly permit board section** (inside `CSL-W77-WKR-nnC`; template in `templates/`): headline line; eight blocks in the order of 3.4; source note. Tables for started, closed, new, and flags; one line each for walkthroughs, windows, and work with no record when there are none to table. Tier cells use the status colors of `csl-brand` 1.4 with the tier word and rule present. The Monday WKR-nnA carries a two-column strip: permits starting in the commitment week with gate progress.

**Work-done-no-record notice**: item, permit search performed (board, date range, contractors searched), what was observed and by whom, RED (R6), exposure, action requested (backfill and cause), owner, date; `CSL-<PROG>-MEM-<yymmdd>` or the facilities notice format when the work touched a utility.

**Shutdown package**: the nine parts of 3.7 as sections; gate count line at T-14, T-7, T-2, T-0; isolation table with restoration column; controlled document `CSL-<PROG>-SDP-<yymmdd> Rev <n>` (package convention of this skill; add to `csl-document-control` 1.1 when the table is next revised), filed with the permits it covers.

**Post-event reconciliation**: one page: permits closed of total; isolations restored of total; telemetry windows checked with the channels named; excursions attributed or investigated; lessons as dated docket items.

**Permit board pull file**: the columns of `references/permit-board-schema.md` plus the derived fields (days open, days to start, gate progress, gated in time, duration at close), saved as the pull snapshot beside the report (`csl-document-control` Section 8).

---

## 5. Voice and formatting rules

- Permit number first in every sentence about a permit: "Permit 51718 (utility tie-in) closed 09/18/26 at 46 days with gates complete."
- Gate counts as cleared of total: `37/40`, never a percentage alone.
- Dates as the board carries them; an inverted pair is quoted as found ("START 10/12/26, END 10/09/26") beside the flag.
- Contractor explanations for late permits or missing records are recorded as their position with the date.
- Client-executive editions: no dash constructions in running prose; spell out SIPP, LOTO, BDA, and JSA on first use per page.
- Incidents are described as conditions with permit numbers and times; no personal or health information about anyone.

---

## 6. Worked example: permit board section, week ending 09/18/26

From the WKR-38C record (week Mon 09/14/26 to Fri 09/18/26; SIPP Permits 289677048237956 pulled 09/18/26 06:42 ET). Restricted to the permit facts on record in this package; the walkthrough and window lines show the "not available" form because the alignment log was not part of that pull. Re-pull before any reuse.

**Headline.** Perfect week: yes; fourth consecutive perfect week through 09/18/26. One permit started fully gated, one permit closed, one new permit for October flagged for inverted dates, no work reported without a record. The roadmap did not change over the same window while these permits moved (RED (R5) in the roadmap section).

| Started this week | Description and type | Start | Gate progress at start | Gated in time |
|---|---|---|---|---|
| 53782 | Crane lift | Wed 09/16/26 | All gates cleared before start | Yes |

| Closed this week | Description and type | Opened | Closed | Duration | Closeout record |
|---|---|---|---|---|---|
| 51718 | Utility tie-in | 08/03/26 | Fri 09/18/26 | 46 days (tie-in sequence; above the 30-day KPI, reason stated) | Complete; gates complete |

Walkthroughs held: not available at the 09/18/26 06:42 ET pull (source: alignment meeting log held by the site permit coordinator, not part of the sheet pull); added before issue from the log.

Windows executed: not available at the 09/18/26 06:42 ET pull (window schedule held on the constituent permits, not on the board); added before issue.

| New for the coming month | Description and type | Start / End as entered | Days to start | Gate progress | Flag |
|---|---|---|---|---|---|
| 54164 | REMA pump | START 10/12/26, END 10/09/26 | 24 | 3/5 | AMBER (A6): dates inverted; correction requested 09/18/26 |

Work reported with no record: none this week; field reports and contractor dailies for 09/14 to 09/18 matched to permit rows.

Source note: SIPP Permits 289677048237956 pulled 09/18/26 06:42 ET, hash changed from 09/11/26. Roadmap Master 1059284113641348 pulled 09/18/26 06:40 ET, hash identical to 09/11/26 (frozen-tracker finding carried in the roadmap section).

What the owner learns from the section: the week was clean and the streak is four; the tie-in that has run since 08/03 is closed on the record; October's pump permit needs its dates fixed and two more gates before 10/12; the frozen roadmap, not the field, is the governance problem.

---

## 7. Failure modes and how to avoid them

| Failure | What it looks like | Avoidance |
|---|---|---|
| Counting gate progress as gated in time | `5/5` reported for a permit whose last gate cleared after the start time | Test every gate timestamp against the start; "gated in time" is a separate column |
| Perfect week claimed with an R6 item in the same week | The streak grows while unpermitted work is on the field report | Package convention in 3.2: an R6 item breaks the week |
| Carrying the streak forward | "Fifth perfect week" typed from last week's edition | Re-derive from this Friday's pull; the streak is a computed field |
| Duration read as neglect | A 46-day tie-in permit reported as "open too long" | Report duration with the reason the record gives; multi-window permits state remaining windows |
| Inverted dates excluded and forgotten | The flagged row drops out of the gate count | Flag the dates, request the correction, and still report gate progress |
| Adopting an access-limitation claim | Schedule slip attributed to the owner on the contractor's word | Check the board first; report submission and approval dates |
| Reconciling a shutdown by handshake | Isolations restored "per the foreman"; telemetry never checked | Restoration line per isolation; telemetry windows checked; rig stops attributed with the permit cited |
| Treating a telemetry stop as a fault without checking the board | A vendor call opened on a rig that stopped because the building was down | Permit window check before any RED (R9) |
| Backfill reported as if the record had always existed | The notice disappears from the next edition | Report the backfill, its date, and that the week it broke stays broken |
| Renumbering permits | A `200-####` style number given to a W77 site permit | Cite the board's number; never renumber |

---

## 8. Pre-issue checklist

- Every permit cited by the board's own number; no renumbering.
- Gate counts as cleared of total; gated-in-time tested against timestamps for every started permit.
- Perfect week and streak recomputed from this Friday's pull; any R6 item in the week breaks it.
- Every data-quality flag carries its rule, AMBER (A6), and the correction request date.
- Every work-done-no-record item carries RED (R6), the search performed, and the backfill status.
- Closed permits carry duration and, above 30 days, the reason the record gives.
- Shutdown packages show the gate count at T-2 and the closing count; reconciliation lists permits, isolations, and telemetry windows.
- Metrics the pull did not carry are written as "not available at <pull time>, source <name>".
- Escalation triggers from csl-operating-rules Section 6 checked (R5 for frozen trackers with permit movement, R6, R9).
- Brand QA run (`csl-brand/references/brand-qa-checklist.md`); status colors from Section 1.4 with the tier word present; number and file name per `csl-document-control`.

---

## Files in this skill

- `references/permit-board-schema.md` — columns of the permit board pull, the derived fields, the QA rules with their tiers, and the status vocabulary mapping.
- `templates/shutdown-package.md` — the nine-part shutdown and outage package skeleton with gate staging, isolation and restoration table, and reconciliation.
- `templates/permit-board-weekly-section.md` — the Friday permit board section skeleton with one populated example row per table.

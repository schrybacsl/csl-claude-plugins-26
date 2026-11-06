---
name: csl-design-construction-oversight
description: >
  Owner's-rep oversight of design and construction: OAC prep, design review comment logs, submittal
  and RFI logs with days-in-court, weekly field reports and site walks, NCRs and punch lists,
  commissioning oversight (Cx plan, FPT, IST), turnover and closeout packages with data and
  drawings, equipment planning and decision logs, healthcare ICRA/ILSM, AHJ permitting support, and
  contractor accountability. Use it whenever someone says "review this submittal", "RFI log", "field
  report", "punch list", "commissioning", "turnover package", "closeout", "OAC", or "who owns this
  response", or asks whether a response is late or a space is ready for the owner.
---

# CSL Design and Construction Oversight

Design and construction oversight is where the owner's representative earns the title: it is the daily work of making sure what gets designed, submitted, built, tested, and handed over is what the owner asked for, at the price and on the dates the owner approved. This skill defines how CSL reviews (and what it does not review), what CSL brings to the Owner-Architect-Contractor (OAC) meeting, the log standards that make response time and ownership visible, the field report, quality and punch discipline, commissioning oversight, the turnover package, equipment planning, and the healthcare and active-manufacturing specifics. Its outputs feed OAC minutes (`csl-meeting-records`), the weekly report series (`csl-weekly-reporting`), change and payment reviews (`csl-cost-change-control`), and the asset-data hand-off (`csl-asset-data-cmms`). Tiers come from `csl-schedule-risk`.

---

## 1. Bottom line / when this runs

| Product | Cadence | Feeds |
|---|---|---|
| OAC prep one-pager (look-ahead, aged RFIs, submittals pending owner decision, COs pending, safety and permit board, decision log) | Before every OAC, usually weekly | OAC agenda and minutes (`csl-meeting-records`) |
| Log extracts with aging and days-in-court (submittal, RFI, design comment, decision, NCR, punch, Cx issues) | Weekly, from the CSL-kept logs | WKR editions; OAC prep; docket |
| Submittal or RFI review recommendation | Per item routed to the owner | Owner decision record; the log |
| Weekly field report FR #nn | Weekly (daily walk notes roll into it) | Dashboard field module; pay app review evidence |
| Commissioning oversight status block | Per Cx milestone; monthly during Cx | WKR; turnover readiness |
| Equipment decision log extract and equipment planning tiles | Weekly with the OAC prep | `csl-dashboard-kpi` tiles |
| Turnover package index with status per line | From 75% complete through final acceptance | Closeout recommendation; `csl-asset-data-cmms` |
| Problematic-equipment watchlist; assessment with triage rule | Per workstream, issued in the ASM family | `csl-technical-docs`; mitigation sheet rows |

The posture in one sentence: CSL reviews for conformance to the owner's requirements, budget, schedule, and operability; the Architect/Engineer (A/E) remains responsible for design intent and code; CSL recommends and never stamps, approves, or accepts design. Every item that leaves this skill carries a tier with its rule, an owner, and a date, because an oversight log without those three is a diary.

---

## 2. Inputs and pulls

| Source | What this skill reads | QA before use |
|---|---|---|
| CM submittal and RFI logs (Procore, ACC, or spreadsheet export) | Item, spec section, dates in and out per party, status, ball-in-court | Reconcile counts against the CSL log every week; report differences as record discrepancies, AMBER (A6). Blank ball-in-court or "under review" with no party is a defect |
| A/E design review responses and submittal actions | Action taken, date, reviewer | Action vocabulary per `references/log-schemas.md`; an undated action is not an action |
| Executed contract and specifications (A201 general conditions, supplementary conditions, Divisions 01 and 23/26 for review and closeout terms) | Response periods, submittal turnaround, closeout list, warranty terms | Read the executed set, not the bid set; article-level reading in `aia-contracts-capital-projects` |
| Owner's Project Requirements (OPR), Basis of Design (BOD), owner design standards, room data sheets | The yardstick every review is measured against | Revision and date on every citation |
| Project schedule (P6 export) and CM look-ahead | Activity dates, float, milestone the item gates | Data date stated; look-ahead compared to the schedule, not taken alone |
| Field notes, photos, Clerk of the Works daily log | Manpower, work in place, observations | Photo numbers referenced; observations dated and located by room or grid |
| Commissioning agent (CxA) plan, checklists, test scripts, issues log | PFC completion, FPT results, IST scope, open issues | Acceptance criteria traced to the OPR; issues log reconciled with the punch list |
| Equipment planner's list and room data drawings (RDD) | OFOI/CFCI/VFCI, new/existing/relocate/dispose, vendor quotes, move costs, RDD status | Category per item; missing category is a defect |
| Permit board (SIPP or the site's permit system) | Permits started, gated, closed; work done with no record | `csl-permits-shutdowns` QA rules |
| W77 specifics: Equipment Summary RPN (Smartsheet 7673299942199172), BR+A FMEA edition on file, Mitigation Plan (2158727850315652) WS-02 rows, FM contractor corrective work-order history | RPN ranking, failure modes, WO history for the watchlist | FMEA edition date on every RPN; WO history never supplied as of 08/06/26, reported as an open data gap |

Record sheet or file name, ID or path, and pull timestamp (ET) for every pull, per `csl-data-pipeline`. Compute days-in-court and aging in code from the date history, never from the current status column, because the current holder hides how long the previous holder sat on it.

---

## 3. Method

### 3.1 Reviewing posture and recommendation language

Review every drawing, specification, submittal, RFI response, and change against four owner questions: does it meet the owner's requirements (OPR, program, standards, room data); does it hold the budget; does it hold the schedule; can the owner's staff operate and maintain it. Code compliance and design intent are the A/E's professional responsibility; when CSL sees a code question, it flags it to the A/E in writing and records the flag, and it does not adjudicate it. CSL does not stamp, approve, or accept design, because doing so transfers liability the owner pays CSL not to carry.

Write the outcome of a review in one of four forms, and no other:

| Form | Use when | Wording |
|---|---|---|
| Recommend acceptance | The item meets the four owner questions | "CSL recommends the Owner accept Submittal 23 73 13-02 as returned by the A/E (No Exceptions Taken, 09/22/26)." |
| Recommend acceptance with conditions | Owner requirements are met if named conditions are closed | "CSL recommends acceptance on condition that the vendor confirm the 460 V / 3-phase connection matches Panel Schedule E-601 before release." |
| Recommend the owner not accept | An owner requirement, budget, schedule, or operability failure | "CSL recommends the Owner not accept PCO-014 as submitted; quantity exceeds the abatement survey by 340 SF." |
| No CSL objection to the A/E's action | The item is a design or code matter the A/E has actioned | "No CSL objection to the A/E's action of Revise and Resubmit." |

Never write "approved by CSL", "CSL accepts", or "CSL confirms code compliance". The agent drafts; the named CSL reviewer signs; the Owner decides (csl-operating-rules, Section 9).

### 3.2 OAC meeting cadence and what the owner's rep brings

Hold the OAC weekly during construction and biweekly in design, with the CM's look-ahead, the A/E's log, and CSL's log all on the table; CSL ran weekly OACs with site visits and field reports on Cytiva Project Falcon (`csl-projects`), and that cadence is the default. Bring, on one page, prepared the day before (template: `templates/oac-prep.md`):

1. Look-ahead for the next two weeks, reconciled against the schedule, with the constraint on any activity CSL does not believe will start.
2. Open RFIs aged beyond the contract response period, with days open, ball-in-court, and cost or schedule impact.
3. Submittals pending an owner decision, with the milestone each one gates and the date the decision is needed.
4. Change orders and PCOs pending, with amounts and CSL's review position (`csl-cost-change-control`).
5. Safety and permit board: incidents, ICRA/ILSM status in healthcare, SIPP permits and gates in manufacturing (`csl-permits-shutdowns`).
6. Decision log items due, each with its schedule and cost lever (3.3).
7. Docket: what CSL needs from whom by when.

Each party brings its own instrument, and CSL reads all three against each other before the meeting, because the differences between them are usually the agenda:

| Party | Brings | CSL reads it for |
|---|---|---|
| CM | Three-week look-ahead, RFI and submittal logs, PCO log, safety report, manpower | Activities that moved without a schedule update; items marked closed that CSL's log shows open; scope riding an RFI |
| A/E | Submittal actions, RFI responses, site observation reports, design comment responses | Response dates against the contract period; code flags answered in writing; observations that should be NCRs |
| Owner (facilities, end user, EH&S or infection prevention) | Decisions owed, access and outage windows, operational constraints | Decisions past their lever date; windows that conflict with the look-ahead |
| CSL | The prep sheet, the owner's logs, field report, decision log with levers, permit board | The owner's position on every open item, stated before the meeting starts |

The prep sheet is the owner's brief and stays with the owner side; the minutes that follow the meeting are the record, issued per `csl-meeting-records`. A decision made in the OAC and not in the minutes did not happen.

### 3.3 Logs: submittal, RFI, design comment, decision log with a lever

Keep CSL's own log for each series and reconcile it against the CM's weekly. Full columns and status vocabularies are in `references/log-schemas.md`; the rules that matter most:

| Log | Key fields | Rule that makes it useful |
|---|---|---|
| Submittal | Spec section per MasterFormat 2018 (`masterformat-2018`), submittal number and revision, dates in and out per party, A/E action, workflow status, days-in-court by party (CM / A/E / Owner / Vendor), milestone gated | Status is always a party plus an action; "under review" without a party is rejected. Days-in-court is computed per party from the date history |
| RFI | Number, question in one sentence, drawing and spec reference, cost impact yes/no, schedule impact yes/no, ball-in-court, response due (contract period), aging band (0–7, 8–14, 15–30, > 30 days), response, closed date | An RFI with a cost or schedule impact opens a PCO number or a schedule note the same day; an RFI used to carry new scope gets its own change number (csl-operating-rules, Section 8) |
| Design review comment | Comment ID, discipline, sheet or spec reference, comment, category (owner requirement / budget / schedule / operability / coordination / code flag to A/E), A/E response, CSL disposition, closed by, date | A comment is closed by a named person with a date and the document that closed it, never by the next drawing issue alone |
| Decision | Decision needed, options with cost, recommendation, decision owner, due date tied to a named milestone, schedule consequence if late (days), cost consequence if late ($), escalation at +5 business days (to whom), decision recorded (minutes ref) | The lever columns are mandatory; see below |

Aging and days-in-court are computed the same way on every log so the weekly numbers compare:

| Measure | Definition | Reporting rule |
|---|---|---|
| Days open | Pull date minus date opened, calendar days | Shown on every open item |
| Response period | The period the executed contract sets for that series (RFIs commonly 10 business days in supplementary conditions; submittals per Section 01 33 00) | Stated once at the top of the log extract |
| Aged | Days open beyond the response period | Aged items sort to the top |
| Aging band | 0–7, 8–14, 15–30, > 30 calendar days open | Count per band in the header line |
| Days-in-court by party | Sum of the days each party held the item across every hand-off, from the date history | Reported per party; the current holder alone is never the number |
| Response time (closed items) | Date returned minus date received, per party, median and worst | Weekly and trailing four weeks |

Worked arithmetic for one RFI: opened 09/22/26 by the CM; to the A/E 09/23; returned to the CM for clarification 09/30; back to the A/E 10/02; open at the 10/07/26 pull. Days open 15; days-in-court CM 3 (09/22 to 09/23 and 09/30 to 10/02), A/E 12 (09/23 to 09/30 and 10/02 to 10/07); response due 10/06/26 under a 10-business-day period, so aged 1 day. The line reads "RFI-087, 15 days open, A/E 12 / CM 3, aged 1 day, with A/E".

The decision-log lever comes from a real failure. On the OSU Medical Center Expansion Wing (three-year job completing 2028), the equipment planners' decision log carried the decision, the owner, and a date, and responding parties let the dates pass because nothing happened when they did; the planners had no way to hold anyone accountable. The fix built into the OSU Project Hub: every decision row carries a due date tied to a named milestone, the schedule consequence in days and the cost consequence in dollars if it is late, and an escalation column naming who hears it at +5 business days. A decision row without the lever is a request, not a decision item.

### 3.4 Drawing and specification review

Run drawing sets through the orientation, extraction, correlation, and clash method in the installed `mep-drawing-review` skill (title block, general notes, drawing type, scale, cross-references; equipment tags against schedules; one-lines against panel schedules; P&IDs against plans). Cite specification sections by MasterFormat 2018 number and title from `masterformat-2018` so the comment lands in the right section of the right log. CSL's comments go in the design review comment log under the four owner categories; anything that is a code or design-intent question is logged as a flag to the A/E with the sheet reference, and the A/E's written response closes it. Chilled water and process cooling questions (delta-T, flow, pump and coil selection, mixing valves) use the engineering in `chilled-water-systems`; system color and MasterFormat/UniFormat cross-walks for trackers use `asml-mep-system-color-codes`.

### 3.5 Field reports and site walks

Walk the site daily when a Clerk of the Works is staffed (CSL: R. DiTucci, G. Schaaf) and at least weekly by the PM otherwise; issue one weekly field report per project (template: `templates/field-report.md`). The Brown University Health weekly field report FR #16 (F. MacPherson, Senior PM) was the seed for the field-report module of the Brown Health dashboard, and its sections are the standard:

| Section | Content | Rule |
|---|---|---|
| Header | FR number, week, weather by day, prepared by, distribution | FR numbers run as a series per project (`FR #16`), like minutes |
| Manpower | Headcount by trade by day, CM-reported and CSL-observed | Report both figures when they differ |
| Work in place by area | Room, floor, or zone; what was installed; percent of the activity | Tie each line to a schedule activity ID |
| Safety observations | Condition, location, time, corrected when, by whom | No names of injured persons; incidents by number only |
| Quality observations | Condition against spec section, photo number, NCR opened yes/no | Spec section cited on every quality line |
| Schedule status against look-ahead | Activities planned this week, started yes/no, reason if not | The variance is the finding, not the list |
| Photos referenced | Photo log numbers, location, subject | Photos live in the project photo log; the report cites them |
| Open items | Item, owner, date, first appeared in FR # | Carried until closed with the closing FR number |

The field report is evidence in pay application review (`csl-cost-change-control`): work in place claimed on the requisition that the field report does not show is a question, not a payment.

### 3.6 Quality, nonconformance, and punch lists

Open a nonconformance report (NCR) when installed work departs from the contract documents; the disposition (rework, repair, use-as-is with the A/E's written acceptance, reject and replace) is the A/E's, and CSL records it with the cost and schedule consequence. Run the punch in three passes: CM's own list; A/E's list; then the owner walk, attended by CSL, facilities, and the end user, whose items are the owner's list and are added, never negotiated off. A punch item has four states, and the counts by state are the weekly punch metric:

| State | Meaning | Who moves it | Evidence |
|---|---|---|---|
| Open | Identified on a walk, owner of the fix named | CSL or A/E | Item in the log with room, discipline, photo |
| CM reports complete | Contractor states the fix is done | CM | Dated line on the CM's list |
| CSL verified | CSL walked it and the fix meets the item as written | CSL | Verifier's initials and date; photo when the item was visual |
| Owner accepted | Facilities or end user accepted it on the owner walk | Owner | Signed walk sheet or minutes item |

Substantial completion is recommended only when the owner walk has happened, the life-safety and owner-critical items are at owner accepted, and the remaining items carry a dollar value the retainage covers (`aia-contracts-capital-projects` for the certificate and retainage mechanics; `csl-cost-change-control` for the withholding recommendation). "Punch complete" from the CM is a position; the verified and accepted counts are the fact.

### 3.7 Problematic-equipment watchlist (W77 WS-02.01, 08/06/26)

When a client asks which units are the problem, build the answer from the data, not the nominations. The WS-02.01 assessment (issued 08/06/26 in the ASM family) set the method:

1. Rank the full population by RPN from the FMEA edition on file, listing every unit; W77's was 90 air-handling, makeup-air, and return-air units, laid out by rooftop zone so a reader can find a unit on the roof.
2. Band the top of the ranking. The W77 watchlist carried two bands: Tier 1, the top-ranked units (MAU-01 at RPN 512; MAU-02 / AHU-18N at RPN 504; MAU-04 and RAH-03 completing the band, scores in the assessment table), and Tier 2, units flagged end-of-life by the FMEA (RAH-19, RAH-22, RAH-54, AHU-05N). The watchlist bands are the assessment's ranking; each row still carries its RAG tier with rule, and every RPN in the 400 to 699 band is AMBER (A1).
3. Build the failure-mode matrix: unit against failure mode (coil, fan and drive, damper and actuator, controls, casing and condensate, heat recovery), populated from the FMEA text and field observation.
4. Specify the corrective work-order query for the FM contractor in the assessment appendix: date range (trailing 24 months), the asset list, WO type corrective only, and problem code and cause code mandatory on every row, with WO number, open and close dates, remedy, labor hours, and parts. Without problem and cause codes the history cannot be joined to the failure-mode matrix.
5. Report the overlap between what people nominated and what the data ranked. On W77 the charter nominations and the FMEA top-ranked units had zero units in common, and the corrective WO history had never been supplied; both were reported as findings, the second as an open data gap (open confirm; AMBER (A5) once unanswered five business days), not filled with assumptions.

### 3.8 Assessment triage rule (W77 WS-02.02, 08/06/26)

Give every assessment a triage rule the client can apply before the next complaint arrives. WS-02.02 (`CSL-W77-ASM-WS02.02 Rev 0`) found that low delta-T was the common pathway behind the air-side complaints, arising from air binding, waterside fouling, 3-way mixing valves bypassing at part load, and branch velocities under 2 fps that let air and debris settle. The rule: record the coil delta-T, the chilled-water supply temperature at the coil, and the zone flow before assigning an air-side complaint to a workstream, because a complaint routed to the wrong workstream spends the owner's money on the wrong fix. Actions that need no CMMS data (valve stroke checks, air bleed of suspect coils, verifying 3-way valve position at part load, computing branch velocity from design flow) start immediately; actions that need the WO history wait on the data gap and say so. Engineering basis in `chilled-water-systems`.

### 3.9 Commissioning oversight

Commissioning (Cx) is how the owner learns the building does what the OPR says before the owner's staff inherit it. Oversee it in this order, recording each step in the Cx status block:

1. Review the Cx plan (ASHRAE Guideline 0 and Standard 202 structure) for scope: every system the OPR names, the OPR and BOD alignment, roles, schedule, and the acceptance criteria written against the OPR, not against the equipment nameplate.
2. Track pre-functional checklists (PFC) to completion by system before any functional test is scheduled; a functional test on an unchecked system is a wasted witness day.
3. Witness functional performance tests (FPT) on owner-critical systems; record pass, fail, or deferred with the script revision and the witness names. A failed FPT opens a Cx issue with a retest date.
4. Require integrated systems tests (IST) that exercise the sequences across systems (loss of normal power, smoke control, chiller failover, BMS alarms) with the owner's operators present.
5. Schedule seasonal and deferred testing in writing with dates and the retainage or warranty lever that keeps the contractor coming back.
6. Keep the Cx issues log reconciled with the punch list and the NCR log; an issue that appears in one and not the others is a record discrepancy.
7. Tie acceptance to the OPR criteria and, for process-critical facilities (semiconductor, life sciences), to production or tool readiness: utility qualification before tool hookup, cleanroom certification to the specified ISO 14644 class before first wafer or first batch, and for cGMP space the IQ/OQ record the quality unit will require. Cytiva Project Falcon (ISO-5 / ISO-7 / ISO-8 space, 2,050+ tons of cooling, 10 MW redundant power) is the CSL reference for that scale.

The Cx status block, in the shape it takes inside a weekly edition (illustrative values for a phased healthcare project; populate from the CxA's log at the pull):

| System | PFC complete | FPT witnessed / passed / failed | IST | Open issues (high / medium / low) | Deferred |
|---|---|---|---|---|---|
| AHU-2 and terminal units, Phase 2 | 41 of 41 | 6 / 5 / 1 (relief damper failed to close on loss of power; retest 11/19) | 11/24 with loss-of-normal-power scenario | 1 / 3 / 4 | Heating-season economizer test, 01/2027 |
| Medical gas, Phase 2 | 12 of 12 | Third-party verification 11/18 (NFPA 99) | Alarm panel to BMS 11/24 | 0 / 0 / 2 | None |
| BMS points and sequences, Phase 2 | 188 of 204 points verified | 3 / 3 / 0 | Included 11/24 | 0 / 2 / 6 | None |

Every FPT line names the script revision and the witnesses in the CxA's log; the block cites the log and its date. A system with PFCs incomplete inside two weeks of its FPT date is AMBER (A2) with the count of open checklists.

### 3.10 Turnover and closeout

A closeout package without data and drawings is not complete, and the standing client direction on W77 says so: turnover packages must carry data and drawings (the W77 engagement context file (`engagement-context-W77.md` in the W77 Claude Project), Section 5). Build the turnover package index from 75% complete (template: `templates/turnover-package-index.md`) so the contractor knows what is owed before the last pay application:

| Group | Contents | Spec anchor |
|---|---|---|
| Contract closeout | Certificate of substantial completion, final punch with owner acceptance, final change order, consent of surety, final lien waivers, warranty start dates | 01 77 00 |
| Record documents | As-builts (marked record set plus CAD/BIM), record specifications, approved submittals, RFI log, single-lines, P&IDs, panel schedules, controls drawings and points lists, sequences of operation, TAB report, test reports (pressure, megger, medical gas verification where applicable) | 01 78 39 |
| Operating documents | O&M manuals by system, warranties with start and end dates and contacts, training records and recordings, spare parts and attic stock with quantities and storage location, keys and access credentials | 01 78 23, 01 78 36, 01 79 00, 01 78 43 |
| Commissioning | Final Cx report, issues log at closure, seasonal test schedule, systems manual | 01 91 13 |
| Authorities | Certificate of occupancy or equivalent, AHJ sign-offs, permits closed | Per jurisdiction |
| Data | Asset list for the CMMS with nameplate data, location, functional code, parent/child, and PM plan; equipment planning final list; RDD final | `csl-asset-data-cmms` |

Name files per the client's convention when the package lands on the client's tenant (W77: Enterprise_Site_Building + project + discipline + document type, pattern `ASML_WLT_077_<project>_<discipline>_<doctype>_<yyyy-mm-dd>`), and keep the CSL document number inside the document (`csl-document-control`, Section 6). Recommend release of final payment only when every index line is Accepted or has a written waiver from the owner.

### 3.11 Equipment planning oversight

Equipment planning decides who buys, who installs, and when a room is ready, and it fails quietly when nobody owns the matrix. Keep one equipment list per project with, for every item: responsibility, disposition (new / existing / relocate / dispose), room, RDD status, vendor quote and date, move cost, utility requirements confirmed against the RDD, delivery and install dates against the schedule, and the open decision number if any. The responsibility matrix decides what CSL checks for each item:

| Responsibility | Who buys | Who installs | What CSL checks |
|---|---|---|---|
| OFOI (owner-furnished, owner-installed) | Owner | Owner or owner's vendor | Purchase order date against the lead time; room ready date (rough-in, power, data, medical gas or process utilities) on the CM's schedule; delivery access and permit window |
| OFCI (owner-furnished, contractor-installed) | Owner | CM | Vendor cut sheets in the CM's submittals; rough-in coordination in the RDD; receipt, storage, and damage responsibility written down before delivery |
| CFCI (contractor-furnished, contractor-installed) | CM | CM | Submittal against the RDD and the owner standard; substitution requests routed as changes |
| VFCI (vendor-furnished, contractor-installed) | Owner's vendor | CM | Vendor drawings against the RDD; utility connections by tag; who pays for rework when the vendor drawing changes after rough-in |

Disposition drives the cost question: an item marked relocate carries a move, rigging, and recertification cost; an item marked new carries a vendor quote and a disposal cost for what it replaces; either without a number is an open decision. Report the list as four tiles, the set used on the OSU Project Hub for the OSU Medical Center Expansion Wing: Equipment & Furniture Items (count by responsibility and disposition), Schedule Tasks Complete (of total), Room Data Drawing Complete (rooms of total), Open Equipment Decisions (count, oldest, and the lever on each). An RDD not complete for a room whose rough-in is inside the look-ahead is an AMBER (A2) finding with the room and the activity named.

### 3.12 Healthcare: ICRA, ILSM, and phased work in active clinical facilities

In an active clinical facility the project's health includes the Infection Control Risk Assessment (ICRA) status and violations, and CSL reports them beside cost and schedule. Confirm the ICRA class per the facility's matrix before mobilization, walk the barrier daily against the ICRA permit checklist (negative pressure, anteroom, HEPA exhaust, walk-off mats, debris routing), and log every deficiency with time, photo, correction, and who corrected it; repeated deficiencies are a contractor-accountability finding (3.15). Track Interim Life Safety Measures (ILSM) the same way: the assessment on file, the measures in effect, and the daily checks. Phase the work around the clinic, not the other way: CSL's Tufts Medical Center 4-Phase GI Endoscopy renovation kept an active clinic running through four phases, and the Tufts CPD Central Sterile renovation replaced sterilizers in a 24-hour facility in phases (`csl-projects`). Each phase turnover is its own owner walk, its own Cx closure, and its own punch; medical gas work has the third-party verification on the schedule before the phase turnover date.

### 3.13 Active manufacturing: cleanroom, tie-ins, and SIPP

In an operating fab or cGMP plant the constraint is production, and the owner's rep's job is to keep contractor work inside permitted windows. Confirm cleanroom protocol (gowning, materials, particle monitoring, vibration limits) is on the permit before entry; schedule utility tie-ins in windows agreed with operations and staged as shutdown packages; and require every task on the floor to carry a SIPP permit with its gates cleared before start. The permit method, gate model, perfect-week counting, and shutdown package are in `csl-permits-shutdowns`; the SIPP form and workflow are in the installed `sipp` skill. Work observed without a permit is RED (R6) whatever the schedule says.

### 3.14 AHJ and permitting support

Map the authorities before design is complete: local building, fire, and health; state plan review where the occupancy requires it; utility companies; and, in cleanroom and battery plants, the specialty fire suppression reviews. CSL provided permitting support with local and state authorities on the ErlingKlinger EV battery production facility in Easley, SC (`csl-projects`), and the method is the same everywhere: a permit matrix tracked on the look-ahead, with the AHJ's written comments logged like design review comments and closed by a named person. The matrix, in the shape it takes for a phased healthcare renovation (illustrative rows):

| Authority | Permit or review | Submitted | Review period | Inspection sequence | Needed for |
|---|---|---|---|---|---|
| State department of public health | Plan review, clinical occupancy | 06/15/26 | 60 days; approval on file 08/11/26 | Final licensure inspection before occupancy | Phase 2 occupancy |
| Local building department | Building permit, Phase 2 | 08/14/26 | Issued 08/28/26 | Framing, above-ceiling, final | Ceiling close-in 11/18; certificate of occupancy |
| Local fire department | ILSM acknowledgement; fire alarm modification | 09/02/26 | Issued 09/10/26 | Alarm acceptance test with the IST 11/24 | Phase 2 occupancy |
| Third-party medical gas verifier (NFPA 99) | Verification report | Scheduled 11/18/26 | Report within 5 days of test | After rough and final piping inspections | Phase 2 turnover |

An inspection date that is not on the CM's look-ahead is a finding; an inspection failed is an NCR with the AHJ's comments attached.

### 3.15 Contractor accountability

Accountability is response time made visible. Report days-in-court by party every week; the contractor, the A/E, and the owner each see their own number, and the owner's own late decisions are reported with the same arithmetic, because a log that only counts the contractor's days is not believed. Escalate on aging, not on tone:

| Aging | Step | Form | Skill |
|---|---|---|---|
| Past the response period | Item on the OAC prep with days-in-court; owner of the response named in the minutes | OAC prep; minutes action item | This skill; `csl-meeting-records` |
| Two response periods | Written notice citing the contract clause and the milestone at risk | Notice letter, drafted for the CSL signatory | `csl-client-comms`; `aia-contracts-capital-projects` |
| Three response periods, or a milestone lapsed | Schedule recovery plan requested; withholding recommendation on the next requisition where the contract allows | Memo with exposure in days and dollars | `csl-cost-change-control`; `csl-executive-memo` |
| Repeat pattern across items | Pattern reported as a record with dates and counts, not as character | Weekly report finding, AMBER (A6) or RED (R4) by the worst item | `csl-weekly-reporting` |

Record every contractor explanation as their position with the date. Never let the CM's log be the only log; the owner's numbers come from the owner's log, reconciled weekly.

---

## 4. Output specification

| Deliverable | Structure | Number and file name |
|---|---|---|
| OAC prep one-pager | Header line; bottom line in two sentences; seven blocks in the order of 3.2; docket; source note | Carries the OAC meeting number like minutes: `OAC #23 Prep`; file `CSL-<PROG>-OAC-023_prep_<yyyy-mm-dd>.pdf` |
| Weekly field report | Sections per 3.5; 2 to 4 pages; photos by log number | `FR #<nn>` series per project; file `CSL-<PROG>-FR-<nnn>_<yyyy-mm-dd>.pdf` |
| Log extract | Count header ("<n> open; <a> aged past response period; oldest <d> days with <party>"); table sorted by tier then age; source line | Inside the WKR edition or the OAC prep |
| Review recommendation | Item and revision; what it was reviewed against (OPR section, spec section, RDD); finding; recommendation in one of the four forms; conditions; CSL signatory | Logged against the item number |
| Cx status block | Systems in scope; PFC complete of total; FPTs witnessed / passed / failed; IST date and result; open issues by severity; deferred tests with dates | Inside the WKR or a `CSL-<PROG>-MEM-<yymmdd>` |
| Turnover package index | Groups per 3.10; one line per document with status Received / Reviewed / Accepted / Missing and date | `CSL-<PROG>-TOP-<yymmdd> Rev <n>`, controlled |
| Equipment decision log extract | Columns per `references/log-schemas.md` Section 4; four tiles | Inside the OAC prep; tiles per `csl-dashboard-kpi` |
| Watchlist / assessment | Ranked population, bands, failure-mode matrix, query spec, findings, triage rule | `CSL-<PROG>-ASM-WS<nn.nn> Rev <n>` via `csl-technical-docs` |

The `OAC`, `FR`, and `TOP` families are package conventions of this skill; add them to `csl-document-control` Section 1.1 when the numbering table is next revised. Rendering per `csl-brand`: navy table headers, status colors from Section 1.4 with the tier word present, source line under every table built from a pull.

---

## 5. Voice and formatting rules

- Item, tier with rule, exposure, owner, action, date, in that order, on every finding.
- Review outcomes use the four forms in 3.1 verbatim; the words "approved" and "accepted" belong to the A/E's action and the Owner's decision, never to CSL.
- Status is a party plus an action ("with A/E, Revise and Resubmit, 9 days"), never a bare "under review".
- Contractor and A/E explanations are recorded as their position with the date.
- Spec sections carry number and title on first use per page; drawings carry sheet number and revision.
- Client-executive editions: no dash constructions in running prose; spell out OAC, RFI, ICRA, and Cx on first use per page.
- Safety and ICRA lines describe conditions, locations, and corrections; no personal or health information about anyone.

---

## 6. Worked example: OAC prep one-pager, phased endoscopy renovation

Illustrative content in the shape of the Tufts Medical Center 4-Phase GI Endoscopy renovation type (active clinic, four phases); parties are role labels, the program code `GIE` is not an issued CSL code, and the figures are for shape and standard, not the Tufts record.

**OAC #23 Prep** | GI Endoscopy suite renovation, Phase 2 of 4 | OAC Thu 10/08/26 9:00 AM ET | Prepared by <operator>, CSL Consulting, for the Owner PM | Time zone ET

**Bottom line.** Phase 2 substantial completion holds at 12/04/26 only if the A/E answers RFI-087 (medical gas zone valve box location) by 10/12/26 and the Owner decides the procedure-room fixture color temperature (D-031) by 10/09/26. The ICRA Class IV barrier logged one deficiency this week, corrected the same hour; two PCOs totaling $20,570 are pending with CSL positions below.

| Look-ahead (weeks of 10/12 and 10/19) | Area | CM date | CSL check | Constraint |
|---|---|---|---|---|
| Medical gas rough-in and AHJ rough inspection | Procedure rooms 2 and 3 | 10/13 to 10/14 | Inspection booked 10/14; RFI-087 open | Zone valve box location |
| Above-ceiling electrical rough | Procedure rooms 2 and 3, corridor 2C | 10/12 to 10/16 | Electrical rough inspection 10/13 | None |
| Reprocessing room plumbing rough-in | Reprocessing 2R | 10/26 | Depends on D-032 (AER new vs relocate) | Owner decision |

| Open RFIs at or near the 10-business-day response period | Days open | Ball in court | Cost / schedule impact | Action |
|---|---|---|---|---|
| RFI-087: zone valve box on M-401 conflicts with casework elevation A-501 in procedure room 3 | 12 business days (opened 09/22/26; due 10/06) | A/E (12 of 15 calendar days) | Possible / Yes (gates 10/14 inspection) | A/E response by 10/12; CSL notice at 15 business days |
| RFI-091: ceiling height at pass-through window, reprocessing 2R | 8 business days (opened 09/28/26; due 10/12) | A/E | No / No | Answer with the 10/12 batch |

| Submittals pending owner decision | Spec section | Gates | Decision needed by |
|---|---|---|---|
| 26 51 13-04 procedure-room luminaires, 3500 K vs 4000 K per facility lighting standard | 26 51 13 Interior Lighting | Fixture release 10/12 (4-week lead), install week of 11/09 | 10/09 (D-031) |

| Change orders and PCOs pending | Amount | CSL position |
|---|---|---|
| PCO-014 abatement of floor mastic found 09/29/26 in the Phase 2 area | $18,420 | Recommend the Owner not accept as submitted; quantity exceeds the abatement survey by 340 SF; revised backup requested 10/06 |
| PCO-015 owner-requested data drop, procedure room 3 | $2,150 | Recommend acceptance; owner contingency draw |

| Safety, ICRA, ILSM, permits | Status |
|---|---|
| ICRA Class IV barrier, anteroom with HEPA negative air | Daily checklist 5 of 5 days; one deficiency 10/05/26 (anteroom door held open by cart), corrected within 10 minutes, logged with photo P2-118 |
| ILSM assessment 09/28/26 | Corridor 2C egress width reduced at the barrier; signage and daily check in effect; no fire watch required |
| AHJ | State plan approval on file; local electrical rough 10/13, plumbing and medical gas rough 10/14; third-party medical gas verification scheduled 11/18 |

| Decision log | Owner | Needed by | Milestone gated | Lever if late | Escalation at +5 business days |
|---|---|---|---|---|---|
| D-031 luminaire color temperature | Owner Facilities | 10/09 | Fixture release 10/12 | 1 day per day after 10/12; $1,800 expediting after 10/16 | Owner Facilities Director |
| D-032 AER units: relocate existing two or buy new | Owner Clinical Director | 10/16 | Reprocessing plumbing rough 10/26 | Rough-in slips day for day; new units quoted $46,900 vs move and recertification $6,200 | Owner PM sponsor |

**Docket.** A/E: RFI-087 and RFI-091 by 10/12. Owner Facilities: D-031 by 10/09. Owner Clinical: D-032 by 10/16. CM: PCO-014 revised backup by 10/09; barrier checklist continues daily. CSL: notice letter on RFI-087 if unanswered 10/13; owner walk for Phase 2 booked for the week of 11/30.

Source note: CM RFI and submittal logs exported 10/07/26 16:10 ET; CSL logs reconciled same day (0 count differences); ICRA log through 10/07/26; schedule data date 10/05/26.

What the owner learns from the page: two dated decisions and one A/E answer hold the phase date; the money items have positions; the barrier is being watched daily and the record shows it.

---

## 7. Failure modes and how to avoid them

| Failure | What it looks like | Avoidance |
|---|---|---|
| Reviewing for design intent instead of owner requirements | CSL comments debate the engineer's approach; owner requirement misses go unflagged | Four owner questions in 3.1; code and intent flagged to the A/E, not adjudicated |
| Accepting "under review" as a status | Log shows 40 items "under review" with no party and no days | Status is a party plus an action; days-in-court by party computed from the date history |
| Punch list without the owner walk | Substantial completion recommended off the CM's and A/E's lists | Owner walk with facilities and end user; owner's items added, not negotiated |
| Closeout without data | O&Ms delivered, no asset list, no single-lines, final payment released | Turnover index from 75% complete; data and drawings group; release only when Accepted or waived in writing |
| Decision log with no lever | Dates pass and nothing happens (OSU lesson) | Due date tied to a milestone; days and dollars if late; escalation column |
| Letting the CM own the RFI log narrative | The weekly report quotes the CM's counts and the CM's reasons | CSL log reconciled weekly; differences reported as AMBER (A6); reasons recorded as the CM's position |
| RFIs carrying scope | New work rides an RFI answer with no change number | Cost or schedule impact opens a PCO the same day (csl-operating-rules, Section 8) |
| Cx tested against nameplate, not OPR | Every FPT passes and the owner's operators cannot run the sequence | Acceptance criteria written against the OPR; IST with operators present |
| Watchlist from nominations | The problem units are the ones people mention | Rank the full population by RPN; report nomination overlap; query the WO history with codes mandatory |
| ICRA treated as the CM's paperwork | Deficiencies found by the facility, not by CSL | Daily barrier walk on the checklist; deficiencies logged and reported in project health |

---

## 8. Pre-issue checklist

- Every finding carries item, tier with rule, exposure, owner, action, date.
- Every review outcome uses one of the four forms in 3.1; no "approved by CSL" anywhere.
- Every open log item shows a party and days-in-court; aging computed in code from the date history.
- CSL log reconciled with the CM log this week; differences listed.
- Every decision row has due date, milestone, days and dollars if late, escalation column.
- Field report sections complete; photos by log number; work in place tied to activity IDs.
- Cx acceptance criteria traced to OPR sections; issues log reconciled with punch and NCR logs.
- Turnover index includes the data and drawings group; file names per client convention.
- Spec sections by MasterFormat 2018 number and title; drawings by sheet and revision.
- Escalation triggers from csl-operating-rules Section 6 checked (R6 for work without a permit; R8 for irreversible steps on unconfirmed records).
- Brand QA run (`csl-brand/references/brand-qa-checklist.md`); number and file name per `csl-document-control`.

---

## Files in this skill

- `references/log-schemas.md` — columns and status vocabularies for the submittal, RFI, design review comment, decision, NCR, punch, and Cx issues logs, with aging and days-in-court rules.
- `templates/field-report.md` — weekly field report skeleton in the FR #16 shape, one populated example row per table.
- `templates/oac-prep.md` — the OAC prep one-pager skeleton with the seven blocks and docket.
- `templates/turnover-package-index.md` — turnover package index by group with status per line and the client naming pattern.

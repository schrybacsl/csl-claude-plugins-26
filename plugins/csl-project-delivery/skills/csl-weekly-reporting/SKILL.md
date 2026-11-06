---
name: csl-weekly-reporting
description: >
  CSL's recurring weekly report family for an owner's-rep engagement: Monday One-Week Look-Ahead
  (WKR-nnA), Wednesday Mid-Week Executive Update (WKR-nnB), Friday End-of-Week Executive Report
  (WKR-nnC), supplements (WKR-nnD), and the Friday program-activity one-pager, with page maps, KPI
  set, data pulls, numbering, voice, and QA. Use it whenever someone asks for the look-ahead, the
  mid-week, the EOW, "this week's report", "the Friday report", a weekly executive status, a reissue
  of an edition, a new weekly series for another program, or the headline for a week.
---

# CSL Weekly Report Family (WKR series)

The weekly editions are the client executive's primary window into the program and the program's most-read record. They are built from live tracker pulls, not from memory, and they say plainly what moved, what did not, what is red, and what happens next. The W77 series (CSL-W77-WKR-nnA/B/C) is the reference implementation; the method transfers to any engagement by swapping the sheet registry and the KPI set.

---

## 1. Bottom line

Three editions a week, each a branded PDF from the report factory, each answering the executive's questions in the first content page: what is the state of the program, what changed since the last edition, what is red and why, what CSL needs decided. Every number is traceable to a pull with a timestamp. Every red carries its rule ID. Every edition ends with a docket.

| Edition | Day | Pages | Question it answers |
|---|---|---|---|
| WKR-nnA One-Week Look-Ahead | Monday (from Sunday pulls) | 10 | What is committed this week, on what anchors, with what risks |
| WKR-nnB Mid-Week Executive Update | Wednesday | 5 | Is the week holding; what needs a decision before Friday |
| WKR-nnC End-of-Week Executive Report | Friday | 8 to 11 | What happened, what moved, what is red, what carries over |
| WKR-nnD Supplement | As needed | 5 to 8 | A deep dive the C edition could not carry (insights, drill-down) |
| Program activity one-pager | Friday | 1 | Single-page activity summary for a specific program thread (W77: Planon) |

`nn` is the ISO week number (`csl-document-control`). Reissues carry `R1`.

---

## 2. Inputs and pulls

Pull every sheet the edition depends on, in the same session, and record the pull block. For W77:

| Sheet | ID | Feeds |
|---|---|---|
| Roadmap | 1390098374414212 (report pull) / 1059284113641348 (master) | Roadmap section: rows moved, frozen weeks, RPN watchlist, health |
| CSL Tasks | 7673437876080516 | CSL action board: Reds, anchors, closures, byte-identity |
| SIPP Permits | 289677048237956 | Permit board: started, gated, closed, new, flags |
| ST CHW/PCW Mitigation | 2158727850315652 | Mitigation: open, past-target, closures, owner load, WS-22 pipeline |
| CTRW telemetry (weekly zip) | file | Rig states when the zip has arrived |

Run `csl-data-pipeline` scripts: `smartsheet_pull.py` per sheet, `freeze_check.py`, `diff_pulls.py` against the previous edition's snapshot, `qa_rules.py`. The diff output is the raw material for "what moved". Keep the pull snapshots beside the PDF.

Other inputs: the previous edition (to compare every KPI), the week's meeting minutes and any counterpart recaps (for discrepancies), issued notices and memos (to cite by number), the operator's inputs for the week (given as a short list; e.g., WKR-36A took five inputs including a blocked PO and a ticket number).

Pull block (goes on the last page and in the delivery note):

```
Pulled 09/18/26 06:42 ET: Roadmap 1390098374414212 (239 rows, md5 unchanged since 08/14 pull, frozen 6th week);
CSL Tasks 7673437876080516 (74 rows); SIPP Permits 289677048237956 (58 rows); Mitigation 2158727850315652 (188 rows).
```

---

## 3. Method

1. **Frame the edition.** Confirm the week number and window (`date -d <monday> +%V`). Identify the audience and cover block from the engagement context file, Section 5 (W77 reference: prepared by the CSL owner's rep for the client executive sponsor, with the standing distribution list); the preparer is the operator running the session. Check the previous edition's docket: every item on it must be dispositioned in this one.
2. **Pull and QA.** Section 2. Any pull failure is stated on the page it affects as "not available at [pull time], source [name]" rather than filled from memory.
3. **Compute the KPI set.** Section 4.4. Compare each to the previous edition; write a one-line cause for each that moved and flag each that has not moved for two editions.
4. **Tier the findings.** Apply `csl-schedule-risk` tier rules; every red and amber carries its rule ID. Check the ten escalation triggers in `csl-operating-rules` against this week's data before writing a word of narrative.
5. **Write the headline.** One paragraph, page 2, the whole week in five sentences: the biggest change, the streak or the freeze, the red that matters most, the decision needed, the date it is needed by. Write it last but place it first.
6. **Build the sections** per the page map for the edition (Section 4). Tables from the diff and KPI outputs; charts from the chart library; prose only where reasoning is needed.
7. **Write the docket.** Every open item with owner, due date, tier. Carry items from the previous docket with their age. A docket item older than three editions gets a sentence explaining why.
8. **Render** with the report factory (`csl-data-pipeline`, family config `WKR`), file per `csl-document-control`, run the brand QA (`csl-brand`), and open the PDF to read it as the executive will.
9. **Deliver** with the document number, a two-sentence summary, and the single next action. Attach to the tracker row when the program does that.

---

## 4. Output specification

### 4.1 WKR-nnA One-Week Look-Ahead (Monday, 10 pages)

| Page | Content |
|---|---|
| 1 | Cover (royal-blue engagement cover from WKR-40A on for W77; navy default elsewhere) |
| 2 | Bottom line for the week; KPI strip (6 cards); the commitment statement: anchor rows this week is built around, with their tracker END dates and any verbally framed outer date stated separately |
| 3 | Look-ahead table: day by day, what starts, what closes, who owns it, permit and gate status, tier |
| 4 | Permit board look-ahead: permits starting this week and gate progress (3/5 style), windows, walkthroughs, new permits next 30 days, date-quality flags |
| 5 | Roadmap: rows due this week, rows due that did not move last week, frozen-tracker statement if applicable, RPN watchlist changes |
| 6 | Mitigation workstreams: rows targeted this week, past-target count and trend, owner load, WS-22 pipeline steps due |
| 7 | CSL action board: Reds and anchors, what closes this week |
| 8 | Program thread page (W77: Planon deliveries, gates open, confirms due; other engagements: the dominant workstream) |
| 9 | Risks and red flags for the week, in a plain narrative register (the operator's direction: casual-toned red-flag narratives with charts and visual aids), each with the rule ID and the action |
| 10 | Docket, source note, as-of statement |

The A edition is a plan, so its verbs are future and conditional: "closes Wednesday if the PDS is approved Monday." Where a stakeholder has named a date verbally that differs from the tracker (a ~09/15 outer frame against an 08/28 row END), show both and say which one the docket is built to.

### 4.2 WKR-nnB Mid-Week Executive Update (Wednesday, 5 pages)

Standing since 07/29/26 (ten weeks running through WKR-40B); replaced the three-slide PPTX; white background with charts; official CSL palette from 39B; plain human voice.

| Page | Content |
|---|---|
| 1 | Cover per the engagement look; cover block "Prepared by <operator> for <client recipient>" from the engagement context file; distribution line; no sources note on the cover (09/01/26 direction) |
| 2 | Executive summary: bottom line paragraph; KPI strip; "since Monday" table (what moved in two days, what did not) |
| 3 | Critical path and risk: the week's anchors with mid-week status; RED list with rule IDs; decisions needed before Friday with owner and time |
| 4 | Visual page: two or three charts (mitigation past-target trend; permit gates; rig state or the week's featured thread), each titled with the finding and stamped with its source |
| 5 | Featured item (rev 2 practice: mitigation, reviews, rig visuals, or a project intake such as IN 12896), then docket and source note |

If a deck is requested instead of the PDF, the standard is three slides (cover; KPI strip + executive summary; critical path + risk) built with `pptx_theme.py`; the KPI set is the same.

### 4.3 WKR-nnC End-of-Week Executive Report (Friday, 8 to 11 pages)

C-series standard since WKR-38C (09/18/26): official palette, plain voice, all four live sheets.

| Page | Content |
|---|---|
| 1 | Cover |
| 2 | Headline paragraph; KPI strip; "what moved this week" summary table (from the diff) |
| 3 | Permit board: started (gated y/n), closed with duration, walkthroughs, windows, new permits next month with gate progress, flags (inverted dates), work-done-no-record reconciliation, perfect-week streak |
| 4 | Roadmap: rows changed, frozen-weeks statement with the rows that should have moved, RPN watchlist (≥ 700 highlighted; report count of consecutive weeks each has appeared), health distribution, quarter-close notes |
| 5 | Mitigation workstreams: open rows, past-target trend (e.g., 15 to 17), closures this week (zero closures is a headline fact), owner load (e.g., 10 of 20 open on one owner), WS-22 pipeline with steps-complete-of-10 and committed $ vs planning budget, data defects |
| 6 | CSL action board: Reds untouched (count and age), anchors closed, byte-identity statement, prior Friday's open rows dispositioned |
| 7 | Program thread (W77: Planon deliveries, meeting outcomes with minute numbers, gates, confirms, deadline countdown to 10/30/26) |
| 8 | Engineering and telemetry: rig states (RED/AMBER/GREEN with the signature), notices issued (FM-…), escalations and their current disposition |
| 9 | New requests and decisions this week (e.g., a client request for a merged tracker proposal; a dashboard scoping call held) with the CSL response and date owed |
| 10 | Risks and red flags narrative; next week's frame (hands off to the A edition) |
| 11 | Docket; consolidated source note; as-of statement |

Pages 8 and 9 collapse into one when the week is quiet; the page count follows the content, not the other way around.

### 4.4 The KPI set (W77 reference; swap per engagement)

| KPI | Definition | Source | Shown as |
|---|---|---|---|
| Permits gated in time | permits started this week with all gates cleared before start / permits started | SIPP | n/n and streak of perfect weeks |
| Permits closed | count, with duration in days for tie-ins and long permits | SIPP | count, longest duration |
| Roadmap rows moved | rows with any cell change since last pull | Roadmap diff | count; "frozen n weeks" when zero |
| RPN ≥ 700 without mitigation | rows at or above threshold with no owner/dated action | Roadmap | count, weeks reported |
| Mitigation past target | rows past target date, open | Mitigation | count and delta (15 → 17) |
| Mitigation closures | rows closed this week | Mitigation | count (zero is reported as zero) |
| Owner load | open rows on the single most-loaded owner | Mitigation | n of N |
| CSL Reds | red rows on the action board and their age | CSL Tasks | count, oldest age |
| Program deliveries | records delivered to date by file, convention built to | Asset program register | count and date |
| Gates and confirms open | G-nn gates open; open confirms > 5 business days | PLN register | counts |
| Rig state | TR7/TR2/TR5 tier with signature (runway days, dark days) | CTRW | three tiers |
| Days to hard deadline | to 10/30/26 (Loops + AHS) and to the next quarter close | calendar | days |

Full definitions and thresholds: `csl-dashboard-kpi/references/kpi-catalog.md`.

---

## 5. Voice and formatting

- Plain human voice for the B and C editions: short declarative sentences, active verbs, no dash constructions in running prose, acronyms spelled out on first use per page, no engineering shorthand a client executive would have to decode. A reader who is not an engineer must be able to follow every page.
- The A edition may be more conversational in its red-flag narratives (the operator asked for casual-toned red-flag narratives with visual aids); precision does not drop.
- Numbers with units and denominators; deltas against the previous edition in parentheses; dates with weekdays inside the window ("closed Fri 09/18 at 46 days").
- Attribute positions: "the client data owner stated on the call", "the FM contractor reports"; never adopt a counterpart's explanation as fact.
- Name documents by number (Minutes #020, FM-W77-UTM-0903 R2, IN 12896) so the reader can find them.
- Tables for permits, moved rows, watchlists, docket; charts for trends; prose for the headline, the reasoning behind a tier, and the risk narrative.
- One featured visual per page at most in the B edition; the C edition may carry two on the visual-heavy pages.
- Brand per `csl-brand`; cover block and distribution exactly as directed for the engagement; official palette; report factory renders.

Headline sentence forms that work:

- "The permit board held its fourth perfect week; the roadmap did not move for the sixth."
- "Mitigation closed 43 rows this week after three weeks with none; 17 remain past target, 9 of them on one owner."
- "CSL delivered the mechanical upload sheet Wednesday 3:22 PM, inside the 48-hour commitment; the import failed on the client side on 09/01 and the stated cause arrived 09/29."
- "One decision is needed before Friday: whether QR label printing waits for the written code confirmation. CSL recommends it waits."

---

## 6. Worked example (WKR-38C, week of 09/14 to 09/18/26, headline and KPI strip)

**Headline.** The site ran a fourth consecutive perfect permit week. The crane permit for the CRS work started Wednesday fully gated, the tie-in permit closed Thursday at 46 days, and the wall opening was gated in time for Saturday's three-machine delivery. Two October permits opened with their dates inverted and need correcting before they are worked. The roadmap has not changed in six weekly pulls while field milestones moved, so its schedule dates cannot be relied on this week; the RPN 1000 electrical item appears for the ninth week without a dated mitigation. Mitigation posted zero closures and past-target rows rose from 15 to 17, ten of the twenty open rows on the program lead. The Planon weekly on Tuesday re-baselined the September 15 frame in writing against the functional-code change; a versioned spec is still owed. The client asked CSL for a proposal to merge the 2024 building condition assessment with the roadmap into one maintained source; CSL built a 348-record proof of concept Thursday and owes the level-of-effort proposal next week.

**KPI strip.** Permits gated 5/5 (streak 4) GREEN · Roadmap rows moved 0 (frozen 6 wks) RED (R5) · RPN ≥ 700 without mitigation 1 (9 wks) RED (R1) · Mitigation past target 17 (+2) AMBER (A2) · Closures 0 (3rd week) AMBER · Days to 10/30 hard deadline 42.

**Docket (excerpt).** Versioned 8-level code spec, client data owner, due before recode (open since 09/10) RED (R8 if tagging proceeds) · Inverted dates on 54164 and 54157, permit coordinator, 09/22 · LOE proposal for BCA+IRO merge, S. Schryba, 09/25 · Roadmap refresh request, tracker owner, 09/22 (open 6 weeks).

---

## 7. Failure modes

- Carrying a KPI from last week because the pull failed. State "not available" and why.
- Reporting a frozen sheet as a quiet field. The freeze is the finding; name the rows that should have moved.
- Letting the docket forget. Every prior docket item is dispositioned or carried with age.
- Softening a zero. "Zero closures for the third week" is the sentence; "closures were limited" is not.
- Writing the headline first from expectation and fitting data to it. Compute, tier, then write.
- Editorial adjectives about counterparts. Dates, documents, and record discrepancies only.
- A cover block that drifts from the standing direction (wrong "prepared for", missing distribution, a sources note the direction removed).
- Reissuing without `R1` and without stating what changed.
- Dash constructions and shorthand creeping back into the B/C prose.

---

## 8. Pre-issue checklist

- Week number verified with `date`; window on the cover matches.
- Pull block complete: every sheet, ID, timestamp, row count, md5 status.
- Every KPI compared to the previous edition; causes written for movers; two-edition freezes flagged.
- Every RED/AMBER carries a rule ID; ten escalation triggers checked.
- Previous docket fully dispositioned; new docket has owner, date, tier for every row.
- Headline is five sentences or fewer and matches the body.
- Voice rules (no dash constructions, acronyms spelled, positions attributed) applied to B/C prose.
- Cover block and distribution per the engagement's standing direction.
- Brand QA passed (`csl-brand/references/brand-qa-checklist.md`); fonts verified in the PDF.
- Numbered and named per `csl-document-control`; snapshot saved beside the PDF; transmittal drafted.

## Files in this skill

- `references/page-maps.md` — the three page maps with per-page data contracts and chart assignments.
- `references/kpi-set-w77.md` — the W77 KPI set with formulas, thresholds, and the sheet columns each reads.
- `templates/look-ahead.md` — WKR-A skeleton with one populated row per table.
- `templates/mid-week.md` — WKR-B skeleton.
- `templates/end-of-week.md` — WKR-C skeleton.
- `templates/program-activity-onepager.md` — the Friday single-page program thread summary.

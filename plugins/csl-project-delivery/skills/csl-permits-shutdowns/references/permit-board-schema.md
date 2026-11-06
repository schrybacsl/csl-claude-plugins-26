# Permit Board Pull Schema

The columns CSL reads from a permit board (W77: SIPP Permits, Smartsheet 289677048237956), the derived fields computed after the QA pass, the QA rules with their tiers, and the status mapping used for reporting. The board's own column names and picklists govern at pull time; map them to these names in the pull script rather than renaming anything on the client's sheet. The SIPP form fields behind these columns are in the installed `sipp` skill (Part 3); the Smartsheet master tracker structure is in its Part 7.

## 1. Source columns

| # | Column | Type | Rule |
|---|---|---|---|
| 1 | Permit number | Text | The board's own number (W77 site numbers such as `53782`; generic SIPP `200-0142`); never renumbered; duplicates flagged |
| 2 | Start date (and time where the board carries it) | Date | Required; a past start with no gate timestamps is tested as an ungated start |
| 3 | Finish date | Date | Required on Closed rows; must not precede start |
| 4 | Location / room | Text | Building, floor, room, roof zone, or grid; blank is a defect on submitted or later rows |
| 5 | Workflow status | Picklist | Board's own values; mapped per Section 4 |
| 6 | Type of work | Picklist | Hot work, LOTO, confined space, crane lift, wall opening, utility tie-in, roof work, radio/BDA, pump replacement, shutdown, other (`sipp` Part 2 categories map onto these) |
| 7 | Description | Text | The step-by-step task list summarized to one line for reporting |
| 8 | Contractor | Text | Legal entity; blank is a defect |
| 9 | PM reviewed | Yes/No with date | The CSL or owner PM approval gate; date required when Yes |
| 10 | Hazards | Multi-select | Identified hazards; each one implies a control gate |
| 11 | Controls | Multi-select or text | One control per hazard; a hazard without a control is an open gate |
| 12 | Isolation | Text or attachment | LOTO points, lock numbers, verification timestamp |
| 13 | Gas measurements | Text or attachment | Readings, instrument, time, tester; required for confined space and enclosed hot work |
| 14 | PPE | Multi-select | Per the `sipp` PPE matrix |
| 15 | Related JSA | Attachment or reference | Crew-signed; date |
| 16 | Approvals per role | Picklist and date per role | System owner, PM, EH&S, manufacturing/operations (`sipp` Part 4) |
| 17 | Alignment meeting | Date | The meeting at which the permit was reviewed before start |
| 18 | Window schedule | Text | For multi-window permits: window k of n with dates |
| 19 | Closeout documentation | Yes/No | Required for Closed status |
| 20 | Production impact | Yes/No and detail | From the form; drives the operations approval |

## 2. Derived fields (computed in code after QA)

| Field | Formula | Notes |
|---|---|---|
| Gates declared | Count of approval roles + hazards + isolation (if any) + gas measurement (if required) + PPE + JSA + alignment meeting | The permit's N |
| Gates cleared | Count of those with a timestamp | A cleared mark with no timestamp counts as open |
| Gate progress | Cleared / declared, shown as `k/N` | |
| Gated in time | True when every gate timestamp precedes the start date and time | The perfect-week input |
| Days open | Pull date − start date, for started rows not Closed | |
| Days to start | Start date − pull date, for future rows | New-for-the-coming-month block |
| Duration at close | Finish − start, Closed rows, excluding rows with a date-order flag | 30-day KPI (`sipp` Part 8) |
| Windows executed | From the window schedule | Reported as window k of n |
| Field witness | Start or finish inside the current pull window | Frozen-tracker test (`csl-schedule-risk` 3.6) |
| Perfect week | All started rows in the week gated in time AND no RED (R6) item in the week | Package convention (`SKILL.md` 3.2) |
| Streak | Consecutive perfect weeks through the current Friday, recomputed from the snapshots | Never carried forward |

## 3. QA rules

| Rule | Test | Tier (rule) | Action |
|---|---|---|---|
| Date order | Finish < start | AMBER (A6) | Quote both dates as found; correction requested same day; excluded from duration statistics; gate progress still reported |
| Status versus dates | Closed with blank finish; Approved or Active with past start and no gate timestamps; Submitted with past start | AMBER (A6) | Row named; ungated-start test applied |
| Missing contractor | Blank contractor on Submitted or later | AMBER (A6) | Row listed; attribution withheld |
| Duplicate numbers | Same number on two or more rows | AMBER (A6) | Both listed; coordinator states the record |
| Missing location | Blank location on Submitted or later | AMBER (A6) | Row listed |
| Aged open | Days open > 30 with no window schedule or closeout entry | Listed | Reason the record gives; multi-window permits state remaining windows |
| Ungated start | Started row with any gate timestamp after start, or missing | Breaks the perfect week | Named in the headline with the gate |
| Work done, no record | Field activity with no matching row | RED (R6) | Same-day notice; backfill reported when it happens |
| Sheet unchanged | Hash identical to last Friday while field reports show permitted work | AMBER (A4); RED (R5) at two pulls | Attributed to the board, not the field |

## 4. Status mapping for reporting

Read the board's picklist at pull time and map it; report the mapped value with the board's value in parentheses when they differ.

| Reported status | Typical board values | Counted in |
|---|---|---|
| Draft | Draft, Not submitted | Nothing |
| Submitted | Submitted, Pending approvals, More information requested | New-for-the-coming-month when start is within 31 days |
| Approved | Approved, Fully approved, Approved with conditions | New-for-the-coming-month; started when start date is reached |
| Active | Active, In progress, Started | Started this week when start is in the week; aged-open when > 30 days |
| On hold | On hold, Suspended | Listed with the reason |
| Closed | Closed, Complete, Closed out | Closed this week when finish is in the week |
| Cancelled | Cancelled, Void, Declined and withdrawn | Excluded from counts; listed if it had started |

## 5. Snapshot file

Save the pull as `SIPP-Permits_<yyyy-mm-dd>_<HHMM>ET.csv` with the source columns, the derived fields, the QA flags per row, and a header block (sheet name, ID, pull timestamp, row count, hash, previous hash, changed yes/no) beside the report it fed (`csl-document-control` Section 8). The weekly section's every number traces to this file.

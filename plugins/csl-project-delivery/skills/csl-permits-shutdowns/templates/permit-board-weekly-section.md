# Permit Board Weekly Section (inside CSL-<PROG>-WKR-<ww>C)

Skeleton for the Friday permit board section, in the eight-block order of `csl-permits-shutdowns` 3.4. Populate from this Friday's pull only; recompute the streak from the snapshots. One populated example row per table; example values are from the W77 record at the 09/18/26 pull (SIPP Permits 289677048237956) and are not reused without a fresh pull. Variables in `<angle brackets>` change every issue. Tier cells use the status colors of `csl-brand` 1.4 with the tier word and rule present. Plain voice for the C edition: no dash constructions; spell out SIPP, LOTO, BDA, and JSA on first use per page.

---

**Permit board** | Week Mon <MM/DD/YY> to Fri <MM/DD/YY> | Pull <MM/DD/YY HH:MM ET> | Sheet <name>, ID <id> | Time zone ET

## Headline

One or two sentences: perfect week yes or no; streak; counts of started, closed, new, flagged, and work with no record. Cross-reference the roadmap section when permits moved while a tracker did not.

> Perfect week: yes; fourth consecutive perfect week through 09/18/26. One permit started fully gated, one closed, one new permit for October flagged for inverted dates, no work reported without a record.

## 1. Permits started this week

| Permit | Description and type of work | Contractor | Start | Gate progress at start | Gated in time |
|---|---|---|---|---|---|
| 53782 | Crane lift | <per the board> | Wed 09/16/26 | All gates cleared before start | Yes |

Any No names the gate and its clearance time relative to start, and breaks the perfect week.

## 2. Permits closed this week

| Permit | Description and type of work | Opened | Closed | Duration | Windows executed of total | Closeout record |
|---|---|---|---|---|---|---|
| 51718 | Utility tie-in | 08/03/26 | Fri 09/18/26 | 46 days (tie-in sequence; above the 30-day KPI, reason stated) | As the permit's window schedule states | Complete; gates complete |

## 3. Walkthroughs held

| Date | Permits covered | Attendees by role | Outcome |
|---|---|---|---|
| <MM/DD/YY> | <numbers> | CSL PM, facilities, EH&S, operations, <contractor> | <conflicts found and resolved; permits cleared to start> |

Source is the alignment meeting log, not the permit sheet. When the log was not part of the pull: "not available at <pull time>, source alignment meeting log".

## 4. Windows executed

| Permit | Window | Date | Outcome | Remaining windows and dates |
|---|---|---|---|---|
| <number> | Window 2 of <n> | <MM/DD/YY> | Executed; restoration verified | Windows 3 to <n>, <dates> |

## 5. New permits opened for the coming month

| Permit | Description and type of work | Start / End as entered | Days to start | Gate progress | Approvals outstanding by role |
|---|---|---|---|---|---|
| 54164 | REMA pump | START 10/12/26, END 10/09/26 | 24 | 3/5 | Named from the board at the pull |

## 6. Data-quality flags

| Permit | Flag | As found | Tier (rule) | Correction requested | Status |
|---|---|---|---|---|---|
| 54164 | Date order | START 10/12/26 after END 10/09/26 | AMBER (A6) | 09/18/26, permit coordinator | Open; gate progress still reported |

## 7. Work reported with no record

| What | Where | When | Reported by (source) | Permit search performed | Tier (rule) | Backfill status |
|---|---|---|---|---|---|---|
| None this week | | | Field reports and contractor dailies 09/14 to 09/18 matched to permit rows | Board, 09/14 to 09/18, all contractors | | |

When there is an item: RED (R6) the same day; notice issued; backfill reported with the permit number and date when it happens; the week it broke stays broken.

## 8. Source note

> SIPP Permits <ID> pulled <MM/DD/YY HH:MM ET>, <n> rows, hash <changed / identical> from <MM/DD/YY>; alignment meeting log <dates or "not in the pull">; window schedules from permits <numbers>; field reports FR #<nn>; contractor dailies <dates>.

---

Pre-issue: every permit by the board's number; gate counts as cleared of total; gated in time tested against timestamps; streak recomputed; every flag with rule, tier, and correction date; every R6 item with the search performed; metrics the pull did not carry written as "not available at <pull time>, source <name>"; brand QA per `csl-brand`; number and file name per `csl-document-control`.

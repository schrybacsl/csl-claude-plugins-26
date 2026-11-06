# Risk Register Schema

One register per program, maintained by CSL as owner's representative, reviewed every Friday before the End-of-Week report. The register turns an RPN score into something the owner can act on: an owner, a dated action, and a quantified exposure. Rows in the client's own trackers (the W77 Roadmap Master, the BR+A FMEA, the mitigation sheet) are sources; the register cites them and never edits them.

## 1. Fields

| # | Field | Type | Rule |
|---|---|---|---|
| 1 | Risk ID | `RSK-<PROG>-<nnn>` | Sequential, never reused; retired rows keep their ID |
| 2 | Title | Text, under 80 characters | Names the failure, not the asset alone ("18-inch CHW main wall loss below tolerance", not "CHW piping") |
| 3 | System / WS | Picklist + text | E-GRP or taxonomy per the roadmap; WS number when a mitigation row exists |
| 4 | Source row | Text | Sheet name, ID, row name or WS ID the risk is read from |
| 5 | SEV | 1–10 | From the source; anchors in `SKILL.md` 3.2 |
| 6 | Occ | 1–10 | From the source |
| 7 | Det | 1–10 | From the source |
| 8 | RPN-B | Integer | Baseline score from the FMEA edition on file; never recomputed by CSL |
| 9 | RPN C | Integer | Current score; checked as SEV x Occ x Det; a mismatch is logged under field 22 |
| 10 | RPN change reason | Text | Required whenever RPN C differs from the previous review; the factor that moved and the document that justified it |
| 11 | Tier | RED / AMBER / GREEN | Per `references/tier-rules.md` |
| 12 | Rule | R1–R9, A1–A6, G | The rule that produced the tier; never blank |
| 13 | Trigger / leading indicator | Text | The observable that says the risk is materializing (zero-flow reading, past-target date, second frozen pull, CAAR not on the tollgate tracker) |
| 14 | Exposure ($) | Currency | Committed or at-risk dollars with the source (budget line, PO, quote); "not quantified" is allowed only with the reason |
| 15 | Exposure (days) | Integer | Schedule days at risk against the baseline named in field 16 |
| 16 | Baseline referenced | Text | Which baseline the days are measured against, with its date and minutes number |
| 17 | Exposure (records / assets / gates) | Integer + unit | Records to recode, assets untagged, permit gates open |
| 18 | Owner | Name, organization | One person; a team is not an owner |
| 19 | Mitigation action | Text | The next physical or documentary step, not a goal |
| 20 | Action date | MM/DD/YY | The date the action is due; blank means "no active mitigation" |
| 21 | Status | Open / Mitigating / Monitoring / Closed / Retired | Closed requires the closing document in field 24 |
| 22 | Data defects | Text | Anything that stops the row rolling up (ID format, blank baseline, arithmetic mismatch) |
| 23 | Last review | MM/DD/YY | Set on every Friday touch; rows past 14 days are flagged in the header |
| 24 | Source document | Text | FMEA edition, notice number, minutes number, transmittal, telemetry summary number |
| 25 | History | Append-only log | `MM/DD/YY: <what changed>` lines; nothing is overwritten |

## 2. Example rows

Populated from the W77 program record as of the 09/18/26 pull; exposure figures cite their sources. Live pulls are required before any reuse.

| Risk ID | Title | System / WS | RPN-B | RPN C | Tier (rule) | Trigger / leading indicator | Exposure | Owner | Mitigation action, date | Status | Last review | Source document |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RSK-W77-001 | Electrical distribution MV and LV failure with no mitigation plan on the roadmap row | Electrical / roadmap parent row "Electrical Distribution MV & LV" | 1,000 | 1,000 | RED (R1) | Row unchanged nine consecutive weekly pulls; no owner, action, or date | $ per roadmap budget line (pull required); site-wide outage severity per FMEA | B. Gannon (ASML CRE) | Mitigation owner and dated action requested in writing 09/18/26; response by 09/22/26 | Open | 09/18/26 | Roadmap Master 1059284113641348, 09/18/26 pull; BR+A FMEA edition on file |
| RSK-W77-002 | CHW carbon-steel piping wall loss below manufacturer lower tolerance | Mech Piping / CHW mains | Per FMEA | Per FMEA | AMBER (A3), held per client de-escalation direction | MTI UT report S-1000 (07/17/26): 11 of 15 carbon-steel locations below lower tolerance; 18-inch mains 36 to 37% below nominal if schedule 40 is confirmed | Days: rides the IRO strategy to REDM 10/01/26; $: not quantified until PDS; open data gap on pipe schedule | D. Wolf (CSL) with J. Vigo / E. Koning (ASML) | PDS first per client direction; schedule confirmation requested; review at REDM 10/01/26 | Monitoring | 09/18/26 | FM-W77-UTM-0903 R1 / R2 (09/03/26); MTI S-1000 |
| RSK-W77-003 | Functional-code structure change forces recode of delivered upload records before relabel | Planon migration / WS-n/a | n/a | n/a | AMBER (A5) | Versioned spec requested in writing 09/10/26; depth ruled verbally three ways since 08/24/26 | Records: ~1,480 to recode; days: measured against the 09/15/26 re-baseline (Minutes #019); $: relabel rework if printed early | T. Dube (spec); S. Schryba (recode) | Versioned spec and written delta review before any QR print; #020 follow-up | Mitigating | 09/18/26 | Minutes #019 (09/15/26); Functional Code Structure v1.1 |
| RSK-W77-004 | QR labels printed on unconfirmed codes (TCWP-1 collision; BFP01 vs DCW_BFP01) | Planon migration / tagging | n/a | n/a | RED (R8) if a print is scheduled; otherwise AMBER (A5) | Print request from Brady queue while code path unresolved | Records: 2 known conflicts; $: reprint plus re-walk per building | T. Dube (ASML) | Written code-stability confirmation before print; collision rulings requested | Open | 09/18/26 | PLN-SUM open-confirm register; WKR-38C |
| RSK-W77-005 | WS-06.02 flush deferred by blocked PO | ST CHW/PCW / WS-06.02 | Per mitigation sheet | Per mitigation sheet | AMBER (A3) | PO $25,947.71 blocked 18 days since first report 08/31/26 | $25,947.71 committed but not released; TR2 exposure continues (rig dark since 07/19/26) | D. Wolf (CSL) via ASML requester | Delegate approver requested; unblock date to be confirmed | Open | 09/18/26 | WKR-36A R1; mitigation sheet 2158727850315652 |
| RSK-W77-006 | TR7 chronic coolant loss | CTRW / TR7 (m4535) | n/a | n/a | AMBER (A1); RED (R9) if runway < 90 days | Loss 0.12 to 0.15 L/day; reservoir runway tracked weekly | Days of runway per latest CTRW summary | D. Wolf (CSL); E. Koning (ASML) | Weekly runway calculation in the CTRW summary; notice if under 90 days | Monitoring | 09/18/26 | CSL-W77-CTRW-TR7-yymmdd series |

## 3. Weekly review routine (Friday, before the C edition)

1. Pull the source sheets in this session; record timestamps and hashes.
2. For every row, compare RPN C to the previous review; fill field 10 for any change; an unexplained change is an A6 finding on the source sheet.
3. Re-test every row with RPN C >= 700 for active mitigation (owner, dated action, date not passed); re-tier.
4. Expire actions whose date has passed with no update: status stays Open, field 20 is flagged, and the row is retested under R1 if it is at or above threshold.
5. Add new rows from the week's minutes, notices, telemetry summaries, permit board findings, and cost pipeline; retire rows only with the closing document in field 24.
6. Refresh exposure fields from the cost pull (`csl-cost-change-control`) and the schedule pull.
7. Set field 23 on every row touched; list rows past 14 days in the register header.
8. Produce the extract for the C edition: top 10 by RPN C, every RED, every tier change, and the count header ("Register: n rows; r RED; a AMBER; c tier changes this week; p rows past review date").

## 4. Roll-up to a program master (multi-project programs)

Per-project risk logs keep the same 25 fields plus a Project ID column and roll to the program register by union; the master adds a project column and keeps each project's Risk IDs unchanged. The same pattern applies to change-order logs (`csl-cost-change-control`, budget workbook standard), so one project's rows can be traced from the master back to the source without renumbering.

## 5. What the register is not

- Not a copy of the FMEA. The FMEA scores; the register acts.
- Not an issues list. A missing document is an open confirm (`csl-asset-data-cmms`, PLN-SUM register), not a risk, unless its absence exposes cost, schedule, or an irreversible step.
- Not a place for opinions about people. A counterpart's late response is a date on field 13 and an A5 tier, nothing more.

# Open-Confirm Register (section of PLN-SUM; standalone when requested)

An open confirm is a question put to the client in writing that blocks or qualifies a deliverable until answered (`references/glossary.md`). The register is how the owner sees what CSL is waiting on, for how long, and what it costs to wait. Columns and tiering per `csl-asset-data-cmms` 4.8: a confirm unanswered more than five business days is AMBER (A5); a confirm that gates a print is RED (R8) once a print date exists; a confirm answered verbally stays open, marked "verbal, written confirmation requested [date]". Populated rows are W77 confirms as of 09/30/26; asked dates marked * are illustrative where the record does not carry them. Eight standing confirms were carried at `CSL-W77-PLN-SUM-260828 R1`.

---

**Open-confirm register** | Program: W77 Planon / asset migration | As of Fri <MM/DD/YY> | Maintained by <operator>, CSL Consulting | Time zone ET

## 1. Register

| # | Question (as asked, in writing) | Asked | To whom (role, name) | Channel / document | Blocks | Business days open | Status | Tier (rule) |
|---|---|---|---|---|---|---|---|---|
| 1 | Issue a versioned functional-code structure spec fixing depth (six / seven / eight levels) | 09/22/26 (after the verbal eight-level ruling) | Client data owner, T. Dube | Email following the 09/22/26 call; agenda item at the Planon weekly | QR prints; code sets beyond mechanical; Loops PML finalization before 10/30/26 | Computed at issue | Open; "up to seven" stated 09/29/26, still no spec | AMBER (A5); RED (R8) if a print is scheduled |
| 2 | Child pump token: PUM (08/24/26 example), PMP (legacy form), or CWP (condenser-water pumps under HEX) | 08/24/26 | Client data owner | Transmittal of mechanical R4; Control sheet open item | Final child codes; PM records for pumps | Computed at issue | Open | AMBER (A5) |
| 3 | TCWP-1 tag collision at W59: confirm TCWP01 / TCWP02 or rule otherwise | 08/28/26* | Client data owner; FM PM | PLN-SUM-260828 R1 | QR prints at W59 | Computed at issue | Open | RED (R8) before prints; AMBER (A5) |
| 4 | BFP01 versus DCW_BFP01 NEW-Placeholder in CHAMPS: code path and merge | 08/27/26* | Client data owner | New Asset Form batch transmittal | Upload of the Watts LF009 RPZ record | Computed at issue | Open | AMBER (A5) |
| 5 | Which of the six CHAMPS templates (Process / Multi-Asset / Standard Asset; IMP / Update) applies to process and multi-asset records | 09/29/26 | Client import owner | Email following the 09/29/26 root-cause statement | Mechanical re-import | Computed at issue | Open | GREEN (G) until 10/06/26; AMBER (A5) after |
| 6 | Instance padding: 2-digit versus 3/4-digit | 08/24/26 | Client data owner | Control sheet open item | Format validation rule; label width | Computed at issue | Open | AMBER (A5) |
| 7 | FAN as a level-2 code versus fan-family child tokens | 08/26/26 | Client data owner | v_3 R2 transmittal | Fan population coding; SE05–10 | Computed at issue | Open | AMBER (A5) |
| 8 | Written confirmation that the functional code will not change when system relationships are layered in (prerequisite to any print) | 09/10/26* | Client data owner | Email; gate G-13 | All QR printing | Computed at issue | Open | RED (R8) on any print date |

## 2. Closed this period

| # | Question | Asked | Answered | By | Document | Effect |
|---|---|---|---|---|---|---|
| — | None closed this period | | | | | |

When a confirm closes, the row moves here for one edition with the answering document cited, then to the code scheme record ledger (`references/code-scheme-record.md` Section 2) if it changed a convention.

## 3. Rules of the register

- One question per row, quoted as asked; a compound question is split so each part can close on its own.
- Asked date is the date of the written request; a question first raised on a call carries the call date in the question text and the written request date in the Asked column.
- Business days open is computed from the Asked date to the edition date and never typed.
- Blocks names the deliverable, print, or import held, so the owner can weigh the wait.
- A verbal answer does not close a row; the row reads "verbal [date]; written confirmation requested [date]".
- Tier and rule on every row (`csl-schedule-risk/references/tier-rules.md`); the tier changes only on evidence.
- Rows never disappear; they close with a document or are withdrawn with a reason and date.
- The count of open confirms is restated in the PLN-SUM bottom line every edition.

---

Pre-issue: every row has asked date, addressee by role and name, channel, blocks, computed age, status, tier with rule; verbal answers marked; closed rows carry the answering document; register count matches the PLN-SUM bottom line; number per `csl-document-control` when issued standalone.

# End-of-Week Gate Register Edition (CSL-<PROG>-PLN-EWO-<yymmdd>)

One to two pages, Friday, per `csl-asset-data-cmms` 4.7. The gate register is the list of numbered conditions (G-nn) that must be satisfied before a program step proceeds; a gate closes on evidence, never on a statement that it will be met. Populated rows are the W77 standing gates as of 09/30/26 (G-13 spec, G-16 walk-through, G-17 SOP, G-18 sensors, G-19 process/systems master list); opened dates marked * and the named owners on G-16 and G-18 are illustrative where the record does not carry them (the record names the gate, not its owner). Companion to PLN-SUM (`templates/program-summary.md`); numbering per `csl-document-control`.

---

**CSL-W77-PLN-EWO-<yymmdd>** | Planon / asset-program gate register | Week <nn>, Fri <MM/DD/YY> | Prepared by <operator>, CSL Consulting | Prepared for B. Gannon, ASML | Distribution: T. Dube (ASML); N. Grubler, E. Hubert (CSL) | ET

## 1. Bottom line

> Five gates open, none closed this week. G-13 (versioned structure spec) blocks tagging and every code set beyond mechanical and is the critical gate for the 10/30/26 Loops + AHS hierarchy deadline. G-18 needs a re-send of the sensor calibration PDF, which arrived truncated at exactly 2 MiB in every copy.

## 2. Gate register

| Gate | Condition to satisfy | Blocks | Owner | Opened | Status | Evidence needed to close | Tier (rule) |
|---|---|---|---|---|---|---|---|
| G-13 | Versioned functional-code structure specification issued in writing (depth fixed; six / seven / eight resolved) | QR label printing; code sets beyond mechanical; Loops PML finalization | Client data owner (T. Dube) | 09/10/26 (first departure from six levels) | Open | The spec document with a version number and date | AMBER (A5); RED (R8) on any print date |
| G-16 | Walk-through questionnaire complete for every unit in the mechanical set (nameplate, space, field tag, photo) | Walk-down closure; nameplate metrics; tag readiness | CSL PM on site (D. Wolf) with FM PMs | 08/27/26* | Open | Questionnaire count = unit count; walk-down items list at zero | AMBER (A3) if unresolved past two weeks |
| G-17 | SOP review complete for the released filter SOPs and any naming SOP (W77-SOP-PCW-040 / -024 Rev 0; draft W77-SOP-GFC-001 corrected) | PM record creation under WS-12.03; naming guidance on the floor | Client technical reviewer (P. Gorman) | 08/04/26 (SOP issue) | Open | Review comments closed; approval dates in the control blocks; GFC-001 reissued under its own properties (`csl-technical-docs` 4.1) | AMBER (A6) on the GFC-001 record discrepancy |
| G-18 | Sensor calibration batch received and reviewable: 350 points across 123 nodes | Sensor child records; calibration fields on the upload | Client controls / BMS (J. Vigo) | 09/12/26* | Open | Complete PDF (size matches the sender's); the batch listed by node | AMBER (A5) once the re-send request is 5 business days old |
| G-19 | Process / systems master list issued before the associated uploads | Process and multi-asset uploads; loop associations | Client data owner | 09/23/26 (Loops PML delivery) | Open | Master list with IDs the upload rows can reference | AMBER (A3) at two weeks |

## 3. Gate movements this week

| Gate | From | To | Evidence | Date |
|---|---|---|---|---|
| G-18 | Open (file received) | Open (re-send requested) | PDF truncated at exactly 2 MiB in every copy; size check against the sender's stated size | <MM/DD/YY> |

## 4. Gates proposed for opening

| Proposed gate | Condition | Why now | Owner |
|---|---|---|---|
| G-20 | Template class ruling for process and multi-asset records (which of the six CHAMPS templates) | Root cause stated 09/29/26; mechanical re-import cannot proceed without it | Client import owner |

## 5. Physical-tagging gate statement

> No QR print is scheduled. Printing requires, in writing: G-13 closed; TCWP-1 at W59 resolved; BFP01 / DCW_BFP01 merge ruled; label stock and printer readiness confirmed; tagging sequence (central plant → roof → tool areas) and CSL / FM split agreed; and the direction on riding the maintenance provider's PM cycles. A print date set before these close is RED (R8) and draws a same-day hold request stating the reprint and re-walk cost.

---

Source note: gate evidence files and their dates as listed; confirm register per PLN-SUM-<yymmdd>; pulled <MM/DD/YY HH:MM ET>.

Pre-issue: every gate has condition, blocks, owner, opened date, status, evidence needed, tier with rule; movements carry evidence and dates; no gate closed on a promise; tagging statement present every edition; number per `csl-document-control`; brand QA per `csl-brand`.

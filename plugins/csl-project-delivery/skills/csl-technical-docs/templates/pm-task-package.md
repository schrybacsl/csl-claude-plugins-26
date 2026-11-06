# PM Task Package (CSL-<PROG>-PM-<sys>-<nnn> Rev <n>)

Skeleton for one preventive-maintenance task package per `csl-technical-docs` 4.3, in the W77 series style `CSL-W77-PM-TRC-001`, `-002`. One package per PM; the package is what the CMMS record is built from and what the maintenance provider signs for at go-live. Example values follow the TR7 point-of-use filter PM to be created under WS-12.03 on release of `W77-SOP-PCW-024 Rev 0`; frequency, duration, headcount, and part numbers are illustrative until the OEM interval and the first timed changeout are on record. Controlled document: control block first, revision history last (`csl-brand` document anatomy Section 5). Asset codes come from `csl-asset-data-cmms` and are confirmed in writing before the record is created.

---

## Document control

| Field | Value |
|---|---|
| Document No. | CSL-<PROG>-PM-<sys>-<nnn> |
| Revision | 0 |
| Title | TR7 24-inch POU Filter Changeout PM |
| Author | <name>, CSL Consulting |
| Technical reviewer | Client technical reviewer (W77: P. Gorman, ASML) |
| Approver | Client system owner (W77: B. Gannon, ASML) |
| Date issued | <MM/DD/YY> |
| Supersedes | None (first PM record for this asset in the current CMMS) |
| Distribution | Client data owner (CMMS); maintenance provider PM; CSL PM on site |

## 1. Asset(s) and functional codes

| Asset | Functional code | Code status | Building / space | Cost center |
|---|---|---|---|---|
| TR7 point-of-use filter housing, 24-inch | As confirmed in writing by the client data owner | Confirmed <MM/DD/YY> by <name> / Provisional (no PM record until confirmed) | W77, TR7 rig area, space code per the upload sheet | Per the upload sheet |

A PM created against a provisional code is RED (R8): the code prints on the work order and the label.

## 2. PM title, frequency, trigger

| Field | Value |
|---|---|
| PM title | TR7 24-inch POU filter changeout |
| Frequency | Quarterly (illustrative) |
| Condition trigger | Differential pressure at or above 8.0 psid at steady flow (illustrative), whichever comes first |
| First due date | <MM/DD/YY>, set at go-live from the last changeout date on record |

## 3. Craft, headcount, duration

| Craft | Headcount | Estimated duration | Basis |
|---|---|---|---|
| Mechanical technician (maintenance provider) | 2 | 2.0 hours including isolation and leak check (illustrative) | First timed execution to replace the estimate |

## 4. Safety and permits

| Item | Value |
|---|---|
| Permit | SIPP permit, type per the installed `sipp` skill; permit number recorded on each execution |
| LOTO | Points per SOP Section 6 (inlet and outlet isolation valves, vent, drain) |
| PPE | Per SOP Section 6 |
| Stop-work | Per SOP Section 6 |

## 5. Parts and consumables

| Part | Part number | Quantity per PM | Stock location | Reorder point |
|---|---|---|---|---|
| Filter element, 24-inch | PCW-24-POU-E1 (illustrative; from the OEM manual) | 1 | Site stores | 2 on hand |
| Housing O-ring | Per OEM manual | 1 | Site stores | 2 on hand |

## 6. Tools and instruments

| Tool | Range / spec | Calibration |
|---|---|---|
| Torque wrench | 10 to 100 ft·lb | Within 12 months |
| Differential pressure reading | Housing gauges or portable dP instrument, 0 to 30 psid (illustrative) | Within 12 months |

## 7. Procedure reference

| SOP | Revision | Steps executed by this PM |
|---|---|---|
| W77-SOP-PCW-024 | Rev 0 | 8.1 to 8.8; acceptance per Section 9 |

## 8. Acceptance and record fields

| Field recorded on close | Unit | Acceptance |
|---|---|---|
| dP after changeout at steady flow | psid | ≤ 2.0 (illustrative) |
| Leak check | pass / fail, minutes held | Pass at 5 minutes |
| Element part number and lot | text | Matches Section 5 |
| Technician, witness, permit number, date, time | text | Complete |

## 9. CMMS PM record fields (Planon)

| Planon field | Value |
|---|---|
| PM name | TR7 24-inch POU filter changeout |
| Asset | Functional code from Section 1 (confirmed) |
| Frequency | Quarterly, or dP ≥ 8.0 psid (illustrative) |
| Standard duration | 2.0 hours (illustrative) |
| Instructions | "Execute W77-SOP-PCW-024 Rev 0, steps 8.1 to 8.8; record dP, part number, lot, permit number" |
| Linked SOP document number | W77-SOP-PCW-024 Rev 0 |

For CSV / XML / JSON packaging of the record, use the installed `planon-doc-generator` skill; keep the client template unaltered when a bulk import is used (`csl-asset-data-cmms`).

## 10. Go-live checklist

| Item | Evidence | Status | Owner | Date |
|---|---|---|---|---|
| SOP at issued revision and linked | W77-SOP-PCW-024 Rev 0 transmittal | Done | S. Schryba | 08/04/26 |
| Asset code confirmed in the CMMS (not a placeholder) | Written confirmation from the client data owner | Open | Client data owner | <MM/DD/YY> |
| PM record created with first due date | Planon PM ID | Open | Client data owner | <MM/DD/YY> |
| Parts in stores or on order with part numbers | Stores record or PO | Open | Maintenance provider | <MM/DD/YY> |
| Craft and provider assigned (IFM 2.0 transition noted) | Provider acknowledgment | Open | Maintenance provider PM | <MM/DD/YY> |
| Permit template referenced | SIPP template ID | Open | CSL PM on site | <MM/DD/YY> |
| Record fields defined in the CMMS | Field list matches Section 8 | Open | Client data owner | <MM/DD/YY> |
| Handover to the maintenance provider recorded | Handover note with date | Open | CSL PM on site | <MM/DD/YY> |

## Revision history

| Rev | Date | Author | Description of change |
|---|---|---|---|
| 0 | <MM/DD/YY> | <name> | First issue |

---

Pre-issue: asset code status stated (confirmed with date and name, or provisional with no record created); SOP number, revision, and step range cited; every part has a part number; frequency and duration sourced or labeled illustrative; Planon fields complete; go-live checklist owners and dates filled; control block first, revision history last; file properties set; PDF alongside; brand QA per `csl-brand`; number per `csl-document-control`.

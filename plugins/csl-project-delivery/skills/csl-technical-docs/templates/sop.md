# Standard Operating Procedure (<SITE>-SOP-<SYS>-<nnn> Rev <n>)

Skeleton for a site-convention SOP per `csl-technical-docs` 4.2. Eleven numbered sections in fixed order, document control block first, revision history last. Example values follow `W77-SOP-PCW-024 Rev 0` (TR7 24-inch point-of-use filter changeout, WS-12.02, issued 08/04/26) where the record supplies them; valve tags, part numbers, torque, pressure, and duration values are illustrative and are replaced from the OEM manual and P&ID before issue. Render with `csl-brand/assets/docx_styles.py`; set file properties to this document; PDF alongside; file name `<SITE>-SOP-<SYS>-<nnn>_Rev<n>_<yyyy-mm-dd>.docx` (`csl-document-control` Section 3).

---

## Document control

| Field | Value |
|---|---|
| Document No. | W77-SOP-PCW-024 |
| Revision | 0 |
| Title | TR7 24-inch Point-of-Use Filter Changeout (WS-12.02) |
| Author | S. Schryba / D. Wolf, CSL Consulting |
| Technical reviewer | P. Gorman, ASML |
| Approver | B. Gannon, ASML |
| Date issued | 08/04/26 |
| Supersedes | Legacy 10-inch point-of-use filter procedure |
| Distribution | Per transmittal CSL-<PROG>-TRN-<yymmdd>-<seq> |

## 1. Purpose

One paragraph: what the procedure achieves and the condition it returns the system to.

> This procedure replaces the 24-inch point-of-use filter element serving test rig TR7 and returns the filter housing to service leak-free at the clean-filter differential pressure baseline, with the changeout recorded against the asset's PM in the CMMS.

## 2. Scope and applicability

| Applies to | Asset / functional code | Location | Excluded |
|---|---|---|---|
| TR7 point-of-use filter housing, 24-inch element | Functional code as confirmed in writing by the client data owner (provisional codes are marked provisional) | TR7 rig area, W77 | 40-inch system filters (W77-SOP-PCW-040); cabinet backflushing (W77-IRO-SOP-014 Rev 1.0) |

## 3. References

| Ref | Document | Number / revision | Date | Note |
|---|---|---|---|---|
| R1 | P&ID, TR7 process cooling water | <drawing number> Rev <n> | <MM/DD/YY> | Valve tags in Section 8 are read from this sheet |
| R2 | Filter housing OEM manual | <title, document number> | <MM/DD/YY> | Torque and element part number |
| R3 | Superseded procedure | Legacy 10-inch point-of-use filter procedure | — | Retired on issue of this SOP |
| R4 | Mitigation sheet row WS-12.02 | Smartsheet 2158727850315652, pulled <MM/DD/YY HH:MM ET> | — | Done-definition and PM linkage (WS-12.03) |

## 4. Definitions

| Term | Meaning in this SOP |
|---|---|
| POU | Point of use: the filter housing at the rig, downstream of the system filter |
| dP | Differential pressure across the housing, inlet to outlet, psid |

Definitions agree with `references/glossary.md` and the delivered code scheme record; a term defined here contrary to a written ruling is an audit finding.

## 5. Roles and RACI (one table for the whole document)

| Activity | Client system owner | Engineering | FM lead | FM technician | Owner's rep (CSL) | Rig owner |
|---|---|---|---|---|---|---|
| Release the window and permit | A | C | R | I | C | R |
| Isolate and verify zero energy | I | I | A | R | C | I |
| Changeout steps 8.3 to 8.6 | I | C | A | R | I | I |
| Leak check and return to service | A | C | R | R | C (witness) | I |
| Records and PM closure | A | I | R | R | C | I |

## 6. Safety

| Hazard (step group) | Control | PPE | Permit / LOTO | Reference |
|---|---|---|---|---|
| Pressurized housing (8.1 to 8.3) | Isolate, vent, and read 0 psig before opening | Safety glasses, gloves, face shield at the vent | SIPP permit, type per `sipp`; locks and tags on V-101 / V-102 (illustrative tags) | Site LOTO procedure <number> Rev <n> |
| Water release in the rig area (8.3, 8.7) | Containment staged; approved drain; spill kit at the housing | Per site protocol | Rig owner notified in 8.1 | Area protocol <number> |

Stop-work conditions: pressure will not fall to 0 psig; visible damage to the housing or bolts; leak persists after the 5-minute hold.

## 7. Prerequisites, materials, tools, parts

| Item | Part number / range | Quantity | Check |
|---|---|---|---|
| Filter element, 24-inch | PCW-24-POU-E1 (illustrative; from R2) | 1 | In stores, lot recorded |
| Housing O-ring | Per R2 | 1 | New, correct size |
| Torque wrench | 10 to 100 ft·lb, calibrated | 1 | Calibration date within 12 months |
| Pressure gauge PI-101 | 0 to 100 psig (illustrative) | — | Reads zero with the housing vented |

Communications before start: rig owner release recorded; SIPP permit active; FM lead and CSL witness available for hold points.

## 8. Procedure

| Step | Action | Expected result | Verification / hold point | Who |
|---|---|---|---|---|
| 8.1 | Confirm the SIPP permit is active and the rig owner has released TR7; close V-101 (inlet) and V-102 (outlet); apply locks and tags | Both valves closed, locked, tagged; permit number on the checklist | HOLD: FM lead and CSL witness initial | FM technician; FM lead; CSL witness |
| 8.2 | Open vent V-103; read PI-101 | 0 psig ± gauge tolerance within 2 minutes | Record reading and time | FM technician |
| 8.3 | Open drain V-104 to the approved drain; capture volume | Housing drains; approximately 40 L (illustrative) | Record volume; no water outside containment | FM technician |
| 8.4 | Remove bolts in a star pattern; lift the bowl; remove the spent element; bag and label with asset code, date, initials | Element out intact; bag labeled | Photo (Appendix C) | FM technician |
| 8.5 | Inspect O-ring seat; fit new O-ring; install new element per the OEM arrow | New element seated | Part number and lot on the checklist | FM technician |
| 8.6 | Refit the bowl; torque to 25 ft·lb (illustrative), star pattern, two passes | All bolts at torque | Wrench serial and reading recorded | FM technician |
| 8.7 | Close V-104; crack V-101 to fill; vent at V-103 to a steady stream; close V-103; hold 5 minutes | No air; no leak at the joint | HOLD: leak check witnessed | FM technician; CSL witness |
| 8.8 | Open V-102; return to service; read dP at steady flow | ≤ 2.0 psid clean baseline (illustrative) | Record dP, flow, time; complete Section 10 | FM technician; rig owner notified |

## 9. Acceptance criteria and return to service

| Criterion | Value | Verified by |
|---|---|---|
| Leak check | No visible leak after 5 minutes at operating pressure | CSL witness and FM lead initials |
| Clean-filter dP | ≤ 2.0 psid at steady flow (illustrative) | Recorded reading |
| Locks removed, permit closed | All LOTO points cleared; permit closeout recorded | FM lead |

"In service" means V-101 and V-102 open, dP recorded, rig owner notified, permit closed.

## 10. Records

| Record | Where | Fields |
|---|---|---|
| Changeout checklist (Appendix A) | Retained with the SIPP permit | Permit number, readings, part number, lot, initials, times |
| CMMS PM record | Planon PM created under WS-12.03 on release | PM name, asset, frequency, standard duration, instructions (steps 8.1 to 8.8), linked SOP W77-SOP-PCW-024 Rev 0; closed with dP, part number, lot, technician |

## 11. Appendices

- A. Changeout checklist (one page, fields matching Section 10).
- B. P&ID excerpt, <drawing number> Rev <n>, valves V-101 to V-104 highlighted.
- C. Photo log: asset code, date, orientation on every photo.

## Revision history

| Rev | Date | Author | Description of change |
|---|---|---|---|
| 0 | 08/04/26 | S. Schryba / D. Wolf | First issue; supersedes the legacy 10-inch point-of-use filter procedure |

---

Pre-issue: control block first and complete; file properties Title / Subject / Author set to this document; one RACI with Engineering present; every step has action, expected result, verification, who; every value sourced (illustrative labels removed); references by number and revision; appendices attached; permit and LOTO named; PDF alongside; brand QA per `csl-brand`; number and file name per `csl-document-control`.

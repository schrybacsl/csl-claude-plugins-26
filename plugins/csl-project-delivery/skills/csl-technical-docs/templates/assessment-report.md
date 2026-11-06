# Assessment / Technical Report (CSL-<PROG>-ASM-<WS> Rev <n>)

Skeleton for an engineering or technical assessment per `csl-technical-docs` 4.5. Verdict table first, fixed vocabulary per failure mode: **CONFIRMED PRESENT** / **PROBABLE, unverified** / **NOT SUPPORTED**. Example values follow `CSL-W77-ASM-WS02.02 Rev 0` (20 pages, issued 08/06/26) where the record supplies them: eight failure modes defined by the workstream; principal finding low delta-T as the common pathway (air binding, waterside fouling, 3-way mixing valves, sub-2-fps branch velocity); field triage rule; actions A1 to A6 with a data-dependency flag. Verdicts, confidence levels, and owners in the example rows are illustrative unless marked as issued. Tiers per `csl-schedule-risk/references/tier-rules.md`; number per `csl-document-control`.

---

## Document control

| Field | Value |
|---|---|
| Document No. | CSL-W77-ASM-WS02.02 |
| Revision | 0 |
| Title | CHW Terminal Performance Assessment: Failure-Mode Verdicts and Field Triage (WS-02.02) |
| Author | <name>, CSL Consulting |
| Technical reviewer | CSL MEP (S. Dube / D. O'Brien) or the client engineering lead |
| Approver | Client engineering lead |
| Date issued | 08/06/26 |
| Supersedes | None |
| Distribution | Client engineering lead; client program lead; workstream owner; maintenance provider PM |

## 1. Bottom line

> Of the eight failure modes the workstream defined, the ones the evidence supports share one pathway: low delta-T at the coil. The field should record coil delta-T, chilled-water supply temperature at the coil, and zone flow before assigning any complaint to a cause. Six actions follow; four need no CMMS data and can start now.

| # | Failure mode | Verdict | Confidence | Action it drives |
|---|---|---|---|---|
| FM-1 | 3-way mixing valves at terminal coils (illustrative row) | CONFIRMED PRESENT | High (drawings + walk-down) | A3: HX replacement scope (WS-22.08) |

One row per failure mode, all eight, in the workstream's numbering.

## 2. Scope and done-definition

| # | Failure mode as the workstream defined it | "Assessed" means |
|---|---|---|
| FM-1 | <definition from the WS-02.02 row> | Presence confirmed or ruled out on at least one unit per zone, with the evidence class stated |

Sources: mitigation sheet row WS-02.02 (Smartsheet 2158727850315652), pulled <MM/DD/YY HH:MM ET>.

## 3. Method and evidence sources

| Source | What it provided | Pull or visit date | Limits |
|---|---|---|---|
| Walk-downs by zone | Valve types, vent locations, strainer condition, visible fouling | <MM/DD/YY> | Units accessible in the window only |
| BMS trends | Coil delta-T, supply temperature, valve position | <MM/DD/YY> to <MM/DD/YY> | Points with trend history only |
| CMMS history (legacy extract) | Corrective work orders by asset | Extract of <MM/DD/YY> | Migration in progress; coverage stated in Section 8 |
| Drawings | Branch sizes for velocity calculation | Drawing numbers and revisions listed in Section 9 | As-built status uncertain where noted |

## 4. Findings per failure mode

Repeat this block for each of the eight:

**FM-n <name>.** Verdict: <CONFIRMED PRESENT / PROBABLE, unverified / NOT SUPPORTED>. Evidence: <observations with unit, date, reading, units>. Confidence: <High / Medium / Low> because <one clause>. What would change the verdict: <the data or test>.

## 5. Principal finding

> Low delta-T is the common pathway. Air binding, waterside fouling, 3-way mixing valves, and branch velocities below 2 fps each reduce heat transfer or bypass the coil, and each presents to the occupant as the same complaint. Treating the complaint without the three readings in Section 6 assigns the wrong cause and the wrong scope.

## 6. Triage rule for the field

| Before assigning a complaint, record | Where | Unit |
|---|---|---|
| Coil delta-T | Coil supply and return sensors or contact readings | °F |
| CHW supply temperature at the coil | Coil inlet | °F |
| Zone flow | Balancing valve or flow station | gpm |

Then classify: delta-T low with supply temperature at setpoint points to flow or bypass causes; delta-T low with supply temperature high points upstream.

## 7. Actions

| # | Action | Owner | Due | Data dependency | Tier (rule) |
|---|---|---|---|---|---|
| A1 | Vent survey and air-bleed on the units listed in Appendix B (illustrative) | Maintenance provider | <MM/DD/YY> | Needs no CMMS data, can start now | AMBER (A1) |

Continue A2 to A6. Each action becomes a tracker row citing this report number.

## 8. Data gaps

| Gap | Source that should hold it | Effect on the verdicts | Closes when |
|---|---|---|---|
| Corrective-work-order history by asset | CMMS (migration in progress) | Frequency evidence unavailable for FM-<n> | Legacy extract reconciled (`csl-asset-data-cmms`) |

## 9. References

| Ref | Document | Number / revision | Date |
|---|---|---|---|
| R1 | WS-02.02 row and attachments | Smartsheet 2158727850315652 | Pulled <MM/DD/YY HH:MM ET> |
| R2 | Equipment watchlist workbook | WS-02.01 | 08/06/26 |

## Appendices

- A. Trend plots by zone (source line under each: point names, date range, pull time).
- B. Walk-down sheets by unit with functional codes.
- C. Photo log with asset code, date, orientation.

## Revision history

| Rev | Date | Author | Description of change |
|---|---|---|---|
| 0 | 08/06/26 | <name> | First issue |

---

Pre-issue: verdict table covers every failure mode in the workstream's numbering with the fixed vocabulary; every finding has evidence with units and dates and states what would change it; triage rule is three measurable readings; every action has owner, due date, data-dependency flag, tier with rule; data gaps name the source and the closing event; references by number and revision; control block first, revision history last; PDF alongside; brand QA per `csl-brand`; number per `csl-document-control`.

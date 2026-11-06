# Turnover Package Index (CSL-<PROG>-TOP-<yymmdd> Rev <n>)

Skeleton for the closeout index CSL opens at 75% complete and carries to final acceptance. It tells the contractor what is owed before the last requisition and tells the owner what has arrived. Every line carries a status and a date; the package is complete when every line is Accepted or waived in writing by the owner. The data and drawings group is mandatory: turnover packages carry data and drawings (standing client direction, the W77 engagement context file (`engagement-context-W77.md` in the W77 Claude Project) Section 5), and the asset-data side is built with `csl-asset-data-cmms`. One populated example row per group; example content is illustrative. Controlled document with a revision history table (`csl-document-control` Section 2).

---

**CSL-<PROG>-TOP-<yymmdd> Rev <n>** | <Project name and phase> | Substantial completion <MM/DD/YY> (certificate reference) | Prepared by <name>, CSL Consulting | Prepared for <Owner PM> | Time zone ET

## Status vocabulary

| Status | Meaning |
|---|---|
| Missing | Owed under the contract; not received |
| Received | Received; not yet reviewed |
| Reviewed | Reviewed by CSL or the A/E; comments returned, resubmittal owed |
| Accepted | Meets the specification; accepted by the named owner reviewer with date |
| Waived | Owner has waived the item in writing (letter or minutes reference) |

## Summary

| Group | Lines | Missing | Received | Reviewed | Accepted | Waived |
|---|---|---|---|---|---|---|
| All groups | 64 | 9 | 12 | 7 | 36 | 0 |

## Revision history

| Rev | Date | Change | By |
|---|---|---|---|
| 0 | 10/26/26 | First issue at 75% complete; 64 lines opened | S. Schryba |

---

## A. Contract closeout (Section 01 77 00)

| # | Document | Spec / contract reference | Responsible | Status | Date | Reviewer | Note |
|---|---|---|---|---|---|---|---|
| A-01 | Certificate of substantial completion with the attached punch list and warranty start dates | A201 §9.8; G704 | A/E | Missing | | Owner PM | Issued only after the owner walk (Section 3.6 of the skill) |

Other lines in this group: final punch list at owner accepted; final change order; consent of surety to final payment; final lien waivers from CM and subcontractors; final application for payment; release of retainage schedule; certificate of occupancy or equivalent (also in Group E).

## B. Record documents (Section 01 78 39)

| # | Document | Spec reference | Responsible | Status | Date | Reviewer | Note |
|---|---|---|---|---|---|---|---|
| B-04 | Electrical single-line diagram, record set, with panel schedules 2LP-A through 2LP-D | 01 78 39; 26 24 16 | Electrical subcontractor via CM | Received | 11/30/26 | CSL MEP (S. Dube) | Panel schedules to be checked against the field-verified circuit list before acceptance |

Other lines: as-built drawings (marked record set plus CAD/BIM native files); record specifications; approved submittals (final set); RFI log with responses; P&IDs for process and mechanical systems; controls drawings, points list, and sequences of operation; TAB report; pressure test, megger, and other test reports; medical gas verification report where applicable.

## C. Operating documents (Sections 01 78 23, 01 78 36, 01 79 00, 01 78 43)

| # | Document | Spec reference | Responsible | Status | Date | Reviewer | Note |
|---|---|---|---|---|---|---|---|
| C-02 | Warranty register: every warranty with start date, end date, vendor contact, and the certificate attached | 01 78 36 | CM | Reviewed | 12/02/26 | Owner Facilities | Two vendor certificates carry a start date earlier than substantial completion; corrected certificates requested 12/02 |

Other lines: O&M manuals by system (indexed, searchable PDF and binder if specified); training records with attendance and recordings; spare parts and attic stock with quantities, part numbers, and storage location; keys, access cards, and credentials; software licenses and BMS passwords transferred per the owner's IT process.

## D. Commissioning (Section 01 91 13)

| # | Document | Spec reference | Responsible | Status | Date | Reviewer | Note |
|---|---|---|---|---|---|---|---|
| D-01 | Final commissioning report with issues log at closure and the seasonal test schedule | 01 91 13 | CxA | Missing | | Owner Facilities; CSL | Two seasonal tests deferred to 01/2027 with dates; retainage lever stated in the certificate |

Other lines: systems manual; PFC and FPT records by system; IST record; deferred test schedule with the contract lever.

## E. Authorities

| # | Document | Reference | Responsible | Status | Date | Reviewer | Note |
|---|---|---|---|---|---|---|---|
| E-01 | Certificate of occupancy (or the jurisdiction's equivalent) for Phase 2 | Local building department | CM | Missing | | Owner PM | Final inspections scheduled 12/01 to 12/03 |

Other lines: AHJ inspection sign-offs by trade; fire alarm acceptance; state licensure inspection (healthcare); permits closed on the permit board.

## F. Data and drawings for operations

| # | Item | Format | Responsible | Status | Date | Reviewer | Note |
|---|---|---|---|---|---|---|---|
| F-01 | Asset list for the CMMS: one row per maintainable asset with tag, functional code, location, parent/child, nameplate data, warranty end, PM plan reference | Client upload template (`csl-asset-data-cmms`) | CM with CSL | Received | 11/24/26 | Owner Facilities; CSL | 212 rows; 14 missing nameplate serials; walk-down scheduled 12/01 |

Other lines: single-lines, P&IDs, and panel schedules in native CAD (also in Group B; listed here because operations needs them on day one); equipment planning final list with responsibility and disposition closed; room data drawings final; BMS graphics and points export; photo log of concealed conditions before close-in.

## File naming on the client tenant

Use the client's convention for files placed on the client's document system and keep the CSL document number inside the document (`csl-document-control` Section 6). W77 pattern: Enterprise_Site_Building + project + discipline + document type, for example `ASML_WLT_077_IN12896_Mech_OM_2027-03-15.pdf`; the client is writing this convention into future contracts, so put it in the closeout section of the specification on new projects.

## Recommendation block (final payment)

> CSL recommends the Owner release final payment when Groups A through F stand at Accepted or Waived. At Rev <n> (<date>), <m> lines remain Missing or Reviewed; the withholding recommendation for the current requisition is in `csl-cost-change-control` memo CSL-<PROG>-MEM-<yymmdd>.

---

Pre-issue: every line has a status and a date; Group F present and populated; warranty start dates checked against substantial completion; asset list row count and defect count stated; file names per client convention; revision history current; brand QA per `csl-brand`; number per `csl-document-control`.

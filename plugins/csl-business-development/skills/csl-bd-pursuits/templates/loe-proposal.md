# Level-of-Effort (LOE) Proposal

Three pages plus an exhibit, for defined work requested by a client inside a running engagement. Number `CSL-<PROG>-LOE-<yymmdd>` (`csl-document-control`); Word via `skills/csl-brand/assets/docx_styles.py` with the document control block first. The narrative names roles, hours, and the rate table; it never types rates or fee totals, which live in the cost side produced per `csl-cost-change-control` 3.10 and reviewed by the Project Director before issue. Method in `csl-bd-pursuits` Section 3.9. Populated below with the W77 case: the client program lead's request for a proposal to merge the building condition assessment sheet (about 2024) with the IRO roadmap into one maintained source on a PMO / IMT update cadence; proof of concept of 348 consolidated records built Thu 09/17/26; proposal owed the week of 09/21/26. Hours below are illustrative of the format and are replaced by the task estimate.

---

**CSL-W77-LOE-260925** | Level-of-Effort Proposal: Consolidated BCA + IRO Roadmap Source and Maintenance | Rev 0 | Prepared by <operator>, CSL Consulting | Prepared for B. Gannon, ASML CRE | Reviewed by E. Hubert | Fri 09/25/26 | Time zone ET

## 1. Objective (bottom line)

One maintained source that combines the building condition assessment records with the IRO roadmap, keyed so that a record appears once, updated on the PMO / IMT cadence, and reported through the existing Friday editions, so the two sources are never reconciled by hand again.

## 2. Current state

| Item | State at 09/25/26 |
|---|---|
| Request | Client program lead's request for a proposal to merge the assessment sheet with the IRO roadmap into one maintained source with a PMO / IMT update cadence (cite the request email date or minutes item on issue) |
| Roadmap | W77 Roadmap Master 2025–2032, Smartsheet 1059284113641348; parent and child rows; pending migration to SharePoint |
| Assessment sheet | Building condition assessment records, about 2024; static file; keys differ from the roadmap |
| Proof of concept | 348-record consolidated tracker, `CSL-W77-TRK_Roadmap-IRO-Consolidated_2026-09-17.xlsx`, built 09/17/26; key mapping and unmatched-record list on its Control sheet |
| Reporting | Friday End-of-Week report (WKR-nnC) and Planon summary carry roadmap figures weekly; assessment records are not yet in any edition |

## 3. Proposed deliverable

1. The consolidated tracker as the maintained source: in Smartsheet until the migration, then a SharePoint list with the same columns.
2. A data dictionary (column, source, key rule, refresh rule).
3. A reconciliation log: every record matched, merged, or held, with the rule applied and the date.
4. A monthly PMO / IMT update package: what changed, what is unmatched, decisions requested, one page.

## 4. Method

| Step | Work | Output |
|---|---|---|
| 1 | Freeze the key mapping from the proof of concept; document the rule per source | Data dictionary v1.0 |
| 2 | One-time reconciliation of the full record set; unmatched records listed with a proposed disposition | Reconciliation log R0; change list proposed to the client (no write to a client sheet without instruction) |
| 3 | Client review of the change list; dispositions recorded by date | Reconciliation log R1 |
| 4 | Build the maintained source and its views (by system, by E-GRP, by year) | Consolidated source v1.0 |
| 5 | Maintenance cycle: weekly refresh with the Friday editions; monthly PMO / IMT package; quarterly re-baseline check | Weekly refresh note; monthly package |

## 5. Cadence

Weekly refresh alongside WKR-nnC and PLN-SUM; monthly PMO / IMT package five business days before the meeting; quarterly re-baseline check with the roadmap close.

## 6. Roles and hours by task (illustrative figures; replaced by the task estimate)

| Task | Project Manager | Assistant PM | Data / dashboard specialist | Project Director | Basis |
|---|---|---|---|---|---|
| 1 Data dictionary | 6 | 4 | 8 | 1 | Columns in the proof of concept |
| 2 One-time reconciliation | 8 | 16 | 12 | 1 | 348 records plus unmatched set |
| 3 Client review cycle | 4 | 4 | 2 | 1 | One review cycle |
| 4 Maintained source and views | 6 | 6 | 16 | 1 | Three views |
| 5 Maintenance, per month | 2 | 6 | 4 | 0.5 | Weekly refresh and monthly package |

Build phase (tasks 1 to 4) and maintenance phase (task 5, per month) are priced separately in the cost side.

## 7. Assumptions

Client supplies both sources and edit access on the client tenant; one review cycle per package; the roadmap remains the system of record for budget and forecast figures; no new data sources in the base scope; meetings are the existing Planon weekly and the PMO / IMT cadence.

## 8. Exclusions

Field verification of assessment records; new condition assessments; software licensing; dashboard rebuilds beyond the existing views; data entry into the client's CMMS.

## 9. Dependencies on client access

Named owner of the assessment sheet; SharePoint migration timing (columns carry over unchanged); PMO / IMT calendar for the monthly package.

## 10. Schedule

Build phase: four weeks from written acceptance, with the reconciliation log R0 at week two and the maintained source at week four. Maintenance: from the first Friday after acceptance of the source.

## 11. Fee basis

Hours by role per Section 6 against the CSL rate table for the engagement, referenced by contract and edition in the cost side (`csl-cost-change-control` 3.10). Change triggers: new data source; cadence change; record count above the proof-of-concept scale by more than a stated percentage; additional review cycles.

## 12. Acceptance

| | Client | CSL Consulting, LLC |
|---|---|---|
| Name and title | B. Gannon, ASML CRE | E. Hubert, Project Director |
| Signature and date | | |

Exhibit A: proof-of-concept tracker Control sheet (348 records; key mapping; unmatched list).

Pre-issue: request cited by thread and date; current state dated with sheet IDs; deliverable named; hours from the task estimate; no rates or totals in the narrative; cost side reviewed by the Project Director; document control block complete; brand QA per `csl-brand`.

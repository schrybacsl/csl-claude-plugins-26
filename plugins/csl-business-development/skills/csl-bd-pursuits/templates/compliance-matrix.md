# Compliance Matrix

Built before the outline, because it is the outline and the red-team checklist. Every "shall", "must", "will provide", "required", and every evaluation criterion in the solicitation becomes one row. Lives as a tab in the pursuit workbook (openpyxl per `csl-brand` Section 5: Control sheet first, navy header row, filters on) and exports to the response appendix when the solicitation asks for a cross-reference. Method in `csl-bd-pursuits` Section 3.4.

---

## Columns

| Column | Content | Rule |
|---|---|---|
| # | Sequence | Never renumbered after draft 1; new rows from addenda take the next number with the addendum cited |
| Section ref | Solicitation section, page, and paragraph | Quote the reference exactly as the document numbers it |
| Requirement | The operative words, quoted | One requirement per row; split compound sentences |
| Type | Mandatory (pass/fail) / Scored / Format / Logistics / Form | Mandatory rows are checked first at red team |
| Response location | Tab and heading in the response | Must exist in the final file; verified page number added at red team |
| Owner | Person drafting the response to this row | One name |
| Status | Open / Drafted / Reviewed / Final | Updated at each review |
| Page budget | Pages allotted to this row's response | Sum per tab checked against the limit |
| Addendum | Number of the addendum that added or changed the row | Blank when original |
| Notes | Interpretation questions, pre-submittal answers, evaluator emphasis | Cite the Q&A number or memo |

## Extraction method

1. Read the whole package in order: instructions, scope, evaluation criteria, forms, exhibits, sample contract.
2. Extract in document order; quote; one row each. Evaluation criteria become rows even when phrased as "the owner will consider", because they decide the score.
3. Classify each row by type.
4. Assign a response location so that headings mirror the solicitation's words; the table of contents is generated from this column.
5. Assign owners and page budgets; total the budget against the limit the owner's way (exclusions and inclusions as the solicitation states them).
6. After every addendum and every pre-submittal Q&A, re-extract; mark added or changed rows with the addendum number.
7. At red team the reviewer reads the final file against this matrix, row by row, and records the verified page number in the response location column.

## Lists kept beneath the matrix

**Forms and certifications**: form name | solicitation reference | signatory (Partner, VP, CFO) | notarization required | status.

**Format rules**: page limit and what counts; font and minimum size; margins; paper size; single or double sided; tab order; binding; file format and size limit for portal upload; file naming the portal requires.

**Submission logistics**: method (portal, hard copies, email); number of originals and copies; USB or electronic copy; delivery address and room; due date, day of week, time, and zone; late-submittal rule; receipt or confirmation expected; delivery one day early for physical submittals.

## Excerpt (City of Pensacola RFQ 26-062; requirement wording illustrative; the real matrix quotes the RFQ)

| # | Section ref | Requirement (illustrative wording) | Type | Response location | Owner | Status | Page budget | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | RFQ §2.3 | Attendance at the mandatory pre-submittal conference on 09/01/26 is required for a submittal to be considered | Mandatory | Appendix A: sign-in confirmation | S. Schryba | Complete 09/01/26 | 0 | Sign-in evidence filed with the pre-submittal memo |
| 2 | RFQ §3.1 | Submittals received after 2:30 PM CT on Thu 09/24/26 will not be opened | Logistics | Delivery plan: hand delivery Wed 09/23/26 | N. Graboyes | Open | 0 | Receipt to be obtained at delivery |
| 3 | RFQ §4.1 | Provide a firm profile including years in business, office locations, and the office that will serve this contract | Scored | Tab 1, Firm Profile | N. Graboyes (figures); S. Schryba (text) | Drafted | 2 | Office of record to be stated |
| 4 | RFQ §4.3 | Provide a minimum of three comparable public projects completed in the last ten years, with owner reference contacts | Scored | Tab 3: North Charleston Intermodal Center; Azalea Complex; North Charleston Aquatic Center | S. Schryba; N. Graboyes (references, dates) | Drafted; references open | 6 | Completion dates from Marketing confirm the ten-year window |
| 5 | RFQ §4.5 | Provide resumes for the proposed Project Manager and key staff and a statement of availability for the contract term | Scored | Tab 4, Team; availability table by phase | PX; N. Graboyes | Open | 5 | Team named by the PX 08/28/26 |
| 6 | RFQ §5.2 | Acknowledge all addenda on the form provided, signed by an officer of the firm | Form | Tab 7, Forms | Partner signature | Open | 0 | Watch for addenda after the 09/01 Q&A |

Pre-issue: every requirement quoted; types assigned; every response location exists in the final file with a verified page number; page budgets total inside the limit; forms list complete with signatories; logistics block complete with day, time, zone; addenda rows marked; red team signed the matrix.

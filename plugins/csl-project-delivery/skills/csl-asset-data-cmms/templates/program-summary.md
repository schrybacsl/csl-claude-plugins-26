# Weekly Program Critical Summary (CSL-<PROG>-PLN-SUM-<yymmdd> R<n>)

One to two pages, Friday, per `csl-asset-data-cmms` 4.6 and `csl-brand` PDF anatomy (running header with document number; source note at the foot). Seven sections in fixed order so editions compare. Counts are re-derived from this session's files; nothing is carried forward from last week's edition or taken from a counterpart's recap. Populated rows below are from the W77 record as of 09/30/26; asked dates marked * are illustrative. A substantive same-day change increments the revision (`CSL-W77-PLN-SUM-260828 R1` superseded R0). Feeds the Friday WKR-nnC (`csl-weekly-reporting`).

---

**CSL-W77-PLN-SUM-<yymmdd> R0** | Planon / asset-program weekly critical summary | Week <nn>, Mon <MM/DD/YY> to Fri <MM/DD/YY> | Prepared by <operator>, CSL Consulting | Prepared for B. Gannon, ASML | Distribution: N. Grubler, E. Hubert (CSL); T. Dube (ASML) | Time zone ET

## 1. Bottom line

> Delivered to date: 972 records across three files (MEP list R3, 672; mechanical v_5, 239; New Asset Forms, 61), plus the Loops PML of 09/23/26 (18 loops, 17 in scope). The mechanical set awaits re-import on an unaltered CHAMPS template following the root cause stated 09/29/26. Structure depth remains OPEN after four rulings with no versioned spec, so no QR print is scheduled (gate G-13). Asked this week: the versioned structure spec and the template class ruling for process and multi-asset records.

## 2. Delivered to date

| File | Rev / version | Date | Records | Convention built to | Status |
|---|---|---|---|---|---|
| MEP list | R3 | 08/24/26 | 672 | Six-level codes (V1.0) | Delivered; superseded R0 to R2 in `_superseded/` |
| Mechanical segment builder | v_5 | 08/26/26 | 239 (v_4 235 + 4 parents) | 08/24/26 rulings; depth OPEN | Delivered |
| Client template, mechanical, POPULATED | R0 | 08/26/26 3:22 PM ET | 237 named assets; 216 Active in CHAMPS; 21 Not in CHAMPS | 08/24/26 rulings | Delivered (TRN-260826-01); re-import pending |
| New Asset Forms | Batch | 08/27/26 | 61 (IN 12366, 12491, 12548; BFP01) | 08/24/26 rulings | Delivered; 21 of 32 slurry rows on the walk-down list |
| Loops PML | R0 | 09/23/26 | 18 loops with sub-assets; 17 of 18 in scope (HW heat excluded) | Convention in force 09/23/26; depth OPEN | Delivered |
| Total | | | 672 + 239 + 61 = 972 | | CSL 09/11/26 itemization of 962 under reconciliation to this file-level total |

## 3. Open-confirm register

| # | Question | Asked | To whom | Blocks | Status / tier (rule) |
|---|---|---|---|---|---|
| 1 | Versioned structure spec fixing depth | 09/22/26 (verbal ruling; written confirmation requested) | Client data owner (T. Dube) | QR prints; code sets beyond mechanical; Loops PML finalization before 10/30/26 | Open; AMBER (A5); RED (R8) if a print is scheduled |
| 2 | Child pump token PUM / PMP / CWP | 08/24/26 | Client data owner | Final child codes; PM records | Open; AMBER (A5) |
| 3 | TCWP-1 collision at W59 (TCWP01 / TCWP02) | 08/28/26* | Client data owner; FM PM | QR prints at W59 | Open; RED (R8) before prints |
| 4 | BFP01 versus DCW_BFP01 placeholder: code path and merge | 08/27/26* | Client data owner | New Asset Form upload | Open; AMBER (A5) |
| 5 | Template class for process and multi-asset records (which of six CHAMPS templates) | 09/29/26 | Client import owner | Mechanical re-import | Open |

Full register: `templates/open-confirm-register.md`. Eight standing confirms were carried at PLN-SUM-260828 R1; the count is restated every edition.

## 4. Import status

| File | Submitted | Result | Rejection log | Root cause on record | Next step |
|---|---|---|---|---|---|
| Client template, mechanical, R0 | 08/26/26 | Not imported | Requested; log not yet received* | Stated 09/29/26: unaltered CHAMPS templates required ("any change and they will not upload") | Re-issue on the pristine template class ruled in confirm 5; T1 to T7 pass recorded |

Live records verified this week: none pulled (no import has completed); the post-import checks in `csl-asset-data-cmms` 3.8 run on the first live pull.

## 5. Intake line (New Asset Forms)

| Received | Coded | Approved | Uploaded | Waiting (oldest age) |
|---|---|---|---|---|
| 61 assets in three INs (08/27/26 batch) | 61 | Pending data-owner approval | 0 | 61; oldest since 08/27/26 |

Visibility fix in place: shared tracker view with edit access for the data owner; this line appears every edition.

## 6. Next deliveries

| Deliverable | Date | Depends on |
|---|---|---|
| Mechanical re-issue on the ruled template class | Within 2 business days of confirm 5 | Confirm 5 |
| Gases and plumbing code set v_1 | <MM/DD/YY> | Scope ruling in writing for the family; census |
| Loops + AHS hierarchy, final | Before 10/30/26 (IFM 2.0 transition) | G-13 versioned structure spec |

## 7. Risks

| Item | Tier (rule) | Exposure | Owner | Action | Date |
|---|---|---|---|---|---|
| Structure depth unspecified (four rulings, no versioned spec) | AMBER (A5); RED (R8) on any print date | Reprint and re-walk of every tagged asset if the code changes after printing; Loops PML rework before 10/30/26 | Client data owner | Issue the versioned spec (G-13) | 10/07/26* |
| Counterpart recap states mechanical "work in progress" and only 3 assets uploaded | AMBER (A6) | Delivery record misstated | S. Schryba | Record correction with TRN-260826-01 evidence; reconcile CSL's 962 itemization to the 972 file total by file | Same day as the recap |
| Iron in mixing columns 580 ppm against 0.1 total-Fe specification (found while building the loop hierarchy) | Reported to the client engineering lead as an engineering finding (memo / notice per `csl-technical-docs` 4.7) | Loop chemistry, outside this program's scope | D. Wolf | Pointer only here; finding lives in the memo | Issued <MM/DD/YY> |

---

Source note: files listed in Section 2 with their Control-sheet hashes; intake tracker pulled <MM/DD/YY HH:MM ET>; live CMMS extract <date or "none this week">. This summary reflects the files and records as of the pull timestamps listed.

Pre-issue: counts re-derived and re-added in code; every file row states the convention built to; every confirm has an asked date and a tier with rule; import root cause quoted with its date; engineering findings pointed to, not embedded; number and file name per `csl-document-control`; brand QA per `csl-brand`.

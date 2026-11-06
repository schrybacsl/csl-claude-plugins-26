# Reconciliation Method: Census to Legacy Extract

Read this before joining a candidate asset list to a legacy CMMS extract (`csl-asset-data-cmms` 3.3) and before answering "is this asset already in CHAMPS". The output is one classified row per candidate asset, a findings list by pattern, and the counts that go on the Control sheet and into PLN-SUM. W77 references: CHAMPS Total Combined Assets extract, 2,645 records; the 672-record MEP list (R0 08/06/26 to R3 08/24/26); the mechanical client template of 08/26/26 (237 named assets: 216 resolved to Active CHAMPS records, 21 Not in CHAMPS). The extract is never edited; every finding is a row in the reconciliation tab with the extract's record identifiers.

---

## 1. Inputs

| Input | Required fields | Provenance recorded |
|---|---|---|
| Candidate list (census or segment builder) | Draft functional code, unit token, description, building, location, source row reference | Source sheet, ID, pull time |
| Legacy extract | Legacy asset ID, legacy code, description, building, location, status, record class (Active / placeholder / inactive) | File name, extract date, MD5, row count (2,645) |
| Cross-reference aids | Panel lists, drawings extractions, walk-down sheets | Revision and date |

## 2. Join order

Run the joins in this order and stop at the first match per candidate, recording which join matched:

| Order | Join key | Normalization | Typical yield |
|---|---|---|---|
| J1 | Legacy code, exact | Trim; uppercase; strip separators | Highest confidence |
| J2 | Legacy code, token-normalized | Collapse `SE05` / `Smoke Exhaust 05`; `AHU15ERV` / `AHUERV15` | Catches source double-listings |
| J3 | Description plus building | Lowercase; remove punctuation; unit tokens compared | Medium; verify by location |
| J4 | Location plus equipment family | Space code and family token | Low; walk-down candidate |
| — | No match | — | Not in legacy |

A J3 or J4 match is marked "verify" until a walk-down or a nameplate confirms it; it is never counted as resolved in the delivered counts.

## 3. Classification classes

| Class | Definition | Counts as | Next step |
|---|---|---|---|
| Active with code | One Active legacy record; legacy code present; single match | Resolved | Carry legacy ID; new code assigned |
| Active without code | One Active legacy record; legacy code blank or malformed | Resolved | New code assigned; defect noted |
| Not in legacy | No match after J1 to J4 | Not in legacy (W77 mechanical: 21 of 237) | New record; nameplate and space required |
| Double-listed | Two or more legacy records for one physical asset, or one legacy record for two candidates | Finding | Merge ruling on the confirm register; one record carried |
| Code defect | Legacy record carries another asset's code or a self-contradicting code | Finding | Corrected in the code set; defect reported with IDs |
| Placeholder | Legacy record class is a placeholder (`NEW-Placeholder`) | Not Active | Code-path ruling plus merge; never counted as resolved |
| Dangling child | Candidate child whose parent has no record in either set | Finding | Parent record added to the code set |

## 4. Findings patterns (W77 instances) and dispositions

| Pattern | Instance | How it was detected | Disposition recorded |
|---|---|---|---|
| Source double-listing | SE05–10 versus Smoke Exhaust 05–10 | J2 token normalization | One record per fan; the duplicate listed for merge |
| Source double-listing | AHU15ERV / AHUERV15 | J2 | Single CHAMPS record confirmed; one code |
| Tag collision | Two pumps field-tagged TCWP-1 at W59 | Walk-down against J3 candidates | Provisionally TCWP01 / TCWP02; confirm register; QR print held (RED (R8) if scheduled) |
| Placeholder | BFP01 (Watts LF009 RPZ, NE entrance) versus DCW_BFP01 NEW-Placeholder | Extract record class | Code-path ruling plus merge requested |
| Code defect | SCHWP06 record carrying CHW01_PMP05, duplicating SCHWP05 | C3 uniqueness on legacy codes | Defect reported with both record IDs; code set corrected |
| Dangling parent | HEX3 / HEX4 condenser-water pumps under HEX3 / HEX4 with no HEX records | C4 parent-exists | HEX03 / HEX04 (and CDP03 / CDP05) parent records added in v_5, 08/26/26 |
| Nameplate gap | 21 of 32 slurry-machine rows (IN 12491) lacking nameplate data; forms with zero commissioning dates | R3 / R4 completeness | Walk-down items with the IN number; rows held |

## 5. Reconciliation tab layout (companion workbook)

| Column | Content |
|---|---|
| Candidate ID | Row reference in the census or segment builder |
| Draft code | Assembled code per the convention built to |
| Description, building, location | As carried |
| Join matched | J1 / J2 / J3 / J4 / none |
| Legacy asset ID(s) | One or more; all listed for double-listings |
| Legacy code(s) | As the extract carries them |
| Legacy status / class | Active / placeholder / inactive |
| Class | Section 3 value |
| Finding pattern | Section 4 value or blank |
| Confirm # | Open-confirm row holding this record, if any |
| Walk-down # | Walk-down item, if any |
| Disposition | Carry / merge / add parent / hold / review |
| Notes | Dated, initialed |

Roll-up at the top of the tab: counts per class; resolved of total with the base stated ("216 of 237 resolved to Active CHAMPS records"); findings by pattern; holds by confirm.

## 6. Reporting the result

- On the Control sheet: counts per class and the extract's date and hash.
- In PLN-SUM Section 2: the file's record count with "resolved / Not in legacy" and the number of open findings.
- In the transmittal: the holds and what unblocks them.
- To the client data owner: the findings list with legacy record IDs, because the merges and defects are corrections in their system, not in CSL's file.
- Never: a resolved percentage without its base; a placeholder counted as Active; a J3 / J4 match reported as resolved before verification; a candidate dropped silently because it did not join.

## 7. Re-running after a new extract

A new extract (new date, new hash) re-runs the whole join; classes can change (a placeholder merged, a defect fixed) and the delta is reported by class with the two extract dates. Do not patch last month's classification by hand.

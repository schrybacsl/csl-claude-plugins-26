# Received Technical Document Audit: Checklist and Memo Form

Use when an SOP, PM package, scope, or technical report issued by someone else arrives for CSL review, comment, or signature (`csl-technical-docs` 4.9). Run the checks in order, because each scopes the next; write every finding as a record discrepancy with document numbers and dates, never as a judgment of the author. Findings go out as a memo per `csl-executive-memo` (`CSL-<PROG>-MEM-<yymmdd>`). The worked example is the real case: draft `W77-SOP-GFC-001 Rev 0` built by Save-As from `W77-SOP-PCW-040 Rev 0`, carrying PCW-040's title and number in its file properties and teaching the code structure superseded by the 08/24/26 format rulings (Functional Code Structure v1.1); logged in the GFC structure record memo `CSL-W77-MEM-260919`. Received and correction-request dates are those of the actual review.

---

## Part 1. Checklist

| # | Check | How | Pass condition | Finding form if it fails |
|---|---|---|---|---|
| 1 | File properties | Open Title, Subject, Author, Company, created and modified dates (Word: File > Info; or `python-docx core_properties`) and compare with the control block | All four name this document | "Properties carry Title = '<other title>', Subject = <other number>: Save-As inheritance from <source document>" |
| 2 | Supersession | Read the control block's Supersedes line; check the document system for the document it should retire | Supersedes named and correct; the retired document is the one still in circulation | "Supersedes line absent; <legacy number> still circulating" |
| 3 | Dictionary versus delivered corpus | Compare Definitions and any worked examples with `references/glossary.md`, the code scheme record (`csl-asset-data-cmms/references/code-scheme-record.md`), and issued SOPs | No term or example contradicts a written ruling in force | "Section 4 defines <term> contrary to the ruling of <date> (<document>)" |
| 4 | RACI count and completeness | Count RACI tables; list every "who" in the steps; check Engineering appears as a role | Exactly one RACI; every step role in it; Engineering present | "Two RACIs (§5, §8) disagree on <activity>"; "Steps 8.3 to 8.6 assign <role> not in the RACI" |
| 5 | Appendices and references | For each citation (Appendix, drawing, form, prior SOP), confirm the item exists at the stated revision | All cited items attached or retrievable | "Appendix B cited at §8.4, not attached"; "Drawing <number> cited without revision" |
| 6 | Examples versus current ruling | Re-derive each worked example from the written ruling | Examples reproduce the ruled structure | "Example code <x> follows the pre-08/24/26 structure" |
| 7 | Review and approval evidence | Names and dates in the control block against the correspondence on file | Reviewer and approver evidence exists for the dates shown | "Approver field filled <date>; no approval on record" |
| 8 | Step quality (SOPs and PM packages) | Sample five steps for action, expected result, verification, who; search for "as required", "as needed", "appropriate" | Every sampled step complete; no open-ended phrases | "Steps <n> lack verification; 'as required' at <n>" |
| 9 | Values and units | Sample values for source, unit, tolerance, part number | Every sampled value sourced with unit | "Torque at 8.6 has no unit or source" |
| 10 | Label or record exposure | Ask whether any content prints on a tag, work order, or contract exhibit | None, or all such content confirmed in writing | RED (R8): "Section <n> would put <code> on labels before written confirmation" |

Tiers: record discrepancies are AMBER (A6); a defect that would reach a label, tag, work order, or contract exhibit is RED (R8); a document that reverses a minuted decision without a written change is RED (R7). Cite the rule with the tier every time.

## Part 2. Worked example, findings as recorded

| # | Finding | Tier (rule) | Evidence |
|---|---|---|---|
| 1 | Draft W77-SOP-GFC-001 Rev 0 file properties carry Title and Subject of W77-SOP-PCW-040 (Save-As inheritance) | AMBER (A6) | Properties inspected <received date>; PCW-040 Rev 0 issued 08/04/26 |
| 2 | Section 4 Definitions describes the functional-code structure superseded by the 08/24/26 format rulings (Functional Code Structure v1.1: `ASML_WLT_077_` prefix, code resets at the unit, loop association as a column) | RED (R8) if adopted for tagging; AMBER (A6) as a record discrepancy while tagging is held | 08/24/26 rulings; GFC structure record CSL-W77-MEM-260919 |
| 3 | Worked examples in the draft produce codes that differ from the delivered code sets (mechanical v_5, 08/26/26) | AMBER (A6) | Code set Control sheet, convention built to |

## Part 3. Memo form (CSL-<PROG>-MEM-<yymmdd>)

```
MEMORANDUM                                   CSL-W77-MEM-<yymmdd>
To: <document author>, <organization>        From: <name>, CSL Consulting
Date: <MM/DD/YY>                             Re: Review of <document number and revision>, received <MM/DD/YY>
Distribution: <client program lead>; <client data owner>; CSL Project Director

Bottom line. <One paragraph: the document is / is not ready for approval; the count of findings by tier; the one action that unblocks it.>

Findings.
1. <Finding as a record discrepancy, with document numbers and dates> — <TIER (rule)>.
2. ...

Recommended actions.
| Action | Owner | Due |
| Reissue the draft under its own properties and control block; restate Section 4 to the 08/24/26 rulings | Document author | <MM/DD/YY> |
| Hold any tagging or PM creation that cites the draft until the reissue | Client data owner | Standing |

Basis. <Documents relied on: the draft, the rulings by date, the code scheme record, the delivered code sets with Control-sheet conventions, the glossary.>

<name>, CSL Consulting
```

## Part 4. What the memo never contains

- Adjectives about the author or the drafting; only discrepancies with documents and dates.
- Health, HR, or personal information.
- CSL approval language; CSL recommends, the client approves.
- A verbal ruling presented as the standard; verbal rulings are cited as "stated on the call by <name>, <date>; written confirmation requested <date>".

---

Pre-issue: all ten checks recorded with pass or the finding form; every finding tiered with its rule; worked examples re-derived, not eyeballed; memo numbered per `csl-document-control`; distribution includes the data owner when a code or label is involved; correction requested in writing the same day for RED (R7) and RED (R8) items.

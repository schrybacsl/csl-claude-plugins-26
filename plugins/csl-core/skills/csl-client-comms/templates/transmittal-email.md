# Transmittal Email

The email is the transmittal record when no separate form exists (`csl-document-control` Section 5). It carries the transmittal number, the document numbers with revision, what changed, the purpose, the response date, and the attachments with counts, so that a share-log entry plus this email settles any later question of what was delivered when. Method in `csl-client-comms` Section 3.10; numbering `CSL-<PROG>-TRN-<yymmdd>-<seq>`.

---

## Draft block

| Field | Entry |
|---|---|
| To | The recipients who act on the document (import, review, approve) |
| Cc | The standing list for the family; CSL Project Director on anything contractual or first-of-kind |
| Subject | `[Program] \| [Document title] \| [Transmittal number]` |
| Share | From the client tenant, edit access where import or edit is expected; the share sent before the email so the log timestamp precedes it |
| Attachments | The files, or the tenant links when the files exceed mail limits; each listed with row or page count |

## Body skeleton

1. Transmittal number, date and time with zone.
2. Documents: number, revision, title, what changed since the previous revision (one line each; "first issue" for R0).
3. Purpose: For import / For review / For approval / For record / For information.
4. Response requested by: date, day of week; "none" for information-only.
5. Commitment met, when one exists: minutes item or agreement date.
6. Attachments listed with counts; share location named so the log and the email agree.
7. Sign-off and signature block.

## Populated example (program record, 08/26/26)

> Subject: W77 | Mechanical asset upload sheet | CSL-W77-TRN-260826-01
>
> Bill, Tom,
>
> Transmittal CSL-W77-TRN-260826-01, Wed 08/26/26 3:22 PM ET.
>
> Documents:
> 1. ASML_WLT_077_Mechanical Asset Upload Sheet August 26 2026 CSL-Consulting.xlsx, 237 rows (216 resolved to Active CHAMPS records, 21 Not in CHAMPS). Built on the CHAMPS template CSL holds, data rows only, to the 08/24/26 format rulings (Functional Code Structure v1.1). First issue of the mechanical set on the client template.
> 2. Copy-paste-ready CSV of item 1, same 237 rows.
>
> Purpose: for import.
>
> Response requested by: Fri 08/28/26, so the import can run this week. Please send the importer's log either way.
>
> This meets the 48-hour commitment made 08/24/26 (Minutes #016, item 016-002). Both files are shared with edit access from the program SharePoint library to the four of us on this email; the companion CSL workbook (segment builder v_5, 239 rows, with the Control sheet and reconciliation tab) sits beside them for reference and is not an import file.
>
> Thanks,
> Steven
>
> Cc: N. Grubler, E. Hubert (CSL)

## Register row (transmittal register, same day)

| Number | Date / time | From | To | Method | Documents | Purpose | Response by | Notes |
|---|---|---|---|---|---|---|---|---|
| CSL-W77-TRN-260826-01 | 08/26/26 3:22 PM ET | S. Schryba | B. Gannon, T. Dube (ASML); N. Grubler, E. Hubert (CSL) | M365 share (edit) + email | Mechanical upload sheet xlsx (237 rows); CSV | For import | 08/28/26 | Meets 016-002 |

## Reissue form

Same-day reissue with a substantive change: new transmittal sequence (`-02`), document revision incremented (`R1`), one line stating what changed and that it supersedes the earlier file, which moves to `_superseded/`. Typo-only fix: same revision, new transmittal sequence, the body says "corrected file, no data change".

Pre-send: number formed and unused; documents by number with revision and counts; what changed stated; purpose and response date present; share sent first from the tenant; register row drafted; evidence of delivery retained (share log screenshot when the stakes justify it); nothing sent by the agent.

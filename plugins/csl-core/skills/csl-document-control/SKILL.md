---
name: csl-document-control
description: >
  Document numbering, revision control, file naming, transmittals, filing locations, and record
  retention for everything CSL issues. Use it whenever a deliverable needs a number or revision (WKR
  reports, memos, notices, SOPs, PM and scope packages, assessments, upload sheets, minutes,
  proposals), whenever a file is named, saved, or filed to SharePoint, whenever something is
  transmitted to a client or contractor, whenever a counterpart document needs a provenance check
  (metadata, Save-As inheritance, superseded revisions), and whenever someone asks "where does this
  live" or "when did we deliver that".
---

# CSL Document Control

The document number is the handle the whole program uses to refer to a deliverable. It proves what was issued, when, in what revision, and it is how a delivery is defended later ("mechanical upload sheet delivered Wed 08/26/26 at 3:22 PM, shared to Gannon/Dube/Grubler/Hubert"). Number everything that leaves the agent as an issued file. Drafts carry the number with a `DRAFT` watermark and no issue date.

---

## 1. Number format

```
CSL-<PROG>-<FAM>-<ID>[<ED>] [R<n> | Rev <n>]
```

| Segment | Meaning | Examples |
|---|---|---|
| `CSL` | Issuer. Always CSL for CSL-authored documents. Client-convention prefixes are used when the client's system requires them (see 1.3). | `CSL` |
| `PROG` | Program code. Short, stable, assigned once per engagement. | `W77` (ASML W77 IRO), `BUH` (Brown University Health), `OSUMC`, `PNS` (Pensacola airport pursuit), `HUN` (DASNY Hunter) |
| `FAM` | Document family (table below). | `WKR`, `PLN`, `MEM` |
| `ID` | Sequence: ISO week number for weekly families; `yymmdd` for dated series; zero-padded sequence (`001`) for numbered series. | `40`, `260925`, `014` |
| `ED` | Edition letter for weekly families only: `A` Monday Look-Ahead, `B` Wednesday Mid-Week, `C` Friday End-of-Week, `D` supplement. | `40B` |
| Revision | `R<n>` for data files, notices, and same-week reissues; `Rev <n>` for controlled documents (SOPs, PM packages, scope packages, assessments). First issue is `R0` / `Rev 0`. | `R1`, `Rev 0` |

Week numbers are ISO 8601 weeks (Monday start). `WKR-40` = Mon 09/28/26 to Fri 10/02/26. Check with `date -d 2026-09-28 +%V` before numbering; do not count weeks by hand.

### 1.1 Families in use (2026)

| FAM | Family | ID type | Owner skill | Notes |
|---|---|---|---|---|
| `WKR` | Weekly report series | ISO week + edition | `csl-weekly-reporting` | `CSL-W77-WKR-40A/B/C`; `D` for supplements (e.g., 32D) |
| `PLN-SUM` | Program (Planon / asset-program) weekly critical summary | `yymmdd` + `R<n>` | `csl-asset-data-cmms` | `CSL-W77-PLN-SUM-260828 R1` supersedes `R0` |
| `PLN-EWO` | Program end-of-week edition carrying the gate register (G-nn) | `yymmdd` | `csl-asset-data-cmms` | `CSL-W77-PLN-EWO-260925` |
| `CTRW-<rig>` | Test-rig telemetry summaries | `yymmdd` | `csl-data-pipeline` | `CSL-W77-CTRW-TR7-260827` |
| `PM-<sys>` | PM task packages | `001` sequence | `csl-technical-docs` | `CSL-W77-PM-TRC-001` |
| `MEM` | Executive memo / decision memo | `yymmdd` | `csl-executive-memo` | `CSL-W77-MEM-260919` |
| `GAP` | Gap analysis / program-record one-pager | `yymmdd` | `csl-executive-memo` | `CSL-W77-GAP-260819` |
| `SCP` | Scope package | WS or sequence + `Rev` | `csl-technical-docs` | `CSL-W77-SCP-WS04.01 Rev 0` |
| `ASM` | Assessment / technical report | WS or sequence + `Rev` | `csl-technical-docs` | `CSL-W77-ASM-WS02.02 Rev 0` |
| `OPT` | Options menu / intake checklist | `v<n.n>` | `csl-dashboard-kpi` | `CSL-W77-OPT-KPI v1.1` |
| `LOE` | Level-of-effort proposal | `yymmdd` | `csl-bd-pursuits` | `CSL-W77-LOE-260925` |
| `SOQ` / `RFQ` | Pursuit responses | solicitation number | `csl-bd-pursuits` | `CSL-PNS-SOQ-26-062` |
| `TRN` | Transmittal | `yymmdd-<seq>` | this skill | `CSL-W77-TRN-260826-01` |
| `UPL` | Upload / import data file (when client naming is not mandated) | `yymmdd` + `R<n>` | `csl-asset-data-cmms` | see 1.3 for client-mandated names |

Minutes and agendas are numbered as a meeting series, not with the CSL prefix: `Minutes #016`, `Agenda #017`, items `016-001`. The series number belongs to the meeting, whoever issues it; when CSL audits minutes issued by a counterpart, the audit memo is `CSL-<PROG>-MEM-<yymmdd>` and cites the minutes number.

### 1.2 Client-convention documents

Some families follow the client's site convention because they live in the client's document system:

| Convention | Format | Example | Rule |
|---|---|---|---|
| Site SOP | `<SITE>-SOP-<SYS>-<nnn> Rev <n>` | `W77-SOP-PCW-040 Rev 0`, `W77-SOP-GFC-001 Rev 0` | Author field names CSL; approver is the client owner; `Rev 0` first issue; whole-number revisions on approved changes |
| Legacy site SOP | `<SITE>-IRO-SOP-<nnn> Rev <n.n>` | `W77-IRO-SOP-014 Rev 1.0` | Retained for documents already in circulation; do not start new numbers in this format |
| Facilities / engineering notice | `FM-<SITE or AREA>-<TOPIC>-<mmdd> R<n>` | `FM-W77-UTM-0903 R1`, `FM-DUV-LOG-0828` | `mmdd` is the condition date, not the issue date; `R<n>` for updates; a new notice supersedes an earlier one by stating `supersedes FM-...` on its face |
| Client project intake | `IN <nnnnn>` | `IN 12896` | Never renumber; cite as issued |
| Client permit | site permit number | `53782` (W77 SIPP), `200-0142` (generic SIPP) | Cite the permit number and the gate count (`37/40`) |
| Workstream tasks | `WS-<nn>.<nn>[.<nn>]` | `WS-22.08`, `WS-12.01` | One format per tracker; flag mixed formats (`WS209`) as a data defect |
| Client-mandated import files | client template name + date + `R<n>` | `ASML_W77_..._August_24_2026_R3.csv` | Keep the client's name pattern; append `_R<n>`; never rename an import template |

---

## 2. Revision rules

1. `R0` / `Rev 0` is the first issue. A document without a revision marker is a draft.
2. Same-day reissue with substantive change increments the revision (`WKR-36A` revised same day → `WKR-36A R1`; `PLN-SUM-260828 R1 supersedes R0`). A typo-only fix reissues under the same revision with a corrected time in the transmittal, and the transmittal says so.
3. The superseding document states what it supersedes on its cover or control block. The superseded file is not deleted; it is moved to `_superseded/` in the same folder with its revision intact.
4. A revision never changes the document number, program code, or family. If the scope changed enough to need a different number, it is a new document that references the old one.
5. Controlled documents (SOPs, PM packages, scope packages, assessments) carry a revision history table. Data files carry a change log on the `Control` sheet.
6. Editions (A/B/C/D) are not revisions. `WKR-32D` is a supplement to `WKR-32C`, not a revision of it.
7. Version strings (`v1.1`) are for living documents that are expected to iterate weekly (options menus, code schemes, dashboards). Record the change that moved the version (`v1.1: G3 corrected to CAAR`).

---

## 3. File naming

```
<DOC-NUMBER>_<yyyy-mm-dd>[_<short-descriptor>][_R<n>].<ext>
```

| Deliverable | File name |
|---|---|
| Weekly report | `CSL-W77-WKR-40B_2026-09-30.pdf` |
| Same-day reissue | `CSL-W77-WKR-36A_2026-08-30_R1.pdf` |
| Program summary | `CSL-W77-PLN-SUM-260828_R1.pdf` |
| SOP | `W77-SOP-PCW-040_Rev0_2026-08-04.docx` and `.pdf` |
| Scope package | `CSL-W77-SCP-WS04.01_Rev0_2026-08-14.docx` |
| Memo | `CSL-W77-MEM-260919_GFC-structure-record.pdf` |
| Upload file (client-mandated) | `ASML_W77_Assets_Template_POPULATED_2026-08-26.xlsx` (client pattern kept) |
| Tracker workbook | `CSL-W77-TRK_Roadmap-IRO-Consolidated_2026-09-17.xlsx` |
| Minutes / agenda | `CSL_MeetingMinutes_016_2026-08-18.pdf`, `Planon-Weekly_Agenda-017_2026-09-08.pdf` |
| Chart image | `WKR-40C_fig03_mitigation-past-target.png` |

Rules: no spaces (use `_` between segments and `-` inside a segment); ISO dates in file names even when the document body uses `MM/DD/YY`; the document number first so folders sort by series; never `final`, `final2`, `latest`, `new`; never a person's name in a file name unless the document is about that person's role (e.g., a KPI options menu for a named recipient uses their surname: `CSL-W77-OPT-KPI_Koning_v1.1.pdf`).

---

## 4. Dates and times inside documents

| Where | Format | Example |
|---|---|---|
| Minutes, agendas, cover metadata, action registers | `MM/DD/YY` | `08/18/26` |
| Reporting windows | `Day MM/DD/YY` | `Mon 09/28/26 to Fri 10/02/26` |
| Document IDs | `yymmdd` | `260925` |
| File names | `yyyy-mm-dd` | `2026-09-25` |
| Pull timestamps in source notes | `MM/DD/YY HH:MM ET` | `09/25/26 06:40 ET` |
| Telemetry and logs | ISO 8601 with zone | `2026-08-26T06:57:00-04:00` |
| Narrative in client-executive prose | Month day, year on first mention, then `MM/DD` | `September 15, 2026 … the 9/15 frame` |

State the time zone once per document (ET for W77 and northeast programs; CT for Pensacola pursuits).

---

## 5. Transmittals

Every issued document to a client or contractor goes with a transmittal record, even when the transmittal is the email itself. Minimum content:

```
Transmittal CSL-W77-TRN-260826-01
Date/time: 08/26/26 3:22 PM ET
From: S. Schryba, CSL Consulting
To: B. Gannon, T. Dube (ASML); N. Grubler, E. Hubert (CSL)
Method: Microsoft 365 share (edit access) + email
Documents:
  1. ASML_WLT_077_Mechanical Asset Upload Sheet August 26 2026 CSL-Consulting.xlsx (237 rows)
  2. Copy-paste-ready CSV of item 1
Purpose: For import / For review / For approval / For record / For information
Response requested by: MM/DD/YY (or "none")
Notes: Meets the 48-hour commitment made 08/24/26 (Minutes #016, item 016-002).
```

Log transmittals in the program's transmittal register (Smartsheet or the `Control` sheet of the deliverable). The register is the first place to look when someone says "we never got that" or "that was work in progress"; a share log entry with edit access and a timestamp settles it.

Retain evidence of delivery: the share log (M365 "shared with" history), the sent email, the Teams post. Screenshot and file it with the transmittal when the stakes justify it.

---

## 6. Where files live

| Content | Location | Rule |
|---|---|---|
| CSL working files, drafts, factory code | CSL server / CSL SharePoint, program folder | Not client data; may contain CSL-internal notes |
| Client program data, issued deliverables, upload sheets, turnover packages | Client SharePoint / document system | Client data stays on the client's tenant; a periodic compliance sweep moves anything that drifted onto the CSL server (W77 sweep assigned 09/08/26) |
| Live trackers | Smartsheet (or the client's chosen platform after a migration) | Attach issued PDFs to the row they report on; never attach drafts |
| Report factory outputs | `outputs/<PROG>/<FAM>/<yyyy>/` with `_superseded/` beneath | One folder per family; never overwrite an issued file |
| Meeting records | `<PROG>/Meetings/<Series>/` with agenda, minutes, transcript, audit memo together | Same meeting number on all four |
| Templates and brand assets | `csl-work-agent/skills/csl-brand/assets`, `csl-work-agent/templates` | Read-only for the agent; changes go through this package |

Client-side naming conventions that the client is standardizing (W77 example: `Enterprise_Site_Building` + project + discipline + document type, being written into future contracts) apply to files placed on the client tenant. When a client convention exists, use it for the file on their tenant and keep the CSL document number inside the document.

---

## 7. Provenance checks on documents received

Before relying on or responding to a document someone else issued, check:

1. **File properties.** Title, subject, author, company, created/modified dates. A document whose properties still carry another document's title and number was made by Save-As and may carry inherited content, headers, or numbering (the `W77-SOP-GFC-001` draft carried `W77-SOP-PCW-040` in its properties). Note it in the review; it is a controlled-document defect on their side and a fact for the record.
2. **Revision and supersession.** Is this the current revision? Does it say what it supersedes? Does an earlier version still circulate?
3. **Byte-identity.** For data exports, hash them (`md5sum`). A re-sent file with an identical hash is not a new export, whatever the email says.
4. **Truncation.** Check file size against the sender's stated size or page count; a PDF cut at exactly 2 MiB in every copy is a transfer artifact, and the fix is a re-send, not a review of the partial.
5. **Attribution.** Who is named as author, reviewer, approver, and were they actually involved? Attendance tables that mark absent people present, or approver fields filled without approval, are corrected in writing the same day.

---

## 8. Retention and the program record

- Keep every issued revision for the life of the program plus the client's retention period (assume seven years when unspecified).
- Keep pull data (the CSV/JSON snapshot each report was built from) with the report, so the report can be reproduced and defended.
- Keep transcripts, recordings, and AI meeting notes with the minutes they informed; they are the evidence when minutes are disputed.
- Keep record-correction emails and their replies with the document they correct.
- Nothing in the record is edited after issue; corrections are new documents that cite the old.

---

## 9. Quick checks before issue

- Number formed correctly and not already used (grep the outputs folder).
- Revision marker present; supersession stated if applicable.
- File name matches Section 3.
- Cover / control block complete (see `csl-brand`).
- Transmittal drafted and register row ready.
- File properties set for this document.
- Pull snapshot saved alongside.

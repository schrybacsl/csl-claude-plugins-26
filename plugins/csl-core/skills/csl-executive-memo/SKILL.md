---
name: csl-executive-memo
description: >
  Stand-alone executive documents: decision memos, program-record memos, record-correction and
  transcript-audit memos, gap-analysis one-pagers, escalation memos, position papers, and cover
  memos for proposals or data deliveries. Use it whenever a finding must stand on its own outside
  the weekly report, or someone says "write it up", "put this on the record", "memo to the client",
  "one-pager", "gap analysis", "document the disconnect", "decision memo", or "position paper", and
  whenever a counterpart document must be answered formally rather than by email. Engineering
  notices (FM- format) belong to csl-technical-docs.
---

# CSL Executive Memo Family

A memo exists because a finding, decision, or discrepancy must survive on its own: it will be attached to a tracker row, cited in minutes, forwarded up a client hierarchy, or read in eighteen months by someone reconstructing what happened. It is short, dated, numbered, and built on documents.

---

## 1. Bottom line

One to two pages (gap analysis: one landscape page). Bottom line first, findings numbered, actions in a table with owners and dates, basis documents listed by number and date. Numbered `CSL-<PROG>-MEM-<yymmdd>` (gap analysis `GAP`). Third person for records, first person plural for recommendations. No adjectives about people; dates and documents about events.

## 2. Inputs

The documents the memo rests on: minutes and their numbers, transcripts with timestamps, emails with dates and times, transmittals and share-log entries, tracker snapshots with pull times, issued reports and notices. Pull or open each one; quote the exact line where the finding depends on wording. A memo that cites a document the author has not opened is not issuable.

## 3. Memo types and their shapes

| Type | Trigger | Body shape |
|---|---|---|
| Decision memo | A choice the client or CSL leadership must make (e.g., whether QR label printing waits for a written code spec) | Decision requested · Options with cost/schedule/risk · Recommendation and rule · Deadline and consequence of no decision · Basis |
| Program-record memo | A ruling, scope change, or delivery must be fixed in the record (e.g., functional-code structure ruled four ways in 19 days with no versioned spec) | Chronology table (date, source document, what was stated) · What is currently in force and what is open · Effect on delivered work · Request |
| Record-correction memo | A counterpart's minutes or recap misstate CSL's delivery, attendance, or position and the email reply (csl-client-comms) is not enough | Item-by-item: their record says / the record shows / evidence · Corrections requested · Attachments |
| Transcript-audit memo | Minutes arrive from a counterpart; CSL audits them against the transcript | Attendance check · Item-by-item conformity (matches / omits / adds / attributes differently) with timestamps · Items missing from the action register · Corrections requested with due date |
| Gap-analysis one-pager | A process disconnect harmed the work (e.g., a two-week build proceeded while hierarchy changes were being discussed in sidebar meetings the builder was not told about) | Landscape page: left column timeline; right column gap statement, impact (days, records, rework), record request; footer "Program record" |
| Escalation memo | A RED condition needs a decision above the working level | Condition · Tier and rule · Exposure quantified · What has been done · Decision requested · Owner and date · Attachments |
| Position paper | CSL's technical or commercial position on a contested question (e.g., structure-by-system versus search-based grouping for a CMMS hierarchy) | Question · Positions held (attributed) · CSL position and reasoning · Consequences of each · Recommendation |
| Cover memo | Accompanies a proposal, data delivery, or options menu | What is attached · What changed since the last version · What is asked and by when |

## 4. Output specification

```
[Logo]                                              MEMORANDUM
CSL-W77-MEM-260919 | Rev 0 | 09/19/26
To: B. Gannon, ASML CRE            From: S. Schryba, CSL Consulting
Cc: E. Hubert, CSL; T. Dube, ASML  Re: Functional-code structure — program record and open decisions
Distribution: as addressed          Classification: Program record

1. Bottom line  (one paragraph)
2. Findings  (numbered; each: fact, date, source document)
3. Actions requested  (table: Action | Owner | Due | Tier (rule))
4. Basis  (documents relied on: number, title, date, where filed)
Signature line: S. Schryba, Owner's Representative, CSL Consulting
```

Page anatomy per `csl-brand/references/document-anatomy.md` Section 3. Render with `docx_styles.py` and issue PDF; file per `csl-document-control`.

## 5. Voice

Declarative, dated, sourced. "Minutes #020, item 020-001, records the structure as confirmed at eight levels; the 09/29 recap states 'up to seven'." Not "the client keeps changing its mind." Quantify impact in records, days, dollars, reprints. Attribute every statement to a person by role and date or to a document by number. Recommendations in first person plural with the rule that drives them.

## 6. Worked example (program-record memo, condensed)

**Bottom line.** The functional-code structure governing 972 delivered asset records has been ruled four times since 08/24/26 without a versioned specification. Recoding, QR label printing, and the 10/30/26 Loops + AHS deadline all depend on it. We request a written, versioned spec by 10/03/26 and confirmation of which delivered sets are retroactively in scope.

**Findings.** 1. 08/24/26 coding meeting (Schryba, client data owner, program lead, APM): six-level scheme, `ASML_WLT_077_` prefix, code resets at the unit; reference Functional Code Structure v1.1 (to be posted). 2. 09/10/26 "Change Decision" email (APM to client data owner, cc CSL): structure to extend past six levels; standard-asset classification no longer the filter. 3. Minutes #020 (issued 09/23/26), item 020-001: eight levels "confirmed verbally on the call, no further written confirmation required". 4. 09/29/26 recap of a client-side conversation: levels "up to seven"; resubmission on unaltered templates required. 5. Delivered sets built to the convention in force on each issue date: 672 (R3, 08/24), 239 (v_5, 08/26), 61 (08/27), Loops PML (09/23).

**Actions requested.** Versioned spec issued (client data owner, 10/03/26, RED (R8)) · Retroactivity ruling per delivered set (program lead, 10/03/26) · QR printing held until both (all, standing).

**Basis.** Minutes #016, #017, #020/#021; email 09/10/26; recap 09/29/26; transmittal CSL-W77-TRN-260826-01; PLN-SUM-260828 R1.

## 7. Failure modes

Adjectives and motive · a memo longer than the reader's patience (two pages is the ceiling; appendices carry the rest) · findings without a source document · a request without a date · answering a discrepancy in the weekly report instead of on the record · issuing without a number · mixing a decision memo with a record memo (one purpose per memo).

## 8. Pre-issue checklist

Number and revision · every finding sourced · every action has owner, date, tier · bottom line answers "so what" · attachments listed and filed · brand QA · transmittal drafted.

## Files in this skill

- `templates/executive-memo.md` — the memo skeleton with a populated example row per section.
- `templates/gap-analysis-onepager.md` — landscape one-pager layout.
- `templates/transcript-audit-memo.md` — item-by-item conformity table.

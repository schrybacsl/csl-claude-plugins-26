---
name: csl-meeting-records
description: >
  Agendas, CSL-branded minutes from transcripts or notes, action registers carried meeting to
  meeting, transcript audits of minutes issued by others (attendance, attribution, omissions,
  decisions recorded as confirmed), agenda audits, and the 48-hour correction workflow. Use it
  whenever a transcript, Teams recording, AI meeting notes, or counterpart minutes arrive; whenever
  someone asks for "minutes", "agenda", "action items", "what did we agree", "check these minutes",
  or "carry the open items"; and before any recurring meeting such as an OAC, program meeting, or
  1:1.
---

# CSL Meeting Records

Minutes are the program's legal memory. Whoever issues them defines what was decided. When CSL issues, the record is complete and attributable; when a counterpart issues, CSL audits within the 48-hour correction window so the record does not drift.

---

## 1. Bottom line

Before the meeting: an agenda built from the open action register and the report docket. After: minutes within two business days, every item numbered `[meeting]-[seq]`, every action with owner and date, decisions recorded with who stated them and whether written confirmation is still owed. When someone else issues: audit against the transcript the same day, send corrections within 48 hours (csl-client-comms), file the audit memo (csl-executive-memo).

## 2. Inputs

Transcript (Teams VTT/DOCX, Zoom, pasted), recording, AI meeting notes (treated as a secondary source; the transcript governs), the previous minutes and action register, the agenda, the current report docket, the attendee list confirmed by the operator (the legacy skill requires the user to confirm actual attendees; keep that rule). Note transcript defects: coverage (minutes covered of total), diarization failures (every line labeled one speaker), gaps.

## 3. Method

**Agenda (issue the business day before).** Pull the open action register and the latest report docket. Every open item older than one meeting appears under "Carried items" with its age. Add decision items (mark Decide / Inform / Discuss), owners, time boxes, pre-reads by document number. Check the counterpart's agenda when they issue: list what the record shows open that the agenda omits (e.g., an agenda with two items while eight standing confirms, an import failure root cause, and four emailed questions remain open) and send the additions before the meeting.

**Minutes (CSL issuing).** Parse per the legacy parsing guide: every named speaker attended; referenced-absent marked; one action item per substantive topic minimum; language elevated to formal third-person past tense; profanity and filler removed. Add these package rules: decisions carry the speaker (by name and organization) and the words "stated on the call" until a written confirmation exists, with a follow-up item to obtain it; scope, date, or structure changes are recorded as changes with the prior baseline named; commitments carry the exact deliverable, date, and time zone; items closed on the call cite the evidence (transmittal number, share timestamp). Render with the legacy `generate_minutes.py` or the brand-compliant equivalent (status colors per `csl-brand` 1.4 replace the legacy red).

**Action register.** One register per meeting series (Smartsheet or the minutes' summary table): ID, title, description, responsible, open date, due date, status (Open / Closed / In Progress / Record), last update note. Closed items stay visible for one meeting, then archive. The register is the source for the next agenda and for the weekly report's program-thread page.

**Transcript audit (counterpart issuing).** Attendance table against the transcript (a person on PTO marked present is a correction; an absent decision-maker marked present changes what the minutes can claim). Item-by-item conformity: matches / omits / adds / attributes to a different speaker, with timestamps. Decisions recorded as "confirmed" that the transcript shows as stated by one party without CSL assent are flagged; a minute that waives a written-confirmation requirement CSL had requested is flagged RED (R7). Items raised in the meeting but missing from the action register are listed. Findings go in the audit memo and the correction email; the weekly report cites the memo number, not the argument.

**Corrections workflow.** Within 48 hours of issue (the minutes disclaimer window): reply-all to the issuing email with the numbered corrections; ask for a reissued minutes number with `R1`; file the request with the minutes. If not reissued, the next agenda carries "Corrections to Minutes #nnn outstanding" as an item.

## 4. Output specification

Minutes: the legacy 4-page CSL template (cover with metadata and attendee grid; key action items summary; detailed log; disclaimer). Item numbering `016-001`. Dates `MM/DD/YY`. Footer `[Meeting description] | [Meeting date]`. Status vocabulary Open / Closed / In Progress / Record.

Agenda: one page; header block; timed items table (Time · Item · Lead · Purpose · Pre-read); Carried items block; Decisions needed block.

Audit memo: `csl-executive-memo/templates/transcript-audit-memo.md`.

Log entry form (detailed log narrative): "09/08/26 — The client data owner stated that asset-record and functional-code correction precedes QR tagging and that tagging is 'not in a rush', superseding item 017-003. S. Schryba confirmed the CSL gate (written code stability before printing). Tagging to ride the incoming maintenance provider's PM cycles; provider to be named by 09/11/26. Written confirmation of the structure requested; open."

## 5. Voice

Formal, third person, past tense, attributable. No characterization. Quote only where wording matters (a ruling, a commitment). Numbers, dates, document numbers throughout.

## 6. Worked example (audit findings, condensed, W77 Minutes #017 for the 09/01/26 meeting)

Coverage: transcript ~45 of ~60 minutes; diarization broken (all lines one label). Attendance: S. Schryba marked attended, on PTO (correction); program lead marked attended, transcript references him in absentia (correction). Items: 017-003 records the bulk upload as accepted with tagging to begin 09/08, while the transcript shows the import failed and was redone manually; root cause not stated (add as open item). Register omits: import root cause, gases and plumbing format risk, template-integrity verification, TCWP-1 tag collision. Corrections requested 09/08/26 on return; carried to Agenda #018 when not reissued.

## 7. Failure modes

Minutes without attendee confirmation · a decision written as agreed when one party stated it · closing an item without evidence · letting a counterpart's minutes stand uncorrected past 48 hours · agendas that ignore the register · arguing minutes in a weekly report · AI notes treated as the transcript.

## 8. Pre-issue checklist

Meeting number continues the series · attendance confirmed by operator · every topic has an item · every decision has a speaker and a confirmation status · every action has owner and date · prior register items dispositioned · rendered per template · disclaimer present · filed with transcript and agenda under the same number.

## Files in this skill

- `references/parsing-and-attribution.md` — parsing rules (from the legacy guide) plus the attribution and confirmation-status rules.
- `templates/agenda.md` — one-page agenda skeleton.
- `templates/action-register.md` — register schema and carry-forward rules.
- `templates/minutes-data.json` — the JSON schema the legacy renderer consumes, with one populated item.

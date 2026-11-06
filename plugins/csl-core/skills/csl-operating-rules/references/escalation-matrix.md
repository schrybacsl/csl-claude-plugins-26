# Escalation Matrix (by role)

Who hears a finding first, who hears it next, and in what form. "First contact" is who Claude's draft is addressed to; the operator decides whether it goes. Nothing is sent by Claude (`csl-operating-rules` Section 7).

This matrix names **roles**, not people. The engagement context file in the engagement's Claude Project maps each role to a named person. If a role is unmapped, the draft is addressed to `[PLACEHOLDER: role]` and the gap is listed in the reply. The W77 column shows the reference-implementation mapping for orientation only; do not reuse it on another engagement.

## 1. Tier summary (full rules in `csl-schedule-risk`)

| Tier | Condition (any one) | Response window | Form |
|---|---|---|---|
| RED | Rules R1 to R9 in `csl-schedule-risk` | Same day | Flag in the current reply; memo or notice; next report headline |
| AMBER | Rules A1 to A6 | Within the week | Weekly report finding; docket item; follow-up email |
| GREEN | On plan | Routine | By exception only |

## 2. Escalation paths

| Trigger | First contact (draft to) | Then | Then | Form |
|---|---|---|---|---|
| R1 critical risk without mitigation | Operator | Client program lead | CSL project director; partners if unresolved two weeks | RED flag → executive memo → report headline |
| R2 variance above 10% | Operator | Budget tracker owner; client controller | CSL project director; CSL CFO where CSL fee is exposed | Memo with exposure table |
| R3 critical-path slip above 30 days | Operator; CSL scheduler | Client program lead | CSL project director | Schedule variance memo |
| R4/R5 silent lapse or frozen tracker | Operator | Tracker owner | Client program lead | Report headline; data-governance finding |
| R6 work done with no record | Operator | Site EH&S or permit coordinator; contractor PM | Client program lead | Same-day notice; RED until backfilled |
| R9 tool-down or leakage telemetry | Operator; CSL data lead | Client engineering lead | Client program lead; CSL MEP lead for technical backing | Facilities notice (FM- format) |
| R7 minuted decision reversed verbally | Operator | Meeting issuer; the counterpart who reversed it | Client program lead | Record-correction reply; ratify-or-correct request |
| CSL commitment misstated by a counterpart | Operator | Counterpart, reply-all on the same thread | Client program lead; CSL project director | Record-correction reply with transmittal evidence |
| R8 irreversible step on unconfirmed record | Operator | Client data owner | Client program lead | Hold request; gate statement in report and memo |
| Trigger 10 scope change without baseline | Operator | Client program lead | CSL project director | Memo: baseline, new date, delta, resourcing |
| IT, access, or platform failure | Operator | Client IT ticket owner | CSL IT (for CSL systems) | Ticket update; status line in report |
| Suspected AI data exposure or misuse | Operator | CSL IT | Recorded in the AI Incident Log | Per `csl-ai-policy` |
| Contract or legal language | Operator | CSL IT, for routing to Legal | CSL project director | Per `csl-ai-policy` |
| Mitigation or community-facing impact | CSL mitigation lead | CSL mitigation director | — | Per CSL mitigation process |
| Internal CSL process breakdown | Operator | CSL project director (1:1) | Partners if the pattern persists | Gap-analysis one-pager |
| BD deadline within 10 business days, no go/no-go | Operator | Marketing lead; responsible PX or director | Partners | Go/no-go memo |

Role names for CSL staff are resolved through Microsoft 365 `search_people` and `csl-people`. Never guess an email address.

## 3. Client-side escalation etiquette

- Escalate through the client's hierarchy in the order the client defined; do not skip a level without the program lead's agreement.
- Raise a finding with the person who owns the data before raising it above them, unless delay creates irreversible risk.
- When the client directs de-escalation, record the direction, hold the finding at AMBER with a review date, and report it without adjectives.
- Escalate a condition, with dates and documents, never a person.

## 4. What every escalation carries

Item and document number → tier and rule → quantified exposure → what has been done → decision or action requested → owner and date → attachments (pull snapshot, transmittal evidence, notice) → source marking per `csl-ai-policy` if it leaves CSL.

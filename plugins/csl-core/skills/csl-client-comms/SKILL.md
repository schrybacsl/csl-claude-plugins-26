---
name: csl-client-comms
description: >
  All written communication a CSL owner's rep drafts: client and contractor emails, Teams posts,
  record-correction replies to minutes or recaps that misstate CSL's position, ratify-or-correct and
  written-confirmation requests, escalation and transmittal emails, IT ticket scoping, stakeholder
  registers, distribution and reply-all rules, subject lines, and signature blocks. Use it whenever
  someone says "draft a reply", "email the client", "respond to this", "correct the minutes", "get
  that in writing", "escalate", "who should be copied", or pastes a thread; whenever a counterpart
  attributes a date or scope to CSL; and whenever a ruling was given only on a call. Drafts only;
  nothing is sent without explicit instruction.
---

# CSL Client Communications

Correspondence is where the program record is made or lost. A counterpart's recap that goes unanswered becomes the record; a verbal ruling repeated in CSL's own email becomes the baseline; a correction sent a week late reads as an afterthought. This skill defines the voice, the situation-type calibration, and the fixed patterns for the emails and posts an owner's representative sends, with the record-correction reply as the pattern that matters most. Everything here produces a draft for the operator to send; nothing is sent by the agent (csl-operating-rules Section 7). Numbering and transmittals per `csl-document-control`; escalation paths per `references/escalation-matrix.md`; tiers per `csl-schedule-risk/references/tier-rules.md`; minutes and transcript audits per `csl-meeting-records`; names and titles per `csl-people`.

---

## 1. Bottom line / when this runs

| Request as spoken | Pattern | Section |
|---|---|---|
| "their minutes say we committed to", "that recap is wrong", "put this on the record" | Record-correction reply | 3.3 |
| "I don't remember confirming that", "the minutes say confirmed on the call" | Ratify-or-correct request | 3.4 |
| "they said it on the call", "get it in writing", "can we print yet" | Written-confirmation request | 3.5 |
| "he wasn't even there", "that wasn't me who said it" | Attendance / attribution correction | 3.6 |
| "they're saying our file was broken", "respond to this criticism" | Reply to criticism on the record | 3.7 |
| "escalate", "this needs to go to Bill", "who else needs to hear this" | Escalation email | 3.8 |
| "reply to IT", "scope the ticket", "what do they need from us to host it" | IT / ticket scoping email | 3.9 |
| "send the upload sheet", "transmit", "issue the memo" | Transmittal email | 3.10 |
| "set up a meeting", "invite for Tuesday" | Meeting invitation text | 3.11 |
| "post in Teams", "drop a note in the channel" | Teams post | 3.12 |
| "who should be copied", "who owns that decision" | Distribution rules; stakeholder register | 4.2, 4.4 |
| "fix the tone", "make this sound less stiff" | Tone adjustment; then the operator's tone-polish skill | 3.13 |

Three rules hold over everything: the output is a draft, with To, Cc, Subject, body, and attachments listed by document number; a tone change never alters a fact, figure, date, name, or action item; and a counterpart misstatement is corrected the same day, on the thread where it appeared (csl-operating-rules Section 6, trigger 7).

---

## 2. Inputs and pulls

| Input | Where | QA before drafting |
|---|---|---|
| The full thread | Outlook / Teams via the M365 connector, or pasted | Read from the first message, not the latest; note who started it, who has been added or dropped, and the time zone of each timestamp |
| The record being defended | Transmittal register, M365 share log ("shared with" history with timestamps), issued minutes and item numbers, transcript, tracker snapshot | Pull the entry; never recall it. Quote timestamps as the log shows them, with zone |
| The document being corrected | Counterpart's minutes, recap, email, or tracker row | Cite it by number and date; quote the misstated words exactly |
| Stakeholder register | `templates/stakeholder-register.md`, program copy | Decision rights and preferred channel of every addressee; last-contact date |
| Names and titles | `csl-people` for CSL; the register and the engagement context file (`csl-operating-rules` Section 5) for client and vendor | Every name verified; initials-style ("S. Schryba") only in action lists |
| Calendar | M365 calendar | Due dates fall on business days; both zones stated where the audience spans ET and CT |
| Escalation path | `references/escalation-matrix.md` | Who hears it first, who next; the client's own hierarchy order |

If the evidence cannot be pulled in the session (share log unavailable, transcript not yet posted), say so in the draft's cover note and mark the affected sentence "confirm before sending"; do not soften the correction to cover the gap.

---

## 3. Method

### 3.1 Voice profile

Write as a senior construction professional and owner's advocate in the Northeast professional register: understated, competent, collegial. Relationship-aware with long-term counterparts, because clients, design teams, and contractors recur across engagements, and firm on the position when the situation calls for it. First person plural for CSL positions ("we recommend", "we will hold"); first person singular only for the operator's own observations ("I don't have that confirmation in my notes"). Plain human voice: short declarative sentences, active verbs, numbers with units and dates, no jargon a client executive would have to decode. No performative openers or closers ("Great question!", "I hope this email finds you well"), no filler, no adjectives about people, no motive. Client-executive prose carries no dash constructions; use a period, comma, or colon.

The draft's substance comes from this skill. Rhythm and openers are polished last with the operator's tone-polish skill (installed as `audhd-email-humanizer`), which changes tone only; run it after the pre-send checklist, not before, so the facts are locked when the polish happens.

### 3.2 Situation-type matrix

Choose the type before writing a word; it sets warmth and assertiveness independently. Openers and closes below are exemplars in the house voice, not mandatory text.

| Type | Warmth | Assertiveness | Opening exemplar | Close exemplar |
|---|---|---|---|---|
| Routine client update | Medium-high | Low | "Quick update on the mechanical set ahead of Friday's report." | "Full detail in WKR-40C Friday; say the word if you want anything pulled forward." |
| Meeting follow-up | Medium | Low-medium | "Thanks for the time today. Three items came out of it; owners and dates below." | "I will carry these on Tuesday's agenda unless they close sooner." |
| Transmittal | Low-medium | Low | "Transmittal CSL-W77-TRN-260826-01 attached: the mechanical upload sheet (237 rows) and the copy-paste CSV." | "Response requested by 08/28/26 so the import can run this week." |
| Change-order or scope pushback | Low | High | "We have reviewed PCO-007 and are not in a position to recommend approval as submitted; four comments follow." | "Once comments 1 to 3 are addressed we can turn the recommendation around in a day." |
| Schedule / deadline pressure | Medium | Medium-high | "The 10/30/26 Loops and AHS date is 22 business days out and two inputs are still open on the client side." | "If items 1 and 2 close by 10/07 the date holds; after that we re-plan and say so in Friday's report." |
| Dispute or claim notice | Low | Very high | "CSL Consulting, on behalf of the Owner, provides notice that the work described below does not conform to the approved submittal." | "Sincerely, [full name, title], CSL Consulting" (no warmth tokens anywhere in the letter) |
| Vendor / sub management | Medium | Medium | "Following up on the WS-22.05 quotes due 09/30; we have not received them." | "Please confirm a revised date by close of business tomorrow; the requisition cannot raise without them." |
| Client relationship | High | Low | "Wanted to close the loop on the dashboard scoping before the week ends." | "Appreciate the time your team put into this. Talk Tuesday." |
| Internal CSL | High | Low | "Eric, quick one on W77." | "Thanks." |
| BD introduction | High | Low | "We attended the 09/01 pre-submittal for RFQ 26-062 and wanted to introduce CSL Consulting ahead of the submittal." | "Happy to walk through our comparable public work whenever convenient." |
| Record correction | Low-medium | High | "Correcting three points in the 09/21 reply so the thread record stays straight." | "Can we have items 1 and 2 by Wed 09/23? Happy to walk the share log on a call." |
| Escalation | Medium | High | "One item needs your decision this week: the QR print date is set and the code structure is not yet confirmed in writing." | "Recommend option 1; a decision by 10/02 keeps the print date." |

### 3.3 Record-correction reply (the most important pattern)

**Trigger.** A counterpart's minutes, recap, email, or tracker misstates CSL's position, a delivery date, delivered scope, attendance, or attributes a commitment CSL did not make. csl-operating-rules Section 6 trigger 7 fires; tier AMBER (A6) while open, RED (R7) if the misstatement reverses a minuted decision.

**Rules.**

1. Same day. A correction a week later reads as an afterthought and the misstatement has already been forwarded.
2. Reply-all on the same thread, so the correction sits with the misstatement for everyone who saw it. Never a new thread, never a private note, never the next weekly report (csl-operating-rules Section 8).
3. Lead with the specific correction, in three parts: what the record says (quoted), what the record should say, and the evidence (transmittal number, share-log timestamp, minutes item, email date).
4. No adjectives, no motive. Do not characterize the counterpart, the error, or the reason for it. State the record.
5. Re-ask every open confirmation in a numbered list, because a thread that disputes delivery is also a thread where the open questions have been sitting unanswered.
6. Close with the action requested and the date.
7. Keep it short. Three corrections and five re-asks fit in 180 words; anything longer belongs in a memo (`csl-executive-memo`) that the email attaches.

**Evidence hierarchy.** Share log with edit-access timestamp > transmittal number and time > sent email header > minutes item number > transcript timestamp > tracker cell history. Cite the highest available; quote the timestamp as the system shows it.

**Variants by what was misstated.**

| Misstatement | Lead sentence form | Evidence to cite |
|---|---|---|
| Delivery called incomplete or "work in progress" | "The [file] was shared [date time zone] with edit access and marked completed." | Share log entry; transmittal number; row count |
| Delivery date moved | "The [file] was delivered [date], not [date stated]; transmittal [number]." | Transmittal register; sent header |
| Scope attributed to CSL that CSL does not hold | "[Scope] came off CSL's list on [date] per Minutes #[nn] item [nn-nnn]." | Minutes item; scope ruling document |
| Commitment CSL did not make | "CSL did not commit to [x] on [date]; the transcript at [hh:mm:ss] records [what was said]." | Transcript timestamp; agenda item |
| Decision recorded as CSL's that was the counterpart's | "The direction to [x] was given by [role] on [date]; CSL recorded it and requested written confirmation [date]." | Confirmation request email; open-confirm register row |
| Tracker row edited to show a different status or date | "Row [id] read [value] at the [date] pull and reads [value] today with no change note; cell history shows the edit on [date]." | Cell history; pull snapshot hash |

**After sending.** Log the discrepancy in the program record (open-confirm register or the meeting series file) with the correction's date; keep the correction and any reply with the document it corrects (`csl-document-control` Section 8); cite the correction in the next report rather than re-arguing it. If no reply arrives in five business days, the item is AMBER (A5) and the follow-up is one line: the original correction date and the question still open. Skeleton: `templates/record-correction-reply.md`. Worked example: Section 6.

### 3.4 Ratify-or-correct request

**Trigger.** Minutes record a decision as "confirmed on the call" and the operator does not recall it being confirmed, or recalls it stated as a direction with the written spec still to come.

**Pattern.** A short note to the meeting issuer (W77: the CSL APM who issues the Planon minutes), copied to the thread the minutes went to, asking for one of two outcomes: ratify the item with the transcript timestamp, or correct it to "stated on the call; written confirmation requested [date]". Give a date that lets the minutes issue clean. State what CSL does in the meantime (holds to the last written convention).

> Subject: W77 | Planon Minutes #021 (number illustrative) | Item on structure depth: ratify or correct
>
> Noah, item 4 records the functional code structure at eight levels as "confirmed on the call" on 09/22. I don't have that confirmation in my notes; I have it stated by the client data owner as a direction, with the versioned spec still to come. Could you either cite the transcript timestamp where it was confirmed, or amend the item to "stated on the call; written confirmation requested 09/22/26"? By Thursday would let the minutes issue clean. Our code sets stay on the 08/24 written convention until the spec exists. Thanks, Steven

Template: `templates/ratify-or-correct.md`.

### 3.5 Written-confirmation request

**Trigger.** A ruling, date, scope change, or acceptance given on a call, in a hallway, or in a chat, that CSL's own documents would otherwise have to carry as fact (csl-operating-rules Section 8, "verbal rulings").

**Pattern.** Restate the ruling as heard, with speaker role and date; ask for it in writing in a named form (a versioned spec, a one-line email, a minuted item); give a due date; state the consequence of not receiving it in operational terms, never as a threat. The consequence is the hold CSL will apply and why the hold protects the owner.

> On the 09/29 call the structure was stated as up to seven levels. We need that in writing, as a versioned Functional Code Structure spec or a one-line email confirming the depth and the version number, by Fri 10/02/26. Until it arrives we will hold QR label printing, because the code prints on the label and a later change means reprinting and re-walking every tagged asset. Code sets continue on the 08/24/26 written convention in the meantime.

The request date goes on the open-confirm register the same day; unanswered after five business days it is AMBER (A5), and RED (R8) the moment a print, cut, or order is scheduled against it. Template: `templates/confirmation-request.md`.

### 3.6 Attendance and attribution corrections to minutes

Handle as a factual correction with the transcript reference, in one or two sentences per item, on the thread the minutes went to, the day they arrive:

> Two corrections to Minutes #021 (number and items illustrative) before they file. Attendance: the table marks one CSL attendee present on 09/22 who was out of the office that day (out-of-office reply on this thread; not on the transcript participant list). Attribution: the remark on the CHAMPS template class at 00:41:10 is attributed to the CSL PM; the transcript shows the client import owner. Please amend both and reissue, or note the corrections in #022.

Attendance matters because the table is who can be held to the decisions; attribution matters because a ruling attributed to CSL becomes CSL's position. Full transcript-audit method in `csl-meeting-records`.

### 3.7 Responding to criticism of CSL work on the record

**Trigger.** A counterpart states, on a thread or in minutes, that a CSL deliverable was defective, late, incomplete, or "work in progress".

**Pattern.** Acknowledge the specific claim in its own words; ask for the specific defect and the date it was found and communicated; state what was delivered and when, with the evidence; offer the fix path with a turnaround; no defensiveness and no counter-criticism. The reader should see a firm that wants the defect fixed and a record that shows what was delivered.

> Your reply on this thread says the populated template arrived with the auto-populate and taxonomy machinery stripped and had to be rebuilt. We want to fix that if it happened. Which columns or sheets were rebuilt, and when was that communicated to us? Our record: the mechanical set was populated on the CHAMPS template CSL holds, data rows only, and shared with edit access 08/26/26 3:22 PM ET (CSL-W77-TRN-260826-01); the root cause stated on the 09/29 call was that unaltered templates are required. If the file on your side differs from that, name the template of the six that applies and we will repopulate the 237 rows onto the unaltered copy within 48 hours of receiving it.

Import triage itself is in `csl-asset-data-cmms` 4.10; the email asks the two questions that triage needs (what was rebuilt, when communicated) and offers the fix.

### 3.8 Escalation email

Escalate a condition, never a person (`references/escalation-matrix.md` Section 3). Structure, in order: condition (item and document number); tier and rule; exposure quantified (dollars, days, records, gates); what has already been done, with dates; decision or action requested; owner; date; attachments by number. The reader should be able to decide from the first two sentences and verify from the attachments.

Client hierarchy etiquette, applied to the addressing:

| Situation | To | Cc | Why |
|---|---|---|---|
| Data or record issue owned by a counterpart | The data owner | CSL Project Director | Raise it with the person who owns the data before anyone above them |
| Same issue, unresolved after the response window, or an irreversible step scheduled | Client program lead | Data owner; CSL Project Director | The lead hears it from CSL before hearing it from the field; the owner stays on the thread |
| Client program lead has directed de-escalation | Client program lead (acknowledgment) | CSL Project Director | Record the direction; hold the item at AMBER with a review date; report without adjectives |
| CSL-internal process issue | CSL Project Director, 1:1 | None | Internal first; a gap-analysis one-pager if a pattern persists |
| Skipping a client level | Only with the program lead's agreement, stated in the email | | The client defined its own order; the exception is theirs to grant |

Exposure is written in the owner's units: records to recode, labels to reprint, days to a hard date (10/30/26 Loops and AHS hierarchy), dollars on a blocked PO, gates open on a permit. Template with a populated example: `templates/escalation-email.md`.

### 3.9 IT / ticket scoping email

**Trigger.** A CSL-built system (dashboard, pipeline, report factory) is moving onto the client's platform, or the client's IT has asked what a ticket should contain.

**Pattern.** Define the ticket scope in numbered items IT can size in one pass; name what CSL will supply for each; separate this ticket from later phases; ask who owns the ticket on their side and the review cadence. The W77 case (reply of 08/20/26 to the client's Controls & BMS manager, defining the ticket for moving the Roadmap Insight Dashboard onto the client's server): 1 security review of the application, with the sanitized deployment template and dependency list supplied by CSL; 2 transfer method, repository hand-off or container image at IT's preference; 3 hosting, Azure App Service preferred; 4 DNS name, TLS certificate, and API egress to the data sources (Smartsheet API now, Microsoft Graph after the SharePoint migration); 5 Entra ID app registration including the CSL author as a contributor so updates continue after transfer. Noted for later phases and kept out of the ticket: the BMS data layer, the test-rig telemetry connection, and the Copilot linkage. Full text: `templates/it-ticket-scoping.md`.

### 3.10 Transmittal email

The email is the transmittal record when no separate form exists (`csl-document-control` Section 5). Body carries: transmittal number; document numbers with revision; what changed since the last revision (one line each); purpose (for import / review / approval / record / information); response requested by, with date; attachments listed with row counts or page counts; the commitment it meets, by minutes item, when one exists. Share files from the client tenant with edit access where import or edit is expected, and name the share in the email so the log and the email agree. Template: `templates/transmittal-email.md`.

### 3.11 Meeting invitation text

Body of the calendar invite, in this order: purpose in one sentence; decisions needed, numbered; pre-reads with document numbers and tenant links; time with zone for every audience present (W77 Planon weekly: Tue 3:00 to 4:00 PM ET, 2:00 PM CT); agenda number when the meeting is a series (`Agenda #017`); required and optional attendees. No agenda text in the invite beyond the decisions list; the agenda is its own numbered document (`csl-meeting-records`).

> Subject: W77 | Planon weekly | Agenda #017 | Tue 09/08/26 3 PM ET
>
> Purpose: close the structure-depth question and set the gases and plumbing delivery date.
> Decisions needed: 1. Which Functional Code Structure version governs code sets issued after 09/08. 2. Delivery date for the gases and plumbing set. 3. Owner and date for the TCWP-1 tag-collision ruling.
> Pre-reads: Agenda #017 (tenant link); CSL-W77-PLN-SUM-260904 R0; open-confirm register rows 1 to 5.
> Time: Tue 09/08/26 3:00 to 4:00 PM ET (2:00 to 3:00 PM CT). Teams link below.
> Required: client program lead, client data owner, CSL PM, CSL APM (issuer). Optional: CSL Project Director, CSL on-site PM.

The pre-read numbers above are illustrative of the numbering rules; confirm each against the issued file before the invite goes out.

### 3.12 Teams posts

One topic per post. The decision or ask is the first line; context follows. Document numbers, never "the latest file". Tag the owner of the ask; give the date with zone. Decisions that belong in minutes are not taken in a thread; the post points to the agenda item where the decision will be recorded. Screenshots of tables are not posted when the document number and link suffice. Posts are drafts until the operator posts them.

> @[client data owner] Ask: the importer's rejection log behind the 09/29 root cause (unaltered templates required), by Thu 10/01 EOD ET. Context: CSL-W77-TRN-260826-01 (237 rows) was built on the CHAMPS template CSL holds; triage step 0 needs the log before we test anything. Decision on template class stays on Tuesday's agenda (item 1), not here.

Three lines, one ask, one date with zone, one document number, and the decision routed to the minutes.

### 3.13 Tone adjustment

When asked to soften, warm, tighten, or formalize a draft: change openers, closes, sentence rhythm, connectors, and register. Do not change facts, figures, dates, names, action items, the ask, the due date, or the position. "Soften the tone" never means "soften the position"; if the request would require the position to move, say so and offer two drafts (same position, two registers). Then hand the draft to the operator's tone-polish skill for the final pass.

| Register change | Allowed | Not allowed |
|---|---|---|
| Warmer | Add a one-sentence opener that acknowledges the context; offer a call | Remove the hold, the date, or the consequence |
| Tighter | Cut connectors and repeated context; merge paragraphs | Cut a correction, a re-ask, or an evidence citation |
| More formal | Full names and titles; "CSL Consulting" on first reference; no contractions | Passive voice that hides the actor ("it was decided") |
| Less formal | Contractions; first names; shorter close | Vague dates ("soon", "next week") in place of MM/DD/YY |

### 3.14 After the operator sends

The agent does not send, but it closes the loop on the record once told the draft went: log the item (open-confirm register, meeting series file, or transmittal register) with the sent date; set the follow-up date (five business days for confirmations and corrections, the response-requested date for transmittals); note the tier and rule; and carry the item into the next Friday edition as a one-line citation ("correction sent 09/21/26; reply pending"), never as a restatement of the argument.

---

## 4. Output specification

### 4.1 Subject line

`[Program] | [Topic] | [Doc no. or date]`

| Situation | Subject |
|---|---|
| Transmittal | `W77 \| Mechanical asset upload sheet \| CSL-W77-TRN-260826-01` |
| Record correction | `W77 \| Planon asset uploads \| Record correction to reply of 09/21/26` (keep the original subject when replying; prepend nothing) |
| Confirmation request | `W77 \| Functional code depth \| Written confirmation requested by 10/02/26` |
| Escalation | `W77 \| QR print gate \| Decision requested by 10/02/26` |
| Meeting | `W77 \| Planon weekly \| Agenda #017 \| Tue 09/08/26 3 PM ET` |
| BD | `RFQ 26-062 \| CSL Consulting \| Pre-submittal follow-up 09/01/26` |

When replying on an existing thread, keep the thread's subject so the correction stays attached to the misstatement; the convention applies to threads CSL starts.

### 4.2 Distribution

- Cc the CSL lead (Project Director) on client-facing threads that carry a position, a correction, a commitment, or a date; routine transmittals to a standing list may omit them when the list already includes CSL leadership.
- Reply-all on the thread that carries the misstatement, the decision, or the request. Trimming recipients on a reply is a decision; state it if you make it ("dropping the vendor from this reply, internal to owner and CSL").
- Never drop the client program lead from a thread they started.
- BCC is never used for client work; a copy for the CSL record is a forward after sending.
- Standing lists per the engagement context file (`csl-operating-rules` Section 5) (W77 executive report, Planon weekly, dashboard transfer, Brown Health); verify membership each quarter against the register.
- Time zones stated for every time; both zones when the audience spans ET and CT.

### 4.3 Signature block

Plain text, no images, no brand colors, no quotations. Name; CSL title per `csl-people` with the engagement role after a vertical bar; CSL Consulting, LLC; 152 Middlesex Turnpike, Burlington, MA 01803; email; mobile from the operator's Outlook signature. Engagement line optional for client threads. Text and variants in `templates/signature-block.md`.

### 4.4 Stakeholder register

One row per person with decision rights or standing on the program. Columns: name | org | role | decision rights | what they care about | preferred channel | cadence | last contact | open items. Maintain it from the mailbox and the minutes; refresh last-contact dates before drafting any escalation. W77 excerpt as of 09/30/26 (roles from the W77 engagement context file (`engagement-context-W77.md` in the W77 Claude Project); refresh last-contact from the mailbox before use):

| Name | Org | Role | Decision rights | Cares about | Channel | Cadence | Last contact | Open items |
|---|---|---|---|---|---|---|---|---|
| B. Gannon | ASML CRE | Client program lead | Program scope, Planon realignment, dashboard views, BCA + IRO merge | Reliability record, executive visibility, 10/30/26 hierarchy date | Email; Planon weekly | Weekly | 09/29/26 Planon weekly | LOE proposal for the BCA + IRO merged source; REDM 10/01 |
| T. Dube | ASML | Client data owner (Planon structure and imports) | Functional code structure, template class, import acceptance | Import success on unaltered templates | Email; Planon weekly | Weekly | 09/29/26 (root cause stated) | Versioned structure spec (G-13); template class ruling; rejection log |
| E. Koning | ASML CRE | Client engineering lead; command dashboard recipient | KPI selection for his view | Utility and telemetry signals | Email | As needed | Per mailbox | KPI options menu v1.1 selections |
| P. Gorman | ASML | Technical reviewer (SOPs); WKR-B/C recipient | SOP approval | Procedure accuracy | Email | Per SOP | Per mailbox | W77-SOP-GFC-001 review |
| J. Vigo | ASML CRE | Controls and BMS manager | Dashboard hosting ticket on the client side | Security review, hosting path | Email; ticket REQ 999 / RITM5248681 | Per ticket | 09/14/26 scoping call thread | Entra ID app registration; hosting decision |
| J. de Boer | ASML CoE | Product Owner Building Automation | Deployment approach for the dashboard | Fit with the building-automation platform | Teams call; email | Per milestone | 09/14/26 scoping call | Deployment approach decision |
| A. Pfordresher | ASML CRE | CRE PM, IN 12896 | Change management on WS-22.08 | CAAR path | Email | Per project | Per mailbox | Design CAAR on the CARR tracker |
| E. Hubert | CSL | Project Director | CSL positions, fee, escalation | Record integrity, client relationship | Teams; weekly 1:1 | Weekly | This week's 1:1 | LOE review before issue |
| D. Wolf | CSL | On-site PM | Notices, budget tracker, WS co-ownership | Field record, blocked POs | Teams; on site | Daily | This week | WS-06.02 PO; FM-W77-UTM R2 |
| N. Grubler | CSL | APM; Planon meeting issuer | Agenda and minutes content | Clean minutes | Teams | Weekly | This week | Minutes corrections; intake tracker |

Template and maintenance rules: `templates/stakeholder-register.md`.

### 4.5 What the agent hands back

Every draft is delivered as: To / Cc (verified names) / Subject / body / attachments by document number / a two-line cover note stating the evidence pulled (log, timestamp) and anything to confirm before sending. No commentary on the counterpart. No "sent" language anywhere.

---

## 5. Voice and formatting rules

- Bottom line first: the correction, the ask, or the decision is the first sentence after the greeting.
- One ask per email where possible; when several are unavoidable, number them and put the date on the one that gates the others.
- Numbers with units, denominators, and dates: "237 rows, shared 08/26/26 3:22 PM ET", never "the file we sent a while back".
- Documents by number; attachments listed; files referenced by the tenant link that matches the share log.
- Third person for records quoted inside the email ("Minutes #016 item 016-002 records"); first person plural for CSL's position.
- Client-executive prose without dash constructions; acronyms spelled out on first use when the recipient is outside the working team.
- Counterparts by name in the greeting and by role in any sentence that describes a discrepancy ("the reply of 09/21 states"), so the sentence is about the record, not the person.
- Time zone on every time; MM/DD/YY on every date; day of week added when the date is a deadline.
- No personal information about anyone, including in an attendance correction ("out of the office" is the whole statement; the reason is never stated).

---

## 6. Worked example: record-correction reply, 09/21/26

Facts from the program record: on 09/21/26 a counterpart's reply disputed the "962 assets / 5 upload sheets" itemization that had stood undisputed for 10 days, described CSL files as "work in progress", stated that only 3 assets had been uploaded, and stated that electrical came off CSL's list in "late July". The M365 share log shows the upload sheets shared with edit access from the 06/22 central-plant sheet through the 09/21 program schedule; the mechanical sheet shared 08/26 and marked completed; the electrical scope change is minuted 08/24. Five confirmations were open. Reply-all, same thread, same day, about 180 words:

> Subject: (thread subject kept) RE: W77 Planon asset uploads
>
> All,
>
> Correcting three points in the 09/21 reply so the thread record stays straight.
>
> 1. The 962 assets / 5 upload sheets itemization went out 09/11 and stood 10 days without comment. The M365 share log shows every sheet shared with edit access, from the central-plant sheet on 06/22 through the program schedule on 09/21. Those are delivered files, not work in progress.
> 2. The mechanical sheet was shared 08/26 and marked completed. If 3 assets are uploaded on the import side, that is import status, not delivery status. Please send the rejection log.
> 3. Electrical came off CSL's list on 08/24, per that day's minutes, not in late July.
>
> Still open, and needed in writing before we code further:
>
> 1. Structure depth past six levels: which spec version governs.
> 2. Whether that change applies retroactively to the delivered sets.
> 3. Electrical disposition: complete in-house, or returning to CSL.
> 4. Recode scope and the record delta it produces.
> 5. Tagging scope.
>
> Can we have 1 and 2 by Wed 09/23? The gases and plumbing set waits on them. Happy to walk the share log on a call.
>
> Thanks,
> Steven

Why it is built this way: each correction quotes the claim, states the record, and names the evidence; no sentence describes the counterpart or a reason; the five confirmations are re-asked because the same thread had left them unanswered; the close carries one gating date and an offer that costs the reader nothing. Distribution: reply-all as received, CSL Project Director already on the thread. After sending: discrepancy logged AMBER (A6) on the open-confirm register with the correction date; the next PLN-SUM cites the correction rather than restating the argument.

---

## 7. Failure modes and how to avoid them

| Failure | What it looks like | Avoidance |
|---|---|---|
| Arguing the correction in the next weekly report | A paragraph in WKR-nnC explaining what really happened; the thread still carries the misstatement | Correct on the thread the same day; the report cites the correction by date |
| Adjectives and motive | "Unfortunately your inaccurate summary", "as you are aware" | Quote the record; state the record; name the evidence; stop |
| Burying the ask | The due date in the last line of the third paragraph | Ask in the first sentence or in a numbered list with a date on the gating item |
| Dropping people from the thread | Reply to one person on a thread five people saw | Reply-all; state any trim; never drop the client program lead |
| Letting a verbal ruling stand in your own reply | "Per the eight-level structure agreed on 09/22" in a CSL email | "Stated on the call 09/22; written confirmation requested 09/22" until the spec exists |
| Sending late | Correction drafted Friday for a Monday recap | Same day; if evidence is missing, send the correction with the evidence you have and the rest to follow by a date |
| Softening the position when asked to soften the tone | "Perhaps we could consider" replacing "we will hold printing" | Tone moves; position and dates do not; offer two registers if pressed |
| Verbal ruling adopted in the subject line or invite | Meeting titled "Eight-level structure rollout" | Subjects carry document numbers and dates, not unconfirmed rulings |
| Missing zone | "3 PM" to an audience in Wilton and Pensacola | Zone on every time; both zones for mixed audiences |
| Attachment by nickname | "the latest sheet attached" | Document number, revision, row count |
| New thread for an old dispute | Fresh email titled "Clarification" | Reply on the thread where the record is |

---

## 8. Pre-send checklist

- Situation type chosen; warmth and assertiveness match it.
- First sentence after the greeting is the correction, the ask, or the decision.
- Every fact, figure, date, name, and document number verified against a pull or a document in this session; names checked against `csl-people` and the register.
- Evidence cited at the highest level available (share log > transmittal > email > minutes item > transcript > cell history) with timestamps and zone.
- No adjectives about people; no motive; discrepancies described as record discrepancies.
- Verbal rulings marked as such with the confirmation-request date; none adopted as fact.
- One ask, or a numbered list with a date on the gating item; consequence stated operationally.
- Reply-all on the original thread for corrections; CSL Project Director copied on positions; client program lead not dropped; no BCC.
- Time zones on every time; deadlines on business days; MM/DD/YY.
- Subject per 4.1 for new threads; thread subject kept for replies.
- Attachments listed by document number and revision; share link matches the log.
- Signature block per 4.3; no images or brand colors in the email body (`csl-brand` Section 5, Email).
- Tone polish run last, with facts locked; draft handed back as To / Cc / Subject / body / attachments / cover note; nothing sent.
- Discrepancy logged (register or meeting file) with the correction date; tier and rule recorded.

---

## Files in this skill

- `templates/record-correction-reply.md` — skeleton, evidence hierarchy, and two populated examples (delivery misstatement; date misstatement).
- `templates/ratify-or-correct.md` — the two-outcome request to a meeting issuer, with exemplar.
- `templates/confirmation-request.md` — verbal-ruling conversion with due date and consequence phrasing bank.
- `templates/escalation-email.md` — the eight-part structure with a populated RED (R8) example and the client-hierarchy etiquette.
- `templates/transmittal-email.md` — transmittal email body keyed to `csl-document-control` Section 5, populated with CSL-W77-TRN-260826-01.
- `templates/it-ticket-scoping.md` — ticket-scope email for moving a CSL-built system onto a client platform, populated with the 08/20/26 dashboard case.
- `templates/signature-block.md` — plain-text signature and variants for engagement threads, BD threads, and other CSL staff.
- `templates/stakeholder-register.md` — register schema, maintenance rules, and the W77 excerpt.

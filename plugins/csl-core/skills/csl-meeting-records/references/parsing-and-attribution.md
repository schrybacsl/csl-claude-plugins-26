# Parsing and Attribution Rules

## Metadata extraction
| Field | Rule |
|---|---|
| meeting_description | Concise professional title from the dominant topics ("ASML W77 Planon Weekly #018") |
| meeting_location | "Microsoft Teams — Virtual" unless a physical location is stated |
| meeting_date / time | From timestamps; time zone ET unless stated; "Time Not Recorded" if absent |
| date_issued / issued_by | Issue date; CSL lead with organization |
| next_meeting | Capture if stated; else "To Be Scheduled" |

## Attendance
- Named speaker → attended. Referenced but silent → confirm with operator before marking attended (silent attendees exist; diarization can also mislabel).
- Operator confirms the final list before render (legacy rule kept).
- Record diarization quality; if broken, attribute remarks by content and transcript-internal evidence and say so in the audit.

## Action items
- ID `[meeting]-[seq]`, order of appearance; minimum one per substantive topic.
- Title 4–7 words; description one formal sentence; responsible as initials-style names; open date = meeting date; due date or "TBD".
- Log: 2–4 sentences, third person past tense: who stated what, why it matters, constraint, next step.

## Decisions and confirmation status
- A decision is recorded with the speaker (name, organization) and one of: "confirmed in writing (doc no.)", "stated on the call; written confirmation requested [date]", "disputed".
- A waiver of a written-confirmation requirement is never recorded as CSL's agreement unless CSL stated it; flag RED (R7) in the audit.
- Changes to scope, date, or structure name the prior baseline and the delta.
- Closure requires evidence (transmittal, share timestamp, document number).

## Language elevation
Remove profanity and filler; convert idiom to professional equivalents; never soften a stated position or add one.

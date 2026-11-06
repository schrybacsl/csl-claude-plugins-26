# Written-Confirmation Request

Converts a ruling, date, scope change, or acceptance given verbally into a written request with a due date and an operational consequence. Until the confirmation exists, CSL documents carry the item as "stated on the call by [role], [date]; written confirmation requested [date]" (csl-operating-rules Section 8). Method in `csl-client-comms` Section 3.5. Register the request the same day; AMBER (A5) after five business days unanswered; RED (R8) the moment a print, tag, cut, or order is scheduled against the unconfirmed item.

---

## Draft block

| Field | Entry |
|---|---|
| To | The person who gave the ruling, by name; role stated in the body |
| Cc | Client program lead when the ruling affects a deliverable date or gate; CSL Project Director; meeting issuer if the ruling was given in a meeting |
| Subject | `[Program] \| [Subject of the ruling] \| Written confirmation requested by MM/DD/YY` |
| Timing | Same day as the call |
| Attachments | The document the confirmation should take the form of, when one exists (spec template, confirm register row) |

## Body skeleton

1. The ruling as heard: subject, value, speaker role, date, forum ("on the 09/29 Planon weekly").
2. The form requested: a versioned specification, a one-line email, a minuted item with the words to be recorded.
3. Due date, day of week, zone if a time is given.
4. Consequence, stated as the hold CSL will apply and why it protects the owner; never as a threat.
5. What continues meanwhile, and on what basis.
6. Sign-off.

Sixty to one hundred twenty words.

## Exemplar (structure depth, ruling of 09/29/26)

> Subject: W77 | Functional code depth | Written confirmation requested by 10/02/26
>
> Tom, on the 09/29 call the structure was stated as up to seven levels. We need that in writing, as a versioned Functional Code Structure spec or a one-line email confirming the depth and the version number, by Fri 10/02/26. Until it arrives we will hold QR label printing, because the code prints on the label and a later change means reprinting and re-walking every tagged asset. Code sets continue on the 08/24/26 written convention in the meantime, and the gases and plumbing set will be built to whichever depth the spec confirms.
>
> Thanks,
> Steven

## Consequence phrasing bank (operational, owner-protective)

| Verbal item | Consequence sentence |
|---|---|
| Code structure, token, or padding | "We will hold QR label printing until this is confirmed in writing, because the code prints on the label." |
| Delivery date compressed on a call | "We will carry the baseline date in the tracker until the new date is confirmed in writing, and report both with the delta." |
| Scope added on a call | "We will open a new task row and budget line on written confirmation; until then the existing row keeps its scope." |
| Scope removed on a call | "We will stop work on [scope] on written confirmation; until then the row stays open and the delivery proceeds." |
| Acceptance or approval given on a call | "We will record the acceptance as verbal until the signed [form] arrives; the next requisition does not reference it before then." |
| De-escalation directed on a call | "We will hold the item at AMBER with a review date of [date] and record the direction; the finding stays in the weekly edition without adjectives." |
| Template or file class named on a call | "We will populate on the template you name once it is confirmed in writing, because a re-import on the wrong class rejects the whole file." |

## After sending

- Open-confirm register row: question, asked date, to whom (role and name), what it blocks, status, tier and rule.
- Code scheme record or baseline record updated with the verbal ruling marked verbal and the request date.
- Follow-up on the sixth business day: one line, request date, item, and the hold still in place.

Pre-send: ruling quoted as heard with speaker role and date; form of confirmation named; due date on a business day; consequence operational; interim basis stated; register row drafted; nothing sent by the agent.

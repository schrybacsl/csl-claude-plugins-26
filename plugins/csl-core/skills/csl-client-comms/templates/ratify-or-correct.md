# Ratify-or-Correct Request

Short note to a meeting issuer when minutes record a decision as "confirmed on the call" that the operator does not recall being confirmed, or recalls as a direction given with the written specification still to come. Two outcomes are offered and either is acceptable: ratify with the transcript timestamp, or correct the item to "stated on the call; written confirmation requested [date]". Method in `csl-client-comms` Section 3.4; transcript audit method in `csl-meeting-records`; tier RED (R7) if the recorded "decision" reverses a minuted one, otherwise AMBER (A6) until resolved.

---

## Draft block

| Field | Entry |
|---|---|
| To | The meeting issuer (W77 Planon weekly: the CSL APM) |
| Cc | The distribution the minutes went to; CSL Project Director |
| Thread | Reply to the email that circulated the minutes; subject kept |
| Timing | The day the minutes arrive; before they file |
| Attachments | None; cite the item number and the transcript timestamp if known |

## Body skeleton

1. Item reference: minutes number, item number, the recorded words in quotes.
2. What the operator has: "stated by [role] as a direction; written spec to follow", or "not in my notes".
3. The two outcomes: cite the transcript timestamp where it was confirmed, or amend to the "stated on the call; written confirmation requested [date]" form.
4. Date by which the minutes should issue clean.
5. What CSL does meanwhile: holds to the last written convention or baseline.
6. Sign-off, first name.

Forty to ninety words. No argument about whether the decision is right; the note is about what the record can support.

## Exemplar (structure-depth ruling of 09/22/26; minutes number illustrative)

> Subject: RE: W77 Planon Minutes #021
>
> Noah, item 4 records the functional code structure at eight levels as "confirmed on the call" on 09/22. I don't have that confirmation in my notes; I have it stated by the client data owner as a direction, with the versioned spec still to come. Could you either cite the transcript timestamp where it was confirmed, or amend the item to "stated on the call; written confirmation requested 09/22/26"? By Thursday would let the minutes issue clean. Our code sets stay on the 08/24 written convention until the spec exists.
>
> Thanks,
> Steven

## When the issuer is a counterpart rather than CSL

Same note, addressed to the counterpart issuer, with one added sentence stating what CSL's record shows and where ("CSL's note of the call and the transcript at 00:38:20 record the depth as a direction pending the spec"). Copy the client program lead only if the item affects a deliverable date or a gate; otherwise the issuer and the minutes distribution.

## After sending

- Open-confirm register row: item, date asked, issuer, what it blocks, tier and rule.
- If the minutes file without change and without a timestamp, the discrepancy is logged as unresolved (AMBER (A6)) and the CSL record carries the item as "stated on the call; ratification requested [date]; not ratified".
- The next CSL document that touches the subject cites the request date, not the disputed item.

Pre-send: item and words quoted exactly; two outcomes offered; date given; interim position stated; no argument on the merits; nothing sent by the agent.

# Record-Correction Reply

Same-day, reply-all, same-thread correction of a counterpart's minutes, recap, email, or tracker that misstates CSL's position, a delivery date, delivered scope, attendance, or a commitment. Method in `csl-client-comms` Section 3.3; tier AMBER (A6) while open, RED (R7) when the misstatement reverses a minuted decision (`csl-schedule-risk/references/tier-rules.md`). The agent produces the draft; the operator sends.

---

## Draft block

| Field | Entry |
|---|---|
| Thread | Reply-all to the message carrying the misstatement; subject unchanged |
| To / Cc | As received; CSL Project Director added if absent; client program lead never dropped |
| Sent by | Operator, same business day the misstatement was received |
| Attachments | None where the evidence is a share log or transmittal already on the tenant; the transmittal PDF when the counterpart has no tenant access |
| Cover note to operator | Evidence pulled (log entry, timestamp, zone); any sentence marked "confirm before sending" |

## Body skeleton

1. Greeting: first names or "All".
2. Lead: "Correcting [n] point(s) in the [date] [reply / minutes / recap] so the thread record stays straight."
3. Corrections, numbered. Each: what the record says (quoted or paraphrased tightly) → what the record should say → the evidence (share-log timestamp with zone, transmittal number, minutes item, email date). No adjectives; no motive; no explanation of why the error might have occurred.
4. Open confirmations, numbered, one line each, with the date on the one that gates the next deliverable.
5. Close: the action requested and the date; an offer that costs the reader nothing (walk the log on a call).
6. Sign-off: first name for working threads; full signature block per `templates/signature-block.md`.

Target length: 120 to 200 words. Anything longer becomes a memo (`csl-executive-memo`) attached to a short email.

## Evidence hierarchy (cite the highest available)

| Rank | Evidence | Quote it as |
|---|---|---|
| 1 | M365 share log, edit access, timestamp | "shared with edit access 08/26/26 3:22 PM ET" |
| 2 | Transmittal number and time | "CSL-W77-TRN-260826-01, 08/26/26 3:22 PM ET, 237 rows" |
| 3 | Sent email header | "sent 09/11/26 4:05 PM ET to the distribution on this thread" |
| 4 | Minutes item | "Minutes #016, item 016-002" |
| 5 | Transcript timestamp | "transcript 00:41:10, 09/22/26" |
| 6 | Tracker cell history | "row WS-22.08, END column, edited 09/19/26 with no change note" |

## Example 1: delivery and scope misstated (program record, 09/21/26)

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

## Example 2: delivery date misstated in minutes (the misstatement is illustrative; the transmittal facts are from the record)

> Noah, one correction to Minutes #017 (number illustrative) item 3 before they file: it records the mechanical upload sheet as delivered 08/28. Transmittal CSL-W77-TRN-260826-01 shows delivery Wed 08/26/26 at 3:22 PM ET, shared with edit access to the four addressees on the transmittal, which met the 48-hour commitment in item 016-002. Please amend the date and reissue, or carry the correction in #018. Thanks, Steven

## After sending

- Log the discrepancy: open-confirm register or meeting series file; date of the misstatement, date of the correction, tier and rule.
- File the correction and any reply with the document it corrects (`csl-document-control` Section 8).
- Next Friday edition cites the correction by date; it does not restate the argument.
- No reply in five business days: one-line follow-up citing the correction date; AMBER (A5).

Pre-send: same day; reply-all; lead with the correction; evidence at the highest rank available with zone; no adjectives or motive; confirmations re-asked and numbered; one gating date; under 200 words; CSL Project Director on the thread; nothing sent by the agent.

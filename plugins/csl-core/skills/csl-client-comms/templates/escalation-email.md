# Escalation Email

Escalates a condition, with its documents and dates, up the path in `references/escalation-matrix.md`. Eight parts in a fixed order so the reader can decide from the first two sentences and verify from the attachments: condition; tier and rule; exposure; what has been done; decision requested; owner; date; attachments. Method and hierarchy etiquette in `csl-client-comms` Section 3.8. The agent drafts; the operator sends.

---

## Draft block

| Field | Entry |
|---|---|
| To | First contact per the matrix row for the trigger (data owner before anyone above them; client program lead when the window has passed or an irreversible step is scheduled) |
| Cc | CSL Project Director on anything above working level; the data owner stays on the thread when the lead is addressed |
| Subject | `[Program] \| [Condition] \| Decision requested by MM/DD/YY` |
| Timing | Same day for RED; within the week for AMBER |
| Attachments | Pull snapshot, transmittal evidence, notice, or memo, each by document number |

## Body skeleton (eight parts, in this order)

1. **Condition.** Item and document number; one sentence.
2. **Tier and rule.** `RED (R8)`, `AMBER (A5)`; the rule ID always accompanies the tier.
3. **Exposure.** Quantified in the owner's units: records, labels, days to a hard date, dollars, gates.
4. **What has been done.** Dated actions: request sent, correction sent, hold applied, register row opened.
5. **Decision or action requested.** One decision, with the options if there are options, and the recommended one.
6. **Owner.** Who acts on the decision once made.
7. **Date.** When the decision is needed and what happens to the exposure after that date.
8. **Attachments.** By document number and revision.

Client hierarchy: escalate in the client's own order; skip a level only with the program lead's agreement, stated in the email; when de-escalation is directed, acknowledge it, hold at AMBER with a review date, and record the direction without adjectives.

## Populated example (facts from the W77 record as of 09/30/26; the print date is illustrative)

> Subject: W77 | QR print gate | Decision requested by 10/02/26
>
> Bill,
>
> One item needs your decision this week. Condition: a QR label print for the mechanical set is being discussed for the week of 10/05 while the functional code structure depth remains unconfirmed in writing (open-confirm register row 1; G-13 in CSL-W77-PLN-EWO-260925). Tier: RED (R8), an irreversible step scheduled against an unconfirmed record.
>
> Exposure: 237 delivered mechanical records and 61 New Asset Form records carry codes built to the 08/24/26 written convention. Depth has been stated four ways since (six levels 08/24; extended 09/10; eight levels verbal 09/22; up to seven 09/29) with no versioned spec. A print followed by a depth change means reprinting every label and re-walking every tagged asset, on top of the 10/30/26 Loops and AHS hierarchy date.
>
> Done so far: written confirmation requested from the data owner 09/22; renewed request after the 09/29 call, due 10/02; code sets held on the 08/24 convention; the TCWP-1 collision and BFP01 merge rulings still open.
>
> Decision requested: either (1) hold the print until the versioned spec issues, which we recommend, or (2) direct a print on the 08/24 convention with the reprint cost accepted in writing. Owner on your side: the data owner for the spec; on ours, S. Schryba to release the print file within one business day of the spec.
>
> Needed by Fri 10/02/26 to keep or move the 10/05 print window with notice to the tagging crews.
>
> Attachments: CSL-W77-PLN-EWO-260925; open-confirm register extract; confirmation request of 09/29/26.
>
> Thanks,
> Steven

## Variants

| Trigger (matrix row) | To | Body emphasis |
|---|---|---|
| CSL commitment misstated by a counterpart, unresolved after correction | Client program lead; cc data owner, CSL Project Director | Attach the correction and the transmittal evidence; ask that the record be settled in the next minutes |
| Forecast versus budget variance above 10% | Budget tracker owner (D. Wolf) and client controller; then CSL Project Director; CFO for CSL-fee exposure | Exposure table from `csl-cost-change-control`; decision on re-baseline or scope |
| Silent milestone lapse or frozen tracker | Tracker owner; then client program lead | Rows named; field movement in the window; the change list requested |
| Work done, no record | Site EH&S / permit coordinator and contractor PM; then client program lead | Backfill requested; RED until the record exists |
| Telemetry signature | Client engineering lead; CSL MEP for technical backing | Facilities notice attached (`csl-technical-docs`); action window |
| BD deadline inside 10 business days, no go/no-go | Marketing Manager and responsible PX/Director; then Partners | Go/no-go memo attached (`csl-bd-pursuits`) |

Pre-send: eight parts in order; tier with rule ID; exposure quantified; dated actions; one decision with the recommendation; owner and date; attachments by number; addressed per the matrix and the client's hierarchy; no adjectives; nothing sent by the agent.

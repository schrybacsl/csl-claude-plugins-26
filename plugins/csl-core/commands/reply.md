---
description: Draft a reply to an email thread in CSL voice (draft only, never sent)
argument-hint: "[thread subject, sender, or paste the thread] [goal of the reply]"
---
Load `csl-client-comms`, `csl-operating-rules`, and `csl-ai-policy`. Find the thread with the Microsoft 365 connector if a subject or sender is given; otherwise use the pasted text. Goal and context: $ARGUMENTS

Classify the situation type, check whether the thread attributes any commitment, date, or scope to CSL (record-correction pattern if it does), confirm names with `search_people`, and draft the reply. Create it in Outlook Drafts only if the operator asks; never send. Close with who should be copied and why.

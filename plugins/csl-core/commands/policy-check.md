---
description: Run the CSL AI Policy pre-handover check on a draft or on the current task
argument-hint: "[what to check, or leave blank for the current draft]"
---
Load `csl-ai-policy` and `csl-operating-rules`. Run the pre-handover checklist in `csl-ai-policy` Section 9 against: $ARGUMENTS (if blank, the most recent draft in this conversation).

Report in this order: (1) pass or the items that fail, each with the fix; (2) a sourced / inferred / assumed table if the output leaves CSL; (3) every `[PLACEHOLDER]` still open; (4) the named reviewer line. Do not rewrite the draft unless asked.

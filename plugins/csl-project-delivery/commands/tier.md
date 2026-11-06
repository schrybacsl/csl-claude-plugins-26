---
description: Assign a RED / AMBER / GREEN tier with its rule ID to a finding
argument-hint: "[describe the finding]"
---
Load `csl-schedule-risk` (`references/tier-rules.md`). Finding: $ARGUMENTS

Apply the decision table top to bottom; return the tier with its rule ID, the other rules that also fire, the response window, the first form, and the escalation first contact by role from `csl-operating-rules` references/escalation-matrix.md. If information needed to decide is missing, say which and give the tier under each case.

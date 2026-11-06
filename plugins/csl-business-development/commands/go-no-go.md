---
description: Screen a solicitation and draft the go/no-go memo
argument-hint: "[attach or link the RFQ/RFP] [responsible PX or director]"
---
Load `csl-bd-pursuits`, `csl-projects`, `csl-people`, and `csl-ai-policy`. Solicitation: $ARGUMENTS

Extract deadlines, mandatory items, evaluation criteria, and disqualifiers. Score fit, and select candidate qualifications from `csl-projects` only. Draft the go/no-go memo from `templates/go-no-go-memo.md` with a dated resourcing plan. If the deadline is within ten business days, say so first. Every value not in the portfolio is `[PLACEHOLDER]` for Marketing.

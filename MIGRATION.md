# Migration from the 2026-09-30 Package

## Where each skill went

| 2026-09 skill | 2.0.0 plugin | Changes beyond the common ones below |
|---|---|---|
| (missing `AGENT.md`) | csl-core / `csl-operating-rules` | New. Same section numbers as the old citations |
| (none) | csl-core / `csl-ai-policy` | New. CSL AI Policy checks |
| `csl-brand` | csl-core | Logo source moved to Marketing-maintained `assets/logo/` |
| `csl-document-control` | csl-core | Empty `references/` folder removed |
| `csl-people` | csl-core | Microsoft 365 authoritative; no email construction |
| `csl-client-comms` | csl-core | Signature block generic, built from `get_me` |
| `csl-executive-memo` | csl-core | — |
| `csl-meeting-records` | csl-core | — |
| `csl-owners-rep-core` | csl-project-delivery | — |
| `csl-schedule-risk` | csl-project-delivery | — |
| `csl-cost-change-control` | csl-project-delivery | — |
| `csl-design-construction-oversight` | csl-project-delivery | — |
| `csl-permits-shutdowns` | csl-project-delivery | — |
| `csl-asset-data-cmms` | csl-project-delivery | — |
| `csl-technical-docs` | csl-project-delivery | — |
| `csl-weekly-reporting` | csl-project-delivery | Cover block from the engagement context file |
| `csl-dashboard-kpi` | csl-project-delivery | Hosting approval note |
| `csl-data-pipeline` | csl-project-delivery | Connector access; Make section rewritten; chart library finds brand tokens across plugins |
| `csl-bd-pursuits` | csl-business-development | Personal details about one employee removed |
| `csl-projects` | csl-business-development | `[PLACEHOLDER]` rule in description |

## Package references

| 2026-09 file | 2.0.0 location |
|---|---|
| `references/escalation-matrix.md` | `csl-operating-rules/references/escalation-matrix.md` (rewritten by role) |
| `references/glossary.md` | `csl-operating-rules/references/glossary.md` |
| `references/quality-checklist.md` | `csl-operating-rules/references/quality-checklist.md` (AI Policy items added) |
| `references/report-catalog.md` | `csl-operating-rules/references/report-catalog.md` |
| `references/skill-authoring-guide.md` | `docs/skill-authoring-guide.md` (org rules added) |

## Common changes applied to every skill

| Old text | New text |
|---|---|
| `AGENT.md Section n` | `csl-operating-rules Section n` |
| `config/client-context-<prog>.md`, `config/user-profile.md` | the engagement context file (`csl-operating-rules` Section 5) |
| `config/tool-registry.md` | `csl-operating-rules` references/connector-map.md |
| "the installed X skill" | "the `X` companion skill (`csl-operating-rules` Section 11)" |
| "Prepared by S. Schryba" in templates | "Prepared by <operator>" |
| Description (up to 1,022 characters) | Rewritten, 554 to 724 characters |

Worked examples that record what happened on W77 (who prepared which document, who attended which meeting) are unchanged; they are history, labeled as the reference implementation.

## What users do differently

1. Start engagement work inside that engagement's Claude Project, which holds the context file.
2. Expect Claude to ask before sending, filing, or uploading anything.
3. Expect a sourced / inferred / assumed table and a named-reviewer line on anything leaving CSL.
4. Use the slash commands in Claude Code and Cowork; in chat, describe the task and the skills trigger on their own.

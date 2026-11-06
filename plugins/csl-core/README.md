# CSL Core

Firm-wide standards for every CSL Consulting employee using Claude. Install this plugin first; the other CSL plugins depend on it.

## Skills

| Skill | Purpose |
|---|---|
| `csl-operating-rules` | The rules every CSL skill cites (replaces the agent rules file the 2026-09 package cited but never shipped): finding standard, skill map, ten escalation triggers, limits on what Claude does on its own, change discipline, sign-off, weekly cadence, output formats |
| `csl-ai-policy` | CSL AI Policy in practice: data intake check, sourcing rules, `[PLACEHOLDER]`, source marking, named-reviewer sign-off, routing to IT |
| `csl-brand` | Palette, type, logo, page anatomy, brand QA, token files |
| `csl-document-control` | Numbering, revisions, file names, transmittals, filing |
| `csl-people` | Staff directory fallback; Microsoft 365 is authoritative |
| `csl-client-comms` | Emails, Teams posts, record corrections, escalations (drafts only) |
| `csl-executive-memo` | Memos, one-pagers, gap analyses, position papers |
| `csl-meeting-records` | Agendas, minutes, action registers, transcript audits |

## Commands (Claude Code and Cowork)

`/csl-core:policy-check`, `/csl-core:reply`, `/csl-core:minutes`, `/csl-core:audit-minutes`, `/csl-core:memo`, `/csl-core:brand-check`, `/csl-core:engagement-setup`

## Setup

Connectors: Microsoft 365 (required for directory, mail drafts, SharePoint filing). Engagement work also needs an engagement Claude Project with a context file built from `skills/csl-operating-rules/references/engagement-context-template.md`.

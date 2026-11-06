# Governance

## Ownership

| Area | Owner (role) | Approves changes to |
|---|---|---|
| Repository, CI, deployment, connectors | CSL IT | Everything; final merge |
| `csl-ai-policy`, `csl-operating-rules` Sections 7 and 9 | CSL IT with the AI Policy owner | AI Policy alignment |
| `csl-brand`, `csl-projects`, `csl-people` | Marketing | Brand, portfolio, directory fallback |
| `csl-project-delivery` skills | Project Management lead | Methods, tier rules, templates |
| `csl-bd-pursuits` | Marketing and BD lead | Pursuit method |

Named owners are recorded in `.github/CODEOWNERS`; the entries there are [PLACEHOLDER] until IT assigns GitHub teams.

## Relationship to the CSL AI Policy

The CSL AI Policy governs. `csl-ai-policy` summarizes it for Claude from the organization instructions; it is not the policy. When the policy changes, IT opens a pull request updating `csl-ai-policy` within ten business days, and bumps `csl-core` by a minor version.

## Review rules

1. Every change goes through a pull request; no direct pushes to `main`.
2. CI (`scripts/validate.py` and `claude plugin validate`) must pass.
3. One CODEOWNER approval for the area changed; two for `csl-ai-policy` or `csl-operating-rules`.
4. No client-confidential detail beyond what the W77 reference implementation already contains, unless the client program lead has agreed and the PX confirms.
5. No credentials, PHI, PCI, unreleased financials, or personal data other than business contact details.

## Versioning and release

Semantic versioning per plugin, recorded in `plugin.json` and the marketplace entry. Major: a breaking change to a rule, number format, or tier. Minor: a new skill, command, or template. Patch: wording and fixes. Every merge adds a `CHANGELOG.md` entry. Merges to `main` sync to the organization automatically.

## Incidents

If a skill causes data exposure or misuse, report it to IT and record it in the AI Incident Log. IT may disable the plugin for the organization while it is fixed.

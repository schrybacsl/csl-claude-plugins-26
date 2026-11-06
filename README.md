# CSL Consulting Claude Plugins

Internal Claude plugin marketplace for CSL Consulting LLC. It packages CSL's owner's-project-management methods, firm standards, and AI Policy guardrails as skills, commands, and an agent that every CSL employee can use in Claude chat, Claude Cowork, and Claude Code under the CSL organization account.

**Confidential. Internal use only.** This repository contains CSL methods and worked examples from client engagements. It must stay private on GitHub (organization sync does not accept public repositories).

## Plugins

| Plugin | Audience | Skills | Depends on |
|---|---|---|---|
| `csl-core` | All CSL employees | operating rules, AI Policy, brand, document control, people, client comms, executive memo, meeting records (8) | none |
| `csl-project-delivery` | Project Management | owner's-rep core, schedule and risk, cost and change, design and construction oversight, permits and shutdowns, asset data and CMMS, technical docs, weekly reporting, dashboards and KPIs, data pipeline (10) | `csl-core` |
| `csl-business-development` | Marketing, BD, pursuit teams | pursuits, project portfolio (2) | `csl-core` |

20 skills, 18 commands, 1 agent. See each plugin's `README.md`.

## Repository layout

```
.claude-plugin/marketplace.json     marketplace catalog (name: csl-consulting)
plugins/
  csl-core/                         .claude-plugin/plugin.json, skills/, commands/
  csl-project-delivery/             .claude-plugin/plugin.json, skills/, commands/, agents/
  csl-business-development/         .claude-plugin/plugin.json, skills/, commands/
docs/skill-authoring-guide.md       how skills here are written
scripts/validate.py                 repository validator (run by CI)
.github/                            CI workflow, CODEOWNERS, PR template
REVIEW.md                           review of the 2026-09 skill package
MIGRATION.md                        what changed from the 2026-09 package and why
GOVERNANCE.md                       ownership, review, release, and AI Policy alignment
CONTRIBUTING.md                     how to propose a change
CHANGELOG.md
```

## Deploying to the CSL Claude organization (admins)

Requirements: a Team or Enterprise plan, with Skills and Cowork enabled for the organization; an Owner or Primary Owner (or an Enterprise custom role that manages libraries).

1. Keep this repository private or internal on github.com, and install the Claude GitHub App on it.
2. In claude.ai, go to **Organization settings > Plugins & skills > Marketplaces**, choose **Add**, then **Sync from GitHub**, and enter `<owner>/csl-claude-plugins`.
3. Set availability per plugin: `csl-core` for everyone; `csl-project-delivery` for the Project Management group; `csl-business-development` for Marketing and BD (Enterprise group overrides).
4. Turn on **Sync automatically** so merges to `main` publish. The person enabling it needs admin access to the repository.

If a sync fails, plugins can be temporarily removed for members, so CI must pass before merge. Reference: Anthropic Help Center, "Manage plugins for your organization" (support.claude.com/en/articles/13837433).

## Claude Code (individual testing)

```
claude plugin marketplace add <owner>/csl-claude-plugins
claude plugin install csl-core@csl-consulting
claude plugin install csl-project-delivery@csl-consulting
```

For local development: `claude --plugin-dir ./plugins/csl-core`.

## Connectors the skills expect

| Connector | Needed by | Purpose |
|---|---|---|
| Microsoft 365 | all plugins | Directory, Outlook drafts, Teams, SharePoint filing |
| Smartsheet | `csl-project-delivery` | Tracker reads (full sheet, filtered locally) |
| Scoro | optional | Projects, time, resourcing reads |

Connectors are enabled per user by IT. Skills degrade gracefully: if a connector is missing, Claude says so and works from an uploaded export.

## Engagement setup

Each client engagement gets one Claude Project holding `engagement-context-<PROG>.md`, built with `/csl-core:engagement-setup` from the template in `plugins/csl-core/skills/csl-operating-rules/references/`. Client names, role holders, sheet IDs, and thresholds live there, not in this repository.

## Validate before every pull request

```
python3 scripts/validate.py
claude plugin validate .
```

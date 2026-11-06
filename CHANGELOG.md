# Changelog

## 2.0.0 (2026-11-06)

First release as a Claude organization plugin marketplace, rebuilt from the 2026-09-30 single-user skill package. See `MIGRATION.md` for the full list.

- Split 18 skills into three plugins (`csl-core`, `csl-project-delivery`, `csl-business-development`) with dependencies.
- Added `csl-operating-rules` (replaces the missing `AGENT.md`, same section numbers) and `csl-ai-policy`.
- Added engagement context template, connector map, and role-based escalation matrix.
- Rewired data access from environment-variable tokens and Make scenarios to organization connectors.
- Removed single-user personalization; templates use `<operator>`; signatures built from Microsoft 365.
- Rewrote all 18 descriptions within the 1,024-character limit.
- Documented companion skills that are not bundled, with fallbacks.
- Added 18 commands, the `independent-reviewer` agent, a validator, and CI.

## 1.0.0 (2026-09-30)

Original package: 18 skills, package references; not distributed as a plugin.

# Contributing

1. Read `docs/skill-authoring-guide.md`.
2. Branch from `main`: `skill/<name>-<change>`.
3. Edit or add files under `plugins/<plugin>/`. A new skill needs a folder named for it, a `SKILL.md` with `name` and `description` frontmatter (description under 900 characters), and every file it lists under "Files in this skill".
4. If the skill produces a recurring deliverable, add it to `csl-operating-rules` Section 4 and `references/report-catalog.md`.
5. Bump the plugin version in both `plugin.json` and `.claude-plugin/marketplace.json`; add a `CHANGELOG.md` entry.
6. Run `python3 scripts/validate.py` and `claude plugin validate .`.
7. Open a pull request using the template. Request review from the CODEOWNER for the area.

Engagement-specific content (client names, staff, sheet IDs, thresholds) goes in the engagement's Claude Project, not here.

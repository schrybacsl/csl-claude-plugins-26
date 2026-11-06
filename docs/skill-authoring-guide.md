# Skill Authoring Guide for this package

How every `plugins/<plugin>/skills/csl-*/SKILL.md` in this repository is written, so they read as one system and can be maintained by anyone at CSL.

## Format

```
---
name: csl-<slug>
description: >
  One paragraph. What the skill does AND when to use it, written a little pushy so the agent
  triggers it whenever the topic is near (name the deliverables, the verbs people use, the
  situations). All "when to use" language goes here, not in the body.
---

# Title

One-paragraph purpose: what the deliverable is for, who reads it, what it protects.

## 1. Bottom line / when this runs
## 2. Inputs and pulls (what data, from where, QA rules)
## 3. Method (numbered steps; imperative voice; say why each step matters)
## 4. Output specification (exact structure, page map or section list, numbering, naming)
## 5. Voice and formatting rules specific to this deliverable
## 6. Worked example (populated with realistic CSL content, W77 or another CSL engagement)
## 7. Failure modes and how to avoid them
## 8. Pre-issue checklist
## Files in this skill (references/, templates/, scripts/)
```

Keep `SKILL.md` under ~450 lines. Put long tables, schemas, and worked examples in `references/` and `templates/` and point to them with "read this when…".

## Content rules

- Realistic, not templated. Examples carry real CSL document numbers, sheet names, workstream IDs, and dates where they are already in the program record; invent nothing that reads as fact. Any fact a skill or template cannot know is written `[PLACEHOLDER]` (CSL AI Policy).
- Org-wide, not personal. Never name one employee as "the operator" or hard-code one person's signature, profile, or history. Role holders come from the engagement context file; people from Microsoft 365.
- Connector-first. Data access is described through the organization connectors (`csl-operating-rules` references/connector-map.md). Never describe tokens, environment variables, or local paths as the way to reach a system.
- Engagement specifics stay in the engagement's Claude Project. W77 is the reference implementation; new client detail is not added to shared skills without the program lead's agreement.
- Owner-first. Every method step ends in what the owner learns or what the owner must decide.
- Bottom line up front in every output specification.
- Explain the why in one clause rather than shouting MUST. Reserve absolute language for the ten escalation triggers in `csl-operating-rules` Section 6, the CSL AI Policy rules in `csl-ai-policy`, and the brand red rule.
- Cross-reference by skill name (`csl-document-control`), never by path guesses.
- Terminology per `references/glossary.md`; brand per `skills/csl-brand`; numbering per `skills/csl-document-control`; tiers per `skills/csl-schedule-risk`.
- Voice: plain, declarative, technically precise. No filler, no marketing adjectives. Client-executive outputs: no dash constructions in running prose.
- Privacy: no health, HR, or personal information about anyone. Interpersonal disputes are described as record discrepancies with documents and dates, not as character.
- Dates `MM/DD/YY` in examples of records; ISO in file names.

## Templates

Templates in `templates/` are Markdown skeletons with real section headings and one populated example row per table. They show the shape and the level of specificity; they never ship with placeholders like "Lorem" or "[insert]". Use `<angle-bracket>` variables only for values that change every issue (`<yymmdd>`, `<week>`).

## Checklist before adding a skill

- Frontmatter valid YAML; `name` matches the folder; description under 900 characters (hard limit 1,024; `scripts/validate.py` enforces both).
- No duplicate of a bundled or companion skill's content; point to it instead.
- Every file referenced in "Files in this skill" exists.
- Ran the brand checklist on any example output.
- Added a row to `csl-operating-rules` references/report-catalog.md if the skill produces a recurring deliverable, and to `csl-operating-rules` Section 4.
- Ran `python3 scripts/validate.py` with no errors.
- Bumped the plugin version and added a CHANGELOG entry.

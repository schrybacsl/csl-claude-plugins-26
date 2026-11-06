# Review of the 2026-09-30 CSL AI Agent Skills Package

Reviewed 11/06/26 ahead of the move to CSL's Claude organization account. Source: `CSL-Consulting_AI_Agent_Skills.zip` (145 files, 18 skills, 5 package references, 7 Python scripts, 6 brand asset files).

## Bottom line

The method content is strong and worth keeping intact: the tier rules, the pull-snapshot-diff discipline, the record-correction pattern, document numbering, and the deliverable templates are specific, internally consistent, and grounded in a real engagement. The package was, however, built for one person running a standalone agent. It cannot be deployed to the organization as is because it depends on files it never shipped, is personalized to one employee, reaches data through credentials rather than connectors, and has no layer for the CSL AI Policy. The rebuild keeps the method content and fixes the environment around it.

## Strengths kept

1. A single tier authority (`csl-schedule-risk`, rules R1 to R9 and A1 to A6) that every other skill cites, with rule IDs printed beside every tier.
2. Evidence discipline: every number tied to a pull with timestamp and md5, never carried from a prior edition.
3. Clear authority limits: drafts only, no writes to client systems, CSL recommends and the owner decides.
4. Consistent skill anatomy (bottom line, inputs, method, output spec, voice, worked example, failure modes, checklist).
5. Working Python: all scripts and brand assets compile; the chart library and brand tokens import cleanly.

## Findings

| # | Finding | Effect | Severity | Resolution in 2.0.0 |
|---|---|---|---|---|
| 1 | `AGENT.md` is cited 38 times across 20 files (Sections 2, 4, 6 to 10) but is not in the package | The ten escalation triggers, authority limits, and cadence the skills depend on were undefined | High | New `csl-operating-rules` skill with the same section numbers; all citations redirected |
| 2 | `config/user-profile.md`, `config/client-context-<prog>.md`, `config/tool-registry.md` cited in 13 files, not shipped | Role holders, sheet IDs, and thresholds had no home | High | Engagement context template held in each engagement's Claude Project; connector map |
| 3 | Personalized to one operator: named in 44 files; one employee's signature block, prior employers, and outside ventures embedded; a second employee named as the skill's user in two descriptions | Unusable as-is by other staff; personal information in an org-wide asset | High | "Operator" redefined as the employee running the session; templates use `<operator>`; signatures built from Microsoft 365; personal details removed. Historical W77 examples kept as examples |
| 4 | Data access through an environment-variable Smartsheet token, the SDK or REST, and Make scenarios; outputs written to local `outputs/` folders | Does not work in claude.ai, where the sandbox cannot reach the Smartsheet API and tokens must not be handled in chat | High | Connector-first access; scripts run on connector data with `--from-csv`; filing to SharePoint on instruction |
| 5 | No CSL AI Policy layer: no intake check for PHI, PCI, or PII; no sourced / inferred / assumed marking; no named-reviewer handover; no routing of legal language to IT; template rule forbade placeholders, conflicting with the policy's `[PLACEHOLDER]` requirement | Policy non-compliance risk on client deliverables | High | New `csl-ai-policy` skill; quality checklist and authoring guide updated |
| 6 | Eight companion skills cited but not bundled (`sipp`, `planon-doc-generator`, `masterformat-2018`, `mep-drawing-review`, `aia-contracts-capital-projects`, `higher-ed-bidding`, `tone-polish`, legacy `csl-meeting-minutes`) | Silent gaps when a skill defers to a missing companion | Medium | Listed in `csl-operating-rules` Section 11 with fallbacks |
| 7 | Ten descriptions between 1,009 and 1,022 characters against the 1,024 limit | Valid, but any edit would break validation | Medium | All 18 rewritten to 554 to 724 characters, trigger phrases kept |
| 8 | Escalation matrix named specific client and CSL individuals | Wrong people on the next engagement | Medium | Role-based matrix; names mapped in the engagement context file |
| 9 | Client-confidential W77 detail (client staff names, sheet IDs, ticket numbers) throughout worked examples | Visible to every CSL employee once distributed | Medium, decision needed | Kept as the labeled reference implementation; repository must be private; new client detail stays in engagement Projects (GOVERNANCE rule 4). Leadership should confirm this is acceptable or request anonymization |
| 10 | Staff directory scraped from the public website July 2025 with an instruction to construct emails from a pattern | Stale titles; risk of misaddressed client mail | Medium | Microsoft 365 directory made authoritative; pattern-based construction prohibited |
| 11 | Official logo files not included; skill pointed to a missing registry | Issued documents could fall back to the CSS approximation | Low | Marketing to commit files under `csl-brand/assets/logo/`; interim SharePoint source |
| 12 | Client dashboard hosting on Replit with no tool-approval check | Client data on a platform that may not be on the Approved AI Tools Register | Low | Note added to `csl-dashboard-kpi`; routed to IT per policy |
| 13 | No packaging, versioning, validation, or ownership | No safe way to update an org-wide asset | Medium | Marketplace manifests, plugin versions, validator, CI, CODEOWNERS, governance |
| 14 | HR, IT, and Accounting staff have no skills of their own | Most of the firm gets only `csl-core` | Observation | Not built: no CSL source material for those functions was provided. Candidates for future plugins |

## Verification of the rebuild

- `python3 scripts/validate.py`: 0 errors, 0 warnings.
- `claude plugin validate` (Claude Code 2.1.318): marketplace and all three plugins pass.
- All Python compiles; `chart_library.py` resolves `csl-brand` tokens across the plugin boundary.

## Review of marketplace 2.0.0

Reviewed 11/06/26. Scope: repository documentation and governance, marketplace and plugin manifests, CI, validator, and the data-pipeline scripts. This records findings only; no implementation fixes were made.

| # | Finding | Effect | Severity | Recommendation |
|---|---|---|---|---|
| 15 | `smartsheet_pull.py:158` sets the REST `Authorization` header to the literal `"******"` instead of using the supplied token | Every REST request is unauthenticated. `--mode rest` fails, as does `auto` when the optional SDK is unavailable | Medium | Send the token using Smartsheet's required bearer authorization format; add a mocked REST request test |
| 16 | `scripts/validate.py:172` compares platform-native relative paths against POSIX allowlist suffixes | On Windows, the intentional historical references in `csl-operating-rules/SKILL.md` are not allowlisted, so the repository validator exits with four false-positive errors | Low | Normalize relative paths to POSIX form before matching, and test the validator on Windows and Linux |
| 17 | `freeze_check.py:93,110` returns exit code 0 when `--pulls-dir` is missing or no snapshots are found | Automation can treat a check with no usable input as successful, despite there being no freeze result | Low | Return a nonzero configuration/input error code for these cases |
| 18 | `.github/CODEOWNERS` still assigns every area to `[PLACEHOLDER]` teams | The CODEOWNER approvals required by `GOVERNANCE.md` cannot be reliably routed until IT replaces the placeholders with real teams | Medium (setup gate) | Assign valid GitHub teams before relying on CODEOWNERS for release approvals |

### Verification

- `C:/Users/Esteban/AppData/Local/Programs/Python/Python312/python.exe scripts/validate.py`: failed with four errors, all the Windows allowlist issue in finding 16; no warnings or Python compile errors were reported.
- Direct `freeze_check.py` execution could not reach its CLI behavior because the configured Python environment does not have `pandas` installed (`ModuleNotFoundError`). Finding 17 is from code inspection, not a completed runtime test.
- `claude plugin validate` was not run because the Claude CLI is not available in this environment.
- GitHub visibility could not be confirmed: `gh repo view schrybacsl/csl-claude-plugins` could not resolve the repository. Treat the required private visibility as unverified, not as confirmed exposure.

# CSL Project Delivery

Owner's-representative and owner's project management skills for CSL Project Management staff. Requires `csl-core`.

## Skills

| Skill | Purpose |
|---|---|
| `csl-owners-rep-core` | The owner's-rep role, RACI, engagement setup, duties by phase |
| `csl-schedule-risk` | Authority for RED / AMBER / GREEN tier rules; schedule and risk register |
| `csl-cost-change-control` | Budgets, change orders, pay apps, CAPEX gates, LOE cost side |
| `csl-design-construction-oversight` | OAC, RFIs, submittals, field reports, commissioning, turnover |
| `csl-permits-shutdowns` | Permit boards, shutdown packages, gates |
| `csl-asset-data-cmms` | Asset registers, CMMS uploads, reconciliation |
| `csl-technical-docs` | SOPs, PM and scope packages, assessments, notices |
| `csl-weekly-reporting` | WKR weekly report family (A, B, C, D) |
| `csl-dashboard-kpi` | KPI catalog, command views, dashboards |
| `csl-data-pipeline` | Connector pulls, snapshots, diffs, QA rules, report factory, chart library |

## Commands and agent

Commands: `/csl-project-delivery:weekly-report`, `:pull`, `:tier`, `:co-review`, `:pay-app-review`, `:field-report`, `:oac-prep`. Agent: `independent-reviewer`, a fresh-eyes check for high-stakes deliverables.

## Setup

Connectors: Smartsheet and Microsoft 365. The Python scripts run in code execution on data a connector returned or an uploaded export (`--from-csv`); the claude.ai sandbox cannot call the Smartsheet API directly. Each engagement needs a Claude Project with its context file.

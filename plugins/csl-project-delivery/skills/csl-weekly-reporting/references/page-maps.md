# WKR Page Maps — data contracts per page

Each row: page, section, data source (sheet / script output), chart from `csl-data-pipeline/scripts/chart_library.py`, tier logic.

## WKR-nnA Look-Ahead (10 pp)
| Page | Section | Data | Chart | Tier logic |
|---|---|---|---|---|
| 2 | Bottom line + KPI strip + commitment statement | KPI set; anchor rows from CSL Tasks + Mitigation (rows with END inside the window) | none | strip cards per tier rules |
| 3 | Day-by-day look-ahead | rows with START or END in window across all sheets; permits starting | none | RED if a start has open gates < 2 days out |
| 4 | Permit look-ahead | SIPP: START in window or next 30 days; gate counts | `permit_gates_bar` | inverted dates AMBER (A6) |
| 5 | Roadmap due this week | Roadmap: END in window; diff vs last pull | `frozen_weeks_indicator` | frozen A4/R5 |
| 6 | Mitigation targets | Mitigation: target date in window; past-target trend | `mitigation_trend` | A2 on past-target growth |
| 7 | CSL board | CSL Tasks: Red rows, anchors | none | age of Reds |
| 8 | Program thread | PLN register: deliveries due, gates, confirms | none | R8 tagging gate |
| 9 | Red-flag narrative | all REDs with rule IDs | one featured chart | — |
| 10 | Docket + source note | prior docket + new | none | — |

## WKR-nnB Mid-Week (5 pp)
| Page | Section | Data | Chart |
|---|---|---|---|
| 2 | Executive summary; "since Monday" table | diff Monday snapshot vs Wednesday pull | none |
| 3 | Critical path + RED list + decisions before Friday | anchors; tier register | none |
| 4 | Visual page | mitigation trend; permit gates; rig state | 2–3 from library |
| 5 | Featured item; docket | operator input | optional |

## WKR-nnC End-of-Week (8–11 pp)
| Page | Section | Data | Chart |
|---|---|---|---|
| 2 | Headline; KPI strip; what-moved table | `diff_pulls.py` what_moved.md | none |
| 3 | Permit board | SIPP week rows; `qa_rules.py` flags | `permit_gates_bar` |
| 4 | Roadmap | diff; RPN watchlist; health | `rpn_watchlist_bar`, `health_distribution` |
| 5 | Mitigation | open/past-target/closures/owner load; WS-22 pipeline | `mitigation_trend`, `closures_per_week` |
| 6 | CSL board | Reds, anchors, byte-identity | `board_reds_anchors` |
| 7 | Program thread | PLN-SUM / PLN-EWO registers | none |
| 8 | Engineering + telemetry | CTRW outputs; notices | `rig_timeseries`, `drawdown_regression` |
| 9 | New requests and decisions | operator input; minutes | none |
| 10 | Risk narrative + next week frame | tier register | optional |
| 11 | Docket; consolidated source note; as-of | all | none |

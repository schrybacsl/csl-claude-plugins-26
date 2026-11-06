# Command View Specification

Read this when a command or executive header view is being designed, changed, or audited. A command view is what a named stakeholder reads in ninety seconds: a KPI strip of at most eight tiles, the RED list with rule IDs, the docket, then drill-downs. Nothing scrolls above the RED list; the last-pull timestamp sits in the header. The template is Section 1; the worked example (client program lead view, the Gannon Command view on the W77 Roadmap Insight Dashboard) is Section 2.

## 1. Specification template

| Field | Content |
|---|---|
| View name and code | `<Program> <Role> Command`; version string `v<n.n>` |
| Reader | Role; the decisions the view supports (one sentence each) |
| Access | Main executive view, or gated beside it with its own access codes or SSO group; who issues and rotates codes |
| Header | Program name; view name; last-pull timestamp (ET) per source; data source names with IDs; link to the KPI catalog version |
| KPI strip | At most 8 tiles; per tile: catalog ID, label, value with denominator, delta versus last pull, tier bar with the word, source on hover |
| RED list | Every item where an R-rule fires across all sources; columns: rule, item, exposure (dollars, days, records), owner, since (first pull it appeared), evidence link |
| Docket | Item, tier (rule), owner, due, evidence of closure expected; carried items show first-appearance edition |
| Drill-downs | Named sections below the fold, each with its own source line; tables sortable with `aria-sort`; charts from `chart_library.py` contracts |
| Empty states | "not available at <pull time>, source <name>" with the reason; a tile never shows 0 for missing data |
| Refresh | Pull cadence per source; manual refresh allowed only from the operator |
| Verification | Independent audit pass before any republish (Section 3) |

Tile anatomy (implemented by `.kpi` in `brand-tokens.css`): label in caps 7.5 pt slate; value 20 pt navy bold with denominator in the same line ("17 / 20"); delta line "vs last pull +2" in slate; 3 pt top bar in the tier color with the tier word and rule at the right ("AMBER A2"); hover or footer with "Source: <sheet> (ID) pulled <MM/DD/YY HH:MM ET>".

## 2. Worked example: client program lead command view (Gannon Command, W77)

Reader: the client program lead for the W77 IRO Capital Program. Decisions the view supports each week: which tracker owners must move rows, which risks need an engineering owner this week, whether the mitigation block needs an owner-by-owner review, whether the permit board is clean, whether any cost line needs a memo, whether the asset-data deadline is at risk, and whether telemetry needs a facilities notice. Access: the main executive view of the Roadmap Insight Dashboard; the CRE engineering view (Koning view) sits beside it behind two access codes and reuses tiles 1, 2, 6, and 7.

Header: `W77 IRO Capital Program | Gannon Command v1.3 | Pulls: Roadmap Master 1059284113641348 09/18/26 06:40 ET; Mitigation Plan 2158727850315652 06:41 ET; SIPP Permits 289677048237956 06:42 ET; CSL Tasks 7673437876080516 06:43 ET; CTRW metrics 09/18/26 (weekly zip)`. Values below are the 09/18/26 readings carried in WKR-38C where the record has them and are marked illustrative where it does not.

| # | Tile (catalog ID) | Value shown | Delta vs last pull | Tier (rule) and threshold | Source |
|---|---|---|---|---|---|
| 1 | Roadmap rows changed / frozen weeks (KPI-RDM-01, KPI-RDM-02) | 0 rows changed; frozen 6 pulls | +1 frozen pull | RED (R5): >= 2 frozen pulls with witnesses (SIPP 53782 started 09/16, 51718 closed 09/18) | Roadmap Master 1059284113641348 |
| 2 | RPN >= 700 without active mitigation (KPI-RDM-04) | 1 of 5 rows >= 700 (Electrical Distribution MV & LV, RPN C 1,000; count of rows >= 700 illustrative) | 0 | RED (R1): >= 1 | Roadmap Master; risk register |
| 3 | Mitigation past-target with closures (KPI-MIT-02, KPI-MIT-03) | 17 of 20 open; 0 closures | +2 | AMBER (A2); R4 for anchor or minuted dates | Mitigation Plan 2158727850315652 |
| 4 | Permit perfect-week streak (KPI-PRM-03) | 4 weeks | +1 | GREEN (G); reset by any R6 | SIPP Permits 289677048237956 |
| 5 | Worst forecast vs budget variance by E-GRP (KPI-RDM-09) | not available at 09/18/26 06:40 ET, source Roadmap Master: forecast columns frozen for Q3 close on 09/30 | n/a | R2 > 10%, A2 5–10% | Roadmap Master |
| 6 | Asset records delivered / business days to 10/30/26 (KPI-AST-01, KPI-AST-05) | 237 mechanical records (08/26/26, Functional Code Structure v1.1); 30 business days to 10/30/26 with gate G-13 open | -5 days | AMBER (A3): G-13 open > 2 weeks against a dated deliverable | Delivery Control sheet; PLN-EWO gate register |
| 7 | Open confirms > 5 business days (KPI-AST-03) | 8 standing confirms; count over 5 business days per the current register (illustrative until pulled) | per register | AMBER (A5); RED (R8) if one gates a scheduled print | Open-confirm register (PLN-SUM) |
| 8 | Reservoir runway, minimum across rigs (KPI-TEL-01) | TR7 runway from the latest regression (loss 0.12 to 0.15 L/day range on record; days illustrative until the weekly zip is processed) | per zip | RED (R9) < 90 days; AMBER (A1) falling | CTRW `_metrics.json` |

RED list query (the union of R-rules across sources; each source contributes rows already tiered by its skill):

```python
red = concat([
    roadmap[(roadmap.rpn_c >= 700) & no_active_mitigation(roadmap)].assign(rule="R1"),
    freeze[(freeze.streak >= 2) & freeze.witnesses.notna()].assign(rule="R5"),
    lapses[lapses.status_unchanged & lapses.end_passed & lapses.constraint.isna()].assign(rule="R4"),
    permits[permits.work_no_record].assign(rule="R6"),
    variance[variance.pct.abs() > 10].assign(rule="R2"),
    gates[gates.print_scheduled & ~gates.code_confirmed_in_writing].assign(rule="R8"),
    telemetry[(telemetry.runway_days < 90) | (telemetry.zero_flow > 0)].assign(rule="R9"),
    records[records.minuted_decision_reversed_without_change].assign(rule="R7"),
])[["rule", "item", "exposure", "owner", "since", "evidence"]].sort_values(["rule", "since"])
```

Rendered as a table under the strip: `Rule | Item | Exposure | Owner | Since | Evidence`, with the exposure quantified (dollars, days, records, gates) and the evidence a link to the transmittal, minutes item, or snapshot row. The docket follows (item, tier with rule, owner, due, closure evidence expected), then the drill-downs in this order: roadmap movement and frozen indicator; RPN watchlist; mitigation table with steps of 10; permit board; asset program (files, confirms, gates); telemetry panels; commercial (when the quarter-close variance table exists).

What the reader learns in ninety seconds on 09/18/26: two REDs are tracker-governance conditions with named fixes; the mitigation sheet needs an owner-by-owner review rather than more rows; the permit board is clean; the asset deadline is thirty business days out with one gate blocking; telemetry status depends on the weekly zip being processed the same day.

## 3. Verification before a republish

1. Build the change in the workspace copy; the live link is untouched.
2. Independent audit pass by a fresh session that has not seen the change: every tile against `metrics.json` of the same pull; every tier word against its rule; every empty state honest. The W77 audit found a category key mismatch rendering zeros and a missing role label; both were fixed before the republish.
3. Stage, screenshot, and record the version string and the pull timestamps.
4. Republish only on instruction in the session (csl-operating-rules Section 7); note the version and date in the dashboard's about panel and in the next Friday source note.

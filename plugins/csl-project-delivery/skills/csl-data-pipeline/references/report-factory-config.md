# Report Factory Configuration (WKR family example)

Read this when a report family is being set up, changed, or debugged, and when a template needs a sheet ID, column, KPI definition, or page map: it comes from here, never from the template. One `config.yaml` per family lives with the factory code (CSL server, program folder); the version string prints in the PDF properties so an issued file names the config that produced it.

## 1. Annotated `config.yaml` for the W77 WKR family

```yaml
family:
  program: W77                          # PROG segment of the document number (csl-document-control 1)
  fam: WKR                              # FAM segment; editions A/B/C/D per csl-document-control 1
  config_version: "2026.09.3"           # bump on any change; printed in PDF properties
  timezone: America/New_York            # every timestamp in the PDF is ET
  number_pattern: "CSL-{program}-{fam}-{iso_week}{edition}"   # ISO week computed by code, never counted
  file_pattern: "{number}_{yyyy-mm-dd}{rev}.pdf"

sources:                                # every sheet the family reads; IDs live here only
  roadmap_master:
    platform: smartsheet                # smartsheet | graph_excel | sharepoint_list | make (adapter, graph-repoint-plan.md)
    id: 1059284113641348
    name: "W77 Roadmap Master 2025-2032"
    parents_only: true                  # child rows are phases and double count
    columns:                            # titles as the sheet shows them; renames are schema drift
      health: "Health"
      title: "Roadmap + Equipment + Task"
      egrp: "E-GRP"
      start: "START"
      end: "END"
      baseline_finish: "Baseline Finish"
      variance: "Variance2"
      pct: "%"
      constraints: "Constraints"
      sev: "SEV"
      occ: "Occ"
      det: "Det"
      rpn_c: "RPN C"
      rpn_b: "RPN-B"
      budget: "Budget"
      forecast_2026: "Forecast 2026"
      year: "YR."
    hash_ignore: []                     # keep empty unless the sidecar must say why a column is excluded
  roadmap_weekly:
    platform: smartsheet
    id: 1390098374414212
    name: "Roadmap (weekly report pull)"
  csl_tasks:
    platform: smartsheet
    id: 7673437876080516
    name: "CSL Tasks"
    columns: {title: "Task Name", assigned: "Assigned To", owner: "Owner", state: "State", pct: "% Complete", start: "Start Date", end: "End Date", health: "Health"}
  sipp_permits:
    platform: smartsheet
    id: 289677048237956
    name: "SIPP Permits"
    columns: {permit: "Permit #", start: "START", end: "END", status: "Status", contractor: "Contractor", gates_cleared: "Gates Cleared", gates_total: "Gates Total"}
  mitigation:
    platform: smartsheet
    id: 2158727850315652
    name: "ST CHW/PCW System Mitigation Plan"
    columns: {ws: "WS #", title: "Workstream", owner: "Owner", step: "Lifecycle Step", target: "Target Date", status: "Status", baseline: "Baseline Status", egroup: "E-Group", po: "In Place"}
    id_regex: "^WS-\\d{2}\\.\\d{2}(\\.\\d{2})?$"     # mixed formats (WS209) are an A6 population finding

kpis:                                   # formula, denominator, threshold, rule ID, source; the dashboard catalog mirrors these
  roadmap_rows_changed:
    formula: "count(rows where any compared cell differs vs previous snapshot)"
    denominator: "parent rows compared"
    source: roadmap_master
    tier: {rule: "A4/R5 via freeze_check", note: "0 changed and md5 identical -> frozen"}
  rpn_ge_700_no_mitigation:
    formula: "count(rpn_c >= 700 and (owner blank or action date blank or action date passed with no status change))"
    denominator: "rows with rpn_c >= 700"
    source: roadmap_master
    tier: {rule: "R1", threshold: ">= 1"}
  behind_baseline_pct:
    formula: "count(variance < 0) / count(baseline_finish present) * 100"
    denominator: "rows carrying a baseline"
    source: roadmap_master
    tier: {rule: "A2", threshold: "reported; tier set per row class"}
  mitigation_past_target:
    formula: "count(open rows with target < pull date)"
    denominator: "open rows"
    source: mitigation
    compare_to: previous_edition          # printed as 17 (15)
    tier: {rule: "A2; R4 if an anchor or minuted date"}
  mitigation_closures:
    formula: "count(rows closed since previous snapshot)"
    source: mitigation
    note: "always printed beside past_target so a sweep reads as a sweep"
  permit_perfect_week:
    formula: "all(started this week gated in time) and no work-done-no-record"
    source: sipp_permits
    tier: {rule: "R6 when a start has no record"}
  forecast_vs_budget_egrp:
    formula: "(sum(forecast) - sum(budget)) / sum(budget) * 100 by egrp, parents only"
    source: roadmap_master
    tier: {rule: "R2 > 10%; A2 5-10%"}

charts:                                 # chart_library functions with the KPI feeding each; titles are written per edition
  - {fn: fig_mitigation_open_past_target, from: [mitigation_open, mitigation_past_target, mitigation_closures], editions: [C]}
  - {fn: fig_rpn_watchlist, from: [rpn_watchlist], threshold: 700, editions: [C]}
  - {fn: fig_permit_gates_weekly, from: [permits_weekly], editions: [C]}
  - {fn: fig_frozen_weeks, from: [freeze_chain_roadmap], editions: [A, C]}

page_maps:                              # section order per edition; a section with no data prints "not available at <pull>, source <name>"
  A: [cover, headline, look_ahead_framing, anchors_and_docket, permits_next_week, roadmap_movement, mitigation_strip, risks, sources]
  B: [cover, kpi_strip, executive_summary, critical_path_and_risk, docket, sources_last_page]
  C: [cover, headline, permit_board, roadmap, mitigation, csl_board, commercial, docket, sources]
page_counts: {A: [10, 10], B: [5, 5], C: [8, 11]}

cover:
  style: {A: royal_blue_field, B: white, C: navy_field}   # A adopted the client cover field with WKR-40A (09/28/26); reuse the last issued hex
  prepared_by: "S. Schryba"
  prepared_for: "S. Kazantzidis"
  sources_note_on_cover: false          # 09/01/26 direction for the B and C covers

distribution:
  B_C: ["B. Gannon (ASML)", "P. Gorman (ASML)", "D. Wolf (CSL)", "E. Hubert (CSL)"]
  transmittal: "email draft per csl-client-comms; subject 'W77 | WKR-{week}{edition} {edition_name} | {MM/DD/YY}'"

render:
  engine: playwright                    # HTML + brand-tokens.css -> Chromium; reportlab for table-heavy pages
  page: {size: Letter, orientation: portrait, margin_in: 0.75}
  font: {print: "Avenir Medium", fallback: "Arial Narrow"}   # fallback is reported in the delivery note

qa:
  forbid_hex: ["#C8102E"]
  red_allowed_only_in: ["logo", "hairline-red"]
  require_rule_id_beside_tier: true
  pdffonts_must_include_one_of: ["Avenir", "ArialNarrow"]
  page_count_from: page_counts

outputs:
  root: "${CSL_OUTPUT_ROOT}/W77/WKR/{yyyy}"
  superseded: "_superseded"
  keep_beside_pdf: [pulls, metrics.json, what_moved.md, qa_findings.csv, qa.json]
```

## 2. Stage inputs and outputs

| Stage | Command shape | Output |
|---|---|---|
| pull | `factory pull --family WKR --edition C` (calls `smartsheet_pull.py` per source) | `pulls/<date>/<id>.csv` + `.json`, pull log blocks |
| compute | `factory compute --edition C --previous <date>` | `metrics.json` (every KPI with value, denominator, source, pull time, previous value), `what_moved.md`, `qa_findings.csv`, freeze results |
| charts | `factory charts` | `fig01_...png` and so on, each with a stamped source line |
| template | `factory template` | `report.html` built from the page map; each section reads `metrics.json` |
| pdf | `factory pdf` | `<number>_<date>.pdf` |
| qa | `factory qa` | `qa.json`; non-zero exit blocks filing |
| file | `factory file` | copies to `outputs/`, moves superseded, writes the transmittal register row |

`metrics.json` is the contract between compute and everything after it. Each KPI entry carries `value`, `denominator`, `previous`, `delta`, `tier`, `rule`, `source` (sheet name, ID, pulled_at), and `note` (for example "child rows excluded: 3 with blank baseline"). Templates print `note` beside the figure; that is how footnotes stay attached to their numbers.

## 3. Determinism and reproduction

- A run is identified by family, edition, ISO week, and the set of snapshot md5s; `qa.json` lists them.
- To reproduce an issued edition: check out the config version printed in the PDF properties, point `pull` at the archived snapshot folder (`--from-snapshots <folder>`), and run compute through pdf. The only allowed difference is the generation timestamp.
- Any change to a KPI formula bumps `config_version` and is noted in the next edition's source note ("mitigation past-target now excludes rows with mixed-format IDs; previous editions counted them").

## 4. Adding a family

Copy the skeleton, set `program` and `fam` per `csl-document-control` Section 1.1, list sources with IDs and column titles, define KPIs with denominators and rule IDs, write the page map, set page counts and cover style per `csl-brand/references/document-anatomy.md`, run once against a saved snapshot folder, run the brand QA checklist, and add the family to `references/report-catalog.md` and csl-operating-rules Section 4.

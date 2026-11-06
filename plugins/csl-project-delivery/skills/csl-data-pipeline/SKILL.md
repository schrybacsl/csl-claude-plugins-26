---
name: csl-data-pipeline
description: >
  Every data pull and data-QA step behind CSL reporting: Smartsheet and SharePoint reads through the
  organization connectors, snapshots with timestamp and md5, diffs against the last pull, freeze and
  silent-lapse detection, QA rules with tier IDs, the report factory, the chart library, rig
  telemetry, and the Graph repoint. Use it whenever someone says "pull the sheet", "did anything
  change", "is the tracker frozen", "diff this week vs last", "what moved", "why do the numbers
  differ", "snapshot", or "telemetry zip came in", whenever an xlsx or csv export is ingested, and
  before any csl-* skill cites a number.
---

# CSL Data Pipeline

Every number in a CSL deliverable traces to a pull made in this session, with a sheet name, an ID, a timestamp in ET, a row count, and an md5, or it does not go in. This skill defines the pull standard and snapshot layout, the Smartsheet specifics that make W77 pulls correct, the normalization and hashing that make two pulls comparable, the row-level diff that produces the "what moved" table, the QA rules with their tier IDs, the CTRW telemetry pipeline, the report-factory architecture that renders the WKR and PLN families, the chart library, the Microsoft Graph repoint plan for the client's SharePoint migration, and the scheduled-pull fallback. Tiers come from `csl-schedule-risk/references/tier-rules.md`; numbering and filing from `csl-document-control`; colors and page anatomy from `csl-brand`. What the pipeline protects is the owner's ability to defend a report eighteen months later: the snapshot next to the PDF is the evidence.

> **Claude organization environment.** In claude.ai the pull is a Smartsheet or Microsoft 365 connector read; the scripts in `scripts/` run in code execution on the saved snapshot (`--from-csv`), because the sandbox has no route to the Smartsheet or Graph APIs. Snapshot paths such as `outputs/<PROG>/pulls/...` describe the filing structure on the engagement SharePoint (filed on instruction, `csl-document-control`), not a local disk. Everything else in this skill, the normalization, hashing, diffing, QA rules, and tiering, applies unchanged. See `csl-operating-rules` Section 3.

---

## 1. Bottom line / when this runs

| Product | Cadence | Script | Feeds |
|---|---|---|---|
| Pull log block + snapshot (`.csv` + `.json` sidecar) per sheet | Sunday, Wednesday, Friday; on demand | `scripts/smartsheet_pull.py` | Every source note; every other product below |
| "What moved" diff (added / removed / changed, per-cell old -> new) + weekly change log | After every pull pair | `scripts/diff_pulls.py` | `csl-schedule-risk` what-moved table; `csl-weekly-reporting` A and C editions |
| Freeze check (md5 chain, frozen streak, tier) | Every pull | `scripts/freeze_check.py` | Headline when A4 or R5 fires |
| QA findings table (silent lapse, inverted dates, mixed IDs, missing baseline, duplicates, RPN arithmetic, schema drift) | Every pull | `scripts/qa_rules.py` | Data-defect footnotes; docket rows for the sheet owner |
| CTRW telemetry summary per rig (`CSL-W77-CTRW-<rig>-<yymmdd>` xlsx + PDF) | Friday, when the weekly zip arrives | `scripts/ctrw_pipeline_skeleton.py` pattern | `csl-permits-shutdowns` reconciliation; FM- notices via `csl-technical-docs` |
| Report-factory run (pull -> compute -> charts -> template -> PDF -> QA -> file) | Monday A, Wednesday B, Friday C and PLN editions | Family `config.yaml` (`references/report-factory-config.md`) | Issued PDFs with snapshots beside them |
| Standard figures | Inside factory runs; on demand | `scripts/chart_library.py` | WKR, memos, decks, dashboards |
| Graph repoint (adapter, dual-read, parity tests) | Migration window | `references/graph-repoint-plan.md` | Roadmap Insight Dashboard ingestion; factory pulls |

Three rules hold without exception, because they are the difference between a report and an opinion: never report from memory of a prior pull (re-pull, then compare); never trust a server-side filter on the W77 connector (pull the whole sheet, filter locally); never write to a client-owned sheet (proposed change lists only, csl-operating-rules Section 7). What the owner learns from this skill's outputs is which numbers moved, which did not and should have, and which cannot be trusted yet.

---

## 2. Inputs and pulls

### 2.1 Pull standard

Every pull records, at pull time and in this order: sheet name, sheet ID, pull timestamp (ET, `MM/DD/YY HH:MM ET` in prose, ISO with offset in the sidecar), row count (parents and children separately), column count, md5 of the normalized CSV, source (`smartsheet-sdk`, `smartsheet-rest`, `csv:<file>`), and whether the md5 matches the previous snapshot on file. Snapshots are saved to `outputs/<PROG>/pulls/<yyyy-mm-dd>/<sheet-id>.csv` with a `.json` sidecar carrying the same fields plus the column list; a second pull on the same day gets an `_HHMMSS` suffix rather than overwriting, because a same-day re-pull that differs is itself evidence. The pull log block (Section 4.1) is pasted into the deliverable's source note unchanged. A metric whose pull is missing from the source note is shown as "not available at <pull time>, source <name>" (csl-operating-rules Section 9), never filled from last week.

### 2.2 Smartsheet specifics (W77 workspace 1069369850652548)

| Point | Rule | Why |
|---|---|---|
| Access | The Smartsheet connector in CSL's Claude organization, enabled per user by IT. No API token is pasted into chat, a file, or a deliverable; if a connector is unavailable, say so and work from an attached export | Credentials stay with the connector (`csl-operating-rules` references/connector-map.md) |
| Path | Connector read of the full sheet, saved as the snapshot CSV, then the scripts run in code execution with `--from-csv`. Outside claude.ai (Claude Code on a CSL machine with an IT-issued token), the SDK or REST path in `smartsheet_pull.py` still works | The claude.ai sandbox cannot reach the Smartsheet API; the snapshot, hash, and diff method is identical either way, and the sidecar records `source: smartsheet-connector` |
| Filtering | Full sheet, always; filter dates, weeks, and statuses locally in pandas | The connector's server-side date filter returned wrong windows on W77; a local filter is reproducible from the snapshot |
| Values | `display_value` by default (what the sheet shows: `$1,500,000`, `45%`, `09/18/26`); `--values raw` for typed values | Normalization (3.1) makes both hash the same; display values match what counterparts read |
| Column map | By title, built from the sheet's `columns` at pull time; column IDs (for example Health 3755936387387268, RPN C 3192986433965956) are recorded in family config, never hard-coded in templates | Titles are what people rename; a renamed title is caught as schema drift (3.3) |
| Hierarchy | `_indent` derived from the `parentId` chain (0 = parent); roll-ups use parents only | The GET response does not reliably populate `indent`; child rows are phases (D/P, EXEC) and double count |
| Pagination | `pageSize=500`, loop `page` until `totalPages`; the Roadmap Master runs about 907 rows x 65 columns | A default page returns 100 rows and a silent truncation |
| Attachments and discussions | `--include attachments,discussions` adds count columns when a deliverable needs them | Attachment counts witness delivery on a row; discussions carry verbal rulings |
| Rate limits | Roughly 300 requests per minute per token; the scripts back off on 429 and 5xx and honor `Retry-After` | A failed page must never be skipped |
| Write-back | Never. Edits to a client sheet are drafted as a change list (row, field, value evidenced, evidence document) | csl-operating-rules Section 7; the tracker owner applies and the diff proves it |

The canonical read, whichever door is used (the script implements it; templates never do):

```python
sheet = client.Sheets.get_sheet(SHEET_ID, page_size=500, page=n)      # loop n until total_row_count
col = {c.id: c.title for c in sheet.columns}                          # map by title, at pull time
for row in sheet.rows:
    rec = {"_row_id": str(row.id), "_row_number": row.row_number,
           "_parent_id": str(row.parent_id or ""), "_indent": 0}      # _indent filled from the parentId chain
    for cell in row.cells:
        rec[col.get(cell.column_id, f"Col_{cell.column_id}")] = cell.display_value or cell.value
```

W77 sheets in weekly use: Roadmap Master 2025–2032 (1059284113641348), Roadmap weekly pull (1390098374414212), CSL Tasks (7673437876080516), SIPP Permits (289677048237956), ST CHW/PCW System Mitigation Plan (2158727850315652), Equipment Summary RPN (7673299942199172), Electrical Panel List Rev2 (3077374458417028), BGP trackers (the W77 engagement context file (`engagement-context-W77.md` in the W77 Claude Project) Section 2). Pull them in the order `csl-schedule-risk` Section 2 gives, because each step's QA uses the previous sheet as a witness.

### 2.3 Other sources

| Source | How it enters | Watch |
|---|---|---|
| Smartsheet xlsx or csv export attached by the user (`Sheet_-_J_2026_CSL_Tasks.xlsx`) | `smartsheet_pull.py --from-csv <file> --key "<title column>"` | Exports carry no row IDs, so the key is synthesized from the named columns and the sidecar says so; hierarchy survives only in xlsx outline levels, so pass `--indent-col` when one exists |
| Client extracts (CHAMPS Total Combined Assets, PO and invoice extracts) | Read as a snapshot; hashed; extract date recorded | Never edited; joined to (`csl-asset-data-cmms`, `csl-cost-change-control`) |
| CTRW weekly zip `RE__<date>_TR7__TR2__TR5_Data_.zip` | Section 3.6 pipeline | Both logger paths per rig; md5 every file |
| Scheduled exports (client-side Make or Power Automate, owned by IT) | Fallback when the connector is unavailable (3.10) | Claude reads the exported file; the source field says `make` or `flow` |
| Microsoft 365 / SharePoint | Microsoft 365 connector for reads; Graph adapter for the client's own hosted ingestion after migration (3.9) | Dual-read until parity is proven |

---

## 3. Method

### 3.1 Normalize, then hash

Normalize every cell before anything is compared or hashed (`pipeline_common.normalize_frame`, version 1): strip whitespace; blanks and NaN tokens become empty; US dates `M/D/YY` and `M/D/YYYY` become ISO `YYYY-MM-DD`; currency and thousands-separated numbers become plain decimals (`$1,500,000.00` -> `1500000`); percentages drop the sign (`45%` -> `45`). The md5 is taken over the normalized CSV text (LF line endings, sheet column order, no index). The consequence the owner cares about: a formatting change never shows as movement, and every md5 change is a value change. Exclude a column from the hash only with `--hash-ignore` and only when the sidecar records it (system columns such as `Modified` are legitimate to exclude when a test is about tracker content rather than tracker activity).

### 3.2 Diff: the "what moved" method

1. Read both snapshots, normalize, and key by `_row_id`; fall back to a composite `--key` (title plus START, or the WS number) when an export has no row IDs. Duplicate keys are counted and reported as a data defect, not silently collapsed.
2. Classify rows: added (key only in the new pull), removed (only in the old), changed (any compared cell differs). For changed rows record every cell as old -> new with a delta (numeric difference, or days for dates).
3. Report schema drift first: columns present in one pull and not the other stop the run until the sheet owner confirms the rename, because every KPI downstream is keyed by title.
4. Write `added.csv`, `removed.csv`, `changed_cells.csv`, `diff_summary.json`, and `what_moved.md` (Section 4.3), and append one line to the sheet's running change log `outputs/<PROG>/pulls/changelog_<sheet-id>.csv` (old and new pull, md5s, identical flag, counts, drift flag). The change log is what answers "when did that row last move" without re-diffing a quarter of snapshots.
5. Hand the table to `csl-schedule-risk`, which fills tier, cause, owner, and next action. The script never assigns a tier to a moved row; the analyst does, with the rule ID.

What the owner learns: exactly which rows and fields moved between two dated pulls, with the evidence columns filled by code and the judgment columns filled by a named person.

The Friday sequence for W77, in the order the witnesses are needed (`PULLS=outputs/W77/pulls`):

```
python3 scripts/smartsheet_pull.py --sheet-id 1059284113641348 --out-dir $PULLS --program W77 --sheet-name "W77 Roadmap Master 2025-2032"
python3 scripts/smartsheet_pull.py --sheet-id 2158727850315652 --out-dir $PULLS --program W77 --sheet-name "ST CHW/PCW System Mitigation Plan"
python3 scripts/smartsheet_pull.py --sheet-id 289677048237956  --out-dir $PULLS --program W77 --sheet-name "SIPP Permits"
python3 scripts/smartsheet_pull.py --sheet-id 7673437876080516 --out-dir $PULLS --program W77 --sheet-name "CSL Tasks"
python3 scripts/freeze_check.py --sheet-id 1059284113641348 --pulls-dir $PULLS --last 8 --field-movement "<permits started/closed, deliveries, minuted closures>"
python3 scripts/diff_pulls.py --old $PULLS/<last Friday>/1059284113641348.csv --new $PULLS/<today>/1059284113641348.csv --parents-only
python3 scripts/qa_rules.py --current $PULLS/<today>/2158727850315652.csv --previous $PULLS/<last Friday>/2158727850315652.csv \
    --end-col "Target Date" --id-col "WS #" --id-regex "^WS-\d{2}\.\d{2}(\.\d{2})?$" --baseline-col "Baseline Status" --out $PULLS/<today>/qa_2158727850315652.csv
```

Offline (an attached export, no token): add `--from-csv <file> --key "<title column>"` to the pull and run the same freeze, diff, and QA commands on the snapshots it writes.

### 3.3 QA rules and tiers

| Test | Condition | Tier (rule) | Script behavior |
|---|---|---|---|
| Frozen, one pull | md5 identical to the previous pull | AMBER (A4) | `freeze_check.py`; name the rows expected to move |
| Frozen, two or more pulls, field moved | md5 identical across >= 2 consecutive pulls while permits started or closed, deliveries landed, or minuted actions closed | RED (R5) | `freeze_check.py --field-movement "<witnesses>"`; headline attributed to the tracker |
| Frozen, two or more pulls, no witness | Same, no field witness | AMBER (A4) held open | Witnesses sought before R5 |
| Silent lapse | END passed; not closed; % and status unchanged since the previous pull; no constraint or comment | RED (R4) | `qa_rules.py --previous` |
| Past END with constraint | As above with a constraint picklist value | AMBER (A3) | Age the constraint; over two weeks stays A3 with the enabling owner named |
| Past END, moving or untested | Progress or status moved but not closed; or no previous pull | AMBER (A2) | R4 stays untested until a previous pull exists |
| Inverted dates | START after END (SIPP 54164 on 09/18/26) | AMBER (A6) | Correction requested; gate count still reported |
| Mixed ID formats | `WS-22.01.01` and `WS209` in one column | AMBER (A6), population | Nonconforming rows excluded from roll-ups with a footnote |
| Missing baseline | Baseline status or dates blank (mitigation child rows) | AMBER (A6), population | Rows cannot roll up against baseline; docket item for the sheet owner |
| Duplicates by key | Same permit number, WS number, or asset code twice | AMBER (A6) | Listed; the roll-up uses one |
| RPN arithmetic | RPN C not equal to SEV x Occ x Det | AMBER (A6) | Tracker conflicting with itself |
| Schema drift | Column renamed or missing since the previous pull | STOP | `qa_rules.py` exits 2; confirm the map before any roll-up |

The population rule of `tier-rules.md` applies: one finding per data condition with the count and examples, never forty AMBER rows for one defect.

### 3.4 Freeze check and field witnesses

Run `freeze_check.py` on every sheet after every pull. The script computes the streak; the analyst supplies the witnesses, because a sheet cannot testify about the field. Witnesses come from other sheets pulled in the same session (SIPP Permits started or closed, CSL Tasks closures), from transmittals, and from minutes. The W77 Roadmap Master was byte-identical for six consecutive pulls through 09/18/26 while permits 53782 (started 09/16/26) and 51718 (closed 09/18/26) moved; WKR-38C carried it as RED (R5) with a change list of the rows that should have moved. Attribute the frozen state to the tracker ("the roadmap has not changed in six pulls"), never to the field ("no work occurred").

### 3.5 Export ingestion

An attached export is a pull like any other: ingest with `--from-csv`, key it, hash it, snapshot it, and diff it against the previous export of the same sheet. Record the export's own timestamp (file properties or the user's statement) beside the ingestion timestamp, because the two differ and the report must say which one governs. Two exports with the same md5 are one export (`csl-document-control` Section 7.3).

### 3.6 Telemetry pipeline (CTRW test rigs)

Facts the pipeline encodes: three rigs, one logger each, TR7 (m4535, 35 channels), TR2 (m8357, 35 channels), TR5 (m5794, 25 channels, no bath instrumentation); a weekly zip `RE__<date>_TR7__TR2__TR5_Data_.zip` of PDF-export logs; each logger alternates between a CT share path and a disk3 path with zero timestamp overlap, so a single-path read shows "dark" weeks that are not dark; cadence is mixed 30 and 60 seconds; TR7 carries a chronic coolant loss on the order of 0.12 to 0.15 L/day (the W77 engagement context file (`engagement-context-W77.md` in the W77 Claude Project)), TR2 has been dark since 07/19/26 with bath instrumentation electrically faulted, TR5 is intermittent.

Module structure: `ctrw_lib.py` holds `parse_log` (channel-count-aware; a short channel set is recorded, not fatal), `detect_resends` (md5 per file against a registry), `merge_paths` (both paths, overlap counted, one row per timestamp), `classify_dark_windows`, `detect_refills`, `drawdown_regression`, `uptime_minutes`, `valve_saturation`, `zero_flow_events`, `compute_metrics`; `pipeline.py` orchestrates unzip -> resend check -> parse both paths per rig -> merge -> classify -> metrics -> formula-driven xlsx + branded PDF. `scripts/ctrw_pipeline_skeleton.py` carries both layers and runs offline (`--demo`). The signatures other code depends on:

```python
detect_resends(files, registry_path) -> DataFrame[file, md5, bytes, class, resend_of]
parse_log(path, rig, ts_col, source) -> DataFrame (+ attrs["channel_check"] = {expected, found, ok})
merge_paths(frames) -> (merged DataFrame, {"overlap_timestamps", "sources": {path: rows, start, end}})
classify_dark_windows(merged, spans, single_frames, cadence_s, min_gap_min=5, midnight_tol_min=30, boundary_tol_h=6)
    -> DataFrame[start, end, duration_min, class, evidence]
drawdown_regression(df, refills, min_points=20, min_volume_l) -> {slope_l_per_day, r2, n, runway_days, tier, ...}
uptime_minutes(df, window) -> {minutes_with_data, window_minutes, uptime_pct}
valve_saturation(df, hi=95, lo=5) -> {saturated_pct, longest_saturated_min, watch}
zero_flow_events(df, tol=0.05) -> {zero_flow_samples, first, last, tier}
```

| Step | Rule | What the owner learns |
|---|---|---|
| Resend check | md5 every file; identical hash = not new data | Whether the week's zip added anything |
| Parse | One frame per file with `_source` and `_file`; PDF exports via `pdftotext -layout` then column mapping | Channel completeness per rig |
| Merge | Concatenate both paths; report overlap; keep one row per timestamp | Coverage per path with start and end |
| Classify gaps | Threshold = max(5 min, 3 x longest cadence). `midnight_cut_artifact`: short gap straddling 00:00. `export_artifact`: gap at a file boundary within tolerance, or a single-path gap covered by the other path. `true_dark`: the rest | Dark hours by class; only `true_dark` counts as an outage |
| Refills | Step increase in reservoir volume above 0.5 L between samples | Segments for regression |
| Drawdown | OLS of volume on days since the last refill: L/day, R², n; runway = (current median volume - minimum safe volume) / loss per day | Runway < 90 days RED (R9); falling but >= 90 AMBER (A1); not falling GREEN (G) |
| Uptime | Minutes with at least one sample / window minutes | The KPI the dashboard shows |
| Valve watch | Share of samples at >= 95% or <= 5% and the longest saturated run | A saturated valve is a control loop out of authority |
| Zero flow | Samples at or below tolerance | R9 candidate; facilities notice via `csl-technical-docs` |

Outputs per rig: `CSL-W77-CTRW-<rig>-<yymmdd>.xlsx` (raw data sheet plus a Metrics sheet whose slope, R², runway, and uptime are live formulas, so a reviewer audits the arithmetic in the workbook) and the branded PDF from the report factory, with merged data, dark-window table, and metrics JSON saved beside them.

### 3.7 Report factory

One `config.yaml` per report family (annotated example in `references/report-factory-config.md`): sheets with IDs and the columns each stage needs, KPI definitions with formula, denominator, threshold, and rule ID, the page map, cover style, distribution, and QA thresholds. Stages run in a fixed order and each writes to disk so a failed run is resumable: pull (Section 2; snapshots) -> compute (KPIs, diffs, QA; a `metrics.json`) -> charts (`chart_library.py` with `brand_tokens.apply_matplotlib_style`; PNG at 200 dpi) -> template (HTML with `brand-tokens.css`, or ReportLab for table-heavy pages) -> PDF (Playwright/Chromium, Letter portrait, 0.75 in margins) -> QA (`pdffonts` shows the Avenir subset or the declared fallback; page count within the family's range; grep of the HTML and PDF text for `C8102E` and for `BF311A` outside the logo; every tier word paired with a rule ID) -> file (`outputs/<PROG>/<FAM>/<yyyy>/<DOC>_<yyyy-mm-dd>.pdf`, superseded editions moved to `_superseded/`, the pull snapshots and `metrics.json` copied beside the PDF). Determinism is a requirement: the same snapshot set produces the same PDF apart from the generation timestamp, which is why nothing in a template calls the API and nothing hard-codes a sheet ID (it reads the config). Stage contract, so a failure is located in one stage and the run resumes there:

| Stage | Reads | Writes | Fails the run when |
|---|---|---|---|
| pull | `config.sources` | `pulls/<date>/<id>.csv` + `.json` | A sheet is unreachable and no fallback snapshot is authorized in the session |
| compute | snapshots, previous edition's snapshots | `metrics.json`, `what_moved.md`, `qa_findings.csv` | Schema drift; a KPI's denominator is zero or its source column is missing |
| charts | `metrics.json` | `fig<nn>_<slug>.png` at 200 dpi | A figure lacks a source line or a title |
| template | `metrics.json`, figures, `config.page_maps` | `report.html` (or ReportLab story) | A page-map section has no data and no "not available" statement |
| pdf | `report.html` + `brand-tokens.css` | `<DOC>_<date>.pdf` | Playwright fails to embed the declared font |
| qa | the PDF | `qa.json` | `pdffonts` shows an unapproved face; page count out of range; legacy red found; a bare tier word |
| file | everything above | `outputs/<PROG>/<FAM>/<yyyy>/` + `_superseded/` | The document number already exists without a revision bump |

Determinism rules: no stage calls the API except pull; every random or time-dependent value is fixed by the snapshot timestamp; figures are regenerated from `metrics.json`, never hand-placed; the config is versioned with the family and the version prints in the PDF properties. Re-running the factory on last week's snapshot folder must reproduce last week's PDF, which is how a disputed figure is defended.

| Day | Editions | Sequence |
|---|---|---|
| Monday | WKR-nnA (10 pages) | Sunday pulls -> freeze -> diff -> `csl-schedule-risk` framing -> factory -> brand QA -> number check |
| Wednesday | WKR-nnB (5 pages, white background, official palette) | Wednesday pulls -> KPI refresh (`csl-dashboard-kpi`) -> factory -> QA |
| Friday | WKR-nnC (8 to 11 pages), PLN-SUM, PLN-EWO, CTRW per rig | Friday pulls -> QA rules -> permits, cost, asset skills -> factory -> QA -> filing with snapshots |

Every run ends with `csl-brand/references/brand-qa-checklist.md` and the `csl-document-control` number check.

### 3.8 Chart library

Standard figures and their data contracts (all in `scripts/chart_library.py`; titles state the finding; source line stamped under every figure; series in brand order; tier colors only on tier-coded marks and always with the word):

| Figure | Contract (columns) | Used in |
|---|---|---|
| Permit gates cleared vs started per week | week, started, gated_in_time | WKR-C permit board |
| Mitigation open vs past-target with closures | week, open, past_target, closures | WKR-C mitigation section |
| Closures per week | week, closures | WKR-C, memos |
| Roadmap health distribution | health -> count | WKR-C roadmap section; dashboards |
| RPN watchlist bar, >= 700 highlighted, threshold hairline | item, rpn, mitigation | WKR-C risk; memos |
| Frozen-weeks indicator | [{date, identical}] from the freeze chain | WKR headline block |
| CSL board Reds and anchors closed | week, reds, anchors_closed | WKR-C CSL board |
| Forecast vs budget by E-GRP with variance % and rule marks | egrp, budget, forecast | WKR-C commercial; quarter close |
| Quarterly cash flow vs plan with cumulative lines | quarter, plan, actual | Quarter close; cost memos |
| Rig flow and valve time series, stacked panels, dark windows shaded | timestamp, flow_lpm, valve_pct (+ dark windows) | CTRW PDF |
| Reservoir drawdown with regression line and runway annotation | timestamp, volume_l (+ fit, refills, minimum volume) | CTRW PDF; FM- notices |

`python3 scripts/chart_library.py --demo --out-dir <dir>` renders all eleven from synthetic data labeled DEMO for template work; a demo image never appears in an issued document.

### 3.9 Microsoft Graph repoint (SharePoint migration)

The client has decided to move the sheets to SharePoint; dashboard and factory ingestion repoint from the Smartsheet API to Microsoft Graph without changing any downstream contract. The plan (`references/graph-repoint-plan.md`): a `SheetSource` adapter with `pull(sheet_ref) -> DataFrame` implemented by `SmartsheetSource`, `GraphExcelSource` (workbook table rows via Graph), and `SharePointListSource` (list items with expanded fields); an Entra ID app registration with delegated permissions for interactive CSL use and application permissions (`Sites.Selected`) for the scheduled factory; incremental change tracking through delta queries; dual-reading both sources during the migration so the Roadmap Insight Dashboard never goes dark; and a two-week parity test (row count, normalized checksum, KPI values) before cutover. The adapter is why the migration touches one module and not every template:

```python
class SheetSource(Protocol):
    def pull(self, sheet_ref: SheetRef) -> pd.DataFrame: ...      # normalized frame with _row_id, _indent
    def changes_since(self, sheet_ref: SheetRef, token: str) -> tuple[pd.DataFrame, str]: ...  # delta + new token

SmartsheetSource(token_env="ASMLW77")                 # today
GraphExcelSource(site_id, drive_id, item_id, table)   # workbook table rows via Graph
SharePointListSource(site_id, list_id)                # list items with expanded fields; delta supported
```

`SheetRef` carries both the Smartsheet ID and the Graph coordinates during dual-read, and the sidecar records which source produced the snapshot.

### 3.10 Scheduled pulls and hosted ingestion

Claude does not schedule anything. Where a program needs an unattended pull (the W77 Make scenarios `get_w_77_roadmap_sheet` and `_v_2`), it runs client-side or in a CSL automation owned by IT, and writes into the same snapshot layout with `source: make`; Claude reads those files like any other snapshot, and the diff and freeze checks run unchanged. Hosted dashboard ingestion (Replit or a client server) is governed by `csl-dashboard-kpi`; any hosting platform for client data must be on the CSL Approved AI Tools Register or cleared by IT (`csl-ai-policy` Section 6).

### 3.11 When the numbers differ

Two figures for the same thing (factory versus dashboard, CSL versus a counterpart's recap, this week versus last) are reconciled in this order, and the report states which step explained it:

1. Same snapshot? Compare the pull log blocks: sheet ID, timestamp, md5. Different md5s mean different data, and the later pull governs unless the deliverable is dated to the earlier one.
2. Same population? Parents only versus all rows; open versus open-plus-closed; a filter applied on one side (the quarterly-sum test in `csl-cost-change-control` found child rows summed into quarterly columns).
3. Same definition? Denominator, closed values, as-of date, time zone. "Past target" on the sheet's target date versus a minuted date is two KPIs, not one.
4. Same normalization? A currency or percent format, a two-digit year, a trailing space.
5. A data defect? Mixed IDs, duplicates, a renamed column; the QA table names it.
6. Still different: report both figures with their provenance, name the discrepancy, and put the resolution on the docket with the sheet owner. Never average, never pick silently.

---

## 4. Output specification

**4.1 Pull log block** (printed by `smartsheet_pull.py`; pasted into source notes):

```
PULL      <sheet name> (<sheet id>)
pulled_at MM/DD/YY HH:MM ET   source smartsheet-sdk | smartsheet-rest | csv:<file> | make
rows      <n> (parents <p>, children <c>)   columns <k>
md5       <32 hex> (normalized CSV[, ignoring <cols>])
previous  <yyyy-mm-dd> md5 <short>  IDENTICAL | changed | none on file
snapshot  outputs/<PROG>/pulls/<yyyy-mm-dd>/<sheet-id>.csv (+ .json)
```

**4.2 Snapshot files.** `outputs/<PROG>/pulls/<yyyy-mm-dd>/<sheet-id>.csv` and `.json`; sidecar fields: program, sheet_name, sheet_id, pulled_at (ISO with offset), pulled_at_display, source, values, row_count, column_count, parent_rows, child_rows, md5, md5_ignore_cols, columns, server_side_filters, previous {date, md5, identical}, notes. Never edited after the pull.

**4.3 What-moved table** (`what_moved.md`): headline line (last pull, this pull, md5s, hash identical or changed, counts), schema-drift and duplicate-key warnings, then `Row / ID | Field | Last pull | This pull | Delta | Tier (rule) | Cause | Owner | Next action, date`, then the source line. The last four columns are the analyst's; the table is not issuable until they are filled (`csl-schedule-risk` Section 4).

**4.4 QA findings table.** `Tier (rule) | Scope (row or population) | Row / ID | Detail | Evidence`, sorted STOP, RED, AMBER; counts by tier in the header; CSV with `--out` filed beside the snapshot.

**4.5 Freeze check.** Table of pull, md5, rows, columns, identical-to-previous; the streak; the tier and reason; the sentence form from `tier-rules.md` Section 4 with the rows and witnesses to be named.

**4.6 CTRW.** `CSL-W77-CTRW-<rig>-<yymmdd>.xlsx` and `.pdf` per rig, plus `_merged.csv`, `_dark-windows.csv`, `_metrics.json`, `_summary.md` beside them; bottom line first (loss rate, R², runway, tier, uptime, true dark days).

**4.7 Factory outputs.** `outputs/<PROG>/<FAM>/<yyyy>/<DOC-NUMBER>_<yyyy-mm-dd>[_R<n>].pdf` with the run's snapshots and `metrics.json` in a sibling folder of the same stem; superseded files in `_superseded/` with their revision intact (`csl-document-control` Section 6).

---

## 5. Voice and formatting rules

- Pull facts are stated as pull facts: "Roadmap Master 1059284113641348 pulled 09/18/26 06:40 ET, md5 identical to 09/11/26", never "the roadmap is unchanged".
- Counts carry both parts: "17 of 20 open rows", "907 rows (268 parents)", "19,891 of 20,160 minutes".
- Dark windows are named by class in prose ("4.0 hours true dark; 0.5 hours export artifacts"), never summed into one "downtime".
- Regression results carry n, R², and the segment ("0.140 L/day over 13,896 samples since the 08/22/26 refill, R² 0.99").
- Two sources that disagree are both stated with the discrepancy named; nothing is averaged or picked silently.
- Client-executive editions spell out acronyms on first use per page and avoid dash constructions in running prose (`csl-brand` Section 7).
- Illustrative values in examples are labeled as such; the live figure comes from this session's pull.

---

## 6. Worked example: Friday 09/18/26 pulls behind WKR-38C

Pull log for the four live sheets (timestamps from the WKR-38C source note; row counts and hashes illustrative, shown for shape):

```
PULL      W77 Roadmap Master 2025–2032 (1059284113641348)
pulled_at 09/18/26 06:40 ET   source smartsheet-sdk
rows      907 (parents 268, children 639)   columns 65        [illustrative counts]
md5       3f6c0a91…9a1e (normalized CSV)
previous  2026-09-11 md5 3f6c0a91…9a1e  IDENTICAL            -> freeze streak 6, RED (R5) with witnesses below
PULL      ST CHW/PCW System Mitigation Plan (2158727850315652)
pulled_at 09/18/26 06:41 ET   source smartsheet-sdk
rows      61 (parents 12, children 49)   columns 24            [illustrative counts]
md5       b81d44c2…07f3   previous 2026-09-11 md5 a02e…c4d1  changed
PULL      SIPP Permits (289677048237956)      pulled_at 09/18/26 06:42 ET   previous changed (1 row added, 1 closed)
PULL      CSL Tasks (7673437876080516)        pulled_at 09/18/26 06:43 ET   previous changed
```

What-moved excerpt after the analyst filled the judgment columns (`csl-schedule-risk` Section 6 carries the full table):

| Row / ID | Field | Last pull (09/11) | This pull (09/18) | Delta | Tier (rule) | Cause | Owner | Next action, date |
|---|---|---|---|---|---|---|---|---|
| Roadmap Master, all parent rows | md5 | identical to 09/04 | identical; sixth frozen pull | 0 cells | RED (R5) | Tracker not maintained while SIPP 53782 started 09/16 and 51718 closed 09/18 | Roadmap owner (ASML) via client program lead | Change list issued with WKR-38C; review Tue 09/22 |
| Mitigation sheet, past-target count | derived | 15 | 17 | +2; 0 closures | AMBER (A2) | Two targets passed in the week | Row owners | Owner-by-owner review at the Planon weekly |
| SIPP 54164 REMA pump | START / END | not on board | START 2026-10-12, END 2026-10-09 | new row | AMBER (A6) | Inverted dates on a new permit | Permit coordinator | Correction requested 09/18; gates 3 of 5 |
| SIPP 51718 tie-in | Status | Open, 39 days | Closed 09/18, 46 days | closed | GREEN (G) | Gates complete | Contractor PM | None |

QA findings on the mitigation pull: mixed ID formats (`WS-22.01.01` and `WS209`) AMBER (A6) population, nonconforming rows footnoted out of the past-target denominator; blank baseline status on child rows AMBER (A6) population, docket item for the sheet owner. What the owner learns from the page: the two REDs are tracker-governance conditions with a named fix, the mitigation movement is two lapses and no closures, and the permit board is clean apart from one data-entry defect.

---

## 7. Failure modes and how to avoid them

| Failure | What it looks like | Avoidance |
|---|---|---|
| Reporting from a stale snapshot | Friday figures that match Wednesday's because nothing was re-pulled | Pull in-session; timestamp in the block; `previous` line checked |
| Trusting server-side filters | A "this week" permit list missing rows that started Thursday | Full pull, local filter; the sidecar records `server_side_filters: none` |
| Double-counting child rows | Portfolio budget 21% above the parent sum | Parents only for roll-ups; `parent_rows` stated in the block |
| Treating an export artifact as an outage | "TR7 dark 36 hours" when disk3 held the data | Both paths merged; gaps classified; only `true_dark` reported as dark |
| Averaging conflicting sources | Tracker END and minuted date blended into "mid-September" | Both stated with provenance (`csl-schedule-risk` 3.4) |
| Renaming columns silently | KPI drops to zero after the sheet owner renamed `Baseline Status` | Schema drift stops the run; config updated with the rename dated |
| Hard-coding sheet IDs in templates | Migration breaks every report | IDs in family config; templates read config only |
| Hash without normalization | A currency reformat reported as movement | Normalize first (3.1); version recorded in the sidecar |
| Tiering rows by script | Forty AMBER rows for one data defect | Population findings; the analyst tiers moved rows |
| Losing the snapshot | A disputed report with no data beside it | Snapshot and `metrics.json` filed with the PDF (`csl-document-control` Section 8) |

---

## 8. Pre-issue checklist

- Every sheet the deliverable cites was pulled in this session; pull log blocks pasted into the source note with ET timestamps.
- Snapshot `.csv` and `.json` written for every pull; sidecar `previous` line read and the freeze check run.
- Diff run against the last edition's snapshot; what-moved table filled with tiers and rule IDs by the analyst.
- QA findings reviewed; population defects footnoted out of denominators; schema drift cleared before any roll-up.
- Parent-only roll-ups stated as such; row counts with denominators.
- Telemetry: both paths merged, dark windows classified, regression stated with n and R², runway tier cited.
- Factory QA passed: fonts confirmed with `pdffonts`, page count in range, no `C8102E`, no `BF311A` fill, every tier word paired with a rule ID.
- Outputs filed per `csl-document-control` with snapshots beside the PDF; superseded editions moved, not deleted.
- No token, path secret, or personal data in any output or log.

---

## Files in this skill

- `scripts/pipeline_common.py` — shared normalization, md5, ET timestamps, snapshot read/write, snapshot discovery.
- `scripts/smartsheet_pull.py` — full pull (SDK or REST, or `--from-csv` offline) with column map, `_indent`, display values, snapshot and sidecar, pull log block.
- `scripts/diff_pulls.py` — row-level diff by key; added / removed / changed CSVs; `what_moved.md`; running change log.
- `scripts/freeze_check.py` — md5 chain across the last N snapshots; frozen streak; tier with rule ID and sentence form.
- `scripts/qa_rules.py` — silent lapse, inverted dates, mixed ID formats, missing baseline, duplicates, RPN arithmetic, schema drift; findings table with tier IDs.
- `scripts/chart_library.py` — the eleven standard figures with brand tokens and stamped source lines; `--demo` renders labeled samples.
- `scripts/ctrw_pipeline_skeleton.py` — parse / merge / classify / metrics skeleton with the dark-window classifier and drawdown regression implemented; `--demo` runs end to end offline.
- `references/report-factory-config.md` — annotated `config.yaml` for the WKR family and the stage contract.
- `references/graph-repoint-plan.md` — adapter interface, Entra ID registration, delta queries, dual-read, parity test plan, cutover.

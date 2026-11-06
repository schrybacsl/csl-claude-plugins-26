# W77 KPI Set (reads with formulas and columns)

| KPI | Formula | Sheet / columns | Threshold → tier |
|---|---|---|---|
| Permits gated in time | count(started in window AND gates_cleared = gates_total before START) / count(started in window) | SIPP: Start Date, Workflow Status, gate columns | < 100% → AMBER (A6); work with no record → RED (R6) |
| Perfect-week streak | consecutive weeks with gated in time = 100% and no R6 | derived | informational |
| Permits closed, duration | Finish − Start for rows closing in window | SIPP: Start/Finish Date | informational; > 45 days noted |
| Roadmap rows moved | rows with any changed cell vs previous snapshot | Roadmap diff | 0 for 1 pull AMBER (A4); ≥ 2 pulls with field movement RED (R5) |
| RPN ≥ 700 without mitigation | rows where RPN C ≥ 700 and (Owner blank OR no dated action OR action date passed) | Roadmap: RPN C, Owner, Constraints, General Comments | ≥ 1 → RED (R1) |
| Health distribution | count by Health | Roadmap: Health | informational |
| Behind baseline % | rows with Variance2 < 0 / parent rows | Roadmap: Variance2 | trend |
| Mitigation open | rows Status not Closed | Mitigation: Status | informational |
| Mitigation past target | open rows with Target Date < pull date | Mitigation: Target Date, Status | growth week over week → AMBER (A2) |
| Closures | rows moved to Closed in window | Mitigation: Status, Modified | 0 for ≥ 2 weeks → headline |
| Owner load | max open rows per Assigned To | Mitigation: Assigned To | ≥ 50% on one owner → note |
| WS-22 pipeline | steps complete of 10 per project; committed $ vs planning budget | Mitigation: step columns, PO In Place; Containment Budget Tracker | step 9 stalled > 2 wks → AMBER (A3) |
| CSL Reds | rows Health = Red; age since last modified | CSL Tasks | age > 14 days → note |
| Board byte-identity | md5 unchanged vs previous pull | `freeze_check.py` | A4 / R5 |
| Program deliveries | records delivered, by file and convention | PLN register | informational |
| Gates / confirms open | count G-nn open; confirms > 5 business days | PLN-EWO, confirm register | > 5 bd → AMBER (A5) |
| Rig state | per `ctrw_pipeline_skeleton.py` (runway < 90 d RED (R9); dark > 7 d RED (R9); valve saturation > 90% AMBER (A1)) | CTRW | as stated |
| Days to hard deadline | 10/30/26 − pull date | calendar | < 30 days → weekly countdown on page 2 |

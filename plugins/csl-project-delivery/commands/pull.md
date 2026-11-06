---
description: Pull a tracker through the connector, snapshot it, and report what moved
argument-hint: "[sheet name or ID] [compare to: last pull | date]"
---
Load `csl-data-pipeline` and `csl-schedule-risk`. Target: $ARGUMENTS

Read the full sheet through the Smartsheet (or Microsoft 365) connector. Save it as the snapshot CSV, then in code execution run the normalize, hash, freeze-check, diff, and QA scripts with `--from-csv`. Report: pull block (sheet, ID, time ET, rows, md5, source), byte-identical or not, the what-moved table, and QA findings with tiers. Never write to the sheet; propose a change list if corrections are needed.

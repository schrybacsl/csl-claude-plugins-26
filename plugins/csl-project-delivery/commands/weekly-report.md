---
description: Build this week's WKR edition (A look-ahead, B mid-week, C end-of-week)
argument-hint: "[A|B|C] [program code]"
---
Load, in order: `csl-ai-policy`, `csl-data-pipeline`, `csl-schedule-risk`, `csl-weekly-reporting`, `csl-document-control`, `csl-brand`. Edition and program: $ARGUMENTS

1. Read the engagement context file for the sheet registry, distribution, and thresholds.
2. Pull every registered sheet through the connector now; record the pull block. Do not reuse any prior number.
3. Run freeze, diff, and QA; tier findings with rule IDs; check the ten triggers in `csl-operating-rules` Section 6 and flag any that fire before writing narrative.
4. Build the edition to its page map; write the headline last, place it first.
5. Deliver as PDF with the two-sentence summary, the QA exceptions, the source-marking table, and the named-reviewer line.

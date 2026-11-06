# Stakeholder Register

One row per person with decision rights or standing on the program. It answers "who should be copied", "who owns that decision", and "when did we last hear from them" before any draft goes out, and it is the source for the To / Cc lines in every pattern in `csl-client-comms`. Maintain it in the program workspace (Smartsheet or the program's SharePoint list) and refresh last-contact dates from the mailbox before drafting an escalation. Client and vendor names come from the engagement context file (`csl-operating-rules` Section 5) and the minutes; CSL names and titles from `csl-people`. The register holds work roles and program facts only; nothing personal about anyone.

---

## Schema

| Column | Content | Rule |
|---|---|---|
| Name | Initials-style in the register (`B. Gannon`); full name on first reference in a record | Verified against the source list |
| Org | Client organization and unit, vendor, or CSL | As the client names its units (CRE, CoE) |
| Role | Program role, not job title alone | "Client data owner (Planon structure and imports)" |
| Decision rights | What this person can decide without going higher | The basis for To versus Cc |
| What they care about | The two or three things this person asks about first | Drives the lead sentence of any email to them |
| Preferred channel | Email, Teams, ticket, meeting | Use it; note exceptions |
| Cadence | How often CSL is in contact by design | Weekly meeting, per ticket, per SOP |
| Last contact | Date and forum of the last substantive exchange | Refreshed before escalations |
| Open items | Items this person owes or is owed, by document number | Mirrors the open-confirm register and docket |

Optional columns for larger programs: escalation level (1, 2, 3 in the client's own order); time zone; delegate when out of office; contract role (Owner, A/E, CM, vendor).

## W77 excerpt (as of 09/30/26; refresh last-contact from the mailbox before use)

| Name | Org | Role | Decision rights | Cares about | Channel | Cadence | Last contact | Open items |
|---|---|---|---|---|---|---|---|---|
| B. Gannon | ASML CRE | Client program lead | Program scope, Planon realignment, dashboard views, BCA + IRO merge | Reliability record, executive visibility, 10/30/26 hierarchy date | Email; Planon weekly | Weekly | 09/29/26 Planon weekly | LOE proposal for the BCA + IRO merged source; REDM 10/01/26 |
| T. Dube | ASML | Client data owner (Planon structure and imports) | Functional code structure, template class, import acceptance | Import success on unaltered templates | Email; Planon weekly | Weekly | 09/29/26 (root cause stated) | Versioned structure spec (G-13); template class ruling; rejection log |
| E. Koning | ASML CRE | Client engineering lead; command dashboard recipient | KPI selection for his view | Utility and telemetry signals | Email | As needed | Per mailbox | KPI options menu v1.1 selections |
| P. Gorman | ASML | Technical reviewer (SOPs); WKR-B/C recipient | SOP approval | Procedure accuracy | Email | Per SOP | Per mailbox | W77-SOP-GFC-001 review |
| J. Vigo | ASML CRE | Controls and BMS manager | Dashboard hosting ticket on the client side | Security review, hosting path | Email; ticket REQ 999 / RITM5248681 | Per ticket | 09/14/26 scoping call thread | Entra ID app registration; hosting decision |
| J. de Boer | ASML CoE | Product Owner Building Automation | Deployment approach for the dashboard | Fit with the building-automation platform | Teams call; email | Per milestone | 09/14/26 scoping call | Deployment approach decision |
| A. Pfordresher | ASML CRE | CRE PM, IN 12896 | Change management on WS-22.08 | CAAR path | Email | Per project | Per mailbox | Design CAAR on the CARR tracker |
| B. Nolan | ASML | Loops / B20 | Loop taxonomy questions on the PML board | Loops hierarchy | Planon weekly (loops sessions) | Per session | Per minutes | Loops PML R0 review |
| E. Dean | ASML | GFC direction (via the data owner) | Functional code direction | Code stability | Via T. Dube | Per ruling | Per minutes | Versioned spec |
| J. Poulos / J. Castaneda / T. Kuzmich | ASML | CHW piping escalation recipients | Piping strategy path | Wall-loss findings; REDM 10/01/26 | Email; REDM | Per milestone | Per FM-W77-UTM-0903 R2 | PDS for the piping strategy |
| E. Hubert | CSL | Project Director | CSL positions, fee, escalation | Record integrity, client relationship | Teams; weekly 1:1 | Weekly | This week's 1:1 | LOE review before issue |
| S. Kazantzidis | CSL | Technical PM; "prepared for" on WKR-B/C | Executive report sign-off | Report accuracy | Email | Wed / Fri | WKR-40B | None |
| D. Wolf | CSL | On-site PM | Notices, budget tracker, WS co-ownership | Field record, blocked POs | Teams; on site | Daily | This week | WS-06.02 PO; FM-W77-UTM R2 |
| N. Grubler | CSL | APM; Planon meeting issuer | Agenda and minutes content | Clean minutes | Teams | Weekly | This week | Minutes corrections; intake tracker |

Vendors and partners (Emcor, HaSe, Nalco/Ecolab, Vanderweil, MMI, Brady, Jacobs, BR+A) are added by named contact when a thread with them opens; until then the firm and its role are carried on one row each with no name.

## Maintenance

- Add a row the first time a person appears in minutes or on a thread with a decision or an ask.
- Update decision rights when a client reorganization or a minuted delegation changes them; cite the minutes item.
- Refresh last-contact before any escalation and at the Friday edition.
- Open items mirror the open-confirm register and the docket; an item closes in both or in neither.
- Review the standing distribution lists (the engagement context file (`csl-operating-rules` Section 5)) against the register each quarter; a name on a list and not on the register is a finding.
- Never record anything about a person that is not their work role, their decisions, or their program items.

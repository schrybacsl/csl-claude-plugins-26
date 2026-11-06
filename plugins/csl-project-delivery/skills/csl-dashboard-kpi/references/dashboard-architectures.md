# Dashboard Architectures

Read this when choosing how a dashboard will be built and hosted, when a deployment template must be handed to client IT, when a static demo export is needed for a meeting, or when a Replit app must be updated. Three architectures cover CSL's owner's-rep work; the choice is driven by who must maintain it after handover and where the client's data may live.

## 1. Choosing

| Architecture | Use when | Data path | Auth | Maintainer after handover | Examples |
|---|---|---|---|---|---|
| Single-file HTML | One audience, data refreshed by CSL from an export, no backend allowed or wanted; meeting handouts; offline review | Smartsheet xlsx or csv export -> data embedded as a JavaScript array in the file | File share permissions only | CSL (regenerate from the export) | CSL Task Dashboard (`csl-task-dashboard` pattern: 74 tasks, 9 workstreams, tabs, Gantt) |
| Hosted app on Replit (CSL-run) | Live data from Smartsheet needed daily; several stakeholder views; fast iteration; CSL retains operation | Live Smartsheet API through the `csl-data-pipeline` adapter; snapshots kept | Access codes per view; CSL-managed | CSL | Roadmap Insight Dashboard (Replit 6335fcc2, roadmapinsightdashboard.live) with Gannon Command and Koning views; Health Asset Manager; OSU Project Hub |
| Client-self-hosted template | The client will own and operate it; data must stay on the client tenant; SSO required | Client connectors (SharePoint or Smartsheet via Graph proxy, BMS) through the same adapter | Entra ID SSO; role claims | Client IT with CSL support | W77 sanitized deployment template handed to ASML IT (scoping call 09/14/26 with the Product Owner Building Automation; ticket REQ 999 / RITM5248681; Azure App Service target) |

A static demo export (Section 5) is not an architecture; it is a snapshot of any of the three for a meeting.

## 2. Single-file HTML (zero backend)

- One `.html` file; only external reference is Google Fonts when permitted, otherwise system fonts with Arial Narrow fallback; `brand-tokens.css` inlined.
- Data block: `const TASKS = [...]`, `const COMMENTS = [...]`, plus a `META` object with source file name, export timestamp, and generation timestamp, printed in the header.
- Tabs for the views (overview with KPI strip and alert banner, table with filters, team workload, Gantt, comments); event delegation on the tab bar and tables; `DocumentFragment` for bulk row writes; ~250 ms debounced search; chart click cross-filters the table.
- Regeneration: `smartsheet_pull.py --from-csv <export> --key "Task Name"` -> compute -> the build script writes the data block; the diff against the previous export is printed in the header's "changes since last export" line.
- Limits: no live data; anyone with the file has the data (so no personal or HR content, ever); size stays under a few megabytes.

## 3. Hosted app on Replit (CSL-run)

- Stack in use: Node/Express API + React/Vite client; PostgreSQL when history must persist (pull snapshots, KPI series); Smartsheet token in Replit secrets, never in code.
- Ingestion job runs the adapter on the pull cadence, writes snapshots in the `csl-data-pipeline` layout, and exposes `metrics.json` per pull to the client app; the header shows the pull timestamps.
- Views: main executive view and named command views; each named view is access-gated (the Koning view carries two access codes) and reads the same pulls; codes are issued by the CSL author and rotate on request.
- Change control: updates are made through the Replit agent on a workspace copy, verified by an audit pass (`command-view-spec.md` Section 3), and the live link is republished only on instruction in the session (`csl-operating-rules` references/connector-map.md).
- Bugs found in the W77 verification pass and the pattern to prevent them: a category key mismatch between the API payload and the client's lookup table rendered zeros (fix: one shared enum file; a tile shows "not available" when a key is unknown, never 0); a missing role label on a scoped view (fix: the header label is part of the view config and is asserted in the audit).

## 4. Client-self-hosted deployment template

Contents of the sanitized template handed to client IT (no CSL secrets, no client data, no CSL-internal notes):

| Component | Content |
|---|---|
| `client/` | React/Vite application with `brand-tokens.css`, the command-view components, and the KPI catalog file |
| `server/` | Express API; adapter module with `SmartsheetSource`, `GraphExcelSource`, `SharePointListSource`, and a BMS connector stub; scheduled ingestion; `metrics.json` endpoint |
| `db/` | PostgreSQL schema (pulls, metrics, views, access audit) and migrations |
| `docker-compose.yml` | client, server, database, reverse proxy; environment variables documented, none populated |
| `auth/` | Entra ID SSO (OpenID Connect) with role claims mapping to views; local access-code fallback disabled by default |
| `azure/` | App Service recipe: resource group, App Service plan, managed identity, Key Vault references, egress rules to `graph.microsoft.com` and the Smartsheet API during dual-read, custom domain and certificate steps |
| `DEPLOYMENT.md` | Operator guide: prerequisites, secrets to create and where, first deployment, adding a view, rotating credentials, backup and restore, health checks, log locations, support contact and escalation |
| `SECURITY.md` | Data classification, what leaves the tenant (nothing), dependency update policy, audit log retention |
| `CHANGELOG.md` | Version history keyed to the dashboard version strings |

Ticket scope to agree with client IT before transfer (the W77 scoping call on 09/14/26 covered these; put them in the ticket in this order):

1. Security review of the template (dependency scan, secret scan, data-flow diagram) and who signs it off.
2. Transfer method (repository invitation to the client tenant, or archive through the client's approved channel) and integrity check (archive hash recorded in the transmittal).
3. Hosting target and owner (Azure App Service under the client subscription; resource group; cost owner).
4. DNS, certificate, and API egress (custom domain, certificate issuance, allowed outbound hosts).
5. Entra app registration: name, owners including the CSL author for support, permission set (`Sites.Selected` scoped to the program site), redirect URIs, admin consent approver.
6. Cutover and dual-run: how long the CSL-hosted app stays up; who flips the link; rollback.
7. Support model after transfer: CSL support window, response times, and how changes are requested and versioned.

Numbering and evidence: the handover is a transmittal (`csl-document-control` Section 5) listing the archive name, hash, version string, and recipients; the ticket numbers are recorded in the engagement context file (`csl-operating-rules` Section 5).

## 5. Static demo export

A non-live HTML snapshot for a meeting or a leadership deck, produced from any architecture:

1. Pick the pull (date and md5) the demo represents; state it in the header as "Static snapshot of <pull timestamps>; not live".
2. Render the views server-side or in a headless browser with the data inlined; strip API calls and access controls; remove any tile whose data is not cleared for the audience (Internal-tagged items on the healthcare variant).
3. Watermark "DEMO" when any tile carries synthetic or illustrative data; never mix synthetic and live tiles without the label on each.
4. Verify in a browser with the network disabled; then run the brand QA checklist (`csl-brand`).
5. File as `<DOC-NUMBER>_<yyyy-mm-dd>_demo.html` beside the pull it came from; a demo is never republished to the live link.

## 6. Design system checklist for any architecture

- `brand-tokens.css` on `:root`; paper page ground; navy header bar with a white logo block, program name, view name, and last-pull timestamps.
- Cards on white with mist borders and 3 pt tier top bars; tables per the CSS (navy header, zebra rows); numbers right-aligned; dates and IDs centered.
- Tier dots and bars always with the word and rule ID; status colors from `csl-brand` Section 1.4; never CSL Red as a fill.
- Chart series in the fixed order navy, dark teal, teal, olive; tier colors only on tier-coded marks; one axis per panel; source line under every chart.
- Force light theme unless every token is redefined for dark.
- Accessibility: WCAG 2.1 AA contrast on every text and tier pairing; `aria-sort` on sortable headers; keyboard reachable tabs and filters; focus visible.
- Performance: event delegation; `DocumentFragment` for bulk DOM writes; ~250 ms debounced search; chart click cross-filtering without full re-render.
- Mobile width (below 720 px): the KPI strip wraps to two columns and keeps its order; the RED list stays above every drill-down; tables scroll horizontally with a sticky first column or collapse to cards; charts keep their source line.

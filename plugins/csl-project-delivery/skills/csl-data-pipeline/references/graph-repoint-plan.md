# Microsoft Graph Repoint Plan (Smartsheet to SharePoint migration)

Read this when ingestion for the Roadmap Insight Dashboard or the report factory must move from the Smartsheet API to Microsoft Graph, when the client's IT ticket (W77: REQ 999 / RITM5248681 with the dashboard-transfer distribution) asks what CSL needs, or when a parity question comes up during dual-read. The client decided to move the W77 sheets to SharePoint; the CSL commitment is that no report, KPI, or dashboard tile changes meaning during the move. The commitment is kept by an adapter, a dual-read window, and a parity test with numbers, not by a cutover weekend.

## 1. Adapter interface

Every consumer (factory pull stage, dashboard ingestion, ad-hoc pulls) reads through one interface, so the platform change touches one module:

```python
@dataclass(frozen=True)
class SheetRef:
    key: str                      # config key, e.g. roadmap_master
    smartsheet_id: int | None     # 1059284113641348 during dual-read
    graph: dict | None            # {"site_id", "drive_id", "item_id", "table"} or {"site_id", "list_id"}
    parents_only: bool = False

class SheetSource(Protocol):
    name: str                     # "smartsheet" | "graph_excel" | "sharepoint_list"
    def pull(self, ref: SheetRef) -> pd.DataFrame: ...
        # returns the normalized frame with _row_id, _row_number, _parent_id, _indent + titled columns
    def changes_since(self, ref: SheetRef, token: str | None) -> tuple[pd.DataFrame, str]: ...
        # incremental rows and the next delta token; full pull when token is None
```

| Implementation | Reads | Row identity | Hierarchy | Notes |
|---|---|---|---|---|
| `SmartsheetSource` | `GET /2.0/sheets/{id}` paged 500 | Smartsheet row ID | parentId chain | Today's path; token env `ASMLW77` |
| `GraphExcelSource` | `GET /sites/{site}/drives/{drive}/items/{item}/workbook/tables/{table}/rows` | A stable key column the client maintains (recommend a hidden `RowKey` GUID column; fallback composite title + START) | An explicit `Indent` or `Parent` column, because a workbook table has no hierarchy | Workbook sessions (`workbook/createSession`, `persistChanges=false`) for consistency across pages; 5,000-row pages |
| `SharePointListSource` | `GET /sites/{site}/lists/{list}/items?expand=fields` | List item ID | A lookup column to the parent item | Supports delta queries natively; picklists map to choice columns |

The sidecar records `source: graph_excel` or `sharepoint_list` and the Graph coordinates, so a snapshot from either platform is diffed and hashed exactly as a Smartsheet snapshot is.

## 2. Entra ID app registration

| Item | CSL interactive use | Scheduled factory / dashboard service |
|---|---|---|
| Permission type | Delegated (signed-in CSL user with the client's guest account) | Application |
| Scopes | `Sites.Read.All` or, preferred, `Sites.Selected` granted to the program site; `Files.Read.All` only if workbooks sit outside the site | `Sites.Selected` scoped to the program site; no tenant-wide read |
| Auth flow | Device code or auth code with PKCE through the Microsoft 365 connector where possible | Client credentials with a certificate held in the client's key vault (Azure App Service managed identity when the dashboard moves there) |
| Registered by | Client IT (the registration lives in the client tenant); the CSL author is named in the ticket as a co-owner of the app registration for support | Same |
| Secrets | None in files; `MS_GRAPH_*` variables or connector-managed | Managed identity or vault reference |

Ticket scope to put in writing (`csl-client-comms/templates/it-ticket-scoping.md`): app registration name and owners, permission set with justification per scope, the site and libraries in scope, redirect URIs for the hosted dashboard, certificate issuance and rotation owner, egress rules from the hosting environment to `graph.microsoft.com`, and who approves admin consent.

## 3. Incremental change tracking

- SharePoint lists: `GET /sites/{site}/lists/{list}/items/delta`; store the `@odata.deltaLink` token in the sidecar of the last full snapshot; a delta response with zero items over a week is the Graph equivalent of a byte-identical pull and feeds `freeze_check` unchanged.
- Drive items (workbooks): `GET /drives/{drive}/root/delta` tells you the file changed, not which rows; on a change, re-pull the table in full and diff locally. Excel has no row-level delta, which is one reason lists are preferred for trackers.
- Column changes: compare the table's column collection to `config.sources.<key>.columns` on every pull; a rename is schema drift and stops the run, exactly as on Smartsheet.
- Cell history, discussions, and attachments have no direct Graph equivalent on a workbook table; where a deliverable depends on them (verbal rulings captured in discussions), the migration plan names the replacement (list comments, version history) before cutover.

## 4. Dual-read during the migration

1. Add the Graph coordinates to each `SheetRef` while the Smartsheet ID stays primary. Every pull runs both sources and writes two snapshots: `<sheet-id>.csv` and `<sheet-id>.graph.csv`, each with its own sidecar.
2. The dashboard and the factory keep reading the Smartsheet snapshot; the Graph snapshot is compared, not published.
3. A parity report per pull (Section 5) is filed with the snapshots and summarized in the Friday source note ("Graph parity: rows 907/907, checksum match, 14 of 14 KPIs equal").
4. Cutover flips `primary: graph` in config for one family at a time (PLN family first, WKR last), after two consecutive weeks of full parity. Smartsheet remains readable until the client retires it; the adapter keeps both until then, so a rollback is a config flag.

## 5. Parity test plan (two weeks minimum)

| Test | Pass condition | On failure |
|---|---|---|
| Row-count parity | Parents and children equal on both sources at the same pull time | List the keys missing on either side; usually a filtered view or a deleted-row lag |
| Checksum parity | md5 of the normalized frame equal after mapping column titles through config | Diff the two frames with `diff_pulls.py --key <RowKey>`; classify by column (formatting, picklist label, date serial) |
| KPI parity | Every `metrics.json` value equal to the cent, the day, and the row | Trace the KPI to its columns; a mismatch is usually the hierarchy column or a percent stored as a fraction |
| Freshness | Graph pull timestamp within 10 minutes of the Smartsheet pull | Schedule alignment; workbook session caching |
| Access | Service principal reads succeed from the hosting environment, not only from a CSL laptop | Egress or consent gap; ticket update |

Two clean weeks of all five tests is the cutover gate; the parity reports are kept with the migration record.

## 6. What changes downstream

Nothing in templates, page maps, KPI definitions, chart contracts, tier rules, or numbering. The sidecar's `source` field, the `SheetRef` in config, and the delta token are the only new facts. The Roadmap Insight Dashboard's ingestion job calls the same adapter, so command views and access codes (`csl-dashboard-kpi`) are untouched; the dashboard transfer to the client's Azure App Service proceeds on its own ticket and consumes this adapter when it lands.

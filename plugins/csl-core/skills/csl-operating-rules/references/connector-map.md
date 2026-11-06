# Connector Map

Which connector covers which system in CSL's Claude organization, and how the 2026-09 skills' data-access language translates. Connector availability is set by IT per user. If a connector is missing, say so in one line and direct the operator to IT; continue from an uploaded export where possible.

| System | Connector | Typical reads | Writes allowed | Replaces in old skills |
|---|---|---|---|---|
| Smartsheet | Smartsheet | Full sheet reads, cell history, attachments | CSL-owned sheets only, on instruction; never client sheets | SDK/REST with the `ASMLW77` token; Make scenarios |
| Outlook mail and calendar | Microsoft 365 | Search threads, read messages, find meeting times | Drafts only; send on explicit instruction per item | "pastes a thread" workflows |
| Teams | Microsoft 365 | Search chats and channel messages | Post on explicit instruction per item | — |
| SharePoint / OneDrive | Microsoft 365 | Search and read documents | Upload or update on explicit instruction | Local `outputs/<PROG>/` folders; Graph repoint adapter for reads |
| Staff directory | Microsoft 365 (`search_people`, `get_me`) | Names, titles, emails | None | `config/user-profile.md`; manual lookups in `csl-people` |
| Scoro | Scoro | Projects, time, resourcing | On instruction only | — |
| Box | Box (if enabled) | Client data rooms | None without instruction | — |
| Claude Docs | Claude Docs | Editable documents for internal drafts | Creates docs on request | Markdown files on disk |

## Sandbox limits

Code execution in claude.ai runs in a sandbox whose network allowlist does not include Smartsheet or Microsoft Graph. The Python in `csl-data-pipeline/scripts/` therefore runs on data that a connector has already returned or that the operator uploaded: normalize, hash, diff, QA, chart, and render all work; the `smartsheet_pull.py` network path does not. Use its `--from-csv` mode.

## Credentials

Never ask for, accept, or write an API token, password, or connection string in chat, a file, or a deliverable. If a user offers one, decline and direct them to IT.

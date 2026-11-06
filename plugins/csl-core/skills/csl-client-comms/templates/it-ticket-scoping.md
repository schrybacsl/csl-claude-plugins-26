# IT / Ticket Scoping Email

Defines, in one email, what a client IT ticket must contain to move a CSL-built system (dashboard, pipeline, report factory) onto the client's platform, so IT can size it in one pass and CSL keeps the ability to maintain what it built. Method in `csl-client-comms` Section 3.9; the W77 case is the Roadmap Insight Dashboard transfer (ticket REQ 999 / RITM5248681 once opened; distribution per the engagement context file (`csl-operating-rules` Section 5)).

---

## Draft block

| Field | Entry |
|---|---|
| To | The client IT or controls lead who opened the conversation (W77, 08/20/26: the Controls and BMS manager) |
| Cc | Client program lead; the product owner for the target platform; CSL Project Director; CSL CIO when CSL systems or credentials are involved |
| Subject | `[Program] \| [System] transfer \| Ticket scope` |
| Attachments | Sanitized deployment template; dependency list; architecture one-pager; none of them containing credentials |

## Body skeleton

1. One sentence of thanks for taking the ticket, then the purpose: scope the ticket so IT sizes it once.
2. Numbered scope items. For each: what IT does, what CSL supplies, and the preference where CSL has one.
3. Explicit list of what is out of this ticket and parked for later phases.
4. Two questions: the ticket owner on their side and the review cadence.
5. Sign-off.

## Populated example (reply of Thu 08/20/26 to the client's Controls and BMS manager)

> Subject: W77 | Roadmap Insight Dashboard transfer | Ticket scope
>
> José,
>
> Thanks for taking this on. To let IT size the ticket in one pass, we suggest the scope below.
>
> 1. Security review of the application. Node/Express API with a React/Vite front end, Entra ID single sign-on, and a Graph proxy for data access. CSL supplies the sanitized deployment template, the dependency list with versions, and the architecture one-pager. No credentials are in the package.
> 2. Transfer method. Repository hand-off to a tenant-owned repo, or a container image; IT's preference. CSL prepares whichever is chosen.
> 3. Hosting. Azure App Service preferred; the application is stateless apart from configuration, so it fits the service without a database migration.
> 4. DNS name, TLS certificate, and API egress. Egress to the Smartsheet API today, and to Microsoft Graph once the sheets move to SharePoint, so the ingestion can repoint without a second ticket.
> 5. Entra ID app registration, with the CSL author included as a contributor on the registration and the App Service so updates continue after transfer. Without this, every dashboard change becomes a new ticket.
>
> Noted for later phases and kept out of this ticket: the BMS data layer, the test-rig telemetry connection, and the Copilot linkage. We will bring each as its own scoped request once the base application is running on your side.
>
> Two questions: who on the IT side should we name as ticket owner, and what review cadence works for you while the transfer is in progress?
>
> Thanks,
> Steven

## Scope items that recur on any transfer (pick the ones that apply)

| Item | CSL supplies | Decision the client makes |
|---|---|---|
| Security review | Template, dependency list, architecture, data-flow diagram | Review path and approver |
| Transfer method | Repo or image, README, environment variable list (names only) | Repo location or registry |
| Hosting | Sizing note (requests per day, data volume) | Service and tier |
| Identity | App registration requirements; redirect URIs; contributor list including the CSL author | Registration owner |
| Network | Egress list by hostname; certificate needs | DNS name; certificate issuance |
| Data sources | Current source and the planned migration target | Service account or delegated access |
| Operations | Update process; who deploys; rollback | Change window; ticket cadence |
| Out of scope now | Named parked items with a phase | Phase order |

## After sending

- Register row on the stakeholder register for the ticket owner once named; ticket number recorded in the program record and cited in the weekly report status line.
- Every later request references the ticket number and the scope item it belongs to.

Pre-send: scope numbered; CSL supplies stated per item; CSL author on the identity item; parked items listed; two questions asked; no credentials anywhere; nothing sent by the agent.

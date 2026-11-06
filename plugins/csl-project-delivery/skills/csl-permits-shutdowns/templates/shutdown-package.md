# Shutdown / Outage Package (CSL-<PROG>-SDP-<yymmdd> Rev <n>)

Skeleton for a building shutdown or utility outage executed as one window. Nine parts in the order of `csl-permits-shutdowns` 3.7, with the gate count reported at T-14, T-7, T-2, and T-0 and the post-event reconciliation attached. One populated example row per table; example values follow the W77 08/22/26 building shutdown where the record supplies them (37 of 40 gates at T-2 on 08/20/26; closed 40 of 40 with no incidents) and are otherwise illustrative. Variables in `<angle brackets>` change every issue. Controlled document with a revision history; filed with the permits it covers (`csl-document-control` Section 6).

---

**CSL-<PROG>-SDP-<yymmdd> Rev <n>** | <Event name> | Window <Day MM/DD/YY HH:MM> to <Day MM/DD/YY HH:MM> ET | Prepared by <name>, CSL Consulting | Approved by <system owner>, <operations>, <EH&S> | Alignment meeting <MM/DD/YY HH:MM ET>

## Gate count line

| Checkpoint | Date | Gates cleared / declared | Open gates (name, owner, latest clearance time) |
|---|---|---|---|
| T-2 | Thu 08/20/26 | 37/40 | Three open, each named with its owner and latest clearance time in the package as issued |
| Close | Sat 08/22/26 | 40/40 | None; no incidents |

## 1. Scope

What is being done, by whom, in which window, and the abort criteria in one paragraph. Name the constituent permits.

> Building shutdown (illustrative scope: normal power to one wing) to permit <work> by <contractor> on Sat <MM/DD/YY>, window <HH:MM> to <HH:MM> ET. Constituent permits: <numbers>. Abort if any isolation cannot be verified by <HH:MM>, if weather closes the roof, or if operations withdraws the window; the go / no-go decision is recorded at the T-0 alignment meeting.

## 2. Affected systems and areas

| System tag | Description | Areas served | Production or tool impact (per operations) | Operations sign-off |
|---|---|---|---|---|
| Normal power, north wing (illustrative) | Distribution from the wing switchboard | Rooftop air handlers; test rigs on the wing | Rigs stop for the window and restart per the rig SOP; the stop is expected and is attributed to this package in the reconciliation | <name>, <date> |

## 3. Sequence

| Time (ET) | Step | Owner | Verification |
|---|---|---|---|
| 05:30 | Pre-shutdown checks: BMS alarms cleared, rig states recorded, communications T-0 sent | CSL PM; controls | BMS snapshot saved with timestamp |

Continue through isolation, work, restoration, and verification; every step has an owner and a verification.

## 4. Isolation plan

| Isolation point | Type (valve / breaker / blind) | Lock number | Applied by, time | Zero-energy verified by, time | Restoration by, time | Restoration verified by, time |
|---|---|---|---|---|---|---|
| Wing switchboard main breaker (illustrative) | Breaker | L-0417 | <name>, 06:10 | <name>, 06:18 | <name>, 15:40 | <name>, 15:52 |

Every isolation line has its restoration line filled before the package closes.

## 5. Communication plan

| When | Message | From | To | Channel | Sent (date, time) |
|---|---|---|---|---|---|
| T-14 | Window requested; affected systems listed; objections by <date> | CSL PM | Operations, facilities, EH&S, affected tenants | Email with the package draft | 08/08/26 |

Continue for T-7 (window confirmed), T-2 (gate count, final sequence), T-0 (start), and restoration (systems back, verification results).

## 6. Permits and gates staged

| Permit | Type of work | Contractor | Gates cleared / declared at T-2 | Open gates | Gated in time at T-0 |
|---|---|---|---|---|---|
| <number> | <type> | <contractor> | <k/N> | <named> | Yes / No |

Package count = sum of the rows. Report the count at each checkpoint in the gate count line above.

## 7. Contingency and restoration

| Condition | Decision | Decided by | Restoration order and verification points |
|---|---|---|---|
| Isolation cannot be verified by the sequence time | Abort or re-sequence | System owner with CSL PM | Restore in reverse order of isolation; verify pressures, flows, and alarms cleared at each step |

## 8. Post-event reconciliation (within two business days)

| Item | Result | Evidence |
|---|---|---|
| Permits closed | <k> of <n> | Closeout records |
| Isolations restored and verified | <k> of <n> | Isolation table, restoration columns complete |
| Telemetry checked | Channels and logger paths named; window in ISO 8601 with zone | CTRW summaries (`csl-data-pipeline`) |
| Excursions attributed | Test-rig stop coincident with the window attributed to the planned shutdown (this package, window <dates>) | Telemetry plot with the window shaded |
| Excursions unexplained | None, or listed and tiered | `csl-schedule-risk` (R9 for tool-down or leakage signatures) |
| Incidents and near misses | None | Site EH&S log |

## 9. Lessons for the next look-ahead

| Lesson | Action | Owner | Date | Carried in |
|---|---|---|---|---|
| Rig stops inside a planned window generate telemetry alarms that look like faults | Add the shutdown window to the CTRW summary header for the week | S. Schryba | Next Friday pull | WKR-nnA docket |

## Revision history

| Rev | Date | Change | By |
|---|---|---|---|
| 0 | <MM/DD/YY> | First issue at T-14 | <name> |

---

Pre-issue: gate count line complete for every checkpoint reached; every isolation line has a restoration line; communications sent dates filled; reconciliation attached within two business days of restoration; excursions attributed with the permit and window; no personal or health information; brand QA per `csl-brand`; number and file name per `csl-document-control`.

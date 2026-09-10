# Package 004 — Wave 0 Authorization Decision

## Authoritative decision record

| Field | Value |
|---|---|
| Decision ID | `FD-P004-W0-AUTH-001` |
| Decision | `APPROVE_PACKAGE_004_WAVE_0_AUTHORIZATION` |
| Classification | `FOUNDER_DECISION` |
| Decisor | Founder |
| Effective timestamp | `2026-09-04T09:22:37-03:00` |
| Package | Package 004 — Product Factory |
| Package state | `TASKS_GENERATION_AUTHORIZED` — unchanged |
| Requirements / Design / Tasks | v1.0 `APPROVED` / v1.0 `APPROVED` / v1.0 `TASKS_APPROVED` |
| Authorized wave | W0 only |
| Authorized Task | T004-001 only |
| W0 authorization/status | `AUTHORIZED_FOR_EXECUTION / NOT_STARTED` |
| Global execution | `PARTIALLY_AUTHORIZED / W0_ONLY` |
| W1–W7 / implementation | `NOT_AUTHORIZED_FOR_EXECUTION / NOT_AUTHORIZED` |

## Founder decision

[Decisión] The Founder authorizes documentary execution of W0 and only T004-001 within the approved Task contract and the output boundary below. This decision does not execute W0, authorize W1–W7, start implementation, create governed Product entities or change any Asset.

Plain approval is appropriate: W0 is a safe precondition/integrity wave, all prerequisites are satisfied, baselines are fresh and no Architecture, upstream or infrastructure change is required.

## Baseline freshness and plan integrity

| Control | Result |
|---|---|
| Requirements | v1.0 `APPROVED` — `FD-P004-REQ-001` |
| Design | v1.0 `APPROVED` — `FD-P004-DESIGN-001` |
| Task Plan | v1.0 `TASKS_APPROVED` — `FD-P004-TASKS-001` |
| Freshness classification | `BASELINE_FRESHNESS_CONFIRMED` |
| Post-approval semantic changes | `0` |
| Tasks / waves | `32 / 8` |
| W0 membership drift | `0` |
| Dependency cycles | `0` |
| Hidden Task/wave execution | `0 / 0` |

Approval metadata and this wave authorization do not alter Requirement, Design or Task semantics.

## W0_TASK_SET

| Field | Repository-derived value |
|---|---|
| Task ID | `T004-001` |
| Title | Establish Tasks baseline and execution boundary |
| Task type | `AUDIT` |
| Execution classification | `DOCUMENTARY` |
| Purpose | Verify authoritative baselines, authorization, Package states and source precedence |
| Requirements / AC | R01–R25; R01.4, R03.1, R19.1–R19.4, R20.4, R21.3–R21.4, R25.2 |
| Design / decisions | C01–C20; D001–D015 |
| Dependencies | None; W0 blocker for T004-002–032 |
| Inputs | Approved Requirements/Design and Founder decisions; Architecture Freeze; P003/P005 boundaries; P006/P007 state |
| Outputs | Tasks source map, baseline checklist, initial integrity snapshot and named conflicts/gaps |
| Acceptance evidence | Requirements/Design approval, Tasks authority, Freeze, P003 closure, P005–P007 dormancy, unchanged Assets, paused Human Performance and optional infrastructure all confirmed |
| Prohibited actions | Change baselines, create operational records/entities, mutate upstream packages, select/implement technology or authorize downstream execution |
| Completion condition | Every source/state resolves, or a blocking change classification is recorded; human cross-check and signature required |
| Authorization readiness | `READY / AUTHORIZED_FOR_EXECUTION` |

W0 contains no additional Task. It is strictly a precondition/integrity audit. Software implementation, controlled verification fixtures, external research and real-world validation in W0 are all `0`.

## Dependency gate

T004-001 has no Task prerequisite. Its external prerequisites are the approved baselines and decisions listed above, the preserved Freeze, closed P003 boundary, dormant downstream packages and repository access; each is satisfied. No incomplete Task from another wave is required.

## Architecture, Package and Asset gates

| Control | Result |
|---|---|
| Architecture Baseline impact | `EXTENDS_BASELINE` |
| Architecture Freeze | `PRESERVED` |
| Requirements / Design / Architecture changes | `0 / 0 / 0` |
| Package 003 reopened | `NO` |
| ADR required | `NO` |
| Package 005 / 006 / 007 | `DORMANT / DORMANT / DORMANT` |
| Human Performance | `PAUSED_BY_FOUNDER` |

P003→P004 remains `READ / REFERENCE / CONSUME DECISION`. W0 has no permission to write or override Asset identity, lifecycle, ownership, provenance, SOT, version, restrictions or attachment eligibility.

ASSET-1, ASSET-2 and ASSET-3 remain `VALIDATED / NOT_CANONICAL / NOT_ATTACHABLE`; their existing records are read-only. W0 cannot promote, attach or otherwise modify them.

## Execution environment and output boundary

W0 can execute with repository/documentary operations only. No external system, software platform, automation, database, Persistence/Historical Truth implementation, RAG, MCP or AI Agent Runtime is required or authorized.

| Access | Exact boundary |
|---|---|
| CREATE during W0 execution | `docs/packages/package-004-product-factory/wave-0-baseline-integrity-record.md` only |
| UPDATE during W0 execution | Package 004 `tasks.md`, `tasks-execution-waves.md` and `README.md` status/evidence metadata only |
| READ_ONLY | Approved Package 004 Requirements/Design/Tasks and decisions; Architecture Baseline/Freeze/change control/roadmap; P003 handoff/Asset records; P005–P007 state records; Human Performance state evidence |
| NO_WRITE | Package 003; Crypto; Package 005–P007; Human Performance; approved Requirements/Design/Task semantics; all systems outside Package 004 W0 outputs |

The single W0 evidence file may consolidate the already-approved source map, baseline checklist, integrity snapshot and named conflict/gap results. Choosing this bounded file is `METADATA_ONLY / NON_NORMATIVE` execution scoping, not a Task Plan semantic change. No W0 output may be a Candidate, Product, Asset attachment/transition, commercial artifact or software implementation.

## Execution and completion governance

Resulting authority:

- T004-001 and W0: `AUTHORIZED_FOR_EXECUTION / NOT_STARTED`.
- T004-002–T004-032 and W1–W7: `NOT_AUTHORIZED_FOR_EXECUTION`.
- Global Task execution: `PARTIALLY_AUTHORIZED / W0_ONLY`.
- Implementation: `NOT_AUTHORIZED`.

W0 becomes COMPLETE only after T004-001 satisfies its approved completion condition, evidence is recorded, status metadata is updated and an integrity audit confirms no unauthorized expansion. If execution finds baseline drift, dependency mismatch, Architecture conflict, Asset-state mismatch, Package-boundary violation or unauthorized infrastructure dependency, it must stop as `W0_EXECUTION_BLOCKED`; silent remediation is prohibited.

Governance sequence remains:

`W0 authorization → W0 execution → W0 review → W1 authorization decision`.

W0 completion does not authorize W1.

## Integrity declaration

W0 executed: `NO`. W1–W7 authorized: `NO`. Additional Tasks completed: `0`. Implementation: `0`. Product Candidates/Products/attachments: `0 / 0 / 0`. Asset lifecycle/CANONICAL changes: `0 / 0`. Package 003 changes caused: `0`. Package 005/006/007 activation: `NO / NO / NO`. Human Performance resumed: `NO`. Crypto modifications: `0`. Persistence/Historical Truth/RAG/MCP/AI Agent implementation: `NO / NO / NO / NO / NO`.

Next safe action: `PACKAGE_004_WAVE_0_EXECUTION`. Do not execute automatically.


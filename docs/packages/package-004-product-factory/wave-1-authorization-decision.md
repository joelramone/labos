# Package 004 — Wave 1 Authorization Decision

## Decision record

| Field | Decision |
|---|---|
| Decision ID | `FD-P004-W1-AUTH-001` |
| Decision | `APPROVE_PACKAGE_004_WAVE_1_AUTHORIZATION` |
| Classification | `FOUNDER_DECISION` |
| Founder | LabOS Founder Governance Authority |
| Effective timestamp | `2026-09-04T09:53:48-03:00` |
| Package | Package 004 — Product Factory |
| Scope | Wave 1 only; authorization does not execute W1 or authorize W2–W7 |
| Prior state | W0 `COMPLETE`; W1–W7 `NOT_AUTHORIZED_FOR_EXECUTION` |
| Result | W1 `AUTHORIZED_FOR_EXECUTION / NOT_STARTED`; global execution `PARTIALLY_AUTHORIZED / W1_ONLY` |
| Implementation | `NOT_AUTHORIZED` |
| Next safe action | `PACKAGE_004_WAVE_1_EXECUTION` |

## Founder determination

The approved Requirements, Design and Task Plan remain fresh, W0 completed cleanly, and every W1 prerequisite is satisfied. W1 contains four documentary/manual Tasks and requires no new Product Factory semantics, implementation, external research, real-world validation or cross-package activation. The Architecture Freeze and all upstream/downstream authority boundaries remain preserved. Plain approval is therefore warranted.

This authorization is not execution. T004-002–005 remain `NOT_STARTED` until a separately invoked W1 execution action begins them.

## W0 completion gate

| Control | Repository evidence | Result |
|---|---|---|
| T004-001 | `wave-0-baseline-integrity-record.md` | `COMPLETE` |
| W0 | Same record and execution metadata | `W0_EXECUTION_COMPLETE / COMPLETE` |
| Independent review | Same record | `PACKAGE_004_WAVE_0_APPROVE` |
| Blockers | W0 gap/conflict audit | `0` |
| Baseline freshness | W0 evidence, rechecked at this decision | `BASELINE_FRESHNESS_CONFIRMED` |

## Baseline freshness and architecture gate

| Baseline/control | Current authoritative state | Finding |
|---|---|---|
| Requirements | v1.0 `APPROVED` | Fresh; semantic changes `0` |
| Design | v1.0 `APPROVED` | Fresh; Design changes required `0` |
| Task Plan | v1.0 `TASKS_APPROVED`; 32 Tasks; W0–W7; cycle-free DAG | Fresh; Task Plan changes required `0` |
| Architecture | `LABOS-ARCH-BASELINE-001` v1.0 `APPROVED_WITH_CONDITIONS` | Impact `EXTENDS_BASELINE`; `MODIFY_BASELINE: NO` |
| Architecture Freeze | `PRESERVED` | Architecture changes required `0`; ADR `NOT_REQUIRED` |

Approval/execution metadata introduced after baseline approval is `METADATA_ONLY / NON_NORMATIVE`. No Task entered or left W1, and no Task semantics changed.

## W1_TASK_SET

| Task | Title | Type / execution classification | Dependencies | Inputs | Expected output | Acceptance evidence / completion | Prohibited actions |
|---|---|---|---|---|---|---|---|
| T004-002 | Create Product Candidate governance template | `TEMPLATE / DOCUMENTARY` | T004-001 (`COMPLETE`) | Candidate Design, common terminology, W0 baseline | Candidate template covering identity, owner, problem, consumer, hypothesis, context, proposed inputs, evidence/restrictions, SOT, state and review trigger | Field/gap audit; complete only after independent field/wording review and a non-registering blank dry-run | No Candidate instance or Product claim |
| T004-003 | Create governed Product aggregate record template | `TEMPLATE / DOCUMENTARY` | T004-001 (`COMPLETE`) | Approved aggregate/cardinalities, W0 baseline | Product template referencing owner, consumer/problem/value, composition, context, evidence, dependencies, restrictions, SOT, lifecycle and version | Entity/mandatory-gap audit and duplicate-identity flag; every R01 identity element present-or-missing | No Product instance, approval or copied Asset truth |
| T004-004 | Create reusable Governance Decision Record | `GOVERNANCE_ARTIFACT / DOCUMENTARY` | T004-001 (`COMPLETE`) | Governance Design, W0 baseline | Common envelope plus event-specific sections for action, subject/state, evidence, restrictions, decision, authority/delegation, timestamp, rationale, resulting/unchanged state and follow-up | Event-to-envelope matrix; common and event-specific fields remain separable | No decision instance, automatic transition or merged decision semantics |
| T004-005 | Create Product ownership and SOT declaration templates | `TEMPLATE / DOCUMENTARY` | T004-003 and T004-004 (authorized in W1; must complete first) | Outputs of T004-003/004 and upstream ownership/SOT contracts | Ownership/transfer section and single Product-version SOT declaration distinguishing Asset SOT, evidence, managed mirror, working/derived/unmanaged copies | Role and SOT conflict scenarios; completion only when one authoritative Product/version source resolves and conflicts fail closed | No ownership transfer, storage selection or competing authority |

## W1 dependency readiness

`W1_DEPENDENCY_READINESS: READY`.

- T004-002, T004-003 and T004-004 depend only on completed T004-001 and may begin independently after execution is invoked.
- T004-005 is authorized with W1 but may begin only after T004-003 and T004-004 are `COMPLETE`.
- No W2+ Task is a prerequisite. The approved DAG remains cycle-free.
- Authorization does not waive internal ordering or permit a Task to start before its prerequisites complete.

## W1_ARTIFACT_PATH_BASELINE

The prior filename note is resolved non-normatively for W1. Future W1 execution is authorized to create only these planned outputs:

| Task | Stable output path |
|---|---|
| T004-002 | `docs/packages/package-004-product-factory/product-candidate-template.md` |
| T004-003 | `docs/packages/package-004-product-factory/product-record-template.md` |
| T004-004 | `docs/packages/package-004-product-factory/governance-decision-record-template.md` |
| T004-005 | `docs/packages/package-004-product-factory/product-ownership-sot-template.md` |

Path selection is documentary organization only and adds no Product semantics. Downstream links must use this baseline unless governed change control explicitly updates it.

### Write boundary for future W1 execution

- `CREATE`: the four paths in `W1_ARTIFACT_PATH_BASELINE`.
- `UPDATE`: `tasks.md`, `tasks-execution-waves.md` and `README.md`, only for W1 execution status/evidence.
- `READ_ONLY`: Requirements, Design and Task Plan baselines; Founder decisions; W0 authorization/evidence; architecture controls; Package 003 and Asset records; Package 005–007; Human Performance; Crypto if inspected.
- No other write is authorized by this decision. This authorization record and its three metadata updates are the only writes made now.

## Semantic and governance protections

- Templates are not governed entity instances. W1 may create no real Product Candidate, Product, approval, activation, attachment or commercial offering.
- Product Candidate and Product remain separate. Any illustrative text must be visibly `EXAMPLE`; controlled fixtures belong to W6 and are not authorized in W1.
- Lifecycle remains exactly `CANDIDATE → UNDER_REVIEW → READY → APPROVED → ACTIVE → DEPRECATED → RETIRED`. `REJECTED` remains a terminal Candidate review outcome, not an eighth state.
- The common governance envelope reduces physical record proliferation while retaining distinct review, readiness, approval, activation, risk acceptance, sharing, deprecation and retirement semantics.
- Final authority remains the Founder or explicitly delegated human. AI may assist only within the approved non-authoritative permission boundary and cannot approve, execute transitions, change authority/provenance, override Asset eligibility or authorize commercialization.
- Documentary current truth and historical truth remain distinguishable; no Historical Truth infrastructure or storage technology is selected.
- Product SOT remains distinct from Asset SOT, evidence sources, managed mirrors, working copies, derived representations and unmanaged copies.

## Asset and package boundaries

Package 003 remains `CLOSED` and authoritative for Asset identity, lifecycle, ownership, provenance, SOT, versioning, restrictions and attachment eligibility. P003→P004 remains `READ / REFERENCE / CONSUME DECISION`; `WRITE / OVERRIDE` is prohibited.

ASSET-1, ASSET-2 and ASSET-3 remain `VALIDATED / NOT_CANONICAL / REFERENCE_ONLY / NOT_ATTACHABLE`. W1 authorizes no Asset change, promotion or attachment.

Package 005, Package 006 and Package 007 remain `DORMANT`. W1 performs no pricing, payment, transaction, revenue accounting, optimization, commercialization, AI/runtime activation or downstream implementation. Human Performance remains `PAUSED_BY_FOUNDER`.

W1 requires no database, application, API, UI, automation, Persistence, Historical Truth implementation, RAG, MCP, AI Agent Runtime or software platform.

## Execution success and stop conditions

Each Task may become `COMPLETE` only when its approved artifact, traceability, acceptance evidence and manual review condition are satisfied, with no real entity, implementation or unauthorized write. W1 completes only when T004-002–005 are all complete and independently reviewed.

Future execution must stop as `W1_EXECUTION_BLOCKED` upon missing Design authority, ambiguous Product semantics, unresolved path dependency, Task dependency mismatch, Asset authority conflict, architecture conflict or need for unauthorized implementation. No silent scope expansion or remediation is permitted.

## Resulting authorization and integrity

| Scope | Result |
|---|---|
| W0 | `COMPLETE` |
| T004-002–005 / W1 | `AUTHORIZED_FOR_EXECUTION / NOT_STARTED` |
| W2–W7 | `NOT_AUTHORIZED_FOR_EXECUTION` |
| Global Task execution | `PARTIALLY_AUTHORIZED / W1_ONLY` |
| Implementation | `NOT_AUTHORIZED` |

Integrity after this decision: W1 Tasks executed `0`; W2–W7 authorized `0`; implementation `0`; Product Candidates `0`; Products `0`; attachments `0`; Asset lifecycle changes/CANONICAL promotions `0/0`; Package 003 modifications `0`; Package 005/006/007 activations `NO/NO/NO`; Human Performance resumed `NO`; Crypto modifications `0`; Persistence/Historical Truth/RAG/MCP/AI Agent implementations `NO`; unauthorized writes `0`.

Next safe action: `PACKAGE_004_WAVE_1_EXECUTION`. It is not executed by this decision.

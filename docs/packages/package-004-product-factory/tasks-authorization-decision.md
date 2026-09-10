# Package 004 — Tasks Authorization Decision

## Authoritative decision record

| Field | Value |
|---|---|
| Decision ID | `FD-P004-TASKS-AUTH-001` |
| Decision | `APPROVE_PACKAGE_004_TASKS_AUTHORIZATION` |
| Classification | `FOUNDER_DECISION` |
| Decisor | Founder |
| Effective timestamp | `2026-09-03T20:17:49-03:00` |
| Package | Package 004 — Product Factory |
| Previous state | `AUTHORIZED_FOR_DESIGN` |
| Resulting phase state | `TASKS_GENERATION_AUTHORIZED` |
| Requirements baseline | v1.0 — `APPROVED` — `FD-P004-REQ-001` |
| Design baseline | v1.0 — `APPROVED` — `FD-P004-DESIGN-001` |
| Authorization scope | Task planning/creation only |
| Tasks | `AUTHORIZED_FOR_CREATION` |
| Task execution | `NOT_AUTHORIZED` |
| Implementation | `NOT_AUTHORIZED` |

`TASKS_GENERATION_AUTHORIZED` is the established Package 003 precedent for the phase following approved Design. This decision does not invent a broader package lifecycle state or imply execution authority.

## Founder decision

[Decisión] The Founder authorizes creation of the Package 004 Task plan derived from Requirements v1.0 and Design v1.0. Tasks may be derived, structured, dependency-ordered, traced, reviewed and grouped into proposed execution waves. This decision creates no Task and authorizes no Task execution, software implementation or Product Factory operation.

## Authorization gates

| Gate | Result |
|---|---|
| Requirements | v1.0 `APPROVED`; 25 Requirements; 100 acceptance criteria |
| Requirements Founder decision | `FD-P004-REQ-001` |
| Requirements blocking remediation / normative change | `0 / 0` |
| Design | v1.0 `APPROVED` |
| Design Founder decision | `FD-P004-DESIGN-001` |
| Components / Design Decisions / diagrams | `20 / 15 / 7` |
| Requirements / acceptance-criteria Design coverage | `25/25 / 100/100` |
| Orphan normative Design decisions | `0` |
| Blocking Design remediation | `0` |
| `REQUIREMENTS_CHANGE_REQUIRED` | `0` |
| `ARCHITECTURE_CHANGE_REQUIRED` | `0` |
| Technology selection | `NONE` |

All mandatory gates pass. Plain approval is appropriate; no hidden condition is used to defer a defect.

## Authorized Task-planning contract

Every future Task must record Task ID, title, purpose, Requirements trace, Design Decision/component trace, inputs, outputs, dependencies, acceptance evidence, execution boundary, prohibited actions where applicable and completion condition. Orphan Tasks are prohibited. A work item requiring absent behavior must stop as `DESIGN_CHANGE_REQUIRED` or `REQUIREMENTS_CHANGE_REQUIRED`; Task planning cannot add Product Factory semantics.

The plan must be dependency-ordered rather than flat. It may derive coherent waves from foundation/integrity through core structures, governance, evidence/readiness, lifecycle/Registry, boundaries/manual workflow, controlled verification and final audit/closure. Exact Task IDs, counts, wave numbers and dependencies belong to `PACKAGE_004_TASKS`, not this authorization.

Planning may cover documentary Product aggregate/Candidate, lifecycle and terminal `REJECTED` outcome, composition and eligibility, ownership/SOT/provenance/versioning, quality/risk/value/demand/readiness, approval/activation, packaging/dependencies/sharing, review/deprecation/retirement, Registry, human governance/AI boundary, manual workflow, P003/P005 handoffs and domain-neutral extension. Every major Design area therefore has a legitimate realization path.

## Verification and historical-semantics protections

Future planning may define controlled verification for transition correctness, terminal `REJECTED` handling, readiness not becoming lifecycle, mandatory human approval, AI authority prohibition, eligibility consumption, restriction propagation, sharing/lifecycle separation, `ACTIVE ≠ PUBLIC`, the Revenue boundary, historical-truth preservation and manual operation. No verification is executed now.

`REJECTED` remains a terminal Candidate review outcome, not a lifecycle state, DEPRECATED or RETIRED. Its Candidate identity, evidence, authority, timestamp, reason and history must remain representable. A readiness result cannot cause an automatic transition. Synthetic scenarios, if later authorized by the approved plan, must be explicitly marked `CONTROLLED_TEST_FIXTURE` and cannot create a real Candidate, Product, attachment or approval.

Task planning should reuse the Design's common governance-record contract where compatible, without collapsing conceptually distinct decisions. This is a realization constraint, not a new Requirement.

## Asset boundary and current limitation

Package 004 may plan only the consuming side of `READ / REFERENCE / CONSUME DECISION`; `WRITE / OVERRIDE` against Package 003 authority is prohibited.

| P003 condition | Required P004 treatment |
|---|---|
| `CANDIDATE / UNDER_REVIEW` | `NOT_COMPOSABLE` |
| `VALIDATED / NOT_CANONICAL` | `REFERENCE_ONLY / NOT_ATTACHABLE` |
| `CANONICAL` with incomplete handoff | `NOT_ELIGIBLE` |
| `CANONICAL` with complete handoff | `ELIGIBLE_FOR_GOVERNED_ATTACHMENT` |

ASSET-1, ASSET-2 and ASSET-3 remain reference scenarios at `VALIDATED / NOT_CANONICAL / NOT_ATTACHABLE`. Zero currently attachable Assets does not block Task planning because documentary structures and controlled verification can be specified without an attachment. Asset governance is not weakened to advance Package 004.

## Human, AI and manual-first boundaries

Final Product and lifecycle authority remains human. Future Tasks may realize representations for AI permissions: READ, ANALYZE, SUMMARIZE, COMPARE and DETECT_GAP are non-authoritative assistance; DRAFT and RECOMMEND require human review. AI may not independently execute transitions, approve, change authority/provenance, override eligibility or authorize commercialization. No AI Agent is implemented or authorized.

The planned realization must preserve a complete governed documentary path. A database, automation, Package 006/007, Persistence/Historical Truth implementation, RAG, MCP or AI Agent Runtime cannot be mandatory. No language, framework, API, cloud, storage, RAG/MCP/Agent stack or UI technology is selected by this decision.

## Package and architecture boundaries

Package 003 remains sole authority for Asset identity, lifecycle, ownership, SOT, provenance, qualification, restrictions, versioning and attachment eligibility. Package 004 may plan the read-only consumer realization only.

Package 004 may plan a documentary Product→Revenue dossier but not pricing, payment, transaction, revenue accounting, optimization or commercialization execution. Package 005 remains DORMANT. Packages 006 and 007 remain DORMANT. The core and planned artifacts remain domain-neutral; Human Performance stays paused, no cross-domain Candidate is created, and the first real cross-domain Candidate retains the `DOMAIN_NEUTRALITY_REVIEW` trigger.

| Architecture control | Result |
|---|---|
| Baseline | `LABOS-ARCH-BASELINE-001` v1.0 `APPROVED_WITH_CONDITIONS` |
| Impact | `EXTENDS_BASELINE` |
| `MODIFY_BASELINE` | `NO` |
| Architecture Freeze | `PRESERVED` |
| Package 003 reopened | `NO` |
| Package 005 activated | `NO` |
| ADR required at authorization | `NO` |

Any future Task requiring frozen semantic change must stop under Architecture change control.

## Resulting authority and next safe action

Package 004 enters `TASKS_GENERATION_AUTHORIZED`, matching the established Package 003 phase vocabulary. Requirements v1.0 and Design v1.0 remain APPROVED. Tasks are `AUTHORIZED_FOR_CREATION`; Task execution and implementation remain `NOT_AUTHORIZED`.

Next safe action: `PACKAGE_004_TASKS`. Do not execute automatically.

## Integrity declaration

Tasks created/executed: `0 / 0`. Implementation: `0`. Product Candidates/Products/attachments: `0 / 0 / 0`. Asset lifecycle/CANONICAL changes: `0 / 0`. Package 003 changes caused by this decision: `0`. Package 005/006/007 activation: `NO / NO / NO`. Human Performance resumed: `NO`. Crypto modifications: `0`. Persistence/Historical Truth/RAG/MCP/AI Agent implementation: `NO / NO / NO / NO / NO`.


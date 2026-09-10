# Package 004 — Founder Task Plan Decision

## Authoritative decision record

| Field | Value |
|---|---|
| Decision ID | `FD-P004-TASKS-001` |
| Decision | `APPROVE_PACKAGE_004_TASKS` |
| Classification | `FOUNDER_DECISION` |
| Decisor | Founder |
| Effective timestamp | `2026-09-03T21:03:37-03:00` |
| Package | Package 004 — Product Factory |
| Previous package state | `TASKS_GENERATION_AUTHORIZED` |
| Resulting package state | `TASKS_GENERATION_AUTHORIZED` |
| Task Plan reviewed | v0.1 — `DRAFT / READY_FOR_FOUNDER_DECISION` |
| Approved Task Plan baseline | v1.0 — `TASKS_APPROVED` |
| Requirements baseline | v1.0 — `APPROVED` — `FD-P004-REQ-001` |
| Design baseline | v1.0 — `APPROVED` — `FD-P004-DESIGN-001` |
| Tasks authorization | `FD-P004-TASKS-AUTH-001` |
| Independent review | `PACKAGE_004_TASKS_APPROVE_WITH_NON_BLOCKING_NOTES` |
| Approval scope | Task Plan baseline only |
| Task execution / waves / implementation | `NOT_AUTHORIZED / NOT_AUTHORIZED / NOT_AUTHORIZED` |

The package-level phase label remains `TASKS_GENERATION_AUTHORIZED`: Package 003 precedent defines `TASKS_APPROVED` as the Task Plan status and records execution authorization separately, but does not establish a distinct post-approval package-state token. This decision does not invent one.

## Founder decision

[Decisión] The Founder approves Package 004 Task Plan v0.1 as the first approved Task Plan baseline, version v1.0, with status `TASKS_APPROVED`. The plan faithfully translates Requirements v1.0 and Design v1.0 into discrete, dependency-ordered, documentary-first and verifiable work without adding Product Factory semantics. Approval is plain; the three review notes remain genuinely non-blocking.

This decision approves only the plan. It executes no Task, authorizes no wave and grants no implementation, Product, Asset or commercialization authority.

## Baseline and coverage gates

| Control | Result |
|---|---|
| Requirements | v1.0 `APPROVED`; 25 Requirements; 100 acceptance criteria |
| Design | v1.0 `APPROVED`; 20 components; 15 Design Decisions |
| Task Plan | 32 Tasks; W0–W7 |
| Requirements coverage | `25/25` |
| Acceptance-criteria coverage | `100/100` |
| Design component coverage | `20/20` |
| Applicable Design Decision coverage | `15/15` |
| Orphan / duplicate Tasks | `0 / 0` |
| Requirements / Design / Architecture changes | `0 / 0 / 0` |
| Blocking remediation | `0` |

Every Task defines ID, title, purpose/type, Requirements and acceptance-criteria trace, Design/component/decision trace, inputs, outputs, dependencies, execution boundary, prohibited actions, acceptance evidence, completion condition, risk/caution and manual path. No Task requires the executor to invent scope.

## Granularity, dependency and waves

The 32 Tasks are independently reviewable. T004-020 (Registry), T004-027 (manual procedure) and T004-032 (final audit) are integration Tasks with broad dependencies but one coherent output each; none is a hidden “implement Product Factory” epic. No artificial micro-task or redundant governance system is required.

The eight-wave DAG preserves:

`baseline → core structures → composition/evidence → readiness → lifecycle/Registry → boundaries/manual workflow → controlled verification → final audit`.

Dependency cycles: `0`. Downstream prerequisites are explicit. Wave membership is planning structure only. All W0–W7 remain `NOT_AUTHORIZED_FOR_EXECUTION`; future authority may be granted wave-by-wave and must respect each wave's internal dependency layers.

## Task types and implementation classification

| Task type | Count |
|---|---:|
| TEMPLATE | 10 |
| GOVERNANCE_ARTIFACT | 4 |
| MATRIX | 4 |
| CONTROLLED_VERIFICATION | 4 |
| REGISTRY | 3 |
| WORKFLOW | 3 |
| INTERFACE_CONTRACT | 2 |
| AUDIT | 2 |

| Execution classification | Count |
|---|---:|
| DOCUMENTARY | 28 |
| CONTROLLED_VERIFICATION | 4 |
| SOFTWARE_IMPLEMENTATION | 0 |
| EXTERNAL_RESEARCH | 0 |
| REAL_WORLD_VALIDATION | 0 |

Documentary Tasks hide no software, market validation, real Product creation or external research. Package 004 v1 remains operable through templates, matrices, registries, workflows, governance records, interface contracts and audits without a database or platform runtime.

## Product, lifecycle and governance integrity

Tasks create structures/templates only. They do not automatically create real Candidates, Products, approvals, activations or commercial offerings. The lifecycle remains exactly `CANDIDATE → UNDER_REVIEW → READY → APPROVED → ACTIVE → DEPRECATED → RETIRED`. `REJECTED` is a terminal Candidate review outcome, not an eighth state, DEPRECATED or RETIRED.

The plan separately realizes Product Quality, Product Risk, Product Value and Demand Validation. Product Value preserves `HYPOTHESIZED / EVIDENCED / DEMONSTRATED`. Readiness remains a governed matrix without opaque score or automatic transition. Planned checks preserve `READY ≠ APPROVED`, `APPROVED ≠ ACTIVE`, `ACTIVE ≠ PUBLIC`, `ACTIVE ≠ COMMERCIALIZED` and `ACTIVE ≠ REVENUE_GENERATING`.

The reusable Governance Decision Record minimizes physical record proliferation while retaining distinct event authority/evidence. The Human Governance Gate keeps final authority with the Founder or explicitly delegated human. The AI matrix allows non-authoritative assistance and proposals under review, while autonomous transition, approval, authority/provenance change, eligibility override and commercialization remain prohibited.

## Controlled fixtures

Ten future documentary fixtures are explicitly classified `CONTROLLED_TEST_FIXTURE`: simple Candidate, rejected Candidate, VALIDATED/not-CANONICAL reference, synthetic eligible CANONICAL scenario, NOT_READY, READY-not-approved, approved-not-active, active-not-public, licence propagation and P005 handoff boundary. They remain synthetic, non-authoritative and unexecuted. The synthetic CANONICAL case changes no Asset lifecycle and performs no attachment.

No fixture or governed entity is created by this decision.

## Registry, source and history

The approved plan realizes manual Candidate/Product Registry views for identity, version, owner, lifecycle, composition/eligibility, restrictions, dependencies, evidence, readiness, approval, sharing, SOT and review/freshness. Product SOT, Asset SOT references, provenance, supersession, compatibility and review triggers remain distinct. `CURRENT_TRUTH` and `HISTORICAL_TRUTH` remain documentarily preservable without Historical Truth infrastructure.

## Package and Asset boundaries

P003→P004 remains `READ / REFERENCE / CONSUME DECISION`; `WRITE / OVERRIDE` is prohibited. Package 003 retains Asset identity, lifecycle, ownership, SOT, provenance, qualification, restrictions, versioning and attachment authority.

ASSET-1, ASSET-2 and ASSET-3 remain `VALIDATED / NOT_CANONICAL / REFERENCE_ONLY / NOT_ATTACHABLE`. The plan neither promotes nor attaches them.

P004→P005 remains a documentary Product→Revenue dossier. Pricing, payment, transaction, revenue accounting, optimization and commercialization execution are absent. Package 005 remains DORMANT. Packages 006/007 and future infrastructure are not dependencies. Human Performance remains paused, and `DOMAIN_NEUTRALITY_REVIEW` remains required for the first real cross-domain Candidate.

## Architecture status

| Control | Result |
|---|---|
| Architecture Baseline | `LABOS-ARCH-BASELINE-001` v1.0 `APPROVED_WITH_CONDITIONS` |
| Impact | `EXTENDS_BASELINE` |
| `MODIFY_BASELINE` | `NO` |
| Architecture Freeze | `PRESERVED` |
| Package 003 reopened | `NO` |
| ADR required | `NO` |
| Technology selections | `0` |

## Non-blocking notes

1. Resolve final filenames for reusable governance sections during W1 before downstream linking: `ACCEPTED / NON_BLOCKING`; operational only, no semantic dependency.
2. Future wave authorization must respect internal DAG layers: `ACCEPTED / NON_BLOCKING`; enforced by execution authorization review.
3. `CONTROLLED_TEST_FIXTURE` must be visually unmistakable: `ACCEPTED / NON_BLOCKING`; the fixture contract already requires explicit non-authoritative labelling.

No note became blocking or requires Requirements, Design or Architecture change.

## Resulting authority and next action

Requirements v1.0 and Design v1.0 remain APPROVED. Task Plan v1.0 is `TASKS_APPROVED`. Package-level phase remains `TASKS_GENERATION_AUTHORIZED` for lack of an established alternative package token. Task execution, W0–W7 and implementation remain `NOT_AUTHORIZED`.

Package 003 initially bundled Task Plan approval with W0–W1 execution authority, but this decision expressly does not. The separated next safe action is `PACKAGE_004_WAVE_0_AUTHORIZATION_DECISION`.

Do not execute it automatically.

## Integrity declaration

Task Plan semantic changes during approval: `NO`. Tasks/waves executed: `0 / 0`. Implementation: `0`. Product Candidates/Products/attachments: `0 / 0 / 0`. Asset lifecycle/CANONICAL changes: `0 / 0`. Package 003 changes caused: `0`. Package 005/006/007 activation: `NO / NO / NO`. Human Performance resumed: `NO`. Crypto modification: `0`. Persistence/Historical Truth/RAG/MCP/AI Agent implementation: `NO / NO / NO / NO / NO`.


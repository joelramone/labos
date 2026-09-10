# Package 004 — Founder Design Decision

## Authoritative decision record

| Field | Value |
|---|---|
| Decision ID | `FD-P004-DESIGN-001` |
| Decision | `APPROVE_PACKAGE_004_DESIGN` |
| Classification | `FOUNDER_DECISION` |
| Decisor | Founder |
| Effective timestamp | `2026-09-03T17:18:48-03:00` |
| Package | Package 004 — Product Factory |
| Prior package state | `AUTHORIZED_FOR_DESIGN` |
| Resulting package state | `AUTHORIZED_FOR_DESIGN` |
| Design reviewed | v0.1 — `DRAFT / READY_FOR_FOUNDER_DECISION` |
| Approved Design baseline | v1.0 — `APPROVED` |
| Requirements baseline | v1.0 — `APPROVED` — `FD-P004-REQ-001` |
| Design authorization | `FD-P004-DESIGN-AUTH-001` |
| Independent review | `PACKAGE_004_DESIGN_APPROVE_WITH_NON_BLOCKING_NOTES` |
| Approval scope | Design baseline only |
| Tasks / implementation | `NOT_AUTHORIZED / NOT_AUTHORIZED` |

## Founder decision

[Decisión] The Founder approves Package 004 Design v0.1 as the first approved Design baseline, version v1.0. The reviewed structure is complete, traceable, implementation-neutral, domain-neutral, manual-first and consistent with the Architecture Baseline and Freeze. This decision resolves Design approval only. It creates no Tasks and grants no Tasks-generation, execution or implementation authority.

## Completeness and traceability

| Control | Result |
|---|---|
| Conceptual components | `20` |
| Design Decisions | `15` |
| Mermaid diagrams | `7` |
| Requirements coverage | `25 / 25` |
| Acceptance criteria support | `100 / 100` |
| Orphan normative Design decisions | `0` |
| Blocking Design gaps | `0` |
| Technology selections | `NONE` |
| `REQUIREMENTS_CHANGE_REQUIRED` | `0` |
| `ARCHITECTURE_CHANGE_REQUIRED` | `0` |

The Design aggregate keeps Product Candidate and Product distinct and introduces no Product behavior beyond Requirements v1.0. The fifteen Design Decisions have rationale, Requirements trace, alternatives/constraints and consequences; none requires Requirements or Architecture change.

## Lifecycle and REJECTED confirmation

The approved lifecycle has exactly seven states:

`CANDIDATE → UNDER_REVIEW → READY → APPROVED → ACTIVE → DEPRECATED → RETIRED`.

[Decisión] `REJECTED` remains a terminal Candidate review outcome, not an eighth lifecycle state. A rejected Candidate preserves its identity, evidence, human decision authority, timestamp and reason; it does not become RETIRED, DEPRECATED or ACTIVE and cannot silently re-enter progression. Any later reconsideration must use an appropriate new governed review or Candidate path under the approved governance.

Every governed transition identifies source, destination, trigger, evidence, guard, human authority and resulting record. Automatic lifecycle promotion is prohibited. Readiness outcomes are decision-record results; they are not lifecycle states and cannot directly mutate lifecycle.

## Composition and Package 003 authority

The approved composition model supports one Asset, multiple Assets, shared Asset dependencies and external dependencies without requiring software or multiple Assets. It references upstream Asset identity, version, SOT, provenance, ownership, restrictions and eligibility rather than copying or replacing Asset authority.

The Package 003 interface is strictly `READ / REFERENCE / CONSUME DECISION`; `WRITE / OVERRIDE` is prohibited. Package 003 remains sole authority over Asset identity, lifecycle, ownership, SOT, provenance, qualification, restrictions, versioning and attachment eligibility.

| P003 condition | Approved P004 treatment |
|---|---|
| `CANDIDATE / UNDER_REVIEW` | `NOT_COMPOSABLE` |
| `VALIDATED / NOT_CANONICAL` | `REFERENCE_ONLY / NOT_ATTACHABLE` |
| `CANONICAL` with incomplete P003 handoff | `NOT_ELIGIBLE` |
| `CANONICAL` with complete P003 handoff | `ELIGIBLE_FOR_GOVERNED_ATTACHMENT` |

ASSET-1, ASSET-2 and ASSET-3 remain `VALIDATED / NOT_CANONICAL / REFERENCE_ONLY / NOT_ATTACHABLE`. This decision creates no Candidate or attachment and changes no Asset.

## Readiness, evidence and governance

Readiness remains a governed, non-numeric matrix over composition, evidence, Product quality, Product risk, provenance, ownership, dependencies, restrictions, target consumer, demand evidence and documentation. It is neither automatic threshold nor commercialization permission.

Product Quality, Product Risk, Product Value and Demand Validation remain separate evidence models. Product value is `HYPOTHESIZED`, `EVIDENCED` or `DEMONSTRATED`; Asset value does not transfer automatically. Composition may preserve or increase upstream restrictions and may not silently reduce them.

The reusable Human Governance Gate records requested action, subject/state, evidence, restrictions, decision, human authority, timestamp, rationale, resulting or unchanged state and follow-up. Final authority remains human. AI may read, analyze, summarize, compare, detect gaps, draft and recommend subject to the approved permission matrix; it may not execute transitions, approve, change authority/provenance, override eligibility or authorize commercialization.

The complete workflow remains operable with governed documents and records. Package 006/007, a database, automation, Persistence/Historical Truth implementation, RAG, MCP and AI Agent Runtime are not dependencies.

## Registry, provenance, versioning and historical truth

The conceptual Registry answers Candidate/Product identity, lifecycle, version, owner, composition/eligibility, restrictions, dependencies, evidence, readiness, approval, sharing, SOT and review timing. Current truth is distinguishable from immutable historical decisions. Each governed Product version has one Product SOT distinct from Asset SOT references.

Traceability supports `Research → Knowledge → Asset → Product Candidate → Product` where applicable, without fabricating absent links. Product identity/version, supersession, Asset-version dependency, compatibility, material change and review triggers use only the version semantics mandated by Requirements v1.0. No Historical Truth infrastructure is required.

## Approval, activation, sharing and retirement

`READY`, `APPROVED` and `ACTIVE` remain separate human-governed stages. `APPROVED ≠ ACTIVE`; `ACTIVE` implies neither PUBLIC, COMMERCIALIZED nor REVENUE_GENERATING. Sharing is orthogonal to lifecycle and cannot broaden upstream licensing, sensitivity or Asset restrictions. Review/freshness triggers do not automatically change state. Deprecation and retirement preserve the approved progression and historical truth.

## Package boundaries and architecture

Package 004 consumes Package 003 decisions without authority leakage. The Product→Revenue handoff is a documentary dossier containing the approved Product identity/version, owner/SOT, consumer/problem/value proposition, demand evidence, composition/dependencies, restrictions, readiness, approval/activation and provenance. It stops before pricing, payment, transaction, revenue accounting or revenue optimization and does not activate Package 005.

The core remains domain-neutral: it contains no trading lifecycle, profitability gate, backtesting, optimizer, journal or software-only assumption. The first real cross-domain Product Candidate must trigger `DOMAIN_NEUTRALITY_REVIEW`. Human Performance remains paused.

| Architecture control | Result |
|---|---|
| Architecture Baseline | `LABOS-ARCH-BASELINE-001` v1.0 `APPROVED_WITH_CONDITIONS` |
| Architecture Freeze | `PRESERVED` |
| Conflict classification | `NO_CONFLICT`, with documented Design clarifications only |
| Requirements change required | `0` |
| Architecture change required | `0` |

## Non-blocking notes

1. The prior note requesting Founder confirmation of the `REJECTED` representation is `RESOLVED` by this decision.
2. Future realization should minimize physical governance-record proliferation by reusing the common record contract. `PRESERVED / NON_BLOCKING`.
3. Future tests should prevent readiness outputs from being stored or interpreted as lifecycle states. `PRESERVED / NON_BLOCKING`.
4. The first real cross-domain Candidate triggers `DOMAIN_NEUTRALITY_REVIEW`. `PRESERVED / NON_BLOCKING`.

Notes 2–4 are realization considerations traceable to the approved Design; they do not create new Requirements.

## Resulting authority and next action

Package 004 remains `AUTHORIZED_FOR_DESIGN`. Requirements v1.0 remain `APPROVED`; Design v1.0 is `APPROVED`. Tasks and implementation remain `NOT_AUTHORIZED` because this decision's approval scope is Design baseline only. Package 003 remains CLOSED. Packages 005, 006 and 007 remain DORMANT.

Next safe action: `PACKAGE_004_TASKS_AUTHORIZATION_DECISION`. Do not execute automatically.

## Integrity declaration

Requirements normative changes: `NO`. Founder decision recorded: `YES`. Tasks/implementation: `0 / 0`. Product Candidates/Products/attachments: `0 / 0 / 0`. Asset lifecycle/CANONICAL changes: `0 / 0`. Package 003 changes caused by this decision: `0`. Package 005/006/007 activation: `NO / NO / NO`. Human Performance resumed: `NO`. Crypto modifications: `0`. Persistence/Historical Truth/RAG/MCP/AI Agent implementation: `NO / NO / NO / NO / NO`.

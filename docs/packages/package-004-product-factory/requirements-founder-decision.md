# Package 004 — Requirements Founder Decision

## Decision record

| Field | Value |
|---|---|
| Decision ID | `FD-P004-REQ-001` |
| Decision | `APPROVE_PACKAGE_004_REQUIREMENTS` |
| Classification | `FOUNDER_DECISION` |
| Decisor | Founder |
| Effective timestamp | `2026-09-03T09:05:30-03:00` |
| Package | `Package 004 — Product Factory` |
| Requirements reviewed | v0.1, `DRAFT / READY_FOR_FOUNDER_DECISION` |
| Approved baseline | v1.0, `APPROVED` |
| Package state before | `AUTHORIZED_FOR_REQUIREMENTS` |
| Package state after | `AUTHORIZED_FOR_REQUIREMENTS` |
| Review verdict | `PACKAGE_004_REQUIREMENTS_APPROVE_WITH_NON_BLOCKING_NOTES` |
| Scope | Requirements baseline only |

## Founder determination

The Founder approves the Package 004 Requirements as the normative v1.0 baseline. The approval is unconditional at Requirements level: all mandatory gates pass, blocking requirement gaps are zero, unresolved authority conflicts are zero and no architecture change is required. Existing activation conditions and the five independent-review notes remain authoritative; they do not constitute defects in the approved baseline.

This decision does not authorize Design, Tasks, implementation, Product Candidate or Product creation, Asset attachment, Asset lifecycle change, commercialization, or activation of Packages 005–007.

## Gate evidence

| Control | Result |
|---|---|
| Top-level Requirements | `25 / 25` |
| Acceptance criteria | `100` |
| Requirements without criteria | `0` |
| Orphan Requirements | `0` |
| Required coverage omissions | `0` |
| Traceability / testability | `PASS / PASS` |
| Normative language | `PASS` |
| Technology / domain neutrality | `PASS / PASS` |
| Blocking gaps / authority conflicts | `0 / 0` |
| Architecture changes required | `0` |

## Approved Product model

- Product is a governed entity distinct from Idea, Research, Knowledge, Asset, Product Candidate, Revenue, Capability and Lab.
- Product Candidate is a governed proposal and conveys no Product approval, demand validation, commercialization or Revenue readiness.
- The v1 lifecycle is `CANDIDATE → UNDER_REVIEW → READY → APPROVED → ACTIVE → DEPRECATED → RETIRED`.
- `REJECTED` is a terminal review outcome record, not an eighth lifecycle state. A renewed proposal requires a new Candidate identity.
- `NO_PRODUCT_FAST_PATH_IN_V1` remains binding.

## Attachment eligibility determination

Package 003 remains authoritative for Asset attachment eligibility:

| Asset condition | Product Factory treatment |
|---|---|
| `CANDIDATE` or `UNDER_REVIEW` | `NOT_COMPOSABLE` |
| `VALIDATED / NOT_CANONICAL` | `REFERENCE_ONLY / NOT_ATTACHABLE` |
| `CANONICAL` with incomplete handoff gates | `NOT_ELIGIBLE` |
| `CANONICAL` with complete Package 003 handoff | `ELIGIBLE_FOR_GOVERNED_ATTACHMENT` |

The complete handoff includes applicable stability, ownership, relevance, Revenue_Thesis presence, maintainability, licensing/sensitivity, version compatibility and dependency declarations. Product approval cannot override ineligibility. P004 trigger eligibility based on VALIDATED Assets is distinct from Product attachment eligibility.

ASSET-1, ASSET-2 and ASSET-3 remain `VALIDATED / NOT_CANONICAL / NOT_ATTACHABLE` and are reference cases only.

## Governance and evidence constraints

- Product Candidate Owner and Product Owner must be human.
- Final Product authority remains the Founder or an explicitly delegated human.
- AI ownership, AI final approval, automatic Product approval, automatic promotion and automatic Asset attachment are prohibited.
- Manual-first operation is mandatory; Packages 006/007, Persistence, Historical Truth implementation, RAG, MCP and AI Agent Runtime are not mandatory dependencies.
- Product quality is distinct from Asset quality. Product risk aggregates applicable upstream risks without reducing them through composition.
- Product value uses `HYPOTHESIZED`, `EVIDENCED`, `DEMONSTRATED`; it does not inherit Asset value and does not imply revenue.
- Demand validation requires a falsifiable hypothesis, target segment, method, observable signal, pass/fail criterion, timeframe and evidence source; it is neither a transaction nor Revenue validation.
- Readiness is governed across composition, evidence, quality, risk, provenance, ownership, dependencies, restrictions, target consumer, demand evidence and documentation. `READY ≠ APPROVED ≠ ACTIVE`; none implies commercialization.

## Package and architecture boundaries

- Package 003 retains Asset identity, lifecycle, ownership, provenance, SOT, qualification, restrictions, versioning and attachment eligibility.
- Package 004 owns Product/Candidate semantics, lifecycle, composition, quality, risk, readiness, approval, packaging, dependencies, sharing and retirement.
- Package 004 stops before pricing execution, payment, transaction, revenue accounting and revenue optimization; Package 005 remains dormant.
- Packages 006 and 007 remain dormant. Future infrastructure remains optional and dormant.
- The approved Requirements extend the planned Architecture Baseline without modifying frozen upstream semantics. Architecture Freeze and change control remain in force.

## Commercialization boundary

`Product approved ≠ commercialization authorized`; `Product active ≠ Public`; `demand validated ≠ transaction`; `Product readiness ≠ revenue`; and `VALIDATED Asset ≠ commercially distributable Asset`. Product packaging cannot broaden upstream rights.

## Non-blocking notes preserved

1. Design must distinguish the `REJECTED` terminal outcome from active `UNDER_REVIEW`.
2. Design may formalize templates and cardinalities but must not add contradictory normative requirements.
3. The first real cross-domain Product Candidate must trigger domain-neutrality review.
4. Package 000's `productizado` terminology must not be used as Product lifecycle shorthand.
5. Current ASSET-1/2/3 are not attachment-eligible.

No note became blocking.

## Resulting authority

Requirements v1.0 is authoritative. Package 004 remains `AUTHORIZED_FOR_REQUIREMENTS`; approval does not silently create `AUTHORIZED_FOR_DESIGN` authority. The next safe action is `PACKAGE_004_DESIGN_AUTHORIZATION_DECISION`. Until that separate Founder decision, `PACKAGE_004_DESIGN` is not authorized.

## Integrity declaration

Design created: NO. Tasks created: NO. Implementation: NO. Product Candidates/Products/attachments: `0 / 0 / 0`. Asset lifecycle/CANONICAL changes: `0 / 0`. Package 003 modifications: `0`. Package 005/006/007 activations: `NO / NO / NO`. Human Performance resumed: NO. Crypto modifications: `0`. RAG/MCP/AI Agent implementation: NO.

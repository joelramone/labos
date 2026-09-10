# Package 004 — Design Authorization Decision

## Decision record

| Field | Value |
|---|---|
| Decision ID | `FD-P004-DESIGN-AUTH-001` |
| Decision | `APPROVE_PACKAGE_004_DESIGN_AUTHORIZATION` |
| Classification | `FOUNDER_DECISION` |
| Decisor | Founder |
| Effective timestamp | `2026-09-03T09:12:16-03:00` |
| Package | `Package 004 — Product Factory` |
| Prior state | `AUTHORIZED_FOR_REQUIREMENTS` |
| Resulting state | `AUTHORIZED_FOR_DESIGN` |
| Requirements baseline | v1.0, `APPROVED`, `FD-P004-REQ-001` |
| Authorization scope | Design only |

## Decision

The Founder authorizes Package 004 to begin Design against the unchanged approved Requirements v1.0 baseline. The decision is a plain approval: all mandatory gates remain satisfied and no additional material condition is required beyond the approved Requirements, Architecture Baseline, activation conditions and preserved review notes.

Design may resolve implementation-neutral structural detail and produce conceptual models, templates, schemas, cardinalities, state diagrams and interfaces only where traceable to approved Requirements. A structural decision that needs new normative behavior must be classified `REQUIREMENTS_CHANGE_REQUIRED` and routed through change control.

## Authorization gates

| Gate | Result |
|---|---|
| Requirements version/status | `1.0 / APPROVED` |
| Founder Requirements decision | `FD-P004-REQ-001` |
| Top-level Requirements / acceptance criteria | `25 / 100` |
| Blocking remediation | `0` |
| Unresolved architecture conflicts | `0` |
| Architecture changes required | `0` |
| Requirements integrity | `PASS` |
| Package-state precedent | `AUTHORIZED_FOR_DESIGN` confirmed |

## Design scope

Design is authorized to define implementation-neutral structures for Product and Product Candidate identity, lifecycle and guards, Registry, composition and Asset references, ownership/authority, SOT/provenance/versioning, quality/risk/value/demand evidence, readiness and approval records, packaging, dependencies, review/freshness, sharing, retirement, Package 005 handoff, manual workflows and AI permission boundaries.

## Baseline constraints

- Lifecycle remains `CANDIDATE → UNDER_REVIEW → READY → APPROVED → ACTIVE → DEPRECATED → RETIRED`.
- `REJECTED` remains a terminal review outcome, not an eighth state.
- `NO_PRODUCT_FAST_PATH_IN_V1` remains binding.
- Human ownership and final approval remain mandatory; automatic approval, promotion and attachment remain prohibited.
- Product quality, risk and value remain distinct from Asset quality, risk and value.
- Manual/documentary operation must remain complete without a database, automation, Package 006/007, Persistence, Historical Truth implementation, RAG, MCP or AI Agent Runtime.
- AI may assist with inspection, summarization, comparison, drafting, gap detection and recommendation but may not exercise ownership, final approval, lifecycle authority, attachment override, commercialization authority, provenance erasure or silent canonical modification.

## Asset attachment constraints

Package 003 remains authoritative:

| Asset condition | Design treatment |
|---|---|
| `CANDIDATE` or `UNDER_REVIEW` | `NOT_COMPOSABLE` |
| `VALIDATED / NOT_CANONICAL` | `REFERENCE_ONLY / NOT_ATTACHABLE` |
| `CANONICAL` with incomplete handoff | `NOT_ELIGIBLE` |
| `CANONICAL` with complete Package 003 handoff | `ELIGIBLE_FOR_GOVERNED_ATTACHMENT` |

Design may consume but not redefine this contract. ASSET-1, ASSET-2 and ASSET-3 remain non-attachable.

## Package and architecture boundaries

- Package 003 owns Asset governance and attachment eligibility.
- Package 004 owns Product governance, composition and readiness.
- Package 005 owns pricing, transactions and the revenue lifecycle and remains dormant.
- Packages 006 and 007 remain dormant; future infrastructure remains optional.
- Authorization `EXTENDS_BASELINE`; it does not `MODIFY_BASELINE`, reopen Package 003 or require an ADR now.
- Architecture Freeze is preserved. A future Design need to alter frozen semantics must stop and be classified `ARCHITECTURE_CHANGE_REQUIRED`.

## Non-blocking notes preserved

1. Design must clearly distinguish terminal `REJECTED` from active `UNDER_REVIEW`.
2. Templates and cardinalities must not add contradictory Requirements.
3. The first real cross-domain Product Candidate must trigger domain-neutrality review.
4. Package 000 `productizado` terminology must not be Product lifecycle shorthand.
5. Current ASSET-1/2/3 are not attachment-eligible.

No note became blocking.

## Explicit exclusions

Tasks, implementation, Product Candidate/Product creation, Asset attachment or lifecycle change, CANONICAL promotion, commercialization, and Package 005/006/007 activation are not authorized. No Design artifact is created by this decision.

## Result and next action

Requirements: `APPROVED v1.0`. Design: `AUTHORIZED`. Tasks: `NOT_AUTHORIZED`. Implementation: `NOT_AUTHORIZED`.

Next safe action: `PACKAGE_004_DESIGN`.

## Integrity declaration

Design documents created: `0`. Tasks: `0`. Implementation: `0`. Product Candidates/Products/attachments: `0 / 0 / 0`. Asset lifecycle/CANONICAL changes: `0 / 0`. Package 003 changes: `0`. Package 005/006/007 activations: `NO / NO / NO`. Human Performance resumed: `NO`. Crypto modified: `NO`. RAG/MCP/AI Agents implemented: `NO`.

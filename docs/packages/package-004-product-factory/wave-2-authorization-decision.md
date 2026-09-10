# Package 004 — Wave 2 Authorization Decision

## Decision record

| Field | Decision |
|---|---|
| Decision ID | `FD-P004-W2-AUTH-001` |
| Decision | `APPROVE_PACKAGE_004_WAVE_2_AUTHORIZATION` |
| Classification | `FOUNDER_DECISION` |
| Founder | LabOS Founder Governance Authority |
| Effective timestamp | `2026-09-04T10:39:45-03:00` |
| Package | Package 004 — Product Factory |
| Scope | Wave 2 only; authorization does not execute W2 or authorize W3–W7 |
| Prior state | W0 `COMPLETE`; W1 `COMPLETE`; W2–W7 `NOT_AUTHORIZED_FOR_EXECUTION` |
| Result | W2 `AUTHORIZED_FOR_EXECUTION / NOT_STARTED`; global execution `PARTIALLY_AUTHORIZED / W2_ONLY` |
| Implementation | `NOT_AUTHORIZED` |
| Next safe action | `PACKAGE_004_WAVE_2_EXECUTION` |

## Founder determination

The Founder authorizes W2 for ordered documentary execution. W0 and W1 completed cleanly, the approved Requirements, Design and Task Plan remain fresh, the W1 artifact-path baseline is stable, and W2 can realize composition, P003 eligibility consumption, dependencies, packaging and provenance without implementation, real entities, real attachment, upstream mutation or architecture change.

This decision is authorization only. It executes no Task. T004-006–010 remain `NOT_STARTED`; each may start only when every prerequisite in its approved Task contract is `COMPLETE`.

## Previous-wave gate

| Control | Repository evidence | Result |
|---|---|---|
| T004-001 / W0 | `wave-0-baseline-integrity-record.md` | `COMPLETE / COMPLETE` |
| W0 independent review | Same record | `PACKAGE_004_WAVE_0_APPROVE` |
| T004-002–005 / W1 | `wave-1-execution-record.md` and four stable templates | `4/4 COMPLETE / W1 COMPLETE` |
| W1 independent review | `wave-1-execution-record.md` | `PACKAGE_004_WAVE_1_APPROVE` |
| W0/W1 blockers | Execution records | `0` |
| W1 filename baseline | Four authorized paths | `STABLE / PRESENT`; conflicts `0` |

## Baseline freshness and architecture gate

| Baseline/control | Current authoritative state | Finding |
|---|---|---|
| Requirements | v1.0 `APPROVED` — `FD-P004-REQ-001` | `BASELINE_FRESHNESS_CONFIRMED`; post-W1 semantic changes `0` |
| Design | v1.0 `APPROVED` — `FD-P004-DESIGN-001` | `BASELINE_FRESHNESS_CONFIRMED`; post-W1 semantic changes `0` |
| Task Plan | v1.0 `TASKS_APPROVED` — `FD-P004-TASKS-001` | `BASELINE_FRESHNESS_CONFIRMED`; membership/semantics changes `0` |
| Architecture | `LABOS-ARCH-BASELINE-001` v1.0 `APPROVED_WITH_CONDITIONS` | Impact `EXTENDS_BASELINE`; `MODIFY_BASELINE: NO` |
| Architecture Freeze | `PRESERVED` | Requirements/Design/Task Plan/Architecture changes `0/0/0/0` |
| ADR | Change-control review | `NOT_REQUIRED` |

Authorization/status metadata is non-normative and does not alter any baseline.

## W2_TASK_SET

Approved membership is exactly T004-006–010.

| Task | Title | Type / execution classification | Dependencies | Inputs | Expected output | Acceptance evidence | Completion condition / prohibited actions |
|---|---|---|---|---|---|---|---|
| T004-006 | Create Product composition record template | `TEMPLATE / DOCUMENTARY` | T004-003 | Product record, P003 Asset authority, composition Design | Versioned composition snapshot with input identity/version, contribution, relationship, SOT/provenance/restriction and fit references | Cardinality/restriction mapping for one, many, shared and external cases; unresolved license/risk blocks Product gate only | Complete when every upstream constraint maps to effect or justified non-applicability; no embedded Asset authority, attachment or eligibility grant |
| T004-007 | Create P003 attachment-eligibility reference contract | `INTERFACE_CONTRACT / DOCUMENTARY` | T004-006 | Composition output and closed P003 Asset→Product handoff | Eligibility-reference template for P003 decision/evidence, intended Product use and immutable consumption result | Only `READ / REFERENCE / CONSUME DECISION`; exact four P003 outcome mappings | Complete when P004 may reject fit but cannot grant eligibility; no `WRITE / OVERRIDE / RECOMPUTE` or Asset update |
| T004-008 | Create Product dependency declaration | `REGISTRY / DOCUMENTARY` | T004-003, T004-006 | Product record, composition output and dependency Design | Four-class dependency template with identity, type, version/compatibility, purpose, criticality, provider, restrictions, status, failure impact, fallback/exit and review trigger | Asset/external/operational/platform completeness plus undeclared/critical-change scenario criteria | Complete when all classes and failure behavior are inspectable; no implicit RAG, MCP, agents, automation or Persistence dependency |
| T004-009 | Create Product packaging manifest | `TEMPLATE / DOCUMENTARY` | T004-003, T004-006, T004-007, T004-008 | Product record, composition, eligibility and dependency outputs | Technology-neutral manifest for Product/version, eligible Asset/SOT references, documentation, guidance, restrictions, dependencies, provenance, consumer and delivery assumptions | Required-element/gap audit, exact input versions and point-of-delivery restriction visibility | Complete when gaps are explicit and rights unchanged; no packaging technology selection or broadened right |
| T004-010 | Create Product provenance record | `REGISTRY / DOCUMENTARY` | T004-002, T004-003, T004-005, T004-006 | W1 Candidate/Product/ownership-SOT outputs, composition and upstream provenance references | Provenance graph record with source authority, exact versions, Candidate origin, decision references and explicit missing-link gaps | Complete/partial/external-origin lineage cases answer evidence, Assets/versions and human decisions | Complete when absent links remain honest gaps; no copied authority, fabricated evidence or overwritten history |

Execution classifications: `DOCUMENTARY 5`; `SOFTWARE_IMPLEMENTATION 0`; `EXTERNAL_RESEARCH 0`; `REAL_WORLD_VALIDATION 0`; `CONTROLLED_VERIFICATION 0`.

## W2 dependency readiness

`W2_DEPENDENCY_READINESS: READY`.

| Task | Upstream prerequisites now | Internal W2 start gate |
|---|---|---|
| T004-006 | T004-003 `COMPLETE` | Ready when W2 execution is invoked |
| T004-007 | None outside completed baseline/W1 | Must wait for T004-006 `COMPLETE` |
| T004-008 | T004-003 `COMPLETE` | Must wait for T004-006 `COMPLETE` |
| T004-009 | T004-003 `COMPLETE` | Must wait for T004-006, T004-007 and T004-008 `COMPLETE` |
| T004-010 | T004-002, T004-003 and T004-005 `COMPLETE` | Must wait for T004-006 `COMPLETE` |

All prerequisites exist. W3+ prerequisites: `0`. DAG cycles: `0`. Authorization covers the wave; it does not waive Task start gates. Execution order is T004-006; then T004-007/T004-008; then T004-009; T004-010 after T004-006 and its completed W1 sources.

## Documentary-first and semantic boundaries

W2 is executable with documents, templates, Registry-style records, manual contracts and governance references only. Database, application, API, UI, automation, Persistence, Historical Truth implementation, RAG, MCP, agents and infrastructure are neither selected nor required.

A composition snapshot belongs to one Candidate/Product version and may contain `1..N` governed inputs, `0..N` Asset references depending on domain, shared Asset references and declared external inputs/dependencies. W2 imposes no single-Asset, multi-Asset, software or trading requirement. Outputs reference `product-record-template.md`; they do not duplicate the Product aggregate.

Where human decisions are needed, W2 outputs reference `governance-decision-record-template.md` and use event-specific payloads without inventing an incompatible envelope. Final authority remains human. AI assistance is optional and `NON_AUTHORITATIVE`; AI cannot grant/override eligibility, approve attachment, remove restrictions or alter provenance.

## Asset eligibility and P003 interface

The exact consumed Package 003 contract is:

| P003 Asset condition | P004 consumption result |
|---|---|
| `CANDIDATE` or `UNDER_REVIEW` | `NOT_COMPOSABLE` |
| `VALIDATED / NOT_CANONICAL` | `REFERENCE_ONLY / NOT_ATTACHABLE` |
| `CANONICAL` with incomplete P003 handoff | `NOT_ELIGIBLE` with named gaps |
| `CANONICAL` with complete P003 handoff | `ELIGIBLE_FOR_GOVERNED_ATTACHMENT`; P004 may still reject Product fit |

P003→P004 remains strictly `READ / REFERENCE / CONSUME DECISION`; `WRITE / OVERRIDE / RECOMPUTE` is prohibited. Template ≠ attachment; eligibility decision ≠ attachment; reference ≠ attachment; Product approval ≠ eligibility override.

ASSET-1, ASSET-2 and ASSET-3 remain `VALIDATED / NOT_CANONICAL / NOT_ATTACHABLE`. Future W2 execution may mention them only as `READ_ONLY / REFERENCE_ONLY / NOT_ATTACHABLE`; it may not create a real attachment record.

## Restriction, dependency and provenance boundary

Every applicable upstream licensing, sharing, usage, dependency, distribution, sensitivity and risk constraint must retain its source authority and provenance, map to an effective Product restriction or justified non-applicability, expose conflicts, and route competent changes to human review at the owning authority layer. Composition and packaging cannot silently reduce or broaden rights.

Dependency declarations support identity, class/source, version/compatibility, purpose, provider/authority, provenance, restriction/licensing reference, criticality, status, failure/absence impact, fallback/exit and review trigger. No dependency-management technology is selected. Provenance gaps remain explicit and may not be fabricated.

## W2_ARTIFACT_PATH_BASELINE

The approved Tasks define semantics but not filenames. This authorization establishes the following documentary paths without changing Task meaning:

| Task | Stable future CREATE path |
|---|---|
| T004-006 | `docs/packages/package-004-product-factory/product-composition-record-template.md` |
| T004-007 | `docs/packages/package-004-product-factory/p003-attachment-eligibility-reference-contract.md` |
| T004-008 | `docs/packages/package-004-product-factory/product-dependency-declaration-template.md` |
| T004-009 | `docs/packages/package-004-product-factory/product-packaging-manifest-template.md` |
| T004-010 | `docs/packages/package-004-product-factory/product-provenance-record-template.md` |

### Future W2 execution write boundary

- `CREATE`: the five stable Task outputs above and one documentary execution evidence record, `docs/packages/package-004-product-factory/wave-2-execution-record.md`.
- `UPDATE`: `tasks.md`, `tasks-execution-waves.md` and `README.md`, status/evidence metadata only.
- `READ_ONLY`: Requirements, Design and Task Plan normative semantics; Founder decisions; W0/W1 records and artifacts; architecture baseline/freeze/change control; all Package 003 and Asset records; Package 005–007; Human Performance; Crypto; future infrastructure records.

No W2 output is created by this authorization decision. The only authorized writes now are this decision record and the three authorization-status metadata updates.

## Execution success and stop conditions

Future execution may mark a W2 Task `COMPLETE` only when its artifact exists, approved traceability and acceptance evidence are recorded, prerequisites were complete at start, no real entity/attachment was created, and human/P003/architecture boundaries remain intact.

Execution must stop the affected branch as `W2_EXECUTION_BLOCKED` and classify `DESIGN_CHANGE_REQUIRED`, `REQUIREMENTS_CHANGE_REQUIRED` or `ARCHITECTURE_CHANGE_REQUIRED` as applicable upon Asset-authority ambiguity, eligibility mismatch, missing Design authority, weakened restrictions, unresolved composition semantics, need to modify Package 003, need for implementation or architecture conflict. Silent remediation is prohibited.

## Resulting authorization and integrity

| Scope | Result |
|---|---|
| W0 | `COMPLETE` |
| W1 | `COMPLETE` |
| T004-006–010 / W2 | `AUTHORIZED_FOR_EXECUTION / NOT_STARTED` |
| W3–W7 | `NOT_AUTHORIZED_FOR_EXECUTION` |
| Global Task execution | `PARTIALLY_AUTHORIZED / W2_ONLY` |
| Implementation | `NOT_AUTHORIZED` |

Integrity after authorization: W2 Tasks executed `0`; W3–W7 authorized `0`; implementation `0`; Product Candidates `0`; Products `0`; attachments `0`; Asset lifecycle changes/CANONICAL promotions `0/0`; Package 003 modifications `0`; Package 005/006/007 activations `NO/NO/NO`; Human Performance resumed `NO`; Crypto modifications `0`; Persistence/Historical Truth/RAG/MCP/AI Agent implementations `NO/NO/NO/NO/NO`; external research/real-world validation `0/0`; unauthorized writes `0`.

Next safe action: `PACKAGE_004_WAVE_2_EXECUTION`. It is not executed by this decision.


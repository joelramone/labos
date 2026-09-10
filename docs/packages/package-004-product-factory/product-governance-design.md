# Package 004 — Product Governance Design

## Common governance record

Candidate intake, review, readiness, approval, activation, risk acceptance, sharing, freshness review, deprecation, retirement and Revenue handoff reuse one envelope:

`record_id`, action requested, subject identity/version, current state, evidence references, restrictions, decision/result, human authority/delegation reference, timestamp, reason, resulting state or unchanged-state result, and follow-up/review trigger.

Specialized payloads add only content required by their approved Requirement. AI may draft the envelope; only competent human authority finalizes authority-controlled decisions.

## Human Governance Gate

The gate verifies action, subject/current state, evidence completeness, applicable restrictions, transition guard and human authority. It emits an immutable decision record and either the permitted resulting state or a named failure with no state change.

| Gate result | Meaning | Lifecycle effect |
|---|---|---|
| `DECIDED_PASS` | Competent human authority accepts the requested governed action | Only the exact transition/action named in the record may occur |
| `DECIDED_FAIL` | Guard, evidence, restriction or authority fails | State remains unchanged; named failures and follow-up are preserved |
| `RETURNED_FOR_REVIEW` | Human decision requires clarification or additional evidence | State remains unchanged; this is not a lifecycle state |

## Readiness model

Readiness is a matrix, not a score. It evaluates composition, evidence, quality, risk, provenance, ownership, dependencies, restrictions, target consumer, demand evidence and documentation. The governed decision result is `READY`, `NOT_READY` or `REVIEW_REQUIRED`; the first is a decision result authorizing the separately recorded transition to lifecycle state `READY`, while the others preserve `UNDER_REVIEW`. These labels are evaluation outcomes in the readiness record, not additional lifecycle states. Every result names the human decisor, date, subject/version, evidence, rationale, restrictions, per-control blocking disposition and follow-up.

## Quality evidence

The quality packet references evidence for composition correctness, completeness, usability, reproducibility where applicable, dependency integrity, documentation, consumer suitability, failure behavior and operational readiness. Each dimension records `PASS`, `PARTIAL`, `FAIL` or `NOT_APPLICABLE`, evidence and blocking disposition. Asset quality is input evidence only.

## Risk evidence

The risk packet covers financial, legal/licensing, operational, technical, evidence, user-impact, misuse, dependency and reputational categories with likelihood, impact, mitigation, residual status and blocking decision. Upstream restrictions propagate. Any acceptance/escalation identifies competent human authority, scope, expiry/review trigger and rationale.

## Value and demand

Value classification progresses only by evidence:

- `HYPOTHESIZED`: consumer + problem + value proposition.
- `EVIDENCED`: dated non-transactional demand evidence in target context.
- `DEMONSTRATED`: real use plus attributable user outcome.

Demand Validation Record: hypothesis, target segment, method, observable signal, pass/fail criterion, timeframe, evidence source, dated context and participant/source, result, limitations, privacy/sensitivity handling and human review authority. Neither classification nor demand result implies readiness, approval, transaction or Revenue.

## Review and freshness record

A review record compares current evidence, dependencies, restrictions and source accessibility with the prior decision. It identifies the triggering material Asset/Product/dependency/version/schema, licensing/risk, new or failed-use evidence, demand/consumer/context, first external exposure, source failure or scheduled freshness date; records impact and human disposition; and preserves lifecycle unless a separate authorized transition is approved.

## Approval and activation

READY → APPROVED requires a human approval record referencing the exact evidence packet and restrictions. APPROVED → ACTIVE requires a separate activation record defining delivery/operating scope. AI output or record completeness cannot execute either transition.

## AI permission matrix

| Operation | Classification | Constraint |
|---|---|---|
| READ, ANALYZE, SUMMARIZE, COMPARE, DETECT_GAP | `ALLOWED` | Preserve source references and uncertainty |
| DRAFT, RECOMMEND, PROPOSE_TRANSITION | `ALLOWED_WITH_HUMAN_REVIEW` | Non-authoritative; no state change |
| EXECUTE_TRANSITION, APPROVE | `PROHIBITED` | Human authority required |
| CHANGE_AUTHORITY, CHANGE_PROVENANCE | `PROHIBITED` | Owning governance only; history cannot be erased |

## Domain extension

Domain extensions may supply domain-specific quality evidence, risk evidence and dependency types through referenced evidence profiles. They cannot change core lifecycle, authority, Registry truth or Package boundaries. The first real cross-domain Candidate triggers `DOMAIN_NEUTRALITY_REVIEW` before its next governance gate.

Trace: R07, R11–R16, R19–R20, R22–R24.

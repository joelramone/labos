# Product Approval and Activation Event Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank event-specific payloads. This file creates no Product approval, activation, lifecycle transition, Public status, commercialization, Revenue status, or governed decision.

## Common authority boundary

Task: `T004-018`. Use each payload with `governance-decision-record-template.md`; do not create a competing governance envelope. Founder or an explicitly delegated competent human is final authority. AI/software may read, analyze, compare, draft, recommend and detect gaps, but may not approve, activate, manufacture evidence, override Readiness/Risk/Asset eligibility/restrictions, or execute a transition.

`READY ≠ APPROVED`; `APPROVED ≠ ACTIVE`; `READY ≠ ACTIVE`.

## Product approval event — READY → APPROVED

| Field | Entry |
|---|---|
| Product reference / SOT | `<REQUIRED>` |
| Product version | `<REQUIRED>` |
| Current state / requested target | `READY / APPROVED` |
| Readiness decision reference | `<REQUIRED>` |
| Evidence references | `<REQUIRED>` |
| Restrictions | `<REQUIRED REFERENCES or NONE with rationale>` |
| Approval authority / delegation | `<FOUNDER or DELEGATED HUMAN / REFERENCE>` |
| Governance decision record | `<REQUIRED REFERENCE>` |
| Decision timestamp / effective timestamp | `<ISO 8601 WITH OFFSET>` |
| Approval conditions and exact scope | `<REQUIRED>` |
| Rationale | `<REQUIRED>` |
| Review trigger | `<DATE/EVENT>` |
| Supersession/history reference | `<REFERENCE or NONE>` |
| Activation status | `NOT_GRANTED_BY_THIS_EVENT` |
| Public/commercial/revenue implication | `NONE` |

Approval fails closed and leaves state unchanged when Product/version, readiness, evidence, restrictions, scope, or human authority is missing or invalid. APPROVED does not imply ACTIVE, PUBLIC, COMMERCIALIZED or REVENUE_GENERATING.

## Product activation event — APPROVED → ACTIVE

| Field | Entry |
|---|---|
| Product reference / SOT | `<REQUIRED>` |
| Product version | `<REQUIRED>` |
| Current state / requested target | `APPROVED / ACTIVE` |
| Prior approval decision | `<REQUIRED REFERENCE>` |
| Activation prerequisites/evidence | `<REQUIRED REFERENCES>` |
| Delivery/operating scope | `<REQUIRED>` |
| Operational controls | `<REQUIRED>` |
| Restrictions | `<REQUIRED REFERENCES or NONE with rationale>` |
| Activation authority / delegation | `<FOUNDER or DELEGATED HUMAN / REFERENCE>` |
| Governance decision record | `<REQUIRED REFERENCE>` |
| Decision timestamp / effective timestamp | `<ISO 8601 WITH OFFSET>` |
| Activation conditions | `<REQUIRED>` |
| Rationale | `<REQUIRED>` |
| Review trigger | `<DATE/EVENT>` |
| Supersession/history reference | `<REFERENCE or NONE>` |
| Public/commercial/revenue implication | `NONE` |

Activation fails closed and leaves state unchanged when exact Product/version, prior approval, prerequisites, scope, controls, restrictions, or human authority is missing or invalid. ACTIVE does not imply PUBLIC, COMMERCIALIZED or REVENUE_GENERATING.

## Separation checklist

- [ ] Approval and activation use separate decision IDs, payloads, guards, authorities, timestamps and history references.
- [ ] Approval references a valid readiness decision for the exact Product/version; it does not activate.
- [ ] Activation references a valid prior approval for the exact Product/version; it does not grant sharing or commercialization.
- [ ] Quality, Risk, Value, Demand Validation and Readiness remain separate evidence authorities.
- [ ] Asset eligibility and restrictions remain P003-authoritative and are not overridden.
- [ ] Missing/invalid guard or authority yields failed/returned decision and `UNCHANGED` lifecycle.
- [ ] AI/software is non-authoritative and executed no event.
- [ ] No real Product, event, transition, Public/commercial/revenue status or Registry entry exists here.

## Traceability

| Trace type | Approved mapping |
|---|---|
| Task | `T004-018` |
| Requirements / acceptance criteria | `R16`; `R16.1–R16.4`; `R22.1` |
| Design components | `C05`, `C19` |
| Design Decisions | `P004-D004`, `P004-D008`, `P004-D009` |
| Authoritative inputs | `product-record-template.md`, `governance-decision-record-template.md`, `product-readiness-matrix-template.md`, `lifecycle-transition-matrix-and-guard-checklist.md` |

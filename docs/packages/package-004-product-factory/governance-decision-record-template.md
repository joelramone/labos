# Governance Decision Record Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank reusable structure. It records no actual decision and executes no transition, approval, activation, sharing, risk acceptance, commercialization or other governance action.

## Purpose

Provide one reusable governance envelope plus event-specific payloads without making distinct decisions semantically identical.

## Usage and authority boundary

- Complete the common envelope and exactly the payload(s) required by the selected decision type. Event-specific evidence, guards and authority remain mandatory even when the common fields are complete.
- Final authority is the Founder or an explicitly delegated human with competence for the action. AI or software may never be recorded as final governance authority.
- AI-generated content is `NON_AUTHORITATIVE` until reviewed and accepted by human authority. AI may read, analyze, summarize, compare, draft, recommend, detect gaps and, where authorized, propose a transition. AI may not execute a transition, approve, change authority/provenance/ownership, override attachment eligibility or authorize commercialization.
- A decision record is immutable historical evidence. Correction or replacement uses a superseding record; do not silently rewrite it.
- Package 003 decisions remain authoritative for Assets. This template may reference/consume them and cannot override them.

## Common required envelope

Use `MISSING — <named gap>` for absent required information. A missing/invalid guard or authority fails closed and preserves current state.

| Field | Entry |
|---|---|
| Decision ID | `<DECISION_ID — PLACEHOLDER; do not use a real ID in this template>` |
| Decision type | `<CANDIDATE_REVIEW / PRODUCT_READINESS / PRODUCT_APPROVAL / PRODUCT_ACTIVATION / RISK_ACCEPTANCE / SHARING_DECISION / REVIEW_DECISION / DEPRECATION / RETIREMENT / REVENUE_HANDOFF or other approved type>` |
| Subject/entity type | `<Product Candidate / Product / Product version / other approved subject>` |
| Subject identity/reference | `<REQUIRED>` |
| Subject version | `<VALUE or NOT_APPLICABLE>` |
| Current lifecycle state | `<EXACT CURRENT STATE or NOT_APPLICABLE>` |
| Requested action | `<REQUIRED>` |
| Requestor/actor | `<REQUIRED reference>` |
| Evidence considered | `<REQUIRED references; see event payload>` |
| Restrictions/constraints | `<REQUIRED references or NONE with rationale>` |
| Decision authority | `<REQUIRED Founder or explicitly delegated human>` |
| Delegated-authority reference | `<REFERENCE or NOT_APPLICABLE>` |
| Decision | `<DECIDED_PASS / DECIDED_FAIL / RETURNED_FOR_REVIEW or approved event result>` |
| Resulting state/result | `<EXACT RESULTING STATE/RESULT or UNCHANGED>` |
| Reason/rationale | `<REQUIRED>` |
| Decision timestamp | `<REQUIRED ISO 8601 with offset>` |
| Effective timestamp | `<ISO 8601 with offset or NOT_APPLICABLE>` |
| Provenance/source references | `<REQUIRED; include AI assistance and uncertainty where used>` |
| Supersedes/reference | `<PRIOR DECISION REFERENCE or NONE>` |
| Follow-up action | `<REQUIRED action/owner/due trigger or NONE>` |
| Review trigger/expiry | `<DATE/EVENT or NOT_APPLICABLE with reason>` |
| Record status | `<DRAFT_NON_AUTHORITATIVE / FINAL_AUTHORITATIVE / SUPERSEDED>` |

### Fail-closed control

| Check | Result | Named gap/reference |
|---|---|---|
| Subject/current state verified | `<PASS / FAIL>` | `<VALUE>` |
| Requested action is permitted | `<PASS / FAIL>` | `<VALUE>` |
| Required event evidence complete | `<PASS / FAIL>` | `<VALUE>` |
| Restrictions satisfied/preserved | `<PASS / FAIL>` | `<VALUE>` |
| Human authority valid for this event | `<PASS / FAIL>` | `<VALUE>` |
| Transition guard valid, if applicable | `<PASS / FAIL / N/A>` | `<VALUE>` |

Any `FAIL` yields `DECIDED_FAIL` or `RETURNED_FOR_REVIEW`, with lifecycle state `UNCHANGED`. Record completeness alone never executes an action.

## Event-specific payload selector

| Decision type | Mandatory specialized payload/evidence | Semantic protection |
|---|---|---|
| Candidate review | Candidate identity, intake/evidence/restriction review, outcome, terminality when rejected | `REJECTED` is terminal outcome, not lifecycle state; no silent re-entry |
| Product readiness | Eleven-control readiness reference, blocking dispositions, exact subject/version | `READY` decision result is separate from approval/activation |
| Product approval | Valid readiness packet, exact Product/version, scope and restrictions | `READY ≠ APPROVED`; valid human approval required |
| Product activation | Prior approval, delivery/operating scope, controls and effective date | `APPROVED ≠ ACTIVE`; ACTIVE implies neither Public nor commercial/revenue status |
| Risk acceptance | Risk categories, likelihood/impact, mitigation, residual/blocking status, acceptance scope and expiry | Does not reduce upstream restriction or Asset risk outside competent authority |
| Sharing decision | Audience/context, licensing, sensitivity, risk, Product/upstream restrictions, effective scope | Lifecycle ≠ sharing; ACTIVE ≠ PUBLIC; most restrictive rule preserved |
| Review decision | Trigger, comparison with prior decision, freshness/source access and impact | Review does not automatically change lifecycle |
| Deprecation | Reason, consumers/dependencies, successor and migration/exit plan | No silent retirement |
| Retirement | Prior DEPRECATED record, obligations/exceptions, historical preservation | RETIRED is terminal; no deletion/reactivation |
| Revenue handoff | Approved Product/version/state and complete documentary dossier reference | Dossier only; no P005 activation, pricing, transaction or revenue action |

## Specialized payloads

Complete only the section matching the decision type. Reference dedicated later-wave evidence artifacts where required; do not fabricate them in W1.

### Candidate review

| Field | Entry |
|---|---|
| Candidate record/SOT reference | `<REFERENCE>` |
| Intake/evidence/restriction findings | `<REFERENCES>` |
| Review outcome | `<ACCEPTED_FOR_GOVERNED_CONTINUATION / RETURNED_FOR_REVIEW / REJECTED>` |
| Terminality acknowledged | `<YES required for REJECTED / N/A>` |
| Historical preservation reference | `<REFERENCE required for final REJECTED>` |
| Renewed-proposal rule | `New Candidate identity required; link to this record; no re-entry` |

### Product readiness

| Field | Entry |
|---|---|
| Eleven-control readiness matrix reference | `<REFERENCE>` |
| Mandatory blocking controls | `<NONE or named controls>` |
| Readiness result | `<READY / NOT_READY / REVIEW_REQUIRED>` |
| Lifecycle transition separately authorized | `<DECISION REFERENCE or NO>` |

### Product approval

| Field | Entry |
|---|---|
| Product/version | `<REFERENCE>` |
| Readiness decision/evidence packet | `<REFERENCE>` |
| Approval scope | `<VALUE>` |
| Approval restrictions | `<VALUE>` |
| Activation status | `NOT_GRANTED_BY_THIS_DECISION` |

### Product activation

| Field | Entry |
|---|---|
| Product/version | `<REFERENCE>` |
| Prior approval decision | `<REFERENCE>` |
| Delivery/operating scope | `<VALUE>` |
| Operational controls | `<VALUE>` |
| Sharing/commercial/revenue implication | `NONE` |

### Risk acceptance

| Field | Entry |
|---|---|
| Risk record reference | `<REFERENCE>` |
| Residual risk and blocking disposition | `<VALUE>` |
| Acceptance scope | `<VALUE>` |
| Competent human authority basis | `<REFERENCE>` |
| Expiry/review trigger | `<VALUE>` |
| Upstream restrictions preserved | `<YES / NO — NO fails closed>` |

### Sharing decision

| Field | Entry |
|---|---|
| Requested audience/context | `<VALUE>` |
| Licensing/sensitivity/risk references | `<REFERENCES>` |
| Product and upstream restriction references | `<REFERENCES>` |
| Effective most-restrictive scope | `<VALUE>` |
| Lifecycle/commercialization implication | `NONE` |

### Review decision

| Field | Entry |
|---|---|
| Trigger | `<DATE/EVENT>` |
| Prior decision reference | `<REFERENCE>` |
| Evidence/dependency/restriction/source comparison | `<REFERENCES and finding>` |
| Freshness/source-access finding | `<VALUE>` |
| Human disposition | `<VALUE>` |
| Lifecycle effect | `<UNCHANGED unless separately authorized decision is referenced>` |

### Deprecation

| Field | Entry |
|---|---|
| Product/version | `<REFERENCE>` |
| Reason/trigger evidence | `<VALUE/REFERENCES>` |
| Affected consumers/dependencies | `<REFERENCES>` |
| Successor | `<REFERENCE or NONE>` |
| Migration/exit plan | `<REFERENCE>` |

### Retirement

| Field | Entry |
|---|---|
| Product/version | `<REFERENCE>` |
| Prior DEPRECATED decision | `<REFERENCE>` |
| Active-consumer obligations | `<RESOLVED references / documented exceptions>` |
| Historical SOT/decision preservation | `<REFERENCES>` |
| Reactivation | `PROHIBITED; renewed demand follows a governed new Candidate/version path` |

### Revenue handoff

| Field | Entry |
|---|---|
| Product→Revenue dossier reference | `<REFERENCE>` |
| Approved Product/version/state verification | `<REFERENCE>` |
| Boundary confirmation | `No pricing execution, payment, transaction, accounting, optimization, revenue record or P005 activation` |

## Validation checklist

- [ ] Banner remains `TEMPLATE — NOT_A_GOVERNED_INSTANCE`; no real decision ID or actual decision is present.
- [ ] Common envelope is complete or gaps are named; exactly the relevant specialized payload is used.
- [ ] Distinct decision types retain their event-specific evidence, guards, result and authority.
- [ ] Final authority is Founder or explicitly delegated human; AI/software is never authority.
- [ ] Invalid authority/evidence/restrictions preserve current state and fail closed.
- [ ] `REJECTED` is only a terminal Candidate review outcome with immutable history and no re-entry.
- [ ] Approval and activation are separate; sharing/commercialization/Revenue are not inferred.
- [ ] P003 Asset authority and restrictions remain referenced and unmodified.
- [ ] Supersession preserves the prior record; no history is overwritten.
- [ ] No technology, implementation, automation or autonomous agent dependency is assumed.

## Traceability and related references

| Trace type | Approved source |
|---|---|
| Task | `T004-004` |
| Requirements / acceptance criteria | `R03.2–R03.4`, `R07.2`, `R12.3`, `R15.3`, `R16.1–R16.4`, `R22.3`, `R24.1–R24.3`, `R25.4` |
| Design components | `C05`, `C17`, `C19` |
| Design Decisions | `P004-D004`, `P004-D008`, `P004-D009`, `P004-D012` |
| Upstream | `requirements.md`, `design.md`, `product-governance-design.md`, `product-lifecycle-design.md`, `design-decision-register.md` |
| Downstream | T004-005, T004-012, T004-015–018, T004-021–024 (later-wave authority required) |


# Deprecation and Retirement Decision Sections

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank event payloads. This file executes no deprecation, retirement, deletion, reactivation, approval, activation or other lifecycle transition.

## Lifecycle and authority boundary

Task: `T004-023`. Use these payloads with `governance-decision-record-template.md`; do not create a competing decision envelope.

The lifecycle remains exactly `CANDIDATE → UNDER_REVIEW → READY → APPROVED → ACTIVE → DEPRECATED → RETIRED`. `REJECTED` is a terminal Candidate review outcome, not a lifecycle state. Approved deprecation paths are `APPROVED → DEPRECATED` and `ACTIVE → DEPRECATED`; retirement is only `DEPRECATED → RETIRED`. Direct retirement and reactivation are prohibited.

Founder or explicitly delegated competent human Product Authority decides. Freshness, Quality, Risk, Value, Demand Validation, Readiness, usage or AI recommendation may trigger review but cannot automatically deprecate or retire.

## Deprecation payload

| Field | Entry |
|---|---|
| Product / exact version / Product SOT | `<REQUIRED REFERENCES>` |
| Current state / requested target | `<APPROVED or ACTIVE> / DEPRECATED` |
| Trigger and reason | `<REQUIRED>` |
| Trigger evidence | `<REQUIRED REFERENCES>` |
| Review/freshness record | `<REFERENCE>` |
| Approval/activation history | `<REFERENCES>` |
| Version/compatibility record | `<REFERENCE>` |
| Current Registry/history view | `<REFERENCES>` |
| Affected consumers | `<REFERENCES or NONE EVIDENCED>` |
| Affected dependencies/compositions | `<REFERENCES>` |
| Successor | `<REFERENCE or NONE>` |
| Migration/exit plan | `<REQUIRED>` |
| Notice/restriction continuation | `<REQUIRED>` |
| Exceptions and competent authority | `<REFERENCES or NONE>` |
| Decision authority/delegation | `<HUMAN REFERENCE>` |
| Effective time and review trigger | `<ISO 8601 / EVENT>` |
| Governance Decision Record | `<REQUIRED for an actual decision>` |

Deprecation does not delete, retire, reactivate, remove restrictions or erase existing obligations. New consumers are prohibited unless a competent human exception remains within all restrictions.

## Retirement payload

| Field | Entry |
|---|---|
| Product / exact version / Product SOT | `<REQUIRED REFERENCES>` |
| Current state / requested target | `DEPRECATED / RETIRED` |
| Prior DEPRECATED decision/history | `<REQUIRED REFERENCE>` |
| Deprecation period and notices | `<REFERENCES>` |
| Consumer obligations | `<RESOLVED REFERENCES or documented exceptions>` |
| Dependency/composition obligations | `<RESOLVED REFERENCES or documented exceptions>` |
| Migration/exit completion | `<REFERENCE>` |
| Remaining legal/licensing/risk duties | `<REFERENCES>` |
| Historical SOT/decision preservation | `<REQUIRED REFERENCES>` |
| Successor/cross-references | `<REFERENCE or NONE>` |
| Decision authority/delegation | `<HUMAN REFERENCE>` |
| Effective time | `<ISO 8601 WITH OFFSET>` |
| Governance Decision Record | `<REQUIRED for an actual decision>` |
| Reactivation | `PROHIBITED; renewed demand follows a new governed Candidate/version path` |

## Fail-closed guard checklist

- [ ] Exact Product/version and current state resolve from Product SOT and Registry current truth.
- [ ] Requested transition is `APPROVED→DEPRECATED`, `ACTIVE→DEPRECATED` or `DEPRECATED→RETIRED` only.
- [ ] Trigger evidence and review record are cited; trigger alone did not execute the transition.
- [ ] Consumer/dependency impact, successor, migration/exit, notices, restrictions and exceptions are resolved or explicitly blocking.
- [ ] Retirement references a prior DEPRECATED decision and resolved obligations.
- [ ] Founder/delegated competent human authority, rationale, timestamp and immutable decision history are present.
- [ ] AI/software did not decide, execute or rewrite the transition/history.
- [ ] Missing/invalid evidence, state, prior decision, obligations or authority leaves lifecycle `UNCHANGED`.
- [ ] Historical evidence is preserved; correction uses supersession, never deletion or silent rewrite.

## Traceability

| Trace | Approved source |
|---|---|
| Task | `T004-023` |
| Requirements / AC | `R24`; `R24.1–R24.4`; `R23.2–R23.4` |
| Design components | `C05`, `C17`, `C19` |
| Design Decisions | `P004-D004`, `P004-D008`, `P004-D010` |
| Inputs | `governance-decision-record-template.md`, `lifecycle-transition-matrix-and-guard-checklist.md`, `product-approval-and-activation-event-template.md`, `product-version-and-compatibility-record-template.md`, `manual-product-registry-contract.md`, `product-review-and-freshness-record-checklist.md` |

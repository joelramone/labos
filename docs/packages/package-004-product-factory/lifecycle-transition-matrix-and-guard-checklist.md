# Lifecycle Transition Matrix and Guard Checklist

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Documentary workflow structure only. This file creates no Candidate, Product, lifecycle transition, review outcome, approval, activation, deprecation, retirement, or historical event.

## Authority and invariant

Task: `T004-016`. The complete Product lifecycle is exactly:

`CANDIDATE → UNDER_REVIEW → READY → APPROVED → ACTIVE → DEPRECATED → RETIRED`

`REJECTED` is a terminal Candidate review outcome attached to an `UNDER_REVIEW` Candidate; it is not an eighth Product lifecycle state. `NO_PRODUCT_FAST_PATH_IN_V1` is binding. Any transition not enumerated below fails closed and leaves state unchanged.

`READY ≠ APPROVED`; `APPROVED ≠ ACTIVE`; `READY ≠ ACTIVE`; `ACTIVE ≠ PUBLIC`; `ACTIVE ≠ COMMERCIALIZED`; `ACTIVE ≠ REVENUE_GENERATING`.

## Approved transition matrix

| ID | Source | Target / outcome | Required evidence | Required prerequisites and guards | Blocking conditions | Required human authority | Decision record / effective time | Restrictions, review trigger and history |
|---|---|---|---|---|---|---|---|---|
| T01 | Entry | `CANDIDATE` | Complete intake request; Candidate identity and SOT reference | Intake identifies owner and does not claim Product status | Missing identity/SOT/owner; Product or attachment claim | Human Candidate Owner | Intake record; recorded effective timestamp | Preserve source restrictions; review trigger; predecessor/history reference or `NONE` |
| T02 | `CANDIDATE` | `UNDER_REVIEW` | Review request; composition proposal; evidence and restriction inventory | Owner identified; review formally initiated | Incomplete inventory, invalid authority, silent completeness promotion | Founder or delegated human reviewer authority | Governance decision reference; effective timestamp | Preserve all restrictions; review trigger; prior-state/history reference |
| T03 | `UNDER_REVIEW` | `READY` | Readiness decision and eleven-control matrix | Applicable composition, evidence, Quality, Risk, provenance, ownership, dependencies, restrictions, consumer, Demand Validation and documentation controls pass | Any mandatory control fails; missing evidence/authority; inferred readiness | Founder or delegated human Product Authority | Readiness decision reference; effective timestamp | Carry restrictions and gaps; review trigger; supersession/history reference |
| T04 | `UNDER_REVIEW` | `REJECTED` outcome | Candidate review evidence and explicit rationale | Terminality acknowledged; exact Candidate/version verified | Missing reason/evidence/authority; attempted Product-state mutation or silent re-entry | Founder or delegated human Product Authority | Candidate review decision reference; effective timestamp | Preserve evidence/restrictions; reconsideration requires new governed proposal; immutable history link |
| T05 | `READY` | `APPROVED` | Valid readiness packet for exact Product/version/scope | Readiness reference valid; restrictions and approval scope explicit | Missing/invalid readiness or authority; attempted activation/Public/commercial inference | Founder or delegated human Product Authority | Product approval decision reference; effective timestamp | Restrictions continue; review trigger; supersession/history reference |
| T06 | `APPROVED` | `ACTIVE` | Prior approval; delivery/operating scope and controls | Exact approved Product/version; separate activation decision | Missing approval/scope/controls/authority; Public/sale/revenue inference | Founder or delegated human Product Authority | Activation decision reference; effective timestamp | Explicit activation restrictions; review trigger; supersession/history reference |
| T07 | `APPROVED` | `DEPRECATED` | Safety/supersession rationale; dependency/consumer impact and exit plan | Exact Product/version and governed deprecation decision | Missing impact/exit plan/authority; direct retirement | Human Product Authority | Deprecation decision reference; effective timestamp | Restrictions/notices continue; review trigger; successor/history reference |
| T08 | `ACTIVE` | `DEPRECATED` | Trigger evidence; impact; notices and migration plan | Exact Product/version and governed deprecation decision | Missing evidence/plan/authority; unrestricted new consumers | Human Product Authority | Deprecation decision reference; effective timestamp | Preserve restrictions and migration scope; review trigger; successor/history reference |
| T09 | `DEPRECATED` | `RETIRED` | Resolved obligations or explicit exceptions; preserved history | Prior DEPRECATED entry exists; consumer/dependency obligations addressed | Missing prior entry/authority/history; deletion or reactivation | Human Product Authority | Retirement decision reference; effective timestamp | Historical restrictions/evidence retained; terminal status; supersession/history reference |

Review/freshness flags never execute a transition. `APPROVED → DEPRECATED` is the only pre-activation deprecation path; `ACTIVE → DEPRECATED → RETIRED` is mandatory after activation. No other arrow or bypass is approved.

## Per-request guard checklist

- [ ] Exact subject identity, Product/Candidate version and current state are verified from their authoritative SOT.
- [ ] Requested source/target pair is one of T01–T09; otherwise record failure and preserve current state.
- [ ] Required evidence, prerequisites and event-specific payload are present and authoritative.
- [ ] Quality, Risk, Product Value, Demand Validation and Readiness remain separate; Asset Quality/Value do not substitute for Product Quality/Value.
- [ ] P003 Asset eligibility and version truth are referenced, never rewritten, recomputed, promoted or downgraded.
- [ ] All licensing, usage, sharing, distribution, dependency and risk restrictions propagate fail-closed.
- [ ] Founder or explicitly delegated competent human authority is verified and referenced.
- [ ] The existing `governance-decision-record-template.md` envelope is used; no competing governance envelope exists.
- [ ] Effective timestamp, rationale, review trigger and supersession/history references are recorded.
- [ ] CANDIDATE did not skip UNDER_REVIEW; UNDER_REVIEW did not skip readiness evaluation.
- [ ] READY did not imply APPROVED or ACTIVE; APPROVED did not imply ACTIVE.
- [ ] ACTIVE did not imply PUBLIC, COMMERCIALIZED or REVENUE_GENERATING.
- [ ] AI/software only read, analyze, compare, draft, recommend or detect gaps; neither executed nor overrode the decision.
- [ ] No historical evidence is overwritten; correction creates a superseding reference.

Any failed or missing guard yields `DECIDED_FAIL` or `RETURNED_FOR_REVIEW`, lifecycle `UNCHANGED`, and a named gap. AI may not execute, approve, activate, deprecate, retire, override guards, manufacture evidence, or change authority.

## Traceability

| Trace type | Approved mapping |
|---|---|
| Task | `T004-016` |
| Requirements / acceptance criteria | `R03`; `R03.1–R03.4`; `R16.3–R16.4`; `R24.2` |
| Design component | `C05` |
| Design Decisions | `P004-D003`, `P004-D004`, `P004-D009` |
| Authoritative inputs | `product-lifecycle-design.md`, `product-governance-design.md`, `governance-decision-record-template.md`, `product-readiness-matrix-template.md` |

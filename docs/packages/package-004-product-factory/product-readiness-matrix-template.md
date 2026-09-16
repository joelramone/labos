# Product Readiness Matrix Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary structure. It records no actual readiness decision and executes no lifecycle transition, approval, activation, publication or commercialization.

## Purpose and authority

Assess readiness through eleven independent controls without an opaque score or compensating threshold. The governed evaluation result is exactly `READY`, `NOT_READY` or `REVIEW_REQUIRED`. `READY` is a decision result that may support a separately recorded transition to lifecycle state READY; completing this matrix does not execute that transition.

Final authority is the Founder or explicitly delegated human Product Authority. Any actual decision reuses `governance-decision-record-template.md`. AI may assist non-authoritatively but cannot override a control or decide readiness.

## Subject identity

| Field | Entry |
|---|---|
| Product/Product Candidate reference | `<REQUIRED>` |
| Exact Product version | `<VALUE or NOT_APPLICABLE>` |
| Product SOT | `<REQUIRED>` |
| Current lifecycle state | `<REQUIRED>` |
| Readiness record ID/version | `<REQUIRED>` |
| Requested gate | `<REQUIRED>` |
| Truth classification | `<CURRENT_TRUTH / HISTORICAL_TRUTH>` |
| Supersedes | `<REFERENCE or NONE>` |

## Eleven-control readiness matrix

| # | Control | Evidence/reference | Finding | Mandatory/applicable | Blocking status and rationale | Restrictions/gaps |
|---|---|---|---|---|---|---|
| 1 | Composition | `<REFERENCE>` | `<DESCRIPTIVE>` | `<YES/NO + basis>` | `<BLOCKS / DOES_NOT_BLOCK>` | `<VALUE>` |
| 2 | Evidence | `<REFERENCE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |
| 3 | Quality | `<product-quality evaluation reference>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |
| 4 | Risk | `<product-risk evaluation reference>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |
| 5 | Provenance | `<REFERENCE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |
| 6 | Ownership | `<REFERENCE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |
| 7 | Dependencies | `<REFERENCE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |
| 8 | Restrictions | `<REFERENCES>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |
| 9 | Target consumer | `<REFERENCE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |
| 10 | Demand evidence | `<demand validation reference>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |
| 11 | Documentation | `<REFERENCES>` | `<DESCRIPTIVE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |

A mandatory FAIL or insufficient-evidence control prevents `READY`. Controls do not compensate for one another and no numeric or composite score is permitted.

## Human readiness decision section

| Field | Entry |
|---|---|
| Governance decision record | `<REQUIRED reference>` |
| Evaluation result | `<READY / NOT_READY / REVIEW_REQUIRED>` |
| Human decisor and authority basis | `<REQUIRED>` |
| Decision timestamp | `<ISO 8601 with offset>` |
| Product/Candidate and exact version | `<REQUIRED>` |
| Evidence basis | `<REQUIRED references>` |
| Rationale | `<REQUIRED>` |
| Preserved restrictions | `<REQUIRED>` |
| Blocking controls/gaps | `<LIST or NONE>` |
| Follow-up/review trigger | `<REQUIRED>` |
| Lifecycle transition decision | `<SEPARATE REFERENCE or NOT_EXECUTED>` |

`READY ≠ APPROVED ≠ ACTIVE`. `READY` does not imply Public, commercial or revenue-generating status. `APPROVED ≠ ACTIVE`; `ACTIVE ≠ PUBLIC / COMMERCIALIZED / REVENUE_GENERATING`. AI recommendation without valid human authority leaves lifecycle unchanged.

## Validation checklist

- [ ] All eleven controls have evidence and blocking status.
- [ ] Mandatory failure or insufficient evidence prevents `READY`.
- [ ] No score, weighting or automatic threshold is used.
- [ ] Human authority, date, subject/version, evidence, rationale and restrictions are explicit.
- [ ] Evaluation result and lifecycle transition remain separate records.
- [ ] Readiness does not grant approval, activation, sharing or commercialization.
- [ ] Product restrictions and upstream Asset/dependency authority remain unchanged.
- [ ] No real governed decision or lifecycle transition exists in this template.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-015` |
| Requirements / acceptance criteria | `R15`; `R15.1–R15.4`; `R16.2` |
| Design components | `C06`, `C19` |
| Design Decisions | `P004-D007`, `P004-D008`, `P004-D009`, `P004-D011` |
| Inputs | Governance, composition, dependencies, quality, risk, Product Value and demand records |

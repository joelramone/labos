# Product Quality Evaluation Matrix Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary structure. It evaluates no real Product or Product Candidate and grants no readiness, approval, activation, attachment, lifecycle or commercialization outcome.

## Purpose and authority

Evaluate Product-level quality independently from Asset quality. Asset quality may be referenced as input evidence but cannot substitute for a failed Product-level mandatory control. Final interpretation belongs to the Founder or explicitly delegated competent human; AI assistance is `NON_AUTHORITATIVE`.

## Subject and evaluation identity

| Field | Entry |
|---|---|
| Product/Product Candidate reference | `<REQUIRED>` |
| Product version | `<EXACT VERSION or NOT_APPLICABLE>` |
| Product SOT | `<REQUIRED>` |
| Composition reference/version | `<REQUIRED>` |
| Dependency declaration reference/version | `<REQUIRED>` |
| Evaluation ID/version | `<REQUIRED>` |
| Truth classification | `<CURRENT_TRUTH / HISTORICAL_TRUTH>` |
| Evaluation timestamp | `<ISO 8601 with offset>` |
| Human reviewer/authority | `<REQUIRED>` |
| Supersedes | `<REFERENCE or NONE>` |

## Nine-dimension matrix

Use only `PASS`, `PARTIAL`, `FAIL` or `NOT_APPLICABLE`. `NOT_APPLICABLE` requires rationale. A narrative judgment cannot convert missing evidence into PASS.

| # | Product-quality dimension | Applicability/rationale | Evidence reference | Result | Mandatory for requested gate | Blocking disposition | Restrictions preserved | Gap/follow-up |
|---|---|---|---|---|---|---|---|---|
| 1 | Composition correctness | `<VALUE>` | `<REFERENCE or MISSING>` | `<RESULT>` | `<YES/NO + basis>` | `<BLOCKS / DOES_NOT_BLOCK + reason>` | `<YES/NO>` | `<VALUE>` |
| 2 | Completeness | `<VALUE>` | `<REFERENCE or MISSING>` | `<RESULT>` | `<VALUE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| 3 | Usability | `<VALUE>` | `<REFERENCE or MISSING>` | `<RESULT>` | `<VALUE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| 4 | Reproducibility where applicable | `<VALUE>` | `<REFERENCE or MISSING>` | `<RESULT>` | `<VALUE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| 5 | Dependency integrity | `<VALUE>` | `<REFERENCE or MISSING>` | `<RESULT>` | `<VALUE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| 6 | Documentation | `<VALUE>` | `<REFERENCE or MISSING>` | `<RESULT>` | `<VALUE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| 7 | Consumer suitability | `<VALUE>` | `<REFERENCE or MISSING>` | `<RESULT>` | `<VALUE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| 8 | Failure behavior | `<VALUE>` | `<REFERENCE or MISSING>` | `<RESULT>` | `<VALUE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| 9 | Operational readiness | `<VALUE>` | `<REFERENCE or MISSING>` | `<RESULT>` | `<VALUE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |

## Evaluation disposition

| Field | Entry |
|---|---|
| Mandatory failures/insufficient evidence | `<LIST or NONE>` |
| PARTIAL controls and gate effect | `<LIST with blocking rationale>` |
| Overall descriptive finding | `<NO COMPOSITE SCORE; summarize evidence only>` |
| Requested Product gate | `<REFERENCE or NONE>` |
| Governance decision reference | `<governance-decision-record-template.md instance reference or NONE>` |
| Review trigger | `<DATE/EVENT/CHANGE>` |

## Validation checklist

- [ ] All nine dimensions are present and use only the approved results.
- [ ] Applicability, evidence and blocking disposition are explicit.
- [ ] A mandatory Product-level failure cannot be compensated by Asset quality or another dimension.
- [ ] PARTIAL preserves restrictions and states whether it blocks the requested gate.
- [ ] No metric, weighting or opaque composite score was invented.
- [ ] No result automatically changes lifecycle or grants approval/activation.
- [ ] Current and historical records are distinguished without overwrite.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-011` |
| Requirements / acceptance criteria | `R11`; `R11.1–R11.4` |
| Design component | `C07` |
| Design Decisions | `P004-D007`, `P004-D011` |
| Inputs | `product-composition-record-template.md`, `product-dependency-declaration-template.md`, Product-quality Design |

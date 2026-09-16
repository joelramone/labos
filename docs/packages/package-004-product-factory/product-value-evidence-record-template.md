# Product Value Evidence Record Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary structure. It makes no real value claim and creates no Product, demand evidence, lifecycle change or commercialization authority.

## Purpose and separations

Assess Product Value separately from Asset value using exactly `HYPOTHESIZED`, `EVIDENCED` or `DEMONSTRATED`. Value status does not automatically change Product lifecycle, readiness, approval, activation, sharing or commercialization.

## Record identity and value proposition

| Field | Entry |
|---|---|
| Product/Product Candidate reference | `<REQUIRED>` |
| Exact Product version | `<VALUE or NOT_APPLICABLE>` |
| Product SOT | `<REQUIRED>` |
| Value record ID/version | `<REQUIRED>` |
| Target consumer | `<REQUIRED>` |
| Problem | `<REQUIRED>` |
| Proposed value/outcome | `<REQUIRED>` |
| Target context | `<REQUIRED>` |
| Truth classification | `<CURRENT_TRUTH / HISTORICAL_TRUTH>` |
| Review timestamp | `<ISO 8601 with offset>` |
| Human reviewer | `<Founder or explicitly delegated competent human>` |
| Supersedes | `<REFERENCE or NONE>` |

## Evidence classification

| Value class | Mandatory evidence | Evidence supplied | Finding |
|---|---|---|---|
| `HYPOTHESIZED` | Identified consumer, problem and value proposition | `<REFERENCES>` | `<MEETS / DOES_NOT_MEET with rationale>` |
| `EVIDENCED` | Dated non-transactional demand evidence from target context | `<REFERENCES or MISSING>` | `<MEETS / DOES_NOT_MEET with rationale>` |
| `DEMONSTRATED` | Documented real use and attributable user outcome | `<REFERENCES or MISSING>` | `<MEETS / DOES_NOT_MEET with rationale>` |

| Field | Entry |
|---|---|
| Current Product Value classification | `<HYPOTHESIZED / EVIDENCED / DEMONSTRATED>` |
| Prior classification | `<VALUE or NONE>` |
| Upgrade/downgrade rationale | `<REQUIRED evidence-based rationale>` |
| Dated evidence references | `<REQUIRED>` |
| Limitations/uncertainties | `<REQUIRED or NONE with rationale>` |
| Asset-value references | `<REFERENCE or NONE; input evidence only>` |
| Projected Asset value rejected as DEMONSTRATED evidence | `<YES required>` |
| Governance decision reference | `<REFERENCE or NONE>` |
| Review trigger | `<DATE/EVENT/CHANGE>` |

## Validation checklist

- [ ] Classification uses exactly the three approved Product Value states.
- [ ] Consumer, problem, proposed outcome and target context are explicit.
- [ ] Each upgrade is supported by its mandatory dated evidence.
- [ ] Projected Asset value alone cannot establish `DEMONSTRATED`.
- [ ] Product Value remains separate from Asset value and Revenue.
- [ ] No lifecycle, approval, activation or commercialization implication is inferred.
- [ ] No real evidence or claim is instantiated by this template.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-013` |
| Requirements / acceptance criteria | `R13`; `R13.1–R13.4` |
| Design component | `C09` |
| Design Decisions | `P004-D007`, `P004-D011` |
| Inputs | `product-record-template.md`, Product Value Design |

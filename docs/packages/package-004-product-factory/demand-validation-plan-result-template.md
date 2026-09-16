# Demand Validation Plan and Result Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary structure. It conducts no interview, market test, external research, transaction or real-world validation and records no real demand evidence.

## Purpose and boundary

Define a falsifiable, non-transactional Product-demand plan and its later documentary result. Demand evidence is distinct from Product Value, readiness, approval, pricing, sales, transactions and Revenue.

## Identity and plan

| Field | Entry |
|---|---|
| Product/Product Candidate reference | `<REQUIRED>` |
| Exact Product version | `<VALUE or NOT_APPLICABLE>` |
| Product SOT | `<REQUIRED>` |
| Validation record ID/version | `<REQUIRED>` |
| Hypothesis | `<FALSIFIABLE statement>` |
| Target segment | `<REQUIRED>` |
| Problem and proposed Product response | `<REQUIRED>` |
| Method | `<DOCUMENTARY description; execution separately authorized>` |
| Observable signal | `<REQUIRED>` |
| Success criterion | `<REQUIRED>` |
| Failure/inconclusive criterion | `<REQUIRED>` |
| Timeframe | `<REQUIRED>` |
| Planned evidence source | `<REQUIRED>` |
| Privacy/sensitivity plan | `<REQUIRED>` |
| Responsible human | `<REQUIRED>` |
| Plan review authority/date | `<REQUIRED / ISO 8601>` |

## Result section

Completing this blank structure during W3 does not authorize collection. Populate only under separately valid authority for the underlying activity.

| Field | Entry |
|---|---|
| Activity authorization reference | `<REQUIRED before real collection / NOT_EXECUTED>` |
| Evidence date | `<ISO 8601 or NOT_EXECUTED>` |
| Context | `<VALUE or NOT_EXECUTED>` |
| Participant/source | `<REFERENCE preserving privacy or NOT_EXECUTED>` |
| Observed result | `<VALUE or NOT_EXECUTED>` |
| Criterion comparison | `<PASS / FAIL / INCONCLUSIVE / NOT_EXECUTED>` |
| Evidence references | `<REFERENCES or MISSING>` |
| Limitations/uncertainties | `<REQUIRED>` |
| Privacy/sensitivity handling | `<REQUIRED>` |
| Human review authority/date | `<REFERENCE / ISO 8601 or NOT_EXECUTED>` |
| Follow-up/review trigger | `<VALUE>` |

Failure or insufficient evidence is recorded as failed/inconclusive validation, never converted into approval. A sale, price or Revenue target may appear only as a future hypothesis; P004 does not execute or count it as Product validation.

## Validation checklist

- [ ] Hypothesis, segment, method, signal, success/failure criteria, timeframe and source are explicit.
- [ ] Result fields preserve date, context, source, limitations and privacy handling.
- [ ] Failed or inconclusive evidence cannot become approval.
- [ ] Demand result does not imply readiness, approval, activation, transaction or Revenue.
- [ ] No interview, market activity, price test, transaction or real evidence collection occurred.
- [ ] Final interpretation remains human-authoritative; AI output is non-authoritative.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-014` |
| Requirements / acceptance criteria | `R14`; `R14.1–R14.4` |
| Design component | `C10` |
| Design Decisions | `P004-D007`, `P004-D011` |
| Inputs | `product-record-template.md`, Demand Validation Design |

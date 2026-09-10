# Product Candidate Governance Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank reusable structure. Completion of this file does not register a Product Candidate, create a Product, validate demand, authorize commercialization, change an Asset, or execute a lifecycle transition.

## Purpose

Capture a domain-neutral Product Candidate proposal for governed human review while preserving its provisional and unapproved character.

## Usage and authority boundary

- A **Product Candidate** is a governed proposal, not an approved **Product**, an **Asset**, commercialization authorization, or demand validation.
- The **Candidate Owner** must be human. Final review authority is the Founder or an explicitly delegated human.
- AI output is `NON_AUTHORITATIVE` until reviewed and accepted by valid human authority. AI may read, analyze, summarize, compare, draft, recommend, detect gaps and, where authorized, propose a transition. AI may not approve, reject authoritatively, execute a transition, change ownership/authority/provenance, override attachment eligibility, or authorize commercialization.
- Package 003 owns Asset truth. Asset data is referenced only; P004 may `READ / REFERENCE / CONSUME DECISION` and may not `WRITE / OVERRIDE` it.
- Complete intake may support registration only in lifecycle state `CANDIDATE`; it produces no other governance effect.

## Required fields

Use `MISSING — <named gap>` rather than inventing information. A missing required field means the proposal is not ready for complete Candidate registration.

| Field | Entry |
|---|---|
| Candidate provisional ID | `<CANDIDATE_ID — PLACEHOLDER; do not use a real ID in this template>` |
| Candidate title/name | `<REQUIRED>` |
| Problem/opportunity | `<REQUIRED>` |
| Target consumer | `<REQUIRED>` |
| Value hypothesis | `<REQUIRED>` |
| Originating context | `<REQUIRED reference; does not transfer Lab authority>` |
| Candidate Owner | `<REQUIRED human name/reference>` |
| Product SOT (Candidate record) | `<REQUIRED single authoritative location/reference>` |
| Lifecycle state | `CANDIDATE` or `<MISSING until registered>` |
| Current evaluation/review state | `<REQUIRED; distinct from lifecycle state>` |
| Created timestamp | `<REQUIRED ISO 8601 with offset>` |
| Last updated timestamp | `<REQUIRED ISO 8601 with offset>` |

## Proposed composition

At least one coherent proposed input is required. Entries remain proposals; references do not attach Assets.

| Input reference | Input class | Exact/current version expectation | Proposed contribution | Authority/SOT reference | Eligibility/restriction reference | Status or named gap |
|---|---|---|---|---|---|---|
| `<REFERENCE>` | `<Asset / external / other governed input>` | `<VALUE>` | `<VALUE>` | `<UPSTREAM REFERENCE>` | `<REFERENCE or N/A with reason>` | `<VALUE>` |

### Asset references

| Asset ID/version reference | Package 003 SOT | Consumed P003 decision | Candidate use | Restrictions retained |
|---|---|---|---|---|
| `<REFERENCE>` | `<ASSET_SOT_REFERENCE>` | `<REFERENCE_ONLY / NOT_ATTACHABLE, NOT_ELIGIBLE, or other exact P003 decision>` | `<evaluation reference only>` | `<VALUE>` |

### External dependency references

| Dependency identity/reference | Version/compatibility | Purpose | Provider/owner | Criticality/failure impact | Restrictions | Review trigger |
|---|---|---|---|---|---|---|
| `<REFERENCE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |

## Evidence, restrictions and provenance

### Evidence references

| Evidence ID/reference | Evidence type | Source authority | Date/freshness | Relevance | Limitations/uncertainty |
|---|---|---|---|---|---|
| `<REFERENCE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |

Evidence references support evaluation only. They do not themselves establish demand validation, Product Value progression, readiness, approval, or commercialization.

### Known restrictions

| Restriction ID/source | Restriction | Owning authority | Candidate effect | Unresolved conflict/gap |
|---|---|---|---|---|
| `<REFERENCE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |

### Provenance

| Field | Entry |
|---|---|
| Proposal source/creator | `<REFERENCE>` |
| Research/Knowledge references where applicable | `<REFERENCES or explicit gap>` |
| Asset provenance references where applicable | `<P003 REFERENCES; never copied authority>` |
| Prior related Candidate/Product references | `<REFERENCES or NONE>` |
| AI assistance used | `<NO / YES — operation, source references, uncertainty, human reviewer>` |
| Provenance gaps | `<NONE or named gaps; never fabricate links>` |

## Review readiness

| Control | Result | Evidence/reference or named gap |
|---|---|---|
| Required identity fields complete | `<YES / NO>` | `<VALUE>` |
| Human Candidate Owner confirmed | `<YES / NO>` | `<VALUE>` |
| Exactly one Product SOT for the Candidate record identified | `<YES / NO / CONFLICT>` | `<VALUE>` |
| Proposed composition coherent | `<YES / NO / REVIEW_REQUIRED>` | `<VALUE>` |
| Evidence inventory present | `<YES / NO>` | `<VALUE>` |
| Restrictions visible | `<YES / NO>` | `<VALUE>` |
| Provenance gaps explicit | `<YES / NO>` | `<VALUE>` |
| Next review date or event trigger | `<REQUIRED>` | `<VALUE>` |
| Readiness for review | `<READY_FOR_REVIEW / NOT_READY_FOR_REVIEW>` | `<Human assessment; not lifecycle readiness>` |

## Governed review

The authoritative decision is recorded in a referenced **decision record** using `governance-decision-record-template.md`; this section is a usable index, not a substitute decision.

| Field | Entry |
|---|---|
| Review request/action | `<VALUE>` |
| Review authority | `<Founder or explicitly delegated human>` |
| Delegated-authority reference | `<REFERENCE or NOT_APPLICABLE>` |
| Decision record reference | `<REQUIRED for an authoritative outcome>` |
| Review outcome | `<PENDING / RETURNED_FOR_REVIEW / ACCEPTED_FOR_GOVERNED_CONTINUATION / REJECTED>` |
| Outcome timestamp | `<ISO 8601 with offset>` |
| Reason | `<VALUE>` |
| Resulting lifecycle state | `<UNCHANGED or exact authorized state; never automatic>` |
| Follow-up | `<VALUE>` |

### Terminal `REJECTED` outcome

`REJECTED` is a terminal Candidate review outcome, not a Product lifecycle state. When selected, preserve the Candidate identity, evidence references, human decision authority/delegation, timestamp, reason and historical decision-record reference. The Candidate remains historically recorded in `UNDER_REVIEW` with no forward transition. There is no re-entry field or mechanism here; a renewed proposal requires a new Candidate identity linked to the rejected record.

## Supporting notes (optional)

`<NOTES — must not override authoritative fields or decisions>`

## Validation checklist

- [ ] Banner still reads `TEMPLATE — NOT_A_GOVERNED_INSTANCE`; no real Candidate ID or domain content is populated.
- [ ] Every required field is completed or individually marked `MISSING`.
- [ ] Candidate Owner is human; review authority is Founder or an explicitly delegated human.
- [ ] Candidate, Product and Asset meanings remain distinct; no Product/market/commercial claim is made.
- [ ] One Product SOT for the Candidate record is identifiable; Asset SOT and evidence references remain separate.
- [ ] Asset references reproduce no Asset truth and grant no attachment eligibility.
- [ ] Review/evaluation state is not treated as lifecycle state.
- [ ] `REJECTED` is a terminal historical outcome with no silent re-entry.
- [ ] AI assistance, if any, is labelled `NON_AUTHORITATIVE` with sources and uncertainty.
- [ ] At least one next review date or evidence-based trigger is recorded.

## Traceability and related references

| Trace type | Approved source |
|---|---|
| Task | `T004-002` |
| Requirements / acceptance criteria | `P004-R02`; `R02.1–R02.4`; `R07.1`; `R08.1`; `R23.1` |
| Design components | `C01` |
| Design Decisions | `P004-D002`, `P004-D010` |
| Upstream | `requirements.md`, `design.md`, `product-concept-model.md`, `product-registry-design.md`, `product-governance-design.md`, `product-lifecycle-design.md` |
| Downstream | T004-010 provenance, T004-017 terminal outcome, T004-020 Registry, T004-028 controlled fixtures (all later-wave authority required) |

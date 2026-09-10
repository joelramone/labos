# Governed Product Aggregate Record Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank reusable structure. It creates no Product, approval, activation, Asset attachment, sharing permission, commercialization authority, or revenue operation.

## Purpose

Represent one stable **Product** identity and one governed Product version as a domain-neutral, manually operable Product aggregate record.

## Usage and authority boundary

- A Product is distinct from Idea, Research, Knowledge, Asset, Product Candidate, Revenue, Capability and Lab. Use references to upstream/downstream entities; do not redefine or absorb their authority.
- Each governed Product version has exactly one human **Product Owner**, exactly one lifecycle state and exactly one authoritative **Product SOT**.
- Package 003 owns Asset truth. Asset identity, lifecycle, ownership, provenance, SOT, restrictions, version and attachment eligibility are referenced, never copied or overridden.
- Final governance authority is the Founder or an explicitly delegated human. AI-generated content is `NON_AUTHORITATIVE` until human review/acceptance and cannot change state, authority, ownership, provenance, eligibility or commercialization status.
- This record indexes governance decisions. Authoritative decisions use `governance-decision-record-template.md` and remain immutable historical references.

## Product identity — required

Use `MISSING — <named gap>` when information is absent. Duplicate identity claims must be flagged before approval.

| Field | Entry |
|---|---|
| Product ID | `<PRODUCT_ID — PLACEHOLDER; do not use a real ID in this template>` |
| Product name/title | `<REQUIRED>` |
| Purpose | `<REQUIRED>` |
| Target consumer | `<REQUIRED>` |
| Problem | `<REQUIRED>` |
| Value proposition | `<REQUIRED>` |
| Originating context | `<REQUIRED reference; does not transfer Lab authority>` |
| Product version | `<REQUIRED MAJOR.MINOR.PATCH>` |
| Product Owner | `<REQUIRED human name/reference>` |
| Lifecycle state | `<CANDIDATE / UNDER_REVIEW / READY / APPROVED / ACTIVE / DEPRECATED / RETIRED>` |
| Authoritative Product SOT | `<REQUIRED single authoritative location/reference for this Product version>` |
| Identity duplicate check | `<CLEAR / CONFLICT — references>` |
| Effective timestamp | `<REQUIRED ISO 8601 with offset>` |
| Created timestamp | `<REQUIRED ISO 8601 with offset>` |
| Last updated timestamp | `<REQUIRED ISO 8601 with offset>` |

### Lifecycle integrity

The exact and complete lifecycle is `CANDIDATE`, `UNDER_REVIEW`, `READY`, `APPROVED`, `ACTIVE`, `DEPRECATED`, `RETIRED`. No eighth state is permitted; `REJECTED` is a terminal Candidate review outcome, never a Product lifecycle state.

`READY ≠ APPROVED`; `APPROVED ≠ ACTIVE`; `ACTIVE ≠ PUBLIC`; `ACTIVE ≠ COMMERCIALIZED`; `ACTIVE ≠ REVENUE_GENERATING`. Lifecycle is independent of sharing scope. State changes require a separate valid human governance decision and never follow automatically from record completeness, review flags, Product Value, demand evidence or AI output.

## Candidate origin and provenance

| Field | Entry |
|---|---|
| Originating Product Candidate reference | `<REQUIRED where applicable; absent link must be an explicit gap>` |
| Candidate decision reference | `<REFERENCE>` |
| Research/Knowledge/evidence lineage references | `<REFERENCES or explicit gaps>` |
| Composition provenance root | `<REFERENCE>` |
| Missing-link/gap decisions | `<REFERENCES; never fabricate provenance>` |
| AI assistance used | `<NO / YES — operation, sources, uncertainty, human reviewer>` |

## Product composition

This is a summary/index only. Detailed composition is governed by later authorized artifacts. At least one governed input is required; Products need not contain an Asset or be software.

| Composition snapshot reference | Input identity/version | Input class | Contribution | Authority/SOT reference | Eligibility/fit decision reference | Restrictions |
|---|---|---|---|---|---|---|
| `<REFERENCE>` | `<VALUE>` | `<Asset / external / other governed input>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |

### Asset references

| Asset ID/version | Asset SOT reference | P003 eligibility decision reference | Attachment status | Asset restrictions/provenance references |
|---|---|---|---|---|
| `<REFERENCE>` | `<ASSET_SOT_REFERENCE>` | `<P003 DECISION REFERENCE>` | `<REFERENCE_ONLY / NOT_ATTACHABLE / ELIGIBLE decision as supplied by P003>` | `<REFERENCES>` |

The **Product SOT** governs Product truth only. Each **Asset SOT** remains under Package 003. Product SOT ≠ Asset SOT; Product Value ≠ Asset value.

## Dependencies

| Dependency reference | Class | Version/compatibility | Purpose | Owner/provider | Criticality/failure impact | Restrictions | Fallback/exit | Review trigger |
|---|---|---|---|---|---|---|---|---|
| `<REFERENCE>` | `<Asset / external / operational / future-platform>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` |

No database, automation, Persistence, Historical Truth implementation, RAG, MCP, AI Agent Runtime or other future platform may be assumed as an implicit dependency.

## Evidence and governance references

### Quality and risk

| Evidence class | Current reference | Status/result | Human review reference | Restrictions/gaps |
|---|---|---|---|---|
| Product Quality | `<REFERENCE>` | `<VALUE>` | `<REFERENCE>` | `<VALUE>` |
| Product Risk | `<REFERENCE>` | `<VALUE>` | `<REFERENCE>` | `<VALUE>` |

Product Quality is evaluated independently from Asset quality. Product risk preserves or elevates applicable upstream risks until competently resolved; Product status is not assurance beyond evidence.

### Product Value

| Field | Entry |
|---|---|
| Product Value state | `<HYPOTHESIZED / EVIDENCED / DEMONSTRATED>` |
| Evidence record reference | `<REFERENCE>` |
| Target consumer/problem/outcome linkage | `<REFERENCE or named gap>` |
| Governed review/decision reference | `<REFERENCE>` |
| Effective timestamp | `<ISO 8601 with offset>` |

No automatic progression exists. Any Product Value change requires the evidence approved for that class and governed human review. Product Value does not automatically change lifecycle or authorize commercialization.

### Demand evidence

| Demand plan/result reference | Status/result | Evidence date/context | Limitations | Human review reference |
|---|---|---|---|---|
| `<REFERENCE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<REFERENCE>` |

Demand evidence is not transaction or Revenue validation and causes no automatic approval.

### Readiness and governance decisions

| Reference type | Decision/evidence record reference | Current result | Authority | Timestamp | Scope/restrictions |
|---|---|---|---|---|---|
| Readiness | `<REFERENCE>` | `<READY / NOT_READY / REVIEW_REQUIRED / MISSING>` | `<HUMAN>` | `<VALUE>` | `<VALUE>` |
| Approval | `<REFERENCE or NOT_APPLICABLE>` | `<VALUE>` | `<Founder/delegated human>` | `<VALUE>` | `<VALUE>` |
| Activation | `<REFERENCE or NOT_APPLICABLE>` | `<VALUE>` | `<Founder/delegated human>` | `<VALUE>` | `<delivery/operating scope>` |
| Other governance decisions | `<REFERENCES>` | `<VALUE>` | `<HUMAN>` | `<VALUE>` | `<VALUE>` |

## Sharing scope and restrictions

| Field | Entry |
|---|---|
| Current sharing scope | `<NONE / INTERNAL / LIMITED / EXTERNAL / PUBLIC or governed vocabulary reference>` |
| Sharing decision reference | `<REFERENCE; required for requested context>` |
| Applicable Product restrictions | `<REFERENCES>` |
| Applicable Asset/external restrictions | `<UPSTREAM REFERENCES>` |
| Effective most-restrictive scope | `<VALUE>` |
| Commercialization authorization | `<NONE unless separately governed outside this template>` |

Sharing scope is orthogonal to lifecycle and cannot broaden upstream licensing, sensitivity or distribution rights.

## Product source-of-truth classification

| Source/copy reference | Classification | Authority | Current/historical | Notes |
|---|---|---|---|---|
| `<AUTHORITATIVE REFERENCE>` | `AUTHORITATIVE PRODUCT SOT` | `<HUMAN authority>` | `<CURRENT>` | `<VALUE>` |
| `<REFERENCE>` | `<Asset SOT / evidence source / working copy / managed mirror / derived representation / unmanaged copy>` | `<OWNING AUTHORITY or NONE>` | `<VALUE>` | `<VALUE>` |

Only one entry may claim `AUTHORITATIVE PRODUCT SOT` for this Product version. Asset SOT and evidence sources are authoritative only in their own scope. Working copies, managed mirrors, derived representations and unmanaged copies do not become Product authority.

## Review, freshness and history

| Field | Entry |
|---|---|
| Next review date | `<DATE or NOT_SET with named gap>` |
| Evidence-based event triggers | `<1..N references/descriptions>` |
| Review-required flag | `<YES / NO>` |
| Review/freshness record references | `<REFERENCES>` |
| Prior Product version / supersedes | `<REFERENCE or NONE>` |
| Superseded-by reference | `<REFERENCE or NONE>` |
| Deprecation decision reference | `<REFERENCE or NOT_APPLICABLE>` |
| Retirement decision reference | `<REFERENCE or NOT_APPLICABLE>` |
| Successor/migration/exit reference | `<REFERENCE or NOT_APPLICABLE>` |

A fired review trigger preserves the current lifecycle state unless a separate governed transition is approved. Historical decisions and prior states are not overwritten.

## Optional supporting notes

`<NOTES — must not override authoritative fields, source decisions or history>`

## Validation checklist

- [ ] Banner remains `TEMPLATE — NOT_A_GOVERNED_INSTANCE`; no real Product ID/content is populated.
- [ ] Every P004-R01 identity element is present or individually marked `MISSING`.
- [ ] Duplicate identity check is clear; Product Owner is human.
- [ ] Lifecycle contains exactly seven permitted states and no use of `REJECTED` as a state.
- [ ] `READY`, `APPROVED`, `ACTIVE`, sharing, commercialization and Revenue meanings remain separate.
- [ ] Product Value uses exactly `HYPOTHESIZED / EVIDENCED / DEMONSTRATED` with evidence and governed review.
- [ ] Exactly one `AUTHORITATIVE PRODUCT SOT` resolves for the Product version.
- [ ] Product SOT, Asset SOT, evidence source and copy classifications are distinct.
- [ ] Asset truth/eligibility is referenced from P003 without write, duplication or override.
- [ ] Governance decisions are referenced rather than redundantly recreated.
- [ ] Provenance gaps, restrictions, dependencies and freshness triggers are explicit.
- [ ] AI assistance is optional, sourced, uncertain where appropriate and `NON_AUTHORITATIVE`.

## Traceability and related references

| Trace type | Approved source |
|---|---|
| Task | `T004-003` |
| Requirements / acceptance criteria | `P004-R01`; `R01.1–R01.4`; `R07.1`, `R07.3`; `R25.1` |
| Design components | `C02` |
| Design Decisions | `P004-D001`, `P004-D002`, `P004-D010` |
| Upstream | `requirements.md`, `design.md`, `product-concept-model.md`, `product-registry-design.md`, `product-governance-design.md`, Package 003 authority by reference |
| Downstream | T004-005–010, T004-018–024 (later-wave authority required) |


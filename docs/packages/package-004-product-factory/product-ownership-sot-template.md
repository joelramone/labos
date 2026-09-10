# Product Ownership and Source of Truth Declaration Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank reusable structure. It performs no ownership transfer, creates no Product, selects no storage technology and establishes no actual source of truth.

## Purpose

Provide reusable, compact declarations for **Product ownership** and the **Product Source of Truth** without duplicating the full Product aggregate record.

## Usage and authority boundary

- Reference the governed Product record and applicable **decision record**; do not reproduce its full identity, composition, lifecycle or evidence packet.
- The **Product Owner** must be human. AI/software ownership is prohibited.
- Final governance authority is the Founder or an explicitly delegated human. AI-generated content is `NON_AUTHORITATIVE` until reviewed and accepted by valid human authority.
- AI may read, analyze, summarize, compare, draft, recommend, detect gaps and, where authorized, propose a transition. AI may not transfer ownership, execute transitions, approve, change authority/provenance, override attachment eligibility or authorize commercialization.
- Package 003 owns Asset truth. Product ownership never transfers Asset ownership. Product SOT references Asset SOTs and may not duplicate, replace or override them.
- Exactly one current `AUTHORITATIVE PRODUCT SOT` must resolve for each governed Product version. A conflict fails closed pending human reconciliation.

## A. Product Ownership Declaration

### Required fields

| Field | Entry |
|---|---|
| Declaration status | `<DRAFT_NON_AUTHORITATIVE / CURRENT_AUTHORITATIVE / SUPERSEDED>` |
| Product ID/reference | `<PRODUCT REFERENCE — PLACEHOLDER; no real ID in this template>` |
| Product version | `<MAJOR.MINOR.PATCH or governed reference>` |
| Product record/SOT reference | `<REFERENCE>` |
| Product Owner | `<REQUIRED human name/reference>` |
| Ownership effective date | `<REQUIRED ISO 8601 date/time with offset>` |
| Ownership authority | `<Founder or explicitly delegated human>` |
| Delegated-authority reference | `<REFERENCE or NOT_APPLICABLE>` |
| Owner acceptance reference | `<REQUIRED for new/transfer declaration>` |
| Governance decision reference | `<REQUIRED decision record reference>` |
| Evidence/reference basis | `<REFERENCES>` |
| Review trigger/date | `<REQUIRED date or evidence-based event>` |
| Declaration timestamp | `<REQUIRED ISO 8601 with offset>` |
| Provenance / AI assistance | `<SOURCE REFERENCES; AI operation/uncertainty/human reviewer if used>` |

### Responsibilities

| Responsibility | Owner acknowledgement/reference |
|---|---|
| Maintain Product identity/version record and Product SOT reference | `<VALUE>` |
| Maintain declared composition/dependencies and trigger impact review | `<VALUE>` |
| Preserve restrictions, provenance and governance history | `<VALUE>` |
| Keep evidence/review triggers visible and escalate gaps | `<VALUE>` |
| Operate only within governed authority; no Asset-authority override | `<VALUE>` |

### Transfer or supersession (complete only when applicable)

| Field | Entry |
|---|---|
| Outgoing Product Owner | `<HUMAN REFERENCE>` |
| Incoming Product Owner | `<HUMAN REFERENCE>` |
| Incoming-owner acceptance | `<REFERENCE>` |
| Affected Product ID/version | `<REFERENCE>` |
| Transfer/supersession decision | `<DECISION RECORD REFERENCE>` |
| Effective date | `<ISO 8601 with offset>` |
| Prior declaration preserved at | `<REFERENCE>` |
| Asset ownership effect | `NONE` |

## B. Product Source of Truth Declaration

### Required fields

| Field | Entry |
|---|---|
| Declaration status | `<DRAFT_NON_AUTHORITATIVE / CURRENT_AUTHORITATIVE / HISTORICAL / SUPERSEDED>` |
| Product ID | `<PRODUCT REFERENCE — PLACEHOLDER; no real ID in this template>` |
| Product version | `<REQUIRED MAJOR.MINOR.PATCH>` |
| Authoritative location/reference | `<REQUIRED technology-neutral reference>` |
| Classification | `AUTHORITATIVE PRODUCT SOT` |
| SOT authority | `<Founder or explicitly delegated human>` |
| Delegated-authority reference | `<REFERENCE or NOT_APPLICABLE>` |
| Effective date | `<REQUIRED ISO 8601 date/time with offset>` |
| Governance decision reference | `<REQUIRED>` |
| Supersedes Product SOT declaration | `<REFERENCE or NONE>` |
| Superseded by | `<REFERENCE or NONE>` |
| Review trigger/date | `<REQUIRED date or evidence-based event>` |
| Provenance / AI assistance | `<SOURCE REFERENCES; AI operation/uncertainty/human reviewer if used>` |

No repository, database, cloud, filesystem, document platform or other persistence technology is selected by this declaration.

### Source and copy classification index

| Reference | Classification | Owning authority | Permitted use | Current/historical status | Conflict/gap |
|---|---|---|---|---|---|
| `<REFERENCE>` | `AUTHORITATIVE PRODUCT SOT` | `<HUMAN PRODUCT AUTHORITY>` | Product truth for exact version | `<CURRENT / HISTORICAL>` | `<NONE>` |
| `<REFERENCE>` | `WORKING COPY` | `NONE` | Draft/edit support only | `<CURRENT / STALE>` | `<VALUE>` |
| `<REFERENCE>` | `MANAGED MIRROR` | `NONE` | Controlled replica; not competing authority | `<CURRENT / STALE>` | `<VALUE>` |
| `<REFERENCE>` | `DERIVED REPRESENTATION` | `NONE` | View/export only | `<CURRENT / STALE>` | `<VALUE>` |
| `<REFERENCE>` | `UNMANAGED COPY` | `NONE` | Non-authoritative reference only | `<CURRENT / STALE / UNKNOWN>` | `<VALUE>` |
| `<REFERENCE>` | `EVIDENCE SOURCE` | `<EVIDENCE SOURCE AUTHORITY>` | Supports a claim/decision in its scope | `<CURRENT / HISTORICAL>` | `<VALUE>` |
| `<REFERENCE>` | `ASSET SOT` | `Package 003 / Asset authority` | Referenced Asset truth only | `<CURRENT / HISTORICAL>` | `<VALUE>` |

### Asset SOT references

| Asset ID/version reference | Asset SOT reference | P003 authority/decision reference | Product use | Restriction/provenance references |
|---|---|---|---|---|
| `<REFERENCE>` | `<ASSET_SOT_REFERENCE>` | `<P003 REFERENCE>` | `<REFERENCE ONLY / governed composition reference>` | `<REFERENCES>` |

P003→P004 access is `READ / REFERENCE / CONSUME DECISION`; `WRITE / OVERRIDE` is prohibited. Asset SOT authority never migrates into this Product declaration.

### SOT conflict and supersession control

| Check | Result | Evidence/action |
|---|---|---|
| Exactly one current Product SOT claim for this Product/version | `<PASS / FAIL>` | `<REFERENCE or named conflict>` |
| Product SOT distinct from every Asset SOT | `<PASS / FAIL>` | `<VALUE>` |
| Evidence sources and copies classified as non-Product authority | `<PASS / FAIL>` | `<VALUE>` |
| Prior declaration preserved when superseded | `<PASS / FAIL / N/A>` | `<REFERENCE>` |
| Current and historical status distinguishable | `<PASS / FAIL>` | `<VALUE>` |

Any `FAIL` blocks approval or continued reliance pending a referenced human reconciliation decision. No location gains authority by being newer, easier to access or AI-generated.

## Validation checklist

- [ ] Banner remains `TEMPLATE — NOT_A_GOVERNED_INSTANCE`; no real Product ID, owner or SOT is declared.
- [ ] Product reference/version resolves without copying the full Product aggregate.
- [ ] Product Owner and final authority are human; AI/software ownership or final authority is absent.
- [ ] Owner responsibilities, effective date, acceptance, evidence and review trigger are recorded.
- [ ] A transfer preserves outgoing/incoming owners, acceptance, identity, date and prior declaration.
- [ ] Product ownership has no effect on Asset ownership.
- [ ] Exactly one current `AUTHORITATIVE PRODUCT SOT` resolves for the Product version.
- [ ] Asset SOT, evidence sources, working copies, managed mirrors, derived representations and unmanaged copies remain distinct.
- [ ] P003 Asset authority is referenced only and cannot be written or overridden.
- [ ] Supersession preserves current/historical status; conflicts fail closed.
- [ ] No storage or persistence technology is prescribed.

## Traceability and related references

| Trace type | Approved source |
|---|---|
| Task | `T004-005` |
| Requirements / acceptance criteria | `P004-R07–R08`; `R07.1–R08.4` |
| Design components | `C02`, `C19` |
| Design Decisions | `P004-D001`, `P004-D008`, `P004-D010` |
| Dependencies satisfied | `T004-003 COMPLETE`, `T004-004 COMPLETE` before this artifact was created |
| Upstream | `product-record-template.md`, `governance-decision-record-template.md`, `requirements.md`, `design.md`, `product-registry-design.md`, Package 003 authority by reference |
| Downstream | T004-010 provenance and T004-020 Registry (later-wave authority required) |


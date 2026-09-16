# Product Packaging Manifest Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank technology-neutral structure. It creates no Product, package instance, approval, activation, publication, commercialization or Revenue action.

## Purpose and boundary

Describe the governed inputs and supporting material presented or delivered together for an exact Product version without prescribing a ZIP, container, image, repository, build system, package manager, deployment system or other implementation.

`PACKAGED ≠ APPROVED`  
`PACKAGED ≠ ACTIVE`  
`PACKAGED ≠ PUBLIC`  
`PACKAGED ≠ COMMERCIALIZED`  
`PACKAGED ≠ REVENUE_GENERATING`

Packaging remains inside Product Factory and does not activate Package 005.

## Manifest identity

| Field | Entry |
|---|---|
| Product ID/reference | `<REQUIRED>` |
| Product version | `<REQUIRED exact version>` |
| Product SOT | `<REQUIRED>` |
| Manifest ID/version | `<REQUIRED>` |
| Composition reference/version | `<REQUIRED>` |
| Packaging purpose | `<REQUIRED>` |
| Truth classification | `<CURRENT_TRUTH / HISTORICAL_TRUTH>` |
| Effective timestamp | `<ISO 8601 with offset>` |
| Owner | `<REQUIRED human Product Owner reference>` |
| Governance references | `<REQUIRED references>` |
| Supersedes | `<REFERENCE or NONE>` |

## Included governed inputs

| Input ID/reference | Input class | Exact version | Source authority/SOT | Inclusion purpose | Eligibility/fit reference where applicable | Provenance | Restrictions/licensing/sharing limitations | Integrity/evidence reference | Compatibility note |
|---|---|---|---|---|---|---|---|---|---|
| `<VALUE>` | `<Asset / external / operational / platform / other governed input>` | `<VALUE>` | `<REFERENCE>` | `<VALUE>` | `<REFERENCE / NOT_APPLICABLE>` | `<REFERENCE or named gap>` | `<REFERENCES or NONE with rationale>` | `<REFERENCE or named gap>` | `<VALUE>` |

## Supporting material and delivery assumptions

| Supporting material/reference | Exact version | Purpose | Source authority | Consumer/delivery assumption | Restrictions | Missing/gap disposition |
|---|---|---|---|---|---|---|
| `<VALUE>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<NONE or named gap>` |

Missing items, incompatible versions, incomplete eligibility or unresolved restrictions remain explicit and fail closed for packaging/readiness review. Packaging cannot broaden licensing, usage, sharing, distribution, dependency or risk permissions.

## Validation checklist

- [ ] Banner remains `TEMPLATE — NOT_A_GOVERNED_INSTANCE`; no real packaged instance exists.
- [ ] Exact Product, composition, input, Asset and dependency versions are cited.
- [ ] Asset inclusion references authoritative P003 eligibility and does not imply attachment.
- [ ] Supporting material, provenance, compatibility and integrity/evidence are present or gaps are named.
- [ ] Licensing, sharing and all upstream restrictions remain visible at delivery.
- [ ] Technology neutrality is preserved; no packaging/build/deployment mechanism is prescribed.
- [ ] All five `PACKAGED ≠` boundaries remain explicit.
- [ ] Package 005 remains dormant and commercialization/Revenue implications are none.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-009` |
| Requirements / acceptance criteria | `R17`; `R17.1–R17.4`; `R22.4` |
| Design component | `C14` |
| Design Decisions | `P004-D006`, `P004-D012` |
| Upstream | `product-record-template.md`, `product-composition-record-template.md`, `p003-attachment-eligibility-reference-contract.md`, `product-dependency-declaration-template.md` |

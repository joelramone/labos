# Product Version and Compatibility Record Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary structure. It creates no Product/version, version transition, compatibility decision, test result, lifecycle effect, or Asset change.

## Version authority boundary

Task: `T004-019`. Product version, Asset version, dependency version, composition version, packaging manifest version and governance record version are distinct authorities. A Product record references upstream versions; it never rewrites Asset or dependency truth. Compatibility is evidence/reference based, never automatically inferred or claimed as runtime-tested.

## Product version identity

| Field | Entry |
|---|---|
| Product ID / SOT reference | `<REQUIRED REFERENCE>` |
| Product version | `<MAJOR.MINOR.PATCH>` |
| Version record version | `<RECORD VERSION>` |
| Classification | `<MAJOR / MINOR / PATCH>` |
| Classification rationale | `<REQUIRED>` |
| Fundamentally different offering check | `<NO / YES — YES requires new Product identity>` |
| Predecessor / supersedes | `<REFERENCE or NONE>` |
| Successor / superseded by | `<REFERENCE or NONE>` |
| Composition reference and version | `<REFERENCE>` |
| Packaging manifest reference/version | `<REFERENCE or NOT_APPLICABLE>` |
| Effective date | `<ISO 8601>` |
| Owner | `<HUMAN OWNER REFERENCE>` |
| Provenance | `<REFERENCES>` |
| Human review / authority | `<REVIEWER, BASIS, DECISION REFERENCE>` |
| Restrictions | `<REFERENCES or NONE with rationale>` |
| Review trigger | `<DATE/EVENT/CHANGE>` |
| Historical linkage | `<PRIOR/SUCCESSOR/HISTORY REFERENCES>` |

## Inputs and dependency versions

| Input/dependency reference | Authority type | Referenced version/constraint | Asset eligibility decision, if applicable | Source of truth | Restrictions | Evidence/currentness | Change review required |
|---|---|---|---|---|---|---|---|
| `<REFERENCE>` | `<Asset / external / operational / platform>` | `<VERSION / CONSTRAINT>` | `<P003 DECISION REFERENCE / N/A>` | `<AUTHORITATIVE REFERENCE>` | `<REFERENCE>` | `<REFERENCE / NAMED GAP>` | `<YES / NO with rationale>` |

## Compatibility record

| Field | Entry |
|---|---|
| Compatibility statement | `<SUPPORTED / NOT_SUPPORTED / CONDITIONAL / UNKNOWN>` |
| Evidence references | `<REQUIRED references; UNKNOWN if absent>` |
| Compatibility constraints | `<VERSIONS, CONTEXTS, CONDITIONS or NONE>` |
| Known incompatibilities | `<REFERENCES / NONE EVIDENCED / UNKNOWN>` |
| Migration/transition notes | `<REFERENCE / NOT_APPLICABLE>` |
| Runtime compatibility tested | `<NO unless separately evidenced; REFERENCE if evidenced>` |
| Reviewer and human decision | `<HUMAN / DECISION REFERENCE>` |
| Decision effective date | `<ISO 8601>` |
| Supersedes compatibility record | `<REFERENCE or NONE>` |

Material Product, Asset, dependency, composition, schema, restriction, source-access or context change creates a review requirement; it never automatically changes Product version, Asset version, compatibility, readiness or lifecycle. Product classification follows Requirements-defined MAJOR/MINOR/PATCH semantics and records rationale. A fundamentally different offering receives a new Product identity.

## Validation checklist

- [ ] All version authorities are separately labelled and source-referenced.
- [ ] Product version does not copy, rewrite or become authority for Asset/dependency versions.
- [ ] Compatibility has evidence or is explicitly `UNKNOWN`; no runtime claim lacks evidence.
- [ ] MAJOR/MINOR/PATCH classification and rationale are present; fundamentally different offering routes to a new identity.
- [ ] Predecessor, successor, supersession and history remain bidirectionally traceable.
- [ ] Restrictions and P003 attachment eligibility remain source-authoritative and fail closed.
- [ ] Human review is explicit; AI/software did not infer compatibility or execute a version/lifecycle change.
- [ ] Record remains domain- and technology-neutral and contains no real instance.

## Traceability

| Trace type | Approved mapping |
|---|---|
| Task | `T004-019` |
| Requirements / acceptance criteria | `R10`; `R10.1–R10.4`; `R23.1–R23.3` |
| Design component | `C13` |
| Design Decisions | `P004-D001`, `P004-D004`, `P004-D006` |
| Authoritative inputs | `product-registry-design.md`, `product-record-template.md`, `product-composition-record-template.md`, `product-dependency-declaration-template.md` |

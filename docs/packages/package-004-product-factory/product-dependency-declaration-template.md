# Product Dependency Declaration Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary structure. It creates no dependency instance, Product, attachment, implementation or technology selection.

## Purpose and authority boundary

Declare Product dependencies without collapsing their authority models. Asset dependencies remain governed by P003. External, operational and platform dependencies retain their own source authority. P004 records Product-level reliance and impact only.

## Product and declaration identity

| Field | Entry |
|---|---|
| Product ID/reference | `<REQUIRED>` |
| Product version | `<REQUIRED>` |
| Product SOT | `<REQUIRED>` |
| Composition reference/version | `<REQUIRED>` |
| Declaration ID/version | `<REQUIRED>` |
| Truth classification | `<CURRENT_TRUTH / HISTORICAL_TRUTH>` |
| Effective timestamp | `<ISO 8601 with offset>` |
| Responsible human | `<Founder or explicitly delegated competent human>` |
| Supersedes | `<REFERENCE or NONE>` |

## Dependency register

Use one row per dependency. Required/optional status must reflect an approved source or be recorded descriptively as unresolved; this template does not create a new lifecycle-like enum.

| Dependency ID/reference | Type | Source | Source authority | Exact version/reference | Purpose | Required/optional basis | Restrictions/licensing | Provenance | Compatibility constraints | Availability assumption | Failure behavior | Absence impact | Review trigger | Responsible human | Supersession |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `<VALUE>` | `<Asset / external / operational / platform>` | `<REFERENCE>` | `<AUTHORITATIVE SOURCE>` | `<VALUE>` | `<VALUE>` | `<APPROVED BASIS or descriptive uncertainty>` | `<REFERENCES>` | `<REFERENCE or named gap>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<DATE/EVENT/CHANGE>` | `<REFERENCE>` | `<REFERENCE or NONE>` |

## Class-specific authority checks

| Class | Authority rule |
|---|---|
| Asset | P003 Asset SOT, lifecycle, eligibility, handoff and restrictions remain authoritative; P004 cannot recompute or override them. |
| External | The identified external source/provider retains source truth and applicable rights/restrictions. |
| Operational | The competent operational authority owns operating assumptions and failure response; declaration does not implement operations. |
| Platform | The identified platform authority owns platform truth; declaration selects no platform or technology. |

Failure behavior, fallback/exit considerations and absence impact are descriptive fields. They do not define new normative states or execute automated behavior.

## Validation checklist

- [ ] All four approved classes can be represented separately.
- [ ] Identity, authority, version, purpose, restrictions, provenance and compatibility are explicit.
- [ ] Availability, failure behavior and absence impact are inspectable.
- [ ] Asset authority remains with P003; other sources retain their respective authority.
- [ ] Undeclared or materially changed dependencies trigger human review.
- [ ] Current/historical/superseded records preserve prior evidence.
- [ ] No RAG, MCP, agent, Persistence, platform or automation dependency is implied.
- [ ] No real dependency or Product instance exists in this template.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-008` |
| Requirements / acceptance criteria | `R18`; `R18.1–R18.4`; `R23.1–R23.3` |
| Design component | `C11` |
| Design Decisions | `P004-D006`, `P004-D010` |
| Upstream | `product-record-template.md`, `product-composition-record-template.md`, approved dependency Design |

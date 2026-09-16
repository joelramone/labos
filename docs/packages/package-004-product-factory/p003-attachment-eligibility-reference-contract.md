# P003 Attachment-Eligibility Reference Contract

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Read-only P004 consumption contract. It records no real eligibility decision, attachment, Asset mutation or lifecycle transition.

## Purpose and authority

Package 003 remains authoritative for Asset truth. Package 004 may consume an authoritative P003 decision to determine whether a proposed Product composition may proceed, but P004 may reject Product fit and can never grant, recompute or override Asset eligibility. Product approval cannot override Asset eligibility.

## Exact eligibility mapping

| Authoritative P003 Asset state and handoff | P004 consumption result |
|---|---|
| `CANDIDATE` or `UNDER_REVIEW` | `NOT_COMPOSABLE` |
| `VALIDATED / NOT_CANONICAL` | `REFERENCE_ONLY / NOT_ATTACHABLE` |
| `CANONICAL` with incomplete P003 handoff | `NOT_ELIGIBLE` |
| `CANONICAL` with complete P003 handoff | `ELIGIBLE_FOR_GOVERNED_ATTACHMENT` |

No alternative eligibility state is introduced here. `ELIGIBLE_FOR_GOVERNED_ATTACHMENT` permits only a later governed attachment decision; it is not an attachment, Product approval or lifecycle transition.

## Operation boundary

| Permitted | Prohibited |
|---|---|
| `READ` | `WRITE` |
| `REFERENCE` | `OVERRIDE` |
| `CONSUME DECISION` | `RECOMPUTE` |
|  | `PROMOTE` |
|  | `DOWNGRADE` |
|  | `ALTER_HANDOFF` |
|  | `ALTER_ASSET_AUTHORITY` |

## Blank consumption record

| Field | Entry |
|---|---|
| Product composition reference | `<REQUIRED>` |
| Intended Product use | `<REQUIRED>` |
| Asset ID and exact version/reference | `<REQUIRED>` |
| Authoritative Asset SOT | `<REQUIRED P003 reference>` |
| Asset lifecycle/state evidence | `<REQUIRED P003 reference>` |
| Authoritative eligibility decision | `<REQUIRED P003 reference>` |
| Decision authority and timestamp | `<REQUIRED P003 authority / ISO 8601>` |
| Handoff completeness reference | `<REQUIRED>` |
| Eligibility outcome consumed | `<EXACT OUTCOME FROM TABLE ABOVE>` |
| Licensing restrictions | `<REFERENCE/value>` |
| Usage/sharing/distribution restrictions | `<REFERENCE/value>` |
| Dependency/risk restrictions | `<REFERENCE/value>` |
| P004 fit finding | `<FIT / NOT_FIT / REVIEW_REQUIRED; Product-level only>` |
| Immutable consumption-result reference | `<REFERENCE>` |
| Human reviewer | `<Founder or explicitly delegated competent human>` |
| Review timestamp | `<ISO 8601 with offset>` |

Conflicts and gaps remain visible and fail closed for the Product composition. They route to competent human review and never reduce upstream restrictions.

## Protected current references

ASSET-1, ASSET-2 and ASSET-3 remain `VALIDATED / NOT_CANONICAL / NOT_ATTACHABLE`. This contract does not attach, promote, downgrade or create a synthetic decision for any of them.

## Validation checklist

- [ ] One of the four exact P003 mappings is used without reinterpretation.
- [ ] P003 authority, decision, handoff and Asset SOT are cited.
- [ ] Only `READ / REFERENCE / CONSUME DECISION` occurred.
- [ ] Every prohibited operation remained unused.
- [ ] Restrictions remain visible and no Product decision broadens them.
- [ ] No real Asset attachment or eligibility decision is present in this template.
- [ ] Any governed human decision uses `governance-decision-record-template.md`.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-007` |
| Requirements / acceptance criteria | `R05`; `R05.1–R05.4`; `R06.3–R06.4` |
| Design component | `C04` |
| Design Decision | `P004-D005` |
| Upstream | P003 Asset-to-Product handoff, `product-composition-record-template.md` |

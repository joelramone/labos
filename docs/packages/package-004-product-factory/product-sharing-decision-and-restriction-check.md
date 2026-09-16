# Product Sharing Decision and Restriction Check

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary structure. It creates no sharing permission, publication, Product, attachment, approval, activation, commercialization, Revenue event, or governance decision.

## Purpose and authority

Task: `T004-021`. Use this payload with `governance-decision-record-template.md` and decision type `SHARING_DECISION`; it is not a competing governance envelope. Sharing is an orthogonal human-governed decision for an exact Product/version, audience and context.

`ACTIVE ≠ PUBLIC`; `ACTIVE ≠ COMMERCIALIZED`; `ACTIVE ≠ REVENUE_GENERATING`; packaging, approval, activation, Product Value or Demand Validation grants no sharing right.

Final authority is the Founder or an explicitly delegated human competent for every affected authority layer. AI may read, analyze, summarize, compare, draft, recommend and detect gaps; it may not authorize sharing, remove restrictions or become authority.

## Sharing request

| Field | Entry |
|---|---|
| Product / exact version / Product SOT | `<REQUIRED REFERENCES>` |
| Lifecycle state | `<EXACT SEVEN-STATE VALUE>` |
| Requestor | `<REFERENCE>` |
| Requested audience | `<NAMED PEOPLE/GROUP/CLASS>` |
| Sharing context and purpose | `<REQUIRED>` |
| Requested channel/form | `<DESCRIPTIVE; no implementation implied>` |
| Requested geography/duration | `<VALUE>` |
| Packaging manifest | `<REFERENCE>` |
| Product Risk record | `<REFERENCE>` |
| Approval / activation references | `<REFERENCES or NOT_APPLICABLE>` |
| Registry current-truth reference | `<REFERENCE>` |
| Proposed effective/expiry time | `<ISO 8601 / EVENT>` |

## Fail-closed restriction intersection

Every row must cite its authoritative source. `UNKNOWN`, missing, conflicting or inaccessible authority is restrictive and blocks the affected scope.

| Constraint class | Authoritative source | Requested scope | Permitted scope | Conflict/gap | Effective restriction |
|---|---|---|---|---|---|
| Licensing | `<REFERENCE>` | `<VALUE>` | `<VALUE/UNKNOWN>` | `<VALUE>` | `<MOST RESTRICTIVE>` |
| Usage | `<REFERENCE>` | `<VALUE>` | `<VALUE/UNKNOWN>` | `<VALUE>` | `<MOST RESTRICTIVE>` |
| Sharing | `<REFERENCE>` | `<VALUE>` | `<VALUE/UNKNOWN>` | `<VALUE>` | `<MOST RESTRICTIVE>` |
| Distribution | `<REFERENCE>` | `<VALUE>` | `<VALUE/UNKNOWN>` | `<VALUE>` | `<MOST RESTRICTIVE>` |
| Dependency | `<REFERENCE>` | `<VALUE>` | `<VALUE/UNKNOWN>` | `<VALUE>` | `<MOST RESTRICTIVE>` |
| Risk | `<REFERENCE>` | `<VALUE>` | `<VALUE/UNKNOWN>` | `<VALUE>` | `<MOST RESTRICTIVE>` |
| Sensitivity/privacy | `<REFERENCE>` | `<VALUE>` | `<VALUE/UNKNOWN>` | `<VALUE>` | `<MOST RESTRICTIVE>` |
| Product-specific | `<REFERENCE>` | `<VALUE>` | `<VALUE/UNKNOWN>` | `<VALUE>` | `<MOST RESTRICTIVE>` |
| Asset/external-input upstream | `<P003/other authority reference>` | `<VALUE>` | `<VALUE/UNKNOWN>` | `<VALUE>` | `<MOST RESTRICTIVE>` |

Effective permission is the intersection of all applicable permissions, never their union. P003 decisions are consumed through `READ / REFERENCE / CONSUME DECISION`; P004 cannot write, override, recompute, promote, downgrade or alter Asset authority. Packaging cannot broaden rights.

## Decision payload

| Field | Entry |
|---|---|
| Governance Decision Record | `<REQUIRED for an actual future decision>` |
| Effective permitted audience/context | `<VALUE or NONE>` |
| Conditions and redactions | `<VALUE>` |
| Prohibited audience/context | `<VALUE>` |
| Human authority and delegation basis | `<REFERENCE>` |
| Result | `<AUTHORIZED_WITHIN_SCOPE / DENIED / RETURNED_FOR_REVIEW>` |
| Lifecycle effect | `NONE` |
| Public status | `<NOT_PUBLIC unless separately and explicitly authorized>` |
| Commercialization/Revenue effect | `NONE` |
| Review/expiry trigger | `<DATE/EVENT>` |
| History/supersession reference | `<REFERENCE or NONE>` |

## Validation checklist

- [ ] Exact Product/version, Product SOT, audience and context are identified.
- [ ] Licensing, usage, sharing, distribution, dependency, risk, sensitivity and upstream restrictions are cited and intersected fail closed.
- [ ] External or Public scope receives explicit competent-human review; ambiguity yields denial or review.
- [ ] ACTIVE, packaging, approval, Product Value and Demand Validation confer no sharing or commercial permission.
- [ ] AI/software neither authorizes sharing nor removes a restriction.
- [ ] No publication, sharing action, real decision, Product/Asset mutation or P005 action occurs.

## Traceability

| Trace | Approved source |
|---|---|
| Task | `T004-021` |
| Requirements / AC | `R06`, `R12`, `R22`; `R22.1–R22.4` |
| Design components | `C08`, `C16`, `C19` |
| Design Decisions | `P004-D008`, `P004-D012` |
| Inputs | `governance-decision-record-template.md`, `product-packaging-manifest-template.md`, `product-risk-evaluation-and-acceptance-template.md`, `product-approval-and-activation-event-template.md`, `manual-product-registry-contract.md` |

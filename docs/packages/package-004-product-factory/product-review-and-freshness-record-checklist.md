# Product Review and Freshness Record / Checklist

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary workflow. It performs no review event, lifecycle transition, approval, activation, deprecation, retirement, publication or commercialization and implements no persistence or automation.

## Purpose and truth boundaries

Task: `T004-022`. This mechanism compares an exact Product/version and prior decision with current authoritative references. Use the `REVIEW_DECISION` payload in `governance-decision-record-template.md` for an actual future human disposition.

`CURRENT_TRUTH` is resolved from the current Product SOT and valid governance references. `HISTORICAL_TRUTH` is immutable documentary prior-state/event evidence. Review evidence and freshness evidence support comparison but are neither truth authority nor lifecycle authority. Product SOT, Asset SOT and working/derived copies remain distinct.

## Review identity

| Field | Entry |
|---|---|
| Review record ID/version | `<PLACEHOLDER>` |
| Product / exact version | `<REFERENCE>` |
| Product SOT | `<AUTHORITATIVE REFERENCE>` |
| Current Registry view | `<REFERENCE>` |
| Prior decision under review | `<REFERENCE>` |
| Trigger | `<DATE/EVENT/CHANGE>` |
| Review scope | `<REQUIRED>` |
| Reviewer / human authority | `<REFERENCE>` |
| Comparison timestamp | `<ISO 8601 WITH OFFSET>` |
| Historical/supersession links | `<REFERENCES>` |

## Trigger and freshness checklist

| Trigger domain | Current authority/reference | Prior reference | Change/freshness finding | Source accessible? | Human disposition required |
|---|---|---|---|---|---|
| Asset identity/version/eligibility | `<P003 REFERENCE>` | `<REFERENCE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Product identity/version/schema | `<PRODUCT SOT>` | `<REFERENCE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Composition | `<REFERENCE>` | `<REFERENCE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Dependencies/compatibility | `<REFERENCE>` | `<REFERENCE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Licensing/usage/sharing/distribution | `<REFERENCES>` | `<REFERENCE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Product Risk | `<REFERENCE>` | `<REFERENCE>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Quality/readiness evidence | `<REFERENCES>` | `<REFERENCES>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Product Value / Demand Validation | `<SEPARATE REFERENCES>` | `<REFERENCES>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Consumer/context/use/exposure | `<REFERENCES>` | `<REFERENCES>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Ownership/authority/SOT | `<REFERENCES>` | `<REFERENCES>` | `<VALUE>` | `<YES/NO>` | `<VALUE>` |
| Scheduled review | `<SCHEDULE REFERENCE>` | `<LAST REVIEW>` | `<DUE/NOT_DUE>` | `<YES/NO>` | `<VALUE>` |

Missing, stale, conflicting or inaccessible sources are named gaps. They never become presumed-current evidence.

## Copy and history reconciliation

| Check | Result | Evidence/gap |
|---|---|---|
| Current Product SOT uniquely resolves | `<PASS/FAIL>` | `<REFERENCE>` |
| Asset truth resolves only from Asset SOT/P003 | `<PASS/FAIL>` | `<REFERENCE>` |
| Registry view agrees with Product SOT | `<PASS/FAIL>` | `<REFERENCE>` |
| Working/derived copies are labelled non-authoritative | `<PASS/FAIL>` | `<REFERENCE>` |
| Current truth links to applicable history | `<PASS/FAIL>` | `<REFERENCE>` |
| Prior history remains unchanged and supersession-linked | `<PASS/FAIL>` | `<REFERENCE>` |
| Review evidence and freshness evidence are separately cited | `<PASS/FAIL>` | `<REFERENCE>` |

## Human disposition

| Field | Entry |
|---|---|
| Governance Decision Record | `<REQUIRED for actual disposition>` |
| Result | `<CURRENT / REVIEW_REQUIRED / REMEDIATION_REQUIRED / RETURNED_FOR_REVIEW>` |
| Named stale/inaccessible sources | `<LIST or NONE>` |
| Follow-up owner/action/trigger | `<VALUE>` |
| Lifecycle effect | `UNCHANGED unless a separate authorized human decision is referenced` |
| Approval/activation effect | `NONE` |
| Deprecation/retirement effect | `NONE` |
| Publication/commercialization effect | `NONE` |

## Validation checklist

- [ ] Every R23 trigger has a human disposition and source reference.
- [ ] Current Truth, Historical Truth, review evidence and freshness evidence are distinct.
- [ ] Product SOT, Asset SOT and working/derived copies remain distinct.
- [ ] A fired trigger, stale evidence or inaccessible source never silently changes state.
- [ ] Approval, activation, deprecation, retirement, publication and commercialization require their own authorized human decisions.
- [ ] No persistence, Historical Truth infrastructure, database, API, notification or workflow automation is implied.

## Traceability

| Trace | Approved source |
|---|---|
| Task | `T004-022` |
| Requirements / AC | `R18.4`, `R23`; `R23.1–R23.4` |
| Design components | `C11`, `C15` |
| Design Decisions | `P004-D004`, `P004-D010` |
| Inputs | `governance-decision-record-template.md`, `product-dependency-declaration-template.md`, `product-version-and-compatibility-record-template.md`, `manual-product-registry-contract.md` |

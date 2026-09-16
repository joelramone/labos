# Manual Product Registry Contract and Views

> **DOCUMENTARY CONTRACT — NOT_A_GOVERNED_INSTANCE**  
> Manual logical representation only. This file creates no Registry entry, Candidate, Product, lifecycle event, database, API, service, index implementation, event store, persistence, automation, RAG, MCP, or agent.

## Purpose and authority

Task: `T004-020`. The manual Product Registry provides governed lookup over Product/Candidate current truth and references immutable governance history. The authoritative Product SOT remains the Product record; the Registry is a reference index and cannot silently become Product, Asset, Research, Knowledge, external-dependency or Package 005 Revenue truth.

`Product SOT ≠ Asset SOT`; `Product Registry ≠ Asset Registry`; `Product Registry ≠ evidence store`; `Product Registry ≠ Revenue Engine`; copy ≠ authority; reference ≠ ownership.

Package 003 is `CLOSED`. P003→P004 operations are limited to `READ / REFERENCE / CONSUME DECISION`; `WRITE / OVERRIDE / RECOMPUTE / PROMOTE / DOWNGRADE / ALTER_HANDOFF / ALTER_ASSET_AUTHORITY` are prohibited.

## Manual Product index row contract

| Field | Manual entry/reference |
|---|---|
| Product ID | `<AUTHORITATIVE ID>` |
| Product version | `<VERSION>` |
| Lifecycle state | `<CANDIDATE / UNDER_REVIEW / READY / APPROVED / ACTIVE / DEPRECATED / RETIRED>` |
| Owner | `<HUMAN OWNER REFERENCE>` |
| Product SOT | `<AUTHORITATIVE REFERENCE>` |
| Composition | `<REFERENCE>` |
| Dependencies / eligibility | `<REFERENCES>` |
| Product Quality | `<REFERENCE>` |
| Product Risk | `<REFERENCE>` |
| Product Value | `<REFERENCE>` |
| Demand Validation | `<REFERENCE>` |
| Readiness | `<REFERENCE>` |
| Approval | `<REFERENCE or NOT_APPLICABLE>` |
| Activation | `<REFERENCE or NOT_APPLICABLE>` |
| Version / compatibility | `<REFERENCE>` |
| Restriction summary / source | `<SUMMARY and AUTHORITATIVE REFERENCES>` |
| Provenance | `<REFERENCE>` |
| Sharing status/reference | `<REFERENCE / NOT_DECIDED>` |
| Current status timestamp | `<ISO 8601 WITH OFFSET>` |
| Next review | `<DATE/EVENT>` |
| Supersedes / historical links | `<REFERENCES or NONE>` |
| Missing-data report | `<NAMED GAPS or NONE>` |

Lifecycle state cannot collapse Quality, Risk, Value, Demand Validation, Readiness, Approval or Activation. `ACTIVE ≠ PUBLIC / COMMERCIALIZED / REVENUE_GENERATING`.

## Repository-authoritative manual views

Only these logical views defined by `product-registry-design.md` are in scope:

| View | Required answers | Authority rule |
|---|---|---|
| Candidate index | Candidate identity, owner, state, review outcome, proposed composition, SOT, restrictions, next review | References Candidate SOT and review history; REJECTED remains an outcome, not state |
| Product index | Product/version, owner, lifecycle, composition, dependencies, restrictions, readiness, approval/activation, sharing, SOT, next review | Summarizes current Product truth; Product SOT remains authoritative |
| Composition view | Exact referenced input versions, P003 eligibility decisions and contribution relationships | References Asset/dependency authorities; never owns or recomputes them |
| Evidence view | Quality, Risk, Value, Demand Validation, Readiness and provenance references and decision basis | Reference map only; not an evidence store and no status inference |
| History view | Timestamp, prior/new value or state, actor/authority, reason and decision record | Documentary append-only history; correction adds superseding reference |

No technology-specific UI or persistence is implied.

## CURRENT_TRUTH and HISTORICAL_TRUTH

- `CURRENT_TRUTH` is resolved manually from the current authoritative Product/Candidate SOT plus valid, non-superseded human governance references.
- `HISTORICAL_TRUTH` is documentary prior-state/event evidence. It is never overwritten; correction or replacement adds a linked superseding record.
- The current row must link bidirectionally to applicable history, and history must identify its subject/version. A conflict or broken link is a named gap and blocks the claimed current update.
- This contract does not create a Historical Truth Store or persistence implementation.

## Manual update and lookup controls

1. A human verifies identity/version, Product SOT, source authority and current state.
2. A human resolves referenced composition, P003 eligibility, dependencies, evidence, restrictions and governance records without copying their authority.
3. A human records the current view timestamp, next review and historical/supersession links.
4. A second manual check rejects duplicate IDs, invalid transitions, unauthorized changes, missing references and silent history rewrites.
5. Review/freshness flags produce `review_required`; they never change lifecycle, eligibility, approval or activation automatically.

No automatic lifecycle transition, decision execution, eligibility recomputation, Product approval or Product activation is permitted. AI may read, analyze, compare, draft, recommend or detect gaps; it may not become Registry authority or change current truth.

## Validation checklist

- [ ] All five repository-authoritative logical views are represented; no invented view or implementation exists.
- [ ] Product/Candidate identity, version, owner, lifecycle, composition, eligibility, restrictions, dependencies, evidence, readiness, approval, activation, sharing, SOT and review are answerable or explicitly missing.
- [ ] Product SOT, Asset SOT, source evidence, external dependency truth and Registry references remain distinct.
- [ ] Current truth reconciles bidirectionally with non-overwritten documentary history.
- [ ] Duplicate IDs, unauthorized changes, missing authority and conflicts fail closed.
- [ ] P003 restrictions and eligibility decisions are consumed read-only; ASSET-1/2/3 remain `VALIDATED / NOT_CANONICAL / NOT_ATTACHABLE`.
- [ ] Manual-first operation and human authority are explicit; persistence and automation are absent.
- [ ] Package 005–007 remain dormant; no Public, commercialization, transaction, payment or Revenue truth is created.
- [ ] Contract remains domain- and technology-neutral and contains zero real Registry entries.

## Traceability

| Trace type | Approved mapping |
|---|---|
| Task | `T004-020` |
| Requirements / acceptance criteria | `R01–R02`, `R08–R10`, `R18`, `R23–R25`; `R25.1–R25.4` |
| Design components | `C01`, `C02`, `C12`, `C13`, `C15` |
| Design Decisions | `P004-D001–P004-D004`, `P004-D006`, `P004-D010` |
| Authoritative inputs | `product-registry-design.md` and applicable `T004-002–T004-019` outputs |

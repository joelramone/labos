# Product Composition Record Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank reusable structure. It creates no Product, Product Candidate, Asset attachment, eligibility decision, lifecycle transition, approval, activation, packaging instance or commercialization authority.

## Purpose and authority boundary

Use this record to describe a version-aware governed Product composition snapshot. A composition contains one or multiple governed inputs and may contain `0..N` Asset references by domain. A Product may therefore have no Asset attachment when other governed inputs satisfy the approved Design. Product 004 owns Product composition truth only; Package 003 remains authoritative for Asset identity, lifecycle, SOT, eligibility and handoff.

Final authority is the Founder or an explicitly delegated competent human. Use [governance-decision-record-template.md](./governance-decision-record-template.md) for any governed decision; this template is not a competing decision system.

## Composition identity and version

| Field | Entry |
|---|---|
| Product ID/reference | `<REQUIRED>` |
| Product version | `<REQUIRED exact version/reference>` |
| Product SOT | `<REQUIRED authoritative reference>` |
| Composition ID | `<REQUIRED>` |
| Composition version | `<REQUIRED>` |
| Truth classification | `<CURRENT_TRUTH / HISTORICAL_TRUTH>` |
| Composition status | `<CURRENT / SUPERSEDED / historical snapshot description>` |
| Snapshot/effective timestamp | `<REQUIRED ISO 8601 with offset>` |
| Supersedes composition | `<REFERENCE or NONE>` |
| Superseded by | `<REFERENCE or NONE>` |
| Responsible human authority | `<Founder or explicitly delegated human reference>` |
| Composition rationale | `<REQUIRED>` |
| Review trigger | `<DATE/EVENT/CHANGE>` |

Prior snapshots are immutable documentary evidence. A changed composition creates a new version and supersession link; it never silently overwrites historical evidence. This is documentary support, not Historical Truth infrastructure.

## Governed inputs

Record one row per governed input. At least one governed input is required for a composition; an Asset is not required.

| Input ID/reference | Input class | Exact version/reference | Contribution/purpose | Source authority | Authoritative SOT | Provenance reference | Restrictions reference | Relationship/shared-use note | Included status |
|---|---|---|---|---|---|---|---|---|---|
| `<VALUE>` | `<Asset / external / operational / platform / other approved governed input>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<REFERENCE>` | `<REFERENCE or named gap>` | `<REFERENCE or NONE with rationale>` | `<VALUE>` | `<VALUE>` |

## Asset references (`0..N` by domain)

Leave this section empty with rationale when the composition contains no Asset attachment. Shared Assets receive separate rows for each governed relationship; shared use does not merge Product and Asset authority.

| Asset ID | Asset version/reference | Domain | Authoritative Asset SOT | Eligibility decision reference | Eligibility result | P003 handoff completeness reference | Attachment status | Upstream restrictions | Provenance reference | Authority source | Decision timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `<VALUE>` | `<EXACT VALUE>` | `<VALUE>` | `<P003 REFERENCE>` | `<P003 REFERENCE>` | `<P003 RESULT>` | `<P003 REFERENCE>` | `<NOT_ATTACHED / governed attachment reference>` | `<licensing, usage, sharing, distribution, dependency and risk references>` | `<REFERENCE>` | `<P003 AUTHORITY>` | `<ISO 8601 with offset>` |

P004 may only `READ`, `REFERENCE` and `CONSUME DECISION`. It cannot write, override, recompute, promote, downgrade, alter a handoff, reduce restrictions or alter Asset authority/SOT. Product approval cannot override Asset eligibility.

## Dependency and restriction reconciliation

| Reference | Dependency class | Exact version | Source authority | Compatibility/availability | Effective restrictions | Conflict or gap | Product-level effect | Human disposition reference |
|---|---|---|---|---|---|---|---|---|
| `<VALUE>` | `<external / operational / platform / Asset>` | `<VALUE>` | `<VALUE>` | `<VALUE>` | `<licensing / usage / sharing / distribution / dependency / risk>` | `<NONE or named gap>` | `<descriptive effect>` | `<REFERENCE or REQUIRED_REVIEW>` |

All upstream restrictions remain visible. A conflict or unresolved licensing/risk issue fails closed at the Product gate and routes to competent human review; it does not alter the upstream source.

## Validation checklist

- [ ] Banner remains `TEMPLATE — NOT_A_GOVERNED_INSTANCE`; no real subject or attachment exists.
- [ ] One or multiple governed inputs are represented; Asset cardinality is `0..N`.
- [ ] Product, composition and all input versions are exact and version-aware.
- [ ] Current, historical and superseded snapshots are distinguishable without overwriting history.
- [ ] Every Asset row cites P003 SOT, eligibility, handoff, restrictions, provenance and authority.
- [ ] External, operational and platform dependencies retain their own source authority.
- [ ] Every upstream restriction maps to an effect or explicit non-applicability.
- [ ] Final review and any decision remain human-authoritative.
- [ ] The record is domain-neutral and selects no technology.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-006` |
| Requirements / acceptance criteria | `R04`, `R06`; `R04.1–R04.4`, `R06.1–R06.4` |
| Design component | `C03` |
| Design Decisions | `P004-D005`, `P004-D006` |
| Upstream | `tasks.md`, `product-composition-design.md`, P003 Asset authority and handoff records |

# Product Provenance Record Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary lineage structure. It creates no Product, provenance fact, source authority, lifecycle transition or infrastructure.

## Purpose and authority boundary

Represent only lineage that genuinely exists. Supported conceptual paths include `Research → Knowledge → Asset → Product Candidate → Product` and `external source → dependency → Product`. Omit inapplicable nodes and name missing or uncertain links; never fabricate lineage.

P004 owns Product truth only. Research, Knowledge, Asset and external-source authorities remain authoritative for their own records. Referencing their evidence neither copies nor changes their authority.

## Record identity

| Field | Entry |
|---|---|
| Product ID/reference | `<REQUIRED>` |
| Product version | `<REQUIRED exact version>` |
| Product SOT | `<REQUIRED>` |
| Provenance record ID/version | `<REQUIRED>` |
| Truth classification | `<CURRENT_TRUTH / HISTORICAL_TRUTH>` |
| Snapshot/effective timestamp | `<ISO 8601 with offset>` |
| Responsible human authority | `<Founder or explicitly delegated competent human>` |
| Supersedes | `<REFERENCE or NONE>` |

## Lineage nodes

| Node ID | Node type | Exact identity/version | Source/SOT reference | Source authority | Evidence reference | Provenance completeness note |
|---|---|---|---|---|---|---|
| `<VALUE>` | `<Research / Knowledge / Asset / Product Candidate / Product / external source / dependency>` | `<VALUE>` | `<REFERENCE>` | `<AUTHORITATIVE SOURCE>` | `<REFERENCE or named gap>` | `<descriptive status>` |

## Lineage edges

| From node | Relationship | To node | Evidence/decision reference | Timestamp | Authority | Gap/uncertainty |
|---|---|---|---|---|---|---|
| `<VALUE>` | `<DESCRIPTIVE, source-supported relation>` | `<VALUE>` | `<REFERENCE>` | `<ISO 8601 or UNKNOWN>` | `<SOURCE AUTHORITY>` | `<NONE / MISSING / UNKNOWN / NOT_APPLICABLE with explanation>` |

`MISSING`, `UNKNOWN` and `NOT_APPLICABLE` are descriptive gap values only, not normative lifecycle states. Candidate origin, exact input versions, relevant human decision references and external-origin dependencies must be cited when they exist.

## Current and historical preservation

| Field | Entry |
|---|---|
| Current record reference | `<REFERENCE>` |
| Historical snapshot references | `<REFERENCES or NONE>` |
| Supersession rationale | `<VALUE or NOT_APPLICABLE>` |
| Preserved unresolved links | `<REFERENCES/descriptions>` |

Corrections create a superseding record and preserve prior evidence. This template implements no database, event store, persistence layer, Historical Truth Store, RAG index, MCP or agent.

## Validation checklist

- [ ] Banner remains `TEMPLATE — NOT_A_GOVERNED_INSTANCE`; no real provenance instance exists.
- [ ] Every represented link has evidence, authority and exact identity/version, or an explicit gap.
- [ ] Research, Knowledge, Asset and external authorities remain distinct from Product authority.
- [ ] Missing or uncertain lineage is not inferred or invented.
- [ ] Current and historical truth are documentary and prior evidence is not overwritten.
- [ ] Any governed human decision reuses `governance-decision-record-template.md`.
- [ ] AI assistance is non-authoritative and cannot change or invent provenance.
- [ ] Domain and technology neutrality are preserved.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-010` |
| Requirements / acceptance criteria | `R09`; `R09.1–R09.4`; `R17.2`; `R21.1`; `R25.3` |
| Design component | `C12` |
| Design Decisions | `P004-D001`, `P004-D002`, `P004-D006`, `P004-D015` |
| Upstream | `product-candidate-template.md`, `product-record-template.md`, `product-ownership-sot-template.md`, `product-composition-record-template.md`, authoritative provenance sources |

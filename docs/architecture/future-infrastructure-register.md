# Future Infrastructure Register — LabOS

## Status and scope

| Field | Value |
|---|---|
| Document status | PLANNING / NON-GOVERNING |
| Architecture Baseline | LABOS-ARCH-BASELINE-001 v1.0 — unchanged |
| Governance level | SOLO |
| Implementation authorization | NONE |

[Decisión] Este registro evita que concerns transversales se confundan con etapas del Knowledge-to-Value Pipeline. Registra capacidades dormidas y triggers; no selecciona tecnología, asigna nuevos números de Package ni autoriza implementación.

## Capability register

| Capability | Status | Purpose | Dependencies | Evidence-based activation trigger | Prohibited premature assumptions | Architecture owner | Source-of-truth relationship |
|---|---|---|---|---|---|---|---|
| Canonical Persistence | DORMANT / FUTURE | Hacer machine-operable el estado canónico gobernado de Knowledge, Assets y futuros Products | Contratos estables de Package 002/003; ownership y authority definidos | Filesystem/manual operation becomes unreliable; multiple Labs need structured deterministic queries; machine consumers need governed reads; reconciliation cost becomes material | Database, schema engine, cloud, vendor or migration strategy | Founder / Architecture Governance | May persist `CURRENT_TRUTH`; never creates canonical authority |
| Historical Truth | DORMANT / FUTURE | Preservar y reconstruir prior states, versions, provenance, decisions, reviews, supersession and deprecation | Canonical IDs, version/history contracts, immutable decision evidence | Silent-overwrite risk appears; audits require as-of reconstruction; multiple consumers need historical compatibility; manual history reconciliation becomes unreliable | Event store, append-only database, event-sourcing pattern or retention technology | Founder / Architecture Governance | Preserves `HISTORICAL_TRUTH`; cannot overwrite or reinterpret source records silently |
| Retrieval / RAG | DORMANT / FUTURE | Mejorar discovery y retrieval semántico sobre un corpus gobernado | Stable canonical references; sensitivity/access rules; useful corpus | Manual navigation becomes inefficient; cross-Lab discovery is recurrent; semantic retrieval demonstrates measurable time/quality value | Vector database, embedding model, chunking framework, RAG vendor; retrieved text as truth | Founder / Architecture Governance | Retrieval layer only; returns references to canonical/historical sources and is never source of truth |
| MCP Access Layer | DORMANT / FUTURE | Exponer operaciones gobernadas de lectura y, eventualmente, propuestas a tools/clients | Stable read contracts, authorization boundaries, canonical identifiers, error semantics | Two or more external tool/AI clients need governed access; stable LabOS read operations exist; audit/provenance responses are deterministic | MCP server design, transport, hosting, write tools, unrestricted client authority | Founder / Architecture Governance | Interface/access layer only; not persistence and not canonical authority |
| AI Agent Runtime | DORMANT / FUTURE | Ejecutar asistencia repetible para search, trace, compare, summarize, stale/conflict detection and proposals | Structured inputs/outputs; human approval boundaries; repeatable workflows; observability proportional to risk | Repetitive governed workflow exists; human review gates are explicit; automation saves meaningful Founder time; failure behavior is testable | Agent framework, autonomous writes, model/vendor, multi-agent topology, unattended authority | Founder / Architecture Governance | May retrieve and propose; cannot canonicalize Knowledge, promote Assets, change ownership/authority, erase provenance or rewrite history |

## Cohesion and decomposition

[Hipótesis] Canonical Persistence and Historical Truth form one cohesive future foundation because current-state reconstruction and immutable history share identity/version requirements. Retrieval/RAG, MCP access and Agent Runtime are separate consumers/layers with different failure modes and triggers.

```text
Canonical + Historical Truth foundation
                ↓ references
Retrieval / RAG (optional)
                ↓ governed reads
MCP Access (optional) ── Agent Runtime (optional consumer)
```

[Decisión] The arrows express possible dependency, not a mandatory implementation sequence. An agent can operate through human-mediated files before MCP; Product Factory can remain documentary without any of these capabilities.

## Global invariants

- `CURRENT_TRUTH` and `HISTORICAL_TRUTH` are distinguishable.
- Historical versions, provenance, decisions, reviews, supersession and deprecation are not silently overwritten.
- RAG is retrieval, not truth.
- MCP is access, not persistence or authority.
- AI agents may search, retrieve, trace, compare, summarize, identify stale/conflicts and propose.
- AI agents may not autonomously rewrite history, canonicalize Knowledge, promote Assets, change ownership/authority or erase provenance.

## Review triggers

Review this register after a new Package closure, a demonstrated operational pain matching a trigger, a second machine consumer, or a proposed infrastructure Package. Absence of a trigger keeps each capability dormant.

# Diagramas de Arquitectura del Asset System

## Alcance

[Decisión] Estos diagramas representan los modelos normativos de Package 003; no crean arquitectura, runtime ni autoridad nueva.

## 1. Knowledge → Asset

```mermaid
flowchart LR
  subgraph P1[Package 001 / Lab]
    R[Research] --> E[Evidence] --> F[Finding]
  end
  subgraph P2[Package 002]
    F --> K[Knowledge Object]
  end
  subgraph P3[Package 003]
    K --> H[Handoff] --> C[Asset Candidate] --> Q[Qualification] --> A[Asset]
  end
```

[Hecho] Package 002 conserva lifecycle, confidence, freshness y provenance del Knowledge Object. El handoff no renombra ni elimina el KO.

## 2. Lifecycle de Candidate

```mermaid
stateDiagram-v2
  [*] --> CANDIDATE
  CANDIDATE --> UNDER_REVIEW
  CANDIDATE --> VALIDATED: Fast Path con gates y autoridad
  CANDIDATE --> REJECTED
  UNDER_REVIEW --> VALIDATED
  UNDER_REVIEW --> REJECTED
  VALIDATED --> CANONICAL: decisión explícita
  CANONICAL --> DEPRECATED
  DEPRECATED --> ARCHIVED
```

[Decisión] Son exactamente siete estados. ARCHIVED y REJECTED son terminales; reactivation crea un nuevo Candidate referenciado.

## 3. Dimensiones ortogonales

```mermaid
flowchart TB
  X[Asset record]
  X --- L[lifecycle]
  X --- S[sharing_scope]
  X --- C[consumption_state]
  X --- T[content_state]
  X --- Y[sensitivity]
  X --- R[risk]
  X --- P[product_attachment]
  X --- V[review_required]
```

[Decisión] Ningún eje se deriva automáticamente de otro ni se convierte en lifecycle state.

## 4. Promotion

```mermaid
flowchart LR
  C[Asset Candidate] --> E[Evaluation: 5 dimensions + gates]
  E --> D{Explicit Authority Decision}
  D -->|PROMOTED| A[Canonical Asset]
  D -->|REMEDIATION_REQUIRED| R[Preserve state + gaps]
  D -->|REJECTED / DEFERRED| O[Recorded outcome]
  AI[AI assistance] -.evidence / recommendation.-> E
  AI -.no authority.-> D
```

[Decisión] No existe `AUTO_PROMOTE`; AI no decide ni firma.

## 5. Source of truth y sharing entre Labs

```mermaid
flowchart LR
  O[Originating Lab / Owner] --> S[(1 canonical source of truth)]
  S -->|authorized reference| C1[Consumer Lab A]
  S -->|authorized reference| C2[Consumer Lab B]
  C1 -.defect report.-> O
  C2 -.substantial change.-> V[Version / Derived Asset / Fork / New Asset review]
  U[Unmanaged copy] -.not authoritative.-> S
```

[Decisión] Sharing no transfiere ownership ni Canonical_Authority. `sharing_scope` no demuestra consumo.

## 6. Versioning y evolución

```mermaid
flowchart TB
  A[Canonical Asset / asset_id A]
  A -->|PATCH / MINOR / MAJOR applicable| L[Same lineage / asset_id A]
  A -->|derived| D[Derived Asset / new asset_id]
  A -->|fork| F[Fork / new asset_id]
  A -->|replacement or supersession| R[Successor + bidirectional reference]
  A -.history preserved.-> H[Immutable prior versions]
```

[Decisión] MAJOR no oculta un cambio de identidad; derived Asset y fork reciben ID nuevo.

## 7. Asset → Product handoff

```mermaid
flowchart LR
  A[CANONICAL Asset] --> R[Readiness + restrictions + compatibility]
  R --> D[Dependency declaration]
  D --> B{{Product handoff boundary}}
  B -.Package 004 NOT_AUTHORIZED.-> P[Future Product context]
```

[Decisión] Package 003 se detiene en el boundary. No define Product lifecycle, Factory, pricing, customers ni Product architecture.

## 8. Deprecation y conservación

```mermaid
flowchart LR
  C[CANONICAL] -->|explicit decision + impact| D[DEPRECATED]
  D -->|30 days + consumers/migrations resolved| A[ARCHIVED]
  D -.active consumer.-> M[Migration / replacement / accepted impact]
  A -.new demand.-> N[New CANDIDATE referencing history]
```

## Consistency audit

| Control | Resultado |
|---|---|
| Estados lifecycle | 7/7 |
| Automatic promotion/transitions | 0 |
| Orthogonal axes represented separately | 8/8 |
| Canonical sources per Asset | 1 |
| Reference-based sharing | PASS |
| Version history preserved | PASS |
| Product lifecycle represented | 0 |
| Capability activation represented | 0 |
| Runtime/implementation architecture | 0 |

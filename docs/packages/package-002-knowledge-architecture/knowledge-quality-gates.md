# Quality Gates del Conocimiento

## Propósito

Este documento define los criterios mínimos que un Knowledge Object debe cumplir para transitar entre estados del lifecycle. [Decisión] Los gates son proporcionales al contexto: el camino rápido permanece práctico (≤2 minutos de verificación) mientras que transiciones de mayor impacto requieren rigor adicional.

---

## Gate: captured → validated (camino rápido, default)

Este es el camino por defecto per Principio 6. La mayoría del conocimiento transita aquí sin revisión formal separada. [Decisión]

| Criterio | Verificación | Tiempo estimado |
|----------|-------------|-----------------|
| Todos los 10 campos obligatorios presentes | Inspección visual: ningún campo vacío. | ~30 seg. [Hecho] |
| Confianza asignada con justificación (no UNKNOWN) | Campo `confidence` tiene nivel (alto/medio/bajo) + ≥1 oración de justificación. | ~30 seg. [Hecho] |
| `source_reference` verificable | El recurso referenciado existe y es accesible. | ~30 seg. [Hecho] |
| Summary autocontenido | Se entiende sin contexto externo adicional. | ~30 seg. [Hecho] |
| **Aprobación** | Fundador (automática en SOLO — no se requiere revisión separada). | 0 seg. [Decisión] |

**Overhead total:** ≤2 minutos por KO. [Decisión]

**Gate pass:** Si los 4 criterios se cumplen, el KO transita automáticamente a `validated`. [Decisión]

**Gate fail:** Si falta algún criterio, el KO permanece en `captured` hasta completarse. [Decisión]

---

## Gate: captured → under_review (opcional, para alto impacto)

Este camino se usa cuando el fundador decide que un KO requiere evaluación formal antes de validar. [Decisión]

| Criterio | Verificación |
|----------|-------------|
| Todos los campos obligatorios presentes | Misma verificación que el gate rápido. [Decisión] |
| Razón para revisión formal documentada | 1 oración explicando por qué no se usa el camino rápido. [Decisión] |
| **Aprobación** | Fundador decide explícitamente invocar revisión. [Decisión] |

**Cuándo usar:** KOs que informarán decisiones financieras, KOs generados enteramente por agente IA sin supervisión, KOs que contradigan conocimiento existente. [Decisión]

---

## Gate: under_review → validated

| Criterio | Verificación |
|----------|-------------|
| Reviewer confirma coherencia | El fundador revisa la afirmación y confirma que es lógicamente consistente con el conocimiento existente. [Decisión] |
| Confianza asignada | Nivel + justificación completos. [Decisión] |
| Nota de revisión | Resultado (aprobado/rechazado) documentado en ≤2 oraciones. [Decisión] |

**Gate pass:** Si aprobado → `validated`. [Decisión]

**Gate fail — rechazo:** → `archived` con motivo. [Decisión]

**Gate fail — devuelto:** → `captured` para mejora con nota de qué falta. [Decisión]

---

## Gate: validated → canonical

Este es el gate más exigente. Solo conocimiento de alto valor lo transita. [Decisión]

| Criterio | Verificación | Justificación |
|----------|-------------|---------------|
| Confianza: ALTO sostenida | El campo `confidence` es "alto" y ha permanecido así desde la última revisión. | Solo conocimiento de alta certeza merece status canónico. [Decisión] |
| Estabilidad: sin cambios en ≥60 días | No ha habido actualización MAJOR desde hace ≥60 días. | Estabilidad demuestra que el conocimiento no es volátil. [Decisión] |
| Referencias: ≥1 otro documento/decisión lo referencia | Al menos un ADR, otro KO, decisión o Asset cita este KO. | Conocimiento canónico debe tener consumidores activos. [Decisión] |
| Procedencia: COMPLETE o INDIRECT | No acepta PARTIAL, UNVERIFIED ni BROKEN para Capa 3. | Conocimiento canónico debe ser plenamente trazable. [Decisión] |
| Freshness: CURRENT | El KO está dentro de su ventana de validez (no REVIEW_DUE ni STALE). | No se promueve conocimiento que podría estar desactualizado. [Decisión] |
| Conflict check: sin disputas activas | No existe otro KO marcado como `disputed` que contradiga a este. | Conocimiento con conflictos pendientes no es "gold standard". [Decisión] |

**Gate pass:** Todos los 6 criterios se cumplen → transición a `canonical`. [Decisión]

**Gate fail:** Permanece en `validated` hasta cumplir. No es urgente — la mayoría del conocimiento operativo permanece en `validated` indefinidamente. [Hecho]

---

## Gate: canonical → disputed

| Criterio | Verificación |
|----------|-------------|
| Nueva evidencia contradictoria | Existe información documentada que contradice la afirmación del KO. [Decisión] |
| Referencia a la contradicción | Se identifica la fuente o nuevo KO que contradice (knowledge_id, URL, o referencia). [Decisión] |
| **Aprobación** | No se requiere — el trigger es la evidencia misma. El fundador registra la disputa. [Decisión] |

**Nota:** Este gate es defensivo. No requiere aprobación formal porque bloquear la disputa protegería conocimiento potencialmente inválido. [Decisión]

---

## Gate: disputed → canonical (re-confirmado)

| Criterio | Verificación |
|----------|-------------|
| Re-evaluación completada | El fundador revisó la evidencia contradictoria y la comparó con la original. [Decisión] |
| Evidencia contradictoria resuelta | Se refutó, se acotó su alcance, o se incorporó sin invalidar el KO original. [Decisión] |
| Decisión documentada | Rationale de resolución en ≤3 oraciones (per [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md)). [Decisión] |
| Confianza re-afirmada | Campo `confidence` explícitamente confirmado como ALTO con justificación actualizada. [Decisión] |

---

## Gate: canonical → superseded

| Criterio | Verificación |
|----------|-------------|
| Nuevo KO existente que reemplaza | Se creó un KO nuevo con afirmación más actual/completa. [Decisión] |
| Campo `superseded_by` completado | El KO original tiene referencia al sucesor (knowledge_id). [Decisión] |
| Notificación a consumidores | Si el KO era compartido: índice compartido actualizado. [Decisión] |

---

## Gate: cualquier estado activo → deprecated

| Criterio | Verificación |
|----------|-------------|
| Validity window EXPIRED sin revalidación | El KO superó su ventana + período de gracia sin que el fundador lo revisara. [Decisión] |
| O: contexto cambió haciendo el KO irrelevante | Cambio externo documentado que invalida el KO sin contradicción directa. [Decisión] |
| Razón de deprecación | Documentada en ≤2 oraciones. [Decisión] |

---

## Gate: deprecated → archived

| Criterio | Verificación |
|----------|-------------|
| 30 días transcurridos desde deprecación | Período de gracia para que un KO sea reactivado si alguien lo necesita. [Decisión] |
| Sin solicitud de reactivación | Nadie (fundador, Lab, consumidor) pidió re-evaluar el KO. [Decisión] |
| **Aprobación** | Auto-transición — no requiere aprobación explícita. [Decisión] |

---

## Niveles de rigor por contexto

No todos los KOs requieren el mismo nivel de exigencia en los gates: [Decisión]

| Contexto | Nivel de rigor | Gates aplicables | Justificación |
|----------|---------------|-----------------|---------------|
| Lab-internal, KO operativo | Mínimo (camino rápido) | captured → validated (4 criterios) | Bajo riesgo, validez corta, consumo interno. [Decisión] |
| KO compartido cross-Lab | Estándar (todos los gates) | Todos los gates completos | Múltiples Labs dependen de él. [Decisión] |
| KO que informa decisiones financieras | Elevado | Requiere procedencia COMPLETE + confianza ALTO antes de uso | Dinero en riesgo. [Decisión] |
| KO para publicación externa | Máximo | Revisión formal (under_review) + auditoría de procedencia completa | Reputación en juego. [Decisión] |

**Quién decide el nivel de rigor:** El fundador, basado en el impacto potencial del KO. [Decisión] En nivel SOLO no hay burocracia adicional — el fundador simplemente aplica el rigor apropiado al contexto.

---

## Resumen de gates por transición

```text
captured ──── [4 criterios, ≤2 min] ────→ validated
captured ──── [razón documentada] ───────→ under_review
under_review ─ [coherencia + nota] ──────→ validated
validated ──── [6 criterios estrictos] ──→ canonical
canonical ──── [evidencia contradice] ───→ disputed
disputed ───── [resolución + ALTO] ──────→ canonical
canonical ──── [nuevo KO + ref] ─────────→ superseded
activo ─────── [expirado/irrelevante] ──→ deprecated
deprecated ─── [30 días + sin uso] ─────→ archived
```

---

## Cross-references

- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — 8 estados, matriz de transiciones
- [knowledge-object-contract.md](./knowledge-object-contract.md) — 10 campos obligatorios, validación
- [knowledge-confidence-model.md](./knowledge-confidence-model.md) — Niveles de confianza, re-evaluación
- [knowledge-provenance.md](./knowledge-provenance.md) — 5 estados de procedencia
- [knowledge-freshness.md](./knowledge-freshness.md) — Estados de freshness, validity_window
- [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md) — Proceso de resolución de disputas
- [knowledge-layers.md](./knowledge-layers.md) — Capas mapeadas a transiciones
- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 6 (proporcionalidad)
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-05 (proporcionalidad)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 6        | 11%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 47       | 89%        |
| [Visión]      | 0        | 0%         |

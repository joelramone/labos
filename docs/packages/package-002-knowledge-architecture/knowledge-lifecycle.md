# Ciclo de Vida del Conocimiento

## Propósito

Este documento define los estados posibles de un Knowledge Object y las transiciones válidas entre ellos. [Decisión] Establece qué debe ocurrir para que el conocimiento avance, retroceda o se retire del sistema, quién controla cada transición, y qué evidencia se requiere.

---

## Diagrama de estados

```text
                         ┌─────────────────────────────────────────────┐
                         │                                             │
                         ▼                                             │
┌───────────┐     ┌─────────────┐     ┌───────────┐     ┌──────────┐ │
│ captured  │────▶│ under_review│────▶│ validated │────▶│canonical │ │
│           │     │  (opcional) │     │           │     │          │ │
└───────────┘     └─────────────┘     └─────┬─────┘     └────┬─────┘ │
      │                                     │                 │       │
      │            ┌──────────┐             │                 │       │
      │            │ disputed │◄────────────┼─────────────────┘       │
      │            │          │             │                         │
      │            └────┬─────┘             │                         │
      │                 │                   │                         │
      │                 ▼                   ▼                         │
      │           ┌───────────┐     ┌────────────┐                   │
      │           │superseded │     │ deprecated │                   │
      │           │           │     │            │                   │
      │           └─────┬─────┘     └──────┬─────┘                   │
      │                 │                  │                          │
      │                 ▼                  ▼                          │
      │           ┌──────────────────────────┐                       │
      └──────────▶│        archived          │                       │
                  │                          │                        │
                  └──────────────────────────┘                        │
                         │                                            │
                         │ reactivación (raro)                        │
                         └────────────────────────────────────────────┘
```

---

## Estados

### 1. `captured` — Capturado

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Registro inicial de conocimiento. Campos obligatorios presentes. Confianza puede ser provisional. [Decisión] |
| **Capa correspondiente** | Capa 1 — Conocimiento Capturado. [Hecho] |
| **Criterios de entrada** | Cumplir campos obligatorios del [Knowledge Object Contract](./knowledge-object-contract.md). Tener al menos una afirmación sintetizada. [Decisión] |
| **Criterios de salida** | Asignar confianza con justificación + verificar coherencia → `validated`. O solicitar revisión formal → `under_review`. [Decisión] |
| **Owner** | Fundador o agente IA (con revisión humana pendiente). [Decisión] |
| **Evidencia requerida para transición** | Justificación de confianza documentada. [Decisión] |
| **Transiciones válidas** | → `under_review`, → `validated` (camino rápido), → `archived` (descarte). [Decisión] |
| **Transiciones inválidas** | → `canonical` (no puede saltar validación), → `superseded` (nunca fue validado). [Decisión] |

---

### 2. `under_review` — En revisión

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | El conocimiento está siendo evaluado formalmente. Aplica cuando la validación no es trivial o el conocimiento es de alto impacto. [Decisión] |
| **Capa correspondiente** | Transición entre Capa 1 y Capa 2. [Hecho] |
| **Criterios de entrada** | Fundador decide que requiere evaluación antes de validar. O conocimiento producido por agente IA que necesita verificación humana. [Decisión] |
| **Criterios de salida** | Revisión completada: aprobado → `validated`, rechazado → `archived`, requiere más investigación → `captured`. [Decisión] |
| **Owner** | Fundador (único revisor en nivel SOLO). [Decisión] |
| **Evidencia requerida para transición** | Nota de revisión: aprobado/rechazado + motivo en ≤2 oraciones. [Decisión] |
| **Transiciones válidas** | → `validated` (aprobado), → `captured` (devuelto para mejorar), → `archived` (rechazado). [Decisión] |
| **Transiciones inválidas** | → `canonical` (debe pasar por validated), → `disputed`, → `superseded`. [Decisión] |

**Nota de proporcionalidad:** Este estado es OPCIONAL. Per Principio 6, la mayoría del conocimiento puede ir directamente de `captured` a `validated` sin pasar por revisión formal. Usar `under_review` solo cuando la complejidad o el impacto lo justifiquen. [Decisión]

---

### 3. `validated` — Validado

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Conocimiento revisado con confianza asignada. Listo para uso operativo. Puede informar decisiones. [Decisión] |
| **Capa correspondiente** | Capa 2 — Conocimiento Validado. [Hecho] |
| **Criterios de entrada** | Confianza explícita (alto/medio/bajo) con justificación. Fuente verificada. Clasificación epistémica presente. [Decisión] |
| **Criterios de salida** | Estabilidad demostrada + referencias activas → `canonical`. O nueva evidencia contradictoria → `disputed`. O ya no relevante → `deprecated`. [Decisión] |
| **Owner** | Fundador (validación y uso). [Decisión] |
| **Evidencia requerida para transición a canonical** | ≥2 ciclos de revisión sin cambios + ≥1 referencia desde otro documento/decisión. [Decisión] |
| **Transiciones válidas** | → `canonical`, → `disputed`, → `superseded`, → `deprecated`, → `archived`. [Decisión] |
| **Transiciones inválidas** | → `captured` (no se "des-valida"; si hay problemas → `disputed`). [Decisión] |

---

### 4. `canonical` — Canónico

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Conocimiento estable de alta confianza, referenciado activamente. El gold standard del sistema. [Decisión] |
| **Capa correspondiente** | Capa 3 — Conocimiento Canónico. [Hecho] |
| **Criterios de entrada** | Confianza alta sostenida. Sin cambios en ≥60 días. ≥1 referencia activa desde otro documento. Cadena de procedencia documentada. [Decisión] |
| **Criterios de salida** | Contradicción → `disputed`. Reemplazo → `superseded`. Obsolescencia por cambio de contexto → `deprecated`. [Decisión] |
| **Owner** | Fundador (mantenimiento y protección). [Decisión] |
| **Evidencia requerida para degradación** | Evidencia nueva que contradiga o invalide + documentación del motivo. [Decisión] |
| **Transiciones válidas** | → `disputed`, → `superseded`, → `deprecated`. [Decisión] |
| **Transiciones inválidas** | → `captured` (nunca), → `under_review` (si hay duda → `disputed`), → `validated` (degradación va vía `disputed`). [Decisión] |

---

### 5. `disputed` — Disputado

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Conocimiento contradicho por nueva evidencia. Bajo re-evaluación. No debe usarse para decisiones sin advertencia explícita. [Decisión] |
| **Capa correspondiente** | Transición — sale de su capa actual hasta resolución. [Hecho] |
| **Criterios de entrada** | Nueva evidencia que contradice parcial o totalmente la afirmación del KO. [Decisión] |
| **Criterios de salida** | Re-evaluación completa: confirmado (vuelve a estado anterior), invalidado (→ `superseded` o `deprecated`), actualizado (nueva versión → el original se marca `superseded`). [Decisión] |
| **Owner** | Fundador (resolución de conflictos). [Decisión] |
| **Evidencia requerida para transición** | Documentar: qué evidencia nueva contradice + resolución + destino. [Decisión] |
| **Transiciones válidas** | → `validated` (re-confirmado), → `canonical` (re-confirmado si era canónico), → `superseded` (reemplazado), → `deprecated` (invalidado). [Decisión] |
| **Transiciones inválidas** | → `captured` (no se "des-sintetiza"), → `archived` directamente (debe pasar por deprecated o superseded). [Decisión] |

---

### 6. `superseded` — Superado

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Conocimiento reemplazado por una versión más actual o completa. Se preserva para trazabilidad histórica. [Decisión] |
| **Capa correspondiente** | Sale del sistema activo. Preservado como historial. [Hecho] |
| **Criterios de entrada** | Existe un KO nuevo que reemplaza la información de este. Campo `superseded_by` completado. [Decisión] |
| **Criterios de salida** | Solo → `archived` (almacenamiento final). [Decisión] |
| **Owner** | Fundador (decisión de reemplazo). [Decisión] |
| **Evidencia requerida para transición** | Referencia al KO que lo reemplaza (knowledge_id del sucesor). [Decisión] |
| **Transiciones válidas** | → `archived`. [Decisión] |
| **Transiciones inválidas** | → `validated`, → `canonical`, → `captured` (no se "revive" un KO superado; se crea uno nuevo). [Decisión] |

---

### 7. `deprecated` — Deprecado

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Conocimiento que ya no es válido por cambio de contexto, expiración de validez, o invalidación. No fue reemplazado — simplemente ya no aplica. [Decisión] |
| **Capa correspondiente** | Sale del sistema activo. [Hecho] |
| **Criterios de entrada** | Validity_window expirada sin revalidación. O contexto cambió haciendo el conocimiento irrelevante. O invalidado sin reemplazo. [Decisión] |
| **Criterios de salida** | Solo → `archived`. [Decisión] |
| **Owner** | Fundador o trigger automático (validity_window). [Decisión] |
| **Evidencia requerida para transición** | Motivo de deprecación en ≤2 oraciones. [Decisión] |
| **Transiciones válidas** | → `archived`. [Decisión] |
| **Transiciones inválidas** | → `validated`, → `canonical` (si se quiere "revivir", se crea KO nuevo que referencia al deprecado). [Decisión] |

---

### 8. `archived` — Archivado

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Conocimiento congelado. No se usa activamente. Preservado para auditabilidad y trazabilidad histórica. [Decisión] |
| **Capa correspondiente** | Fuera del sistema activo. Almacenamiento permanente. [Hecho] |
| **Criterios de entrada** | KO superado, deprecado, o descartado durante captura. [Decisión] |
| **Criterios de salida** | Reactivación (raro): solo si nueva evidencia hace relevante el conocimiento archivado. Vuelve a `captured` para re-evaluación. [Decisión] |
| **Owner** | Sistema (automático tras 30 días en superseded/deprecated). [Decisión] |
| **Evidencia requerida para reactivación** | Justificación de por qué el conocimiento vuelve a ser relevante + nueva evidencia. [Decisión] |
| **Transiciones válidas** | → `captured` (reactivación — excepcional). [Decisión] |
| **Transiciones inválidas** | → `validated`, → `canonical`, → `disputed` (debe pasar por captured primero). [Decisión] |

---

## Caminos típicos (happy paths)

### Camino completo (conocimiento de alto valor)

```text
captured → under_review → validated → canonical
```

Uso: Conocimiento derivado de investigación formal, alto impacto, que se espera sea estable. [Hecho]

### Camino rápido (mayoría del conocimiento)

```text
captured → validated
```

Uso: Conocimiento donde el fundador puede asignar confianza inmediatamente sin revisión formal separada. Per Principio 6, este es el camino por defecto. [Decisión]

### Camino simplificado para conocimiento operativo

```text
captured → validated (permanece aquí)
```

Uso: Conocimiento operativo con validity_window corta (7-30 días) que nunca aspirará a ser canónico. Ejemplos: configuraciones temporales, observaciones de mercado a corto plazo, notas de troubleshooting. [Decisión]

### Camino de deprecación natural

```text
captured → validated → deprecated → archived
```

Uso: Conocimiento que fue útil pero cuyo contexto cambió. Flujo natural para conocimiento en dominios dinámicos. [Hecho]

### Camino de disputa y resolución

```text
validated/canonical → disputed → validated (re-confirmado)
                               → superseded (reemplazado)
                               → deprecated (invalidado)
```

Uso: Cuando nueva evidencia contradice conocimiento existente. [Hecho]

---

## Triggers automáticos

Acciones que el sistema (o el fundador en su revisión periódica) debe ejecutar sin decisión caso a caso: [Decisión]

| Trigger | Condición | Acción |
|---------|-----------|--------|
| Alerta de validez | `validity_window` expirada Y `last_reviewed_date` > `validity_window` días | Marcar KO como "requiere revisión". Si no se revisa en 14 días adicionales → `deprecated`. [Decisión] |
| Auto-archive | KO en estado `superseded` o `deprecated` por >30 días | Mover a `archived`. [Decisión] |
| Alerta de huérfano | KO en `captured` por >30 días sin transición | Notificar: ¿validar o archivar? [Decisión] |
| Alerta de conflicto | Nuevo KO contradice KO existente en `validated` o `canonical` | Marcar el KO antiguo como candidato a `disputed`. Requiere decisión humana. [Decisión] |

**Implementación actual:** En la etapa pre-software, estos triggers se ejecutan durante la revisión mensual de conocimiento (incluida en el overhead ≤2h/mes del Principio 6). [Decisión]

---

## Matriz de transiciones

| Desde \ Hacia | captured | under_review | validated | canonical | disputed | superseded | deprecated | archived |
|---------------|----------|--------------|-----------|-----------|----------|------------|------------|----------|
| **captured** | — | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **under_review** | ✅ | — | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **validated** | ❌ | ❌ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **canonical** | ❌ | ❌ | ❌ | — | ✅ | ✅ | ✅ | ❌ |
| **disputed** | ❌ | ❌ | ✅ | ✅ | — | ✅ | ✅ | ❌ |
| **superseded** | ❌ | ❌ | ❌ | ❌ | ❌ | — | ❌ | ✅ |
| **deprecated** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | — | ✅ |
| **archived** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | — |

Leyenda: ✅ = transición válida, ❌ = transición inválida.

---

## Mapping estados ↔ capas

| Estado | Capa | Activo en el sistema |
|--------|------|---------------------|
| `captured` | Capa 1 | ✅ Sí |
| `under_review` | Transición 1→2 | ✅ Sí |
| `validated` | Capa 2 | ✅ Sí |
| `canonical` | Capa 3 | ✅ Sí |
| `disputed` | En transición (sale de capa) | ⚠️ Con advertencia |
| `superseded` | Fuera del sistema activo | ❌ No (solo historial) |
| `deprecated` | Fuera del sistema activo | ❌ No (solo historial) |
| `archived` | Almacenamiento permanente | ❌ No |

---

## Ejemplo de lifecycle completo

**(EJEMPLO: Crypto Scalping Core)**

```text
1. [2025-05-01] CAPTURED
   KO-CSC-017: "Spread BTC/USDT se ensancha 02:00-04:00 UTC"
   Confianza: bajo (solo 3 días de observación)
   validity_window: 30 días

2. [2025-05-15] VALIDATED
   Tras 15 días adicionales de datos, confianza sube a "alto".
   Evidencia: 18/20 días confirman el patrón.

3. [2025-07-20] CANONICAL
   Sin cambios en 65 días. Referenciado por:
   - Decisión: "No operar en ventana 02:00-04:00"
   - KO-CSC-023: "Ventanas óptimas de operación"
   Cadena de procedencia documentada.

4. [2025-11-01] DISPUTED
   Binance actualiza su matching engine. Nuevos datos muestran
   que el patrón se redujo a 15-20% de ensanchamiento.

5. [2025-11-10] SUPERSEDED
   Se crea KO-CSC-042 con datos post-actualización.
   KO-CSC-017.superseded_by = KO-CSC-042.

6. [2025-12-10] ARCHIVED
   Auto-archive tras 30 días en superseded.
```

---

## Cross-references

- [knowledge-layers.md](./knowledge-layers.md) — Capas mapeadas a estados
- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campo `status` usa estos valores
- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — P4 (fecha de caducidad), P6 (proporcionalidad)
- [knowledge-quality-gates.md](./knowledge-quality-gates.md) — Criterios detallados de transición (pendiente)
- [knowledge-freshness.md](./knowledge-freshness.md) — Mecanismo de validity_window (pendiente)
- [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md) — Proceso para estado `disputed` (pendiente)
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-05 (proporcionalidad)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 11       | 14%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 67       | 86%        |
| [Visión]      | 0        | 0%         |

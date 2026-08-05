# Versionado del Conocimiento

## Propósito

Este documento define cuándo y cómo se versiona un Knowledge Object, distinguiendo entre actualizaciones menores, cambios sustantivos y creación de nuevo conocimiento. [Decisión] Establece el formato de versión y las reglas de preservación histórica.

---

## Cuándo actualizar un KO existente vs crear uno nuevo

La decisión entre actualizar y crear nuevo KO depende de si la afirmación central cambia: [Decisión]

| Acción | Condición | Ejemplo (EJEMPLO: Crypto Scalping Core) |
|--------|-----------|----------------------------------------|
| **Actualizar (MINOR)** | Typo, corrección de metadata, fuente adicional sin cambiar la afirmación. | Agregar una nueva fuente que confirma el mismo hallazgo de spread nocturno. [Decisión] |
| **Actualizar (MAJOR)** | La afirmación se refina, el alcance cambia, la conclusión se actualiza. | El ensanchamiento de spread se recalcula de "40-60%" a "30-50%" tras más datos. [Decisión] |
| **Nuevo KO** | Afirmación enteramente diferente sobre un tema distinto. | Nuevo hallazgo sobre latencia de API (no es el mismo tema que spread). [Decisión] |
| **Supersede** | Nueva afirmación contradice la anterior y la reemplaza. | Nuevo KO afirma que tras update de Binance el spread nocturno ya no es significativo → KO original se marca `superseded`. [Decisión] |

**Regla fundamental:** Si la afirmación central cambia de tal forma que alguien que dependía de la versión anterior necesitaría saberlo, es un cambio MAJOR o un supersede. [Decisión]

---

## Formato de versión: MAJOR.MINOR

| Componente | Significado | Cuándo incrementa |
|-----------|-------------|-------------------|
| **MAJOR** (X) | La sustancia del conocimiento cambió. | Cambio de afirmación, alcance, conclusión o aplicabilidad. [Decisión] |
| **MINOR** (.Y) | La forma o metadata cambió, no la sustancia. | Corrección de redacción, metadata actualizada, fuente adicional sin cambiar el claim, reformateo. [Decisión] |

### Convención de inicio

- Todo KO comienza en versión **1.0**. [Decisión]
- MINOR se incrementa: 1.0 → 1.1 → 1.2 → ... [Hecho]
- MAJOR se incrementa y resetea MINOR: 1.3 → 2.0 [Hecho]

### Ejemplos de clasificación de cambio

| Cambio realizado | Tipo | Versión resultante |
|-----------------|------|-------------------|
| Corregir typo en summary | MINOR | 1.0 → 1.1 |
| Actualizar `last_reviewed_date` | MINOR | 1.1 → 1.2 |
| Agregar una nueva referencia que confirma el claim | MINOR | 1.2 → 1.3 |
| Cambiar formato del documento sin alterar contenido | MINOR | 1.3 → 1.4 |
| Refinar el porcentaje de spread de "40-60%" a "35-55%" | MAJOR | 1.4 → 2.0 |
| Cambiar el alcance temporal de "02:00-04:00" a "01:30-04:30" | MAJOR | 2.0 → 3.0 |
| Actualizar conclusión basada en nueva evidencia | MAJOR | 3.0 → 4.0 |
| Cambiar aplicabilidad de "Binance Spot" a "Binance Spot + Futures" | MAJOR | 4.0 → 5.0 |

---

## Reglas de versionado

### Obligatorias

| Regla | Descripción |
|-------|-------------|
| `last_reviewed_date` siempre se actualiza | Todo cambio de versión (MINOR o MAJOR) actualiza la fecha de última revisión. [Decisión] |
| MAJOR requiere re-evaluación de confianza | Si la afirmación cambia, la confianza asignada previamente puede no ser válida. Se re-evalúa y se actualiza la justificación. [Decisión] |
| Historial preservado (no borrado) | Las versiones anteriores se preservan como registro histórico. Nunca se eliminan versiones. [Decisión] |
| Solo una versión activa | Solo la versión más reciente tiene estado `validated` o `canonical`. Las anteriores son informativas. [Decisión] |
| Sin versiones paralelas | No se permiten dos versiones del mismo KO coexistiendo como "actuales". Si hay visiones diferentes, es un conflicto → [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md). [Decisión] |

### Condicionales

| Regla | Condición | Descripción |
|-------|-----------|-------------|
| Notificar consumidores | MAJOR en KO compartido | Si un KO compartido (PUBLIC) sufre un cambio MAJOR, los consumidores deben ser notificados vía actualización del índice compartido. [Decisión] |
| Revisar Assets derivados | MAJOR en KO canónico | Si un KO canónico que es fuente de un Asset cambia sustantivamente, evaluar si el Asset sigue siendo válido. [Decisión] |

---

## Relación con otras dimensiones

El versionado interactúa con pero no determina automáticamente otras dimensiones: [Decisión]

| Dimensión | Efecto de MINOR | Efecto de MAJOR |
|-----------|----------------|-----------------|
| **Lifecycle status** | No cambia. Un KO `validated` sigue siendo `validated` tras un MINOR. [Decisión] | No cambia automáticamente. PUEDE requerir re-evaluación por fundador. [Decisión] |
| **Confianza** | Se preserva sin cambios. [Decisión] | Se re-evalúa obligatoriamente. Puede subir, bajar o mantenerse. [Decisión] |
| **Procedencia** | Se puede agregar nueva fuente (enriquece la cadena). [Decisión] | Se actualiza la cadena con la nueva transformación aplicada. [Decisión] |
| **Freshness** | Freshness status se preserva. Timer de `validity_window` no se resetea. [Decisión] | Se resetea el timer de `validity_window` (la afirmación es "nueva" en sustancia). [Decisión] |
| **Boundary/sensibilidad** | No cambia. [Hecho] | No cambia automáticamente (pero puede revisarse). [Decisión] |

---

## Preservación histórica

### Formato de historial (etapa pre-software)

En la etapa actual, el historial se preserva como sección al final del documento del KO o como notas de cambio: [Decisión]

```markdown
## Historial de versiones

| Versión | Fecha | Tipo | Cambio |
|---------|-------|------|--------|
| 1.0 | 2025-06-15 | — | Creación inicial. |
| 1.1 | 2025-06-28 | MINOR | Agregada referencia a dataset extendido. |
| 2.0 | 2025-08-10 | MAJOR | Ajustado rango de spread de 40-60% a 35-55% por nuevos datos. |
```

### Qué se preserva

| Aspecto | Preservado | Formato |
|---------|-----------|---------|
| Afirmación de cada versión MAJOR | Sí | Texto del summary en cada versión MAJOR. [Decisión] |
| Metadata de cada versión | Sí | Fecha, tipo de cambio, motivo breve. [Decisión] |
| Contenido completo de cada versión | No requerido | Solo se preserva contenido completo para KOs canónicos si el fundador lo considera valioso. [Decisión] |

**Overhead estimado:** Mantener el historial de versiones agrega ~1 minuto por cambio (una línea en la tabla). [Hecho] Compatible con Principio 6 (proporcionalidad).

---

## Ejemplo completo

**(EJEMPLO: Crypto Scalping Core)**

```text
KO-CSC-017 — Versión actual: 2.0

Versión 1.0 (2025-06-15):
  Summary: "Spread BTC/USDT se ensancha 40-60% durante 02:00-04:00 UTC"
  Confianza: alto — 30 días de datos cuantitativos.
  
Versión 1.1 (2025-06-28):
  Cambio MINOR: Agregada referencia a dataset de julio como confirmación.
  Summary: sin cambio.
  Confianza: sin cambio.
  
Versión 2.0 (2025-08-10):
  Cambio MAJOR: Rango ajustado tras 60 días adicionales de datos.
  Summary: "Spread BTC/USDT se ensancha 35-55% durante 02:00-04:00 UTC"
  Confianza: re-evaluada → alto (base ampliada a 90 días).
  validity_window reseteada.
```

---

## Cuándo NO versionar

Algunas situaciones no requieren incremento de versión: [Decisión]

| Situación | Tratamiento |
|-----------|-------------|
| Corrección de formato sin afectar contenido ni metadata | No requiere versión. Limpieza cosmética no es cambio. [Decisión] |
| Actualización de estado lifecycle (captured → validated) | Es transición de lifecycle, no cambio de versión del contenido. [Decisión] |
| Cambio de boundary (PRIVATE → PUBLIC) | Es cambio de clasificación, no de contenido. Se refleja en metadata sin versión nueva. [Decisión] |

---

## Cross-references

- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Estados independientes del versionado
- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campo `version`, `supersedes`, `superseded_by`
- [knowledge-confidence-model.md](./knowledge-confidence-model.md) — Re-evaluación en MAJOR
- [knowledge-freshness.md](./knowledge-freshness.md) — Reset de validity_window en MAJOR
- [knowledge-provenance.md](./knowledge-provenance.md) — Actualización de cadena de procedencia
- [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md) — Versiones paralelas = conflicto
- [knowledge-sharing.md](./knowledge-sharing.md) — Notificación a consumidores en MAJOR
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-05 (proporcionalidad)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 5        | 12%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 37       | 88%        |
| [Visión]      | 0        | 0%         |

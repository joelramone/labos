# Resolución de Conflictos de Conocimiento

## Propósito

Este documento define el proceso para manejar Knowledge Objects contradictorios. [Decisión] La regla fundamental: NUNCA sobrescribir silenciosamente. Todo conflicto se detecta, registra, preserva y resuelve con documentación explícita del rationale.

---

## Principio rector

**No existe resolución automática de conflictos.** [Decisión] Cuando dos KOs se contradicen, ambos permanecen accesibles hasta que el fundador decide cuál prevalece o crea una nueva síntesis. Eliminar silenciosamente un KO contradictorio destruye trazabilidad histórica y contexto de decisión.

---

## Proceso de resolución (8 pasos)

### 1. Detectar

El conflicto se identifica durante: [Hecho]
- Investigación activa (nuevo hallazgo contradice KO existente).
- Revisión de freshness (revalidar contenido revela inconsistencia).
- Procesamiento por agente IA (síntesis detecta contradicción).
- Consumo de KO para decisión (al usar, se nota incompatibilidad).

### 2. Registrar

Marcar el KO existente como `disputed` (transición de lifecycle). [Decisión]

Documentar mínimo:
- Qué KO se disputa (knowledge_id). [Decisión]
- Qué nueva información lo contradice (referencia a fuente o nuevo KO). [Decisión]
- Fecha de detección. [Decisión]

### 3. Preservar

Ambas versiones (KO original + nueva evidencia contradictoria) permanecen accesibles. [Decisión] Ninguna se elimina ni se oculta. El estado `disputed` señala a cualquier consumidor que el contenido está bajo re-evaluación.

### 4. Comparar

Evaluar ambas afirmaciones usando los criterios de este documento: [Decisión]
- Procedencia de cada una (ref: [knowledge-provenance.md](./knowledge-provenance.md)).
- Calidad de evidencia que soporta cada afirmación.
- Recencia de la evidencia.
- Reproducibilidad de cada observación.

### 5. Clasificar

Determinar el tipo de conflicto (ver sección "Tipos de conflicto" más abajo). [Decisión] El tipo informa la estrategia de resolución adecuada.

### 6. Resolver

El fundador decide cuál afirmación prevalece, o crea una nueva síntesis que integre ambas perspectivas. [Decisión] La resolución puede ser:
- **Confirmar original:** El KO disputado se revalida. Vuelve a `validated` o `canonical`.
- **Adoptar nuevo:** Se crea nuevo KO. El original se marca `superseded`.
- **Sintetizar:** Se crea nuevo KO que reconcilia ambas afirmaciones con contexto más preciso.
- **Diferir:** Si no hay suficiente evidencia para decidir, el KO permanece `disputed` (máximo 30 días).

### 7. Documentar

Registrar la decisión con rationale en ≤3 oraciones: [Decisión]
- Qué se decidió (cuál prevalece o qué síntesis se creó).
- Por qué (criterio principal de resolución usado).
- Qué acción se toma sobre el KO original (revalidado, superseded, deprecated).

### 8. Actualizar consumidores

Notificar o actualizar referencias downstream: [Decisión]
- Otros KOs que referencian al disputado deben ser revisados.
- Decisiones basadas en el KO disputado deben re-evaluarse.
- En nivel SOLO, "notificar" significa: agregar nota en próxima revisión mensual. [Decisión]

---

## Tipos de conflicto

| Tipo | Definición | Estrategia típica |
|------|-----------|-------------------|
| **Contradicción factual** | Dos KOs hacen afirmaciones incompatibles sobre el mismo observable. [Decisión] | Comparar evidencia directamente. El de mejor procedencia y datos más recientes suele prevalecer. |
| **Mismatch de alcance** | Los KOs parecen contradecirse pero aplican a ámbitos diferentes. [Decisión] | Clarificar el alcance de cada uno. Ambos pueden ser válidos en sus contextos. No es conflicto real. |
| **Conflicto temporal** | Ambos KOs fueron verdaderos pero en momentos diferentes (el contexto cambió). [Decisión] | El más reciente prevalece para decisiones actuales. El anterior se marca `superseded` (no inválido — fue correcto en su momento). |
| **Desacuerdo metodológico** | Diferentes métodos producen diferentes conclusiones sobre el mismo tema. [Decisión] | Evaluar validez de cada método. Si ambos son válidos, documentar la discrepancia como limitación conocida. |
| **Ambigüedad terminológica** | Conflicto aparente causado por lenguaje impreciso. [Decisión] | Clarificar definiciones. Reformular los KOs con terminología precisa. Usualmente no requiere invalidar ninguno. |
| **Conflicto de decisiones** | Dos decisiones asumen conocimiento contradictorio como base. [Decisión] | Resolver el conflicto de conocimiento primero, luego evaluar si las decisiones necesitan revisión. |
| **Hipótesis no resuelta** | Dos hipótesis predicen resultados contradictorios. [Decisión] | Diseñar experimento que discrimine entre ambas. Mantener ambas como `disputed` hasta que haya evidencia. |

---

## Criterios de prioridad para resolución

Cuando dos afirmaciones compiten, estos criterios guían (pero no determinan absolutamente) cuál prevalece: [Decisión]

| Prioridad | Criterio | Racional |
|-----------|----------|----------|
| 1 | Procedencia más fuerte (COMPLETE > PARTIAL > INDIRECT) | Mejor cadena de trazabilidad = más auditable. |
| 2 | Evidencia de mayor calidad (fuentes evaluadas > claims sin evaluar) | Fuentes verificadas > afirmaciones sin soporte. |
| 3 | Evidencia más reciente (para dominios sensibles al tiempo) | En crypto/markets, datos de ayer > datos de hace 6 meses. |
| 4 | Reproducibilidad (confirmado independientemente > observación única) | Lo que se repitió en múltiples contextos es más robusto. |
| 5 | Alcance más específico (claim específica > claim general) | "X ocurre en Binance BTC/USDT 02:00-04:00 UTC" > "X ocurre en exchanges". |
| 6 | ADR o decisión del fundador aplicable | Decisiones arquitectónicas formalizadas tienen precedencia sobre claims operativas. |

**Estos criterios son GUÍA, no algoritmo.** [Decisión] El fundador puede priorizar diferente si tiene motivos documentados. El único requisito es que la decisión sea explícita con rationale.

---

## Gobernanza SOLO para conflictos

En nivel de gobernanza SOLO (1 fundador, pre-revenue): [Decisión]

| Aspecto | Regla |
|---------|-------|
| Quién decide | Fundador, directamente. Sin comité, sin votación, sin escalación. [Decisión] |
| Formato de decisión | ≤3 oraciones de rationale documentado. [Decisión] |
| Tiempo máximo en `disputed` | 30 días. Si no se resuelve en 30 días, el fundador toma la mejor decisión disponible con la evidencia existente. [Decisión] |
| Si no hay evidencia suficiente | El fundador puede: (a) diseñar un experimento para discriminar, (b) mantener ambos como "perspectivas diferentes" con alcance clarificado, (c) archivar el menos referenciado. [Decisión] |
| Documentación mínima | knowledge_id disputado + qué lo contradice + decisión + motivo en ≤3 oraciones. [Decisión] |

---

## Ejemplo de resolución

**(EJEMPLO: Crypto Scalping Core)**

```text
CONFLICTO DETECTADO:

KO existente (KO-CSC-017, canonical):
  "Spread BTC/USDT se ensancha 40-60% durante 02:00-04:00 UTC en Binance"
  Confianza: alto. Procedencia: COMPLETE. Basado en 30 días de datos (jun 2025).

Nueva evidencia (investigación CSC-R-007, oct 2025):
  "Tras actualización de matching engine de Binance (sep 2025), el ensanchamiento
  se redujo a 15-20% en la misma ventana horaria."
  Procedencia: COMPLETE (nuevos datos de API post-actualización).

CLASIFICACIÓN: Conflicto temporal.
  Ambos fueron verdaderos en su momento. El contexto cambió.

RESOLUCIÓN:
  - KO-CSC-017 → superseded (fue válido hasta sep 2025).
  - Crear KO-CSC-042 con datos actualizados post-actualización.
  - KO-CSC-017.superseded_by = KO-CSC-042.
  
RATIONALE (≤3 oraciones):
  "Binance actualizó su matching engine en septiembre 2025, reduciendo
  significativamente el ensanchamiento de spread nocturno. KO-CSC-017 era
  correcto para su período pero ya no refleja condiciones actuales. Se crea
  KO-CSC-042 con datos post-actualización."
```

---

## Prevención de conflictos

Acciones que reducen la probabilidad de conflictos silenciosos: [Decisión]

1. Al capturar nuevo KO: verificar si contradice algún KO existente en el mismo dominio. [Decisión]
2. Mantener `validity_window` apropiada al dominio (evita que KOs obsoletos permanezcan como canónicos). [Decisión]
3. Usar terminología precisa para evitar conflictos por ambigüedad. [Decisión]
4. Documentar alcance explícito de cada KO (temporalidad, contexto, limitaciones). [Decisión]

---

## Cross-references

- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Estado `disputed`, transiciones válidas
- [knowledge-provenance.md](./knowledge-provenance.md) — Procedencia como criterio de resolución
- [knowledge-confidence-model.md](./knowledge-confidence-model.md) — Confianza como criterio de resolución
- [knowledge-freshness.md](./knowledge-freshness.md) — Obsolescencia como trigger de conflicto
- [knowledge-ownership.md](./knowledge-ownership.md) — Fundador como árbitro en SOLO
- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campo `supersedes`/`superseded_by`
- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 2 (fuente única)
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Sección 6: Gobernanza SOLO

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 1        | 2%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 42       | 98%        |
| [Visión]      | 0        | 0%         |

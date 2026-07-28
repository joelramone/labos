# Procedencia del Conocimiento

## Propósito

Este documento define la cadena de procedencia (provenance) que todo Knowledge Object debe tener para ser trazable hasta su origen. [Decisión] Operacionaliza el Principio 5 (Procedencia trazable) de [knowledge-architecture-principles.md](./knowledge-architecture-principles.md).

---

## Cadena de procedencia conceptual

```text
Source → Evidence → Finding → Knowledge Object → Asset/Capability
```

| Etapa | Definición | Gestionada por |
|-------|-----------|----------------|
| **Source** | Fuente original de información (paper, API, observación). | Package 001 — [Source Evaluation](../package-001-research-methodology/007-source-evaluation.md) |
| **Evidence** | Dato con categoría y nivel de confianza. | Package 001 — [Evidence Framework](../package-001-research-methodology/006-evidence-framework.md) |
| **Finding** | Hallazgo específico derivado de investigación. | Package 001 — [Conclusion Framework](../package-001-research-methodology/017-conclusion-framework.md) |
| **Knowledge Object** | Síntesis validada con metadata completa. | Package 002 — este package |
| **Asset/Capability** | Artefacto reutilizable derivado del conocimiento. | Package 003 (futuro) |

**Importante:** Source, Evidence y Finding están definidos en Package 001. [Hecho] Este documento NO los redefine — solo establece cómo el Knowledge Object se conecta con ellos en la cadena de procedencia.

---

## Requisitos mínimos de procedencia por origen del conocimiento

### Afirmación factual de fuente externa

| Requisito | Descripción |
|-----------|-------------|
| URL o referencia de fuente | Enlace al documento, paper, API docs o recurso original. [Decisión] |
| Fecha de evaluación | Cuándo se consultó y evaluó la fuente. [Decisión] |
| Evaluación de calidad | Calificación de la fuente per Source Evaluation de Package 001 (si aplica). [Decisión] |

### Observación interna (insight operativo)

| Requisito | Descripción |
|-----------|-------------|
| Contexto de observación | Dónde y en qué circunstancias se observó. [Decisión] |
| Frecuencia | Cuántas veces se ha observado el fenómeno. [Decisión] |
| Rango de fechas | Período durante el cual se observó. [Decisión] |

### Resultado de experimento

| Requisito | Descripción |
|-----------|-------------|
| ID del experimento | Referencia al experimento formal (ref: Package 001 — [Experiment Design](../package-001-research-methodology/014-experiment-design.md)). [Decisión] |
| Referencia a metodología | Método usado, documentado o referenciado. [Decisión] |
| Referencia a resultados | Datos o evidencia producida por el experimento. [Decisión] |

### Decisión del fundador

| Requisito | Descripción |
|-----------|-------------|
| Contexto de la decisión | Qué problema se estaba resolviendo. [Decisión] |
| Alternativas consideradas | Qué otras opciones se evaluaron (≥1 alternativa). [Decisión] |

### Hipótesis

| Requisito | Descripción |
|-----------|-------------|
| Base de la hipótesis | Qué observación, dato o intuición fundamenta la hipótesis. [Decisión] |
| Plan de validación | Cómo se planea confirmar o refutar (puede ser "pendiente de definir"). [Decisión] |

### Síntesis generada por agente IA

| Requisito | Descripción |
|-----------|-------------|
| Herramienta utilizada | Qué agente/modelo/tool generó la síntesis. [Decisión] |
| Contexto del prompt | Qué instrucción o contexto se le dio al agente. [Decisión] |
| Estado de verificación humana | Si el fundador revisó y confirmó el contenido: `verified` / `pending` / `rejected`. [Decisión] |

### Conocimiento importado de otra fuente

| Requisito | Descripción |
|-----------|-------------|
| Fuente original | De dónde proviene el conocimiento antes de importarlo. [Decisión] |
| Transformación aplicada | Qué síntesis, traducción o adaptación se realizó. [Decisión] |
| Importador | Quién realizó la importación (fundador, agente IA, etc.). [Decisión] |

### Conocimiento operacional

| Requisito | Descripción |
|-----------|-------------|
| Frecuencia de observación | Cuántas veces se ha confirmado en la operación. [Decisión] |
| Última fecha confirmada | Cuándo fue la última vez que se verificó como vigente. [Decisión] |

---

## Preguntas que toda cadena de procedencia debe permitir responder

Todo KO debe permitir determinar: [Decisión]

1. **¿De dónde vino la afirmación?** — Fuente original identificable.
2. **¿Qué evidencia la soporta?** — Referencias a evidencia evaluada.
3. **¿Qué transformaciones ocurrieron?** — Desde dato crudo hasta síntesis final.
4. **¿Quién o qué produjo la síntesis?** — Humano, agente IA o combinación.
5. **¿La fuente original sigue accesible?** — Verificable o declarada como inaccesible.
6. **¿La cadena de procedencia está completa?** — Sin saltos ni eslabones faltantes.

Si alguna de estas preguntas no puede responderse, la procedencia es incompleta. [Hecho]

---

## Estados de procedencia

| Estado | Definición | Acción requerida |
|--------|-----------|------------------|
| **COMPLETE** | Cadena completa documentada desde fuente original hasta KO. Todo eslabón verificable. [Decisión] | Ninguna — estado óptimo. |
| **PARTIAL** | Algunos eslabones documentados, pero existen gaps identificados. [Decisión] | Documentar qué gaps existen. Aceptable para Capa 1-2. |
| **INDIRECT** | El KO referencia una síntesis que a su vez referencia fuentes (≥2 hops). [Decisión] | Aceptable si la síntesis intermedia es verificable. |
| **UNVERIFIED** | Se afirma procedencia pero no se ha verificado que las fuentes existan/sean accesibles. [Decisión] | Verificar en próxima revisión. Flag para Capa 2+. |
| **BROKEN** | Una fuente referenciada ya no es accesible (URL rota, paper retractado, etc.). [Decisión] | Buscar fuente alternativa o degradar confianza del KO. |

---

## Procedencia mínima por capa

| Capa | Estado mínimo aceptable | Justificación |
|------|------------------------|---------------|
| Capa 1 — Capturado | PARTIAL o superior | En captura, basta con identificar la fuente sin cadena completa. [Decisión] |
| Capa 2 — Validado | PARTIAL con gaps documentados | La validación requiere saber qué soporta la afirmación. [Decisión] |
| Capa 3 — Canónico | COMPLETE o INDIRECT | Conocimiento canónico exige trazabilidad completa o declarada. [Decisión] |

---

## Impacto de procedencia en confianza

La procedencia influye en la confianza del KO pero no la determina unilateralmente: [Decisión]

| Procedencia | Efecto en confianza |
|-------------|-------------------|
| COMPLETE | Soporta confianza alta (si la evidencia es sólida). |
| PARTIAL | Limita confianza a media como máximo (gaps no cubiertos). |
| INDIRECT | Aceptable para confianza media-alta (depende de la calidad del intermediario). |
| UNVERIFIED | Limita confianza a baja hasta verificación. |
| BROKEN | Requiere degradación de confianza — la base del conocimiento ya no es verificable. |

Referencia: [knowledge-confidence-model.md](./knowledge-confidence-model.md) para el modelo completo de confianza.

---

## Ejemplo de cadena completa

**(EJEMPLO: Crypto Scalping Core)**

```text
KO-CSC-017: "Spread BTC/USDT se ensancha 40-60% durante 02:00-04:00 UTC"

Cadena de procedencia:
1. SOURCE: Binance WebSocket API (orderbook real-time)
   - Tipo: API pública, datos de primera mano
   - Accesible: Sí (api.binance.com)
   
2. EVIDENCE: Dataset binance-btcusdt-spread-jun2025.csv
   - 30 días de datos tick-by-tick
   - Evaluación: fuente primaria, datos cuantitativos verificables
   
3. FINDING: Research CSC-R-003, Conclusión #2
   - "El spread se ensancha consistentemente en ventana 02:00-04:00 UTC"
   - Método: análisis estadístico de distribución por hora
   
4. KNOWLEDGE OBJECT: KO-CSC-017
   - Síntesis: Afirmación cuantificada (40-60%) con periodo de observación
   - Confianza: alto (30 días consecutivos, 85% de días confirman)

Estado de procedencia: COMPLETE
```

---

## Mantenimiento de procedencia

### Cuándo verificar procedencia

- Al promover de Capa 1 a Capa 2 (verificar que fuentes existen). [Decisión]
- Al promover de Capa 2 a Capa 3 (verificar cadena completa). [Decisión]
- Durante revisión periódica de freshness (verificar que fuentes siguen accesibles). [Decisión]
- Cuando se detecta que una fuente fue retractada o actualizada significativamente. [Decisión]

### Procedencia rota: proceso de manejo

1. Marcar procedencia como BROKEN con fecha de detección. [Decisión]
2. Buscar fuente alternativa equivalente (≤15 minutos de esfuerzo). [Decisión]
3. Si se encuentra alternativa: actualizar referencia, mantener nota de cambio. [Decisión]
4. Si NO se encuentra: degradar confianza del KO y considerar si sigue siendo útil. [Decisión]
5. Si el KO pierde toda base verificable: candidato a `deprecated`. [Decisión]

---

## Cross-references

- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 5 (Procedencia trazable)
- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campos `source_reference`, `evidence_references`, `provenance_chain`
- [knowledge-confidence-model.md](./knowledge-confidence-model.md) — Impacto de procedencia en confianza
- [knowledge-freshness.md](./knowledge-freshness.md) — Verificación de accesibilidad durante revisión
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Procedencia como criterio de promoción
- [Package 001 — Evidence Framework](../package-001-research-methodology/006-evidence-framework.md) — Definición de Evidence
- [Package 001 — Source Evaluation](../package-001-research-methodology/007-source-evaluation.md) — Evaluación de fuentes
- [Package 001 — Conclusion Framework](../package-001-research-methodology/017-conclusion-framework.md) — Definición de Finding

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 2        | 5%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 40       | 95%        |
| [Visión]      | 0        | 0%         |

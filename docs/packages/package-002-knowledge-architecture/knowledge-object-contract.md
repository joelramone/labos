# Contrato del Knowledge Object

## Propósito

Este documento define la unidad atómica de conocimiento dentro de LabOS: el **Knowledge Object**. [Decisión] No es un esquema de base de datos ni una especificación de API — es un contrato conceptual que establece qué información mínima constituye un registro de conocimiento válido, qué información adicional añade rigor, y qué metadata será necesaria para implementación futura.

---

## Definición conceptual

> **Knowledge Object** = Registro documentado de una pieza de conocimiento sintetizado que cumple los principios de la arquitectura del conocimiento: tiene clasificación epistémica, confianza explícita, fuente trazable y ventana de validez definida. [Decisión]

Un Knowledge Object NO es:
- Un bookmark o enlace sin síntesis. [Hecho]
- Una nota mental o reminder. [Hecho]
- Un dato crudo sin contextualización. [Hecho]
- Una copia de información de otra fuente sin valor añadido. [Hecho]

Un Knowledge Object SÍ es:
- Una afirmación sintetizada con contexto suficiente para ser útil sin explicación adicional. [Decisión]
- Autocontenido: se entiende sin necesidad de leer toda la investigación de origen. [Decisión]
- Referenciable: tiene identidad única y puede ser citado por otros documentos. [Decisión]
- Temporal: tiene fecha de creación y horizonte de validez. [Decisión]

---

## Campos obligatorios (mínimo viable)

Estos campos son el **mínimo requerido** para que un registro sea considerado Knowledge Object válido. [Decisión] Un fundador solo NECESITA estos campos para operar. El overhead de registrar un Knowledge Object con solo campos obligatorios no debe exceder 5 minutos. [Decisión]

| Campo | Tipo | Descripción | Restricciones |
|-------|------|-------------|---------------|
| `knowledge_id` | Identificador | Identificador único del Knowledge Object. | Formato: `KO-{LAB}-{NNN}` donde LAB es abreviatura del Lab y NNN es secuencial. [Decisión] |
| `title` | Texto | Título descriptivo que permite entender el contenido sin abrirlo. | ≤80 caracteres. [Decisión] |
| `summary` | Texto | Síntesis de la afirmación principal — qué se sabe y por qué importa. | 1-3 oraciones. Debe ser autocontenido. [Decisión] |
| `type` | Enumeración | Clasificación funcional del conocimiento. | Uno de: `finding`, `methodology`, `decision-context`, `market-insight`, `technical-insight`, `operational`. [Decisión] |
| `domain` | Referencia | Lab que produjo este conocimiento. | Nombre canónico del Lab (ref: Portfolio Model). [Decisión] |
| `confidence` | Compuesto | Nivel de confianza + justificación. | Nivel: `alto` / `medio` / `bajo`. Justificación: ≥1 oración. [Decisión] |
| `status` | Enumeración | Estado actual en el lifecycle. | Valores definidos en [knowledge-lifecycle.md](./knowledge-lifecycle.md). [Decisión] |
| `source_reference` | Referencia | Link o identificador de la investigación o fuente de origen. | Research_ID, URL, o referencia a documento interno. [Decisión] |
| `created_date` | Fecha | Fecha de creación del Knowledge Object. | Formato: YYYY-MM-DD. [Decisión] |
| `validity_window` | Número | Tiempo estimado de vigencia en días. | Entero positivo. Referencia: Principio 4 (fecha de caducidad). [Decisión] |

### Tipos de Knowledge Object

| Tipo | Definición | Ejemplo típico |
|------|-----------|----------------|
| `finding` | Hallazgo factual derivado de investigación. | "El spread promedio en Binance BTC/USDT es 0.02% en horario asiático." |
| `methodology` | Método o proceso probado que puede reutilizarse. | "Para evaluar latencia de exchanges, usar ping TCP al endpoint de WebSocket desde 3 regiones." |
| `decision-context` | Contexto que informa una decisión sin ser la decisión misma. | "Los fees de maker en Binance son 0.02% vs 0.05% en Coinbase — factor relevante para estrategia de scalping." |
| `market-insight` | Comprensión sobre comportamiento de mercado o usuarios. | "El volumen de trading en LATAM se concentra 70% en BTC y ETH — diversificar pares tiene ROI decreciente." |
| `technical-insight` | Comprensión técnica sobre herramientas, infraestructura o código. | "WebSocket de Binance desconecta silenciosamente tras 24h — requiere reconexión automática con backoff." |
| `operational` | Conocimiento de trabajo diario — procesos, observaciones repetidas. | "Los deploys de viernes generan 3x más incidentes que los de martes-miércoles." |

---

## Campos opcionales (rigor adicional)

Estos campos **añaden valor** pero no son requeridos para cada Knowledge Object. [Decisión] Se recomienda completarlos para conocimiento en Capa 2 (validado) y se consideran deseables para Capa 3 (canónico). No completarlos no invalida el Knowledge Object.

| Campo | Tipo | Descripción | Cuándo usarlo |
|-------|------|-------------|---------------|
| `author_or_agent` | Texto | Quién creó este KO: fundador, agente IA específico, o colaborador. | Cuando ≥1 agente IA participa en la captura o síntesis. [Decisión] |
| `evidence_references` | Lista | Referencias a evidencia específica que soporta la afirmación. | Cuando la afirmación se basa en múltiples fuentes verificables. [Decisión] |
| `provenance_chain` | Lista | Secuencia: fuente original → investigación → síntesis → este KO. | Para conocimiento canónico (Capa 3) donde la trazabilidad completa importa. [Decisión] |
| `sensitivity` | Enumeración | Clasificación de visibilidad per boundaries. | Valores: `lab-private` (default) / `lab-published` / `labos-shared`. Ref: [knowledge-boundaries.md](./knowledge-boundaries.md). [Decisión] |
| `version` | Texto | Versión del contenido (no del formato). | Cuando el conocimiento ha sido actualizado desde su primera creación. [Decisión] |
| `supersedes` | Referencia | KO anterior que este reemplaza. | Cuando se crea una versión actualizada de conocimiento existente. [Decisión] |
| `superseded_by` | Referencia | KO posterior que reemplaza a este. | Cuando este KO es reemplazado (se actualiza el antiguo). [Decisión] |
| `related_entities` | Lista | Otros KOs, Assets, Research, o Decisions relacionados. | Cuando existen conexiones explícitas con otras entidades del ecosistema. [Decisión] |
| `intended_consumers` | Lista | Quién se espera que use este conocimiento. | Cuando el conocimiento es específico para ciertos labs o roles. [Decisión] |
| `reuse_restrictions` | Texto | Restricciones sobre cómo puede reutilizarse. | Cuando el conocimiento tiene limitaciones de contexto (e.g., "solo válido para exchanges CEX"). [Decisión] |
| `last_reviewed_date` | Fecha | Última vez que se revisó la vigencia del contenido. | Para conocimiento en Capa 2+ que requiere revalidación periódica. [Decisión] |

---

## Metadata operativa (implementación futura)

Estos campos son para **software futuro** — agentes IA, sistemas de búsqueda, integraciones. [Visión] NO se requieren en la etapa actual. Se documentan aquí para que la arquitectura los prevea sin forzar su implementación prematura.

| Campo | Tipo | Descripción | Trigger de activación |
|-------|------|-------------|----------------------|
| `retrieval_tags` | Lista | Tags para búsqueda semántica y filtrado automatizado. | Cuando se implemente un sistema de búsqueda de conocimiento. [Visión] |
| `embedding_status` | Enumeración | Si el KO ha sido vectorizado para búsqueda semántica. | Valores futuros: `pending` / `embedded` / `failed`. Trigger: implementación de RAG. [Visión] |
| `agent_access_level` | Enumeración | Qué nivel de acceso tienen agentes IA a este KO. | Valores futuros: `read` / `cite` / `synthesize` / `none`. Trigger: agentes consumiendo conocimiento autónomamente. [Visión] |

---

## Campos por capa

La proporción de campos completados varía por capa per Principio 6 (proporcionalidad): [Decisión]

| Capa | Campos obligatorios | Campos opcionales esperados | Metadata operativa |
|------|--------------------|-----------------------------|-------------------|
| Capa 1 — Capturado | ✅ Todos (10 campos) | 0-2 campos | ❌ No requeridos |
| Capa 2 — Validado | ✅ Todos (10 campos) | 3-6 campos recomendados | ❌ No requeridos |
| Capa 3 — Canónico | ✅ Todos (10 campos) | 6-11 campos deseables | ⚠️ Cuando estén disponibles |

---

## Ejemplo completo

**(EJEMPLO: Crypto Scalping Core)**

```markdown
# KO-CSC-017: Spread nocturno BTC/USDT en Binance

## Campos obligatorios
- knowledge_id: KO-CSC-017
- title: Spread BTC/USDT se ensancha 40-60% durante 02:00-04:00 UTC en Binance
- summary: El spread del par BTC/USDT en Binance Spot se ensancha
  consistentemente entre 02:00-04:00 UTC, con incrementos del 40-60%
  respecto al promedio diario. Observado en 85% de los días durante
  30 días de monitoreo.
- type: finding
- domain: Crypto Scalping Core
- confidence: alto — basado en 30 días consecutivos de datos
  cuantitativos del orderbook de Binance.
- status: validated
- source_reference: Research CSC-R-003 (Análisis de microestructura
  de mercado BTC/USDT)
- created_date: 2025-06-15
- validity_window: 90 (condiciones de mercado crypto cambian rápido)

## Campos opcionales (completados por ser Capa 2)
- evidence_references:
  - Dataset: binance-btcusdt-spread-jun2025.csv
  - Notebook: spread-analysis-v2.ipynb
- sensitivity: lab-private
- related_entities:
  - KO-CSC-012 (Latencia óptima para scalping)
  - Decision: "Evitar operaciones 02:00-04:00 UTC"
- intended_consumers: Crypto Scalping Core
- last_reviewed_date: 2025-07-10
```

---

## Validación de un Knowledge Object

Un Knowledge Object es **válido** cuando: [Decisión]

1. Todos los campos obligatorios están presentes y no vacíos.
2. El `type` es uno de los 6 valores definidos.
3. El `confidence` incluye nivel Y justificación (no solo el nivel).
4. El `summary` es autocontenido (se entiende sin contexto adicional).
5. El `source_reference` es verificable (el recurso referenciado existe).

Un Knowledge Object es **inválido** cuando: [Hecho]

1. Falta algún campo obligatorio.
2. El `summary` es una copia textual de una fuente sin síntesis propia.
3. El `confidence` no tiene justificación.
4. No existe conexión verificable entre la afirmación y alguna fuente.

---

## Convención de formato

En la etapa actual (pre-software), los Knowledge Objects se almacenan como documentos Markdown individuales o como entradas en un registro centralizado por Lab. [Decisión] El formato exacto de almacenamiento es decisión operativa del Lab, siempre que cumpla con los campos obligatorios definidos aquí.

Formatos válidos: [Decisión]
- 1 archivo Markdown por Knowledge Object (recomendado para Capa 3).
- Tabla en un documento maestro por Lab (aceptable para Capa 1-2).
- Entrada en Obsidian/Notion con los campos como properties (aceptable).

---

## Cross-references

- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principios 1-7 que informan este contrato
- [knowledge-layers.md](./knowledge-layers.md) — Campos por capa
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Valores de `status`
- [knowledge-boundaries.md](./knowledge-boundaries.md) — Valores de `sensitivity`
- [Package 001 — Evidence Framework](../package-001-research-methodology/006-evidence-framework.md) — Fuente de `evidence_references`
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-01 (clasificación epistémica), INV-05 (proporcionalidad)
- [ADR-0001](../../decisions/0001-terminology-hierarchy.md) — Knowledge como extensión del glosario

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 7        | 12%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 45       | 78%        |
| [Visión]      | 6        | 10%        |

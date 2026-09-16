# Contrato Conceptual del Asset Registry

## Naturaleza

[Decisión] El Asset Registry es un contrato documental technology-independent. No es database, API, service, UI ni runtime. Puede operarse manualmente como Markdown o archivo estructurado, sin seleccionar implementación.

## Tier 1 — Candidate intake

Exactamente ocho campos aportados por el owner:

| # | Campo | Validación |
|---:|---|---|
| 1 | nombre | ≤80 caracteres; único en el Lab |
| 2 | tipo | Uno de siete tipos canónicos |
| 3 | descripción | ≤500 caracteres; 1–3 oraciones |
| 4 | hipótesis_de_uso | Usuario objetivo + contexto |
| 5 | content_state | borrador, validado o productizado |
| 6 | originating_Lab | Identificador de Lab válido |
| 7 | source_of_truth | Una ubicación canónica verificable |
| 8 | provenance | KO, research_id o fuente externa verificable |

El registro asigna un `asset_id` provisional; no es un noveno campo manual. [Decisión]

## Tier 2 — Promotion preparation

Exactamente ocho campos adicionales, completados o referenciados sin reingresar Tier 1:

| # | Campo | Regla |
|---:|---|---|
| 1 | estado_lifecycle | Uno de siete estados; independiente de content_state |
| 2 | versión | 1.0.0 al promover; MAJOR.MINOR.PATCH |
| 3 | Asset_Owner | Identidad humana |
| 4 | fecha_de_creación | ISO 8601; preserva fecha original de intake |
| 5 | nivel_de_compartición | sharing_scope válido |
| 6 | consumption_state | NO_ACTIVE_EXTERNAL_CONSUMERS o ACTIVE_EXTERNAL_CONSUMERS |
| 7 | dimensiones_calificación | Cinco resultados + fecha/evidencia |
| 8 | aprobación_fundador | Decisor, fecha, Asset y justificación |

El ID provisional se consolida como definitivo `{LAB}-{TIPO}-{NNN}` o equivalente sin duplicarse como campo. [Decisión]

## Tier 3 — Metadata opcional/condicional

`consumidores_activos`, `product_attachments`, `dependencias`, `sensibilidad`, `licensing`, `fecha_última_revisión`, `quality_status`, `costo_de_mantenimiento_estimado` y `revenue_thesis` cuando corresponda. Ninguno sustituye Tier 1/2 ni crea Product Factory.

## Autoridad y operaciones

| Operación | Autoridad | Evidencia |
|---|---|---|
| Crear Candidate | Asset_Owner | Tier 1 completo |
| Actualizar metadata | Asset_Owner | Entrada histórica |
| Cambiar lifecycle | Verificación + decisión humana aplicable | Gate/approval record |
| Cambiar sharing_scope | Asset_Owner + Fundador | Aprobación |
| Eliminar registro | Prohibido | REJECTED/ARCHIVED se preservan |

## Duplicados, historia y triggers

[Decisión] Duplicación con VALIDATED/CANONICAL bloquea validación y exige decidir versión, derived Asset o rechazo. Cada cambio registra timestamp, campo, valor anterior/nuevo y autor; el historial es inmutable. `review_required`, source inaccesible, Forma B a 90 días, dos ciclos sin uso y DEPRECATED >180 días generan flags/alertas, no transiciones automáticas.

## Auditoría de cardinalidad y neutralidad

| Control | Resultado |
|---|---|
| Tier 1 owner fields | 8 |
| Tier 2 additional fields | 8 |
| asset_id duplicado | No |
| content_state derivado de lifecycle | No |
| consumption_state derivado de scope | No |
| Database/API/service seleccionado | No |
| Historial eliminable | No |

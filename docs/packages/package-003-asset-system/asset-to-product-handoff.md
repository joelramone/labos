# Handoff Asset → Product

## Scope boundary

[Decisión] Package 003 termina en eligibility y dependency declaration. Package 004 —no autorizado— gobernará cualquier Product real. No todo Asset se convierte en Product input; un Product futuro puede depender de múltiples Assets.

## Asset readiness

Un handoff es elegible únicamente si:

| Criterio | Verificación Package 003 |
|---|---|
| Lifecycle | CANONICAL |
| Stability | Sin MAJOR en últimos 30 días |
| Ownership | Exactamente un Asset_Owner humano |
| Product relevance | Uso propuesto y tipo de contribución documentados |
| Revenue_Thesis | Solo verificar presencia de los tres campos exigidos por R14; no definir ni validar estrategia comercial |
| Maintainability | ≥1 review en últimos 90 días; maintainer/support expectation |
| Licensing/sensitivity | Compatibles con uso propuesto |
| Version compatibility | Versión y rango/expectativa declarados |
| Dependencies | Assets/Labs dependientes identificados |

Falla de cualquier criterio rechaza el attachment indicando gaps; no cambia lifecycle. [Decisión]

## Dependency declaration

| Campo | Regla |
|---|---|
| product_id futuro | Referencia externa; Package 003 no lo crea |
| fecha | ISO 8601 |
| contribution_type | core, supporting u optional |
| asset_version | Versión referenciada |
| Product-critical | Sí para core; explícito para otros casos |
| dependientes afectados | Products/Labs conocidos |
| support expectation | Maintainer, cadencia y límites |
| exit conditions | Removal, replacement, migration o deprecation impact |

## Tipos de contribución

| Tipo | Significado | MAJOR/deprecation |
|---|---|---|
| core | Dependencia indispensable | Impact y migration obligatorios |
| supporting | Mejora no indispensable | Impact requerido; migration recomendada |
| optional | Removible sin degradación | Notificación informativa según riesgo |

## Ownership y cambios

[Decisión] product_attachment no transfiere ownership ni Canonical_Authority. Antes de MAJOR, supersession o deprecation se registra Product/Asset impact, acción (migration/replacement/removal) y confirmación del Asset_Owner. El Asset history permanece intacto.

## Exit conditions del handoff

Package 003 entrega: readiness result, dependency record, restrictions, owner, version y support expectation. Se detiene ahí. [Decisión]

## Explicit non-scope

No define Product lifecycle, pricing, segmentation, revenue mechanisms, sales, Product governance, customer acquisition, Product architecture ni Product Factory. No crea Product ni valida demanda. [Decisión]

## Validación boundary

| Control | Resultado |
|---|---|
| Contribution types | 3/3 |
| Ownership transferred | No |
| MAJOR/deprecation impact required | Sí |
| Product lifecycle defined | No |
| Package 004 initiated | No |
| Product created | No |


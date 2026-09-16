# Quality Gates por Exposición y Riesgo

## Modelo

[Decisión] El rigor resulta de `base exposure + risk override`. `sharing_scope` registra autorización; `consumption_state` registra consumo efectivo. No son equivalentes.

## Niveles de exposición

| Nivel | Clasificación exhaustiva | Gates base |
|---|---|---|
| 1 | `NO_ACTIVE_EXTERNAL_CONSUMERS`, sin dependencias de otros Labs, sin `product_attachment`, scope distinto de Public; incluye Lab-Private y LabOS-Shared autorizado todavía no consumido | Cinco dimensiones R4; validación base; Fast Path elegible según riesgo/calidad |
| 2 | Consumer externo activo o dependencia de otro Lab; scope Lab-Published/LabOS-Shared/Cross-Lab; sin attachment y no Public | Nivel 1 + uso documentado, licencia, sensibilidad y mantenibilidad |
| 3 | `product_attachment` activo o sharing_scope Public | Nivel 2 + estabilidad ≥30 días sin MAJOR, ownership, plan de mantenimiento y análisis de impacto |

[Decisión] Cambiar scope por sí solo no demuestra consumo. Un Asset LabOS-Shared con `NO_ACTIVE_EXTERNAL_CONSUMERS`, sin dependencias/attachment y no Public puede permanecer Nivel 1 después de superar separadamente los gates que autorizaron ese scope.

## Risk override

| Factor | Override mínimo |
|---|---|
| Datos externos/licenciados | Sensibilidad y licensing, aunque sea Nivel 1 |
| Impacto financiero | Review elevado y evidencia explícita; no afirmar rentabilidad |
| Seguridad/autenticación | Sensibilidad y control humano elevados |
| Clientes externos | Gates Nivel 3 apropiados al impacto |

[Decisión] El override eleva gates; no cambia lifecycle ni crea un cuarto nivel. Risk evaluation nunca se omite en Fast Path.

## Gates por transición/acción

| Acción | Gate |
|---|---|
| CANDIDATE → UNDER_REVIEW | Cinco dimensiones obligatorias SATISFECHAS |
| UNDER_REVIEW → VALIDATED | Cinco campos base verificados, escenario concreto y sin duplicación |
| VALIDATED → CANONICAL Nivel 1 | Aprobación explícita; Fast Path permitido si cumple todo el contexto |
| VALIDATED → CANONICAL Nivel 2 | Nivel 1 + uso, licencia, sensibilidad y mantenibilidad |
| VALIDATED → CANONICAL Nivel 3 | Nivel 2 + estabilidad, ownership, mantenimiento e impacto |
| CANONICAL → Cross-Lab/Public | Autorización humana + documentación/licencia/sensibilidad/mantenibilidad |
| CANONICAL → product_attachment futuro | Eligibility Nivel 3 y análisis de dependencias; no crea Product |

## Fast Path

[Decisión] Requiere Nivel 1 efectivo, cinco dimensiones R4, reference de uso/aplicación interna, risk override evaluado y aprobación única del Fundador. Reduce documentación y actos separados; no elimina dimensiones, no depende solo de Lab-Private y no permite `AUTO_PROMOTE`.

## Gate failure

1. Rechazar la transición.
2. Nombrar criterios fallidos.
3. Conservar estado y metadata.
4. Permitir remediación y reintento.
5. Solo el Fundador puede determinar irremediabilidad y REJECTED.

## Matriz de clasificación

| Caso | Base | Override | Resultado |
|---|---|---|---|
| Lab-Private, sin consumers/deps/attachment | Nivel 1 | Ninguno | Fast Path posible |
| LabOS-Shared, sin consumers/deps/attachment | Nivel 1 | Ninguno | Fast Path posible; scope ≠ consumo |
| Consumer externo activo | Nivel 2 | Según riesgo | Gates elevados |
| Public o attachment | Nivel 3 | Según riesgo | Gates máximos |
| Dataset externo sin consumers | Nivel 1 | Licensing | Nivel 1 con gates elevados por riesgo |

## Validación

| Control | Resultado |
|---|---|
| Niveles | 3/3 |
| LabOS-Shared no consumido clasificable Nivel 1 | Sí |
| Risk override | Presente |
| Dimensiones Fast Path omitidas | 0 |
| Scope confundido con consumo | No |
| Promoción automática | Prohibida |

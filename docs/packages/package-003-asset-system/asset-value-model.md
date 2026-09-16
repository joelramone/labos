# Modelo de Valor del Asset

## Clasificación global

| Estado | Evidencia | Decisión vinculada |
|---|---|---|
| DEMOSTRADO | Uso real por alguien distinto del creator o aplicación concreta verificable con fecha | Mayor prioridad de mantenimiento |
| PROYECTADO | Usuario específico, escenario concreto y razón documentada de demanda esperada | Revisar en próximo ciclo; no tratar como uso real |
| INDETERMINADO | No satisface DEMOSTRADO ni PROYECTADO | A >90 días: deprecar o asignar acción ≤30 días |

## Ocho dimensiones

| Dimensión | Pregunta observable | Evidencia aceptable |
|---|---|---|
| Frecuencia de reutilización | ¿Cuántas veces se usó en el ciclo? | Registros fechados de consumo |
| Tiempo ahorrado | ¿Qué esfuerzo evitó? | Estimación documentada del consumer/owner |
| Mejora de calidad | ¿Mejoró el resultado frente a la alternativa? | Comparación o testimonio |
| Reducción de riesgo | ¿Qué error, inconsistencia o pérdida evitó? | Caso verificable |
| Adopción cross-Lab | ¿Cuántos Labs externos al origen lo referencian? | Registro de consumers |
| Contribución a Product | ¿Existe attachment futuro activo? | Metadata de attachment; no crea Product |
| Valor de aprendizaje | ¿Preserva conocimiento reusable? | Cadena de provenance |
| Costo de mantenimiento | ¿Cuántas horas/mes consume? | Registro del owner |

[Decisión] Cada dimensión usa alto/medio/bajo/no-aplica con evidencia citada. Se prohíben scores compuestos, rankings ponderados y falsa precisión. Revenue no es requisito para demostrar aprendizaje, reuse, calidad o reducción de riesgo.

## Registro de evaluación

Fecha, clasificación global, al menos una referencia de evidencia y dimensiones aplicables. La evaluación informa prioridad y deprecación; no cambia lifecycle automáticamente. [Decisión]

## Matriz evidencia–estado

| Caso | Estado permitido |
|---|---|
| Uso verificable fuera del creator/contexto | DEMOSTRADO |
| Solo hipótesis completa de demanda | PROYECTADO |
| Afirmación genérica sin usuario/escenario/evidencia | INDETERMINADO |
| Revenue = 0 pero aprendizaje verificable | Puede ser DEMOSTRADO |

## Validación

| Control | Resultado |
|---|---|
| Dimensiones | 8/8 |
| Estados | 3/3 |
| Revenue obligatorio | No |
| Score compuesto | Prohibido |
| Evidencia por evaluación | Obligatoria |

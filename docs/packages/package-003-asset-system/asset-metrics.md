# Métricas Operativas del Asset System

## Contrato del ciclo

[Decisión] Cada registro identifica fecha y ciclo de revisión de 30–180 días. En contexto SOLO, el ciclo recomendado es 90 días y el registro manual no debe exceder 60 minutos por ciclo mientras el portfolio sea manejable.

## Siete métricas

| # | Métrica | Input observable fechado | Acción vinculada |
|---:|---|---|---|
| 1 | Candidates creados | Registros CANDIDATE creados en el ciclo | Si 0 por dos ciclos, revisar cumplimiento Asset_First_Model |
| 2 | Assets promovidos a CANONICAL | Transiciones aprobadas en el ciclo | Si 0 sostenido, revisar gates; nunca relajar automáticamente |
| 3 | Assets REJECTED | Decisiones REJECTED con motivo | Si elevado, revisar intake/calidad |
| 4 | Assets reutilizados por otro Lab | Referencias de consumo externo con Lab, fecha y versión | Evidencia de valor demostrado |
| 5 | product_attachments activos | Attachments registrados al cierre | Indicador futuro; no crea Products |
| 6 | Assets DEPRECATED | Registros actualmente DEPRECATED | Si crece sin resolución, revisar migración/archivo |
| 7 | Horas de mantenimiento | Horas registradas por Asset durante el ciclo | Si supera límite proporcional, priorizar o evaluar deprecación |

[Decisión] No se usan totales acumulativos sin ciclo ni acción, ni métricas para premiar volumen por sí mismo.

## Triggers

- LabOS-Shared/Cross-Lab/Public sin reutilización externa por dos ciclos: marcar para evaluación de deprecación.
- Lab-Private/Lab-Published sin uso dentro del originating_Lab por dos ciclos: misma marca.
- Reutilización documentada antes del siguiente ciclo remueve la marca.
- Una marca solicita evaluación; no depreca automáticamente.

## Proporcionalidad SOLO

| Assets CANONICAL | Objetivo de esfuerzo |
|---:|---|
| 1–10 | 15–30 min/ciclo |
| 11–30 | 30–60 min/ciclo |
| 31+ | Revisar agrupación/cadencia; no imponer automation |

## Auditoría métrica→decisión

| Control | Resultado |
|---|---|
| Métricas | 7/7 |
| Fecha/ciclo obligatorio | Sí |
| Input observable | 7/7 |
| Acción derivada | 7/7 |
| Vanity metric acumulativa | 0 |
| Deprecación automática | No |

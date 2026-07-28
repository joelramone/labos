# 023 — Research Metrics

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R24.1, R24.2, R24.3, R24.4

## Propósito

Este documento define las métricas que miden la salud y productividad del proceso de investigación en LabOS. Cada métrica tiene un método de medición explícito y un periodo mensual de evaluación. Incluye además señales de advertencia con acciones correctivas y una cadencia de revisión definida.

Las métricas complementan los quality gates definidos en [020-quality-gates.md](./020-quality-gates.md) y se alimentan del lifecycle de 16 etapas documentado en [002-research-lifecycle.md](./002-research-lifecycle.md).

---

## Tabla de contenidos

1. [Métricas de investigación](#métricas-de-investigación)
2. [Cadencia de revisión](#cadencia-de-revisión)
3. [Warning signals y acciones correctivas](#warning-signals-y-acciones-correctivas)
4. [Conexión con Package 000](#conexión-con-package-000)
5. [Resumen de métricas](#resumen-de-métricas)

---

## Métricas de investigación

Todas las métricas se miden con periodo de **un mes calendario**. El primer día del mes se calculan los valores del mes anterior.

### Métrica 1: Investigaciones iniciadas por mes

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Investigaciones iniciadas por mes |
| **Definición operativa** | Cantidad de investigaciones que entraron al estado Proposed (Research_Brief creado con campos obligatorios completos según effort category) durante el mes calendario. |
| **Método de medición** | Conteo de Research_Briefs con fecha de creación dentro del mes, registrados en GitHub con estado inicial Proposed. |
| **Periodo** | Mensual (1 mes calendario) |
| **Línea base** | 0 |

---

### Métrica 2: Investigaciones completadas por mes

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Investigaciones completadas por mes |
| **Definición operativa** | Cantidad de investigaciones que alcanzaron el estado Completed (review aprobado) o Completed-with-limitations durante el mes calendario. |
| **Método de medición** | Conteo de investigaciones cuyo review result fue registrado como "approved" o "approved-with-limitations" con fecha dentro del mes, según registro en GitHub. |
| **Periodo** | Mensual (1 mes calendario) |
| **Línea base** | 0 |

---

### Métrica 3: Días promedio por categoría de esfuerzo

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Días promedio transcurridos por categoría de esfuerzo |
| **Definición operativa** | Promedio de días calendario entre la fecha de creación del Research_Brief (estado Proposed) y la fecha de conclusión del review (estado Completed), agrupado por effort category: Small (≤4h), Medium (5-16h), Large (17-40h). |
| **Método de medición** | Para cada investigación completada en el mes: calcular (fecha_review_aprobado - fecha_research_brief_creado) en días. Promediar por categoría. Si una categoría tiene 0 investigaciones completadas en el mes, se reporta como "N/A". |
| **Periodo** | Mensual (1 mes calendario) |
| **Línea base** | N/A (sin datos históricos) |
| **Desagregación** | Small: ≤4h estimadas / Medium: 5-16h estimadas / Large: 17-40h estimadas |

---

### Métrica 4: Activos producidos por investigación

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Activos producidos por investigación |
| **Definición operativa** | Cantidad total de Research_Assets extraídos dividida entre el número de investigaciones que alcanzaron la etapa de Asset Extraction durante el mes. |
| **Método de medición** | Conteo de assets registrados en `assets/` con fecha de extracción dentro del mes, dividido entre investigaciones que pasaron por etapa 13 (Asset Extraction) en el mismo periodo. Investigaciones sin asset que documentaron justificación de ausencia se incluyen en el denominador con 0 assets. |
| **Periodo** | Mensual (1 mes calendario) |
| **Línea base** | 0 |

---

### Métrica 5: Hipótesis de producto generadas por mes

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Hipótesis de producto generadas por mes |
| **Definición operativa** | Cantidad de Product_Hypotheses o Revenue_Hypotheses formuladas (con todos los campos requeridos completos) durante el mes calendario, derivadas de investigaciones. |
| **Método de medición** | Conteo de hipótesis registradas con identificador HYP-[type]-[seq] y fecha de creación dentro del mes, que cumplen los criterios de completitud definidos en [019-research-to-product-hypothesis.md](./019-research-to-product-hypothesis.md). |
| **Periodo** | Mensual (1 mes calendario) |
| **Línea base** | 0 |

---

### Métrica 6: Tasa de aprobación en quality gates

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Quality gate pass rate |
| **Definición operativa** | Porcentaje de investigaciones que aprueban el quality gate de Review (etapa 12) en su primera presentación, sin requerir ciclos de remediación. |
| **Método de medición** | (Investigaciones aprobadas en primer intento / Total de investigaciones presentadas a review en el mes) × 100. Una investigación cuenta como "primer intento" si no tiene registros previos de resultado "requires-rework" para el mismo review cycle. |
| **Periodo** | Mensual (1 mes calendario) |
| **Línea base** | N/A (sin datos históricos) |
| **Formato** | Porcentaje (0-100%) |

---

### Métrica 7: Dominios investigados por mes

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Dominios distintos investigados por mes |
| **Definición operativa** | Cantidad de dominios únicos (según clasificación de domain en Research_Brief) que tuvieron al menos una investigación activa (en cualquier estado entre Proposed y Archived) durante el mes. |
| **Método de medición** | Conteo de valores únicos del campo "preliminary domain classification" en Research_Briefs de investigaciones activas durante el mes. Dominios marcados como "unassigned" cuentan como un dominio separado. |
| **Periodo** | Mensual (1 mes calendario) |
| **Línea base** | 0 |

---

### Métrica 8: Ratio completadas-a-abandonadas

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Ratio de investigaciones completadas a abandonadas |
| **Definición operativa** | Relación entre investigaciones que alcanzaron estado Completed (o Completed-with-limitations) e investigaciones que alcanzaron estado Rejected durante el mes. |
| **Método de medición** | Completadas en el mes / Abandonadas en el mes. Si no hay abandonadas, se reporta como "∞" (todas completaron). Si no hay completadas ni abandonadas, se reporta como "N/A". Formato: ratio X:Y (e.g., 4:1 = 4 completadas por cada abandonada). |
| **Periodo** | Mensual (1 mes calendario) |
| **Línea base** | N/A (sin datos históricos) |

---

## Cadencia de revisión

### Frecuencia

La revisión de métricas de investigación se realiza **mensualmente**, durante la primera semana del mes siguiente al periodo medido.

### Proceso de revisión mensual

| Paso | Actividad | Responsable |
| ---- | --------- | ----------- |
| 1 | Recopilar datos crudos de todas las métricas del mes anterior | Fundador |
| 2 | Calcular valores de cada métrica según método de medición definido | Fundador |
| 3 | Comparar contra mes anterior (si existe) e identificar tendencias | Fundador |
| 4 | Evaluar warning signals (ver sección siguiente) | Fundador |
| 5 | Documentar acciones correctivas si aplican | Fundador |
| 6 | Registrar resultados con fecha y reviewer en GitHub | Fundador |

### Registro de revisión

Cada revisión mensual se documenta con:

- **Fecha de revisión**: día en que se realizó la evaluación
- **Reviewer**: identidad del evaluador (Fundador en etapa actual)
- **Periodo evaluado**: mes calendario evaluado
- **Valores de métricas**: tabla con las 8 métricas y su valor calculado
- **Warning signals activos**: lista de señales detectadas (si aplica)
- **Acciones correctivas**: decisiones tomadas (si aplica)
- **Notas**: observaciones relevantes para contexto

---

## Warning signals y acciones correctivas

Un warning signal es una condición observable que indica un problema potencial en el proceso de investigación. Cuando se detecta, requiere al menos una acción correctiva documentada.

### Signal 1: Investigación excede timebox por más de 50%

| Campo | Detalle |
| ----- | ------- |
| **Condición** | Una investigación ha consumido más del 150% de su timebox asignado sin haber alcanzado el estado Under Review. |
| **Detección** | Comparar horas acumuladas registradas en Research_Journal contra timebox definido en scope. Se detecta cuando horas_acumuladas > timebox × 1.5. |
| **Acción correctiva 1** | Evaluar si el scope original fue irrealista para la categoría de esfuerzo asignada. Si es así, documentar lección aprendida para mejorar estimaciones futuras y re-clasificar la investigación a la categoría apropiada. |
| **Acción correctiva 2** | Aplicar protocolo de escalación del lifecycle: concluir con hallazgos parciales, reducir scope, o cerrar la investigación con justificación documentada. No permitir extensión silenciosa. |

---

### Signal 2: Menos de 1 activo por cada 2 investigaciones completadas

| Campo | Detalle |
| ----- | ------- |
| **Condición** | En el mes evaluado, el ratio de activos producidos es menor a 0.5 por investigación completada (equivalente: menos de 1 activo por cada 2 investigaciones que pasaron Asset Extraction). |
| **Detección** | Si Métrica 4 (activos por investigación) < 0.5 en el mes. |
| **Acción correctiva 1** | Revisar las investigaciones completadas sin activo para verificar que las justificaciones de ausencia de activo son legítimas y no reflejan un problema sistemático de scope o ambición insuficiente en la formulación de research questions. |
| **Acción correctiva 2** | Evaluar si las investigaciones están siendo cerradas prematuramente antes de llegar a conclusiones lo suficientemente sustanciales para producir activos. Si es así, revisar criterios de completion y quality gates de las etapas de Findings y Conclusion. |

---

### Signal 3: Investigación cerrada sin conclusión documentada

| Campo | Detalle |
| ----- | ------- |
| **Condición** | Una investigación pasa a estado Rejected sin tener un documento de conclusión (ni parcial ni completo) registrado. |
| **Detección** | Investigación con estado Rejected cuyo expediente no contiene documento de conclusión ni registro de partial findings en el Research_Journal. |
| **Acción correctiva 1** | Requerir retroactivamente la documentación de partial findings y lecciones aprendidas antes de archivar. Toda investigación, incluso abandonada, debe dejar un registro mínimo de qué se intentó y por qué se detuvo. |
| **Acción correctiva 2** | Revisar si el abandono fue por un problema en etapas tempranas (mala formulación de pregunta, scope irreal) y documentar la causa raíz para prevenir repetición. |

---

### Signal 4: Misma investigación falla quality gate 2 o más veces

| Campo | Detalle |
| ----- | ------- |
| **Condición** | Una investigación recibe resultado "requires-rework" en el quality gate de Review (etapa 12) en 2 o más intentos consecutivos. |
| **Detección** | Registro de review results muestra ≥2 entradas de "requires-rework" para la misma investigación sin un "approved" intercalado. |
| **Acción correctiva 1** | Analizar los items específicos del checklist que fallan repetidamente. Si son los mismos items, el problema es probablemente metodológico (el investigador no entiende el criterio o el criterio es ambiguo). Documentar clarificación del criterio o proporcionar ejemplo de cumplimiento. |
| **Acción correctiva 2** | Si la investigación falla el gate por tercera vez, aplicar la regla del lifecycle: clasificar como "completed-with-limitations" o "abandoned" según el threshold de 6/8 items, y registrar Decision_Log con las deficiencias irresolubles. |

---

### Signal 5: Más del 70% de investigaciones en un solo dominio

| Campo | Detalle |
| ----- | ------- |
| **Condición** | En el mes evaluado, más del 70% de las investigaciones activas (en cualquier estado entre Proposed y Under Review) pertenecen a un mismo dominio según su clasificación en Research_Brief. |
| **Detección** | Si (investigaciones_dominio_más_frecuente / total_investigaciones_activas) > 0.70 en el mes. |
| **Acción correctiva 1** | Evaluar si la concentración es intencional (sprint temático, proyecto específico) o indica descuido de otros dominios del portfolio. Si es intencional, documentar la razón y el periodo esperado de concentración. |
| **Acción correctiva 2** | Si la concentración no es intencional, revisar el portfolio model para identificar dominios desatendidos y evaluar si existen research questions pendientes en esos dominios que deberían priorizarse en el siguiente mes. |

---

## Conexión con Package 000

Las métricas de investigación alimentan directamente las métricas de éxito del portfolio definidas en [Package 000 — 010-success-metrics.md](../package-000-foundation/010-success-metrics.md).

### Mapeo de métricas

| Métrica de investigación (Package 001) | Métrica de Package 000 | Relación |
| -------------------------------------- | ---------------------- | -------- |
| M4: Activos producidos por investigación | Activos registrados en sistema (Package 000, Métrica 3) | Los activos extraídos de investigaciones alimentan el conteo total de activos del portfolio. Cada Research_Asset completado contribuye al objetivo ≥3 activos registrados. |
| M5: Hipótesis de producto generadas | Hipótesis con monetización documentada (Package 000, Métrica 7) | Las Product_Hypotheses derivadas de investigaciones alimentan el pipeline de hipótesis comerciales del portfolio. Objetivo Package 000: ≥4 hipótesis con monetización documentada. |
| M2: Investigaciones completadas | Experimentos de validación iniciados (Package 000, Métrica 4) | Investigaciones completadas pueden generar experimentos de validación que contribuyen al objetivo ≥1 experimento iniciado a 30 días. |
| M5: Hipótesis de producto generadas | Transacciones reales documentadas (Package 000, Métrica 5) | Las Revenue_Hypotheses validadas eventualmente producen transacciones reales. La cadena completa: investigación → hipótesis → experimento → transacción. |

### Principio de alineación

Las métricas de investigación miden el **proceso** (cómo se investiga); las métricas de Package 000 miden el **resultado** (qué produce el sistema). La conexión es causal: un proceso de investigación saludable (medido aquí) produce activos e hipótesis (medidos en Package 000) que eventualmente generan ingresos.

Si las métricas de proceso son saludables pero las métricas de resultado de Package 000 no avanzan, el problema está en las etapas posteriores al research (productización, validación comercial, distribución). Si las métricas de proceso son deficientes, los resultados de Package 000 se verán afectados downstream.

---

## Resumen de métricas

| # | Métrica | Método de medición | Periodo | Formato |
| - | ------- | ------------------ | ------- | ------- |
| 1 | Investigaciones iniciadas | Conteo de Research_Briefs creados | Mensual | Entero |
| 2 | Investigaciones completadas | Conteo de reviews aprobados | Mensual | Entero |
| 3 | Días promedio por effort category | (fecha_review - fecha_brief) / investigaciones, por categoría | Mensual | Días (decimal) |
| 4 | Activos por investigación | Assets extraídos / investigaciones en Asset Extraction | Mensual | Ratio (decimal) |
| 5 | Hipótesis de producto generadas | Conteo de HYP-[type]-[seq] con campos completos | Mensual | Entero |
| 6 | Quality gate pass rate | (Aprobadas primer intento / presentadas a review) × 100 | Mensual | Porcentaje |
| 7 | Dominios investigados | Conteo de dominios únicos con investigación activa | Mensual | Entero |
| 8 | Ratio completadas-a-abandonadas | Completadas / Abandonadas en el mes | Mensual | Ratio X:Y |

---

## Referencias internas

- [002-research-lifecycle.md](./002-research-lifecycle.md) — Define las 16 etapas y estados que estas métricas miden
- [020-quality-gates.md](./020-quality-gates.md) — Define los quality gates cuya tasa de aprobación se mide en Métrica 6
- [019-research-to-product-hypothesis.md](./019-research-to-product-hypothesis.md) — Define los criterios de completitud de hipótesis medidos en Métrica 5
- [Package 000 — 010-success-metrics.md](../package-000-foundation/010-success-metrics.md) — Métricas del portfolio a las que estas métricas alimentan

---

## Tabla epistémica

| Clasificación | Cantidad | Descripción |
| ------------- | -------- | ----------- |
| [Decisión] | 1 | Este documento completo es una decisión de diseño de métricas e indicadores |

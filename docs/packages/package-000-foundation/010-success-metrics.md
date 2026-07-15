# Métricas de Éxito

## Propósito

Este documento define las métricas específicas y medibles para evaluar el cumplimiento del Package 000 — Foundation y el progreso operativo de LabOS en sus primeros 90 días. Cada métrica tiene un valor objetivo cuantificado, un método de medición concreto y una línea base declarada. No se utilizan objetivos genéricos como "mejorar" o "aumentar" — todo indicador tiene un umbral numérico o condición binaria verificable.

Las métricas se organizan en tres categorías temporales: métricas del package (evaluadas al cierre del package), métricas operativas (evaluadas a 30 días), y métricas de negocio (evaluadas a 90 días). Adicionalmente, se incluye al menos una métrica de salud del portfolio alineada con los principios de negocio de LabOS.

---

## Métricas del Package

Estas métricas evalúan el cumplimiento de los entregables del Package 000 — Foundation al momento de su cierre.

### 1. Documentos fundacionales completados

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Documentos fundacionales completados |
| **Definición operativa** | Cantidad de documentos del package que cumplen todos los criterios de estructura (H1 + ≥1 H2 + ≥100 palabras + tabla epistémica + clasificación completa) y contenido según su spec individual. Se determina cumplimiento verificando cada archivo contra el checklist de 016-foundation-review.md. |
| **Método de medición** | Revisión manual del checklist en 016-foundation-review.md; conteo de archivos con estado "pasa" en todos sus criterios. |
| **Valor objetivo** | 16/16 documentos completados |
| **Frecuencia de revisión** | Semanal |
| **Línea base** | 0/16 |

### 2. Requisitos cubiertos en trazabilidad

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Requisitos cubiertos en matriz de trazabilidad |
| **Definición operativa** | Cantidad de requisitos del package (18 totales) que tienen al menos un documento y sección identificados en la matriz de trazabilidad de 016-foundation-review.md como evidencia de cumplimiento. Se determina cumplimiento cuando la celda correspondiente contiene referencia a documento + sección específica. |
| **Método de medición** | Conteo de filas completas en la matriz de trazabilidad de 016-foundation-review.md. |
| **Valor objetivo** | 18/18 requisitos cubiertos |
| **Frecuencia de revisión** | Semanal |
| **Línea base** | 0/18 |

---

## Métricas Operativas (30 días)

Estas métricas evalúan el progreso operativo de LabOS 30 días después del cierre del Package 000.

### 3. Activos registrados en sistema

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Activos registrados en sistema |
| **Definición operativa** | Cantidad de activos reutilizables registrados en `assets/` que cumplen el criterio mínimo definido en 007-company-model.md: nombre (≤80 chars) + tipo (uno de los 7 de la taxonomía) + descripción (1-3 oraciones) + hipótesis de uso (usuario + contexto) + estado declarado. Se determina cumplimiento cuando el archivo del activo contiene los 5 campos mínimos. |
| **Método de medición** | Conteo de archivos en subdirectorios de `assets/` que cumplan criterio mínimo de activo. |
| **Valor objetivo** | ≥3 activos registrados |
| **Frecuencia de revisión** | Quincenal |
| **Línea base** | 0 |

### 4. Experimentos de validación iniciados

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Experimentos de validación de revenue iniciados |
| **Definición operativa** | Cantidad de experimentos definidos en 009-revenue-thesis.md que han sido iniciados (acción concreta ejecutada, no solo documentada). Se determina "iniciado" cuando existe evidencia observable de la acción: publicación realizada, contacto efectuado, página creada, o similar. |
| **Método de medición** | Revisión del registro de experimentos con fecha de inicio y evidencia de acción documentada. |
| **Valor objetivo** | ≥1 experimento iniciado |
| **Frecuencia de revisión** | Quincenal |
| **Línea base** | 0 |

---

## Métricas de Negocio (90 días)

Estas métricas evalúan el progreso de LabOS hacia la generación de ingresos validados a 90 días del cierre del Package 000.

### 5. Transacciones reales documentadas

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Transacciones reales documentadas |
| **Definición operativa** | Cantidad de transacciones comerciales completadas y documentadas con los 5 campos requeridos por 009-revenue-thesis.md: fecha, monto (USD), segmento del cliente, fuente de ingreso, canal de adquisición. Se determina cumplimiento cuando existe un registro con los 5 campos verificables. |
| **Método de medición** | Conteo de entradas en registro de transacciones con los 5 campos completos. |
| **Valor objetivo** | ≥1 transacción documentada |
| **Frecuencia de revisión** | Mensual |
| **Línea base** | 0 |

### 6. Ingresos totales generados

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Ingresos totales generados (USD) |
| **Definición operativa** | Suma total en USD de todas las transacciones reales documentadas provenientes de cualquiera de las fuentes de ingreso definidas en la Revenue_Thesis. Se determina cumplimiento cuando el monto acumulado es mayor a $0. Cualquier ingreso validado — sin importar el monto — satisface esta métrica. |
| **Método de medición** | Suma de campo "monto" en registro de transacciones documentadas. |
| **Valor objetivo** | >$0 USD (cualquier ingreso real validado) |
| **Frecuencia de revisión** | Mensual |
| **Línea base** | $0 |

---

## Métrica de Salud del Portfolio

Esta métrica evalúa la salud general del portafolio según los principios de negocio de LabOS: toda investigación produce activos, y todo activo tiene hipótesis de monetización.

### 7. Hipótesis con monetización documentada

| Campo | Detalle |
| ----- | ------- |
| **Nombre** | Hipótesis de producto con monetización documentada |
| **Definición operativa** | Cantidad de hipótesis de producto en el portfolio (labs activos en 012-portfolio-model.md) que tienen documentada su ruta de monetización: segmento objetivo + formato de entrega + modelo de ingreso. Se determina cumplimiento cuando la hipótesis contiene los 3 campos de monetización y está vinculada a al menos una fuente de ingreso de la Revenue_Thesis. |
| **Método de medición** | Conteo de labs con estado ≠ "pausado" cuya hipótesis de producto tiene los 3 campos de monetización completos en 012-portfolio-model.md o su documento derivado. |
| **Valor objetivo** | ≥4 hipótesis con monetización documentada |
| **Frecuencia de revisión** | Mensual |
| **Línea base** | 0 |

---

## Resumen de Métricas

| # | Métrica | Categoría | Objetivo | Línea base | Frecuencia |
| --- | ------- | --------- | -------- | ---------- | ---------- |
| 1 | Documentos fundacionales completados | Package | 16/16 | 0/16 | Semanal |
| 2 | Requisitos cubiertos en trazabilidad | Package | 18/18 | 0/18 | Semanal |
| 3 | Activos registrados en sistema | Operativa (30d) | ≥3 | 0 | Quincenal |
| 4 | Experimentos de validación iniciados | Operativa (30d) | ≥1 | 0 | Quincenal |
| 5 | Transacciones reales documentadas | Negocio (90d) | ≥1 | 0 | Mensual |
| 6 | Ingresos totales generados | Negocio (90d) | >$0 | $0 | Mensual |
| 7 | Hipótesis con monetización documentada | Salud portfolio | ≥4 | 0 | Mensual |

---

## Cross-links

- **Criterios de éxito del package**: Las métricas 1 y 2 alimentan directamente el checklist de aprobación en [016-foundation-review.md](./016-foundation-review.md).
- **Entrante desde Revenue Thesis**: Las métricas de negocio (5 y 6) evalúan el progreso de las hipótesis definidas en [009-revenue-thesis.md](./009-revenue-thesis.md).
- **Entrante desde Misión**: Los indicadores de progreso a 90 días definidos en [002-mission.md](./002-mission.md) se alinean con las métricas operativas y de negocio de este documento.

---

## Tabla epistémica

| Clasificación  | Cantidad | Porcentaje |
| -------------- | -------- | ---------- |
| [Hecho]        | 7        | 100%       |
| [Hipótesis]    | 0        | 0%         |
| [Visión]       | 0        | 0%         |
| Sin clasificar | 0        | 0%         |

> **Nota**: Todas las métricas son definiciones operativas verificables con métodos de medición concretos. Los valores objetivo y líneas base son hechos declarados (decisiones del fundador sobre qué medir y qué umbral considerar exitoso), no hipótesis de mercado. Las métricas no afirman que los objetivos se cumplirán — definen qué se observará y cuándo.

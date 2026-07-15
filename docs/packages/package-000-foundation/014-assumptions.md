# Supuestos y Dependencias

## Propósito

Este documento lista explícitamente los supuestos fundacionales de LabOS — aquello que el fundador asume como verdad sin haberlo validado con evidencia concluyente. Cada supuesto incluye un enunciado atómico, nivel de confianza, método de validación propuesto, horizonte temporal y referencia al documento del package donde se utiliza.

El propósito es hacer visible el riesgo epistémico: cuántas decisiones del package se sostienen sobre suposiciones no probadas, y qué se necesita hacer para convertirlas en hechos o descartarlas.

**Cross-links entrantes**: Este documento es referenciado desde [004-startup-thesis.md](./004-startup-thesis.md) (supuestos de capacidad del fundador), [008-business-model.md](./008-business-model.md) (supuestos de monetización) y [009-revenue-thesis.md](./009-revenue-thesis.md) (supuestos de disposición a pagar y mercado).

---

## Criterios de Asignación de Confianza

| Nivel | Criterio | Ejemplo |
| ----- | -------- | ------- |
| **Alto** | Evidencia externa verificable o dato cuantitativo que lo respalde | Estudio publicado, dato de plataforma, benchmark con fuente y fecha |
| **Medio** | Experiencia directa del fundador o analogías documentadas | Experiencia profesional previa en el dominio, comparables de mercado observados |
| **Bajo** | Intuición o deseo sin respaldo verificable | "Creo que la gente pagaría por esto" sin evidencia ni experiencia directa |

---

## Categoría 1: Existencia de Demanda

### Supuesto D-1: Necesidad de sistema integrado para solopreneurs

| Campo | Detalle |
| ----- | ------- |
| **Enunciado** | Fundadores técnicos solopreneurs necesitan un sistema integrado para operar portafolios de micro-productos digitales. [Hipótesis] |
| **Confianza** | Bajo |
| **Método de validación** | Publicar una landing page describiendo el problema + encuesta en 3 comunidades (Indie Hackers, r/SideProject, Twitter). Métrica de éxito: ≥50 respuestas con ≥40% indicando que experimentan el problema descrito. |
| **Horizonte** | 45 días |
| **Utilizado en** | [003-problem-statement.md](./003-problem-statement.md), [008-business-model.md](./008-business-model.md) |

🔴 **Riesgo Abierto** — Confianza baja. No se ha validado directamente con usuarios del segmento objetivo.

---

### Supuesto D-2: Tamaño del segmento objetivo

| Campo | Detalle |
| ----- | ------- |
| **Enunciado** | Existe un segmento de 500K–2M personas globalmente que experimenta el problema de pérdida de conocimiento no capitalizado al operar micro-productos. [Hipótesis] |
| **Confianza** | Bajo |
| **Método de validación** | Triangular datos de Indie Hackers (~200K miembros), Product Hunt makers (~500K), Gumroad creators (~100K activos) y comunidades de solopreneurs. Métrica de éxito: ≥3 fuentes de datos que converjan en un rango de 500K–2M personas en el segmento. |
| **Horizonte** | 60 días |
| **Utilizado en** | [003-problem-statement.md](./003-problem-statement.md), [009-revenue-thesis.md](./009-revenue-thesis.md) |

🔴 **Riesgo Abierto** — Confianza baja. La estimación de tamaño de mercado no tiene fuente primaria verificada.

---

## Categoría 2: Disposición a Pagar

### Supuesto P-1: Pago por servicios de configuración de agentes IA

| Campo | Detalle |
| ----- | ------- |
| **Enunciado** | El segmento objetivo pagaría $500–$2,000 USD por servicios de configuración de agentes IA personalizados. [Hipótesis] |
| **Confianza** | Medio |
| **Método de validación** | Ejecutar Experimento 1 de [009-revenue-thesis.md](./009-revenue-thesis.md): publicar oferta y contactar 10 empresas. Métrica de éxito: ≥1 cliente paga por el servicio completo dentro del rango de precio establecido. |
| **Horizonte** | 30 días |
| **Utilizado en** | [008-business-model.md](./008-business-model.md), [009-revenue-thesis.md](./009-revenue-thesis.md) |

**Justificación de confianza media**: Basado en tarifas observadas en Upwork para ingenieros AI/ML freelance ($50–$150/hora), lo que sitúa un proyecto de 10–15 horas en el rango $500–$2,000. Fuente: Upwork marketplace, consultado 2024. [Hipótesis]

---

### Supuesto P-2: Pago por templates de documentación de startups

| Campo | Detalle |
| ----- | ------- |
| **Enunciado** | El segmento objetivo pagaría $20–$100 USD por packs de templates de documentación para startups (specs, blueprints, decision logs). [Hipótesis] |
| **Confianza** | Medio |
| **Método de validación** | Ejecutar Experimento 2 de [009-revenue-thesis.md](./009-revenue-thesis.md): publicar pack en Gumroad y medir ventas. Métrica de éxito: ≥3 ventas orgánicas en 30 días post-publicación. |
| **Horizonte** | 60 días |
| **Utilizado en** | [008-business-model.md](./008-business-model.md), [009-revenue-thesis.md](./009-revenue-thesis.md) |

**Justificación de confianza media**: Productos similares en Gumroad (templates para Notion, playbooks para indie hackers) se venden en el rango $15–$97. Fuente: Gumroad creator economy reports y observación directa de productos similares, consultado 2024. [Hipótesis]

---

## Categoría 3: Capacidad del Fundador Único

### Supuesto C-1: Disponibilidad de tiempo del fundador

| Campo | Detalle |
| ----- | ------- |
| **Enunciado** | El fundador dispone de 20–25 horas semanales para operar LabOS de forma sostenida. [Hipótesis] |
| **Confianza** | Medio |
| **Método de validación** | Registrar horas efectivas dedicadas a LabOS durante 4 semanas consecutivas usando time-tracking. Métrica de éxito: promedio ≥20 horas/semana con varianza ≤5 horas entre semanas. |
| **Horizonte** | 30 días |
| **Utilizado en** | [004-startup-thesis.md](./004-startup-thesis.md), [008-business-model.md](./008-business-model.md) |

**Justificación de confianza media**: Basado en la estimación personal del fundador de su disponibilidad actual, considerando otras obligaciones. No se ha medido formalmente con time-tracking. [Hipótesis]

---

### Supuesto C-2: Capacidad de operar múltiples labs simultáneamente

| Campo | Detalle |
| ----- | ------- |
| **Enunciado** | Un operador único puede manejar 2–3 labs activos (en estado `explorando` o `validando`) simultáneamente sin degradación de calidad en los entregables. [Hipótesis] |
| **Confianza** | Bajo |
| **Método de validación** | Operar 2 labs activos durante 60 días y evaluar: (1) cumplimiento de deadlines de cada lab, (2) calidad de entregables medida por completitud de campos requeridos, (3) ausencia de burnout (auto-evaluación semanal ≥6/10). Métrica de éxito: los 3 criterios se cumplen simultáneamente durante ≥4 semanas consecutivas. |
| **Horizonte** | 60 días |
| **Utilizado en** | [012-portfolio-model.md](./012-portfolio-model.md), [004-startup-thesis.md](./004-startup-thesis.md) |

🔴 **Riesgo Abierto** — Confianza baja. No se ha probado en la práctica operar múltiples labs simultáneamente con un solo operador.

---

## Categoría 4: Viabilidad del Modelo Asset-First

### Supuesto A-1: Toda investigación produce activo reutilizable

| Campo | Detalle |
| ----- | ------- |
| **Enunciado** | Toda investigación de más de 4 horas acumuladas puede producir al menos un activo reutilizable documentado que cumpla los criterios mínimos definidos en [007-company-model.md](./007-company-model.md). [Hipótesis] |
| **Confianza** | Medio |
| **Método de validación** | Registrar las próximas 5 investigaciones de >4 horas y documentar si cada una produce un activo que cumpla los 5 campos mínimos (nombre, tipo, descripción, hipótesis de uso, estado). Métrica de éxito: ≥4 de 5 investigaciones (80%) producen un activo completo. |
| **Horizonte** | 60 días |
| **Utilizado en** | [007-company-model.md](./007-company-model.md), [008-business-model.md](./008-business-model.md) |

**Justificación de confianza media**: Basado en la experiencia del fundador produciendo documentación técnica — el Package 000 mismo es evidencia de que la investigación produce activos documentados. Sin embargo, no se ha medido sistemáticamente la tasa de conversión investigación→activo. [Hipótesis]

---

### Supuesto A-2: Potencial de monetización de activos internos

| Campo | Detalle |
| ----- | ------- |
| **Enunciado** | Los activos producidos internamente en LabOS (templates, playbooks, frameworks documentales) tienen potencial de monetización externa — al menos un subset de ellos sería comprado por terceros. [Hipótesis] |
| **Confianza** | Bajo |
| **Método de validación** | Seleccionar 3 activos producidos internamente, publicarlos en Gumroad a precio $0+ (pay-what-you-want) y medir descargas e ingresos. Métrica de éxito: ≥1 activo genera ≥$50 USD en 60 días. |
| **Horizonte** | 75 días |
| **Utilizado en** | [007-company-model.md](./007-company-model.md), [009-revenue-thesis.md](./009-revenue-thesis.md) |

🔴 **Riesgo Abierto** — Confianza baja. No se ha validado que activos creados para uso interno tengan valor de mercado externo.

---

## Resumen de Riesgos Abiertos

Los siguientes supuestos tienen confianza **bajo** y representan los mayores riesgos epistémicos del package. Su no-validación podría invalidar decisiones fundamentales del modelo:

| ID | Supuesto | Documento impactado | Horizonte | Consecuencia si es falso |
| -- | -------- | ------------------- | --------- | ------------------------ |
| D-1 | Necesidad de sistema integrado para solopreneurs | 003, 008 | 45 días | El problema central no existe → pivote de posicionamiento requerido |
| D-2 | Tamaño del segmento (500K–2M) | 003, 009 | 60 días | Mercado demasiado pequeño → limita potencial de escalabilidad |
| C-2 | Operación multi-lab por un operador | 012, 004 | 60 días | El portfolio model colapsa → reducir a 1 lab activo |
| A-2 | Monetización de activos internos | 007, 009 | 75 días | El modelo asset-first no genera ingresos directos → solo valor interno |

**Priorización**: Los supuestos D-1 y A-2 son los de mayor impacto porque sostienen la tesis central de monetización. Se recomienda ejecutar sus experimentos de validación en los primeros 60 días.

---

## Cross-links

- **Revisión del package**: Los supuestos y su estado de validación se evalúan como criterio (f) de aprobación en [016-foundation-review.md](./016-foundation-review.md).
- **Entrante desde Startup Thesis**: [004-startup-thesis.md](./004-startup-thesis.md) referencia este documento para los supuestos de capacidad del fundador.
- **Entrante desde Business Model**: [008-business-model.md](./008-business-model.md) referencia este documento para los supuestos de monetización y pricing.
- **Entrante desde Revenue Thesis**: [009-revenue-thesis.md](./009-revenue-thesis.md) referencia este documento para los supuestos de disposición a pagar y tamaño de mercado.

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
| ------------- | -------- | ---------- |
| [Hecho]       | 0        | 0%         |
| [Hipótesis]   | 8        | 100%       |
| [Visión]      | 0        | 0%         |

> **Nota**: El 100% de hipótesis es intencional — este documento existe precisamente para hacer explícitos los supuestos no validados. La proporción se reducirá conforme se ejecuten los experimentos de validación y se documente evidencia que promueva supuestos a [Hecho] o los descarte.

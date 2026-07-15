# Resumen del Package

## Propósito

Este documento consolida las decisiones fundacionales registradas en cada documento del Package 000 — Foundation, y declara el estado de consistencia inter-documentos. [Hecho] Funciona como inventario de decisiones clave que conforman la base constitucional de LabOS, permitiendo verificar coherencia sin necesidad de recorrer los 16 archivos individualmente. [Hecho]

---

## Decisiones registradas por documento

### README.md

- [Decisión] El glosario del README.md es la **fuente de verdad terminológica** única del package. Todo término de dominio se define aquí y se referencia desde los demás documentos sin redefinición.
- [Decisión] El estado del package se declara en este archivo con valores válidos: `pendiente`, `en progreso`, `completo`.
- [Decisión] Se definen 13 términos canónicos en el glosario inicial (Package, LabOS, Lab, Activo, Hipótesis, Hecho, Visión, Asset_First_Model, Revenue_Thesis, Portfolio_Model, Clasificación_Epistémica, Package_Foundation, Fundador).

### 001-company-vision.md

- [Decisión] El horizonte de la visión es de **3 a 5 años**, evaluado por capacidades habilitadas, no por fechas fijas.
- [Decisión] La visión se redacta **sin superlativos** ni promesas de mercado sin evidencia, clasificada íntegramente como [Visión].
- [Decisión] Se distingue explícitamente la visión (estado futuro aspiracional) de la misión (intención operativa actual).

### 002-mission.md

- [Decisión] La misión incluye **3 indicadores de progreso a 90 días** con nombre, línea base, valor objetivo y método de medición.
- [Decisión] La misión se clasifica como [Hecho] — describe lo que LabOS hace hoy, no lo que aspira a ser.
- [Decisión] El límite de extensión es 200 palabras máximo para mantener foco operativo.

### 003-problem-statement.md

- [Decisión] El segmento objetivo definido es **fundadores técnicos solopreneurs** que operan en la intersección investigación-producto.
- [Decisión] La existencia del problema se clasifica como **[Hipótesis]** hasta contar con evidencia cuantitativa de segmento.
- [Decisión] Se identifican ≥2 alternativas existentes por nombre con razón específica de insuficiencia.

### 004-startup-thesis.md

- [Decisión] LabOS se define en estado **pre-revenue, pre-product, documentation-first** como [Hecho].
- [Decisión] El enfoque actual es documentation-first: documentar antes de construir, diseñar antes de implementar.
- [Decisión] Toda afirmación sobre estado futuro (ingresos, equipo, producto) se etiqueta [Hipótesis] o [Visión].

### 005-manifesto.md

- [Decisión] Se establecen **7 principios fundamentales**, cada uno con anti-patrón observable que permite detectar violaciones.
- [Decisión] Los principios deben ser verificables por comportamiento observable — se prohíbe lenguaje aspiracional sin criterio de verificación.
- [Decisión] Los anti-patrones funcionan como test negativo: si se observa el anti-patrón, el principio está siendo violado.

### 006-operating-principles.md

- [Decisión] Se definen **7 reglas operativas** con estructura: condición de aplicación + acción esperada + ejemplo concreto.
- [Decisión] Se establece el **principio de prioridad de ingresos**: actividades generadoras de ingreso tienen prioridad sobre infraestructura que no genera ingreso en 90 días.
- [Decisión] Las reglas operativas no contradicen los principios del manifiesto — cada regla implementa un principio sin prescribir acciones excluyentes.

### 007-company-model.md

- [Decisión] Se adopta el **Asset_First_Model**: toda investigación con >4 horas acumuladas produce al menos 1 activo reutilizable documentado.
- [Decisión] Se define una **taxonomía de 7 tipos de activos**: documento, template, dataset, herramienta, componente, framework, playbook.
- [Decisión] Los activos tienen **3 estados** con transiciones definidas: borrador → validado → productizado.
- [Decisión] Estructura organizativa declarada: 1 fundador, 0 empleados, sin inversión externa, sin contratos activos.

### 008-business-model.md

- [Decisión] Se definen **3 etapas temporales** con distribución de esfuerzo: inmediato 0-30d (60%), corto plazo 30-90d (25%), mediano plazo 90-365d (15%).
- [Decisión] Se identifican **7 rutas de monetización** clasificadas como [Hipótesis], cada una con criterio de validación.
- [Decisión] La etapa inmediata aparece primero con mayor peso — reflejo del principio de prioridad de flujo de caja.

### 009-revenue-thesis.md

- [Decisión] Se documentan **4 fuentes de ingreso** con mecanismo, precio (rango), segmento y criterio de validación.
- [Decisión] **Toda la Revenue_Thesis es [Hipótesis]** hasta que exista una transacción real documentada.
- [Decisión] Cada fuente incluye un experimento mínimo con acción concreta + métrica pass/fail + plazo ≤90 días.
- [Decisión] Precios justificados con referencia de mercado verificable (nombre fuente + fecha consulta).

### 010-success-metrics.md

- [Decisión] Se definen **7 métricas** organizadas en 3 categorías: package (entregables), operativas (30d), negocio (90d).
- [Decisión] Cada métrica incluye 6 campos obligatorios: nombre, definición operativa, método, valor objetivo cuantificado, frecuencia, línea base.
- [Decisión] Se incluye **≥1 métrica de salud del portfolio** alineada con business-principles.
- [Decisión] Se prohíben objetivos genéricos ("mejorar", "aumentar") — todo debe ser cuantificado numéricamente o condición binaria.

### 011-scope-and-boundaries.md

- [Decisión] Se definen **6 exclusiones explícitas** del alcance del package (no SaaS, no usuarios externos, etc.).
- [Decisión] Se establecen **3 categorías de propiedad intelectual**: propiedad exclusiva del fundador, open source, licenciable a terceros.
- [Decisión] Se identifican **marcos regulatorios para 4 jurisdicciones** relevantes en protección de datos, PI e IA generativa.
- [Decisión] Toda expansión de alcance requiere documento de decisión formal en `docs/decisions/`.

### 012-portfolio-model.md

- [Decisión] Se documentan **11 labs** con estado, dominio e hipótesis de producto.
- [Decisión] Se definen **5 estados válidos** con transiciones secuenciales: idea → explorando → validando → operando + pausado (desde cualquier estado).
- [Decisión] **Reglas de priorización**: validación demanda > flujo caja inmediato > señal demanda más reciente.
- [Decisión] Si más de **5 labs activos** simultáneamente, se requiere justificación explícita de capacidad en horas.

### 013-risk-register.md

- [Decisión] Se registran **10 riesgos** con 6 campos cada uno (descripción, probabilidad, impacto, categoría, mitigación, owner).
- [Decisión] **2 riesgos prioritarios** identificados: bus factor=1 (probabilidad alta, impacto crítico) y ausencia de ingresos validados.
- [Decisión] Bus factor incluye ≥2 acciones de mitigación concretas.
- [Decisión] **Revisión trimestral** con fecha próxima programada.

### 014-assumptions.md

- [Decisión] Se documentan **8 supuestos** con 5 campos obligatorios (enunciado atómico, confianza, método, horizonte ≤90d, documento impactado).
- [Decisión] **4 categorías obligatorias** cubiertas: demanda, disposición a pagar, capacidad fundador, viabilidad asset-first.
- [Decisión] Supuestos con confianza "bajo" sin plan → etiqueta 🔴 Riesgo Abierto.
- [Decisión] Se identifican **4 riesgos abiertos** en sección resumen dedicada.

---

## Declaración de consistencia

Tras la producción secuencial de los 16 documentos siguiendo el grafo dirigido acíclico (DAG) de dependencias definido en el diseño del package, se declara: [Hecho]

**No se detectan contradicciones entre documentos.** [Hecho]

Justificación:

1. Cada concepto tiene un único documento como fuente de verdad (ver tabla source-of-truth en el diseño). Los demás documentos referencian sin redefinir. [Hecho]
2. Los documentos se produjeron en orden de dependencias — cada documento posterior respeta las definiciones y decisiones de sus predecesores. [Hecho]
3. Los principios de 005-manifesto.md y las reglas de 006-operating-principles.md no prescriben acciones mutuamente excluyentes para la misma condición. [Hecho]
4. La estructura organizativa es consistente entre 004-startup-thesis.md y 007-company-model.md (1 fundador, 0 empleados, sin inversión, sin contratos). [Hecho]
5. Las fuentes de ingreso de 008-business-model.md y 009-revenue-thesis.md son coherentes y complementarias. [Hecho]
6. Los labs de 012-portfolio-model.md son consistentes con el steering `portfolio-model.md`. [Hecho]

Si en una revisión posterior se identifican contradicciones, estas deberán documentarse aquí con referencia a los documentos y afirmaciones en conflicto, y resolverse mediante actualización del documento no-autoritativo o creación de decisión formal en `docs/decisions/`.

---

## Cross-links

**Cross-link saliente:**

- [016-foundation-review.md](./016-foundation-review.md) — Revisión y aprobación del package

**Cross-links entrantes** (todos los documentos del package cuyas decisiones se consolidan aquí):

- [README.md](./README.md)
- [001-company-vision.md](./001-company-vision.md)
- [002-mission.md](./002-mission.md)
- [003-problem-statement.md](./003-problem-statement.md)
- [004-startup-thesis.md](./004-startup-thesis.md)
- [005-manifesto.md](./005-manifesto.md)
- [006-operating-principles.md](./006-operating-principles.md)
- [007-company-model.md](./007-company-model.md)
- [008-business-model.md](./008-business-model.md)
- [009-revenue-thesis.md](./009-revenue-thesis.md)
- [010-success-metrics.md](./010-success-metrics.md)
- [011-scope-and-boundaries.md](./011-scope-and-boundaries.md)
- [012-portfolio-model.md](./012-portfolio-model.md)
- [013-risk-register.md](./013-risk-register.md)
- [014-assumptions.md](./014-assumptions.md)

---

## Tabla epistémica

Resumen de clasificación de afirmaciones en este documento:

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 8        | 100%       |
| [Hipótesis]   | 0        | 0%         |
| [Visión]      | 0        | 0%         |

# Modelo de Empresa

## Estructura organizativa

LabOS opera con la siguiente estructura organizativa: [Hecho]

- **Personas involucradas**: 1 fundador operador. [Hecho]
- **Empleados**: 0. [Hecho]
- **Inversión externa**: ninguna — sin ángeles, VC, grants ni deuda. [Hecho]
- **Relaciones contractuales activas**: ninguna. [Hecho]

El fundador es el único responsable de todas las funciones: investigación, diseño, documentación, desarrollo, decisiones de negocio y operación del portafolio. [Hecho]

### Estado futuro del equipo

- Se espera que la estructura evolucione a medida que se validen fuentes de ingreso y se justifique inversión en capacidad adicional. [Hipótesis]
- La incorporación de colaboradores o contratistas depende de que al menos un lab genere ingresos recurrentes validados. [Visión]

---

## Asset_First_Model

### Definición

Toda investigación — definida como cualquier actividad exploratoria con duración acumulada mayor a 4 horas — produce al menos un activo reutilizable documentado. [Hecho]

Este modelo asegura que el tiempo invertido en exploración genera valor tangible y catalogable, independientemente de si la investigación resulta en un producto o no. [Hecho]

### Taxonomía de tipos de activos

| # | Tipo | Descripción |
|---|------|-------------|
| 1 | **Documento** | Registro estructurado de conocimiento, análisis o decisiones que resuelve la necesidad de preservar y comunicar información verificable. [Hecho] |
| 2 | **Template** | Plantilla reutilizable con estructura predefinida que resuelve la repetición de formatos comunes en procesos recurrentes. [Hecho] |
| 3 | **Dataset** | Conjunto de datos organizados y documentados que resuelve la necesidad de evidencia cuantitativa para validar hipótesis. [Hecho] |
| 4 | **Herramienta** | Software, script o utilidad ejecutable que resuelve una tarea operativa específica automatizándola o simplificándola. [Hecho] |
| 5 | **Componente** | Módulo técnico aislado y reutilizable que resuelve una función específica dentro de un sistema mayor. [Hecho] |
| 6 | **Framework** | Estructura conceptual o técnica que resuelve la necesidad de organizar múltiples componentes bajo principios coherentes. [Hecho] |
| 7 | **Playbook** | Guía operativa paso a paso que resuelve la ejecución repetible de un proceso con resultado predecible. [Hecho] |

### Criterio mínimo de activo

Para que un artefacto califique como activo dentro del Asset_First_Model, debe cumplir los siguientes 5 campos obligatorios: [Hecho]

| Campo | Requisito | Ejemplo |
|-------|-----------|---------|
| **Nombre** | Máximo 80 caracteres, descriptivo y único dentro del portfolio | "Template de Validación de Hipótesis 30d" |
| **Tipo** | Uno de los 7 tipos de la taxonomía definida arriba | Template |
| **Descripción** | Entre 1 y 3 oraciones indicando qué problema resuelve | "Plantilla para documentar y evaluar hipótesis de negocio con criterio pass/fail en 30 días." |
| **Hipótesis de uso** | Usuario objetivo + contexto de aplicación | "Fundador técnico que necesita estructurar experimentos de validación antes de invertir en desarrollo." |
| **Estado** | Uno de: `borrador`, `validado`, `productizado` | borrador |

Un artefacto que no cumple estos 5 campos no se considera un activo completo y no puede incluirse en el portfolio. [Hecho]

### Hipótesis de monetización por activo

Todo activo que aspire a formar parte del portfolio productizable debe documentar una hipótesis de monetización con los siguientes campos: [Hecho]

| Campo | Descripción |
|-------|-------------|
| **Segmento objetivo** | Quién pagaría por este activo (rol + contexto) |
| **Formato de entrega** | Cómo se entregaría al usuario (descarga, SaaS, servicio, licencia, etc.) |
| **Modelo de ingreso** | Mecanismo de captura de valor (venta única, suscripción, freemium, licencia, etc.) |

Si un activo no tiene hipótesis de monetización documentada con estos tres campos, se clasifica como **"incompleto para portfolio"** y no puede avanzar a productización. [Hecho]

### Transiciones de estado

Los activos transitan entre tres estados con condiciones explícitas: [Hecho]

```text
borrador → validado → productizado
```

| Transición | Condiciones requeridas |
|------------|----------------------|
| **borrador → validado** | (1) Revisión completada por el owner (fundador). (2) Confirmación de que el activo cumple los 5 campos mínimos del criterio de activo. [Hecho] |
| **validado → productizado** | (1) Evidencia de al menos un uso real o prueba con usuario objetivo documentada (fecha, contexto, resultado). [Hecho] |

No existe transición directa de borrador a productizado. [Hecho] Un activo debe pasar por validación antes de considerarse listo para monetización. [Hecho]

### Nota de cierre por investigación sin activo

Si una investigación (>4h acumuladas) concluye sin producir un artefacto que cumpla los criterios mínimos del activo, se requiere registrar una nota de cierre con: [Hecho]

1. **Motivo**: por qué no se produjo un activo calificado (máximo 2 oraciones).
2. **Lecciones aprendidas**: qué se aprendió que pueda informar futuras investigaciones (máximo 3 oraciones).

La nota de cierre no debe exceder 5 oraciones en total. [Hecho] Su propósito es evitar pérdida total de valor incluso cuando la investigación no produce un activo formal. [Hecho]

---

## Cross-links

- **Modelo de negocio**: Los mecanismos de monetización por etapa y la priorización de flujo de caja se definen en [008-business-model.md](./008-business-model.md).
- **Portfolio**: La lista de labs, estados y reglas de priorización se documentan en [012-portfolio-model.md](./012-portfolio-model.md).
- **Supuestos**: Los supuestos sobre viabilidad del asset-first model y capacidad del fundador único se validan en [014-assumptions.md](./014-assumptions.md).
- **Entrante**: Este documento es referenciado desde [004-startup-thesis.md](./004-startup-thesis.md) como fuente de verdad de la estructura organizativa y el Asset_First_Model.

---

## Tabla epistémica

| Clasificación  | Cantidad | Porcentaje |
| -------------- | -------- | ---------- |
| [Hecho]        | 22       | 85%        |
| [Hipótesis]    | 1        | 4%         |
| [Visión]       | 1        | 4%         |
| Sin clasificar | 2        | 8%         |

> **Nota**: El alto porcentaje de hechos es esperado — este documento define estructuras y reglas operativas del modelo actual. Las afirmaciones sobre estado futuro del equipo están separadas y clasificadas apropiadamente. Los enunciados sin clasificar corresponden a referencias estructurales (cross-links).

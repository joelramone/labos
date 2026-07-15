# Manifiesto LabOS

## Propósito

Este documento declara los principios fundamentales que rigen toda actividad dentro de LabOS. Cada principio describe un comportamiento observable y medible, acompañado de un anti-patrón que permite identificar violaciones sin ambigüedad. Los principios aquí definidos son creencias operativas — no aspiraciones. Su implementación concreta se detalla en [006-operating-principles.md](./006-operating-principles.md).

---

## Declaraciones de Principio

### 1. No empezar por código

**Principio:** Antes de implementar cualquier solución, debe existir documentación (spec, blueprint o decisión) que justifique el trabajo y defina el resultado esperado. [Decisión]

**Anti-patrón:** Escribir código, crear features o iniciar desarrollo sin spec, blueprint ni decisión documentada que explique qué se construye y por qué.

---

### 2. Toda investigación produce un activo

**Principio:** Toda investigación que consuma más de 4 horas de esfuerzo debe generar al menos un artefacto reutilizable registrado en el sistema de activos con nombre, tipo y descripción. [Decisión]

**Anti-patrón:** Cerrar una investigación de más de 4 horas sin registrar ningún documento, template, dataset, herramienta ni componente que otro operador pueda reutilizar.

---

### 3. Hipótesis antes de inversión

**Principio:** No se invierte esfuerzo significativo (>1 semana-persona) en un proyecto sin una hipótesis de monetización documentada que especifique quién pagaría, cómo y cuánto. [Decisión]

**Anti-patrón:** Dedicar más de una semana a un proyecto sin documentar la hipótesis de monetización — quién es el segmento, qué formato de entrega, qué modelo de ingreso — clasificada como [Hipótesis] con método de validación.

---

### 4. Vender antes de construir

**Principio:** La validación de demanda (landing page, entrevista, pre-venta o señal de intención de pago) debe preceder al desarrollo completo de cualquier producto. [Decisión]

**Anti-patrón:** Construir un producto completo sin haber obtenido una sola señal de demanda verificable — ninguna landing publicada, ninguna entrevista de descubrimiento, ninguna pre-venta registrada.

---

### 5. Cambios pequeños y revisables

**Principio:** Cada entregable (commit, PR, documento, activo) debe ser revisable por un humano en menos de 15 minutos, lo que implica alcance acotado y separación de preocupaciones. [Decisión]

**Anti-patrón:** Commits masivos con múltiples cambios no relacionados, documentos de más de 20 páginas sin estructura de secciones, o PRs que tocan más de 3 módulos sin justificación.

---

### 6. Hechos y hipótesis, no opiniones

**Principio:** Las decisiones de negocio y técnicas se respaldan con datos, benchmarks, evidencia directa o referencias verificables; las suposiciones se clasifican explícitamente como [Hipótesis] con método de validación. [Decisión]

**Anti-patrón:** Tomar decisiones basándose en "me parece que...", "creo que...", o "es obvio que..." sin referenciar evidencia, y sin clasificar la afirmación como hipótesis cuando no existe dato que la respalde.

---

### 7. Documentación es producto

**Principio:** Un entregable (código, activo, feature, automatización) no se considera completo hasta que su documentación esté actualizada y permita a otro operador entender qué es, cómo funciona y cómo usarlo. [Decisión]

**Anti-patrón:** Declarar un entregable como "completo" o "listo para revisión" sin documentación que permita a un operador distinto al autor comprender su propósito, uso y limitaciones.

---

## Relación con Principios Operativos

Los principios declarados aquí son creencias fundamentales — el *qué* se defiende. Su traducción a reglas operativas concretas con condiciones de aplicación, acciones esperadas y ejemplos se encuentra en [006-operating-principles.md](./006-operating-principles.md).

---

## Tabla Epistémica

| Clasificación | Cantidad | Notas |
|---------------|----------|-------|
| [Hecho]       | 0        | —     |
| [Hipótesis]   | 0        | —     |
| [Visión]      | 0        | —     |
| [Decisión]    | 7        | Los 7 principios son decisiones activas del fundador |

Fecha de última revisión: 2025-01-XX (pendiente revisión formal)

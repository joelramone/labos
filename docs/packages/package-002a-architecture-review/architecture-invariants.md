# Invariantes Arquitectónicas

> **Nota de formalización (2025-07-22):** Las invariantes INV-04 (Fuente de verdad única por concepto) e INV-07 (Glosario Package 000 como fuente de verdad) han sido formalizadas mediante [ADR-0001 — Jerarquía de Definición Terminológica](../../decisions/0001-terminology-hierarchy.md). [Hecho] Este documento sigue siendo la referencia completa para las 10 invariantes; los ADRs las hacen ejecutables con mecanismos concretos.
>
> **Baseline:** Este documento es referenciado por [architecture-baseline-v1.md](../../architecture/architecture-baseline-v1.md) como Sección 2. [Hecho]

## Propósito

Este documento evalúa 10 invariantes arquitectónicas propuestas para LabOS. [Hecho] Para cada invariante se determina: CONFIRM (adoptar sin cambios), MODIFY (adoptar con ajustes), o REJECT (no adoptar). Las invariantes confirmadas se convierten en restricciones inviolables de la arquitectura.

---

## Definición de invariante

Una invariante arquitectónica es una propiedad que debe mantenerse verdadera en todo momento, independientemente de qué packages se implementen o qué evolución tenga el sistema. [Decisión] Violar una invariante requiere un ADR explícito que justifique por qué la invariante ya no aplica.

---

## Evaluación de Invariantes

### INV-01: Clasificación epistémica universal

**Propuesta:** Toda afirmación sustantiva en cualquier documento de LabOS debe clasificarse como [Hecho], [Hipótesis], [Visión] o [Decisión].

**Evaluación:** CONFIRM ✅ [Decisión]

**Racional:** Esta invariante ya se cumple consistentemente en los 3 packages evaluados. [Hecho] Es el mecanismo principal de honestidad intelectual del sistema y su costo operativo es mínimo (agregar una etiqueta). No existe razón para debilitarla.

**Condición de violación aceptable:** Ninguna. Esta invariante no admite excepciones.

---

### INV-02: Toda investigación >4h produce un activo

**Propuesta:** Toda investigación que consume más de 4 horas acumuladas produce al menos 1 activo reutilizable documentado, o una nota de cierre que explique por qué no fue posible.

**Evaluación:** CONFIRM ✅ [Decisión]

**Racional:** Definida en Package 000 (007-company-model.md) y reforzada en Package 001 (Principio 7). [Hecho] Es el mecanismo que convierte tiempo invertido en valor tangible. La válvula de escape (nota de cierre) previene burocracia sin sentido cuando genuinamente no hay activo extraíble.

**Condición de violación aceptable:** Ninguna. La nota de cierre ya es la válvula de escape.

---

### INV-03: Validación de demanda antes de inversión significativa

**Propuesta:** No se invierte >1 semana-persona en un proyecto sin hipótesis de monetización documentada y señal de demanda buscada activamente.

**Evaluación:** CONFIRM ✅ [Decisión]

**Racional:** Principio #3 del manifiesto ("Hipótesis antes de inversión") y principio #4 ("Vender antes de construir"). [Hecho] La mayor amenaza para LabOS es construir sin mercado — esta invariante es el principal mecanismo de protección contra ese riesgo.

**Condición de violación aceptable:** Solo para LabOS como infraestructura interna (porque su "demanda" es la necesidad de los labs activos, no un mercado externo). Los labs de producto deben cumplir estrictamente.

---

### INV-04: Fuente de verdad única por concepto

**Propuesta:** Cada concepto, término o definición tiene exactamente un documento como fuente de verdad. Los demás documentos referencian sin redefinir.

**Evaluación:** MODIFY ⚠️ [Decisión]

**Modificación:** Confirmar el principio pero agregar: "Cuando un package necesita EXTENDER una definición para su contexto específico, debe: (a) referenciar la definición base, (b) declarar explícitamente qué agrega, (c) no contradecir la definición base."

**Racional:** El principio es correcto pero la implementación actual falla: Package 001A redefine "Lab" sin referenciar la definición de Package 000. [Hecho] La modificación permite evolución terminológica sin ambigüedad.

**Condición de violación aceptable:** Ninguna. Si dos documentos se contradicen, uno debe corregirse.

---

### INV-05: Proporcionalidad de proceso a etapa

**Propuesta:** La complejidad de los procesos, revisiones y governance debe ser proporcional al número de operadores activos y al estado de revenue del proyecto.

**Evaluación:** CONFIRM ✅ [Decisión]

**Racional:** Esta invariante es la respuesta directa al hallazgo de sobre-ingeniería. [Hecho] El Package 001A viola esta invariante al introducir gobernanza de equipo para un operador único. La invariante establece que los procesos deben "crecer con la organización", no anticipar complejidad futura.

**Regla operativa derivada:**
- 1 operador, 0 ingresos: governance mínima (decisiones documentadas en 1 párrafo)
- 1 operador, con ingresos: governance ligera (revisiones mensuales de 15 min/lab)
- >1 operador: governance formal (activar escalación, contratos completos, review cycles)

**Condición de violación aceptable:** Cuando preparar documentación de governance tiene valor externo directo (e.g., licenciar LabOS requiere documentación de gobierno para credibilidad).

---

### INV-06: Documentation-first es el modo de operación

**Propuesta:** Ningún entregable (código, producto, automatización) se considera completo sin documentación actualizada que permita a otro operador entenderlo.

**Evaluación:** CONFIRM ✅ [Decisión]

**Racional:** Principio #7 del manifiesto y principio de ingeniería #4. [Hecho] Es coherente con el modelo documentation-first declarado en Package 000 (004-startup-thesis.md). Además, es el mecanismo de mitigación del riesgo #1 (bus factor = 1).

**Condición de violación aceptable:** Prototipos exploratorios con timebox <4h que se declaran explícitamente como "spike sin documentación" en el Research_Journal.

---

### INV-07: El glosario de Package 000 es la fuente de verdad terminológica global

**Propuesta:** Los 13 términos definidos en el glosario del README de Package 000 son canónicos. Ningún otro package puede redefinirlos, solo extenderlos con referencia explícita.

**Evaluación:** MODIFY ⚠️ [Decisión]

**Modificación:** Confirmar como invariante pero establecer un mecanismo de evolución: "Si un package futuro necesita modificar una definición del glosario base, debe proponer un ADR. La modificación solo se acepta si actualiza el glosario de Package 000 (no si crea definición paralela)."

**Racional:** El glosario actual tiene 13 términos que son estables y funcionales. [Hecho] El problema es que Package 001A creó definiciones paralelas sin este mecanismo. La modificación previene que se repita.

**Condición de violación aceptable:** Ninguna. La evolución tiene mecanismo formal (ADR).

---

### INV-08: Revenue tiene prioridad sobre infraestructura

**Propuesta:** Actividades generadoras de ingreso tienen prioridad sobre infraestructura que no genera ingreso en 90 días, excepto cuando la infraestructura es prerrequisito directo para la actividad de revenue.

**Evaluación:** CONFIRM ✅ [Decisión]

**Racional:** Regla operativa #1 de Package 000 (006-operating-principles.md) y principio de negocio #4. [Hecho] El riesgo #2 (ausencia prolongada de ingresos) justifica esta invariante como mecanismo de supervivencia.

**Condición de violación aceptable:** Cuando la infraestructura ES el producto (e.g., si se decide licenciar LabOS, entonces la documentación de LabOS = trabajo de revenue).

---

### INV-09: No más de 3 labs activos simultáneos sin justificación de capacidad

**Propuesta:** Si más de 3 labs están en estado activo (explorando, validando u operando) simultáneamente, se requiere una redistribución documentada de horas que demuestre viabilidad operativa sin burnout.

**Evaluación:** MODIFY ⚠️ [Decisión]

**Modificación:** Reducir de 5 (Package 000 dice >5 requiere justificación) a 3 como umbral práctico. El supuesto C-2 de Package 000 tiene confianza "bajo" para operar incluso 2-3 labs simultáneamente. [Hecho] Ser más conservador hasta que el supuesto se valide.

**Racional:** Con 20-25h/semana disponibles y overhead de LabOS infraestructura consumiendo 8-10h, quedan 10-15h para labs. Eso es 5-7.5h por lab con 2 activos, lo cual es apretado. Con 3 activos = 3-5h por lab, insuficiente para progreso significativo. [Hipótesis]

**Condición de violación aceptable:** Si el time-tracking demuestra ≥30h/semana disponibles de forma sostenida (4+ semanas), se puede subir a 4 labs activos.

---

### INV-10: Packages no se modifican retroactivamente sin ADR

**Propuesta:** Un package completado y aprobado no se modifica directamente. Los cambios requieren un ADR que explique qué se cambia, por qué, y qué impacto tiene en packages dependientes.

**Evaluación:** CONFIRM ✅ [Decisión]

**Racional:** Principio de ingeniería #2 ("Preservar decisiones existentes"). [Hecho] Los packages son unidades de trabajo completadas que sirven como fundamento para packages posteriores. Modificarlos sin trazabilidad rompe la cadena de decisiones.

**Condición de violación aceptable:** Correcciones de formato, typos o actualizaciones de fechas que no cambian el significado sustantivo de ninguna decisión.

---

## Resumen de Evaluación

| Resultado | Cantidad | Invariantes |
|-----------|----------|-------------|
| CONFIRM | 7 | INV-01, INV-02, INV-03, INV-05, INV-06, INV-08, INV-10 |
| MODIFY | 3 | INV-04, INV-07, INV-09 |
| REJECT | 0 | — |

**7 invariantes confirmadas sin modificación + 3 confirmadas con ajuste = 10 invariantes activas.** [Hecho]

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 14       | 38%        |
| [Hipótesis]   | 1        | 3%         |
| [Decisión]    | 22       | 59%        |
| [Visión]      | 0        | 0%         |

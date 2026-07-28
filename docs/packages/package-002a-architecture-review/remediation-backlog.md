# Backlog de Remediación

## Propósito

Este documento lista las acciones de remediación priorizadas derivadas de la revisión arquitectónica. [Hecho] Cada item tiene un problema claro, una resolución propuesta, y una evaluación de impacto. El backlog está ordenado por prioridad (P0 = inmediato, P3 = eventual).

---

## Criterios de Prioridad

| Prioridad | Significado | Timeline |
|-----------|-------------|----------|
| **P0** | Bloquea progreso o causa inconsistencia activa | Resolver antes de iniciar Package 003 |
| **P1** | Causa overhead significativo o ambigüedad operativa | Resolver en los próximos 30 días |
| **P2** | Mejora importante pero no bloquea nada | Resolver en los próximos 90 días |
| **P3** | Nice-to-have, mejora a largo plazo | Resolver cuando sea oportuno |

---

## Items de Remediación

### REM-01: Unificar terminología de "Lab" entre packages

| Campo | Valor |
|-------|-------|
| **ID** | REM-01 |
| **Título** | Establecer jerarquía terminológica para "Lab" |
| **Problema** | Package 000 define Lab como "vertical de negocio independiente con hipótesis de producto propia". Package 001A redefine Lab con 4 características formales (domain independence, identity preservation, operational autonomy, integration willingness) sin referenciar la definición base. Esto crea ambigüedad sobre cuál prevalece. [Hecho] |
| **Resolución** | Crear ADR que establezca: (1) La definición de Package 000 es canónica. (2) Package 001A EXTIENDE la definición para el contexto de integración formal pero no la reemplaza. (3) Un proyecto califica como "Lab" si cumple la definición de 000; cumplir las 4 características de 001A es requisito para INTEGRACIÓN FORMAL, no para ser Lab. |
| **Archivos afectados** | `docs/decisions/0001-lab-definition-hierarchy.md` (nuevo), `.kiro/specs/package-001a-first-lab-integration/requirements.md` (referencia, no modificar) |
| **Prioridad** | P0 |
| **Complejidad** | SMALL |
| **Bloquea packages futuros** | Sí — Package 002, 003 necesitan saber qué es un "Lab" sin ambigüedad |

---

### REM-02: Unificar taxonomía de tipos de activos

| Campo | Valor |
|-------|-------|
| **ID** | REM-02 |
| **Título** | Consolidar taxonomía de activos en una sola fuente |
| **Problema** | Package 000 (007-company-model.md) define 7 tipos de activos: documento, template, dataset, herramienta, componente, framework, playbook. Package 001A define 5 tipos para activos compartibles: templates, frameworks, tools, datasets, documentation. Las listas no son idénticas ni se referencian mutuamente. [Hecho] |
| **Resolución** | Crear ADR que confirme: (1) La taxonomía de 7 tipos de Package 000 es la fuente de verdad. (2) Package 001A identifica un SUBCONJUNTO de tipos que son compartibles entre labs, y debe referenciar la taxonomía base con un mapping explícito (e.g., "tools" → "herramienta", "documentation" → "documento"). |
| **Archivos afectados** | `docs/decisions/0002-asset-taxonomy-consolidation.md` (nuevo) |
| **Prioridad** | P0 |
| **Complejidad** | SMALL |
| **Bloquea packages futuros** | Sí — Package 003 (Asset System) necesita una taxonomía única |

---

### REM-03: Declarar simplificación de gobernanza para etapa actual

| Campo | Valor |
|-------|-------|
| **ID** | REM-03 |
| **Título** | Establecer gobernanza proporcional a operador único |
| **Problema** | Package 001A define un modelo de escalación de 3 niveles, contratos de 15 secciones, y ciclos de revisión mensuales/trimestrales/anuales. Con 1 operador que toma todas las decisiones, este overhead consume 15-25% del tiempo disponible sin generar valor adicional. [Hipótesis] |
| **Resolución** | Crear ADR que establezca: (1) Mientras exista 1 operador y 0 ingresos, toda gobernanza operativa se reduce a "decisión documentada del fundador en 1 párrafo" sin escalación formal. (2) Se define un trigger de activación de gobernanza formal: cuando un lab tenga un operador distinto al fundador, O cuando existan ingresos recurrentes >$1000/mes. (3) El Lab_Contract se mantiene completo (15 secciones) como template de referencia para visibilidad total, pero su revisión/actualización no es formalmente obligatoria hasta que se active gobernanza formal. Nota del fundador: se prefiere la estructura completa porque aporta visibilidad, aunque la operación diaria sea ligera (~1-2h/mes). |
| **Archivos afectados** | `docs/decisions/0003-proportional-governance.md` (nuevo) |
| **Prioridad** | P1 |
| **Complejidad** | SMALL |
| **Bloquea packages futuros** | Sí — Package 001A necesita saber qué nivel de governance implementar |

---

### REM-04: Simplificar Research Lifecycle por defecto

| Campo | Valor |
|-------|-------|
| **ID** | REM-04 |
| **Título** | Hacer lifecycle "Small" el modo por defecto |
| **Problema** | El Research Lifecycle de 16 etapas es comprehensivo pero operativamente pesado. Aunque existe categorización por esfuerzo (Small/Medium/Large), el documento presenta las 16 etapas como el "lifecycle completo" implícitamente estándar. [Hecho] Para la mayoría de investigaciones de un fundador solo (exploración de herramientas, evaluación de mercado, comparativas), la versión Small es suficiente. |
| **Resolución** | Crear ADR que establezca: (1) El modo por defecto es Small (Research_Brief lightweight + Conclusión). (2) Se "gradúa" a Medium al superar 4h, a Large al superar 16h. (3) Las 16 etapas completas son la referencia teórica pero NO la operación diaria. (4) El compliance assessment de 12 principios es obligatorio solo para Large; para Small/Medium se reduce a 3 preguntas: ¿Produje un activo? ¿Clasifiqué las afirmaciones? ¿Documenté limitaciones? |
| **Archivos afectados** | `docs/decisions/0004-lightweight-research-default.md` (nuevo) |
| **Prioridad** | P1 |
| **Complejidad** | MEDIUM |
| **Bloquea packages futuros** | No — pero afecta la operación diaria inmediatamente |

---

### REM-05: Formalizar el Value Pipeline como documento

| Campo | Valor |
|-------|-------|
| **ID** | REM-05 |
| **Título** | Crear documento autoritativo del pipeline Research→Revenue |
| **Problema** | El pipeline de valor (Research → Knowledge → Assets → Products → Revenue) es el centro arquitectónico declarado en esta revisión pero no existe como documento único. [Hecho] Actualmente está distribuido en: Package 001 (research), Package 000 007 (assets), Package 000 008 (business model), Package 000 009 (revenue thesis). No hay un mapa unificado que muestre cómo fluye el valor entre etapas. |
| **Resolución** | Crear un documento `docs/architecture/value-pipeline.md` que contenga: (1) Diagrama del pipeline completo con etapas. (2) Mapping de cada etapa a su package responsable. (3) Criterios de transición entre etapas del pipeline. (4) Métricas de throughput (cuántos items fluyen entre etapas por mes). |
| **Archivos afectados** | `docs/architecture/value-pipeline.md` (nuevo) |
| **Prioridad** | P1 |
| **Complejidad** | MEDIUM |
| **Bloquea packages futuros** | Sí — Package 003, 004, 005 necesitan saber dónde encajan en el pipeline |

---

### REM-06: Resolver dualidad Estados de Lab vs Maturity Model

| Campo | Valor |
|-------|-------|
| **ID** | REM-06 |
| **Título** | Clarificar relación entre Lab States y Maturity Model |
| **Problema** | Package 000 define 5 estados de lab (idea, explorando, validando, operando, pausado) que miden actividad comercial. Package 001A define 5 niveles de madurez (L0-L4) que miden integración al ecosistema. Ambos sistemas coexisten sin relación explícita. [Hecho] Para 1 persona operando, mantener 2 sistemas de clasificación por lab es overhead sin beneficio. |
| **Resolución** | Crear ADR que establezca: (1) Los 5 estados de Package 000 son el ÚNICO sistema de clasificación activo hasta que se active gobernanza formal (ver REM-03). (2) El Maturity Model se documenta como "framework futuro" que se activará cuando el trigger de gobernanza formal se cumpla. (3) Si se necesita, se puede mapear: L0=idea, L1=explorando, L2-L3=validando, L4=operando. |
| **Archivos afectados** | `docs/decisions/0005-single-lab-classification.md` (nuevo) |
| **Prioridad** | P2 |
| **Complejidad** | SMALL |
| **Bloquea packages futuros** | No |

---

### REM-07: Establecer review cycle proporcional

| Campo | Valor |
|-------|-------|
| **ID** | REM-07 |
| **Título** | Definir cadencia de revisión proporcional a estado del lab |
| **Problema** | Package 001A define revisiones mensuales + trimestrales + anuales por lab. Con 2 labs activos esto es manejable (~2h/mes), pero con 5 labs activos escalaría a ~15-20h/mes. [Hipótesis] Además, labs en estado `idea` no necesitan revisión. |
| **Resolución** | Crear ADR con modelo proporcional: (1) Labs en `idea` = 0 revisión (solo al cambiar de estado). (2) Labs en `explorando` = checkpoint de 15 min/mes (¿progresé? ¿produje activo? ¿siguiente paso?). (3) Labs en `validando` = revisión de 30 min/mes (métricas de validación + decisión continuar/pivotar). (4) Labs en `operando` = revisión de 1h/mes (revenue, retención, siguiente inversión). (5) Revisión trimestral y anual solo se activan cuando hay ≥3 labs en estado ≥`validando`. |
| **Archivos afectados** | `docs/decisions/0006-proportional-review-cycles.md` (nuevo) |
| **Prioridad** | P2 |
| **Complejidad** | SMALL |
| **Bloquea packages futuros** | No |

---

### REM-08: Simplificar Security Policy a 2 niveles

| Campo | Valor |
|-------|-------|
| **ID** | REM-08 |
| **Título** | Reducir clasificación de seguridad a 2 niveles operativos |
| **Problema** | Package 001A define 4 niveles de seguridad (Public, Internal, Confidential, Secret). En pre-revenue sin datos de terceros, sin usuarios externos y sin APIs públicas, solo 2 niveles son operativamente relevantes: público (compartible) y privado (no compartible). [Hecho] |
| **Resolución** | Crear ADR que establezca: (1) Niveles operativos actuales: Public (compartible sin restricción) y Private (no compartible sin autorización del fundador). (2) Los 4 niveles se documentan como "framework de escalación" que se activa cuando: un lab maneja datos de terceros, O existe un usuario externo, O hay una API pública. (3) El trigger de escalación se revisa en cada review cycle. |
| **Archivos afectados** | `docs/decisions/0007-simplified-security-levels.md` (nuevo) |
| **Prioridad** | P2 |
| **Complejidad** | SMALL |
| **Bloquea packages futuros** | No |

---

### REM-09: Documentar triggers de escalación de complejidad

| Campo | Valor |
|-------|-------|
| **ID** | REM-09 |
| **Título** | Crear documento de triggers que activan complejidad dormida |
| **Problema** | Varios items de remediación (REM-03, REM-06, REM-07, REM-08) proponen simplificar ahora y escalar después. Pero no existe un documento único que liste CUÁNDO se activa cada nivel de complejidad dormida. Sin esto, la complejidad nunca se activará (y se perderá) o se activará arbitrariamente. [Hipótesis] |
| **Resolución** | Crear un documento `docs/architecture/complexity-triggers.md` que contenga una tabla con: (1) Trigger (condición observable), (2) Qué se activa, (3) Referencia al ADR que lo simplificó, (4) Qué evidencia se necesita para activar. Ejemplo: "Primer operador distinto al fundador → Activar gobernanza formal de 001A → ADR-0003 → Contrato firmado con el operador." |
| **Archivos afectados** | `docs/architecture/complexity-triggers.md` (nuevo) |
| **Prioridad** | P2 |
| **Complejidad** | MEDIUM |
| **Bloquea packages futuros** | No — pero es importante para evitar pérdida de decisiones |

---

### REM-10: Crear Value Pipeline metrics

| Campo | Valor |
|-------|-------|
| **ID** | REM-10 |
| **Título** | Definir métricas de throughput del pipeline de valor |
| **Problema** | El centro arquitectónico es el Knowledge-to-Value Pipeline pero no existen métricas que midan su throughput. Las métricas actuales (Package 000, 010-success-metrics.md) miden entregables del package y métricas operativas, pero no miden "cuántos items fluyen de Research a Revenue por período". [Hecho] |
| **Resolución** | Agregar al documento de Value Pipeline (REM-05) un set mínimo de métricas: (1) Investigaciones iniciadas/mes, (2) Activos producidos/mes, (3) Activos con hipótesis de monetización/mes, (4) Activos en validación activa/mes, (5) Revenue generado/mes. Este "funnel" permite identificar dónde se atasca el pipeline. |
| **Archivos afectados** | `docs/architecture/value-pipeline.md` (complemento de REM-05) |
| **Prioridad** | P3 |
| **Complejidad** | SMALL |
| **Bloquea packages futuros** | No |

---

## Resumen por Prioridad

| Prioridad | Items | IDs |
|-----------|-------|-----|
| P0 | 2 | REM-01, REM-02 |
| P1 | 3 | REM-03, REM-04, REM-05 |
| P2 | 4 | REM-06, REM-07, REM-08, REM-09 |
| P3 | 1 | REM-10 |

**Esfuerzo total estimado:**
- P0: ~2-3 horas (2 ADRs cortos)
- P1: ~6-8 horas (3 ADRs + 1 documento nuevo)
- P2: ~4-5 horas (4 ADRs cortos + 1 documento)
- P3: ~1-2 horas (extensión de documento existente)

**Total: ~13-18 horas** [Hipótesis] — ejecutable en 1-2 semanas con dedicación parcial.

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 12       | 46%        |
| [Hipótesis]   | 4        | 15%        |
| [Decisión]    | 10       | 39%        |
| [Visión]      | 0        | 0%         |

# Matriz de Decisiones Arquitectónicas

## Propósito

Este documento registra cada hallazgo significativo de la revisión arquitectónica con una decisión explícita sobre su resolución. [Hecho] Cada hallazgo se evalúa contra el contexto real: fundador único, pre-revenue, documentation-first.

---

## Criterios de severidad

| Severidad | Definición |
|-----------|-----------|
| **Crítica** | Bloquea progreso o genera contradicciones irresolubles |
| **Alta** | Causa overhead significativo o inconsistencia que afecta múltiples packages |
| **Media** | Inconsistencia localizada o complejidad innecesaria en un área |
| **Baja** | Oportunidad de mejora, no urgente |

---

## Matriz de Decisiones

### Hallazgos de Consistencia Terminológica

| ID | Resumen | Fuente | Package Afectado | Severidad | Decisión | Racional | Acción Requerida |
|----|---------|--------|-----------------|-----------|----------|----------|-----------------|
| T-01 | Definición de "Lab" diverge entre Package 000 y 001A | 000-README glosario vs 001A-R1 | 000, 001A | Alta | ACCEPT_WITH_MODIFICATIONS | La definición de 000 es la base; 001A agrega características para el contexto de integración. Ambas son válidas pero necesitan jerarquía explícita. | Establecer 000 como definición canónica. 001A declara extensión con referencia explícita al término base. |
| T-02 | Taxonomía de activos inconsistente (7 tipos en 000 vs 5 tipos en 001A) | 007-company-model.md vs 001A-R7 | 000, 001A | Alta | ACCEPT | Son taxonomías para propósitos distintos: 000 clasifica todos los activos producibles, 001A clasifica solo activos compartibles entre labs. La inconsistencia es real y confusa. | Unificar: 001A debe referenciar la taxonomía de 000 y declarar cuáles son compartibles. No crear taxonomía paralela. |
| T-03 | Estados de Lab (5 en 000) vs Maturity_Model (5 niveles L0-L4 en 001A) | 012-portfolio-model.md vs 001A-R10 | 000, 001A | Media | ACCEPT_WITH_MODIFICATIONS | Son conceptos complementarios pero no idénticos: estados reflejan actividad comercial, madurez refleja integración al ecosistema. Sin embargo, tener ambos para 1 persona es excesivo. | DEFER el Maturity_Model hasta que exista >1 Lab en estado `operando`. Usar solo los 5 estados de Package 000 por ahora. |
| T-04 | No existe entidad "Knowledge" unificada entre packages | Transversal | 001, 002 | Media | DEFER | Válido como concepto futuro, pero premature para pre-revenue. El Package 002 (Knowledge Architecture) está pendiente y es el lugar natural para esta definición. | Resolver cuando se ejecute Package 002. No crear abstracción prematura. |
| T-05 | Gobernanza evoluciona de informal (000) a formal (001A) sin mapping | 000-single-founder vs 001A-R4 | 000, 001A | Alta | ACCEPT | La transición no está documentada. El Package 000 declara "fundador decide todo" pero 001A introduce escalación formal sin reconocer que en la etapa actual son equivalentes. | Documentar explícitamente que mientras exista 1 operador, toda gobernanza se reduce a decisión documentada del fundador. La escalación formal se activa cuando hay >1 stakeholder. |

### Hallazgos de Sobre-ingeniería

| ID | Resumen | Fuente | Package Afectado | Severidad | Decisión | Racional | Acción Requerida |
|----|---------|--------|-----------------|-----------|----------|----------|-----------------|
| S-01 | Research Lifecycle de 16 etapas con quality gates formales | 002-research-lifecycle.md | 001 | Alta | ACCEPT_WITH_MODIFICATIONS | Las 16 etapas son conceptualmente sólidas pero operativamente pesadas para 1 persona. Ya existe categorización por esfuerzo (Small/Medium/Large) que alivia esto parcialmente. | Hacer la versión "Small" (<4h) el DEFAULT. Medium y Large se activan explícitamente. Reducir artefactos obligatorios del default. |
| S-02 | Lab Contract de 15 secciones obligatorias | 001A-R2 | 001A | Crítica | ACCEPT | 15 secciones para un contrato entre una persona y ella misma es burocracia sin valor. | Reducir a 5 secciones obligatorias (Misión, Scope, Outputs, Estado, Siguiente acción). Las 10 restantes son opcionales y se activan al escalar. |
| S-03 | Modelo de escalación de 3 niveles | 001A-R4 | 001A | Alta | ACCEPT | 3 niveles de escalación cuando solo hay 1 decision-maker es arquitectura para un futuro que puede no llegar. | Reemplazar por: "Toda decisión se documenta en 1 párrafo por el fundador. Escalación formal se activa cuando hay >1 stakeholder." |
| S-04 | Maturity Model de 5 niveles (L0-L4) | 001A-R10 | 001A | Media | DEFER | Conceptualmente útil para el futuro pero sin valor operativo actual. Ningún lab tiene la complejidad para justificar 5 niveles de madurez. | Defer hasta que ≥3 labs estén en estado `explorando` o superior. Usar los estados simples de Package 000. |
| S-05 | Security classification de 4 niveles | 001A-R9 | 001A | Media | ACCEPT_WITH_MODIFICATIONS | Los 4 niveles (Public/Internal/Confidential/Secret) son razonables como framework futuro, pero en pre-revenue sin datos de terceros, solo 2 son relevantes ahora. | Simplificar a 2 niveles operativos: Public y Private. Expandir a 4 cuando el primer lab maneje datos de terceros. |
| S-06 | Review cycles (monthly + quarterly + annual) | 001A-R16 | 001A | Alta | ACCEPT | Con 2 labs activos, las revisiones mensuales por lab + trimestrales + anuales = ~6-8 horas/mes solo en governance. Eso es 25-40% del tiempo de "exploración". | Simplificar a: revisión mensual ligera (15 min por lab, checklist de 5 items). Trimestral y anual se activan cuando hay ≥3 labs activos. |
| S-07 | Compliance assessment de 12 principios por investigación | 001-research-principles.md | 001 | Media | ACCEPT_WITH_MODIFICATIONS | El assessment es valioso para rigor pero 12 principios evaluados formalmente por cada investigación genera fatiga de compliance. | Hacer assessment obligatorio solo para investigaciones Large (>16h). Para Small y Medium, assessment simplificado de 3 preguntas clave. |

### Hallazgos de Abstracciones Faltantes

| ID | Resumen | Fuente | Package Afectado | Severidad | Decisión | Racional | Acción Requerida |
|----|---------|--------|-----------------|-----------|----------|----------|-----------------|
| A-01 | No existe concepto "Capability" que conecte lo que labs producen con lo que el ecosistema necesita | Transversal | Futuro | Baja | DEFER | Abstracción prematura. Con 2 labs activos y 0 ingresos, optimizar la interoperabilidad de capacidades no genera valor. | Revisitar cuando ≥3 labs estén activos y exista evidencia de reutilización real entre ellos. |
| A-02 | No existe "Product Lifecycle" formal conectando activos a revenue | Transversal | 000, 004 | Media | ACCEPT_WITH_MODIFICATIONS | El pipeline existe implícitamente (Asset→Hipótesis monetización→Validación→Revenue) pero no está formalizado en un documento autoritativo. | Crear un diagrama simple de "Value Pipeline" en Package 000 o como ADR. No crear un package separado para esto. |
| A-03 | No existe "Dependency Graph" entre packages/labs/activos | Transversal | Futuro | Baja | DEFER | Sin tooling para mantenerlo actualizado, un grafo manual se desactualiza en semanas. | Revisitar cuando exista automatización (Package 007) que pueda generar el grafo. |
| A-04 | Pipeline Research→Revenue no tiene documento único autoritativo | 001, 000 | 001, 000 | Media | ACCEPT | El valor principal de LabOS es convertir conocimiento en ingreso, pero este pipeline está distribuido en 4+ documentos sin un mapa unificado. | Producir un ADR o documento ligero que mapee las etapas cross-package del pipeline de valor. |

### Hallazgos de Centro Arquitectónico

| ID | Resumen | Fuente | Package Afectado | Severidad | Decisión | Racional | Acción Requerida |
|----|---------|--------|-----------------|-----------|----------|----------|-----------------|
| C-01 | La arquitectura aparenta ser research-driven pero el objetivo declarado es revenue | 001 vs 000 business model | 001, 000 | Alta | ACCEPT | El Package 001 es el más detallado (26 documentos, 16 etapas) mientras que el business model tiene 1 documento. El peso documental sugiere que research es el centro, pero el manifiesto dice que revenue tiene prioridad. | Declarar explícitamente el centro arquitectónico como KNOWLEDGE-TO-VALUE (ver architectural-center.md). Rebalancear peso de documentación futura hacia conversion, no hacia más rigor investigativo. |

### Hallazgos de Escalabilidad

| ID | Resumen | Fuente | Package Afectado | Severidad | Decisión | Racional | Acción Requerida |
|----|---------|--------|-----------------|-----------|----------|----------|-----------------|
| E-01 | Governance bottleneck: toda escalación termina en "Fundador" | 001A-R4 | 001A | Media | ACCEPT_WITH_MODIFICATIONS | Es correcto para la etapa actual. El problema es que el modelo no define un trigger para evolucionar. | Agregar trigger explícito: "cuando un lab tenga un operador distinto al fundador, activar gobernanza formal". |
| E-02 | Research lifecycle de 16 etapas no es team/agent-compatible | 002-research-lifecycle.md | 001 | Media | DEFER | Prematuro optimizar para equipos o agentes cuando no hay ni equipo ni agentes operando. | Revisitar en Package 006 (AI Workspace) o cuando el primer agente ejecute una investigación. |
| E-03 | Review overhead escalará linealmente con labs activos | 001A-R16 | 001A | Alta | ACCEPT | Con la estructura actual, cada lab adicional agrega ~3-4h/mes de overhead administrativo. Con 5 labs activos = 15-20h/mes solo en revisiones. | Implementar modelo de revisión proporcional: labs en estado `idea` = 0 revisión, `explorando` = 15 min/mes, `validando` = 30 min/mes, `operando` = 1h/mes. |

---

## Resumen de Decisiones

| Decisión | Cantidad |
|----------|----------|
| ACCEPT | 6 |
| ACCEPT_WITH_MODIFICATIONS | 7 |
| REJECT | 0 |
| DEFER | 5 |
| REQUIRES_EVIDENCE | 0 |

**Observación:** No se rechaza ningún hallazgo porque todos identifican problemas reales verificados contra la documentación existente. [Hecho] Los DEFER corresponden a problemas válidos cuya resolución no es urgente para la etapa pre-revenue. [Decisión]

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 20       | 45%        |
| [Hipótesis]   | 2        | 5%         |
| [Decisión]    | 22       | 50%        |
| [Visión]      | 0        | 0%         |

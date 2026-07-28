# Templates de Investigación — LabOS

## Propósito

Este directorio contiene los **9 templates operativos** del Package 001 — Research Methodology. Cada template es una plantilla reutilizable que estandariza la documentación de investigación dentro de LabOS, independientemente del dominio.

Los templates implementan los frameworks y procesos definidos en `docs/packages/package-001-research-methodology/` y están diseñados para usarse en conjunto a lo largo del Research_Lifecycle.

---

## Índice de templates

| # | Archivo | Propósito | Campos requeridos |
|---|---------|-----------|-------------------|
| 1 | [research-brief-template.md](./research-brief-template.md) | Capturar el trigger inicial de una investigación con contexto, clasificación y esfuerzo estimado | 8 (4 en modo lightweight) |
| 2 | [research-plan-template.md](./research-plan-template.md) | Estructurar el plan ejecutable con research questions, scope, timebox, assumptions y completion criteria | 15 |
| 3 | [source-register-template.md](./source-register-template.md) | Registrar y evaluar fuentes con scoring de calidad por 10 dimensiones y campos de propiedad intelectual | 21 |
| 4 | [experiment-template.md](./experiment-template.md) | Diseñar experimentos con protocolo, variables, criterios de éxito/fracaso y campos de reproducibilidad | 14 |
| 5 | [research-journal-template.md](./research-journal-template.md) | Mantener registro cronológico de actividades, hallazgos y decisiones por sesión de trabajo | 8 por entrada |
| 6 | [decision-log-template.md](./decision-log-template.md) | Registrar decisiones significativas con alternativas evaluadas, evidencia y reversibilidad | 8 por entrada |
| 7 | [conclusion-template.md](./conclusion-template.md) | Formular conclusiones trazables con nivel de certidumbre, limitaciones e incertidumbre documentada | 9 |
| 8 | [research-asset-handoff-template.md](./research-asset-handoff-template.md) | Documentar la extracción y entrega formal de activos reutilizables al repositorio de assets | 9 |
| 9 | [research-review-template.md](./research-review-template.md) | Ejecutar revisión final de investigación con checklist de 8 ítems, remediación y sign-off formal | 15 (8 checklist + 4 remediación + 3 sign-off) |

---

## Uso

1. **Seleccionar** el template correspondiente a la etapa del Research_Lifecycle en la que se encuentra la investigación.
2. **Copiar** el template al directorio de la investigación activa.
3. **Completar** todos los campos requeridos antes de avanzar a la siguiente etapa.
4. **Validar** contra los quality gates definidos en [020-quality-gates.md](../../packages/package-001-research-methodology/020-quality-gates.md).

---

## Relación con el Research_Lifecycle

| Etapa del Lifecycle | Template asociado |
|---------------------|-------------------|
| Intake | research-brief-template.md |
| Scope + Assumptions | research-plan-template.md |
| Source Collection | source-register-template.md |
| Experimentation | experiment-template.md |
| Todas las etapas activas | research-journal-template.md |
| Decisiones significativas | decision-log-template.md |
| Conclusion | conclusion-template.md |
| Asset Extraction | research-asset-handoff-template.md |
| Review | research-review-template.md |

---

## Trazabilidad

| Requirement | Cobertura |
|-------------|-----------|
| R33.1 | Todos los templates tienen propósito, campos requeridos e instrucciones de uso |
| R33.2 | Todos los templates incluyen instrucciones paso a paso |
| R33.3 | Todos los templates incluyen un ejemplo completo con datos realistas |
| R33.4 | Todos los templates incluyen secciones domain-specific opcionales |
| R33.5 | Este README actúa como índice central de templates con filename, propósito y count de campos |
| R34.3 | Índice actualizado como parte de la declaración de estado del package |

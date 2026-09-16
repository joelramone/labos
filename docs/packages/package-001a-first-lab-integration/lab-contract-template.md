# Template del Lab Contract — 15 Secciones

## Propósito

Este documento define el template estándar del Lab Contract con las 15 secciones canónicas. [Decisión] Cada sección incluye: propósito, texto de guía, ejemplos y errores comunes. El Lab Contract es el documento formal que establece la relación entre un Lab y LabOS. [Decisión]

---

## Metadata del Contrato

Todo Lab Contract instanciado debe incluir este header:

```markdown
| Campo | Valor |
|-------|-------|
| Lab | [nombre del Lab] |
| Dominio | [dominio principal] |
| Estado | [idea/explorando/validando/operando/pausado] |
| Versión del contrato | [1.0] |
| Fecha de creación | [YYYY-MM-DD] |
| Última revisión | [YYYY-MM-DD] |
| Próxima revisión | [YYYY-MM-DD] |
| Fundador/Owner | [nombre] |
```

---

## Sección 1: Mission (Misión)

### Propósito
Declarar el propósito fundamental del Lab en 1-3 oraciones. [Decisión] La misión define POR QUÉ existe el Lab.

### Guía
- Expresar el propósito en términos de valor que produce, no de actividades que ejecuta.
- Ser específico al dominio del Lab.
- No incluir métricas ni plazos — eso pertenece a otras secciones.
- Marcar como [Hipótesis] si el Lab está en estado `idea` (no validado).

### Ejemplo
> "Desarrollar y validar estrategias algorítmicas de scalping en mercados de criptomonedas con gestión de riesgo automatizada." [Hipótesis]

### Errores comunes
- ❌ Misión genérica que podría aplicar a cualquier Lab ("generar valor").
- ❌ Incluir múltiples dominios en una sola misión.
- ❌ Presentar la misión como [Hecho] cuando el Lab no ha validado nada.

---

## Sección 2: Scope (Alcance)

### Propósito
Delimitar los límites operativos del Lab. [Decisión] Define QUÉ hace y QUÉ NO hace.

### Guía
- Incluir dominio principal y sub-dominios si aplican.
- Declarar explícitamente lo que queda FUERA del alcance.
- Referenciar otros Labs si hay áreas de potencial solapamiento.

### Ejemplo
> **Incluido:** Trading cuantitativo, estrategias algorítmicas, backtesting, gestión de riesgo automatizada.
> **Excluido:** Trading manual, análisis fundamental, advisory financiero.

### Errores comunes
- ❌ Alcance demasiado amplio que solapa con otros Labs.
- ❌ No declarar exclusiones explícitas.
- ❌ Confundir alcance con misión.

---

## Sección 3: Inputs (Entradas)

### Propósito
Documentar qué recibe el Lab del ecosistema LabOS o de otros Labs. [Decisión]

### Guía
- Clasificar por origen: LabOS-Shared, Cross-Lab, Externo.
- Ser concreto: nombrar el recurso, no abstracciones.
- Si no se sabe qué inputs necesita, marcar como EVIDENCE_REQUIRED.

### Ejemplo
> - Templates de investigación (LabOS-Shared) [Hecho]
> - Metodología de research (Package 001, LabOS-Shared) [Hecho]
> - Datos de mercado crypto (Externo) [Hipótesis]

### Errores comunes
- ❌ Listar inputs aspiracionales como si existieran.
- ❌ No distinguir entre inputs actuales e inputs futuros.
- ❌ Omitir inputs externos al ecosistema.

---

## Sección 4: Outputs (Salidas)

### Propósito
Documentar qué produce el Lab para el ecosistema. [Decisión] Diferente de Assets (Sección 6) — outputs son resultados operativos, no necesariamente activos reutilizables.

### Guía
- Incluir tanto outputs al ecosistema como outputs propios del Lab.
- Clasificar: Lab-Private, Lab-Published, LabOS-Shared.
- Si el Lab está en `idea`, la mayoría serán [Hipótesis].

### Ejemplo
> - Resultados de backtesting (Lab-Private) [Hipótesis]
> - Metodología de evaluación de estrategias (Lab-Published) [Hipótesis]

### Errores comunes
- ❌ Confundir outputs con productos vendibles (eso es Sección 7).
- ❌ Listar outputs sin clasificación de boundary.
- ❌ Presentar outputs hipotéticos como hechos.

---

## Sección 5: Knowledge Produced (Conocimiento Producido)

### Propósito
Identificar los tipos de conocimiento que el Lab genera. [Decisión] Pendiente de formalización completa por Package 002 (Knowledge Architecture).

### Guía
- Listar dominios de conocimiento, no documentos específicos.
- Clasificar visibilidad: Private, Published, Restricted.
- Referencia: [Knowledge_Sharing_Protocol](./lab-integration-framework.md).

### Ejemplo
> - Conocimiento sobre microestructura de mercados crypto (Private) [Hipótesis]
> - Patrones de efectividad en estrategias de scalping (Published) [Hipótesis]

### Errores comunes
- ❌ Confundir conocimiento con documentos (un documento es un ASSET tipo documento).
- ❌ Marcar todo como Private — considerar qué beneficia al ecosistema.
- ❌ Inventar conocimiento que el Lab no ha producido.

---

## Sección 6: Assets Produced (Activos Producidos)

### Propósito
Listar los activos reutilizables que el Lab produce o podría producir. [Decisión] Usar la taxonomía canónica de 7 tipos (per [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md)).

### Guía
- Clasificar cada activo en uno de los 7 tipos canónicos: documento, template, dataset, herramienta, componente, framework, playbook.
- Indicar estado actual: borrador, validado, productizado.
- Indicar compartibilidad: 5 tipos compartibles por defecto, 2 Lab-Private por defecto.
- Si no existen activos aún, documentar los ESPERADOS con clasificación [Hipótesis].

### Ejemplo
> | Activo | Tipo canónico | Estado | Compartible |
> |--------|--------------|--------|-------------|
> | Framework de backtesting | framework | borrador | Sí (default) |
> | Playbook de evaluación de estrategia | playbook | borrador | No (Lab-Private default) |

### Errores comunes
- ❌ Usar tipos no canónicos (e.g., "library", "module" — usar herramienta o componente).
- ❌ No indicar estado del activo.
- ❌ Asumir que componentes y playbooks son compartibles sin publicación explícita.

---

## Sección 7: Products Produced (Productos Producidos)

### Propósito
Documentar entregables comerciales del Lab, si existen. [Decisión] Nota: "Product" como entidad formal está pendiente de definición (Package 004).

### Guía
- Solo documentar si el Lab tiene un producto identificado o una hipótesis de producto concreta.
- Marcar como [Hipótesis] hasta que exista transacción real.
- Referenciar Revenue_Thesis si existe.
- Si el Lab está en `idea`, esta sección será probablemente UNKNOWN.

### Ejemplo
> No existen productos actualmente. [Hecho]
> Hipótesis de producto: "Estrategias algorítmicas de scalping pueden generar retornos consistentes con gestión de riesgo automatizada." [Hipótesis]

### Errores comunes
- ❌ Listar productos que no existen como si estuvieran disponibles.
- ❌ Confundir activos con productos (un activo se convierte en producto cuando se productiza y tiene usuarios).
- ❌ Omitir la hipótesis de producto cuando existe.

---

## Sección 8: Shared Resources (Recursos Compartidos)

### Propósito
Documentar qué recursos de LabOS consume el Lab. [Decisión]

### Guía
- Listar Shared_Services de LabOS que el Lab utiliza o planea utilizar.
- Servicios compartidos estándar (per lab-boundaries.md): documentation templates, steering files, package structure conventions, research methodology, quality gate definitions, portfolio-level reporting.
- Ser honesto: si no se usa un recurso compartido, no listarlo.

### Ejemplo
> - Research methodology (Package 001) [Hecho]
> - Documentation templates [Hecho]
> - Quality gate definitions [Hecho]
> - Steering files [Hecho]

### Errores comunes
- ❌ Listar recursos compartidos que no existen aún en LabOS.
- ❌ Confundir recursos compartidos con inputs externos.
- ❌ No actualizar cuando se empiezan a usar nuevos recursos.

---

## Sección 9: Private Resources (Recursos Privados)

### Propósito
Documentar qué pertenece exclusivamente al Lab. [Decisión] Estos recursos no son accesibles por otros Labs ni por LabOS sin consentimiento explícito.

### Guía
- Incluir: repositorios, datos, estrategias, configuraciones, secretos.
- Ser exhaustivo — todo lo no listado explícitamente puede generar ambigüedad.
- Referenciar Lab_Boundary classification: Lab-Private.

### Ejemplo
> - Estrategias de trading (código, parámetros, configuraciones) [Hipótesis]
> - Datos propietarios de backtesting [Hipótesis]
> - Credenciales de exchanges [Hipótesis]
> - Resultados de performance de estrategias [Hipótesis]

### Errores comunes
- ❌ No documentar secretos y credenciales como recursos privados.
- ❌ Clasificar como privado algo que debería ser Lab-Published (e.g., metodologías genéricas).
- ❌ Olvidar datos sensibles financieros.

---

## Sección 10: Dependencies (Dependencias)

### Propósito
Documentar qué requiere el Lab para operar. [Decisión] Incluye dependencias internas (LabOS) y externas (servicios, herramientas, conocimiento).

### Guía
- Separar: dependencias de LabOS, dependencias de otros Labs, dependencias externas.
- Para cada dependencia: qué pasa si no está disponible.
- Ser honesto sobre dependencias externas que no se controlan.

### Ejemplo
> | Dependencia | Tipo | Criticidad | Si no disponible |
> |-------------|------|------------|-----------------|
> | Datos de mercado crypto | Externa | Alta | Lab no puede operar backtesting |
> | Research methodology | LabOS | Media | Lab puede operar con método propio |

### Errores comunes
- ❌ No documentar dependencias externas.
- ❌ No evaluar impacto de indisponibilidad.
- ❌ Listar dependencias aspiracionales como reales.

---

## Sección 11: Consumers (Consumidores)

### Propósito
Documentar quién usa los outputs del Lab. [Decisión]

### Guía
- Incluir consumidores internos (otros Labs, LabOS) y externos (si existen).
- Para Labs en `idea`, esta sección será probablemente UNKNOWN o minimalista.
- No inventar consumidores — si no hay, documentar que no hay.

### Ejemplo
> - Consumidores internos: Ninguno confirmado. [Hecho]
> - Consumidores externos: Ninguno. [Hecho]
> - Consumidor potencial: Atlas Wealth Labs (si metodologías de evaluación son publicadas). [Hipótesis]

### Errores comunes
- ❌ Inventar consumidores para justificar la existencia del Lab.
- ❌ Confundir "podría consumir" con "consume actualmente".
- ❌ No distinguir entre consumidores internos y externos.

---

## Sección 12: Quality Gates (Quality Gates)

### Propósito
Definir criterios observables para evaluar la salud del Lab. [Decisión]

### Guía
- Mínimo 1 quality gate por Lab. [Decisión]
- Deben ser observables y verificables, no subjetivos.
- Proporcionales al Lab_State — un Lab en `idea` tiene gates más simples.
- Alinear con criterios de transición del portfolio model.

### Ejemplo
> | Gate | Criterio | Frecuencia | Estado `idea` |
> |------|----------|------------|---------------|
> | Hipótesis documentada | Hipótesis de monetización con 3 campos mínimos | Una vez | Requerido |
> | Actividad mínima | ≥1 acción documentada por período de review | Por review cycle | Requerido |

### Errores comunes
- ❌ Quality gates inalcanzables para el estado actual del Lab.
- ❌ Gates subjetivos ("el Lab está progresando bien").
- ❌ Demasiados gates para un Lab en estado temprano (INV-05).

---

## Sección 13: Metrics (Métricas)

### Propósito
Definir indicadores medibles del performance del Lab. [Decisión] Mínimo 1 métrica por Lab.

### Guía
- Las métricas deben ser recolectables con el esfuerzo actual (sin tooling nuevo).
- Proporcionales al estado: un Lab en `idea` mide actividad, no revenue.
- No confundir métricas con quality gates (gates son pass/fail, métricas son numéricas).

### Ejemplo
> | Métrica | Definición | Target (idea) | Frecuencia |
> |---------|-----------|---------------|------------|
> | Horas invertidas | Horas dedicadas al Lab en el período | >0 si activo | Mensual |
> | Activos producidos | Cantidad de activos documentados | ≥1 para avanzar a explorando | Mensual |

### Errores comunes
- ❌ Métricas que requieren tooling que no existe.
- ❌ Métricas de revenue para Labs en `idea`.
- ❌ No definir frecuencia de medición.

---

## Sección 14: Risks (Riesgos)

### Propósito
Identificar riesgos para la operación del Lab. [Decisión] Mínimo 1 riesgo por Lab.

### Guía
- Incluir riesgos técnicos, de mercado, operativos y de capacidad.
- Para cada riesgo: probabilidad (alta/media/baja), impacto (alto/medio/bajo), mitigación.
- Ser honesto — riesgos omitidos no desaparecen.

### Ejemplo
> | Riesgo | Probabilidad | Impacto | Mitigación |
> |--------|-------------|---------|------------|
> | Pérdida financiera por estrategia defectuosa | Alta | Alto | Backtesting obligatorio, gestión de riesgo automatizada, nunca operar con capital significativo sin validación |

### Errores comunes
- ❌ No documentar riesgos financieros para Labs de trading.
- ❌ Mitigaciones vagas ("tener cuidado").
- ❌ Omitir riesgo de capacidad (fundador con tiempo limitado).

---

## Sección 15: Review Cycle (Ciclo de Revisión)

### Propósito
Definir la cadencia y criterios de evaluación periódica del Lab. [Decisión] Intervalo entre 30 y 180 días. [Decisión]

### Guía
- Proporcional al Lab_State (per architecture-baseline-v1.md Sección 7):
  - `idea`: sin revisión formal obligatoria (0 min).
  - `explorando`: 15 min/mes.
  - `validando`: 30 min/mes.
  - `operando`: 1h/mes.
  - `pausado`: sin revisión.
- Definir: qué se revisa, quién revisa, qué output produce la revisión.
- En nivel SOLO: el fundador se auto-revisa.

### Ejemplo
> | Campo | Valor |
> |-------|-------|
> | Intervalo | 90 días (Lab en estado `idea`) |
> | Duración | 0 min (sin revisión formal en `idea`) |
> | Revisor | Fundador |
> | Output | Decisión: mantener en `idea`, avanzar a `explorando`, o pausar |

### Errores comunes
- ❌ Review cycles demasiado frecuentes para Labs en `idea` (viola INV-05).
- ❌ No definir output concreto de la revisión.
- ❌ Plazos que exceden 180 días.

---

## Reglas Generales del Template

1. Toda sección que no pueda poblarse se marca como "pendiente" con fecha límite ≤90 días. [Decisión]
2. Si más de 5 secciones están pendientes simultáneamente, se requiere una evaluación de integración. [Decisión]
3. Para Labs en estado `idea`, es ACEPTABLE que la mayoría de secciones sean hipótesis o pendientes. [Decisión]
4. El Lab Contract acepta al proyecto en su estado actual — no requiere modificaciones al proyecto. [Decisión]

---

## Cross-references

- [lab-integration-framework.md](./lab-integration-framework.md) — Principios de integración
- `lab-boundaries.md` — HISTORICAL_REFERENCE_MISSING; referencia histórica preservada sin inventar reemplazo
- [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md) — Taxonomía de activos (Sección 6)
- [Package 000 — 012-portfolio-model.md](../package-000-foundation/012-portfolio-model.md) — Lab States
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Governance nivel SOLO

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 6        | 11%        |
| [Hipótesis]   | 8        | 14%        |
| [Decisión]    | 42       | 75%        |
| [Visión]      | 0        | 0%         |

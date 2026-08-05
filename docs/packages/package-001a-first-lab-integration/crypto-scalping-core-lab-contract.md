# Lab Contract — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Lab** | Crypto Scalping Core |
| **Lab ID** | LAB-CSC |
| **Short** | CSC |
| **Dominio** | Trading cuantitativo |
| **Estado** | explorando |
| **Versión del contrato** | 1.0 |
| **Fecha de creación** | 2025-07-24 |
| **Última revisión** | 2025-07-24 |
| **Próxima revisión** | 2025-08-24 |
| **Fundador/Owner** | Joel Diaz |
| **Estado del contrato** | APPROVED |

---

## Approval Record

| Campo | Valor |
|-------|-------|
| **Approval status** | APPROVED |
| **Approved by** | Joel Diaz (Fundador) |
| **Approval date** | 2025-07-30 |
| **Conditions** | None (incondicional) |
| **Decision reference** | [founder-decisions-package-001a-batch4.md](./founder-decisions-package-001a-batch4.md) (FD-B4-01) |
| **Non-blocking remediations** | 7 ítems preservados en [crypto-scalping-core-remediation-plan.md](./crypto-scalping-core-remediation-plan.md) |

[Decisión] Este contrato fue aprobado incondicionalmente por el fundador. Las 15 secciones principales permanecen sin modificación. Las remediaciones P2/P3 se ejecutarán orgánicamente según sus triggers naturales.

---

## Sección 1 — Identity (Identidad)

| Campo | Valor | Clasificación |
|-------|-------|---------------|
| Nombre del Lab | Crypto Scalping Core | [Hecho] |
| Short name | CSC | [Decisión] |
| Lab ID | LAB-CSC | [Decisión] |
| Owner | Joel Diaz (Fundador) | [Hecho] |
| Lab State | `explorando` | [Decisión] |
| Fecha de integración | 2025-07-24 | [Hecho] |
| Repositorio | https://github.com/joelramone/crypto-scalping-core | [Hecho] |
| Branch principal | main | [Hecho] |
| Fuente de verdad | Remote main branch (GitHub) | [Decisión] |
| Dominio | Trading cuantitativo — scalping algorítmico en criptomonedas | [Hecho] |

**Justificación del estado `explorando`:** 14 experimentos formales, 567 optimizer runs, pipeline de 8 etapas operativo, 4 estrategias implementadas, investigación activa. Aprobado por fundador el 2025-07-24 (ref: FD-B3-01). [Decisión]

---

## Sección 2 — Mission (Misión)

> "Investigar sistemáticamente estrategias de scalping cuantitativo en mercados crypto, produciendo conocimiento reproducible, hipótesis validables y activos reutilizables de investigación — sin afirmar rentabilidad ni operar capital real hasta que la evidencia lo justifique." [Decisión]

**Notas sobre la misión:**
- Enfocada en INVESTIGACIÓN, no en trading operativo. [Decisión]
- No afirma rentabilidad — ninguna estrategia ha logrado PF > 1.0. [Hecho]
- Orientada a la producción de conocimiento y activos, no solo a resultados de trading. [Decisión]
- Compatible con el Knowledge-to-Value Pipeline de LabOS (Research → Knowledge → Assets). [Hecho]

---

## Sección 3 — Scope (Alcance)

### Incluido (IN)

| Área | Descripción | Clasificación |
|------|-------------|---------------|
| Market-data research | Descarga, validación y análisis de datos de mercado crypto | [Hecho] |
| Feature engineering | Creación de indicadores y señales derivadas de datos OHLCV | [Hecho] |
| Strategy hypotheses | Formulación y documentación de hipótesis de estrategias | [Hecho] |
| Backtesting | Evaluación histórica de estrategias contra datos reales | [Hecho] |
| Simulation | Ejecución simulada sin capital real (paper trading) | [Hecho] |
| Optimization | Grid search de parámetros, leaderboard ranking | [Hecho] |
| Quality analysis | Análisis de calidad de señales, feature quartiles, quality score | [Hecho] |
| Experiment documentation | Journals formales con resultados y lecciones | [Hecho] |
| KO generation | Identificación y formalización de Knowledge Objects | [Decisión] |
| Reusable research assets | Frameworks, templates y herramientas de investigación | [Decisión] |

### Excluido (OUT)

| Área | Razón de exclusión | Clasificación |
|------|-------------------|---------------|
| Employer/corporate | Separación absoluta corporativo/personal | [Decisión] |
| Managed investments | No es un servicio de gestión de inversiones | [Decisión] |
| Financial advice | No tiene licencia ni calificación para advisory | [Decisión] |
| Guaranteed returns | Expectancy negativa en 100% de configuraciones — sería fraudulento | [Hecho] |
| Personal balances | Información financiera personal fuera de alcance | [Decisión] |
| Credentials en repo | Secretos nunca en repositorio | [Decisión] |
| Brokerage operations | No opera cuentas de terceros | [Decisión] |
| Production live trading | Sin aprobación separada y sin edge demostrado | [Decisión] |

---

## Sección 4 — Ownership (Propiedad)

| Aspecto | Regla | Clasificación |
|---------|-------|---------------|
| Owner del Lab | Joel Diaz (Fundador) | [Hecho] |
| Código del Lab | Propiedad del Lab | [Decisión] |
| Research producido | Propiedad del Lab | [Decisión] |
| Transformaciones y derivados | Propiedad del Lab | [Decisión] |
| Experimentos y resultados | Propiedad del Lab | [Decisión] |
| Reportes generados | Propiedad del Lab | [Decisión] |
| Artefactos de investigación | Propiedad del Lab | [Decisión] |
| Market data externo (crudo) | Proveniencia EXTERNA — RESTRINGIDO hasta verificar licencia | [Decisión] |
| Market data procesado/derivado | Propiedad del Lab (transformación propia) | [Decisión] |
| Información corporativa | EXCLUIDO — absolutamente fuera del Lab | [Decisión] |
| LabOS authority | Solo sobre objetos promovidos explícitamente (KOs/Assets shared) | [Decisión] |
| Authorship/provenance | Preservada después de promoción a LabOS-Shared | [Decisión] |

---

## Sección 5 — Boundaries (Límites)

### Lab-Private (por defecto)

| Contenido | Justificación |
|-----------|---------------|
| Estrategias de trading (código, parámetros, lógica de entrada/salida) | Ventaja competitiva directa [Decisión] |
| Configuraciones de riesgo | Datos operativos sensibles [Decisión] |
| Resultados no validados | Performance data privada [Decisión] |
| Experimentos en progreso | Proceso de descubrimiento propietario [Decisión] |
| Credenciales, API keys, cuentas | Seguridad crítica — NUNCA en repositorio [Decisión] |
| Balances y datos financieros personales | Información financiera privada del fundador [Decisión] |

### Lab-Published (por autorización explícita del fundador)

| Contenido | Condición |
|-----------|-----------|
| Reportes de investigación | Cuando el fundador autoriza publicación [Decisión] |
| Metodología genérica | Cuando no compromete ventaja competitiva [Decisión] |
| Hallazgos generales | Cuando son genéricos, no específicos a estrategia [Decisión] |

### LabOS-Shared (tras promoción explícita)

| Contenido | Mecanismo |
|-----------|-----------|
| Knowledge Objects promovidos | Per Package 002 sharing rules, reference-based [Decisión] |
| Assets promovidos | Per knowledge-to-asset-handoff criteria [Decisión] |

### Externo

| Entidad | Relación |
|---------|----------|
| Binance (exchange) | Proveedor de datos — no controlado por el Lab [Hecho] |
| Otros exchanges/proveedores | Potenciales fuentes de datos — no controlados [Hecho] |

### Exclusión absoluta

| Entidad | Razón |
|---------|-------|
| BYMA | Separación corporativa/personal [Decisión] |
| NRTC | Separación corporativa/personal [Decisión] |
| SentinelOps | Separación corporativa/personal [Decisión] |
| Información del empleador | Absolutamente excluida del Lab y de LabOS [Decisión] |

---

## Sección 6 — Inputs (Entradas)

| Input | Origen | Clasificación boundary | Licencia | Estado |
|-------|--------|----------------------|----------|--------|
| Market data (Binance API OHLCV) | Binance USD-M Futures | Externo | RESTRINGIDO — ToS no verificado | [Hecho] |
| Strategy parameters | Definidos por fundador | Lab-Private | N/A — propio | [Hecho] |
| Research hypotheses | Formuladas por fundador | Lab-Private | N/A — propio | [Hecho] |
| Software dependencies | PyPI (requirements.txt) | Externo | Open source (variada) | [Hecho] |
| Founder decisions | Joel Diaz (humano) | SOLO governance | N/A | [Hecho] |

---

## Sección 7 — Activities (Actividades)

### Pipeline de 8 etapas (OPERATIVO)

| # | Etapa | Herramienta | Estado | Clasificación |
|---|-------|-------------|--------|---------------|
| 1 | Ingestion | `app/research/download_data.py` | OPERATIVO | [Hecho] |
| 2 | Validation | Feature generation con filtros | OPERATIVO | [Hecho] |
| 3 | Features | `app/research/features.py`, `app/data/features.py` | OPERATIVO | [Hecho] |
| 4 | Backtesting | `app/research/backtester.py` | OPERATIVO | [Hecho] |
| 5 | Optimization | `app/optimization/grid_search.py` | OPERATIVO | [Hecho] |
| 6 | Quality Analysis | `app/research/signal_quality/` | OPERATIVO | [Hecho] |
| 7 | Candidate Analysis | `app/research/discovery/` | OPERATIVO | [Hecho] |
| 8 | Reporting | Auto-generated journals + reports | OPERATIVO | [Hecho] |

### Actividades parcialmente implementadas

| Actividad | Código | Outputs | Estado |
|-----------|--------|---------|--------|
| Walk-forward validation | `app/optimization/walk_forward.py` EXISTE | Directorio vacío | PARCIAL [Hecho] |
| Monte Carlo simulation | `app/montecarlo.py` EXISTE | Directorio vacío | PARCIAL [Hecho] |

### Actividades adicionales

| Actividad | Descripción | Estado |
|-----------|-------------|--------|
| Experiment journaling | Registro formal de experimentos (EXP-NNNNNN.md) | OPERATIVO [Hecho] |
| Decision recording | Documentación de decisiones de investigación | OPERATIVO [Hecho] |

---

## Sección 8 — Outputs (Salidas)

| Output | Cantidad existente | Ubicación | Clasificación |
|--------|-------------------|-----------|---------------|
| Experiment journals | 14 | `research/journal/EXP-*.md` | Lab-Private [Hecho] |
| Leaderboard CSVs | 8 | `research/leaderboards/` | Lab-Private [Hecho] |
| Research reports | 2 | `research/reports/` | Lab-Private [Hecho] |
| Candidate signal CSVs | 1 | `research/candidate_signals/` | Lab-Private [Hecho] |
| Strategy implementations | 4 (TODAS status RESEARCH) | `app/strategies/` | Lab-Private [Hecho] |
| Rejected/inconclusive hypotheses | Documentados en journals | `research/journal/` | Lab-Private [Hecho] |
| Knowledge Object candidates | 5 identificados | Documentados en Batch 2 | Lab-Private [Hecho] |
| Asset candidates | 5 identificados | Documentados en Batch 2 | Lab-Private [Hecho] |

**NOTA CRÍTICA:** Ningún output demuestra rentabilidad. [Hecho] Todos los resultados son de INVESTIGACIÓN.

---

## Sección 9 — Knowledge (Conocimiento)

| Aspecto | Regla | Clasificación |
|---------|-------|---------------|
| Framework de referencia | Package 002 — Knowledge Architecture | [Hecho] |
| Visibilidad por defecto | Lab-Private (PRIVATE) | [Decisión] |
| KO candidates identificados | 5 (ref: crypto-scalping-core-knowledge-object-candidates.md) | [Hecho] |
| KO promovidos a LabOS-Shared | 0 (ninguno aún) | [Hecho] |
| Ownership | Lab (hasta promoción explícita) | [Decisión] |
| Mecanismo de promoción | Reference-based, per Package 002 sharing rules | [Decisión] |
| Fuente de verdad | Repositorio del Lab (GitHub main) | [Decisión] |
| Conflicto resolution | Per knowledge-conflict-resolution.md | [Decisión] |

### KO candidates (resumen)

| ID | Tipo | Confianza | Prioridad |
|----|------|-----------|-----------|
| KO-1 | finding (timeframe) | MEDIO | P2 |
| KO-2 | finding (parameter importance) | MEDIO | P2 |
| KO-3 | finding (quality_score filtering) | MEDIO | P3 |
| KO-4 | finding (mean_reversion no rentable) | ALTO | P2 |
| KO-5 | methodology (pipeline) | ALTO | P1 |

---

## Sección 10 — Assets (Activos)

| Aspecto | Regla | Clasificación |
|---------|-------|---------------|
| Taxonomía de referencia | 7 tipos canónicos (ADR-0002) | [Hecho] |
| Asset candidates identificados | 5 (ref: crypto-scalping-core-asset-candidates.md) | [Hecho] |
| Assets validados | 0 (ninguno cumple 4 condiciones de promoción) | [Hecho] |
| Lifecycle actual | `borrador` (ninguno validado) | [Hecho] |
| Mecanismo de promoción | Per knowledge-to-asset-handoff criteria | [Decisión] |
| Reuse boundaries | Lab-Private hasta publicación explícita | [Decisión] |

### Asset candidates (resumen)

| ID | Nombre | Tipo canónico | Esfuerzo | Prioridad |
|----|--------|--------------|----------|-----------|
| ASSET-1 | Framework de backtesting | Herramienta | MEDIO | P2 |
| ASSET-2 | Optimizador Grid Search | Herramienta | MEDIO | P2 |
| ASSET-3 | Template de experiment journal | Template | BAJO | P1 |
| ASSET-4 | Pipeline de discovery report | Herramienta | ALTO | P3 |
| ASSET-5 | Pipeline de quality analysis | Herramienta | ALTO | P3 |

---

## Sección 11 — Dependencies (Dependencias)

### Dependencias internas (entre módulos)

| Módulo | Depende de | Dependido por |
|--------|-----------|---------------|
| `data/` | python-binance, pandas | features, strategies, backtester |
| `strategies/` | features, config | agents, backtester |
| `optimization/` | backtester, strategies | (standalone) |
| `research/` | optimization, backtester | (standalone) |

### Dependencias externas

| Dependencia | Tipo | Criticidad | Sin pin |
|-------------|------|------------|---------|
| python-binance | Library | ALTA — única fuente de datos | ⚠️ Sí |
| pandas | Library | CRÍTICA — core del pipeline | ⚠️ Sí |
| Flask | Library | BAJA — solo dashboard | ⚠️ Sí |
| plotly | Library | BAJA — solo gráficos | ⚠️ Sí |
| pydantic>=2,<3 | Library | MEDIA — config validation | Con rango |

### Dependencias de infraestructura

| Servicio | Tipo | Criticidad | Reemplazable |
|----------|------|------------|-------------|
| Binance API | Exchange REST | ALTA — data only | Parcialmente [Hecho] |
| GitHub | Git hosting | BAJA | Sí [Hecho] |

### Dependencia humana

| Recurso | Tipo | Criticidad |
|---------|------|------------|
| Joel Diaz (Fundador) | Decision-maker | CRÍTICA — todas las decisiones [Hecho] |

### Dependencia con LabOS

| Aspecto | Estado |
|---------|--------|
| Runtime dependency | **NINGUNA** [Hecho] |
| Shared infrastructure | **NINGUNA** [Hecho] |
| Integración operativa | Solo gobernanza (documentación, clasificación) [Decisión] |

---

## Sección 12 — Risks (Riesgos)

5 riesgos identificados y aprobados por el fundador (2025-07-23, ref: FD-B1-03): [Hecho]

| ID | Riesgo | Probabilidad | Impacto | Mitigación |
|----|--------|-------------|---------|------------|
| A | Validez de investigación — resultados in-sample no generalizan | MEDIA | ALTO | Walk-forward, Monte Carlo, out-of-sample validation [Decisión] |
| B | Riesgo financiero — pérdida de capital si se opera prematuramente | MEDIA | CRÍTICO | NO operar capital real sin PF > 1.0 validado + walk-forward + Monte Carlo [Decisión] |
| C | Dependencia de datos — Binance API como única fuente | MEDIA | ALTO | Evaluar fuentes alternativas; datos locales como backup parcial [Decisión] |
| D | Overfitting — optimización produce estrategias que solo funcionan en-sample | ALTA | ALTO | Walk-forward obligatorio antes de promover; Monte Carlo para robustez [Decisión] |
| E | Sostenibilidad operacional — fundador con tiempo limitado | ALTA | MEDIO | Proporicionalidad de proceso (INV-05); review 15min/mes; priorizar por evidencia [Decisión] |

### Triggers de revisión de riesgos

| Trigger | Acción |
|---------|--------|
| PF > 1.0 obtenido | Activar walk-forward inmediato; evaluar risk B [Decisión] |
| Binance API deprecated/restricted | Evaluar alternativas; risk C [Decisión] |
| >30 días sin actividad | Evaluar risk E; considerar pausa [Decisión] |
| Estrategia candidata a live | Revisar todos los riesgos; aprobación explícita del fundador [Decisión] |

---

## Sección 13 — Governance (Gobernanza)

| Aspecto | Implementación | Clasificación |
|---------|---------------|---------------|
| Nivel | SOLO (1 operador, pre-revenue) | [Hecho] |
| Decision-maker | Joel Diaz (Fundador) — decide todo | [Hecho] |
| Validación de resultados | Fundador valida | [Decisión] |
| Publicación de outputs | Solo con autorización explícita del fundador | [Decisión] |
| Sharing de KOs/Assets | Reference-based, requiere aprobación del fundador | [Decisión] |
| Asset promotion | Fundador verifica elegibilidad (4 condiciones) | [Decisión] |
| State transitions | Decisión del fundador con evidencia documentada | [Decisión] |
| Review cycle | 15 min/mes (cadence de `explorando`) | [Decisión] |
| Event-triggered reviews | Per risk triggers (Sección 12) | [Decisión] |
| Escalación | No aplica — 1 decision-maker | [Hecho] |

---

## Sección 14 — Autonomy and Decoupling (Autonomía y Desacoplamiento)

| Aspecto | Estado | Clasificación |
|---------|--------|---------------|
| Autonomía operacional | **CONFIRMADA** — CSC opera independientemente de LabOS | [Hecho] |
| Runtime dependencies con LabOS | CERO | [Hecho] |
| Shared databases con LabOS | CERO | [Hecho] |
| Import de módulos LabOS | CERO | [Hecho] |
| Integración futura con LabOS | OPCIONAL ÚNICAMENTE | [Decisión] |

### Principio de Decoupling

Si se remueve LabOS del ecosistema: [Decisión]
- **Se pierde:** gobernanza, clasificación, trazabilidad, reporting de portfolio, sharing protocol
- **Se conserva:** TODO el código funciona, datos almacenados localmente, pipeline ejecutable, resultados preservados
- **NO se afecta:** capacidad operativa del Lab

### Verificación de autonomía

| Test | Resultado |
|------|-----------|
| ¿El código ejecuta sin LabOS? | SÍ — Python standalone [Hecho] |
| ¿Los datos se almacenan localmente? | SÍ — `data/`, `research/` en el repositorio [Hecho] |
| ¿Hay service calls a LabOS? | NO — cero llamadas [Hecho] |
| ¿El pipeline depende de LabOS infra? | NO — solo depende de Binance API + Python [Hecho] |

---

## Sección 15 — Evolution and Exit (Evolución y Salida)

### Estado actual y transiciones

| Campo | Valor |
|-------|-------|
| Estado actual | `explorando` [Decisión] |
| Fecha de asignación | 2025-07-24 |
| Estado anterior | `idea` (implícito antes de Batch 3) |

### Transiciones posibles

| Transición | Condición | Evidencia requerida |
|-----------|-----------|---------------------|
| `explorando` → `validando` | PF > 1.0 con out-of-sample + walk-forward | Walk-forward positivo, Monte Carlo > p5 positivo, fundador aprueba [Decisión] |
| `explorando` → `pausado` | Decisión del fundador con razón documentada | Razón explícita + fecha [Decisión] |
| `explorando` → `idea` | Degradación por inactividad (regresión) | >90 días sin actividad sin decisión explícita de continuación [Decisión] |

### Pausa

| Aspecto | Regla |
|---------|-------|
| Trigger | Decisión del fundador con razón documentada [Decisión] |
| Duración máxima | Sin límite formal, pero >90 días sin justificación → considerar archivo [Decisión] |
| Restart condition | Resolver razón de pausa + asignar tiempo [Decisión] |

### Archivo

| Aspecto | Regla |
|---------|-------|
| Trigger | Sin actividad en 90 días sin decisión explícita de continuación [Decisión] |
| Preservación | KOs retenidos per Package 002; Assets preservados; código en GitHub [Decisión] |
| Reversibilidad | Posible — re-activar con decisión del fundador [Decisión] |

### Product handoff

| Aspecto | Regla |
|---------|-------|
| Requisito previo | Estado `validando` + monetization hypothesis validada con señal de demanda [Decisión] |
| No aplicable actualmente | Lab en `explorando`, sin edge demostrado [Hecho] |

### Closure (Cierre definitivo)

| Aspecto | Regla |
|---------|-------|
| Trigger | Decisión del fundador [Decisión] |
| KOs producidos | Retenidos per Package 002 rules [Decisión] |
| Assets producidos | Preservados en estado final [Decisión] |
| Código | Permanece en GitHub (read-only) [Decisión] |

---

## Cross-references

- [founder-decisions-package-001a-batch3.md](./founder-decisions-package-001a-batch3.md) — Decisión de Lab State
- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisiones de ownership, risks, autonomy
- [crypto-scalping-core-boundary-analysis.md](./crypto-scalping-core-boundary-analysis.md) — Análisis detallado de boundaries
- [crypto-scalping-core-research-workflow-map.md](./crypto-scalping-core-research-workflow-map.md) — Pipeline de 8 etapas
- [crypto-scalping-core-strategy-inventory.md](./crypto-scalping-core-strategy-inventory.md) — 4 estrategias (TODAS RESEARCH)
- [crypto-scalping-core-knowledge-object-candidates.md](./crypto-scalping-core-knowledge-object-candidates.md) — 5 KO candidates
- [crypto-scalping-core-asset-candidates.md](./crypto-scalping-core-asset-candidates.md) — 5 Asset candidates
- [crypto-scalping-core-dependency-map.md](./crypto-scalping-core-dependency-map.md) — Dependencias detalladas
- [crypto-scalping-core-monetization-hypothesis.md](./crypto-scalping-core-monetization-hypothesis.md) — Hipótesis de monetización
- [lab-contract-template.md](./lab-contract-template.md) — Template utilizado
- [../../architecture/architecture-baseline-v1.md](../../architecture/architecture-baseline-v1.md) — Baseline arquitectónico
- [../../decisions/0002-asset-taxonomy-consolidation.md](../../decisions/0002-asset-taxonomy-consolidation.md) — Taxonomía de activos

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 52       | 38%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 85       | 62%        |
| [Visión]      | 0        | 0%         |

> **Nota:** Alto porcentaje de decisiones es correcto — un Lab Contract es fundamentalmente un documento de decisiones y reglas. Los hechos corresponden a evidencia verificable del repositorio y del ecosistema. Cero hipótesis porque todas las afirmaciones son verificables o son decisiones explícitas.

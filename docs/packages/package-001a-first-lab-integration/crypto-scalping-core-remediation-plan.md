# Plan de Remediación — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Plan de remediación consolidado |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 3 — Lab Contract & Compliance |
| **Fecha** | 2025-07-24 |

---

## Propósito

Consolidar todas las remediaciones no-bloqueantes identificadas durante la evaluación de compliance del Lab Contract. [Hecho] Ninguna de estas remediaciones bloquea la aprobación del contrato — todas son mejoras documentadas para ejecución futura.

---

## Criterio de inclusión

Solo se incluyen remediaciones que: [Decisión]
1. Fueron identificadas en evaluaciones formales (Batch 1, 2 o 3)
2. Tienen severidad P2 o P3 (no bloqueantes)
3. Tienen owner y evidencia de completión definidos
4. NO requieren modificación del Lab Contract para resolverse

---

## REM-001: Verificación de licencia de dataset

| Campo | Valor |
|-------|-------|
| **ID** | REM-001 |
| **Fuente** | Compliance evaluation — Dataset License (P2) |
| **Descripción** | Verificar los Terms of Service de Binance respecto al uso de datos históricos OHLCV descargados vía API para research/backtesting. Determinar si el uso actual es compatible con ToS y documentar el resultado. |
| **Severidad** | P2 |
| **Owner** | Joel Diaz (Fundador) |
| **Target** | Antes de cualquier publicación de datos derivados o productización |
| **Evidencia necesaria** | Documento con extracto relevante de Binance ToS + clasificación: COMPATIBLE / RESTRINGIDO / INCOMPATIBLE |
| **Blocking status** | **NO** — no bloquea Lab Contract ni operación de research |
| **Completión criteria** | Documento `binance-data-license-review.md` creado con conclusión explícita |

---

## REM-002: Walk-forward execution o deferral documentado

| Campo | Valor |
|-------|-------|
| **ID** | REM-002 |
| **Fuente** | Research workflow map — Etapa 9 (parcial) |
| **Descripción** | El código de walk-forward validation existe (`app/optimization/walk_forward.py`) pero no hay outputs generados. Opciones: (a) ejecutar walk-forward en estrategia candidata cuando PF > 1.0, o (b) documentar deferral explícito con razón. |
| **Severidad** | P2 |
| **Owner** | Joel Diaz (Fundador) |
| **Target** | Cuando una estrategia alcance PF > 1.0 in-sample (trigger natural) |
| **Evidencia necesaria** | Opción A: outputs en `research/walk_forward/` con resultados. Opción B: nota de deferral en experiment journal |
| **Blocking status** | **NO** — no bloquea Lab Contract. Bloquea transición a `validando` |
| **Completión criteria** | Directorio `research/walk_forward/` con contenido O documento de deferral explícito |

---

## REM-003: Monte Carlo execution o deferral documentado

| Campo | Valor |
|-------|-------|
| **ID** | REM-003 |
| **Fuente** | Research workflow map — Etapa 10 (parcial) |
| **Descripción** | El código de Monte Carlo simulation existe (`app/montecarlo.py`) pero no hay outputs generados. Opciones: (a) ejecutar Monte Carlo en estrategia candidata cuando PF > 1.0, o (b) documentar deferral explícito con razón. |
| **Severidad** | P2 |
| **Owner** | Joel Diaz (Fundador) |
| **Target** | Cuando una estrategia alcance PF > 1.0 in-sample (trigger natural) |
| **Evidencia necesaria** | Opción A: outputs en `research/monte_carlo/` con resultados. Opción B: nota de deferral en experiment journal |
| **Blocking status** | **NO** — no bloquea Lab Contract. Bloquea transición a `validando` |
| **Completión criteria** | Directorio `research/monte_carlo/` con contenido O documento de deferral explícito |

---

## REM-004: Dependency pinning

| Campo | Valor |
|-------|-------|
| **ID** | REM-004 |
| **Fuente** | Dependency map — riesgo de reproducibilidad |
| **Descripción** | La mayoría de dependencias en `requirements.txt` no tienen versiones pinned (solo pydantic y tabulate tienen rangos). Esto genera riesgo de que el pipeline deje de funcionar por breaking changes en dependencias. Pin all dependencies a versiones específicas. |
| **Severidad** | P2 |
| **Owner** | Joel Diaz (Fundador) |
| **Target** | Próxima sesión de mantenimiento del repositorio |
| **Evidencia necesaria** | `requirements.txt` con versiones exactas (e.g., `pandas==2.1.4`) |
| **Blocking status** | **NO** — pipeline funciona actualmente |
| **Completión criteria** | `requirements.txt` con todas las dependencias pinned + pip freeze verificado |

---

## REM-005: Knowledge Object promotion review

| Campo | Valor |
|-------|-------|
| **ID** | REM-005 |
| **Fuente** | Knowledge Object candidates — 5 identificados, 0 promovidos |
| **Descripción** | Revisar los 5 KO candidates y decidir si alguno está listo para formalización como KO per Package 002 contract. Prioridad: KO-5 (methodology — pipeline) por tener mayor confianza y reutilización. |
| **Severidad** | P3 |
| **Owner** | Joel Diaz (Fundador) |
| **Target** | Cuando el fundador tenga bandwidth para formalización (no urgente) |
| **Evidencia necesaria** | KO formalizado con campos completos per Package 002 contract O decisión explícita de postergar |
| **Blocking status** | **NO** — KOs pueden permanecer como candidates indefinidamente |
| **Completión criteria** | ≥1 KO formalizado O revisión documentada con decisión de postergar |

---

## REM-006: Asset candidate review

| Campo | Valor |
|-------|-------|
| **ID** | REM-006 |
| **Fuente** | Asset candidates — 5 identificados, ninguno cumple 4 condiciones |
| **Descripción** | Revisar los 5 Asset candidates y evaluar si alguno puede avanzar hacia las 4 condiciones de promoción (desacoplamiento, documentación, 5 campos mínimos, hipótesis de monetización). Prioridad: ASSET-3 (Template journal) por mínimo esfuerzo de extracción. |
| **Severidad** | P3 |
| **Owner** | Joel Diaz (Fundador) |
| **Target** | Cuando el fundador decida invertir en extracción de assets |
| **Evidencia necesaria** | ≥1 asset que cumpla las 4 condiciones O decisión de postergar con razón |
| **Blocking status** | **NO** — assets pueden permanecer como candidates |
| **Completión criteria** | ≥1 asset promovido O revisión documentada con decisión de postergar |

---

## REM-007: Monetization hypothesis validation experiment

| Campo | Valor |
|-------|-------|
| **ID** | REM-007 |
| **Fuente** | Monetization hypothesis — 3 hipótesis documentadas, 0 validadas |
| **Descripción** | Diseñar y ejecutar al menos un experimento de validación de demanda para alguna de las 3 hipótesis de monetización. Per INV-03: no invertir >1 semana sin hipótesis validada. El Lab está en compliance actual pero avanzar requiere señal de demanda. |
| **Severidad** | P2 |
| **Owner** | Joel Diaz (Fundador) |
| **Target** | Antes de transicionar a `validando` |
| **Evidencia necesaria** | Pricing research, landing page, customer interview, o cualquier señal de willingness-to-pay |
| **Blocking status** | **NO** — no bloquea Lab Contract ni `explorando`. Bloquea `validando` |
| **Completión criteria** | ≥1 experimento de validación documentado con resultado (positivo o negativo) |

---

## Resumen de remediaciones

| ID | Descripción corta | Severidad | Bloqueante | Target |
|----|--------------------|-----------|------------|--------|
| REM-001 | Licencia dataset Binance | P2 | NO | Pre-publicación |
| REM-002 | Walk-forward execution/deferral | P2 | NO (bloquea `validando`) | PF > 1.0 |
| REM-003 | Monte Carlo execution/deferral | P2 | NO (bloquea `validando`) | PF > 1.0 |
| REM-004 | Dependency pinning | P2 | NO | Próximo mantenimiento |
| REM-005 | KO promotion review | P3 | NO | Cuando haya bandwidth |
| REM-006 | Asset candidate review | P3 | NO | Cuando haya bandwidth |
| REM-007 | Monetization validation | P2 | NO (bloquea `validando`) | Pre-validando |

### Por severidad

| Severidad | Cantidad |
|-----------|----------|
| P2 | 5 |
| P3 | 2 |

### Blocking para transiciones futuras

| Transición | Remediaciones requeridas |
|-----------|--------------------------|
| `explorando` → `validando` | REM-002, REM-003, REM-007 (mínimo) |
| Publicación de datos | REM-001 |
| Asset promotion | REM-005, REM-006 |

---

## Cross-references

- [crypto-scalping-core-lab-contract-compliance.md](./crypto-scalping-core-lab-contract-compliance.md) — Evaluación que identifica gaps
- [crypto-scalping-core-lab-contract.md](./crypto-scalping-core-lab-contract.md) — Contrato con remediaciones pendientes
- [crypto-scalping-core-dependency-map.md](./crypto-scalping-core-dependency-map.md) — Fuente de REM-004
- [crypto-scalping-core-research-workflow-map.md](./crypto-scalping-core-research-workflow-map.md) — Fuente de REM-002, REM-003
- [crypto-scalping-core-knowledge-object-candidates.md](./crypto-scalping-core-knowledge-object-candidates.md) — Fuente de REM-005
- [crypto-scalping-core-asset-candidates.md](./crypto-scalping-core-asset-candidates.md) — Fuente de REM-006
- [crypto-scalping-core-monetization-hypothesis.md](./crypto-scalping-core-monetization-hypothesis.md) — Fuente de REM-007

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 3        | 15%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 17       | 85%        |
| [Visión]      | 0        | 0%         |

> **Nota:** Alto porcentaje de decisiones porque un plan de remediación define acciones, targets y criterios — todas son elecciones de diseño. Los hechos corresponden al contexto de origen.

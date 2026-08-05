# Lab Integration Patterns v1

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Patrones de integración de Labs |
| **Versión** | 1.0 |
| **Package** | 001A — First Lab Integration |
| **Batch** | 4 — Reference Lab Freeze & Package Closure |
| **Fecha** | 2025-07-30 |
| **Reference Lab** | LABOS-REF-LAB-0001 (Crypto Scalping Core) |

---

## Propósito

Documentar los 10 patrones de integración de Labs extraídos del proceso de Package 001A. [Decisión] Estos patrones son domain-neutral y reutilizables para cualquier Lab futuro integrado a LabOS.

---

## PAT-LAB-001 — Evidence Before Contract

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-001 |
| **Nombre** | Evidence Before Contract |
| **Problema** | Se necesita crear un Lab Contract formal, pero sin evidencia del estado real del Lab, el contrato se convierte en ficción aspiracional. |
| **Contexto** | Un Lab existente será integrado al ecosistema LabOS. Se desconoce su estado real, artefactos producidos y madurez operativa. |
| **Fuerzas** | Urgencia por formalizar vs. riesgo de documentar fantasía. Necesidad de rigor vs. overhead de inspección. |
| **Solución** | Antes de redactar cualquier Lab Contract, realizar una inspección completa del repositorio/artefactos del Lab. Documentar inventarios, workflows, dependencies y evidencia verificable. Solo entonces instanciar el contrato con datos reales. [Decisión] |
| **Evidencia del Reference Lab** | Package 001A ejecutó Batch 1 (readiness) y Batch 2 (inspección de repositorio) ANTES de Batch 3 (Lab Contract). El contrato se llenó con datos verificados: 14 experimentos, 567 runs, 4 estrategias — no con aspiraciones. [Hecho] |
| **Aplicabilidad** | Cualquier Lab con historia previa a LabOS. Labs greenfield pueden tener menos evidencia pero el principio aplica: documentar lo que EXISTE, no lo que se DESEA. [Decisión] |
| **Limitaciones** | Labs sin repositorio o artefactos digitales requieren adaptación del proceso de inspección. [Hipótesis] |
| **Anti-patrones** | Crear Lab Contract con campos aspiracionales. Documentar features planeadas como existentes. Inflar métricas para justificar un estado mayor. |

---

## PAT-LAB-002 — Founder Decisions Before Inference

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-002 |
| **Nombre** | Founder Decisions Before Inference |
| **Problema** | El proceso de integración requiere decisiones de governance (estado, scope, boundaries) que NO pueden inferirse de la evidencia técnica sola. |
| **Contexto** | Un arquitecto o agente IA tiene evidencia técnica suficiente para recomendar, pero la decisión final sobre estado, prioridad y scope es del fundador. |
| **Fuerzas** | Eficiencia de auto-decisión vs. legitimidad de decisiones de governance. Velocidad vs. ownership. |
| **Solución** | Identificar decisiones que requieren input del fundador (P0 blockers, state transitions, scope changes). Presentar opciones con evidencia y recomendación, pero NO decidir por el fundador. Documentar la decisión explícitamente con fecha y rationale. [Decisión] |
| **Evidencia del Reference Lab** | Batch 1 identificó 4 decisiones P0 bloqueantes que NO podían inferirse (caso de estudio, Lab State candidates, autonomía, scope). Batch 3 requirió aprobación explícita del Lab State. Batch 4 requirió aprobación del contrato. En todos los casos, se presentaron opciones — no se asumió respuesta. [Hecho] |
| **Aplicabilidad** | Toda integración donde exista un owner/fundador con autoridad de decisión. En equipos, aplica al decision-maker designado. [Decisión] |
| **Limitaciones** | Si el fundador no está disponible, el proceso se bloquea. Mitigación: pre-definir delegation rules. [Hipótesis] |
| **Anti-patrones** | Inferir decisiones de governance sin consultar. Asumir aprobación por silencio. Presentar una sola opción como "la correcta". |

---

## PAT-LAB-003 — Autonomy by Default

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-003 |
| **Nombre** | Autonomy by Default |
| **Problema** | Al integrar un Lab a un ecosistema (LabOS), existe el riesgo de crear dependencias innecesarias que limiten la operación independiente del Lab. |
| **Contexto** | Un Lab tiene su propio repositorio, pipeline y flujo de trabajo. La integración debe agregar valor sin crear acoplamiento que dificulte la operación autónoma. |
| **Fuerzas** | Beneficios de integración (governance, KOs, assets) vs. costo de acoplamiento. Estandarización vs. libertad operativa. |
| **Solución** | Diseñar la integración con cero dependencias operativas por defecto. El Lab debe poder funcionar idénticamente si LabOS desapareciera. La integración agrega capas de governance y knowledge management, NO modifica el código ni la operación del Lab. [Decisión] |
| **Evidencia del Reference Lab** | Sección 14 del Lab Contract documenta explícitamente: "El Lab no depende de LabOS para operar." Cero imports de LabOS, cero APIs compartidas, cero shared state. Package 001A no modificó ningún archivo del repositorio CSC. [Hecho] |
| **Aplicabilidad** | Todo Lab integrado a LabOS. Especialmente crítico en Labs con historia pre-LabOS. [Decisión] |
| **Limitaciones** | Labs que DESEAN integración profunda (shared infra, shared data) requieren patrón diferente: Controlled Coupling (no definido aún). [Hipótesis] |
| **Anti-patrones** | Requerir que Labs importen módulos de LabOS. Crear shared databases. Modificar código del Lab como parte de la integración. Imponer herramientas no solicitadas. |

---

## PAT-LAB-004 — Source of Truth Explicitness

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-004 |
| **Nombre** | Source of Truth Explicitness |
| **Problema** | Cuando un Lab se integra, surge ambigüedad sobre dónde vive la información autoritativa de cada concepto (¿en el Lab? ¿en LabOS? ¿en ambos?). |
| **Contexto** | Un Lab tiene sus propios documentos. LabOS tiene su propia documentación. La integración crea documentos nuevos (contrato, evidence map). Sin definición explícita, se generan conflictos de versión. |
| **Fuerzas** | Conveniencia de duplicar vs. coherencia de fuente única. Proximidad de la info al Lab vs. centralización en LabOS. |
| **Solución** | Para cada concepto relevante, declarar explícitamente cuál es la fuente de verdad: el documento del Lab, el documento de LabOS, o un documento nuevo del contrato. Documentar esta asignación en un Source of Truth Map. [Decisión] |
| **Evidencia del Reference Lab** | Package 001A creó `crypto-scalping-core-source-of-truth-map.md` que declara para cada concepto dónde vive la verdad: resultados → Lab repo, governance → LabOS, contrato → Package 001A. Sin ambigüedad. [Hecho] |
| **Aplicabilidad** | Todo Lab integrado. La complejidad del map escala con el número de conceptos compartidos. [Decisión] |
| **Limitaciones** | Si un concepto evoluciona en ambos lados simultáneamente, requiere protocolo de sincronización (no definido aún). [Hipótesis] |
| **Anti-patrones** | Duplicar información sin declarar cuál es autoritativa. Asumir que "el más reciente gana". Mantener dos versiones sin reconciliación. |

---

## PAT-LAB-005 — Knowledge Is Not Raw Output

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-005 |
| **Nombre** | Knowledge Is Not Raw Output |
| **Problema** | Un Lab produce muchos artefactos (CSVs, logs, configs, outputs). No todos son "conocimiento" en el sentido de LabOS. Si se tratan como equivalentes, el sistema se infla con ruido. |
| **Contexto** | Un Lab con investigación activa genera outputs en cada ejecución. Solo algunos de esos outputs contienen insight transferible, reproducible y reutilizable. |
| **Fuerzas** | Completitud del registro vs. señal/ruido. Preservar todo vs. curar lo valioso. |
| **Solución** | Distinguir explícitamente entre raw outputs (datos de ejecución), artefactos de investigación (documentos con contexto), Knowledge Objects (unidades de conocimiento formalizadas con los 5 campos mínimos) y Assets (unidades reutilizables con hipótesis de monetización). Cada nivel requiere más formalización. [Decisión] |
| **Evidencia del Reference Lab** | Package 001A identificó 567 optimizer runs (raw output), 27+ artefactos de investigación, 5 Knowledge Object candidates y 5 Asset candidates. La distinción permitió foco: solo los KO/Asset candidates requieren atención de formalización. [Hecho] |
| **Aplicabilidad** | Todo Lab con producción de datos o documentos. Especialmente Labs de investigación o experimentación. [Decisión] |
| **Limitaciones** | La frontera entre "artefacto" y "Knowledge Object" puede ser subjetiva. Criterios formales (5 campos) mitigan pero no eliminan la subjetividad. [Hipótesis] |
| **Anti-patrones** | Tratar todo CSV como un asset. Contar outputs como "conocimiento producido". Inflar métricas con raw data. |

---

## PAT-LAB-006 — Assetization Requires Reuse Evidence

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-006 |
| **Nombre** | Assetization Requires Reuse Evidence |
| **Problema** | Existe presión por declarar elementos del Lab como "assets" para demostrar progreso en el Knowledge-to-Value Pipeline. Sin evidencia de reutilización, esto es inflación. |
| **Contexto** | Un Lab produce artefactos valiosos dentro de su contexto. Para ser un Asset de LabOS, debe cumplir criterios de desacoplamiento, documentación y potencial de reutilización. |
| **Fuerzas** | Deseo de progreso visible vs. rigor de clasificación. Optimismo del creador vs. realidad de reutilización. |
| **Solución** | Un artefacto solo se promueve a Asset cuando cumple las 4 condiciones: (1) desacoplado del contexto original, (2) documentado con los campos mínimos, (3) con hipótesis de reutilización o monetización, (4) con evidencia de que alguien más (o el mismo autor en otro contexto) podría usarlo. [Decisión] |
| **Evidencia del Reference Lab** | 5 Asset candidates identificados en CSC, NINGUNO promovido porque ninguno cumple las 4 condiciones. Esto es honestidad operativa, no fracaso. La remediación REM-006 preserva la revisión para cuando haya evidencia. [Hecho] |
| **Aplicabilidad** | Todo Lab en cualquier estado. La presión de assetization aumenta con el tiempo. [Decisión] |
| **Limitaciones** | Labs con productos ya en mercado pueden tener evidencia de reutilización inmediata — el proceso puede acelerarse. [Hipótesis] |
| **Anti-patrones** | Declarar assets sin desacoplar. Contar "candidates" como "assets producidos". Inventar hipótesis de monetización sin señal de demanda. |

---

## PAT-LAB-007 — Conditional Approval

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-007 |
| **Nombre** | Conditional Approval |
| **Problema** | Un Lab Contract puede ser 90% compliant pero tener gaps non-blocking. Esperar perfección bloquea el progreso; ignorar gaps genera deuda. |
| **Contexto** | El proceso de compliance identifica ítems P2/P3 que no son urgentes pero sí relevantes. El fundador debe decidir si aprueba con o sin condiciones. |
| **Fuerzas** | Perfeccionismo vs. pragmatismo. Rigor de compliance vs. velocidad de cierre. Deuda documentada vs. deuda ignorada. |
| **Solución** | Permitir aprobación con remediaciones documentadas. Clasificar cada gap como blocking o non-blocking. Los non-blocking se preservan en un plan de remediación con owners, targets y triggers — pero NO bloquean la aprobación del contrato. [Decisión] |
| **Evidencia del Reference Lab** | Lab Contract aprobado con 7 remediaciones P2/P3 non-blocking. Cada una tiene trigger natural (PF > 1.0, transición a `validando`, etc.). El fundador aprobó incondicionalmente confiando en el plan documentado. [Hecho] |
| **Aplicabilidad** | Cualquier proceso de aprobación en LabOS. Extensible a reviews de packages, arquitectura, productos. [Decisión] |
| **Limitaciones** | Si las remediaciones se acumulan indefinidamente sin ejecutarse, el sistema pierde credibilidad. Review triggers mitigan pero no eliminan el riesgo. [Hipótesis] |
| **Anti-patrones** | Bloquear todo hasta perfección. Aprobar sin documentar los gaps. Crear remediaciones sin owner ni trigger ("algún día"). |

---

## PAT-LAB-008 — Negative Results Are Valid Knowledge

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-008 |
| **Nombre** | Negative Results Are Valid Knowledge |
| **Problema** | Existe sesgo hacia documentar solo resultados positivos ("funciona", "es rentable"). Los resultados negativos tienden a ocultarse o minimizarse, perdiendo conocimiento valioso. |
| **Contexto** | Un Lab de investigación produce tanto resultados positivos como negativos. En dominios como trading cuantitativo, la mayoría de hipótesis se invalidan. |
| **Fuerzas** | Presión por demostrar progreso vs. honestidad intelectual. Sesgo de supervivencia vs. valor del fracaso documentado. |
| **Solución** | Documentar explícitamente los resultados negativos con la misma formalidad que los positivos. Un Lab en `explorando` con PF < 1.0 es un resultado válido y honesto — no un fracaso de integración. La ausencia de rentabilidad es INFORMACIÓN, no ausencia de valor. [Decisión] |
| **Evidencia del Reference Lab** | Lab Contract de CSC declara honestamente: "Ninguna estrategia ha logrado PF > 1.0." [Hecho] Este no es un fracaso — es el estado real de exploración. El contrato se aprobó PORQUE es honesto, no A PESAR de serlo. [Hecho] |
| **Aplicabilidad** | Todo Lab de investigación o experimentación. Labs operativos con revenue pueden tener menos resultados negativos relevantes. [Decisión] |
| **Limitaciones** | Si un Lab solo produce resultados negativos durante un período excesivo sin pivotear, puede indicar problema de dirección (no de documentación). [Hipótesis] |
| **Anti-patrones** | Ocultar PF < 1.0. Reportar solo las mejores métricas. Usar language aspiracional para disfrazar resultados negativos ("casi rentable"). |

---

## PAT-LAB-009 — Proportional Governance

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-009 |
| **Nombre** | Proportional Governance |
| **Problema** | La governance de un Lab puede ser excesiva (burocracia que no agrega valor) o insuficiente (riesgos no gestionados). Ambos extremos destruyen valor. |
| **Contexto** | LabOS opera como operador solo con un portafolio de Labs en diferentes estados. La governance debe escalar con la complejidad real, no con aspiraciones futuras. |
| **Fuerzas** | Rigor vs. overhead. Seguridad vs. agilidad. Governance enterprise vs. realidad de solo operator. |
| **Solución** | Escalar governance proporcionalmente a: (1) número de operadores, (2) estado del Lab, (3) revenue generado, (4) riesgo real. Un Lab en `explorando` con 1 operador y $0 revenue requiere governance MÍNIMA: 15min/mes review, decisiones en 1 párrafo, sin escalación formal. [Decisión] |
| **Evidencia del Reference Lab** | Lab Contract define governance nivel SOLO: review mensual 15min, sin comités, sin escalación multi-nivel, sin approval workflows complejos. Aprobación por fundador en 1 decisión directa. INV-05 (proporcionalidad) satisfecha. [Hecho] |
| **Aplicabilidad** | Todo Lab en LabOS. La governance DEBE escalar cuando cambien las condiciones (más operadores, más revenue, más riesgo). [Decisión] |
| **Limitaciones** | El punto exacto de escalamiento no está definido — se descubrirá empíricamente. [Hipótesis] |
| **Anti-patrones** | Crear workflows de aprobación multi-nivel para 1 persona. Requerir documentos de 50 páginas para decisiones simples. Copiar governance enterprise sin adaptación. |

---

## PAT-LAB-010 — No State Inflation

| Campo | Contenido |
|-------|-----------|
| **ID** | PAT-LAB-010 |
| **Nombre** | No State Inflation |
| **Problema** | Existe presión por asignar estados avanzados a Labs para demostrar progreso ("estamos validando") cuando la evidencia no soporta ese nivel. |
| **Contexto** | LabOS define estados con criterios de transición (`idea` → `explorando` → `validando` → `operando`). Cada transición requiere evidencia específica. |
| **Fuerzas** | Deseo de mostrar progreso vs. honestidad epistémica. Optimismo vs. evidencia. Presión interna vs. realidad del mercado. |
| **Solución** | Asignar Lab State SOLO basado en evidencia que satisface los criterios de transición. Presentar opciones al fundador con justificación clara de por qué SÍ y por qué NO califica para cada estado. No inflar para motivación ni para apariencias. [Decisión] |
| **Evidencia del Reference Lab** | CSC tiene 14 experimentos, 567 runs, pipeline operativo — pero PF < 1.0. El Principal Architect recomendó `explorando` (no `validando`) y documentó explícitamente la razón del NO: "No hay hipótesis de monetización validada." El fundador aprobó. [Hecho] |
| **Aplicabilidad** | Todo Lab en cualquier transición de estado. Especialmente crítico en transiciones `explorando` → `validando` (requiere señal de mercado). [Decisión] |
| **Limitaciones** | Los criterios de transición actuales son v1 — pueden refinarse con experiencia. [Hipótesis] |
| **Anti-patrones** | Declarar `validando` sin PF > 1.0 o señal de demanda. Usar estado avanzado para justificar más inversión. Inflar para reportes o portafolio público. |

---

## Resumen de patrones

| ID | Nombre | Principio clave |
|----|--------|----------------|
| PAT-LAB-001 | Evidence Before Contract | No documentar ficción |
| PAT-LAB-002 | Founder Decisions Before Inference | No decidir por el owner |
| PAT-LAB-003 | Autonomy by Default | No crear dependencias innecesarias |
| PAT-LAB-004 | Source of Truth Explicitness | No duplicar sin declarar autoridad |
| PAT-LAB-005 | Knowledge Is Not Raw Output | No inflar con raw data |
| PAT-LAB-006 | Assetization Requires Reuse Evidence | No declarar assets prematuramente |
| PAT-LAB-007 | Conditional Approval | No bloquear por perfeccionismo |
| PAT-LAB-008 | Negative Results Are Valid Knowledge | No ocultar fracasos |
| PAT-LAB-009 | Proportional Governance | No over-engineer governance |
| PAT-LAB-010 | No State Inflation | No inflar estados sin evidencia |

---

## Cross-references

- [crypto-scalping-core-reference-lab-record.md](./crypto-scalping-core-reference-lab-record.md) — Reference Lab de origen
- [crypto-scalping-core-lab-contract.md](./crypto-scalping-core-lab-contract.md) — Contrato que evidencia los patrones
- [lab-integration-checklist-v1.md](./lab-integration-checklist-v1.md) — Checklist que operacionaliza los patrones
- [../../architecture/architecture-baseline-v1.md](../../architecture/architecture-baseline-v1.md) — Invariantes que los patrones satisfacen

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 12       | 24%        |
| [Hipótesis]   | 10       | 20%        |
| [Decisión]    | 25       | 50%        |
| [Visión]      | 0        | 0%         |

> **Nota:** Balance entre decisiones (diseño de los patrones), hechos (evidencia del Reference Lab) e hipótesis (limitaciones y aplicabilidad no verificada). Sin visiones porque los patrones son retrospectivos, no aspiracionales.

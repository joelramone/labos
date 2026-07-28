# 019 — Research-to-Product Hypothesis

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R16.1, R16.2, R16.3, R16.4, R17.1, R17.2, R17.3, R17.4, R31.1, R31.2, R31.3, R31.4, R31.5

## Propósito

Este documento define el **proceso de derivación de hipótesis de producto y revenue** a partir de investigaciones completadas dentro de LabOS. [Hecho]

El proceso establece:

- Un flujo de evaluación de señales comerciales en 4 pasos
- Un modelo de Product_Hypothesis con 7 campos obligatorios
- Un modelo de Revenue_Hypothesis con 7 campos obligatorios
- 5 criterios explícitos para NO formular hypothesis
- Reglas de prudent monetization alineadas con Package 000
- Decisión final con opciones claras (advance, archive, discard)

La derivación comercial es un proceso de **evaluación prudente**, no de forzamiento.
Una investigación puede concluir sin producto comercial si la evidencia no lo soporta. No toda investigación debe monetizarse. [Decisión]

Este documento cubre la **Etapa 14: Product Hypothesis** del Research Lifecycle, inmediatamente posterior a la extracción de activos documentada en [018-research-to-asset.md](./018-research-to-asset.md). [Hecho]

---

## Tabla de contenidos

1. [Principio fundamental](#principio-fundamental)
2. [Proceso de derivación](#proceso-de-derivación)
3. [Product_Hypothesis: modelo completo](#product_hypothesis-modelo-completo)
4. [Revenue_Hypothesis: modelo completo](#revenue_hypothesis-modelo-completo)
5. [Criterios para NO formular hypothesis](#criterios-para-no-formular-hypothesis)
6. [Reglas de prudent monetization](#reglas-de-prudent-monetization)
7. [Decisión final](#decisión-final)
8. [Diagrama de flujo](#diagrama-de-flujo)
9. [Alineación con Package 000](#alineación-con-package-000)
10. [Referencias](#referencias)

---

## 1. Principio fundamental

> La derivación de hipótesis de producto es un proceso de evaluación, no de forzamiento. Una investigación puede concluir sin producto comercial si la evidencia no lo soporta. [Decisión]

Este principio se alinea con:

- **Package 000, Regla 4:** "La validación de demanda precede a la inversión en desarrollo completo. Preferir: vender → construir → escalar." [Hecho]
- **Package 000, Prohibición:** "No asumir product-market fit sin evidencia de pago." [Hecho]
- **Package 000, Modelo de negocio, Regla 2:** "No invertir en etapa 3 sin validación en etapas 1-2." [Hecho]

La ausencia de hipótesis comercial no es un fracaso. Una investigación que produce un Knowledge Asset sin potencial comercial es un resultado válido y completo. [Decisión]

---

## 2. Proceso de derivación

El proceso consta de 4 pasos secuenciales. No es obligatorio avanzar más allá del paso 1 si las señales no existen. [Decisión]

### 2.1 Paso 1: Evaluación de señales comerciales

| Campo | Valor |
|-------|-------|
| **Propósito** | Determinar si la investigación produjo señales que justifiquen explorar una hipótesis comercial |
| **Input** | Conclusions aprobadas, assets extraídos, evidence register |
| **Actividades** | Revisar conclusions buscando las 4 señales definidas abajo |
| **Output** | Decisión: existen señales suficientes (→ continuar) o no existen (→ archivar sin hypothesis) |

**Señales a evaluar:**

| # | Señal | Qué buscar | Ejemplo |
|---|-------|-------------|---------|
| 1 | Problema confirmado | La investigación validó un problema que afecta a un segmento identificable | "Fundadores técnicos pierden 40+ horas eligiendo frameworks sin guía comparativa" |
| 2 | Activo con demanda potencial | El activo producido resuelve algo que otros podrían necesitar | "La comparativa de orquestación de agentes tiene valor para desarrolladores evaluando opciones" |
| 3 | Conocimiento monetizable | El conocimiento generado es escaso y otros pagarían por obtenerlo | "No existe guía estructurada en español sobre configuración de agentes con tool-use" |
| 4 | Gap de mercado evidenciado | Durante la investigación se identificó un vacío en la oferta actual | "No hay herramienta que permita a un solo operador gestionar 5+ agentes con trazabilidad" |

**Regla:** Se requiere al menos 1 señal para continuar al paso 2. Si no existe ninguna señal, aplicar los criterios de la sección 5 y archivar. [Decisión]

### 2.2 Paso 2: Formulación de Product_Hypothesis

| Campo | Valor |
|-------|-------|
| **Propósito** | Estructurar la oportunidad comercial como hipótesis formal con campos verificables |
| **Input** | Señales identificadas en paso 1 + conclusions + evidence |
| **Actividades** | Completar los 7 campos obligatorios del modelo Product_Hypothesis (ver sección 3) |
| **Output** | Product_Hypothesis completa o marcada como "incomplete" con campos faltantes |
| **Criterio de avance** | Los 7 campos están completos Y existe al menos 1 demand signal externo |

### 2.3 Paso 3: Formulación de Revenue_Hypothesis

| Campo | Valor |
|-------|-------|
| **Propósito** | Definir el mecanismo concreto de generación de ingresos |
| **Input** | Product_Hypothesis viable (paso 2 completado) |
| **Actividades** | Completar los 7 campos obligatorios del modelo Revenue_Hypothesis (ver sección 4) |
| **Output** | Revenue_Hypothesis completa o declaración de evidencia insuficiente |
| **Criterio de avance** | Revenue_Hypothesis completa con experimento diseñado, O documentación de por qué no se puede formular |

**Nota:** La Revenue_Hypothesis solo se formula si la Product_Hypothesis es viable (campos completos y confidence ≥ "emerging"). No es obligatorio formular Revenue_Hypothesis si la Product_Hypothesis es "speculative". [Decisión]

### 2.4 Paso 4: Decisión

| Campo | Valor |
|-------|-------|
| **Propósito** | Decidir el destino de la oportunidad comercial identificada |
| **Input** | Product_Hypothesis + Revenue_Hypothesis (si aplica) |
| **Actividades** | Evaluar si la hypothesis cumple criterios para avanzar a validación comercial |
| **Output** | Una de 3 decisiones: advance, archive, discard |

Las opciones se detallan en la sección 7. [Hecho]

---

## 3. Product_Hypothesis: modelo completo

Todo Product_Hypothesis derivado de una investigación se documenta con los siguientes **7 campos obligatorios**: [Decisión]

### 3.1 Campos obligatorios

```
Product_Hypothesis
├── 1. problem          : string
│   Qué problema fue identificado por la investigación y qué evidencia lo soporta.
│   Requisito: mínimo 1 observación documentada, data point, o declaración de usuario.
│   Ejemplo: "Fundadores técnicos invierten 40+ horas seleccionando frameworks de
│   agentes IA sin guía comparativa estructurada. Evidencia: 3 posts en comunidades
│   reportando frustración + observación directa del fundador."
│
├── 2. segment          : string
│   Quién podría beneficiarse. Descrito como rol o perfil específico.
│   Ejemplo: "Desarrolladores senior y CTOs de startups early-stage (pre-seed a
│   Series A) construyendo productos AI-native con equipos de 1-5 personas."
│
├── 3. asset            : string
│   Qué activo de la investigación puede entregarse como solución.
│   Debe referenciar un activo ya extraído (ver 018-research-to-asset.md).
│   Ejemplo: "Comparativa de 5 frameworks de orquestación de agentes (AST-K-014)."
│
├── 4. format           : enum (service | product | content | tool)
│   Qué formato aplica para la entrega.
│   - service: consultoría, implementación personalizada, sesión
│   - product: plantilla, playbook, curso empaquetado
│   - content: artículo, tutorial, serie de contenido
│   - tool: script, CLI, aplicación, automatización
│   Ejemplo: "product (playbook con decisión guiada + template de evaluación)"
│
├── 5. evidence         : string
│   Qué evidencia comercial existe. Mínimo 1 demand signal:
│   - Search volume (documentado con fuente y cifra)
│   - Direct request (mensaje, email, conversación documentada)
│   - Competitor existence (competidores activos con clientes pagando)
│   - Stated willingness to pay (declaración de un potencial comprador)
│   Ejemplo: "3 hilos en r/LangChain preguntando por comparativas + 2 productos
│   competidores (LangChain Hub, AgentOps) con usuarios pagando."
│
├── 6. validation       : string
│   Qué asunción específica debe validarse antes de vender y método propuesto.
│   Ejemplo: "Asunción: fundadores pagarían $29-49 por una guía comparativa
│   actualizada. Método: landing page con precio + botón de compra midiendo
│   conversión durante 14 días."
│
└── 7. experiment       : string
    Cuál sería el experimento comercial mínimo.
    Debe incluir: acción, métrica y threshold de éxito dentro de ≤30 días.
    Ejemplo: "Publicar landing page con descripción del playbook a $39.
    Métrica: visitantes únicos que hacen clic en 'comprar'. Threshold: ≥5%
    CTR en 14 días con ≥100 visitantes."
```

### 3.2 Campos adicionales

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `source_investigation` | string | Referencia al investigation_id fuente |
| `confidence_level` | enum | speculative / emerging / supported |
| `formulation_date` | date | Fecha de formulación (ISO 8601) |
| `status` | enum | incomplete / complete / advancing / archived / discarded |

### 3.3 Niveles de confianza

| Nivel | Definición | Criterio |
|-------|-----------|----------|
| **Speculative** | No hay evidencia directa; inferido de datos adyacentes | 0 demand signals directos, oportunidad inferida del análisis |
| **Emerging** | 1-2 señales débiles (menciones informales, indicadores indirectos) | 1-2 señales como posts en foros, preguntas en comunidades, interés verbal |
| **Supported** | 3+ señales, o 1 señal fuerte (solicitud de pago, demanda documentada) | ≥3 señales independientes, O ≥1 cliente pidiendo explícitamente el producto/servicio |

### 3.4 Reglas de avance

Una Product_Hypothesis puede avanzar a validación comercial **solo cuando** se cumplen las 3 condiciones: [Decisión]

1. Los 7 campos obligatorios están completos.
2. El `confidence_level` es "emerging" o "supported".
3. Al menos 1 demand signal es **externo al Fundador** (no es una necesidad auto-evaluada).

> Alineación: Package 000 Regla 4 — "Validar demanda antes de desarrollar producto." [Hecho]

### 3.5 Hypothesis incompleta

Si uno o más de los 7 campos no pueden completarse por falta de evidencia: [Decisión]

1. Marcar `status: incomplete`.
2. Identificar los campos faltantes explícitamente.
3. Registrar una acción de follow-up por cada campo faltante.
4. La hypothesis **no puede avanzar** hasta completar todos los campos.

---

## 4. Revenue_Hypothesis: modelo completo

La Revenue_Hypothesis define el mecanismo concreto por el cual fluiría dinero. Se formula **solo si** la Product_Hypothesis es viable (completa y con confidence ≥ "emerging"). [Decisión]

### 4.1 Campos obligatorios

```
Revenue_Hypothesis
├── 1. revenue_mechanism    : string
│   Cómo fluye el dinero (venta directa, suscripción, licencia, comisión, etc.).
│   Ejemplo: "Venta directa one-time de playbook digital vía plataforma de pagos."
│
├── 2. price                : string
│   Hipótesis de precio expresada como rango numérico con moneda y fuente de justificación.
│   Ejemplo: "$29-49 USD. Justificación: competidores similares (AgentOps reports)
│   cobran $39-99. Se posiciona en el rango bajo para facilitar primera compra."
│
├── 3. segment              : string
│   Segmento target descrito por tamaño estimado, perfil y necesidad observable.
│   Ejemplo: "~50,000 desarrolladores en r/LangChain + r/LocalLLaMA que están
│   evaluando frameworks. Perfil: developer senior, startup early-stage. Necesidad
│   observable: preguntas frecuentes sobre comparativas en foros."
│
├── 4. channel              : string
│   Por dónde se distribuiría y llegaría al comprador.
│   Ejemplo: "Distribución orgánica: post en r/LangChain + thread en Twitter/X
│   + newsletter de AI Engineering. Plataforma de venta: Gumroad o Lemon Squeezy."
│
├── 5. volume               : string
│   Estimación de volumen expresada como rango numérico con supuestos subyacentes.
│   Ejemplo: "5-20 ventas/mes basado en: ~1,000 visitas orgánicas esperadas
│   (benchmark de posts similares) × 0.5-2% conversión (benchmark de productos
│   digitales de nicho). Supuesto: contenido resuena con la audiencia target."
│
├── 6. demand_evidence      : string
│   Al menos 1 data point de observación, entrevista o referencia de mercado que
│   soporte la existencia de demanda real.
│   Ejemplo: "3 posts en r/LangChain con 200+ upvotes pidiendo comparativas
│   actualizadas (fecha: enero 2024). 2 competidores (AgentOps, E2B) vendiendo
│   contenido similar con reviews positivas."
│
└── 7. experiment           : string
    Experimento mínimo para validar willingness-to-pay con métrica pass/fail
    y deadline ≤90 días.
    Ejemplo: "Publicar landing page con precio real ($39). Correr ads con $50
    budget durante 14 días. Pass: ≥3 compras. Fail: <3 compras en 14 días.
    Deadline: 30 días desde publicación."
```

### 4.2 Campos adicionales

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `source_product_hypothesis` | string | Referencia a la Product_Hypothesis que origina esta Revenue_Hypothesis |
| `validation_timeline` | string | Tiempo estimado para validar (≤90 días) |
| `formulation_date` | date | Fecha de formulación (ISO 8601) |
| `status` | enum | incomplete / complete / validated / failed / archived |

### 4.3 Regla de transacción real

Una Revenue_Hypothesis **no se considera validada** hasta que ocurra una transacción real. [Decisión]

**Definición de transacción real:** pago documentado con:
- Fecha de la transacción
- Monto en USD
- Segmento del cliente
- Fuente de ingreso (producto/servicio que generó el pago)
- Canal de adquisición (cómo llegó el cliente)

> Alineación: Package 000 Revenue Thesis — "No reportar ingresos proyectados como ingresos reales." [Hecho]

### 4.4 Investigación sin Revenue_Hypothesis

Es válido concluir sin Revenue_Hypothesis cuando: [Decisión]

- La investigación produjo menos de 2 data points independientes que soporten demanda.
- El dominio no permite comercialización por restricciones éticas, regulatorias o de IP.

En este caso, documentar:
1. La research question investigada.
2. La evidencia recopilada.
3. La razón por la cual la evidencia es insuficiente para soportar un revenue mechanism.
4. Las condiciones de follow-up que justificarían revisitar la oportunidad.

### 4.5 Revenue_Hypothesis incompleta

Si uno o más campos no pueden completarse por falta de evidencia: [Decisión]

1. Clasificar como hypothesis incompleta.
2. Marcar los campos faltantes explícitamente.
3. Para cada campo faltante, registrar una acción para obtener la evidencia con plazo ≤30 días.
4. La hypothesis **no puede avanzar** a validación comercial hasta completar todos los campos.

---

## 5. Criterios para NO formular hypothesis

Las siguientes 5 condiciones, si alguna se cumple, **impiden** la formulación de Product_Hypothesis o Revenue_Hypothesis. En estos casos, la investigación se archiva como Knowledge Asset sin presión de monetización. [Decisión]

| # | Condición | Descripción | Ejemplo |
|---|-----------|-------------|---------|
| 1 | **No existe problema confirmado** | La investigación no validó un problema que afecte a un segmento externo. Las conclusiones son descriptivas o exploratorias sin pain point demostrado. | "La investigación documentó el estado del arte de LLM fine-tuning pero no identificó un problema concreto de un segmento." |
| 2 | **Segmento beneficiario no identificable** | No se puede describir quién se beneficiaría con suficiente especificidad como para alcanzarlos. El beneficiario es demasiado genérico o abstracto. | "El conocimiento beneficiaría a 'la industria tech' — demasiado amplio para formular un producto con canal definido." |
| 3 | **No hay demand signal** | No existen señales de demanda: ni directas (alguien pidió algo) ni inferidas (competidores existen, búsquedas documentadas, preguntas en foros). Cero evidencia de que alguien pagaría. | "El framework producido es útil internamente pero no hay evidencia de que otros lo busquen o necesiten." |
| 4 | **Activo de uso exclusivamente interno** | El activo producido solo tiene valor dentro de LabOS y no es transferible a un consumidor externo sin modificación significativa. | "El proceso de research-to-asset es metodología interna de LabOS; no es vendible como producto standalone." |
| 5 | **Restricciones que impiden comercialización** | El dominio tiene restricciones éticas, regulatorias, de IP o contractuales que impiden crear un producto comercial con los hallazgos. | "Los datos del análisis pertenecen a un cliente bajo NDA; no se puede comercializar el insight derivado." |

### 5.1 Regla de aplicación

- Basta con que **1 de las 5 condiciones** se cumpla para no formular hypothesis.
- La condición que aplica debe documentarse explícitamente en el conclusion document.
- La ausencia de hypothesis no es un fracaso — es un resultado válido del proceso de evaluación. [Decisión]

### 5.2 Documentación requerida al no formular

Cuando se aplica una condición de no-formulación, registrar:

| Campo | Contenido |
|-------|-----------|
| `commercial_evaluation_result` | "No hypothesis formulated" |
| `condition_applied` | Número y nombre de la condición (1-5) |
| `justification` | 1-3 oraciones explicando por qué aplica |
| `date` | Fecha de la evaluación (ISO 8601) |
| `follow_up_conditions` | Qué cambiaría para que se pueda revisitar (opcional) |

---

## 6. Reglas de prudent monetization

Las siguientes reglas gobiernan todo el proceso de derivación comercial dentro de LabOS. Son vinculantes y no negociables. [Decisión]

### 6.1 Regla principal: no avanzar sin demand signal externo

> **No se permite iniciar desarrollo de producto o inversión de tiempo >2 horas/semana en una oportunidad comercial sin al menos 1 demand signal verificable externo al Fundador.** [Decisión]

**Definición de demand signal externo:**

Un demand signal externo es una señal verificable de que alguien fuera de LabOS (no el Fundador evaluando su propia necesidad) ha expresado interés, necesidad o disposición de pago. [Hecho]

| Tipo de signal | Ejemplo válido | Ejemplo NO válido |
|---------------|----------------|-------------------|
| **Mensaje directo** | "¿Vendes una guía sobre X?" (DM documentado) | "Yo creo que otros necesitarían esto" (auto-evaluación) |
| **Reunión documentada** | Acta de reunión donde prospecto expresa necesidad | Conversación informal sin registro |
| **Request en comunidad** | Post en foro pidiendo solución al problema que el activo resuelve | Post del propio Fundador sugiriendo la solución |
| **Búsqueda documentada** | Keyword research mostrando volumen >100 búsquedas/mes | "Seguro la gente busca esto" sin datos |
| **Competidor con clientes** | Producto similar con reviews/clientes verificables | Proyecto similar abandonado sin evidencia de uso |

### 6.2 Regla de inversión máxima pre-validación

Antes de validar una hypothesis con transacción real: [Decisión]

- **Máximo 2 horas/semana** dedicadas a desarrollo del producto.
- **Máximo $50 USD** en inversión directa (plataformas, ads para validar).
- Si se requiere más inversión, la hypothesis debe tener `confidence_level: supported`.

### 6.3 Regla de no-forzamiento

No toda investigación debe producir un producto comercial. [Decisión] Las siguientes situaciones son resultado válidos y aceptables del proceso:

- Investigación → Knowledge Asset → Archive (sin monetización)
- Investigación → Technical Asset → Uso interno (sin venta)
- Investigación → Educational Asset → Publicación gratuita (sin revenue)
- Investigación → Product_Hypothesis incompleta → Follow-up pendiente

### 6.4 Regla del Quality Gate comercial

Una hypothesis puede avanzar a validación comercial **solo si** pasa el Quality Gate de utilización comercial: [Decisión]

| # | Criterio del gate | Verificación |
|---|-------------------|--------------|
| 1 | Los 3 campos mínimos de monetización están documentados (target segment, delivery format, revenue model) | Campos presentes y no vacíos |
| 2 | Validation experiment diseñado con métrica numérica de éxito | Métrica y threshold definidos |
| 3 | Deadline del experiment ≤30 días | Fecha límite registrada |
| 4 | Al menos 1 demand signal externo verificable | Signal documentado con fuente y fecha |

### 6.5 Regla de archivado por ausencia de señal

Si un activo registrado ha estado disponible durante 30 días sin generar ningún demand signal externo: [Decisión]

1. Se permite archivar como Knowledge Asset sin requerir plan de monetización.
2. Documentar: fecha de disponibilidad, período de observación, ausencia de señal comercial.
3. El activo permanece reutilizable internamente.
4. Puede revisitarse si aparecen señales futuras.

### 6.6 Regla de fallo del experimento

Si un experiment de validación falla (no alcanza su métrica de éxito dentro del deadline): [Decisión]

1. Documentar el resultado del fallo dentro de 7 días del deadline.
2. Opciones post-fallo:
   - **Reformular:** nueva hypothesis con nuevo experiment (máximo 1 reformulación).
   - **Archivar:** cerrar como Knowledge Asset con lesson learned documentado.
3. No se permite extender indefinidamente. Máximo 2 ciclos de experiment por oportunidad.

---

## 7. Decisión final

Al completar el proceso de derivación, el Fundador toma exactamente una de las siguientes decisiones: [Decisión]

| Decisión | Cuándo aplica | Acción requerida |
|----------|---------------|-----------------|
| **Advance** | Product_Hypothesis completa + confidence ≥ "emerging" + ≥1 demand signal externo + Quality Gate comercial aprobado | La hypothesis pasa a validación comercial. Se asigna a Package 004 (Product Factory) o al lab correspondiente. Se registra la transferencia. |
| **Archive** | Señales existen pero son insuficientes para avanzar hoy. O hypothesis incompleta. O experiment aún no ejecutable. | Documentar la oportunidad para evaluación futura. Registrar condiciones bajo las cuales revisitar. Archivar como Knowledge Asset con nota comercial. |
| **Discard** | Evidencia insuficiente para sostener la hypothesis. O 5 criterios de no-formulación se cumplen. O experiment falló sin reformulación viable. | Documentar rationale de descarte. Preservar la evaluación como aprendizaje. Cerrar sin plan de monetización. |

### 7.1 Registro de la decisión

Toda decisión se registra con: [Decisión]

| Campo | Contenido |
|-------|-----------|
| `decision` | advance / archive / discard |
| `date` | Fecha (ISO 8601) |
| `rationale` | 1-3 oraciones justificando la decisión |
| `conditions_to_revisit` | Qué cambiaría para reconsiderar (solo si archive) |
| `destination` | Package o lab destino (solo si advance) |
| `source_investigation` | Investigation ID |

---

## 8. Diagrama de flujo

```
Investigación pasa Asset Extraction (Etapa 13)
           │
           ▼
┌─────────────────────────────────────────────────────────────────────┐
│  ETAPA 14: PRODUCT HYPOTHESIS                                       │
│                                                                     │
│  PASO 1: Evaluación de señales                                      │
│     └── ¿Existen señales comerciales?                               │
│          ├── NO → ¿Aplica alguno de los 5 criterios de no-formular? │
│          │         └── SÍ → archivar sin hypothesis (§5)            │
│          └── SÍ → continuar                                         │
│                                                                     │
│  PASO 2: Product_Hypothesis                                         │
│     └── Completar 7 campos obligatorios                             │
│          ├── ¿Todos completos?                                      │
│          │    ├── NO → marcar "incomplete" + follow-up actions       │
│          │    └── SÍ → evaluar confidence level                     │
│          └── ¿Confidence ≥ "emerging" + demand signal externo?      │
│               ├── NO → archive                                      │
│               └── SÍ → continuar a paso 3                           │
│                                                                     │
│  PASO 3: Revenue_Hypothesis                                         │
│     └── Completar 7 campos obligatorios                             │
│          ├── ¿Evidencia suficiente (≥2 data points)?                │
│          │    ├── NO → concluir sin Revenue_Hypothesis (§4.4)       │
│          │    └── SÍ → completar campos                             │
│          └── ¿Todos completos?                                      │
│               ├── NO → marcar "incomplete" + acciones ≤30 días      │
│               └── SÍ → continuar a paso 4                           │
│                                                                     │
│  PASO 4: Decisión                                                   │
│     └── ¿Pasa Quality Gate comercial? (§6.4)                        │
│          ├── SÍ → ADVANCE (→ Package 004 o lab)                     │
│          ├── PARCIAL → ARCHIVE (oportunidad para futuro)            │
│          └── NO → DISCARD (cerrar con rationale)                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
           │
           ▼
Estado: Published (si advance) o Converted to Asset / Archived (si archive/discard)
```

---

## 9. Alineación con Package 000

Este documento se alinea explícitamente con los siguientes principios y reglas de Package 000 — Foundation: [Hecho]

| Referencia Package 000 | Documento fuente | Aplicación en este documento |
|------------------------|------------------|------------------------------|
| **Regla de negocio 2:** "Todo activo debe tener una hipótesis de producto o monetización" | business-principles steering | Sección 3 y 4: modelos de Product y Revenue Hypothesis |
| **Regla de negocio 4:** "Evitar construir demasiado antes de vender. La validación de demanda precede a la inversión" | business-principles steering | Sección 6.1: no avanzar sin demand signal externo |
| **Prohibición:** "No asumir product-market fit sin evidencia de pago" | business-principles steering | Sección 4.3: transacción real requerida para validación |
| **Prohibición:** "No invertir más de 90 días en un activo sin señal de demanda" | business-principles steering | Sección 6.5: archivado a 30 días sin señal |
| **Modelo de negocio, Regla 1:** "Ninguna ruta se considera validada hasta cumplir su criterio de éxito" | 008-business-model.md | Sección 4.3 y 6.6: hypothesis no validada sin transacción |
| **Modelo de negocio, Regla 2:** "No invertir en etapa 3 sin validación en etapas 1-2" | 008-business-model.md | Sección 6.2: inversión máxima pre-validación |
| **Anti-pattern (R30):** "Automatically converting every investigation into a commercial product" | R30.2 | Sección 5: 5 criterios para no formular hypothesis |
| **Regla 3 negocio:** "Priorizar activos validables en menos de 30 o 90 días" | business-principles steering | Sección 3.1 campo 7 (experiment ≤30 días), sección 4.1 campo 7 (≤90 días) |

### 9.1 Coherencia con clasificación epistémica

- Product_Hypothesis y Revenue_Hypothesis se clasifican con etiqueta [Hipótesis] hasta que se validen con transacción real.
- Solo después de transacción real documentada, una hypothesis puede considerarse [Hecho] parcial (el mecanismo funciona, no necesariamente a escala).
- Las reglas de este documento se clasifican como [Decisión] porque son elecciones de governance del Fundador.

---

## 10. Referencias

| Requirement | Cobertura en este documento |
|-------------|----------------------------|
| R16.1 | Sección 3.1: 7 campos obligatorios de Product_Hypothesis con definiciones y ejemplos |
| R16.2 | Sección 3.2-3.3: campos adicionales (source_investigation, confidence_level) y criterios de clasificación |
| R16.3 | Sección 3.4: 3 condiciones para avanzar (campos completos, confidence ≥ emerging, demand signal externo) |
| R16.4 | Sección 3.5: hypothesis incompleta con campos faltantes identificados y acciones de follow-up |
| R17.1 | Sección 4.1: 7 campos obligatorios de Revenue_Hypothesis con definiciones y ejemplos |
| R17.2 | Sección 4.4: concluir sin Revenue_Hypothesis cuando <2 data points de demanda |
| R17.3 | Sección 4.3: prohibición de tratar hypothesis como validated revenue sin transacción real |
| R17.4 | Sección 4.5: Revenue_Hypothesis incompleta con acciones ≤30 días por campo faltante |
| R31.1 | Sección 6.1: hypothesis clasificada con [Hipótesis] hasta demand signal + 3 campos mínimos de monetización |
| R31.2 | Sección 5: 5 condiciones que impiden formulación + sección 6.1 no avanzar sin demand signal |
| R31.3 | Sección 6.4: Quality Gate comercial con campos, experiment, métrica, deadline, demand signal |
| R31.4 | Sección 6.5: archivado como Knowledge Asset a 30 días sin demand signal |
| R31.5 | Sección 6.6: documentar fallo + reformular o archivar en 7 días |

---

## Notas finales

- Este documento define el proceso de **evaluación de oportunidad comercial**. La ejecución de la validación comercial corresponde a Package 004 — Product Factory o al lab específico del dominio. [Hecho]
- El proceso es deliberadamente conservador. Prefiere falsos negativos (no monetizar algo monetizable) a falsos positivos (invertir en algo sin demanda). Esta es una decisión de governance para proteger el recurso más escaso: el tiempo del Fundador. [Decisión]
- La conexión con 018-research-to-asset.md es secuencial: primero se extraen activos (Etapa 13), luego se evalúa oportunidad comercial (Etapa 14). No se puede evaluar hypothesis sin activo previo. [Hecho]

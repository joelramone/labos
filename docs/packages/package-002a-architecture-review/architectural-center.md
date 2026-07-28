# Centro Arquitectónico

## Propósito

Este documento determina explícitamente el centro arquitectónico de LabOS — el concepto organizador alrededor del cual todas las decisiones de diseño gravitan. [Decisión] La elección del centro arquitectónico tiene implicaciones profundas: determina qué se optimiza primero, qué se sacrifica en caso de conflicto, y cómo se evalúa el éxito del sistema.

---

## Candidatos Evaluados

### 1. Research-Driven (centrado en investigación)

**Descripción:** La investigación rigurosa es el motor principal. Todo lo demás (activos, productos, revenue) es consecuencia natural de investigación bien ejecutada.

**Evidencia a favor:**
- Package 001 es el más extenso (26 documentos, 16 etapas de lifecycle). [Hecho]
- 12 principios de investigación definidos con nivel de detalle superior a cualquier otro aspecto. [Hecho]
- El Research_Lifecycle tiene más quality gates que cualquier otro proceso. [Hecho]

**Evidencia en contra:**
- El manifiesto (Package 000) establece "Vender antes de construir" como principio #4. [Hecho]
- Las reglas operativas priorizan flujo de caja sobre infraestructura. [Hecho]
- El business model existe explícitamente con rutas de monetización. [Hecho]

**Trade-offs:** Alta calidad epistémica, pero riesgo de nunca convertir a revenue. Perfecto para academia, subóptimo para startup.

---

### 2. Knowledge-Driven (centrado en conocimiento)

**Descripción:** La gestión y capitalización del conocimiento es el núcleo. La investigación alimenta el conocimiento, y el conocimiento se transforma en valor.

**Evidencia a favor:**
- LabOS se define como "sistema operativo para empresas de conocimiento". [Hecho]
- El pipeline completo (research→knowledge→assets→products→revenue) implica conocimiento como intermediario. [Hecho]
- El Asset_First_Model convierte conocimiento en artefactos tangibles. [Hecho]

**Evidencia en contra:**
- No existe un Package de Knowledge Architecture ejecutado aún (002 está pendiente). [Hecho]
- No hay entidad "Knowledge" definida formalmente en ningún glosario. [Hecho]
- El sistema actual es más un "Documentation OS" que un "Knowledge OS" en la práctica. [Hecho]

**Trade-offs:** Alineado con la visión declarada, pero prematuro como centro cuando la abstracción de conocimiento aún no está definida.

---

### 3. Capability-Driven (centrado en capacidades)

**Descripción:** Las capacidades del ecosistema (qué puede hacer cada lab) son el organizador central. El sistema optimiza para descubrir, desarrollar y monetizar capacidades.

**Evidencia a favor:**
- El portfolio model implica capacidades distribuidas entre labs. [Hecho]
- La reutilización de activos requiere entender qué capacidades existen. [Hecho]

**Evidencia en contra:**
- No existe concepto "Capability" en ningún documento. [Hecho]
- Con 2 labs activos, la interoperabilidad de capacidades no es un problema real. [Hecho]
- Abstracción prematura para la etapa actual. [Hecho]

**Trade-offs:** Elegante a escala, pero irrelevante con 1 operador y 2 labs activos.

---

### 4. Product-Driven (centrado en producto)

**Descripción:** El producto (lo que se vende) es el organizador central. Todo se evalúa por su contribución a un producto vendible.

**Evidencia a favor:**
- Los business principles priorizan monetización. [Hecho]
- El principio de "vender antes de construir" implica orientación a producto. [Hecho]
- Las rutas de monetización son explícitas y con timelines. [Hecho]

**Evidencia en contra:**
- No existe un producto definido aún. [Hecho]
- LabOS no es un SaaS, no es una app, no tiene usuarios. [Hecho]
- Ser product-driven sin producto es una contradicción operativa. [Hecho]

**Trade-offs:** Correcto para etapa de scaling, pero prematuro cuando no hay product-market fit.

---

### 5. Document-Driven (centrado en documentación)

**Descripción:** La documentación es el producto y el proceso. Todo se manifiesta primero como documento, y los documentos son la fuente de verdad.

**Evidencia a favor:**
- LabOS se declara "documentation-first". [Hecho]
- Toda actividad produce documentación como output primario. [Hecho]
- Los principios de ingeniería y manifiesto refuerzan este enfoque. [Hecho]
- La estructura de packages ES un sistema de documentos. [Hecho]

**Evidencia en contra:**
- "Documentation-first" es un MÉTODO, no un OBJETIVO. [Decisión]
- El objetivo declarado es revenue, no documentación. [Hecho]
- Riesgo de optimizar para documentación perfecta sin conversión a valor. [Hipótesis]

**Trade-offs:** Describe el cómo correctamente pero confunde medio con fin si se adopta como centro.

---

### 6. Hybrid: Knowledge-to-Value Pipeline

**Descripción:** El centro no es un concepto único sino el PIPELINE de transformación: investigación → conocimiento → activos → productos → revenue. El sistema se optimiza para maximizar el throughput de este pipeline.

**Evidencia a favor:**
- Refleja la misión declarada: "transformar investigación en activos reutilizables y líneas de negocio". [Hecho]
- Reconcilia la tensión research vs revenue: ambos son etapas del mismo pipeline. [Hecho]
- El Asset_First_Model ya es un punto medio en este pipeline. [Hecho]
- Permite evaluar cada package por su contribución al flujo de valor. [Hecho]

**Evidencia en contra:**
- No existe un documento único que formalice este pipeline completo. [Hecho]
- Es un concepto emergente de la revisión, no declarado originalmente. [Hecho]

**Trade-offs:** Requiere formalización, pero es el único candidato que reconcilia todas las tensiones observadas.

---

## Decisión: Centro Arquitectónico

### Centro primario: KNOWLEDGE-TO-VALUE PIPELINE [Decisión]

**Definición:** El centro arquitectónico de LabOS es el pipeline de transformación de conocimiento en valor económico. Cada componente del sistema se evalúa por su contribución al flujo: Research → Knowledge → Assets → Products → Revenue.

**Implicaciones operativas:**

1. **Investigación no es el fin, es la entrada del pipeline.** El Package 001 es riguroso y eso está bien, pero su éxito se mide por cuántos activos y productos genera, no por cuántas investigaciones se completan. [Decisión]

2. **Documentación es el medio de transporte, no el destino.** Documentation-first se mantiene como método pero no como objetivo. La documentación fluye por el pipeline. [Decisión]

3. **Revenue es la salida, no el motor.** No se persigue revenue directamente sin pasar por las etapas previas. El pipeline tiene secuencia por diseño. [Decisión]

4. **El Asset_First_Model es el acelerador del pipeline.** Convierte investigación en artefactos que pueden fluir hacia producto. Es el mecanismo de conversión más importante. [Decisión]

5. **Todo componente que no contribuye al pipeline debe justificar su existencia.** Gobernanza, revisiones, compliance, maturity models — se evalúan por si facilitan o entorpecen el flujo de valor. [Decisión]

### Centro secundario: DOCUMENTATION AS METHOD [Decisión]

Documentation-first se mantiene como el método operativo del pipeline, no como su centro. Significa que cada etapa del pipeline produce documentación como output verificable, pero la documentación es medio, no fin.

---

## Diagrama del Centro Arquitectónico

```text
┌─────────────────────────────────────────────────────────┐
│              KNOWLEDGE-TO-VALUE PIPELINE                  │
│                                                          │
│  ┌──────────┐    ┌───────────┐    ┌──────────┐         │
│  │ Research │───▶│ Knowledge │───▶│  Assets  │         │
│  │ (Pkg 001)│    │ (Pkg 002) │    │ (Pkg 003)│         │
│  └──────────┘    └───────────┘    └──────────┘         │
│       │                                  │               │
│       │         DOCUMENTATION-FIRST      │               │
│       │         (método transversal)     │               │
│       ▼                                  ▼               │
│  ┌──────────┐                      ┌──────────┐        │
│  │ Evidence │                      │ Products │        │
│  │ & Rigor  │                      │ (Pkg 004)│        │
│  └──────────┘                      └────┬─────┘        │
│                                          │               │
│                                          ▼               │
│                                    ┌──────────┐         │
│                                    │ Revenue  │         │
│                                    │ (Pkg 005)│         │
│                                    └──────────┘         │
│                                                          │
│  ─────── Foundation (Pkg 000) ───────────────────       │
│  Principios, modelo, gobernanza, invariantes             │
└─────────────────────────────────────────────────────────┘
```

---

## Consecuencias de esta Decisión

| Aspecto | Antes (implícito) | Después (explícito) |
|---------|-------------------|---------------------|
| Éxito del research | Investigación completa y rigurosa | Investigación que genera activos convertibles |
| Éxito del package | Documentos producidos | Contribución medible al pipeline |
| Priorización | Rigor investigativo primero | Throughput del pipeline primero |
| Governance | Compliance formal | Facilitación del flujo |
| Métricas clave | Investigaciones completadas | Activos productizados, revenue generado |

---

## Riesgos de esta Decisión

1. **Riesgo de sacrificar rigor por velocidad.** Si el pipeline se optimiza solo para throughput, puede degradar la calidad epistémica que hace a LabOS diferente. **Mitigación:** INV-01 (clasificación epistémica) e INV-02 (toda investigación produce activo) permanecen como invariantes. [Hipótesis]

2. **Riesgo de que "Knowledge" sea aún abstracto.** El Package 002 no se ha ejecutado, así que la etapa "Knowledge" del pipeline aún no tiene definición formal. **Mitigación:** No bloquear el pipeline por la ausencia del package. Los activos pueden fluir directamente de research a products en la etapa actual. [Decisión]

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 24       | 53%        |
| [Hipótesis]   | 3        | 7%         |
| [Decisión]    | 18       | 40%        |
| [Visión]      | 0        | 0%         |

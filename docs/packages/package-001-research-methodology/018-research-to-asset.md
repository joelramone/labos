# 018 — Research-to-Asset

[Decisión]

## Propósito

Este documento define el **proceso de extracción de activos reutilizables** a partir de investigaciones completadas dentro de LabOS. [Hecho]

El proceso establece:

- Un flujo de handoff en 5 etapas: identificación, clasificación, documentación, transferencia, quality gate
- 5 tipos de activo con criteria mínimos para cada uno
- Un modelo de Asset Handoff con campos obligatorios
- Un quality gate verificable para determinar si un activo está listo
- Una regla para investigaciones que no producen activos extraíbles

Toda investigación que supera su Conclusion Quality Gate (documentado en [017-conclusion-framework.md](./017-conclusion-framework.md)) debe pasar por este proceso antes de considerarse completamente cerrada. El handoff ocurre en la **Etapa 13: Asset Extraction** del Research Lifecycle. [Decisión]

---

## 1. Proceso de handoff

El proceso de extracción de activos consta de 5 etapas secuenciales. Cada etapa tiene un propósito definido y un output verificable. [Decisión]

### 1.1 Etapa 1: Identificación

| Campo | Valor |
|-------|-------|
| **Propósito** | Determinar qué outputs de la investigación son reutilizables fuera de su contexto original |
| **Input** | Conclusions, findings y artifacts de la investigación aprobada en Review |
| **Actividades** | Revisar cada output preguntando: ¿tiene valor independiente del contexto de esta investigación? ¿Otro lab, proyecto o persona podría beneficiarse? |
| **Output** | Lista de candidatos a activo con justificación de por qué cada uno es reutilizable |
| **Criterio de avance** | Al menos un candidato identificado, o decisión explícita de que no hay activos extraíbles (ver sección 6) |

### 1.2 Etapa 2: Clasificación

| Campo | Valor |
|-------|-------|
| **Propósito** | Asignar tipo de activo a cada candidato según su naturaleza |
| **Input** | Lista de candidatos a activo |
| **Actividades** | Para cada candidato, asignar exactamente un tipo de los 5 definidos (ver sección 2). Evaluar si cumple los criteria mínimos del tipo asignado |
| **Output** | Candidatos clasificados por tipo con evaluación preliminar de criteria |
| **Criterio de avance** | Cada candidato tiene un tipo asignado y una evaluación de criteria mínimos (cumple / no cumple / parcial) |

### 1.3 Etapa 3: Documentación

| Campo | Valor |
|-------|-------|
| **Propósito** | Completar el Asset Handoff Record con todos los campos obligatorios |
| **Input** | Candidatos clasificados que cumplen criteria mínimos |
| **Actividades** | Completar todos los campos del Asset Handoff (ver sección 3) para cada activo. Redactar usage hypothesis y definir target audience |
| **Output** | Asset Handoff Record completo por cada activo |
| **Criterio de avance** | Todos los campos obligatorios están completos y coherentes |

### 1.4 Etapa 4: Transferencia

| Campo | Valor |
|-------|-------|
| **Propósito** | Colocar el activo en su ubicación definitiva dentro del repositorio de activos |
| **Input** | Asset Handoff Record completo |
| **Actividades** | Mover o crear referencia en `assets/{type}/`. Actualizar índice de activos. Crear trazabilidad bidireccional (investigación → activo, activo → investigación) |
| **Output** | Activo accesible en su carpeta correspondiente con metadata y link de trazabilidad |
| **Criterio de avance** | Activo localizable en `assets/{type}/`, referenciado en el conclusion document de la investigación fuente |

### 1.5 Etapa 5: Quality Gate

| Campo | Valor |
|-------|-------|
| **Propósito** | Verificar que el activo cumple los criterios mínimos de calidad para ser considerado un activo válido |
| **Input** | Activo transferido con metadata |
| **Actividades** | Evaluar los 4 criterios del quality gate (ver sección 4). Registrar resultado |
| **Output** | Decisión: activo aprobado (state → "ready") o activo requiere revisión (state permanece "draft") |
| **Criterio de avance** | Los 4 criterios del quality gate están evaluados con resultado explícito |

---

## 2. Tipos de activo

LabOS define 5 tipos de activo. Cada investigación completada debe clasificar sus outputs reutilizables en exactamente uno de estos tipos. [Decisión]

### 2.1 Knowledge Asset

| Campo | Valor |
|-------|-------|
| **Definición** | Insight documentado, framework conceptual, comparativa o análisis que captura conocimiento validado |
| **Criteria mínimos** | (1) Insight documentado con afirmación clara, (2) Fuentes citadas con referencia al Source_Register, (3) Limitaciones declaradas explícitamente |
| **Ejemplos** | Comparativa de frameworks, análisis de mercado, síntesis de estado del arte, framework conceptual documentado |
| **Carpeta destino** | `assets/knowledge/` |

### 2.2 Technical Asset

| Campo | Valor |
|-------|-------|
| **Definición** | Artefacto técnico funcional que resuelve un problema concreto de forma reproducible |
| **Criteria mínimos** | (1) Funcional en el contexto para el que fue diseñado, (2) Documentado con instrucciones de uso, (3) Reproducible — otro usuario puede ejecutarlo o aplicarlo siguiendo la documentación |
| **Ejemplos** | Script de automatización, configuración documentada, arquitectura de referencia, template técnico, herramienta CLI |
| **Carpeta destino** | `assets/technical/` |

### 2.3 Educational Asset

| Campo | Valor |
|-------|-------|
| **Definición** | Material con estructura pedagógica diseñado para transferir conocimiento a una audiencia definida |
| **Criteria mínimos** | (1) Estructura pedagógica clara (progresión lógica del contenido), (2) Prerequisitos definidos explícitamente, (3) Al menos un ejercicio, ejemplo práctico o demostración incluido |
| **Ejemplos** | Tutorial paso a paso, guía práctica, material de curso, workshop documentado |
| **Carpeta destino** | `assets/educational/` |

### 2.4 Commercial Asset

| Campo | Valor |
|-------|-------|
| **Definición** | Artefacto con propuesta de valor clara, orientado a un segmento definido, en formato entregable a un potencial cliente o comprador |
| **Criteria mínimos** | (1) Propuesta de valor articulada en ≤2 oraciones, (2) Target audience definido como un segmento identificable, (3) Formato entregable especificado (plantilla, servicio, producto, herramienta) |
| **Ejemplos** | Template vendible, service blueprint, herramienta productizada, contenido premium |
| **Carpeta destino** | `assets/commercial/` |

### 2.5 Data Asset

| Campo | Valor |
|-------|-------|
| **Definición** | Colección de datos estructurados con schema documentado y condiciones de uso definidas |
| **Criteria mínimos** | (1) Schema documentado con descripción de cada campo o variable, (2) Fuentes de datos citadas con fechas de recopilación, (3) Limitaciones de uso declaradas (temporalidad, alcance geográfico, sesgo conocido) |
| **Ejemplos** | Dataset curado, benchmark con resultados, colección de mediciones, corpus de datos etiquetados |
| **Carpeta destino** | `assets/data/` |

### 2.6 Regla de clasificación

Si un activo podría clasificarse en más de un tipo, se asigna el tipo que mejor describe su **uso principal previsto**. [Decisión] La ambigüedad se documenta en el campo `description` del Asset Handoff Record.

Un mismo investigation puede producir múltiples activos de diferentes tipos. Cada activo se documenta y gestiona independientemente con su propio Asset Handoff Record. [Decisión]

---

## 3. Modelo de Asset Handoff Record

Todo activo extraído de una investigación se documenta con la siguiente estructura: [Decisión]

```
Asset Handoff Record
├── name                    : string (≤80 caracteres)
│   Nombre descriptivo del activo.
│   Ejemplo: "Comparativa de frameworks de orquestación de agentes 2024"
│
├── type                    : enum (knowledge | technical | educational | commercial | data)
│   Tipo de activo según la taxonomía definida en sección 2.
│
├── description             : string (1-3 oraciones)
│   Qué es el activo, qué contiene y qué problema resuelve o qué conocimiento captura.
│   Ejemplo: "Análisis comparativo de 5 frameworks de orquestación de agentes IA
│   evaluados contra 8 criterios técnicos. Incluye matriz de decisión y recomendación
│   contextual para equipos de 1-3 personas."
│
├── usage_hypothesis        : string
│   Quién usaría este activo y cómo.
│   Debe identificar al menos un segmento de audiencia específico y un caso de uso.
│   Ejemplo: "Fundadores técnicos evaluando frameworks de agentes para su primer
│   producto AI-native podrían usar esta comparativa para reducir tiempo de selección
│   de semanas a horas."
│
├── target_audience         : string
│   Segmento o perfil específico del consumidor previsto del activo.
│   Ejemplo: "Desarrolladores senior y CTOs de startups en etapa pre-seed/seed
│   que están construyendo productos con agentes de IA."
│
├── source_investigation    : object
│   ├── investigation_id   : string
│   │   Identificador de la investigación fuente.
│   ├── conclusion_date    : date (YYYY-MM-DD)
│   │   Fecha en que la conclusión fue aprobada en Review.
│   └── conclusion_ref     : string
│       Referencia al Conclusion Record (CON-xxx).
│
├── state                   : enum (draft | ready | published)
│   Estado actual del activo:
│   - draft: extraído pero no verificado contra quality gate
│   - ready: aprobó quality gate, listo para uso o publicación
│   - published: disponible externamente o en uso activo
│
└── metadata_extended       : object (opcional)
    Campos adicionales no obligatorios:
    ├── dependencies        : string[]
    │   Qué necesita el consumidor para usar este activo.
    ├── monetization_potential : enum (none | low | medium | high)
    │   Potencial de monetización con justificación.
    └── tags                : string[]
        Etiquetas para facilitar búsqueda y conexión con otros activos.
```

### 3.1 Reglas del modelo

1. **Todos los campos principales son obligatorios.** Un Asset Handoff Record sin `name`, `type`, `description`, `usage_hypothesis`, `target_audience`, `source_investigation` o `state` no se considera válido. [Decisión]
2. **El campo `state` inicia en "draft"** al momento de la extracción. Solo transiciona a "ready" tras aprobar el quality gate. [Decisión]
3. **El campo `name` no excede 80 caracteres.** Si el nombre natural del activo excede este límite, se acorta y el nombre completo se documenta al inicio de `description`.
4. **Un Asset Handoff Record por activo.** Si una investigación produce 3 activos, se crean 3 records independientes.

---

## 4. Quality Gate de Asset

El quality gate determina si un activo en estado "draft" puede transicionar a "ready". Se evalúan 4 criterios. **Todos deben cumplirse** para aprobar el gate. [Decisión]

### 4.1 Criterios del quality gate

| # | Criterio | Pregunta de verificación | Cumple si... |
|---|----------|--------------------------|--------------|
| 1 | **Autocontenido** | ¿Se puede comprender y usar el activo sin necesidad de leer la investigación fuente completa? | El activo incluye suficiente contexto, definiciones y referencias para ser consumido independientemente. No requiere acceso a documentos internos de la investigación para ser entendido. |
| 2 | **Uso identificado** | ¿Tiene un uso concreto identificado más allá de documentar por documentar? | El campo `usage_hypothesis` describe un caso de uso real y específico. Existe al menos un consumidor potencial identificable (que no sea únicamente el autor). |
| 3 | **Metadata completa** | ¿Están todos los campos obligatorios del Asset Handoff Record completos y coherentes? | Todos los campos obligatorios tienen valores no vacíos. Los valores son coherentes entre sí (el type coincide con la naturaleza del activo, la description refleja el contenido real). |
| 4 | **Sin información sensible** | ¿El activo ha sido sanitizado de información confidencial, personal o propietaria no autorizada? | No contiene credenciales, tokens, datos personales sin anonimizar, información de clientes sin consentimiento, o contenido bajo NDA no autorizado para distribución. |

### 4.2 Proceso de evaluación

1. Evaluar cada criterio como: **cumple** / **no cumple**.
2. Si los 4 criterios se cumplen: `state` → "ready".
3. Si uno o más criterios no se cumplen: `state` permanece "draft", se documenta qué criterio(s) fallan y qué acción correctiva se requiere.
4. Un activo puede re-evaluarse después de correcciones. No hay límite de re-evaluaciones.

### 4.3 Responsable

El Fundador es responsable de evaluar el quality gate. En esta etapa de LabOS (operación unipersonal), el autor y el evaluador son la misma persona. Se espera rigor en la autoevaluación. [Hecho]

---

## 5. Conexión con Package 003 — Asset System

El repositorio de activos (`assets/`) es gestionado formalmente por Package 003 — Asset System. [Hecho] Este documento define el proceso de **entrada** de activos al repositorio desde investigación. Package 003 define:

- Estructura completa del repositorio de activos
- Lifecycle de un activo post-extracción (maduración, actualización, deprecación)
- Índice centralizado y búsqueda
- Métricas de uso y valor de activos

El handoff entre Package 001 (Research Methodology) y Package 003 (Asset System) se produce cuando el activo aprueba el quality gate definido en sección 4 y es colocado en `assets/{type}/`. [Decisión]

---

## 6. Investigaciones sin activo extraíble

No toda investigación produce un activo reutilizable. Cuando una investigación pasa su Conclusion Quality Gate pero el Fundador determina que no hay activo extraíble significativo, se aplica la siguiente regla: [Decisión]

### 6.1 Regla de excepción

**La ausencia de activo requiere justificación obligatoria.** No es válido cerrar una investigación sin activo y sin explicación.

### 6.2 Requisitos de la justificación

La justificación debe:

1. Tener entre 1 y 3 oraciones.
2. Explicar **por qué** no se pudo extraer un activo reutilizable.
3. Registrarse en el conclusion document de la investigación (campo `asset_extraction_note`).

### 6.3 Razones válidas para no producir activo

| Razón | Ejemplo |
|-------|---------|
| Resultado inconclusos sin insight reutilizable | "La investigación no alcanzó conclusiones suficientes para documentar un insight independiente." |
| Conocimiento altamente contextual sin valor fuera del caso | "Los hallazgos son específicos a una configuración particular que no se replicará." |
| Activo ya existente cubre el mismo espacio | "El activo AST-K-014 ya cubre este conocimiento con mayor profundidad." |
| Restricciones de IP o confidencialidad | "Los datos del cliente impiden documentar los hallazgos como activo público." |
| Investigación exploratoria sin hallazgo consolidable | "La exploración sirvió para descartar opciones sin producir un framework o guía aplicable." |

### 6.4 Regla de volumen

Si más del 30% de las investigaciones completadas en un período de 90 días concluyen sin activo extraíble, el Fundador debe revisar la calidad de las preguntas de investigación y el scope de las investigaciones iniciadas. Esto es una señal de alerta, no un bloqueo. [Decisión]

---

## 7. Trazabilidad bidireccional

Toda extracción de activo genera dos links de referencia: [Decisión]

### 7.1 Investigación → Activo

En el conclusion document de la investigación se registra:

- Nombre del activo extraído
- Tipo de activo
- Ubicación en el repositorio (`assets/{type}/{filename}`)
- Estado al momento de la extracción

### 7.2 Activo → Investigación

En el metadata header del activo (dentro de su archivo en `assets/`) se registra:

- Investigation ID de origen
- Fecha de conclusión
- Referencia al Conclusion Record (CON-xxx)

Esta trazabilidad permite navegar en ambas direcciones: desde una investigación ver qué activos produjo, y desde un activo rastrear qué investigación lo originó. [Hecho]

---

## 8. Diagrama de flujo completo

```
Investigación pasa Review (Etapa 12)
           │
           ▼
┌─────────────────────────────────────────────────────┐
│  ETAPA 13: ASSET EXTRACTION                         │
│                                                     │
│  1. Identificación                                  │
│     └── ¿Hay outputs reutilizables?                 │
│          ├── SÍ → continuar                         │
│          └── NO → justificación obligatoria (§6)    │
│                   → investigación se archiva         │
│                                                     │
│  2. Clasificación                                   │
│     └── Asignar tipo (Knowledge/Technical/          │
│         Educational/Commercial/Data)                │
│     └── Evaluar criteria mínimos                    │
│                                                     │
│  3. Documentación                                   │
│     └── Completar Asset Handoff Record              │
│     └── Todos los campos obligatorios               │
│                                                     │
│  4. Transferencia                                   │
│     └── Colocar en assets/{type}/                   │
│     └── Crear links de trazabilidad                 │
│                                                     │
│  5. Quality Gate                                    │
│     └── ¿Autocontenido? ✓                           │
│     └── ¿Uso identificado? ✓                        │
│     └── ¿Metadata completa? ✓                       │
│     └── ¿Sin info sensible? ✓                       │
│          ├── TODO SÍ → state: "ready"               │
│          └── ALGO NO → state: "draft" + corrección  │
│                                                     │
└─────────────────────────────────────────────────────┘
           │
           ▼
Estado: Converted to Asset → continúa a Etapa 14
```

---

## Referencias

| Requirement | Cobertura en este documento |
|-------------|----------------------------|
| R15.1 | Sección 1 (proceso completo de identificación y extracción) |
| R15.2 | Sección 3 (Asset Handoff Record con campos: name, type, description, usage hypothesis, target audience, source investigation, state) |
| R15.3 | Sección 1.4 (procedimiento de transferencia) y sección 7 (trazabilidad) |
| R15.4 | Sección 2.6 (múltiples activos independientes por investigación) — implícito en R15.3 original |
| R15.5 | Sección 4 (quality gate con 4 criterios para transición draft → ready) |
| R15.6 | Sección 6 (regla de excepción para investigaciones sin activo) |

---

## Notas finales

- Este documento define el proceso de **entrada** al repositorio de activos. La gestión completa del lifecycle de activos corresponde a Package 003 — Asset System.
- La obligatoriedad de producir al menos un activo por investigación es un principio de negocio de LabOS (ver [business-principles steering](../../../.kiro/steering/business-principles.md)). La excepción documentada (sección 6) existe para casos legítimos, no como escape general.
- El quality gate es verificable por terceros: cada criterio tiene una pregunta con respuesta binaria (cumple/no cumple). [Hecho]

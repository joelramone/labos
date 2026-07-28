# Modelo de Capas del Conocimiento

## Propósito

Este documento define un modelo de capas que organiza el conocimiento dentro de LabOS según su naturaleza, madurez y función. [Decisión] El modelo establece qué tipo de información pertenece a cada capa, cómo se transita entre capas, y qué nivel de rigor se requiere en cada una.

---

## Decisión arquitectónica: 3 capas, no 5 ni 8

El prompt original sugería 8 capas y la evaluación intermedia propuso 5. Tras evaluar contra el Principio 6 (proporcionalidad de esfuerzo — overhead ≤2h/mes) y la realidad de un fundador solo operando con 20-25h/semana, se adoptan **3 capas operativas**. [Decisión]

**Justificación para colapsar capas:**

1. **Evidence Layer eliminada como capa de conocimiento.** La evidencia bruta (Source_Register, datos de experimentos) NO es conocimiento — es input. Ya está gestionada por Package 001 (Evidence Framework, Source Evaluation). Duplicar su gestión aquí viola Principio 2 (fuente única). [Decisión]

2. **Decision Layer colapsada en Canonical.** Las decisiones son conocimiento validado con un formato específico (ya documentadas en ADRs y decision logs de Package 001). No justifican una capa separada cuando el volumen es bajo y su lifecycle es idéntico al conocimiento canónico. [Decisión]

3. **Research Findings y Operational colapsadas en un modelo de 3 capas** que distingue por madurez y validación, no por origen. [Decisión]

Un fundador solo no necesita 5+ capas porque:
- El volumen de conocimiento no justifica granularidad fina. [Hecho]
- Más capas = más decisiones de clasificación = más overhead sin valor proporcional. [Hecho]
- La distinción relevante es: ¿está validado? ¿es estable? ¿es temporal? [Decisión]

---

## Las 3 capas

```text
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  CAPA 3: CONOCIMIENTO CANÓNICO                         │
│  ─────────────────────────────────────                  │
│  Validado. Estable. Alta confianza.                     │
│  Referenciado por decisiones y activos.                 │
│  Ventana de validez: 90-365 días.                       │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  CAPA 2: CONOCIMIENTO VALIDADO                          │
│  ─────────────────────────────────────                  │
│  Sintetizado. Confianza asignada.                       │
│  Útil para operación y toma de decisiones.              │
│  Ventana de validez: 30-90 días.                        │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  CAPA 1: CONOCIMIENTO CAPTURADO                         │
│  ─────────────────────────────────────                  │
│  Recién registrado. Mínimo viable.                      │
│  Requiere síntesis o validación.                        │
│  Ventana de validez: 7-30 días.                         │
│                                                         │
└─────────────────────────────────────────────────────────┘

        ▼ DEBAJO (NO es conocimiento) ▼

┌─────────────────────────────────────────────────────────┐
│  EVIDENCIA / DATOS CRUDOS                               │
│  Gestionados por Package 001 (Evidence Framework).      │
│  Input al sistema de conocimiento, no parte de él.      │
└─────────────────────────────────────────────────────────┘
```

---

## Capa 1: Conocimiento Capturado

### Definición

Conocimiento recién registrado que cumple el umbral mínimo para ser considerado conocimiento (no es dato crudo) pero que aún no ha sido validado ni ha recibido revisión formal. [Decisión]

### Qué pertenece aquí

- Hallazgos iniciales de una investigación recién concluida. [Hecho]
- Insights operativos capturados durante el trabajo diario. [Hecho]
- Observaciones de mercado con fuente identificada pero sin validación cruzada. [Hecho]
- Conclusiones preliminares de experimentos. [Hecho]

### Qué NO pertenece aquí

- Datos sin sintetizar (esos son evidencia, gestionados por Package 001). [Decisión]
- Bookmarks o listas de enlaces sin síntesis (no cumplen Principio 1). [Decisión]
- Conocimiento ya validado que pertenece a Capa 2 o 3. [Hecho]

### Criterios de entrada

| Criterio | Descripción |
|----------|-------------|
| Síntesis mínima | Existe al menos una afirmación clasificada epistémicamente. [Decisión] |
| Fuente identificada | Se referencia la investigación o fuente de origen. [Decisión] |
| Campos obligatorios | Cumple el mínimo del Knowledge Object Contract (campos mandatory). [Decisión] |

### Criterios de salida (transición a Capa 2)

| Criterio | Descripción |
|----------|-------------|
| Confianza asignada | Se evaluó y asignó nivel alto/medio/bajo con justificación. [Decisión] |
| Validación básica | El fundador revisó la afirmación y confirmó coherencia. [Decisión] |
| Evidencia referenciada | Se documentó la evidencia que soporta la afirmación. [Decisión] |

### Owner

Fundador (captura) o agente IA (captura automatizada con revisión humana pendiente). [Decisión]

### Ventana de validez típica

7-30 días. Si no transita a Capa 2 dentro de 30 días, se marca para revisión (¿sigue siendo relevante?). [Decisión]

### Ejemplo

> **(EJEMPLO: Crypto Scalping Core)** El fundador observa que los spreads en el par BTC/USDT en Binance se ensanchan consistentemente entre 02:00-04:00 UTC. Registra esta observación como Knowledge Object con confianza "bajo" y referencia a 3 días de datos observados manualmente. Capa 1 hasta que se valide con dataset más amplio.

---

## Capa 2: Conocimiento Validado

### Definición

Conocimiento que ha sido revisado, tiene confianza asignada con justificación, y es útil para operación y toma de decisiones. [Decisión] Es el "conocimiento de trabajo" — confiable para actuar, pero no necesariamente estable a largo plazo.

### Qué pertenece aquí

- Hallazgos de investigación confirmados con evidencia suficiente. [Hecho]
- Insights operativos validados por experiencia repetida. [Hecho]
- Conocimiento con confianza media-alta y fuente trazable. [Hecho]
- Metodologías probadas en al menos un contexto real. [Hecho]

### Qué NO pertenece aquí

- Conocimiento sin confianza asignada (pertenece a Capa 1). [Decisión]
- Conocimiento con alta estabilidad y múltiples referencias externas (candidato a Capa 3). [Decisión]
- Datos operativos efímeros (e.g., "precio de BTC hoy" no es conocimiento). [Hecho]

### Criterios de entrada

| Criterio | Descripción |
|----------|-------------|
| Confianza explícita | Nivel alto o medio con justificación documentada. [Decisión] |
| Fuente verificada | La procedencia es trazable y la fuente sigue vigente. [Decisión] |
| Clasificación epistémica | Al menos la afirmación principal está clasificada. [Decisión] |

### Criterios de salida (transición a Capa 3)

| Criterio | Descripción |
|----------|-------------|
| Estabilidad demostrada | No ha cambiado en ≥2 ciclos de revisión consecutivos. [Decisión] |
| Alta confianza | Nivel "alto" con evidencia robusta. [Decisión] |
| Referenciado por otros | Otros Knowledge Objects o decisiones lo referencian. [Decisión] |
| Potencial de activo | Tiene potencial claro de transformarse en Asset reutilizable. [Decisión] |

### Owner

Fundador (validación y decisión de promoción). [Decisión]

### Ventana de validez típica

30-90 días. Conocimiento que no se revalida en 90 días se marca como candidato a revisión. [Decisión]

### Ejemplo

> **(EJEMPLO: Crypto Scalping Core)** Tras analizar 30 días de datos históricos de spread en Binance BTC/USDT, el fundador confirma que el spread se ensancha 40-60% durante 02:00-04:00 UTC en el 85% de los días observados. Confianza: "alto" (evidencia cuantitativa de 30 días). Capa 2 — útil para decisiones de timing operativo. Candidato a Capa 3 si se confirma en el siguiente trimestre.

---

## Capa 3: Conocimiento Canónico

### Definición

Conocimiento estable, de alta confianza, que ha demostrado validez sostenida y es referenciado activamente por decisiones, activos o procesos del ecosistema. [Decisión] Es el "gold standard" — el conocimiento en el que se basa la operación a largo plazo.

### Qué pertenece aquí

- Principios de dominio verificados con evidencia robusta y estabilidad temporal. [Hecho]
- Conocimiento que fundamenta decisiones arquitectónicas o de negocio. [Hecho]
- Metodologías probadas en múltiples contextos o ciclos. [Hecho]
- Conocimiento que ya se transformó o es candidato maduro para transformarse en Asset. [Hecho]

### Qué NO pertenece aquí

- Conocimiento reciente sin historial de estabilidad (pertenece a Capa 2). [Decisión]
- Conocimiento de dominio rápidamente cambiante sin revalidación (e.g., "mejores APIs de 2024" caduca rápido). [Decisión]
- Opiniones o preferencias del fundador sin evidencia externa. [Decisión]

### Criterios de entrada

| Criterio | Descripción |
|----------|-------------|
| Confianza alta | Nivel "alto" sostenido por ≥2 revisiones. [Decisión] |
| Estabilidad | Sin cambios sustantivos en ≥60 días. [Decisión] |
| Referencias activas | ≥1 otro documento, decisión o activo lo referencia. [Decisión] |
| Procedencia completa | Cadena de evidencia documentada hasta fuente original. [Decisión] |

### Criterios de salida (degradación)

| Criterio | Destino |
|----------|---------|
| Contradicción por nueva evidencia | → Estado `disputed` (lifecycle), revisión a Capa 2. [Decisión] |
| Validity window expirada sin revalidación | → Candidato a revisión, potencialmente a Capa 2. [Decisión] |
| Reemplazado por conocimiento más completo | → Estado `superseded` (lifecycle). [Decisión] |

### Owner

Fundador (promoción y mantenimiento). [Decisión]

### Ventana de validez típica

90-365 días dependiendo del dominio. Conocimiento de mercado crypto: ~90 días. Conocimiento metodológico: ~365 días. [Decisión]

### Ejemplo

> **(EJEMPLO: Crypto Scalping Core)** "En exchanges centralizados con orderbook visible, las estrategias de scalping en timeframes ≤5m requieren latencia <50ms para ser consistentemente rentables cuando el spread es <0.05%." Validado durante 6 meses de operación real. Confianza: "alto". Referenciado por: decisión de infraestructura (selección de co-location), diseño de estrategia (filtro de pares), evaluación de exchanges. Capa 3 — canónico.

---

## Flujo entre capas

```text
                    ┌──────────────────┐
                    │ EVIDENCIA / DATA │
                    │ (Package 001)    │
                    └────────┬─────────┘
                             │ síntesis + clasificación
                             ▼
                    ┌──────────────────┐
                    │ CAPA 1           │
                    │ Capturado        │◄──── captura directa
                    └────────┬─────────┘      (insight operativo)
                             │ validación + confianza
                             ▼
                    ┌──────────────────┐
                    │ CAPA 2           │
                    │ Validado         │
                    └────────┬─────────┘
                             │ estabilidad + referencias
                             ▼
                    ┌──────────────────┐
                    │ CAPA 3           │
                    │ Canónico         │──── → Asset (Knowledge-to-Value)
                    └──────────────────┘
```

### Atajos permitidos (Principio 6 — Proporcionalidad)

| Atajo | Condición | Justificación |
|-------|-----------|---------------|
| Capa 1 → Capa 3 directo | Conocimiento proveniente de fuente autoritativa con evidencia irrefutable. | Raro pero posible: e.g., documentación oficial de un exchange sobre sus fees. [Decisión] |
| Captura directa a Capa 2 | Insight operativo con evidencia inmediata y repetida. | El fundador observó algo 10+ veces — no necesita pasar por "capturado". [Decisión] |

---

## Relación con el pipeline Knowledge-to-Value

```text
Research → [Capa 1 → Capa 2 → Capa 3] → Asset → Product → Revenue
           └───── Knowledge ──────────┘
```

El conocimiento en Capa 3 (canónico) es el candidato natural para transformación en Asset per el [knowledge-to-asset-handoff.md](./knowledge-to-asset-handoff.md). [Decisión] Conocimiento en Capa 2 puede transformarse en Asset operativo si el caso lo justifica, pero no es el caso típico.

---

## Volumen esperado por capa

| Capa | Volumen estimado (año 1) | Ratio esperado | Epistémico |
|------|--------------------------|----------------|------------|
| Capa 1 — Capturado | 50-100 objetos | 60-70% del total | [Hipótesis] |
| Capa 2 — Validado | 20-40 objetos | 25-30% del total | [Hipótesis] |
| Capa 3 — Canónico | 5-15 objetos | 5-10% del total | [Hipótesis] |

La proporción refleja que la mayoría del conocimiento capturado no amerita inversión de validación completa (Principio 6). Solo el conocimiento que demuestra valor sostenido asciende. [Decisión]

---

## Triggers de complejidad dormiente

El modelo de 3 capas es suficiente para la etapa actual (1 fundador, 1-2 labs activos). Se considerará expandir a 4-5 capas cuando: [Decisión]

| Trigger | Acción |
|---------|--------|
| ≥3 labs activos produciendo conocimiento | Evaluar si "Operational" merece capa separada de "Validated". |
| ≥1 agente IA consumiendo conocimiento autónomamente | Evaluar capa "Machine-Ready" con metadata específica. |
| ≥200 Knowledge Objects en el sistema | Evaluar si la granularidad actual permite descubrimiento eficiente. |

Hasta que se active un trigger, el modelo de 3 capas prevalece. [Decisión]

---

## Cross-references

- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 1 (síntesis), Principio 6 (proporcionalidad)
- [knowledge-boundaries.md](./knowledge-boundaries.md) — Las capas son ortogonales a los boundaries
- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campos por capa
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Estados mapeados a capas
- [Package 001 — Evidence Framework](../package-001-research-methodology/006-evidence-framework.md) — Input a Capa 1
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Pipeline, INV-05

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 14       | 24%        |
| [Hipótesis]   | 3        | 5%         |
| [Decisión]    | 39       | 67%        |
| [Visión]      | 0        | 0%         |

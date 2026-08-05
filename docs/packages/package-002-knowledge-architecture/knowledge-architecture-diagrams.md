# Diagramas de Arquitectura del Conocimiento

## Propósito

Este documento consolida los diagramas de flujo, relaciones y estructura del sistema de conocimiento de LabOS. [Decisión] Todos los diagramas son representaciones textuales que resumen visualmente las decisiones documentadas en los otros documentos del package.

---

## A. Knowledge-to-Value Pipeline

El pipeline central de LabOS muestra cómo el conocimiento se transforma en valor económico. [Hecho]

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE-TO-VALUE PIPELINE                                │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────┐    ┌─────────────┐    ┌────────┐    ┌──────────┐    ┌───────┐│
│  │ Research │───▶│  Knowledge  │───▶│ Assets │───▶│ Products │───▶│Revenue││
│  │          │    │             │    │        │    │          │    │       ││
│  └──────────┘    └─────────────┘    └────────┘    └──────────┘    └───────┘│
│       │                │                │                                    │
│       │                │                │                                    │
│  ┌────▼────┐     ┌────▼────┐     ┌────▼────┐                               │
│  │Evidence │     │Findings │     │Decisions│                                │
│  │Sources  │     │KO Types │     │ADRs     │                                │
│  │Data     │     │6 tipos  │     │         │                                │
│  └─────────┘     └─────────┘     └─────────┘                               │
│                                                                              │
│  ┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐ │
│  │ [FUTURO/DORMIDO] Capability = combinación de Assets + KOs + workflow  │ │
│  │ Activación: ADR del fundador cuando ≥3 Labs activos + evidencia       │ │
│  └─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘ │
│                                                                              │
│  Inputs de soporte:                                                          │
│  • Evidence (Package 001) ─── alimenta ───▶ Knowledge                       │
│  • Findings (Package 001) ── sintetiza ──▶ Knowledge Object                 │
│  • Decisions ◀── informa ── Knowledge                                        │
│  • Labs ── producen/consumen ── Knowledge Objects                            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Notas clave:** [Decisión]
- Research es la ENTRADA del pipeline, no el fin.
- Knowledge es la etapa 2 — el puente entre investigación y activos.
- Capability es DORMIDA — no se activa sin ADR del fundador.
- Revenue es la SALIDA — no el motor.

---

## B. Modelo de Capas del Conocimiento (3 capas)

Organización por madurez y validación. [Decisión]

```text
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  CAPA 3: CONOCIMIENTO CANÓNICO          (90-365 días)           │
│  ═══════════════════════════════════════════════════             │
│  • Gold standard del sistema                                    │
│  • Confianza ALTA sostenida ≥2 revisiones                       │
│  • Sin cambios en ≥60 días                                      │
│  • ≥1 referencia activa desde otro documento                    │
│  • Cadena de procedencia completa                               │
│  • Candidato natural para → Asset                               │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CAPA 2: CONOCIMIENTO VALIDADO          (30-90 días)            │
│  ═══════════════════════════════════════════════════             │
│  • Conocimiento de trabajo                                      │
│  • Confianza explícita (alto/medio) con justificación           │
│  • Fuente verificada y clasificación epistémica                 │
│  • Útil para decisiones operativas                              │
│  • Puede informar pero no es estable a largo plazo              │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CAPA 1: CONOCIMIENTO CAPTURADO         (7-30 días)             │
│  ═══════════════════════════════════════════════════             │
│  • Recién registrado — mínimo viable                            │
│  • Cumple campos obligatorios del KO Contract                   │
│  • Requiere validación para avanzar                             │
│  • Si no transita en 30 días → alerta de huérfano              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ FRONTERA ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

┌─────────────────────────────────────────────────────────────────┐
│  EVIDENCIA / DATOS CRUDOS — NO ES CONOCIMIENTO                  │
│  Gestionados por Package 001 (Evidence Framework, Sources).     │
│  Input al sistema de conocimiento, no parte de él.              │
└─────────────────────────────────────────────────────────────────┘


FLUJO DE TRANSICIONES:

    Evidencia/Datos (Pkg 001)
           │
           │ síntesis + clasificación epistémica
           ▼
    ┌─────────────┐
    │   CAPA 1    │◄──── captura directa (insight operativo)
    │  Capturado  │
    └──────┬──────┘
           │ validación + confianza asignada
           ▼
    ┌─────────────┐
    │   CAPA 2    │
    │  Validado   │
    └──────┬──────┘
           │ estabilidad + referencias activas
           ▼
    ┌─────────────┐         ┌────────────────────────┐
    │   CAPA 3    │────────▶│ HANDOFF → Asset        │
    │  Canónico   │         │ (Knowledge-to-Value)   │
    └─────────────┘         └────────────────────────┘
```

---

## C. Ciclo de Vida del Conocimiento (8 estados)

Todos los estados y transiciones principales del Knowledge Object. [Decisión]

```text
═══════════════════════════════════════════════════════════════════════
                  LIFECYCLE — 8 ESTADOS
═══════════════════════════════════════════════════════════════════════

                         CAMINO RÁPIDO (default, ≤2 min)
                    ┌────────────────────────────────────┐
                    │                                    │
                    ▼                                    │
┌───────────┐            ┌───────────┐            ┌──────────┐
│           │            │           │            │          │
│ CAPTURED  │───────────▶│ VALIDATED │───────────▶│CANONICAL │
│           │            │           │            │          │
└─────┬─────┘            └─────┬─────┘            └────┬─────┘
      │                        │                       │
      │  CAMINO DE REVISIÓN    │                       │
      │  (alto impacto)        │                       │
      │                        │                       │
      │   ┌──────────────┐     │                       │
      └──▶│ UNDER_REVIEW │─────┘                       │
          │  (opcional)  │                             │
          └──────────────┘                             │
                                                       │
      ┌────────────────────────────────────────────────┘
      │ DISPUTA (nueva evidencia contradice)
      │
      │    ┌──────────┐
      └───▶│ DISPUTED │◄─── también desde VALIDATED
           └────┬─────┘
                │
                │ resolución:
                ├──── re-confirmado ──▶ VALIDATED / CANONICAL
                ├──── reemplazado ───▶ SUPERSEDED
                └──── invalidado ────▶ DEPRECATED


      RETIRO:

      ┌────────────┐         ┌──────────┐
      │ SUPERSEDED │────────▶│          │
      │            │  30d    │ ARCHIVED │◄── también desde CAPTURED
      └────────────┘         │          │    (descarte)
                             └────┬─────┘
      ┌────────────┐              │
      │ DEPRECATED │──── 30d ────▶│
      │            │              │
      └────────────┘              │
                                  │ reactivación (excepcional)
                                  └──────────▶ CAPTURED


═══════════════════════════════════════════════════════════════════════
RESUMEN DE TRANSICIONES PRINCIPALES:
═══════════════════════════════════════════════════════════════════════

• Camino rápido:     captured → validated (default, mayoría de KOs)
• Camino revisión:   captured → under_review → validated
• Promoción:         validated → canonical
• Disputa:           validated/canonical → disputed → resolved
• Superación:        disputed → superseded → archived (30d)
• Deprecación:       validated/canonical → deprecated → archived (30d)
• Reactivación:      archived → captured (excepcional, requiere justificación)

═══════════════════════════════════════════════════════════════════════
```

---

## D. Cadena de Procedencia

Trazabilidad completa desde fuente original hasta activo derivado. [Decisión]

```text
═══════════════════════════════════════════════════════════════════════
              CADENA DE PROCEDENCIA (PROVENANCE)
═══════════════════════════════════════════════════════════════════════

┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌───────┐
│  SOURCE  │────▶│ EVIDENCE │────▶│ FINDING  │────▶│    KO    │────▶│ ASSET │
│          │     │          │     │          │     │          │     │       │
└──────────┘     └──────────┘     └──────────┘     └──────────┘     └───────┘
 (Pkg 001)        (Pkg 001)        (Pkg 001)        (Pkg 002)       (Pkg 003+)


RELACIONES MANY-TO-MANY:

  Múltiples fuentes → 1 Knowledge Object:

    Source A ──┐
    Source B ──┼──▶ Evidence ──▶ Finding ──▶ KO-CSC-017
    Source C ──┘

  1 Knowledge Object → Múltiples Assets:

                        ┌──▶ Asset: Playbook de timing
    KO-CSC-017 ─────────┤
                        ├──▶ Asset: Dataset curado
                        │
                        └──▶ Asset: Herramienta de alertas

  Múltiples KOs → 1 Asset:

    KO-CSC-017 ──┐
    KO-CSC-023 ──┼──▶ Asset: "Guía de ventanas óptimas"
    KO-CSC-028 ──┘


ESTADOS DE PROCEDENCIA (5 niveles):

    ┌──────────────────────────────────────────────────────┐
    │ COMPLETE  │ Cadena completa hasta fuente original    │
    │ PARTIAL   │ Parte de la cadena documentada           │
    │ INDIRECT  │ Vía síntesis de terceros                 │
    │UNVERIFIED │ Fuente declarada pero no verificada      │
    │ BROKEN    │ Eslabón roto — fuente inaccesible        │
    └──────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════
```

**(EJEMPLO: Crypto Scalping Core)** KO-CSC-017 tiene procedencia COMPLETE: Binance WebSocket API (source) → 30 días de datos de orderbook (evidence) → análisis estadístico de spread (finding) → KO sintetizado.

---

## E. Flujo Lab-local a Compartido

Cómo el conocimiento privado de un Lab se publica al ecosistema. [Decisión]

```text
═══════════════════════════════════════════════════════════════════════
         FLUJO: LAB-PRIVATE → COMPARTIDO (PUBLISHED/SHARED)
═══════════════════════════════════════════════════════════════════════

┌──────────────────┐
│   KO Lab-Private │    (default para todo KO nuevo)
│   sensitivity:   │
│   PRIVATE        │
└────────┬─────────┘
         │
         │ ¿Cumple elegibilidad?
         │
         ▼
┌──────────────────────────────────────────────────────┐
│              VERIFICACIÓN DE ELEGIBILIDAD             │
│                                                      │
│  ☐ Estado lifecycle: validated o canonical           │
│  ☐ Procedencia: PARTIAL o superior                  │
│  ☐ Confianza: MEDIO o ALTO                          │
│  ☐ Sensibilidad: ¿promovible a PUBLIC?              │
│  ☐ No contiene información competitiva sensible     │
│                                                      │
│  Decisión: Fundador (explícita, documentada)         │
└──────────────────────────────────────────────────────┘
         │
         │ Aprobado → cambiar sensitivity a PUBLIC
         │            + agregar summary ≤300 chars
         ▼
┌──────────────────┐
│  KO Lab-Published│    (Lab mantiene versión canónica)
│  sensitivity:    │
│  PUBLIC          │
└────────┬─────────┘
         │
         │ Registrar en índice compartido
         ▼
┌──────────────────────────────────────────────────────┐
│              ÍNDICE COMPARTIDO (LabOS)                │
│                                                      │
│  • KO referenciable por knowledge_id                 │
│  • Lab de origen acreditado (Originating Lab)        │
│  • Versión canónica permanece en el Lab propietario  │
│  • Consumidores referencian — NO copian              │
└──────────────────────────────────────────────────────┘
         │
         │ Labs consumidores acceden
         ▼
┌──────────────────────────────────────────────────────┐
│              CONSUMO POR OTROS LABS                   │
│                                                      │
│  • Referencia por knowledge_id + versión             │
│  • NO se copia contenido                             │
│  • Derivados pertenecen al Lab consumidor            │
│  • Verificar freshness antes de usar                 │
│  • Reportar problemas al Lab owner                   │
└──────────────────────────────────────────────────────┘

REGLA FUNDAMENTAL: Referencia sin copia. Fuente de verdad única.
El KO NUNCA se duplica — siempre se referencia. [Decisión]

═══════════════════════════════════════════════════════════════════════
```

---

## F. Frontera de Interacción Agente IA

Límites de lo que un agente IA puede y no puede hacer con Knowledge Objects. [Decisión]

```text
═══════════════════════════════════════════════════════════════════════
       FRONTERA DE INTERACCIÓN: AGENTE IA ↔ CONOCIMIENTO
═══════════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────┐
                    │     AGENTE IA                    │
                    │                                  │
                    │  Acciones PERMITIDAS:            │
                    │  ─────────────────────           │
                    │  • READ (acceder KO)             │
                    │  • CITE (referenciar con ID)     │
                    │  • SUMMARIZE (sintetizar)        │
                    │  • COMPARE (evaluar tensiones)   │
                    │  • LINK (proponer relaciones)    │
                    │  • PROPOSE_UPDATE (sugerir)      │
                    │  • PROPOSE_CONFLICT (señalar)    │
                    │  • REQUEST_REVIEW (solicitar)    │
                    │                                  │
                    └──────────────┬───────────────────┘
                                  │
                                  │ PROPONE
                                  ▼
                    ┌─────────────────────────────────┐
                    │     FRONTERA DE APROBACIÓN       │
                    │     ═══════════════════════      │
                    │                                  │
                    │   REQUIERE APROBACIÓN HUMANA:    │
                    │   • Promover a canónico          │
                    │   • Cambiar ownership            │
                    │   • Cambiar sensibilidad         │
                    │   • Resolver disputas            │
                    │   • Eliminar versiones           │
                    │   • Publicar PRIVATE             │
                    │   • Activar Capability           │
                    │   • Handoff → Asset              │
                    │                                  │
                    └──────────────┬───────────────────┘
                                  │
                                  │ APRUEBA (Fundador)
                                  ▼
                    ┌─────────────────────────────────┐
                    │     KO CANÓNICO (PROTEGIDO)      │
                    │     ═══════════════════════      │
                    │                                  │
                    │  • Solo modificable por          │
                    │    Canonical Authority (Fundador) │
                    │  • Agente NO puede modificar     │
                    │    directamente                  │
                    │  • Inmutable sin proceso formal  │
                    │  • Versiones históricas          │
                    │    preservadas                   │
                    │                                  │
                    └─────────────────────────────────┘


CONTENIDO AI-GENERATED:

    Agente produce contenido
           │
           ▼
    Entra en estado CAPTURED (nunca canonical directamente)
           │
           ▼
    OBLIGATORIO: pasar por UNDER_REVIEW
           │
           ▼
    Fundador aprueba → VALIDATED
    Fundador rechaza → ARCHIVED


PRINCIPIO RECTOR:
┌─────────────────────────────────────────────────────────────────┐
│ "No inferir autoridad silenciosamente."                         │
│  El agente NO asume permisos. Expone incertidumbre. Solicita    │
│  revisión. La modificación del conocimiento es prerrogativa     │
│  humana. Si agente y KO canónico se contradicen, el KO         │
│  canónico PREVALECE.                                            │
└─────────────────────────────────────────────────────────────────┘

ESTADO: CONCEPTUAL / FUTURO — se activa cuando un agente consume
KOs autónomamente sin mediación directa del fundador. [Decisión]

═══════════════════════════════════════════════════════════════════════
```

---

## Cross-references

- [knowledge-layers.md](./knowledge-layers.md) — Modelo de 3 capas detallado
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — 8 estados, transiciones, matriz completa
- [knowledge-provenance.md](./knowledge-provenance.md) — Cadena de procedencia, 8 orígenes, 5 estados
- [knowledge-sharing.md](./knowledge-sharing.md) — Reglas de compartición, elegibilidad
- [knowledge-boundaries.md](./knowledge-boundaries.md) — 4 boundary types
- [knowledge-to-asset-handoff.md](./knowledge-to-asset-handoff.md) — Pipeline Knowledge → Asset
- [knowledge-to-capability-handoff.md](./knowledge-to-capability-handoff.md) — Capability dormida
- [ai-agent-knowledge-contract.md](./ai-agent-knowledge-contract.md) — Contrato de agentes IA
- [knowledge-governance.md](./knowledge-governance.md) — Roles, autoridad, cadencias
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Pipeline central

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 2        | 10%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 18       | 90%        |
| [Visión]      | 0        | 0%         |

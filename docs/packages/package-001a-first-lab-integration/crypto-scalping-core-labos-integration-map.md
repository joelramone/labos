# Mapa de Integración con LabOS — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Mapa de integración con LabOS |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Documentar el estado actual y futuro de la integración entre Crypto Scalping Core y LabOS. [Hecho] Establecer qué conexiones existen, cuáles se proponen y cuáles son opcionales.

---

## Estado actual de integración

| Aspecto | Estado |
|---------|--------|
| Dependencia de runtime | **NINGUNA** [Hecho] |
| Shared code/libraries | **NINGUNO** [Hecho] |
| Shared infrastructure | **NINGUNA** [Hecho] |
| Reporting automático a LabOS | **NINGUNO** [Hecho] |
| Knowledge Objects registrados | **NINGUNO** (candidatos identificados, no formalizados) [Hecho] |
| Assets formales registrados | **NINGUNO** (candidatos identificados, no formalizados) [Hecho] |
| Lab Contract firmado | **NO** — pendiente de creación [Hecho] |
| Lab State asignado | `idea` (actual en Portfolio Model) — posiblemente desactualizado [Hecho] |

**Conclusión:** La integración actual es CERO a nivel técnico. [Hecho] La relación es puramente documental (este package).

---

## Integración propuesta (Package 001A)

### Nivel 1: Gobernanza documental [INMEDIATO]

| Componente | Descripción | Estado |
|------------|-------------|--------|
| Lab Contract | Contrato formal de 15 secciones que define el Lab dentro de LabOS | PENDIENTE — este batch prepara la información necesaria [Hecho] |
| Lab State actualizado | Reconsideración de `idea` a `explorando` basado en evidencia | FOUNDER_DECISION requerida [Hecho] |
| Knowledge classification | KOs identificados y registrados formalmente | PENDIENTE — candidatos documentados en este batch [Hecho] |
| Asset identification | Assets candidatos identificados con tipo canónico | PENDIENTE — candidatos documentados en este batch [Hecho] |

### Nivel 2: Clasificación de conocimiento [SIGUIENTE]

| Componente | Descripción | Prerequisito |
|------------|-------------|-------------|
| Formalizar KOs | Crear Knowledge Objects según contrato de Package 002 | Lab Contract aprobado [Decisión] |
| Asignar sensitivity | Clasificar cada KO como lab-private/lab-published/labos-shared | KOs formalizados [Decisión] |
| Registrar en memory | Conectar con sistema de memoria de investigación existente | KOs formalizados [Decisión] |

### Nivel 3: Promoción de assets [FUTURO]

| Componente | Descripción | Prerequisito |
|------------|-------------|-------------|
| Extraer template de journal | Publicar como Asset tipo Template | Desacoplamiento completado [Decisión] |
| Extraer methodology | Documentar pipeline como Framework | KO-5 validado [Decisión] |
| Evaluar herramientas | Decidir qué herramientas extraer | Demanda identificada [Decisión] |

---

## Integración NUNCA requerida

| Aspecto | Razón |
|---------|-------|
| Runtime dependency en LabOS | El Lab debe poder operar independientemente — principio de decoupling [Decisión] |
| LabOS controla ejecución del Lab | LabOS = gobernanza, NO control operacional [Decisión] |
| Shared databases | Cada lab mantiene sus propios datos [Decisión] |
| LabOS aprueba commits | Owner del Lab tiene autonomía de código [Decisión] |
| LabOS modifica código del Lab | Prohibido explícitamente (Decisión 1, Batch 1) [Decisión] |

---

## Integración opcional futura

| Aspecto | Descripción | Trigger de activación |
|---------|-------------|----------------------|
| Reporting a dashboard | El Lab reporta métricas de research a LabOS dashboard | Cuando exista dashboard implementado [Visión] |
| Shared methodology con Atlas Wealth Labs | Compartir pipeline de research entre labs financieros | Cuando ambos labs estén en `explorando`+ [Hipótesis] |
| Knowledge sharing | KOs promovidos a labos-shared para beneficio cross-lab | Cuando KOs alcancen status `canonical` [Visión] |
| Asset promotion | Herramientas extraídas publicadas como Assets compartidos | Cuando se complete desacoplamiento [Visión] |
| Agentes IA consumiendo KOs | Agentes de LabOS accediendo a knowledge del Lab | Cuando se implemente RAG [Visión] |

---

## Principios de integración

1. **Opt-in, no opt-out** — toda integración con LabOS es voluntaria para el Lab. [Decisión]
2. **Sin lock-in** — el Lab puede desintegrarse de LabOS sin perder funcionalidad. [Decisión]
3. **Gobernanza ligera** — proporcional al Lab State (Lab en `explorando` = ~15 min/mes de review). [Decisión]
4. **Value-first** — LabOS provee valor al Lab (clasificación, visibilidad, cross-pollination), no burocracia. [Decisión]

---

## Próximos pasos concretos

| Paso | Descripción | Bloqueado por |
|------|-------------|---------------|
| 1 | Crear Lab Contract con información de Batch 1 + Batch 2 | Aprobación de Batch 2 |
| 2 | Decisión de fundador sobre Lab State (idea → explorando) | Batch 2 review |
| 3 | Formalizar top 2 KOs (KO-4, KO-5 — más alta confianza) | Lab Contract |
| 4 | Evaluar extracción de template de journal (ASSET-3) | KOs formalizados |

---

## Cross-references

- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisión de autonomía y permisos
- [crypto-scalping-core-dependency-map.md](./crypto-scalping-core-dependency-map.md) — Cero dependencias con LabOS
- [crypto-scalping-core-knowledge-object-candidates.md](./crypto-scalping-core-knowledge-object-candidates.md) — KOs a formalizar
- [crypto-scalping-core-asset-candidates.md](./crypto-scalping-core-asset-candidates.md) — Assets a promover
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-09, Lab States

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 14       | 34%        |
| [Hipótesis]   | 2        | 5%         |
| [Decisión]    | 20       | 49%        |
| [Visión]      | 5        | 12%        |

# Reference Lab Eligibility Criteria v1

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Criterios de elegibilidad para Reference Lab |
| **Versión** | 1.0 |
| **Package** | 001A — First Lab Integration |
| **Batch** | 4 — Reference Lab Freeze & Package Closure |
| **Fecha** | 2025-07-30 |

---

## Propósito

Definir los criterios formales para que un Lab integrado sea elegible como Reference Lab de LabOS. [Decisión] Un Reference Lab es un modelo documentado cuyo proceso de integración completo sirve como referencia para Labs futuros.

---

## Criterios obligatorios (14)

Un Lab debe cumplir TODOS los criterios obligatorios para alcanzar status ACTIVE_REFERENCE_LAB. [Decisión]

### Categoría: Proceso completo

| # | Criterio | Descripción | Verificación |
|---|----------|-------------|--------------|
| 1 | Proceso de integración completado end-to-end | El Lab pasó por todas las fases del checklist de integración (Intake → Closure) | Todos los gates de fase satisfechos [Decisión] |
| 2 | Lab Contract aprobado formalmente | El contrato tiene status APPROVED con decisión del fundador documentada | Founder decision record con status APPROVED [Decisión] |
| 3 | Evidence map con ≥90% cobertura verificada | Las afirmaciones del contrato están respaldadas por evidencia trazable | Evidence map document con % de cobertura [Decisión] |
| 4 | Compliance evaluation ejecutada | Se evaluó el contrato contra los frameworks vigentes de LabOS | Compliance document con veredicto global [Decisión] |

### Categoría: Calidad documental

| # | Criterio | Descripción | Verificación |
|---|----------|-------------|--------------|
| 5 | Clasificación epistémica aplicada en todos los documentos | Cada afirmación sustantiva lleva tag [Hecho]/[Hipótesis]/[Decisión]/[Visión] | Revisión manual o tabla epistémica por documento [Decisión] |
| 6 | Cross-references funcionales | Los documentos se referencian entre sí correctamente | Links verificables entre documentos [Decisión] |
| 7 | Sin profitability claims no sustentados | No se afirma rentabilidad sin evidencia (PF > 1.0 documentado) | Auditoría de claims económicos [Decisión] |
| 8 | Sin live-trading claims | No se afirma operación con capital real sin evidencia de transacciones | Auditoría de claims operativos [Decisión] |

### Categoría: Integridad del proceso

| # | Criterio | Descripción | Verificación |
|---|----------|-------------|--------------|
| 9 | Fundador involucrado en decisiones de governance | Las decisiones de estado, scope y aprobación fueron tomadas por el fundador | Founder decisions documents por batch [Decisión] |
| 10 | Autonomía del Lab preservada | El proceso de integración no creó dependencias operativas del Lab hacia LabOS | Sección 14 del contrato + verificación de código [Decisión] |
| 11 | Governance proporcional al contexto | El nivel de governance es apropiado para el número de operadores y revenue | Evaluación contra INV-05 [Decisión] |
| 12 | Remediaciones documentadas (si existen gaps) | Los gaps non-blocking están capturados con owner, target y trigger | Remediation plan document [Decisión] |

### Categoría: Reutilizabilidad

| # | Criterio | Descripción | Verificación |
|---|----------|-------------|--------------|
| 13 | Patrones extraíbles domain-neutral | El proceso produjo al menos 5 patrones aplicables a otros dominios | Patterns document con patrones verificados [Decisión] |
| 14 | Proceso reproducible por terceros | El checklist y documentación son suficientes para que otro agente/persona replique el proceso | Revisión del checklist por completitud [Decisión] |

---

## Descalificadores (11)

Si un Lab presenta CUALQUIERA de estos descalificadores, NO puede ser Reference Lab. [Decisión]

| # | Descalificador | Razón |
|---|---------------|-------|
| 1 | Lab Contract rechazado (REJECT) | No completó el proceso exitosamente |
| 2 | Evidencia fabricada o no verificable | Viola INV-01 (clasificación epistémica) y honestidad intelectual |
| 3 | Profitability claims sin PF > 1.0 documentado | Viola estándares de honestidad |
| 4 | Live-trading claims sin evidencia de transacciones | Viola estándares de honestidad |
| 5 | Proceso de integración parcial (fases incompletas) | No es modelo reproducible |
| 6 | Decisiones de governance no documentadas | No es modelo de trazabilidad |
| 7 | Dependencias creadas entre Lab y LabOS | Viola principio de autonomía |
| 8 | Código del Lab modificado como parte de integración | Viola principio de no-intervención |
| 9 | Plagio de contenido de otro Lab | No es modelo original |
| 10 | State inflation (estado asignado sin evidencia suficiente) | Viola honestidad epistémica |
| 11 | Remediaciones P1 no resueltas al cierre | Deuda blocking no gestionada |

---

## Statuses de Reference Lab

| Status | Significado | Transiciones posibles |
|--------|-------------|----------------------|
| CANDIDATE | Lab identificado como posible Reference Lab, evaluación en curso | → ACTIVE / → DISQUALIFIED |
| ACTIVE_REFERENCE_LAB | Lab registrado como referencia activa, usable por Labs futuros | → DEPRECATED / → ARCHIVED |
| DEPRECATED | Reference Lab sigue disponible pero ya no es recomendado (nueva versión disponible o contexto cambió significativamente) | → ARCHIVED |
| ARCHIVED | Reference Lab preservado pero no activo — solo consulta histórica | (estado terminal) |
| DISQUALIFIED | Lab evaluado y rechazado como Reference Lab | (estado terminal, puede re-aplicar con nueva evidencia) |

### Transiciones

```text
CANDIDATE ──[14 criterios cumplidos]──→ ACTIVE_REFERENCE_LAB
CANDIDATE ──[descalificador encontrado]──→ DISQUALIFIED
ACTIVE_REFERENCE_LAB ──[nueva versión creada / contexto obsoleto]──→ DEPRECATED
ACTIVE_REFERENCE_LAB ──[6 meses sin uso + sin relevancia]──→ ARCHIVED
DEPRECATED ──[decisión de archivado]──→ ARCHIVED
DISQUALIFIED ──[re-evaluación con nueva evidencia]──→ CANDIDATE
```

---

## Evaluación: Crypto Scalping Core

### Criterios obligatorios

| # | Criterio | Cumple | Evidencia |
|---|----------|--------|-----------|
| 1 | Proceso completo end-to-end | ✅ | 4 batches ejecutados, Fase 0-4 completadas [Hecho] |
| 2 | Lab Contract APPROVED | ✅ | FD-B4-01, aprobación incondicional 2025-07-30 [Hecho] |
| 3 | Evidence map ≥90% | ✅ | 98% VERIFIED (evidence map document) [Hecho] |
| 4 | Compliance evaluation | ✅ | 90% COMPLIANT, 10% PARTIALLY (compliance doc) [Hecho] |
| 5 | Clasificación epistémica | ✅ | Aplicada en todos los documentos de Package 001A [Hecho] |
| 6 | Cross-references | ✅ | Verificadas en cada batch review [Hecho] |
| 7 | Sin profitability claims | ✅ | Explícitamente honesto: PF < 1.0 [Hecho] |
| 8 | Sin live-trading claims | ✅ | Excluido del scope (Sección 3 OUT) [Hecho] |
| 9 | Fundador involucrado | ✅ | 6 founder decisions en 3 batches [Hecho] |
| 10 | Autonomía preservada | ✅ | Sección 14: cero dependencies [Hecho] |
| 11 | Governance proporcional | ✅ | SOLO, 15min/mes, INV-05 satisfecha [Hecho] |
| 12 | Remediaciones documentadas | ✅ | 7 ítems P2/P3 en remediation plan [Hecho] |
| 13 | Patrones domain-neutral | ✅ | 10 patrones en lab-integration-patterns-v1.md [Hecho] |
| 14 | Proceso reproducible | ✅ | Checklist de 5 fases documentado [Hecho] |

**Resultado: 14/14 criterios cumplidos** [Hecho]

### Descalificadores

| # | Descalificador | Presente | Verificación |
|---|---------------|----------|--------------|
| 1 | Contract rechazado | ❌ No | APPROVED [Hecho] |
| 2 | Evidencia fabricada | ❌ No | Evidence map 98% verified [Hecho] |
| 3 | Profitability claims | ❌ No | PF < 1.0 documentado [Hecho] |
| 4 | Live-trading claims | ❌ No | Excluido del scope [Hecho] |
| 5 | Proceso parcial | ❌ No | 4 batches completos [Hecho] |
| 6 | Governance no documentada | ❌ No | 6 founder decisions [Hecho] |
| 7 | Dependencies creadas | ❌ No | Cero LabOS imports [Hecho] |
| 8 | Código modificado | ❌ No | Package 001A es documental [Hecho] |
| 9 | Plagio | ❌ No | Contenido original [Hecho] |
| 10 | State inflation | ❌ No | `explorando` con justificación [Hecho] |
| 11 | P1 no resueltos | ❌ No | Solo P2/P3 pendientes [Hecho] |

**Resultado: 0/11 descalificadores presentes** [Hecho]

### Veredicto

**ELEGIBLE PARA ACTIVE_REFERENCE_LAB** [Decisión]

- 14/14 criterios cumplidos
- 0/11 descalificadores
- Status asignado: ACTIVE_REFERENCE_LAB
- Reference Lab ID: LABOS-REF-LAB-0001

---

## Cross-references

- [crypto-scalping-core-reference-lab-record.md](./crypto-scalping-core-reference-lab-record.md) — Registro del Reference Lab
- [lab-integration-patterns-v1.md](./lab-integration-patterns-v1.md) — Patrones extraídos
- [lab-integration-checklist-v1.md](./lab-integration-checklist-v1.md) — Checklist reutilizable
- [crypto-scalping-core-lab-contract.md](./crypto-scalping-core-lab-contract.md) — Contrato aprobado
- [crypto-scalping-core-lab-contract-evidence-map.md](./crypto-scalping-core-lab-contract-evidence-map.md) — Evidence map

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 25       | 45%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 30       | 55%        |
| [Visión]      | 0        | 0%         |

> **Nota:** Equilibrio entre decisiones (definición de criterios y políticas) y hechos (evaluación verificable de CSC contra criterios). Sin hipótesis porque los criterios son binarios y la evaluación es contra evidencia existente.

# Criterios de Validación para Labs

## Propósito

Este documento clasifica los 17 dimensiones del framework de validación en criterios obligatorios, recomendados y dependientes de madurez. [Decisión] Establece el mínimo absoluto para que un Lab pueda tener un Lab Contract formal, proporcional al contexto de fundador solo.

---

## Principio de Proporcionalidad

Los criterios se calibran para un operador único (nivel SOLO de gobernanza). [Decisión] No se requiere burocracia excesiva — se requiere visibilidad mínima. El overhead de validación para un Lab en `idea` no debe exceder 30 minutos de trabajo del fundador. [Decisión]

---

## Criterios Obligatorios (Mínimo Absoluto)

Estos criterios DEBEN cumplirse para que un Lab tenga un Lab Contract activo, independientemente de su estado: [Decisión]

| # | Criterio | Dimensión | Justificación |
|---|----------|-----------|---------------|
| 1 | Owner nombrado | D2 | Sin responsable no hay accountability. [Decisión] |
| 2 | Misión declarada | D3 | Sin propósito no se puede evaluar si el Lab progresa. [Decisión] |
| 3 | Boundary definido | D5 | Sin límites no se sabe qué pertenece al Lab vs. al ecosistema. [Decisión] |
| 4 | Fuente de verdad identificada | D6 | Sin ubicación conocida no se puede acceder a la evidencia. [Decisión] |
| 5 | Propiedad del conocimiento declarada | D15 | Sin ownership claro hay riesgo de conflictos futuros. [Decisión] |
| 6 | Privacidad y sensibilidad evaluada | D5+D15 | Labs con datos sensibles (financieros, personales) requieren clasificación explícita. [Decisión] |
| 7 | ≥1 riesgo identificado | D16 | Todo Lab tiene al menos un riesgo — no documentarlo es negligencia informada. [Decisión] |
| 8 | Ruta de salida viable | D17 | La integración debe ser reversible (principio no-destructivo). [Decisión] |

**Total: 8 criterios obligatorios.** [Decisión]

---

## Criterios Recomendados (Alta Prioridad)

Estos criterios DEBERÍAN cumplirse para una integración robusta, pero su ausencia no bloquea el Lab Contract: [Decisión]

| # | Criterio | Dimensión | Cuándo se vuelve obligatorio |
|---|----------|-----------|------------------------------|
| 1 | Hipótesis de monetización documentada | D11 | Para transicionar de `idea` a `explorando`. [Hecho] |
| 2 | Interfaces documentadas (inputs/outputs) | D7 | Cuando el Lab inicia operación activa. [Decisión] |
| 3 | Independencia de dominio verificada | D8 | Siempre — pero solo es blocker si hay solapamiento real con Lab activo. [Decisión] |

---

## Criterios Dependientes de Madurez

Estos criterios solo aplican a partir de cierto Lab_State: [Decisión]

### Desde `explorando`

| # | Criterio | Dimensión |
|---|----------|-----------|
| 1 | Trabajo recurrente documentado | D9 |
| 2 | ≥1 output producido | D10 |
| 3 | ≥1 investigación o experimento | D12 |
| 4 | ≥1 activo reutilizable (per INV-02) | D14 |

### Desde `validando`

| # | Criterio | Dimensión |
|---|----------|-----------|
| 1 | ≥1 Knowledge Object válido | D13 |
| 2 | Hipótesis de monetización en validación activa | D11 |

### Desde `operando`

| # | Criterio | Dimensión |
|---|----------|-----------|
| 1 | Todos los criterios anteriores VALIDATED | Todas |
| 2 | Revenue documentado con transacción real | Externo al framework (per portfolio model) |

---

## Mínimo para Lab Contract en Estado `idea`

Para un Lab en estado `idea`, el mínimo para crear un Lab Contract válido es: [Decisión]

| Campo | Fuente mínima aceptable |
|-------|------------------------|
| Owner nombrado | Fundador (implícito en nivel SOLO). |
| Misión | 1-3 oraciones marcadas [Hipótesis]. |
| Boundary | Listado mínimo de inclusiones/exclusiones (puede ser propuesto). |
| Fuente de verdad | Ruta o sistema donde vivirá la documentación. |
| Propiedad del conocimiento | Declaración: "Todo conocimiento producido es Lab-Private hasta publicación explícita." |
| Privacidad | Clasificación básica de sensitivity del dominio. |
| ≥1 riesgo | Riesgo más obvio con mitigación básica. |
| Ruta de salida | Confirmación conceptual de autonomía operacional. |

**Overhead estimado para completar este mínimo: 15-30 minutos.** [Hipótesis]

---

## Criterios que NO se exigen

Los siguientes NO son criterios de validación para integración: [Decisión]

- Tener código escrito o funcional. [Decisión]
- Tener usuarios o clientes. [Decisión]
- Tener revenue. [Decisión]
- Tener investigación completada. [Decisión]
- Tener activos productizados. [Decisión]
- Tener tooling específico configurado. [Decisión]

La integración acepta al Lab en su estado actual — no requiere que el Lab esté "listo" para operar. [Decisión]

---

## Relación con Lab Contract Template

El Lab Contract tiene 15 secciones. La validación cubre los prerrequisitos para que esas secciones puedan poblarse con información verificable: [Hecho]

| Sección del Contract | Criterio de validación relacionado |
|---------------------|-----------------------------------|
| 1. Mission | Criterio obligatorio: Misión declarada |
| 2. Scope | Criterio obligatorio: Boundary definido |
| 3. Inputs | Criterio recomendado: Interfaces documentadas |
| 4. Outputs | Criterio recomendado: Interfaces documentadas |
| 9. Private Resources | Criterio obligatorio: Privacidad evaluada |
| 14. Risks | Criterio obligatorio: ≥1 riesgo identificado |
| 15. Review Cycle | Derivado del Lab_State (automático) |

---

## Cross-references

- [lab-validation-framework.md](./lab-validation-framework.md) — 17 dimensiones referenciadas
- [lab-contract-template.md](./lab-contract-template.md) — 15 secciones del contrato
- [lab-integration-framework.md](./lab-integration-framework.md) — Principio incremental y proporcional
- [Package 000 — 012-portfolio-model.md](../package-000-foundation/012-portfolio-model.md) — Transiciones de estado
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-05, INV-09

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 2        | 6%         |
| [Hipótesis]   | 1        | 3%         |
| [Decisión]    | 30       | 91%        |
| [Visión]      | 0        | 0%         |

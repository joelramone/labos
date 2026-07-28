# ADR-0001: Jerarquía de Definición Terminológica

## Metadata

| Campo | Valor |
|-------|-------|
| **ADR ID** | ADR-0001 |
| **Título** | Jerarquía de Definición Terminológica |
| **Estado** | Accepted |
| **Fecha** | 2025-07-22 |
| **Prioridad** | P0 |
| **Autor** | Fundador |

---

## Contexto

Package 001A introduce definiciones (Lab, tipos de activos) que divergen de las establecidas en Package 000 sin referenciarlas. [Hecho] No existe una regla formal que establezca qué glosario prevalece cuando múltiples packages definen el mismo término de forma diferente. [Hecho] El resultado es ambigüedad sobre qué definición usar en packages futuros y en la operación diaria.

La revisión arquitectónica (Package 002A) identificó este problema como hallazgo T-01 (severidad Alta) y T-05 en la architecture-decision-matrix.md. [Hecho] Las invariantes INV-04 y INV-07 abordan este tema pero requieren formalización mediante ADR para ser ejecutables. [Decisión]

---

## Declaración del Problema

Cuando múltiples packages definen el mismo término de forma diferente, no existe un mecanismo formal para determinar cuál definición es canónica. [Hecho] Esto genera:

1. Ambigüedad operativa: al escribir un nuevo documento, no queda claro cuál definición referenciar. [Hecho]
2. Drift terminológico: cada package puede redefinir términos sin restricción, acumulando inconsistencias. [Hecho]
3. Bloqueo de packages futuros: Package 002 y 003 necesitan saber qué es un "Lab" y qué tipos de activos existen sin ambigüedad. [Hecho]

---

## Decisión

Se establece la siguiente jerarquía terminológica: [Decisión]

1. **El glosario en Package 000 README.md es la FUENTE DE VERDAD GLOBAL** para todos los términos de dominio de LabOS. [Decisión]

2. **Packages posteriores pueden EXTENDER un término** (agregar características para su contexto específico) **pero NUNCA REDEFINIRLO** (cambiar su significado base). [Decisión]

3. **Toda extensión DEBE referenciar la definición base explícitamente** con un cross-link al glosario de Package 000. [Decisión]

4. **Si un package necesita modificar una definición base**, debe proponer un nuevo ADR que actualice el glosario de Package 000. La modificación solo se acepta si actualiza la fuente de verdad, no si crea una definición paralela. [Decisión]

5. **Caso específico — "Lab":** [Decisión]
   - **Definición canónica (Package 000):** "Vertical de negocio independiente dentro del portafolio LabOS, con hipótesis de producto propia y estado de madurez definido."
   - **Extensión (Package 001A):** Para el contexto de INTEGRACIÓN FORMAL, Package 001A agrega 4 características: (a) independencia de dominio, (b) preservación de identidad, (c) autonomía operacional, (d) voluntad de integración.
   - **Regla de aplicación:** Un proyecto califica como "Lab" si cumple la definición de Package 000. Cumplir las 4 características de Package 001A es un requisito para INTEGRACIÓN FORMAL al ecosistema, no para ser considerado Lab. [Decisión]

---

## Alternativas Consideradas

### (a) Cada package posee su propio glosario de forma independiente

**Rechazada.** [Decisión] Genera ambigüedad acumulativa. Con 10+ packages planificados, el mismo término podría tener 10 definiciones sin mecanismo de resolución. Viola el principio de single source of truth (INV-04).

### (b) Crear un documento canónico de glosario separado de Package 000

**Rechazada.** [Decisión] El glosario de Package 000 README.md ya cumple esta función y está establecido como fuente de verdad. Crear un documento separado duplicaría la función sin agregar valor, y requeriría sincronización constante.

### (c) Fusionar todas las definiciones en el package más reciente

**Rechazada.** [Decisión] Viola la inmutabilidad de packages completados (INV-10). Además, el package "más reciente" cambia con el tiempo, generando una fuente de verdad móvil.

---

## Consecuencias

### Positivas

- Fuente de verdad única elimina ambigüedad terminológica. [Hecho]
- Los packages futuros tienen un mecanismo claro para referenciar y extender definiciones. [Hecho]
- Se preserva la inmutabilidad de packages completados. [Hecho]

### Negativas

- Actualizar definiciones base requiere un proceso formal (ADR), lo cual agrega overhead. [Hecho]
- El fundador debe revisar que extensiones no contradigan definiciones base. [Hecho]

### Neutras

- Los packages existentes no requieren modificación retroactiva. [Hecho]
- Las referencias futuras solo necesitan ser explícitas con cross-links. [Hecho]

---

## Trade-offs

**Rigidez vs Claridad.** El proceso ADR para actualizar definiciones base agrega fricción operativa. Sin embargo, esta fricción es intencional: previene drift terminológico silencioso que es más costoso de detectar y corregir después del hecho. [Decisión]

Con 1 operador, el overhead de un ADR para cambiar una definición es ~30 minutos. El costo de ambigüedad no resuelta es potencialmente horas de reescritura en packages futuros. [Hipótesis]

---

## Impacto de Migración

- Package 001A: cuando se ejecute, sus requirements deben referenciar las definiciones de Package 000 para los términos base. No se requiere modificación retroactiva del documento de requirements. [Decisión]
- Package 002A: este ADR formaliza lo identificado en la revisión. Sin cambio adicional requerido. [Hecho]
- Operación inmediata: el glosario canónico consolidado se publica en `docs/architecture/glossary.md` como punto de navegación. [Decisión]

---

## Implicaciones Futuras

- Todos los packages futuros DEBEN referenciar el glosario de Package 000 para términos base. [Decisión]
- Package 002 (Knowledge Architecture) necesitará AGREGAR términos al glosario (e.g., "Knowledge" como entidad formal) mediante ADR cuando defina nuevas entidades. [Hipótesis]
- El documento `docs/architecture/glossary.md` se mantiene como índice de navegación que consolida base + extensiones. [Decisión]

---

## Referencias

- [Package 000 README.md — Glosario](../../packages/package-000-foundation/README.md) [Hecho]
- [Package 001A requirements.md — Glossary](../../.kiro/specs/package-001a-first-lab-integration/requirements.md) [Hecho]
- [architecture-decision-matrix.md — Hallazgos T-01, T-05](../packages/package-002a-architecture-review/architecture-decision-matrix.md) [Hecho]
- [remediation-backlog.md — REM-01](../packages/package-002a-architecture-review/remediation-backlog.md) [Hecho]
- [architecture-invariants.md — INV-04, INV-07](../packages/package-002a-architecture-review/architecture-invariants.md) [Hecho]

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 16       | 36%        |
| [Hipótesis]   | 2        | 5%         |
| [Decisión]    | 26       | 59%        |
| [Visión]      | 0        | 0%         |

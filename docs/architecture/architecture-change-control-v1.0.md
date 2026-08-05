# Control de Cambios Arquitectónicos v1.0 — LabOS

## Metadata

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0 |
| **Fecha** | 2025-07-30 |
| **Estado** | READY_FOR_FOUNDER_APPROVAL |
| **Autor** | Principal Architect (LabOS) |
| **Baseline** | LABOS-ARCH-BASELINE-001 |

---

## Propósito

Definir las reglas, procesos y clasificaciones para cambios al Architecture Baseline v1.0. [Decisión] Este documento establece qué tipo de cambios son posibles, qué evidencia requieren, y quién debe aprobarlos.

---

## Clasificación de Cambios

### PATCH (v1.0.x) — Correcciones menores

| Campo | Definición |
|-------|-----------|
| **Qué incluye** | Correcciones de typos, formato, links rotos, actualizaciones de fechas, clarificaciones de redacción que no alteran significado. [Decisión] |
| **Evidencia requerida** | Descripción del cambio en commit message. [Decisión] |
| **ADR requerido** | No. [Decisión] |
| **Aprobación del fundador** | No. [Decisión] |
| **Plan de migración** | No aplica. [Decisión] |
| **Versionado** | Incremento del tercer dígito (1.0.1, 1.0.2...). [Decisión] |
| **Impacto** | Ninguno. No altera semántica ni decisiones. |

**Ejemplos:**
- Corregir "invesitgación" → "investigación"
- Actualizar un cross-reference roto
- Agregar fecha faltante en una tabla

---

### MINOR (v1.x.0) — Extensiones compatibles

| Campo | Definición |
|-------|-----------|
| **Qué incluye** | Nuevos documentos que operan DENTRO del baseline existente, extensiones terminológicas con referencia explícita, nuevos ADRs que simplifican sin contradecir. [Decisión] |
| **Evidencia requerida** | Documento que justifica la extensión + verificación de no-contradicción con baseline existente. [Decisión] |
| **ADR requerido** | Solo si el cambio establece nuevas reglas o restringe comportamiento existente. [Decisión] |
| **Aprobación del fundador** | Sí — al cierre del package que produce la extensión. [Decisión] |
| **Plan de migración** | Declaración de impacto en documentos existentes (puede ser "sin impacto"). [Decisión] |
| **Versionado** | Incremento del segundo dígito (1.1.0, 1.2.0...). [Decisión] |
| **Impacto** | Aditivo. No rompe nada existente pero amplía el corpus. |

**Ejemplos:**
- Package 003 se cierra y produce nuevos documentos CANONICAL
- Se define formalmente la entidad "Asset" extendiendo el glosario
- Se agrega un nuevo patrón de integración a Lab Integration Patterns

---

### MAJOR (vX.0.0) — Cambios incompatibles

| Campo | Definición |
|-------|-----------|
| **Qué incluye** | Modificación de invariantes, cambio del centro arquitectónico, redefinición de términos canónicos, eliminación o fusión de etapas del pipeline, cambio de taxonomía de activos. [Decisión] |
| **Evidencia requerida** | ADR con: contexto del problema, alternativas evaluadas, justificación de por qué el baseline actual es insuficiente, análisis de impacto completo. [Decisión] |
| **ADR requerido** | Obligatorio. [Decisión] |
| **Aprobación del fundador** | Obligatoria y explícita (no implícita). [Decisión] |
| **Plan de migración** | Obligatorio: lista de documentos afectados, cambios requeridos en cada uno, timeline de migración. [Decisión] |
| **Versionado** | Incremento del primer dígito (2.0.0, 3.0.0...). [Decisión] |
| **Impacto** | Potencialmente disruptivo. Puede invalidar packages futuros en diseño. |

**Ejemplos:**
- Eliminar una etapa del Knowledge-to-Value Pipeline
- Redefinir qué significa "Lab" de forma incompatible con la definición actual
- Remover una invariante arquitectónica
- Cambiar la jerarquía terminológica (superseder ADR-0001)

---

## Cambios Prohibidos

Los siguientes cambios están **absolutamente prohibidos** sin importar el proceso seguido: [Decisión]

| # | Prohibición | Razón | Invariante |
|---|-------------|-------|-----------|
| 1 | Modificación retroactiva de packages CLOSED | Destruye trazabilidad | INV-10 |
| 2 | Eliminación de clasificación epistémica | Destruye honestidad intelectual | INV-01 |
| 3 | Creación de definiciones paralelas sin referencia | Genera ambigüedad acumulativa | INV-04, ADR-0001 |
| 4 | Presentar hipótesis como hechos | Viola principio epistémico fundamental | INV-01 |
| 5 | Eliminar el Asset_First_Model sin ADR MAJOR | Es el acelerador del pipeline central | DEC-01 |

**Nota:** "Prohibido" significa que incluso un ADR no puede autorizar estos cambios sin una justificación extraordinaria que demuestre que la prohibición misma es incorrecta. [Decisión]

---

## Proceso de Cambio

### Para PATCH

```text
1. Identificar el error/corrección
2. Aplicar corrección
3. Commit con mensaje descriptivo
4. No requiere actualización del manifiesto
```

### Para MINOR

```text
1. Completar el package que genera la extensión
2. Verificar no-contradicción con baseline
3. Obtener aprobación del fundador (cierre de package)
4. Actualizar architecture-document-register-v1.0.md
5. Actualizar versión del baseline (si aplica)
```

### Para MAJOR

```text
1. Redactar ADR con el problema, alternativas y justificación
2. Incluir análisis de impacto: qué documentos cambian y cómo
3. Incluir plan de migración con timeline
4. Presentar al fundador para aprobación explícita
5. Ejecutar migración según el plan
6. Actualizar architecture-baseline (nueva versión mayor)
7. Actualizar manifiesto y registro de documentos
8. Comunicar impacto a documentos dependientes
```

---

## Corrección de Emergencia

En caso de que se descubra un error factual grave en el baseline (contradicción interna, afirmación falsa presentada como hecho): [Decisión]

1. **Alcance:** Solo errores factuales verificables, no desacuerdos de diseño.
2. **Proceso:** Corrección inmediata + nota en el commit + notificación al fundador.
3. **Clasificación:** PATCH si no altera decisiones; MAJOR si altera una decisión.
4. **Retroactividad:** Permitida SOLO para corregir afirmaciones factuales falsas (e.g., "Package 000 define 15 términos" cuando en realidad define 13).

---

## Política de Supersesión

Cuando un ADR nuevo supercede a uno anterior: [Decisión]

1. El ADR anterior se marca como `SUPERSEDED` con referencia al nuevo ADR.
2. El ADR anterior NO se elimina ni modifica.
3. El nuevo ADR incluye sección "Supersede" con justificación.
4. El glosario y baseline se actualizan para reflejar la nueva realidad.
5. El registro de documentos se actualiza (categoría del viejo → HISTORICAL).

**Ejemplo hipotético:**
- ADR-0015 supercede ADR-0002 porque se necesita un octavo tipo de activo.
- ADR-0002 se marca SUPERSEDED, ADR-0015 es el nuevo GOVERNING.
- Baseline se actualiza a v2.0.0 con el nuevo tipo.

---

## Gobernanza del Proceso

| Aspecto | Regla |
|---------|-------|
| ¿Quién puede proponer cambios? | Cualquier rol (Architect, Fundador, agente IA futuro). [Decisión] |
| ¿Quién aprueba MINOR? | Fundador (implícito en cierre de package). [Decisión] |
| ¿Quién aprueba MAJOR? | Fundador (explícito y documentado). [Decisión] |
| ¿Se puede revertir un cambio aprobado? | Sí, mediante nuevo ADR que justifique la reversión. [Decisión] |
| ¿Cuál es el SLA de revisión? | Sin SLA formal en nivel SOLO. Proporcional a etapa (INV-05). [Decisión] |

---

## Historial de Cambios al Baseline

| Versión | Fecha | Tipo | Descripción | ADR |
|---------|-------|------|-------------|-----|
| v1.0 | 2025-07-30 | INITIAL | Creación del Architecture Baseline | — |

[Hecho] No existen cambios previos porque esta es la versión inicial.

---

## Cross-references

- [architecture-baseline-v1.md](./architecture-baseline-v1.md) — Baseline congelado
- [architecture-baseline-v1.0-manifest.md](./architecture-baseline-v1.0-manifest.md) — Manifiesto
- [architecture-document-register-v1.0.md](./architecture-document-register-v1.0.md) — Registro
- [architecture-invariants.md](../packages/package-002a-architecture-review/architecture-invariants.md) — Invariantes
- [0001-terminology-hierarchy.md](../decisions/0001-terminology-hierarchy.md) — ADR-0001
- [0002-asset-taxonomy-consolidation.md](../decisions/0002-asset-taxonomy-consolidation.md) — ADR-0002

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 1        | 3%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 36       | 97%        |
| [Visión]      | 0        | 0%         |

> **Nota:** Proporción extremadamente alta de decisiones porque un documento de change control es puramente normativo — define reglas, no describe realidades.

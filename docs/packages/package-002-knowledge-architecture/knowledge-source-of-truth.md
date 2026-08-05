# Fuente de Verdad del Conocimiento

## Propósito

Este documento define la ubicación autoritativa para cada tipo de conocimiento dentro del ecosistema LabOS. [Decisión] Operacionaliza el Principio 2 (fuente única, referencia múltiple) estableciendo dónde vive la versión canónica de cada categoría de información.

---

## Principio rector

**Cada pieza de conocimiento tiene exactamente UNA ubicación autoritativa.** [Decisión]

Todas las demás apariciones de esa información son REFERENCIAS a la ubicación autoritativa, nunca copias independientes. Si la referencia y la fuente divergen, la fuente prevalece siempre. [Decisión]

---

## Ubicaciones autoritativas por categoría

| Categoría | Ubicación autoritativa | Owner | Versión canónica |
|----------|----------------------|-------|-------------------|
| KO Lab-local | Registro de conocimiento del Lab (carpeta/archivo dentro del boundary del Lab). | Lab. | Última versión en el registro del Lab. [Decisión] |
| KO compartido (LabOS-Shared) | Índice compartido de conocimiento LabOS. | LabOS. | Última versión en el índice. [Decisión] |
| Decisiones arquitectónicas | `docs/decisions/NNNN-*.md` | LabOS. | El documento ADR vigente. [Hecho] |
| Evidencia de investigación | Artefactos de Package 001 (Source_Register, Evidence records). | Lab que investigó. | Artefactos de la investigación. [Hecho] |
| Hallazgos de investigación (findings) | Documentos de conclusión de Package 001. | Lab que investigó. | Documento de conclusión. [Hecho] |
| Procedimientos operativos | Documentación interna del Lab. | Lab. | Docs operativos del Lab. [Decisión] |
| Conocimiento de producto | Lab que posee el producto. | Lab. | Docs de producto del Lab. [Decisión] |
| Conocimiento de gobernanza | Documentos de arquitectura (`docs/architecture/`). | LabOS. | Documentos de arquitectura. [Hecho] |
| Referencias externas | Fuente externa original (URL, paper, documentación). | Externo (no controlado por LabOS). | La fuente externa. [Hecho] |
| Conocimiento deprecado | Ubicación original, marcado con estado `deprecated`. | Previous owner (congelado). | Congelado en momento de deprecación. [Decisión] |

---

## Reglas de fuente de verdad

### Regla 1: La ubicación canónica gobierna

Si un KO es referenciado desde múltiples documentos, la ubicación canónica (según tabla anterior) es la fuente de verdad. [Decisión] Las referencias son punteros, no versiones alternativas.

### Regla 2: Referencias DEBEN apuntar a la ubicación canónica

Toda referencia a un KO DEBE usar el knowledge_id y apuntar a la ubicación canónica — no a una copia ni a un resumen en otro documento. [Decisión]

### Regla 3: Copias de trabajo NO son fuente de verdad

Si un Lab tiene una nota de trabajo que resume un KO de otro Lab, esa nota NO es fuente de verdad. La fuente es el KO original en su ubicación canónica. [Decisión]

### Regla 4: Fuente inaccesible → flag, no reemplazo

Si la fuente canónica se vuelve inaccesible (URL rota, Lab pausado, etc.): [Decisión]
1. Marcar como BROKEN en procedencia.
2. Buscar fuente alternativa (≤15 minutos de esfuerzo).
3. NO crear una copia de reemplazo en otra ubicación sin transferencia formal de ownership.
4. Si se necesita reubicar: documentar la transferencia per [knowledge-ownership.md](./knowledge-ownership.md).

### Regla 5: Duplicados requieren reconciliación

Si durante la revisión mensual se detecta que la misma información sustantiva aparece en múltiples ubicaciones sin relación de referencia entre ellas, es una violación del Principio 2 que debe resolverse. [Decisión]

---

## Proceso de reconciliación de duplicados

Cuando se detecta que el mismo conocimiento existe en múltiples ubicaciones: [Decisión]

| Paso | Acción | Criterio |
|------|--------|----------|
| 1 | Identificar cuál es canónica | La más antigua, O la más completa, O la que el owner reconoce como su versión. [Decisión] |
| 2 | Convertir la no-canónica en referencia | Reemplazar contenido duplicado por un enlace a la versión canónica. [Decisión] |
| 3 | Preservar adiciones únicas | Si la versión no-canónica contiene información adicional que la canónica no tiene, agregarla como anotación a la canónica. [Decisión] |
| 4 | Documentar la reconciliación | "Duplicado de KO-XXX-NNN reconciliado. Versión canónica en [ubicación]. Adiciones integradas." en ≤1 oración. [Decisión] |

**Overhead estimado:** ~5 minutos por duplicado detectado. Se espera detectar 0-3 duplicados por revisión mensual en año 1. [Hipótesis]

---

## Detección de duplicados

La detección se realiza durante la revisión mensual de conocimiento: [Decisión]

| Señal de posible duplicado | Acción |
|---------------------------|--------|
| Dos KOs con títulos muy similares en dominios solapados. | Verificar si son el mismo claim con diferente redacción. [Decisión] |
| Un documento cita un claim sin referenciar un KO existente que dice lo mismo. | Agregar la referencia o crear el KO si no existía. [Decisión] |
| Mismo dato numérico o afirmación textual en dos ubicaciones sin link. | Reconciliar per el proceso definido arriba. [Decisión] |

---

## Fuente de verdad para conocimiento externo

El conocimiento que proviene de fuentes externas (papers, documentación de APIs, artículos) tiene una particularidad: LabOS no controla la fuente. [Hecho]

| Escenario | Fuente de verdad | Regla |
|-----------|-----------------|-------|
| Paper académico citado | El paper (URL o DOI). | LabOS almacena la SÍNTESIS (KO), no el paper. La síntesis referencia al paper. [Decisión] |
| Documentación de API | La URL de la documentación oficial. | Si la API docs cambia, el KO derivado puede quedar obsoleto — freshness lo detecta. [Hecho] |
| Post de blog o artículo | La URL del artículo. | Si la URL se rompe, procedencia pasa a BROKEN. [Hecho] |
| Conversación o experiencia no documentada | El KO mismo es la fuente (observación de primera mano). | La fuente es la experiencia del fundador — no existe documento externo. [Decisión] |

---

## Ejemplo de resolución de duplicado

**(EJEMPLO: Crypto Scalping Core)**

```text
DETECCIÓN:
- KO-CSC-017: "Spread BTC/USDT se ensancha 40-60% durante 02:00-04:00 UTC"
  (en registro de conocimiento del Lab CSC)
- Research CSC-R-003, Conclusión #2: afirma exactamente lo mismo con
  redacción diferente (en documentos de investigación)

RECONCILIACIÓN:
1. Canónica: KO-CSC-017 (es el Knowledge Object formal con metadata completa).
2. Research CSC-R-003 Conclusión #2 → se convierte en referencia:
   "Ver KO-CSC-017 para la versión validada de este hallazgo."
3. No hay adiciones únicas en la conclusión que no estén en el KO.
4. Nota: "Duplicado entre Research CSC-R-003 Conclusión #2 y KO-CSC-017
   reconciliado. KO-CSC-017 es la fuente canónica."
```

---

## Cross-references

- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 2 (fuente única, referencia múltiple)
- [knowledge-ownership.md](./knowledge-ownership.md) — Transferencia de ownership para reubicación
- [knowledge-provenance.md](./knowledge-provenance.md) — Estado BROKEN cuando fuente es inaccesible
- [knowledge-boundaries.md](./knowledge-boundaries.md) — Lab-Private vs LabOS-Shared como ubicaciones
- [knowledge-freshness.md](./knowledge-freshness.md) — Detección de obsolescencia por fuente externa cambiada
- [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md) — Duplicados como caso de conflicto
- [knowledge-sharing.md](./knowledge-sharing.md) — Índice compartido como fuente de KOs compartidos
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-04 (fuente de verdad única por concepto)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 7        | 18%        |
| [Hipótesis]   | 1        | 3%         |
| [Decisión]    | 31       | 79%        |
| [Visión]      | 0        | 0%         |

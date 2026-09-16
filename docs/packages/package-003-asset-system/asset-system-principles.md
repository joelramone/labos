# Principios del Asset System

## Propósito y autoridad

[Decisión] Este documento establece principios operativos de Package 003 sin redefinir términos upstream. La definición canónica de **Activo** y el Asset_First_Model pertenecen a [Package 000](../package-000-foundation/README.md) y [007-company-model.md](../package-000-foundation/007-company-model.md). La jerarquía terminológica pertenece a [ADR-0001](../../decisions/0001-terminology-hierarchy.md), la taxonomía a [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md) y las invariantes a [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md).

## Principios

### 1. Extender sin redefinir

[Decisión] Package 003 extiende la gobernanza de Activos; no reemplaza la definición base, la taxonomía ni el estado de contenido de Package 000. Toda divergencia requiere el change control correspondiente.

### 2. Candidate no equivale a Canonical

[Decisión] Cumplir el intake mínimo permite tratar un artefacto como Asset_Candidate. Solo las quality gates y una decisión humana explícita pueden convertirlo en Asset_Canónico. No existe promoción automática.

### 3. Fuente de verdad única

[Decisión] Cada Asset gobernado declara una única ubicación canónica. Los índices, copias y referencias no adquieren autoridad paralela. Package 002 conserva la autoridad sobre Knowledge Objects y su lifecycle.

### 4. Governance proporcional al riesgo

[Decisión] El rigor aumenta con exposición, consumo externo, dependencias y Product attachment. El fast path reduce overhead para riesgo bajo, pero no elimina campos o dimensiones obligatorias.

### 5. Trazabilidad antes que burocracia

[Decisión] Toda decisión relevante debe poder vincularse con Requirement, evidencia, owner y fuente; no se crean reviews, metadata o aprobaciones duplicadas cuando una referencia verificable es suficiente.

### 6. Ownership humano y explícito

[Decisión] Asset_Owner y Canonical_Authority son responsabilidades humanas. En contexto SOLO, el Fundador puede ejercer varios roles, pero sus responsabilidades permanecen conceptualmente separadas y auditables.

### 7. Dimensiones separadas

[Decisión] Lifecycle de gobernanza, content_state, sharing_scope, consumption_state, review_required y product_attachment describen aspectos distintos. Ninguno se convierte silenciosamente en otro.

### 8. Preservación histórica

[Decisión] Rechazo, deprecación, archivo, reemplazo y supersesión preservan registro, provenance y relaciones históricas. La gobernanza no borra evidencia para simplificar el estado actual.

### 9. Boundaries explícitos

[Decisión] Package 003 comienza donde existe un artefacto elegible para Candidate y termina en el handoff de Asset. Package 002 gobierna Knowledge; [Package 001A](../package-001a-first-lab-integration/lab-integration-framework.md) gobierna Lab integration; Package 004 permanece no autorizado y gobernará Products cuando corresponda.

### 10. Technology-independent y documentation-first

[Decisión] El Asset System actual es un sistema documental de contratos, reglas y workflows. No selecciona ni implementa database, API, UI, agent, RAG, registry service o automation runtime.

### 11. Operación SOLO sostenible

[Hecho] LabOS opera actualmente con un único Fundador. [Decisión] Intake, evaluación y review deben conservar el mínimo overhead compatible con trazabilidad, usando referencias y actos de aprobación únicos cuando sea posible.

### 12. Evidencia sin sobreafirmación

[Decisión] Potencial, reutilización proyectada y valor esperado se registran como hipótesis; no se presentan como uso demostrado, rentabilidad o autorización operacional. Un caso de Reference Lab valida el framework, no promociona el candidato ni modifica el Lab.

## Límites

[Decisión] Estos principios no implementan lifecycle, qualification, ownership, registry, sharing, Product handoff ni templates; esos contenidos pertenecen a Tasks de waves posteriores. No autorizan promoción de Assets ni cierre de Package 003.

## Checklist de autoridad

| Control | Resultado |
|---|---|
| Definición de Activo referenciada, no redefinida | PASS |
| ADR-0001 y ADR-0002 preservados | PASS |
| Contexto SOLO proporcional | PASS |
| Package 002 mantiene autoridad de Knowledge | PASS |
| Package 001A mantiene autoridad de Lab integration | PASS |
| Product Factory/software fuera de alcance | PASS |

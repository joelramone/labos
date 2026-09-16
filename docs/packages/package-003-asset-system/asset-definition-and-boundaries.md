# Definición Operativa y Boundaries de Assets

## Autoridad y propósito

[Decisión] Este documento aplica la definición canónica de **Activo** de [Package 000](../package-000-foundation/README.md) y establece criterios operativos para distinguir entidades sin redefinir autoridades upstream. [ADR-0001](../../decisions/0001-terminology-hierarchy.md) gobierna la jerarquía terminológica; [Package 002](../package-002-knowledge-architecture/README.md) gobierna Knowledge Objects; [Package 001A](../package-001a-first-lab-integration/lab-integration-framework.md) gobierna Lab integration. Product y Capability no se definen aquí: se preservan como boundaries de entidades cuya autoridad corresponde a packages posteriores o condicionales.

## Matriz de distinción de siete entidades

| Entidad | Definición operativa de una oración | Relación con Asset_Canónico | Criterio observable de exclusión como Asset_Canónico |
|---|---|---|---|
| File | Unidad almacenada en una ubicación o formato identificable, sin que su mera existencia implique significado, reutilización o governance. | Puede contener o representar un artefacto que posteriormente se evalúe. | Si solo puede observarse el archivo pero no los requisitos de Candidate, evaluación, promoción y aprobación, no es Asset_Canónico. |
| Artifact | Resultado identificable de trabajo o investigación con contenido o función, todavía no calificado por el Asset System. | Puede aportar el objeto base para un Asset_Candidate. | Si falta al menos uno de Nombre, Tipo, Descripción, Hipótesis de uso o content_state, permanece Artifact/File; los campos faltantes se nombran explícitamente. |
| Knowledge_Object | Unidad de conocimiento gobernada por Package 002 con lifecycle, provenance, confidence y ownership propios. | Puede ser fuente de uno o varios Assets mediante handoff; permanece como entidad separada. | Si el objeto solo está gobernado como KO y no existe un registro Asset separado que complete el proceso de Package 003, no es Asset_Canónico. |
| Asset_Candidate | Artefacto que satisface el intake requerido y está propuesto para evaluación de reutilización, pero aún no superó promoción canónica. | Es el precursor evaluable de un posible Asset_Canónico. | Si su lifecycle está en CANDIDATE, UNDER_REVIEW, REJECTED o requiere remediación, o carece de aprobación de promoción, no es Asset_Canónico. |
| Asset_Canónico | Activo reutilizable que completó las quality gates aplicables, posee metadata obligatoria y recibió aprobación humana explícita para estado CANONICAL. | Es la entidad gobernada central de Package 003. | Si no existe evidencia verificable de gates, metadata Tier 1+Tier 2 y aprobación del Fundador, la etiqueta “canónico” es inválida. |
| Capability | Boundary conceptual de una capacidad que podría componerse de Assets y otros elementos; su definición formal y activación no pertenecen a Package 003. | Un Asset_Canónico puede contribuir a una futura Capability sin transformarse automáticamente en ella. | Si solo existe un Asset o agrupación de Assets y no existe autoridad futura que defina/active Capability, no es Capability y esa denominación no altera su estado de Asset. |
| Product | Boundary downstream del pipeline cuyo lifecycle y governance pertenecen a Package 004, actualmente no autorizado. | Un Asset_Canónico puede registrar en el futuro un product_attachment o handoff sin transferir automáticamente ownership. | Si no existe una entidad Product gobernada por su autoridad y solo hay un Asset, hipótesis o attachment, no es Product; CANONICAL no significa productizado ni vendible. |

Las definiciones de File y Artifact son extensiones operativas locales para clasificación, no nuevos términos globales. Las filas de Capability y Product delimitan lo que Package 003 no posee; no anticipan su definición formal. [Decisión]

## Candidate frente a Canonical

[Hecho] Package 000 exige cinco campos mínimos para un activo dentro del Asset_First_Model: Nombre, Tipo, Descripción, Hipótesis de uso y Estado de contenido. [Decisión] Requirements v1.3 los incorpora dentro de los ocho campos Tier 1 de Candidate: `nombre`, `tipo`, `descripción`, `hipótesis_de_uso`, `content_state`, `originating_Lab`, `source_of_truth` y `provenance`.

[Decisión] Un Artifact con los cinco campos base puede clasificarse como Asset_Candidate conforme a R1; su registro gobernado debe completar Tier 1 y las condiciones de intake aplicables. Ninguna de esas condiciones lo convierte en Asset_Canónico. La promoción requiere evaluación, quality gates, Tier 2 y aprobación explícita del Fundador.

```text
File → Artifact → Asset_Candidate → evaluación/gates → Asset_Canónico
```

Las flechas expresan elegibilidad conceptual, no promoción automática ni una ejecución autorizada. [Decisión]

## Regla para campos faltantes o inválidos

[Decisión] Cuando un artefacto no satisface el mínimo, la evaluación devuelve cada incumplimiento por nombre, por ejemplo:

```text
Resultado: NOT_AN_ASSET_INTAKE
Campos faltantes: [hipótesis_de_uso, content_state]
Campos inválidos: [tipo: "Módulo"; valores válidos: Documento, Template,
Dataset, Herramienta, Componente, Framework, Playbook]
Clasificación conservada: Artifact
```

No se infieren valores ausentes y no se incluye el artefacto en el catálogo de Assets gobernados hasta satisfacer el intake. [Decisión]

## Boundaries de autoridad

| Boundary | Autoridad upstream/downstream | Package 003 puede | Package 003 no puede |
|---|---|---|---|
| Research → Knowledge | Package 001 y Package 002 | Referenciar provenance recibida | Alterar evidencia o lifecycle del KO |
| Knowledge → Asset | Package 002 entrega; Package 003 recibe | Crear una entidad Candidate separada cuando sea elegible | Consumir, convertir o eliminar el KO original |
| Lab → Asset | Package 001A gobierna integración y boundaries de Lab | Registrar originating_Lab y ownership del Asset | Modificar el Lab o su contrato de integración |
| Asset → Capability | Autoridad futura/condicional | Registrar una relación futura cuando exista autoridad | Activar Capability System o definir su lifecycle |
| Asset → Product | Package 004 futuro | Detenerse en elegibilidad/handoff documental cuando sea autorizado | Crear Product, Product lifecycle, pricing, revenue o customers |

## Validación de cobertura de entidades

| Control | Resultado |
|---|---|
| Entidades requeridas | 7/7 |
| Definición de una oración por entidad | 7/7 |
| Relación con Asset_Canónico | 7/7 |
| Criterio observable de exclusión | 7/7 |
| Candidate distinto de Canonical | PASS |
| Definición canónica de Activo duplicada | NO |
| Package 002/001A authority preservada | PASS |
| Product Factory o Capability System implementado | NO |

## Alcance de este documento

[Decisión] Este documento no define lifecycle detallado, qualification, promotion, ownership, registry ni Product handoff; esas autoridades pertenecen a waves posteriores. No promociona Assets y no selecciona tecnología.

# Requirements Document

## Approval Status

| Campo | Valor |
|-------|-------|
| **Requirements Status** | APPROVED |
| **Requirements Version** | v1.3 |
| **Previous Approved Version** | v1.2 — APPROVED 2026-08-05 |
| **Founder Approval** | APPROVED |
| **Approval Date** | 2026-08-12 |
| **Next Phase** | DESIGN_FINAL_REVIEW |
| **Tasks** | NOT_AUTHORIZED |
| **Implementation** | NOT_AUTHORIZED |
| **Decision Record** | founder-decisions-package-003-requirements-v1.3.md |

---

## Introduction

Package 003 operacionaliza el Asset_First_Model definido en Package 000. Define qué califica como Asset canónico, cómo se distingue de otros artefactos del ecosistema, cómo se propone, evalúa, promueve, versiona, comparte, mide, depreca y archiva. Este package NO implementa software — produce documentación normativa y workflows operativos para la gobernanza de Assets dentro de LabOS bajo contexto SOLO (1 fundador operador).

**Fuentes autoritativas:** Package 000 (Asset_First_Model), ADR-0001 (Jerarquía Terminológica), ADR-0002 (Taxonomía de 7 tipos), Package 001 (Research Methodology), Package 001A (Lab Integration Framework), Package 002 (Knowledge Architecture, knowledge-to-asset-handoff.md), Architecture Baseline v1.0, architecture-change-control-v1.0.md.

---

## Glossary

- **Asset_System**: Conjunto de reglas, workflows, quality gates y metadata que gobierna el ciclo de vida completo de Assets canónicos dentro de LabOS.
- **Asset_Canónico**: Artefacto reutilizable que ha pasado todas las quality gates de promoción y está gobernado por Package 003.
- **Asset_Candidate**: Artefacto propuesto como reutilizable que aún no ha superado las quality gates de promoción.
- **Asset_Registry**: Registro conceptual (no implementado como software) que cataloga todos los Assets canónicos con su metadata obligatoria.
- **Fundador**: Persona que opera LabOS; único stakeholder con capacidad de decisión y ejecución (ref: Package 000 README).
- **Lab**: Vertical de negocio independiente dentro del portafolio LabOS (ref: Package 000 README).
- **Knowledge_Object**: Unidad de conocimiento validado y gobernado por Package 002 (Knowledge Architecture).
- **Asset_First_Model**: Enfoque donde toda investigación >4h acumuladas produce al menos un activo reutilizable documentado (ref: Package 000, 007-company-model.md).
- **Quality_Gate**: Conjunto de criterios verificables que un Asset debe cumplir para avanzar de un estado del ciclo de vida al siguiente.
- **Source_of_Truth**: Ubicación autoritativa y única donde reside la versión canónica de un Asset.
- **Provenance**: Cadena de trazabilidad que conecta un Asset con sus fuentes originales (KOs, investigación, evidencia).
- **Asset_Owner**: Rol responsable de mantener, actualizar y decidir sobre el ciclo de vida de un Asset específico.
- **Canonical_Authority**: Rol con poder de decisión sobre promoción, deprecación y archivo de Assets (Fundador en contexto SOLO).
- **Product_Factory**: Mecanismo futuro (Package 004) para convertir Assets productizados en productos de mercado.
- **sharing_scope**: Atributo ortogonal al lifecycle state que define el nivel de acceso de un Asset. Valores: Lab-Private, Lab-Published, LabOS-Shared, Cross-Lab, Public. No es un estado del ciclo de vida.
- **product_attachment**: Asociación externa entre un Asset canónico y un Product gestionado por Package 004. No es un estado del ciclo de vida del Asset.
- **content_state**: Estado del contenido de un artefacto según Package 000 (borrador, validado, productizado). Dimensión separada del governance lifecycle state de Package 003; no se deriva de `estado_lifecycle` ni determina automáticamente su valor.
- **consumption_state**: Atributo observable que distingue si un Asset no tiene consumidores externos activos (`NO_ACTIVE_EXTERNAL_CONSUMERS`) o tiene al menos uno (`ACTIVE_EXTERNAL_CONSUMERS`). Es independiente de `sharing_scope`: autorización de acceso no equivale a consumo efectivo.
- **review_required**: Flag/atributo ortogonal al lifecycle state del Asset que indica que el Asset_Owner debe revisar el Asset debido a un cambio en una dependencia upstream (KO fuente) o al vencimiento de un trigger programado (ej: Forma B a 90 días). No es un estado del ciclo de vida — el lifecycle state del Asset permanece sin cambios cuando se activa este flag. El Asset_Owner decide la acción resultante.

---

## Requirements

### Requerimiento 1: Modelo de Distinción de Assets

**User Story:** Como fundador, quiero una definición formal que distinga un Asset canónico de otros artefactos del ecosistema (archivos, artefactos, Knowledge Objects, Capabilities, Products), para que solo los artefactos que cumplen criterios de reutilización y gobernanza se gestionen como Assets.

#### Criterios de Aceptación

1. THE Asset_System SHALL definir cada entidad del ecosistema (File, Artifact, Knowledge_Object, Asset_Candidate, Asset_Canónico, Capability, Product) con al menos: nombre, definición de una oración, relación con Asset_Canónico, y criterio observable de exclusión que permita determinar inequívocamente que dicha entidad NO es un Asset_Canónico.
2. IF un artefacto cumple los 5 campos mínimos obligatorios definidos en Package 000 007-company-model.md (Nombre — máximo 80 caracteres, Tipo — uno de los 7 tipos canónicos, Descripción — 1 a 3 oraciones, Hipótesis_de_uso — usuario objetivo más contexto, Estado — uno de: borrador, validado, productizado), THEN THE Asset_System SHALL clasificar ese artefacto como Asset_Candidate.
3. IF un Asset_Candidate supera las quality gates de promoción definidas en el Requerimiento 5, THEN THE Asset_System SHALL promover ese Asset_Candidate a Asset_Canónico.
4. THE Asset_System SHALL establecer que un artefacto producido en un Lab que no cumple los 5 campos mínimos obligatorios permanece clasificado como File o Artifact según corresponda, y no se incluye en el catálogo de Assets gestionados.
5. THE Asset_System SHALL referenciar la definición canónica de Activo del glosario de Package 000 README sin redefinirla, conforme a ADR-0001.
6. IF un artefacto no cumple al menos uno de los 5 campos mínimos obligatorios, THEN THE Asset_System SHALL indicar qué campos faltan o son inválidos, identificando cada campo incumplido por nombre.

---

### Requerimiento 2: Taxonomía Canónica de 7 Tipos

**User Story:** Como fundador, quiero que el Asset System utilice exclusivamente la taxonomía canónica de 7 tipos definida en ADR-0002, para que la clasificación de Assets sea consistente y trazable en todo el ecosistema.

#### Criterios de Aceptación

1. THE Asset_System SHALL clasificar cada Asset usando exactamente uno de los 7 tipos canónicos: Documento, Template, Dataset, Herramienta, Componente, Framework, Playbook. IF un Asset es registrado sin tipo o con un tipo que no pertenece a la lista canónica, THEN THE Asset_System SHALL rechazar el registro e indicar un error que identifique los tipos válidos.
2. THE Asset_System SHALL asignar sharing_scope por defecto según ADR-0002: Documento, Template, Dataset, Herramienta y Framework inician con sharing_scope LabOS-Shared (compartibles por defecto); Componente y Playbook inician con sharing_scope Lab-Private. IF el Lab de origen publica explícitamente un Componente o Playbook mediante el Asset_Sharing_Protocol, THEN THE Asset_System SHALL permitir la compartición de ese activo como excepción al default. [CORRECCIÓN 4: "compartibles por defecto" mapea explícitamente a nivel LabOS-Shared per R9.1]
3. WHEN se propone la adición de un nuevo tipo de activo, THE Asset_System SHALL rechazar el tipo hasta que exista un ADR aprobado que actualice Package 000 (007-company-model.md) conforme al architecture-change-control-v1.0.
4. THE Asset_System SHALL usar los nombres canónicos en español como identificadores primarios en toda interfaz y registro. WHEN se muestra un tipo de activo, THE Asset_System SHALL presentar el nombre canónico en español seguido opcionalmente del equivalente en inglés entre paréntesis con el formato "NombreCanónico (english_equivalent)".
5. THE Asset_System SHALL aplicar el siguiente criterio de distinción entre Herramienta y Componente: si el artefacto opera de forma autónoma se clasifica como Herramienta; si requiere un sistema mayor para funcionar se clasifica como Componente.

---

### Requerimiento 3: Ciclo de Vida del Asset

**User Story:** Como fundador, quiero un ciclo de vida canónico con estados, transiciones y criterios explícitos, para que cada Asset tenga un camino claro desde su identificación hasta su archivo o rechazo.

#### Criterios de Aceptación

1. THE Asset_System SHALL definir los siguientes estados del ciclo de vida de gobernanza: CANDIDATE, UNDER_REVIEW, VALIDATED, CANONICAL, DEPRECATED, ARCHIVED, REJECTED. **Nota [CORRECCIONES 6, 9]:** El sharing_scope (Lab-Private, Lab-Published, LabOS-Shared, Cross-Lab, Public), el product_attachment y el review_required son atributos ortogonales al lifecycle state — no son estados del ciclo de vida. Un Asset puede ser CANONICAL y Lab-Private simultáneamente. Un Asset puede estar CANONICAL sin product_attachment. El flag review_required puede activarse sobre un Asset en cualquier lifecycle state sin modificarlo. El lifecycle state gobierna la madurez de gobernanza; el sharing_scope gobierna el acceso; el product_attachment registra una asociación externa; el review_required señaliza que el Asset_Owner debe revisar el Asset.
2. WHEN un artefacto cumple los 5 campos mínimos obligatorios (nombre, tipo, descripción, hipótesis de uso, estado) y tiene al menos una señal documentada de potencial de reutilización (referencia explícita a un segundo lab, dominio o caso de uso distinto al original donde el artefacto podría aplicarse), THE Asset_System SHALL permitir su registro como CANDIDATE.
3. WHEN un Asset_Candidate es sometido a evaluación por el Fundador, THE Asset_System SHALL transicionar su estado a UNDER_REVIEW.
4. WHEN un Asset en UNDER_REVIEW cumple todas las quality gates de validación (completitud de los 5 campos obligatorios verificada, hipótesis de uso con al menos un escenario concreto descrito, y ausencia de duplicación con un Asset existente en estado VALIDATED o CANONICAL), THE Asset_System SHALL permitir su transición a VALIDATED.
5. WHEN un Asset VALIDATED recibe aprobación explícita del Fundador, THE Asset_System SHALL transicionar su estado a CANONICAL.
6. WHEN un Asset CANONICAL cumple al menos una de las siguientes condiciones documentadas por el Fundador: (a) existe un Asset CANONICAL que cubre el mismo caso de uso, (b) no ha sido referenciado ni consumido por ningún lab en los últimos 90 días, o (c) requiere actualización cuyo esfuerzo estimado supera 8 horas sin demanda activa que lo justifique, THEN THE Asset_System SHALL permitir su transición a DEPRECATED con justificación documentada que identifique la condición aplicable.
7. WHEN un Asset DEPRECATED ha permanecido sin consumidores activos (ningún lab lo referencia, utiliza o extiende) durante al menos 30 días, THE Asset_System SHALL permitir su transición a ARCHIVED.
8. WHEN un Asset_Candidate o un Asset en UNDER_REVIEW no cumple las quality gates y el Fundador determina que no es remediable, THE Asset_System SHALL transicionar su estado a REJECTED con motivo documentado que indique las quality gates no superadas y la razón de irremediabilidad.
9. THE Asset_System SHALL preservar el registro de Assets REJECTED y ARCHIVED como referencia histórica sin eliminarlos del registro.
10. WHEN un Asset cumple los criterios de bajo riesgo (sharing_scope Lab-Private, sin exposición externa a consumidores fuera del lab de origen, y sin product_attachment activo), THE Asset_System SHALL permitir la transición CANDIDATE → VALIDATED → CANONICAL mediante evaluación simplificada del Fundador consistente en una aprobación única que cubra las quality gates y la aprobación final en un solo acto documentado.
11. IF se intenta una transición de estado no definida en los criterios 2-8 y 10 (transiciones válidas: CANDIDATE→UNDER_REVIEW, CANDIDATE→REJECTED, UNDER_REVIEW→VALIDATED, UNDER_REVIEW→REJECTED, VALIDATED→CANONICAL, CANONICAL→DEPRECATED, DEPRECATED→ARCHIVED, y el fast path CANDIDATE→VALIDATED→CANONICAL), THEN THE Asset_System SHALL rechazar la transición e indicar que la transición solicitada no es válida para el estado actual del Asset.
12. THE Asset_System SHALL permitir únicamente transiciones hacia adelante en el ciclo de vida; un Asset en estado DEPRECATED, ARCHIVED o REJECTED no podrá retornar a un estado anterior sin crear un nuevo registro de Asset como CANDIDATE con referencia al Asset original.

---

### Requerimiento 4: Dimensiones de Calificación del Asset

**User Story:** Como fundador, quiero criterios explícitos para evaluar si un artefacto merece ser Asset, para que la decisión de promoción se base en evidencia y no en intuición.

#### Criterios de Aceptación

1. THE Asset_System SHALL definir las siguientes dimensiones de calificación obligatorias para todo Asset_Candidate, donde cada dimensión se evalúa como SATISFECHA o NO_SATISFECHA según su criterio de aceptación específico: (a) evidencia de reutilización — acepta CUALQUIERA de las dos formas: **Forma A (DEMONSTRATED)** al menos 1 uso documentado fuera del contexto de origen; o **Forma B (DESIGNED-FOR-REUSE)** una declaración escrita de diseño-para-reutilización que identifique ≥1 Lab o dominio destino específico y ≥1 escenario de uso concreto. Cuando aplica Forma B, se requiere un review trigger automático a los 90 días desde la promoción a CANONICAL. [CORRECCIÓN 2: separa evidencia demostrada de declaración de diseño-para-reuso, resolviendo el gap para first-time assets]; (b) calidad mínima documentable — el artefacto cumple los 5 campos mínimos de 007-company-model.md y posee al menos 1 validación registrada por el owner; (c) provenance trazable — origen identificado con referencia a la investigación, Lab o experimento que lo produjo; (d) ownership asignado — un owner nombrado explícitamente responsable de mantenimiento y decisiones sobre el artefacto; (e) source of truth identificado — una ubicación canónica única declarada dentro del repositorio.
2. THE Asset_System SHALL definir las siguientes dimensiones de calificación recomendadas, evaluadas de forma informativa sin bloquear promoción: repetibilidad, mantenibilidad, documentación de uso, estabilidad de dependencias, valor medible y aplicabilidad cross-Lab. Cada dimensión recomendada se registra como PRESENTE o AUSENTE en la evaluación del Asset_Candidate.
3. THE Asset_System SHALL definir las siguientes dimensiones dependientes de madurez, aplicables únicamente cuando el owner declara explícitamente intención de compartición cross-Lab o product_attachment: sensibilidad y licensing, relevancia de Product, costo operativo y diferenciación estratégica.
4. IF un Asset_Candidate tiene al menos 1 dimensión obligatoria con estado NO_SATISFECHA, THEN THE Asset_System SHALL asignar clasificación NEEDS_REMEDIATION e impedir transición a UNDER_REVIEW hasta que todas las dimensiones obligatorias alcancen estado SATISFECHA.
5. WHEN el owner completa la evaluación de todas las dimensiones obligatorias con estado SATISFECHA, THE Asset_System SHALL registrar la fecha de evaluación y el resultado consolidado, habilitando la transición del Asset_Candidate a UNDER_REVIEW.
6. WHEN un Asset CANONICAL promovido con Forma B de evidencia de reutilización alcanza los 90 días desde su promoción, THE Asset_System SHALL generar un review trigger con motivo "evidencia de reutilización Forma B — review a 90 días" para que el Asset_Owner documente evidencia real de uso (Forma A) o escale la evaluación de deprecación.

---

### Requerimiento 5: Quality Gates de Promoción

**User Story:** Como fundador, quiero quality gates progresivas con rigor proporcional al nivel de exposición del Asset, para que Assets internos de bajo riesgo no sufran burocracia innecesaria mientras que Assets compartidos o vinculados a Products tengan gobernanza adecuada.

#### Criterios de Aceptación

1. THE Asset_System SHALL definir quality gates para las siguientes transiciones: CANDIDATE → UNDER_REVIEW, UNDER_REVIEW → VALIDATED, VALIDATED → CANONICAL, CANONICAL → sharing_scope cross-Lab o superior, CANONICAL → product_attachment.
2. WHEN un Asset aspira a sharing_scope Cross-Lab o Public, THE Asset_System SHALL requerir quality gates adicionales: documentación de uso que incluya propósito, instrucciones de aplicación y al menos un ejemplo concreto; licencia explícita seleccionada de las opciones definidas por LabOS; evaluación de sensibilidad con clasificación (pública, interna, confidencial); y confirmación de mantenibilidad mediante identificación de un responsable de mantenimiento y frecuencia de revisión comprometida.
3. WHEN un Asset se vincula a un Product (product_attachment), THE Asset_System SHALL requerir: estabilidad demostrada definida como ausencia de cambios estructurales (MAJOR según architecture-change-control) durante al menos un ciclo de revisión completo (mínimo 30 días), ownership explícito con identidad del responsable registrada, plan de mantenimiento con frecuencia de actualización y criterios de deprecación, y evaluación de impacto ante deprecación que identifique los Products y Labs dependientes.
4. THE Asset_System SHALL clasificar cada Asset en exactamente uno de 3 niveles de exposición usando `sharing_scope`, `consumption_state`, dependencias externas y `product_attachment`: nivel 1 (sin consumidores externos activos, sin dependencias de otros Labs, sin product_attachment y sharing_scope distinto de Public; incluye Assets Lab-Private y Assets autorizados como LabOS-Shared que todavía no tienen consumo externo efectivo), nivel 2 (al menos un consumidor externo activo o una dependencia de otro Lab, con sharing_scope Lab-Published, LabOS-Shared o Cross-Lab, sin product_attachment y no Public), nivel 3 (product_attachment activo o sharing_scope Public). THE Asset_System SHALL registrar `sharing_scope` y `consumption_state` por separado y SHALL aplicar quality gates de rigor creciente. La autorización de sharing_scope LabOS-Shared no constituye por sí sola consumo efectivo ni eleva automáticamente el Asset a nivel 2; los gates requeridos para autorizar el scope se cumplen antes del cambio de scope, independientemente del nivel de exposición operativo resultante.
5. THE Asset_System SHALL preservar un fast path para Assets clasificados como nivel 1 de exposición. El fast path SHALL verificar las 5 dimensiones obligatorias de R4 en el mismo acto ligero de aprobación; reduce profundidad de evidencia, documentación y overhead, pero no elimina ni sustituye ninguna dimensión obligatoria. Requiere: los 5 campos mínimos completos, una referencia documentada de uso o aplicación dentro del Lab de origen, evidencia de reutilización Forma A o Forma B conforme a R4.1, las demás cuatro dimensiones obligatorias SATISFECHAS y aprobación del Fundador.
6. IF un Asset no cumple los criterios de un quality gate durante una evaluación de promoción, THEN THE Asset_System SHALL rechazar la transición, indicar cuáles criterios específicos no fueron satisfechos, y mantener el Asset en su estado actual sin pérdida de metadata registrada.
7. IF un Asset clasificado como nivel 1 adquiere una dependencia cross-Lab o se vincula a un Product, THEN THE Asset_System SHALL reclasificar automáticamente el Asset al nivel de exposición correspondiente y SHALL requerir el cumplimiento de los quality gates del nuevo nivel antes de permitir la operación.

---

### Requerimiento 6: Ownership y Autoridad

**User Story:** Como fundador, quiero un modelo claro de ownership y autoridad sobre Assets que distinga entre creador, propietario y autoridad canónica, para que las responsabilidades de mantenimiento y decisión estén siempre asignadas.

#### Criterios de Aceptación

1. THE Asset_System SHALL definir los siguientes roles respecto a un Asset: creator (quien lo produce), originating_Lab (Lab donde se origina), Asset_Owner (responsable de mantenimiento y lifecycle), maintainer (ejecutor de actualizaciones), reviewer (evaluador de quality gates), Canonical_Authority (decisor de promoción y deprecación) y consumer (usuario del Asset).
2. THE Asset_System SHALL establecer que ownership y authorship son conceptos distintos: el creator de un Asset no es necesariamente su Asset_Owner, y un Asset SHALL registrar ambos roles de forma independiente.
3. THE Asset_System SHALL establecer que ownership y Canonical_Authority son conceptos distintos: el Asset_Owner gestiona el Asset pero la Canonical_Authority decide sobre promoción y deprecación, y un Asset SHALL registrar ambos roles de forma independiente.
4. IF un agente de IA es asignado como Asset_Owner o Canonical_Authority, THEN THE Asset_System SHALL rechazar la asignación e indicar que dichos roles requieren un humano (Fundador en contexto SOLO) como responsable final, permitiendo únicamente que el agente de IA ocupe roles de maintainer o reviewer bajo supervisión del Asset_Owner humano.
5. THE Asset_System SHALL establecer que inputs externos con licencia propia (licencia definida fuera de LabOS por un tercero) permanecen externos y no se reclasifican como Assets canónicos de LabOS, registrándose únicamente como referencias con su licencia original documentada.
6. WHEN un Asset se comparte fuera de su Lab de origen, THE Asset_System SHALL requerir autorización explícita del Asset_Owner y del originating_Lab, donde autorización explícita consiste en un registro documentado que incluye: identidad del autorizante, fecha, Asset identificado, Lab destino, y alcance de uso permitido.
7. WHILE LabOS opera en contexto SOLO, THE Asset_System SHALL permitir que el Fundador ocupe simultáneamente los roles de creator, Asset_Owner, maintainer, reviewer y Canonical_Authority. [CORRECCIÓN 10: se agrega maintainer a la lista de roles que el Fundador puede ocupar en contexto SOLO, cerrando el gap donde el único operador es también el único mantenedor]
8. WHEN el Asset_Owner de un Asset necesita cambiar, THE Asset_System SHALL requerir un registro de transferencia que incluya: Asset identificado, Asset_Owner saliente, Asset_Owner entrante, fecha de transferencia, y confirmación explícita del nuevo Asset_Owner aceptando la responsabilidad de mantenimiento y lifecycle.
9. THE Asset_System SHALL establecer que la Canonical_Authority del originating_Lab retiene autoridad canónica sobre un Asset después de cualquier cambio de sharing_scope, incluyendo Cross-Lab y Public. Un cambio de Canonical_Authority hacia co-governance o autoridad compartida con otro Lab requiere un ADR formal que establezca el nuevo modelo de gobernanza conforme al architecture-change-control-v1.0. [CORRECCIÓN 12: define explícitamente quién tiene Canonical_Authority post cross-Lab promotion y prepara el escalamiento futuro bajo change control]

---

### Requerimiento 7: Provenance y Source of Truth

**User Story:** Como fundador, quiero que cada Asset canónico tenga trazabilidad completa a sus orígenes y una ubicación autoritativa única, para que la procedencia sea auditable y no existan versiones ambiguas.

#### Criterios de Aceptación

1. THE Asset_System SHALL requerir que todo Asset_Canónico documente su provenance con los siguientes campos obligatorios: KO(s) fuente (al menos un knowledge_id válido), investigación de origen (research_id), Lab de origen, fecha de creación (formato ISO 8601) y autor (identificador del fundador o contribuidor responsable); un Asset_Canónico con cualquiera de estos campos vacío o ausente no se considera válido.
2. THE Asset_System SHALL requerir que todo Asset_Canónico tenga exactamente un source_of_truth identificado: la ubicación física (path, repositorio, sistema) donde reside la versión autoritativa.
3. THE Asset_System SHALL mantener un registro de versión independiente por cada Asset_Canónico que incluya como mínimo: número de versión (formato MAJOR.MINOR.PATCH), fecha del cambio, descripción del cambio (máximo 500 caracteres) y autor del cambio; el historial de Git por sí solo NO constituye versionado completo de Asset.
4. THE Asset_System SHALL preservar la cadena de trazabilidad: Asset → Knowledge_Object(s) → Research → Evidence → Source, conforme al modelo de provenance de Package 002, de modo que cada eslabón de la cadena contenga una referencia verificable (ID o path) al eslabón anterior.
5. IF un Asset pierde su referencia a source_of_truth (path inválido, repositorio eliminado, recurso inaccesible), THEN THE Asset_System SHALL marcar el Asset como NEEDS_REMEDIATION hasta que se restaure una referencia válida y verificable.
6. IF un Asset_Canónico es creado a partir de fuentes externas que no poseen un Knowledge_Object registrado, THEN THE Asset_System SHALL requerir que se documente la fuente de origen directa (URL, referencia bibliográfica o identificador externo) en sustitución del knowledge_id, manteniendo la trazabilidad mínima. IF un Asset se origina en investigación propia no formalizada como Knowledge_Object en Package 002, THE Asset_System SHALL aceptar el research_id (identificador de la investigación de origen de Package 001) como referencia de provenance en lugar del knowledge_id, documentando el motivo de la ausencia de KO en el campo de provenance. [CORRECCIÓN 11: cubre el path Research → Asset directo documentado en canonical-domain-map.md, sin KO ni fuente externa]

---

### Requerimiento 8: Versionado de Assets

**User Story:** Como fundador, quiero un esquema de versionado que distinga entre actualizaciones menores, cambios significativos y reemplazos completos, para que los consumidores de un Asset entiendan el impacto de cada cambio.

#### Criterios de Aceptación

1. THE Asset_System SHALL aplicar versionado semántico (MAJOR.MINOR.PATCH) a cada Asset_Canónico.
2. THE Asset_System SHALL definir: PATCH como correcciones que no alteran funcionalidad ni interfaz; MINOR como adiciones compatibles que no rompen uso existente; MAJOR como cambios incompatibles que requieren adaptación por parte de consumidores.
3. WHEN un cambio MAJOR reemplaza completamente la funcionalidad de la versión anterior de modo que ningún consumidor debería seguir utilizándola, THE Asset_System SHALL permitir marcar la versión anterior como SUPERSEDED con referencia al identificador del Asset sucesor.
4. IF un cambio propuesto altera el propósito declarado del Asset O cambia la audiencia objetivo definida en sus metadatos respecto a la versión 1.0.0, THEN THE Asset_System SHALL requerir la creación de un nuevo Asset independiente en lugar de una nueva versión MAJOR.
5. THE Asset_System SHALL mantener un registro histórico inmutable de versiones incluyendo: número de versión, fecha de creación, descripción del cambio (entre 10 y 500 caracteres) y autor del cambio; las entradas existentes no podrán ser eliminadas ni modificadas una vez registradas.
6. WHEN un Asset es promovido al estado CANONICAL, THE Asset_System SHALL asignar la versión 1.0.0 como versión inicial.
7. THE Asset_System SHALL distinguir los siguientes tres casos de evolución de un Asset, preservando el Asset original sin cambios en todos ellos [CORRECCIÓN 8]: (a) **Nueva versión** — mismo propósito, misma audiencia, mismo asset_id, número de versión incrementado (MAJOR, MINOR o PATCH); (b) **Asset derivado** — Asset modificado desde un Asset compartido para un contexto específico, registrado como nuevo Asset con nuevo asset_id y provenance que referencia al Asset original (identificador original + versión base + descripción de modificaciones); (c) **Fork** — copia independiente a partir de la cual se inicia desarrollo nuevo e independiente, registrado como nuevo Asset con nuevo asset_id y provenance que referencia al Asset original. El Asset original permanece CANONICAL, versionado e inmutable en todos los casos.

---

### Requerimiento 9: Compartición y Reutilización

**User Story:** Como fundador, quiero reglas claras de compartición que definan quién puede usar un Asset, bajo qué condiciones y con qué obligaciones, para que la reutilización sea gobernada y no genere conflictos de propiedad o mantenimiento.

#### Criterios de Aceptación

1. THE Asset_System SHALL definir los siguientes niveles de sharing_scope alineados con las boundaries del ecosistema: Lab-Private (solo el Lab de origen), Lab-Published (publicado voluntariamente por el Lab, otros Labs pueden referenciar en modo lectura), LabOS-Shared (infraestructura transversal mantenida por LabOS, accesible por todos los Labs), Cross-Lab (co-creado entre Labs participantes con acuerdo de co-propiedad documentado), y Public (accesible externamente fuera del ecosistema LabOS).
2. THE Asset_System SHALL aplicar los defaults de ADR-0002: Documento, Template, Dataset, Herramienta y Framework inician con sharing_scope LabOS-Shared; Componente y Playbook inician con sharing_scope Lab-Private.
3. WHEN un Asset con sharing_scope Lab-Private se promueve a sharing_scope LabOS-Shared, THE Asset_System SHALL requerir: documentación de uso que no presuponga conocimiento del Lab de origen (conteniendo al menos: propósito, instrucciones de uso, dependencias, y ejemplo de aplicación), autorización explícita del Asset_Owner, y evaluación de mantenibilidad que verifique: existencia de un responsable de mantenimiento asignado, frecuencia de actualización estimada, y ausencia de dependencias a recursos Lab-Private.
4. WHEN un Asset se comparte (sharing_scope Lab-Published o superior), THE Asset_System SHALL establecer que la compartición es basada en referencia (los consumidores referencian el source_of_truth, no crean copias independientes) y que cualquier copia local detectada se clasifica como Asset derivado sujeto al criterio 7.
5. THE Asset_System SHALL definir obligaciones del consumidor: atribución al Asset de origen incluyendo identificador y Lab propietario, verificación documentada de compatibilidad con su contexto (registrando al menos: versión referenciada y confirmación de prueba en contexto propio), y notificación al Asset_Owner de defectos encontrados dentro de los 7 días calendario siguientes a su detección.
6. THE Asset_System SHALL definir obligaciones del Asset_Owner hacia consumidores: notificación de cambios MAJOR con un mínimo de 14 días calendario de anticipación, período de gracia de 30 días calendario antes de completar una deprecación, y documentación de migración cuando el Asset tiene 1 o más consumidores activos registrados.
7. WHEN un consumidor modifica un Asset compartido para su contexto, THE Asset_System SHALL clasificar el resultado como Asset derivado con provenance que referencia al Asset original incluyendo: identificador del Asset original, versión base utilizada, y descripción de las modificaciones realizadas.
8. IF un Asset compartido se depreca y tiene al menos 1 consumidor que lo haya referenciado en los últimos 90 días calendario, THEN THE Asset_System SHALL requerir plan de migración o alternativa documentada antes de completar la deprecación.
9. IF surge un conflicto de propiedad o mantenimiento sobre un Asset compartido entre el Asset_Owner y uno o más consumidores, THEN THE Asset_System SHALL requerir que el Fundador registre una decisión documentada con: partes involucradas, naturaleza del conflicto, resolución adoptada, y fecha de resolución, dentro de los 14 días calendario siguientes a la identificación del conflicto.

---

### Requerimiento 10: Modelo de Valor del Asset

**User Story:** Como fundador, quiero dimensiones explícitas para evaluar el valor de un Asset sin métricas de falsa precisión, para que la priorización de mantenimiento y la decisión de deprecación se basen en valor real demostrado.

#### Criterios de Aceptación

1. THE Asset_System SHALL definir las siguientes dimensiones de valor: frecuencia de reutilización, tiempo ahorrado por uso, mejora de calidad habilitada, reducción de riesgo, adopción cross-Lab, contribución a Product, valor de aprendizaje y costo de mantenimiento, especificando para cada dimensión una pregunta de evaluación respondible con evidencia observable (dato de uso, registro, testimonio documentado o referencia verificable).
2. THE Asset_System SHALL clasificar el valor de cada Asset como: DEMOSTRADO (al menos 1 registro documentado de uso real por alguien distinto al creador, o 1 referencia verificable de aplicación en un contexto concreto con fecha), PROYECTADO (hipótesis escrita que identifica al menos 1 usuario potencial específico, 1 escenario de uso concreto, y 1 razón por la cual se espera demanda), o INDETERMINADO (no cumple los criterios de DEMOSTRADO ni PROYECTADO).
3. THE Asset_System SHALL usar la clasificación de valor como criterio principal para decisiones de mantenimiento y priorización, donde los Assets con valor DEMOSTRADO reciben prioridad sobre PROYECTADO, y los Assets con valor PROYECTADO reciben prioridad sobre INDETERMINADO.
4. IF un Asset permanece en estado INDETERMINADO por más de 90 días sin que se documente evidencia que permita reclasificarlo a PROYECTADO o DEMOSTRADO, THEN the Asset_System SHALL requerir una decisión explícita del Fundador: deprecar el Asset con justificación documentada, o asignar una acción concreta con fecha límite (máximo 30 días) para obtener evidencia de valor.
5. THE Asset_System SHALL prohibir el uso de scores numéricos compuestos, rankings cuantitativos ponderados o índices calculados como mecanismo de evaluación de valor, limitando la evaluación a clasificación por dimensión (alto/medio/bajo/no-aplica respaldado por evidencia citada) y clasificación global (DEMOSTRADO/PROYECTADO/INDETERMINADO).
6. WHEN el valor de un Asset es evaluado, THEN the Asset_System SHALL requerir que la evaluación documente: fecha de evaluación, clasificación asignada, evidencia que sustenta la clasificación (al menos 1 referencia concreta), y dimensiones en las que el Asset aporta valor.

---

### Requerimiento 11: Métricas del Asset System

**User Story:** Como fundador, quiero métricas operativas proporcionales que midan la salud del sistema de Assets sin vanity metrics, para que pueda evaluar si el Asset System está generando valor real.

#### Criterios de Aceptación

1. THE Asset_System SHALL rastrear las siguientes métricas operativas por cada ciclo de revisión (donde un ciclo de revisión es un período definido por el fundador entre 30 y 180 días calendario): candidatos creados en el ciclo, Assets promovidos a CANONICAL, Assets REJECTED, Assets reutilizados por Labs distintos al de origen (donde reutilización es el uso documentado de un Asset por un Lab diferente al que lo creó), product_attachments activos, Assets en estado DEPRECATED, y horas de mantenimiento invertidas en Assets existentes durante el ciclo.
2. THE Asset_System SHALL registrar cada métrica con un valor numérico y la fecha del ciclo de revisión al que pertenece, de modo que toda métrica esté vinculada a un resultado observable (Assets promovidos, reutilizados, deprecados o con product_attachment) y no se registren conteos totales acumulados sin referencia a un ciclo ni a una acción derivada.
3. WHILE LabOS opera en contexto SOLO, THE Asset_System SHALL permitir el registro manual de métricas con un esfuerzo máximo de 60 minutos por ciclo de revisión, sin requerir automatización ni herramientas adicionales al repositorio existente.
4. IF un Asset con sharing_scope LabOS-Shared, Cross-Lab o Public no registra reutilización por ningún Lab distinto al de origen durante 2 ciclos de revisión consecutivos, THEN THE Asset_System SHALL marcar ese Asset para evaluación de deprecación en el siguiente ciclo de revisión. IF un Asset con sharing_scope Lab-Private no registra uso documentado dentro del originating_Lab durante 2 ciclos de revisión consecutivos, THEN THE Asset_System SHALL igualmente marcarlo para evaluación de deprecación. [CORRECCIÓN 3: separa el trigger de deprecación por sharing_scope para que Lab-Private assets no queden permanentemente marcados por ausencia de cross-Lab reuse]
5. IF un Asset marcado para evaluación de deprecación recibe reutilización documentada antes del siguiente ciclo de revisión, THEN THE Asset_System SHALL remover la marca de evaluación de deprecación.

---

### Requerimiento 12: Deprecación y Archivo

**User Story:** Como fundador, quiero un proceso formal para retirar Assets que ya no aportan valor, para que el registro no acumule Assets obsoletos sin mecanismo de limpieza.

#### Criterios de Aceptación

1. WHEN el Asset_Owner identifica que un Asset cumple al menos una condición de deprecación (no ha sido consumido ni referenciado en los últimos 90 días, tiene un Asset sucesor en estado CANONICAL que cubre su funcionalidad, o su costo de mantenimiento documentado supera el valor de su último uso registrado), THE Asset_System SHALL permitir iniciar el proceso de deprecación.
2. WHEN un Asset se marca DEPRECATED, THE Asset_System SHALL requerir: motivo documentado (mínimo 1 oración indicando la condición de deprecación cumplida), fecha de deprecación, referencia al Asset sucesor (si existe), y notificación a todos los consumidores que hayan referenciado o utilizado el Asset en los últimos 180 días.
3. WHEN un Asset DEPRECATED tiene al menos un consumidor notificado, THE Asset_System SHALL requerir un plan de migración que incluya: Asset sucesor o alternativa propuesta, plazo de migración (máximo 90 días calendario), y confirmación de recepción por parte de cada consumidor notificado, antes de permitir la transición a ARCHIVED.
4. WHEN un Asset DEPRECATED no tiene consumidores notificados, o todos los consumidores notificados han confirmado migración completada, y ha transcurrido un ciclo de revisión completo (mínimo 30 días, máximo 180 días desde la fecha de deprecación), THE Asset_System SHALL permitir su transición a ARCHIVED.
5. THE Asset_System SHALL preservar Assets ARCHIVED en el registro con toda su metadata histórica, accesibles mediante consulta directa por identificador o búsqueda en el archivo histórico, pero excluidos de los resultados de búsqueda de Assets disponibles para reutilización.
6. IF nueva evidencia documenta relevancia de un Asset ARCHIVED (al menos 1 referencia verificable a demanda activa o caso de uso sin cobertura por Assets existentes), THEN THE Asset_System SHALL permitir su reactivación, requiriendo re-evaluación por los mismos quality gates que aplicaron a su último estado ACTIVE previo a la deprecación.
7. IF un Asset permanece en estado DEPRECATED por más de 180 días sin transicionar a ARCHIVED ni reactivarse, THEN THE Asset_System SHALL notificar al Asset_Owner para forzar una decisión de resolución (archivar o reactivar) en un plazo máximo de 14 días calendario.

---

### Requerimiento 13: Integración Knowledge-to-Asset

**User Story:** Como fundador, quiero que Package 003 defina su responsabilidad a partir del handoff de Package 002 sin redefinir el ciclo de vida del Knowledge Object, para que la frontera entre Knowledge y Asset sea clara y sin solapamiento.

#### Criterios de Aceptación

1. THE Asset_System SHALL crear una nueva entidad Asset en estado `borrador` (content_state de Package 000) por cada Asset_Candidate que reciba desde el handoff definido en Package 002 (knowledge-to-asset-handoff.md), incluyendo como mínimo los 5 campos obligatorios: nombre, tipo, descripción, hipótesis de uso y estado.
2. IF un Asset_Candidate no cumple todos los criterios de elegibilidad definidos en Package 002 (estado KO `validated` o `canonical`, confianza MEDIO o ALTO, provenance PARTIAL o superior, freshness CURRENT o REVIEW_DUE), THEN THE Asset_System SHALL rechazar el candidato sin crear entidad Asset y sin modificar el Knowledge_Object fuente.
3. WHEN el Asset es creado tras el handoff, THE Asset_System SHALL gestionar su ciclo de vida completo bajo el governance lifecycle de Package 003: intake como CANDIDATE, calificación, promoción a CANONICAL, mantenimiento, compartición, product_attachment y retiro.
4. THE Asset_System SHALL preservar la referencia a uno o más Knowledge_Object(s) fuente como parte obligatoria de la provenance del Asset, soportando relación many-to-many entre Knowledge_Objects y Assets.
5. THE Asset_System SHALL NO modificar el estado, ownership ni metadata del Knowledge_Object fuente durante ni después del handoff.
6. IF un Knowledge_Object fuente cambia a estado `superseded` o `deprecated`, o incrementa versión MAJOR, THEN THE Asset_System SHALL marcar el Asset derivado para revisión sin invalidarlo automáticamente.

---

### Requerimiento 14: Integración Asset-to-Product

**User Story:** Como fundador, quiero que Package 003 defina las condiciones bajo las cuales un Asset canónico es elegible para contribuir a un Product, sin definir el Product Factory (Package 004), para que exista un handoff conceptual claro hacia la productización.

#### Criterios de Aceptación

1. THE Asset_System SHALL definir criterios de elegibilidad para product_attachment: Asset en estado CANONICAL (lifecycle state de Package 003, conforme a R3), sin cambios MAJOR registrados en los últimos 30 días calendario, ownership explícito asignado a exactamente un Asset_Owner, Revenue_Thesis documentada con los 3 campos mínimos (segmento, formato, modelo de ingreso), y mantenibilidad confirmada mediante al menos una revisión completada dentro de los últimos 90 días calendario. [CORRECCIÓN 1: reemplaza la referencia a "estado productizado del ciclo borrador→validado→productizado" de Package 000 por el estado CANONICAL del governance lifecycle de Package 003. El content_state de Package 000 y el governance lifecycle de Package 003 son dimensiones separadas — la elegibilidad para product_attachment se rige por el governance lifecycle state.]
2. WHEN un Asset se vincula a un Product (product_attachment), THE Asset_System SHALL registrar: identificador del Product al que contribuye, fecha de vinculación (formato ISO 8601), tipo de contribución (core: funcionalidad principal sin la cual el Product no opera; supporting: funcionalidad que mejora el Product pero no es indispensable; optional: funcionalidad complementaria removible sin degradar el Product), y lista de dependientes afectados en caso de deprecación.
3. THE Asset_System SHALL establecer que el product_attachment no transfiere ownership del Asset: el Asset_Owner retiene responsabilidad de mantenimiento independientemente del Product.
4. IF un Asset con product_attachment activo recibe una solicitud de cambio MAJOR o deprecación, THEN THE Asset_System SHALL requerir una evaluación de impacto que documente: lista de Products afectados, tipo de contribución en cada Product, acción propuesta (migración, reemplazo o remoción) y confirmación del Asset_Owner antes de proceder.
5. THE Asset_System SHALL NO definir el ciclo de vida del Product, el Product Factory ni mecanismos de revenue — esos pertenecen a Package 004.
6. IF un Asset no cumple uno o más criterios de elegibilidad para product_attachment, THEN THE Asset_System SHALL rechazar la vinculación indicando cuáles criterios específicos no se satisfacen.

---

### Requerimiento 15: Labs como Productores y Consumidores de Assets

**User Story:** Como fundador, quiero definir cómo los Labs interactúan con el Asset System como productores y consumidores, para que la relación Lab-Asset esté gobernada y sea bidireccional.

#### Criterios de Aceptación

1. THE Asset_System SHALL establecer que cada Lab puede producir Assets (crear Asset_Candidates desde su investigación y trabajo operativo) y consumir Assets (referenciar Assets compartidos de otros Labs o de LabOS en su propio trabajo, registrándose como consumidor activo al hacerlo).
2. WHEN un Lab produce un Asset_Candidate, THE Asset_System SHALL registrar el Lab como originating_Lab en la metadata del candidato, incluyendo: identificador del Lab, fecha de registro y referencia a la investigación o actividad operativa que originó el candidato.
3. WHEN un Lab referencia un Asset con sharing_scope LabOS-Shared o Public en su trabajo operativo, investigación o productos, THE Asset_System SHALL registrar el Lab como consumidor activo en la metadata del Asset, incluyendo: identificador del Lab consumidor, fecha de primer consumo y versión del Asset referenciada.
4. THE Asset_System SHALL respetar los boundaries de Lab definidos en Package 001A: Assets con sharing_scope Lab-Private no son accesibles por otros Labs sin publicación explícita vía Asset_Sharing_Protocol.
5. IF un Lab intenta consumir un Asset con sharing_scope Lab-Private de otro Lab sin que este haya sido publicado vía Asset_Sharing_Protocol, THEN THE Asset_System SHALL rechazar el consumo e indicar que el Asset no está disponible para compartición.
6. THE Asset_System SHALL establecer que LabOS (como sistema transversal) puede poseer Assets de infraestructura compartida que no pertenecen a ningún Lab individual, y que dichos Assets tienen como Asset_Owner al Fundador en contexto SOLO.
7. WHEN un Lab deja de referenciar un Asset compartido (no lo utiliza en ningún trabajo activo durante un ciclo de revisión completo), THE Asset_System SHALL permitir su desregistro como consumidor activo de ese Asset.

---

### Requerimiento 16: Asset Registry Conceptual

**User Story:** Como fundador, quiero un modelo conceptual del registro de Assets con metadata obligatoria y opcional definida, para que cuando se implemente (futuramente) exista una especificación clara de qué debe contener.

#### Criterios de Aceptación

1. THE Asset_System SHALL definir exactamente 8 campos de metadata obligatoria mínima para el registro de un Asset_Candidate (Tier 1 intake): nombre (máximo 80 caracteres), tipo (uno de los 7 tipos canónicos), descripción (máximo 500 caracteres y 1–3 oraciones), hipótesis_de_uso, content_state (borrador, validado o productizado), originating_Lab, source_of_truth (ruta o ubicación canónica) y provenance (referencia verificable a KO(s), research_id o fuente externa, mínimo 1). Al registrar el Candidate, THE Asset_System SHALL asignar además un asset_id provisional; este identificador es metadata controlada por el registro y no un noveno campo de intake aportado por el owner. [CORRECCIÓN v1.3 C1/C2 — límite canónico y separación de estados]
2. THE Asset_System SHALL definir exactamente 8 campos adicionales obligatorios (Tier 2) que deben completarse para promoción a CANONICAL: estado_lifecycle (uno de los 7 estados de R3), versión (MAJOR.MINOR.PATCH, inicia en 1.0.0), Asset_Owner, fecha_de_creación (ISO 8601), nivel_de_compartición (`sharing_scope`), `consumption_state`, dimensiones_calificación y aprobación_fundador. El asset_id provisional SHALL consolidarse como identificador definitivo en formato `{LAB}-{TIPO}-{NNN}` o esquema equivalente sin contarse nuevamente como campo adicional. `content_state` y `estado_lifecycle` SHALL registrarse y evolucionar independientemente; ningún valor de uno SHALL derivar, implicar ni transicionar automáticamente el otro. [CORRECCIÓN v1.3 C2/C4 — Tier 2 y exposición observable]
3. THE Asset_System SHALL definir la siguiente metadata opcional: consumidores activos (lista de labs o productos que usan el asset), product_attachments (productos asociados), dependencias de otros Assets (lista de asset_ids), sensibilidad (uno de: pública, interna, confidencial), licensing (tipo de licencia aplicable), fecha_última_revisión (formato ISO 8601), quality_status (uno de: sin_evaluar, en_revisión, validado, rechazado) y costo_de_mantenimiento_estimado (horas/mes, rango 0 a 999).
4. THE Asset_System SHALL establecer que el Asset Registry es un modelo conceptual documentado en este package y NO requiere implementación como software, base de datos, API ni servicio.
5. THE Asset_System SHALL permitir que la implementación inicial del registro sea un documento markdown o archivo estructurado mantenido manualmente por el fundador como único operador.
6. THE Asset_System SHALL definir que los 5 campos mínimos de Package 000 (Nombre, Tipo, Descripción, Hipótesis de uso, Estado) son un subconjunto de Tier 1, mapeados respectivamente a: nombre, tipo, descripción, hipótesis_de_uso y content_state. `estado_lifecycle` pertenece a Tier 2 y es una dimensión de gobernanza separada; no sustituye ni deriva de content_state.

---

### Requerimiento 17: Validación con Crypto Scalping Core

**User Story:** Como fundador, quiero validar los workflows del Asset System contra los 5 Asset candidates reales de Crypto Scalping Core, para que las reglas definidas se prueben contra material concreto antes de considerarse canónicas.

#### Criterios de Aceptación

1. WHEN los workflows del Asset_System están definidos (Requerimientos 1-5 documentados), THE Asset_System SHALL evaluar cada uno de los 5 Asset candidates de CSC (ASSET-1 a ASSET-5) contra las 5 dimensiones obligatorias del Requerimiento 4 (evidencia de reutilización, calidad mínima documentable, provenance trazable, ownership asignado, source of truth identificado), produciendo para cada candidato un resultado por dimensión clasificado como: cumple, no cumple, o no evaluable con justificación.
2. THE Asset_System SHALL clasificar cada candidato de CSC en exactamente una de las siguientes categorías basándose en los resultados de la evaluación por dimensiones: READY_FOR_REVIEW (cumple las 5 dimensiones obligatorias), NEEDS_REMEDIATION (al menos 1 dimensión obligatoria no cumple pero es subsanable), NOT_AN_ASSET (no cumple la definición de Asset del Requerimiento 1 o tiene 3 o más dimensiones obligatorias no cumplidas sin ruta de remediación viable), EVIDENCE_REQUIRED (dimensiones evaluadas como "no evaluable" por falta de información disponible).
3. THE Asset_System SHALL NO promover automáticamente ningún candidato de CSC a CANONICAL; toda promoción requiere evaluación individual y aprobación explícita del Fundador.
4. THE Asset_System SHALL NO alterar código fuente del repositorio Crypto Scalping Core ni reclamar profitabilidad de ninguna estrategia.
5. THE Asset_System SHALL documentar para cada candidato de CSC: gaps identificados por dimensión, remediaciones requeridas con acción específica por cada gap, y próximos pasos para alcanzar el estado READY_FOR_REVIEW (o justificación de por qué READY_FOR_REVIEW no es alcanzable).
6. IF un candidato de CSC tiene acoplamiento fuerte al repositorio de origen que impide demostrar reutilización fuera de CSC, THEN THE Asset_System SHALL documentar el acoplamiento como gap en la dimensión "evidencia de reutilización" e incluir como remediación la acción de desacoplamiento necesaria para que el candidato sea evaluable como Asset independiente.

---

### Requerimiento 18: Gobernanza y Aprobación del Fundador

**User Story:** Como fundador, quiero que toda decisión crítica del Asset System (promoción, deprecación, compartición externa) requiera aprobación explícita documentada, para que la gobernanza SOLO sea ligera pero trazable.

#### Criterios de Aceptación

1. THE Asset_System SHALL requerir aprobación explícita del Fundador para: promoción de VALIDATED a CANONICAL, cambio de sharing_scope de Lab-Private a LabOS-Shared o superior, publicación externa (sharing_scope Public) y deprecación de Asset con 1 o más consumidores activos.
2. WHILE LabOS opera en contexto SOLO, THE Asset_System SHALL aceptar aprobación documentada en forma de commit message, nota en el registro de Asset o campo de aprobación en metadata, sin requerir proceso formal multi-persona.
3. THE Asset_System SHALL registrar cada aprobación con: decisor (Fundador), fecha, Asset afectado y justificación de entre 10 y 280 caracteres que indique el motivo de la decisión.
4. THE Asset_System SHALL respetar el architecture-change-control-v1.0 para cualquier cambio que altere las reglas del Asset System (nueva clasificación, cambio de quality gates, modificación de taxonomía).
5. IF una acción crítica (promoción, cambio de sharing_scope, publicación o deprecación con consumidores activos) se intenta sin aprobación documentada del Fundador, THEN THE Asset_System SHALL bloquear la transición y mantener el Asset en su estado actual hasta que se registre la aprobación con todos los campos requeridos (decisor, fecha, Asset afectado, justificación).
6. IF un registro de aprobación no contiene todos los campos obligatorios (decisor, fecha, Asset afectado, justificación de 10-280 caracteres), THEN THE Asset_System SHALL considerar la aprobación como inválida e indicar los campos faltantes o fuera de rango.

---

### Requerimiento 19: Compatibilidad Arquitectónica y Change Control

**User Story:** Como fundador, quiero que Package 003 opere estrictamente dentro del Architecture Baseline v1.0 sin redefinir conceptos de packages anteriores, para que la integridad del ecosistema se preserve.

#### Criterios de Aceptación

1. THE Asset_System SHALL referenciar la definición canónica de Activo del glosario de Package 000 mediante cross-link explícito, y toda extensión que agregue SHALL preservar el significado base sin alterar los 7 tipos canónicos ni sus descripciones establecidas en ADR-0002, conforme al mecanismo de extensión de ADR-0001 §2.
2. THE Asset_System SHALL NO redefinir los conceptos de: Lab, Knowledge_Object, Product, Research ni Package tal como están definidos en sus packages de origen, donde redefinir significa alterar el significado base del término o crear una definición paralela sin referencia explícita a la fuente canónica.
3. THE Asset_System SHALL NO activar Capability como concepto operativo, manteniéndolo en estado dormant hasta que se satisfaga el trigger formal de ≥3 labs en estado "operando" con al menos 1 activo compartido cross-lab por cada par de labs.
4. THE Asset_System SHALL NO implementar software, crear bases de datos, APIs, interfaces de usuario, servicios de registro ni agentes de IA.
5. THE Asset_System SHALL NO autorizar trading en vivo, reclamar profitabilidad, resolver dataset licensing, walk-forward, Monte Carlo ni monetization validation del Crypto Scalping Core.
6. IF Package 003 requiere modificar una definición base o agregar una invariante arquitectónica, THEN THE Asset_System SHALL proponer un ADR formal clasificado como MAJOR conforme al architecture-change-control-v1.0, incluyendo análisis de impacto y plan de migración antes de aplicar el cambio.
7. WHEN Package 003 produce un documento con estado CANONICAL o GOVERNING, THE Asset_System SHALL verificar que ningún término definido contradice las definiciones del glosario canónico de Package 000 ni los ADRs vigentes (ADR-0001, ADR-0002), registrando el resultado de la verificación de no-contradicción en el documento producido.

---

### Requerimiento 20: Propagación de Cambios desde Knowledge Objects

**User Story:** Como fundador, quiero reglas claras sobre qué ocurre con un Asset cuando su Knowledge Object fuente cambia de estado, para que los Assets no queden silenciosamente invalidados por cambios en sus dependencias upstream.

#### Criterios de Aceptación

1. WHEN un Knowledge_Object fuente de un Asset es marcado como superseded, THE Asset_System SHALL cambiar el estado de revisión del Asset a `review_required` con motivo "KO fuente superseded" y registrar el identificador del KO que cambió de estado.
2. WHEN un Knowledge_Object fuente de un Asset es marcado como deprecated, THE Asset_System SHALL cambiar el estado de revisión del Asset a `review_required` con motivo "KO fuente deprecated" y registrar el identificador del KO que cambió de estado.
3. WHEN un Knowledge_Object fuente de un Asset cambia versión MAJOR, THE Asset_System SHALL cambiar el estado de revisión del Asset a `review_required` con motivo "KO fuente cambió versión MAJOR" e incluir la versión anterior y la nueva versión del KO.
4. WHEN un Knowledge_Object fuente de un Asset cambia versión MINOR, THE Asset_System SHALL mantener el estado de revisión del Asset sin cambios y no generar notificación al Asset_Owner.
5. THE Asset_System SHALL preservar el estado de lifecycle del Asset sin modificación automática cuando cualquier KO fuente cambia de estado o versión; únicamente el Asset_Owner podrá cambiar el lifecycle del Asset eligiendo entre: actualizar el Asset, mantenerlo sin cambios, o deprecarlo.
6. IF un Asset tiene múltiples Knowledge_Objects como fuente y solo uno de ellos cambia de estado o versión MAJOR, THEN THE Asset_System SHALL marcar el Asset como `review_required` indicando específicamente cuál KO cambió, sin afectar la referencia a los demás KOs fuente que permanecen estables.
7. WHEN un Knowledge_Object fuente de un Asset cambia a estado `disputed`, THE Asset_System SHALL agregar un review flag al Asset con motivo "KO fuente en estado disputed" sin invalidar el lifecycle state del Asset ni cambiar el Asset a `review_required`. El review flag es informativo — el Asset_Owner decide si actuar sobre él. [CORRECCIÓN 7: añade manejo de KO en estado disputed, gap identificado en R20]

---

---

## No-Goals Explícitos

Los siguientes quedan explícitamente FUERA del alcance de Package 003:

1. Implementación de software (base de datos, API, UI, servicios, agentes, RAG).
2. Definición de Product Factory, Revenue Engine o mecanismos de monetización (Package 004).
3. Redefinición de Knowledge Object lifecycle (Package 002).
4. Redefinición de Lab, Research o Package (Packages 000, 001).
5. Activación de Capability como concepto operativo.
6. Promoción automática de Asset candidates de CSC.
7. Modificación de código fuente de Crypto Scalping Core.
8. Autorización de trading en vivo o claims de profitabilidad.
9. Resolución de dataset licensing, walk-forward, Monte Carlo o monetization validation.
10. Creación de shared asset index como servicio implementado.

---

## Referencias Arquitectónicas

- Package 000 README.md — Glosario canónico y Asset_First_Model
- Package 000 007-company-model.md — Taxonomía de activos y criterios mínimos (content_state: borrador, validado, productizado)
- ADR-0001 — Jerarquía de Definición Terminológica
- ADR-0002 — Consolidación de Taxonomía de Activos
- Package 001 — Research Methodology (research-to-asset pipeline)
- Package 001A — Lab Integration Framework (Asset_Sharing_Protocol, boundaries)
- Package 002 — Knowledge Architecture (knowledge-to-asset-handoff.md)
- Architecture Baseline v1.0
- architecture-change-control-v1.0.md
- package-003-entry-conditions.md

---

## Notas de Revisión (v1.1 — aplicadas por reviewer independiente)

Las siguientes correcciones se aplicaron respecto a la versión original. Ver `package-003-requirements-change-log.md` para trazabilidad completa.

| ID | Requerimiento(s) afectados | Tipo | Descripción breve |
|----|---------------------------|------|-------------------|
| C1 | R14.1 | Contradicción | Reemplaza referencia a "estado productizado" de Package 000 por estado CANONICAL del governance lifecycle de Package 003 |
| C2 | R4.1 | Gap | Divide evidencia de reutilización en Forma A (demostrada) y Forma B (diseñado-para-reuso) para cubrir first-time assets |
| C3 | R11.4 | Inconsistencia | Separa trigger de deprecación por sharing_scope: cross-Lab reuse para assets compartidos, uso interno para Lab-Private |
| C4 | R2.2 | Ambigüedad | Mapea explícitamente "compartibles por defecto" al nivel LabOS-Shared per R9.1 |
| C5 | R16.1-2 | Incompleto | Divide metadata obligatoria en dos sub-conjuntos: intake (CANDIDATE) y promoción completa (CANONICAL) |
| C6 | R3.1 | Ambigüedad | Agrega nota explícita que sharing_scope y product_attachment son atributos ortogonales al lifecycle state |
| C7 | R20.7 | Gap | Añade manejo de KO en estado `disputed` como review flag informativo sin invalidar lifecycle state |
| C8 | R8.7 | Gap | Añade distinción explícita entre nueva versión, Asset derivado y fork |

---

## Notas de Revisión (v1.2 — correcciones del Principal Architect, 2025-07-31)

Las siguientes correcciones adicionales se aplicaron en esta revisión. Ver `package-003-requirements-change-log.md` sección "Correcciones v1.2" para trazabilidad completa.

| ID | Requerimiento(s) afectados | Tipo | Descripción breve |
|----|---------------------------|------|-------------------|
| C9 | R3.1, R4.6, R20; Glosario | Clarificación | Define `review_required` como flag/atributo ortogonal al lifecycle state en el Glosario y en R3.1; no es un octavo estado de gobernanza |
| C10 | R6.7 | Clarificación | Añade el rol maintainer a la lista de roles que el Fundador puede ocupar en contexto SOLO |
| C11 | R7.6 | Clarificación | Añade sub-caso para Assets originados en Research propia sin KO formalizado: acepta research_id como provenance en lugar de knowledge_id |
| C12 | R6.9 (nuevo) | Añadido | Define que la Canonical_Authority del originating_Lab retiene autoridad post cross-Lab promotion; cambio de co-governance requiere ADR |

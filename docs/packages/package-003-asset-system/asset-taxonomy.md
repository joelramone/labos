# Taxonomía Canónica de Assets

## Autoridad

[Hecho] [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md) consolida como fuente única la taxonomía definida por [Package 000 — 007-company-model.md](../package-000-foundation/007-company-model.md). [Decisión] Package 003 aplica esa taxonomía; no crea una taxonomía paralela.

## Los siete tipos canónicos

| # | Identificador canónico | Descripción referenciada | sharing_scope por defecto |
|---:|---|---|---|
| 1 | Documento | Registro estructurado de conocimiento, análisis o decisiones | LabOS-Shared |
| 2 | Template | Plantilla reutilizable con estructura predefinida | LabOS-Shared |
| 3 | Dataset | Conjunto de datos organizados y documentados | LabOS-Shared |
| 4 | Herramienta | Software, script o utilidad que opera de forma autónoma | LabOS-Shared |
| 5 | Componente | Módulo reutilizable que requiere un sistema mayor para funcionar | Lab-Private |
| 6 | Framework | Estructura conceptual o técnica que organiza componentes bajo principios coherentes | LabOS-Shared |
| 7 | Playbook | Guía operativa paso a paso para ejecución repetible | Lab-Private |

[Decisión] Cada Asset usa exactamente uno de estos siete identificadores primarios en español. Puede mostrarse opcionalmente un equivalente inglés entre paréntesis, sin sustituir el identificador canónico.

## Reglas de clasificación

1. [Decisión] Un tipo ausente o diferente de los siete valores se rechaza y se informan los valores válidos.
2. [Decisión] Herramienta opera autónomamente; Componente requiere un sistema mayor. El tamaño, lenguaje o carácter ejecutable no decide por sí solo.
3. [Decisión] Documento preserva o comunica información; Template define una estructura reutilizable para producir instancias.
4. [Decisión] Framework organiza principios o componentes; Playbook prescribe pasos operativos secuenciales.
5. [Decisión] Dataset es evidencia organizada; un reporte interpretativo derivado normalmente es Documento, no Dataset.
6. [Decisión] Un artefacto ambiguo debe clasificarse por su forma de consumo primaria y documentar la razón; no recibe dos tipos.

## Defaults de compartición

[Decisión] Documento, Template, Dataset, Herramienta y Framework reciben `LabOS-Shared` como autorización por defecto conforme a ADR-0002 y Requirements v1.3. Componente y Playbook reciben `Lab-Private`. El default de sharing_scope no demuestra consumo efectivo, reutilización ni promoción a Asset_Canónico.

[Decisión] Un Componente o Playbook puede compartirse únicamente mediante publicación explícita conforme al futuro protocolo de sharing de Package 003. Esta excepción modifica el scope autorizado, no el tipo.

## Control de cambios

[Decisión] Un octavo tipo o el renombrado de un tipo existente requiere un ADR aprobado que actualice Package 000. Package 003 no puede aceptar tipos ad hoc.

## Validación ADR-0002

| Control | Resultado |
|---|---|
| Tipos canónicos en español | 7/7 |
| Tipos adicionales | 0 |
| Defaults LabOS-Shared | 5 |
| Defaults Lab-Private | 2 |
| Herramienta/Componente distinguibles | PASS |
| Taxonomía renombrada o redefinida | NO |

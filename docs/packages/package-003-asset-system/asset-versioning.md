# Versionado y Evolución de Assets

## Enfoque proporcional

[Decisión] Todo Asset_Canónico registra una versión `MAJOR.MINOR.PATCH`, iniciando en `1.0.0`. La clasificación describe impacto semántico y compatibilidad; no obliga a que todo artefacto use tooling SemVer ni presupone software.

| Cambio | Regla | Ejemplo documental |
|---|---|---|
| Metadata correction | PATCH si no cambia significado | Corregir link o typo |
| Content revision no semántica | PATCH | Clarificar redacción sin cambiar regla |
| Compatible evolution | MINOR | Añadir ejemplo o sección opcional |
| Breaking evolution | MAJOR | Cambiar interfaz, estructura consumida o regla incompatible |

[Decisión] Si cambia propósito fundamental o audiencia respecto de 1.0.0, se crea un Asset nuevo; MAJOR no se usa para ocultar una identidad diferente.

## Evolución e identidad

| Camino | asset_id | Historial/original | Compatibilidad |
|---|---|---|---|
| Nueva versión | Mismo | Entrada inmutable nueva; anterior preservada | PATCH/MINOR compatible; MAJOR requiere adaptación |
| Asset derivado | Nuevo | Provenance: original, versión base y modificaciones | Puede divergir para contexto específico |
| Fork | Nuevo | Provenance al original | Desarrollo independiente; no promete compatibilidad |
| Replacement | Nuevo o versión sucesora según propósito | Original preservado y referencia bidireccional | Sustituye caso de uso con migración explícita |
| Supersession | Referencia al sucesor | Versión anterior marcada SUPERSEDED, nunca sobrescrita | Consumers migran; historial consultable |

## Registro inmutable

Cada entrada contiene versión, fecha ISO 8601, descripción de 10–500 caracteres y autor. Entradas previas no se editan ni eliminan. Correcciones al historial se agregan como entradas nuevas. [Decisión]

## Consumers y breaking change

[Decisión] Antes de MAJOR, replacement o supersession se identifican consumers y futuras dependencias registradas. Se documenta impacto, se notifica según el contrato aplicable y se preserva un camino de migración. No se crea Product ni se define su lifecycle.

## Decisión por naturaleza del Asset

| Naturaleza | Aplicación |
|---|---|
| Documento/Template/Playbook/Framework | Versionar por cambio de significado, estructura o compatibilidad de uso |
| Dataset | Versionar por schema, cobertura, metodología o corrección; la actualización de filas puede requerir regla específica documentada |
| Herramienta/Componente | Versionar por interfaz y comportamiento observable |

[Decisión] Cuando MAJOR/MINOR/PATCH no describe suficientemente una actualización continua, el Asset conserva el número gobernado y añade una revisión fechada o identificador de snapshot; la excepción se documenta sin perder identidad ni historial.

## Validación

| Control | Resultado |
|---|---|
| Versión inicial CANONICAL | 1.0.0 |
| SemVer impuesto como tooling universal | No |
| Derived/fork usan ID nuevo | Sí |
| Historial sobrescrito | Prohibido |
| Breaking change identifica consumers | Sí |
| Propósito nuevo conserva ID | No |

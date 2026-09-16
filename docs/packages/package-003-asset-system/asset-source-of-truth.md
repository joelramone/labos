# Provenance y Source of Truth del Asset

## Regla canónica

[Decisión] Un Asset gobernado tiene exactamente un `source_of_truth`: la ubicación autoritativa de su versión vigente. Las referencias son permitidas; las copias no administradas no son autoritativas y, si se modifican para uso independiente, deben tratarse como Asset derivado.

```text
1 Asset → 1 canonical source_of_truth
```

## Provenance

[Decisión] Package 003 registra referencias de provenance del Asset; no duplica el modelo de Knowledge de [Package 002](../package-002-knowledge-architecture/knowledge-provenance.md). Cuando existe el camino completo se preserva:

```text
Asset → Knowledge_Object(s) → Research → Evidence → Source
```

| Eslabón | Referencia mínima | Autoridad |
|---|---|---|
| Asset | asset_id | Package 003 |
| Knowledge | knowledge_id | Package 002 |
| Research | research_id | Package 001 |
| Evidence | path/ID de evidencia | Lab de origen |
| Source | URL, cita o path identificable | Fuente externa o Lab |

[Decisión] Si no existe KO formal, se acepta `research_id` con motivo de ausencia. Si el origen es externo, se acepta referencia externa directa. Para un Asset_Canónico se registran además originating_Lab, fecha de creación y autor/contribuidor responsable.

## Integridad y copias

- Consumers referencian el source of truth; no crean autoridad paralela.
- Un mirror administrado identifica explícitamente el source canónico y no reemplaza su autoridad.
- Una copia local modificada recibe nuevo asset_id y provenance de derivación.
- Git aporta evidencia técnica, pero no sustituye el historial semántico del Asset.

## Fallas y cambios upstream

| Evento | Acción | Lifecycle |
|---|---|---|
| source inaccesible | Activar NEEDS_REMEDIATION, registrar path/motivo, bloquear nuevas vinculaciones | Sin cambio automático |
| KO superseded | Activar review_required; evaluar validez independiente | Sin cambio automático |
| KO deprecated | Revisar evidencia independiente y posible deprecación | Sin cambio automático |
| KO MAJOR | Evaluar compatibilidad | Sin cambio automático |
| KO MINOR | Registrar referencia actualizada si aplica | Sin review obligatorio |

[Decisión] El lifecycle, ownership, confidence y provenance del KO permanecen bajo Package 002 y no se modifican durante el handoff o review del Asset.

## Escenarios de cadena

| Origen | Cadena válida |
|---|---|
| KO formal | Asset → KO → Research → Evidence → Source |
| Research sin KO | Asset → research_id → Evidence → Source + motivo de ausencia de KO |
| Fuente externa | Asset → referencia externa verificable |

## Validación

| Control | Resultado |
|---|---|
| Sources of truth por Asset | Exactamente 1 |
| References permitidas | Sí |
| Copias no administradas autoritativas | No |
| Modelo Package 002 duplicado | No |
| Ownership/lifecycle del KO alterado | No |

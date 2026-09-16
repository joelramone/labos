# Integración Knowledge → Asset

## Boundary

[Decisión] Package 002 conserva autoridad exclusiva sobre Knowledge_Object, lifecycle, provenance, confidence, freshness y ownership. Package 003 comienza cuando recibe un artefacto elegible para intake como Asset_Candidate.

```text
[Package 002] Knowledge → handoff
                         ↓
[Package 003] Asset_Candidate → qualification → promotion → Asset lifecycle
```

Asset es una entidad nueva; no es un KO renombrado. El KO permanece existente e intacto después del handoff. [Decisión]

## Intake post-handoff

1. Referenciar el contrato [knowledge-to-asset-handoff.md](../package-002-knowledge-architecture/knowledge-to-asset-handoff.md).
2. Verificar elegibilidad Package 002: KO validated/canonical, confidence MEDIO+, provenance PARTIAL+, freshness CURRENT/REVIEW_DUE.
3. Si falla, rechazar intake sin crear Asset y sin modificar KO.
4. Si pasa, crear entidad CANDIDATE con Tier 1 y provenance al/los knowledge_id.
5. Ejecutar qualification y governance Package 003.

## Relaciones

| Relación | Regla |
|---|---|
| Multiple KOs → one Asset | Síntesis permitida; todos los IDs permanecen en provenance |
| One KO → multiple Assets | Permitido; cada Asset tiene identidad/lifecycle propios |
| Asset deprecated | KO no cambia |
| KO changes | Asset se marca/revisa según evento; no se invalida automáticamente |

## Event matrix

| Evento KO | Efecto Asset | Lifecycle Asset |
|---|---|---|
| superseded | `review_required`: KO fuente superseded + ID | Sin cambio automático |
| deprecated | `review_required`: KO fuente deprecated + ID | Sin cambio automático |
| MAJOR | `review_required` + versión anterior/nueva | Sin cambio automático |
| MINOR | Sin flag ni notificación obligatoria | Sin cambio |
| disputed | Review flag informativo con ID | Sin `review_required`; sin cambio |

Con múltiples KOs, el flag identifica únicamente el KO afectado y preserva los restantes. Asset_Owner decide actualizar, mantener con justificación o iniciar deprecación. [Decisión]

## Provenance

[Decisión] Package 003 almacena referencias; no replica el contenido ni el provenance model de Package 002. La cadena preferida es Asset → KO(s) → Research → Evidence → Source. Research directo o fuente externa siguen las excepciones aprobadas.

## Validación de boundary

| Control | Resultado |
|---|---|
| Package 002 authority preservada | Sí |
| Package 003 inicia en Candidate intake | Sí |
| KO convertido/renombrado/eliminado | No |
| Many-to-many | Preservado |
| Superseded/deprecated/MAJOR | Cubiertos |
| Disputed | Flag informativo cubierto |

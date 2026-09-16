# Framework de Calificación de Assets

## Principio

[Decisión] Todo Asset_Candidate se evalúa en las cinco dimensiones obligatorias. El Fast Path reduce profundidad y overhead, nunca elimina dimensiones, risk evaluation ni autoridad humana.

## Cinco dimensiones obligatorias

| # | Dimensión | SATISFECHA cuando | Evidencia mínima Fast Path | Si no se satisface |
|---:|---|---|---|---|
| 1 | Evidencia de reutilización | Forma A o Forma B válida | Referencia verificable A, o declaración B con destino y escenario | NEEDS_REMEDIATION; no UNDER_REVIEW |
| 2 | Calidad mínima documentable | Cinco campos base completos + una validación del owner | Checklist fechado del owner | NEEDS_REMEDIATION |
| 3 | Provenance trazable | KO, research_id o fuente externa verificable y Lab/origen identificable | Una referencia válida | NEEDS_REMEDIATION |
| 4 | Ownership asignado | Asset_Owner humano explícito acepta mantenimiento/lifecycle | Identidad y aceptación | NEEDS_REMEDIATION |
| 5 | Source of truth identificado | Una ubicación canónica única y verificable | Path/URL comprobado | NEEDS_REMEDIATION |

Resultados válidos por dimensión: `SATISFECHA` o `NO_SATISFECHA`. El resultado consolidado y fecha se registran; basta una `NO_SATISFECHA` para bloquear avance. [Decisión]

## Reutilización demostrada y proyectada

| Forma | Nombre | Criterio | Efecto |
|---|---|---|---|
| A | DEMONSTRATED | ≥1 uso fuera del contexto de origen con fecha, contexto y resultado | No requiere trigger especial de Forma B |
| B | DESIGNED-FOR-REUSE / projected reuse | Declaración escrita con ≥1 Lab o dominio destino específico y ≥1 escenario concreto | Al llegar a CANONICAL activa `review_required` a 90 días |

[Decisión] Uso repetido dentro del contexto de origen puede respaldar calidad, pero no se presenta como Forma A fuera del contexto. A los 90 días, Forma B debe aportar uso real o escalar evaluación de deprecación; el lifecycle no cambia automáticamente.

## Dimensiones recomendadas

Repetibilidad, mantenibilidad, documentación de uso, estabilidad de dependencias, valor medible y aplicabilidad cross-Lab se registran como `PRESENTE`/`AUSENTE`; no bloquean promoción salvo que otra gate las vuelva obligatorias por exposición. [Decisión]

## Dimensiones dependientes de madurez

Sensibilidad/licensing, relevancia de Product, costo operativo y diferenciación estratégica aplican solo ante intención Cross-Lab, Public o `product_attachment`, según Design. No crean Products ni Product lifecycle. [Decisión]

## Fast Path

Elegibilidad: exposición efectiva Nivel 1, `NO_ACTIVE_EXTERNAL_CONSUMERS`, sin dependencias externas, sin `product_attachment`, scope no Public, cinco dimensiones SATISFECHAS y sin risk override que exija gates elevados. [Decisión]

Una aprobación del Fundador puede cubrir evaluación y aprobación final. La evidencia puede ser breve y referenciada; ninguna dimensión se omite y no existe `AUTO_PROMOTE`.

## Clasificaciones operativas

- `READY_FOR_REVIEW`: cinco dimensiones satisfechas.
- `NEEDS_REMEDIATION`: al menos una dimensión subsanable no satisfecha.
- `NOT_AN_ASSET`: no cumple definición o la brecha es irremediable.
- `EVIDENCE_REQUIRED`: no hay evidencia suficiente para decidir.

## Validación de completitud

| Control | Resultado |
|---|---|
| Dimensiones obligatorias | 5/5 |
| Forma A/B separadas | PASS |
| Trigger Forma B | 90 días |
| Dimensiones omitibles en Fast Path | 0 |
| Promoción automática | PROHIBIDA |
| Precisión numérica inventada | 0 |

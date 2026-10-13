# Problem Evidence Scorecard — Qualitative

[Decisión] Este scorecard organiza juicio cualitativo. No suma puntos, no produce rankings numéricos y no convierte opiniones aisladas en validación.

## Allowed statuses

| Status | Meaning |
|---|---|
| `STRONG_SIGNAL` | Conducta concreta, repetida o económicamente relevante, respaldada por más de un contexto independiente |
| `MODERATE_SIGNAL` | Evidencia concreta pero limitada en recurrencia, consecuencia o independencia |
| `WEAK_SIGNAL` | Preferencia, opinión o incidente aislado sin conducta suficiente |
| `CONTRADICTED` | Evidencia observable debilita o niega el problema supuesto |
| `INSUFFICIENT_EVIDENCE` | No existe material suficiente para juzgar |

## Per-problem assessment

| Dimension | Question | Strong signal example | Status | Evidence IDs | Contradictions |
|---|---|---|---|---|---|
| Recurrence | ¿Aparece repetidamente en tiempo o participantes independientes? | Episodios recientes y repetidos con contexto | `{status}` | `{IDs}` | `{evidence}` |
| Severity | ¿Produce una consecuencia que cambia conducta o resultado? | Abandono, pérdida significativa de tiempo/esfuerzo o meta bloqueada | `{status}` | `{IDs}` | `{evidence}` |
| Current expenditure | ¿Ya se paga para resolverlo? | Pago/renovación verificable asociado al problema | `{status}` | `{IDs}` | `{evidence}` |
| Workaround effort | ¿Existe una solución improvisada costosa? | Rutina manual repetida, múltiples herramientas o ayuda informal | `{status}` | `{IDs}` | `{evidence}` |
| Dissatisfaction | ¿La alternativa actual deja un gap concreto? | Fallo específico demostrado; no sólo “podría mejorar” | `{status}` | `{IDs}` | `{evidence}` |
| Active search | ¿Busca activamente otra solución? | Comparó, consultó o probó alternativas recientemente | `{status}` | `{IDs}` | `{evidence}` |
| Switching attempts | ¿Cambió o abandonó soluciones por el problema? | Cambio reciente con trigger y resultado documentados | `{status}` | `{IDs}` | `{evidence}` |
| Emotional relevance | ¿Afecta confianza, identidad, motivación o continuidad? | Consecuencia emocional vinculada a conducta concreta | `{status}` | `{IDs}` | `{evidence}` |
| Economic relevance | ¿Implica gasto, pérdida o presupuesto reasignable? | Gasto existente o coste observable; no hypothetical pricing | `{status}` | `{IDs}` | `{evidence}` |

## Consolidated problem signal

| Problem ID | Behavioral segment/context | Overall status | Why | Strongest evidence | Strongest contradiction | Next action |
|---|---|---|---|---|---|---|
| `{P-001}` | `{segment}` | `{allowed status}` | `{qualitative rationale}` | `{IDs}` | `{IDs}` | `{continue/narrow/pivot/stop/collect}` |

## Interpretation rules

- `STRONG_SIGNAL` global requiere evidencia conductual, no unanimidad.
- Gasto fortalece una señal pero no es obligatorio si la consecuencia es clara.
- Emotional relevance sin conducta permanece `WEAK_SIGNAL` o `MODERATE_SIGNAL`.
- Contradicciones nunca se promedian ni se ocultan; cambian scope o confidence.
- No usar “me gusta la idea” como evidencia de problema.


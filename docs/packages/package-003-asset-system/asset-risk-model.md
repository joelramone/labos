# Modelo Proporcional de Riesgo del Asset

## Dos ejes

[Decisión] `base exposure` determina gates ordinarios; `risk override` puede elevarlos independientemente del scope. `risk_level` es ortogonal al lifecycle.

La severidad descriptiva usa `LOW`, `MEDIUM`, `HIGH`, `CRITICAL` sin porcentajes inventados. El gate record conserva `BASE` o `ELEVATED` según requiera override. [Decisión]

## Categorías

| Riesgo | Señal | Severidad típica | Mitigación mínima |
|---|---|---|---|
| Financial | Informa trading, inversión o decisiones económicas | HIGH/CRITICAL según impacto | Evidencia explícita, limitations, human review; no profitability/live-trading claim |
| Licensing | Fuente externa, dataset o dependencia con derechos inciertos | HIGH | Verificar licencia; bloquear external publication si no está clara |
| Security | Credenciales, autenticación, ejecución privilegiada | CRITICAL | Mantener confidencial/privado; review humano; no exponer secretos |
| Privacy | Datos personales o sensibles | HIGH/CRITICAL | Minimizar, clasificar y limitar scope |
| Operational | Fallo rompe proceso o consumers | MEDIUM/HIGH | Compatibility, fallback, maintainer y defect response |
| Customer impact | Uso externo afecta terceros | HIGH/CRITICAL | Gates elevados y explicit authority |
| Product dependency | Attachment supporting/core | HIGH/CRITICAL | Impact/migration before MAJOR/deprecation |
| External publication | Reputación, licensing y uso no controlado | HIGH | Nivel 3 + sensitivity/licensing + approval |
| Destructive behavior | Puede borrar/sobrescribir datos o cambiar sistemas | CRITICAL | Prohibir ejecución sin controles/autoridad; documentar recovery |

## Escalación

| Base exposure | Override | Gate aplicado |
|---|---|---|
| Nivel 1 | Ninguno relevante | Base; Fast Path posible |
| Nivel 1 | Licensing/financial/security/privacy/customer/destructive | ELEVATED; Fast Path puede requerir evidencia/gates Nivel 2/3 |
| Nivel 2 | Riesgo HIGH/CRITICAL | ELEVATED; maintainer, sensitivity, impact y authority explícitos |
| Nivel 3 | Cualquiera | Gates máximos; unresolved HIGH/CRITICAL bloquea acción |

[Decisión] Override no cambia lifecycle, no promociona/depreca y no equivale a sharing_scope.

## Riesgo por lifecycle

| Estado | Riesgo dominante | Acción |
|---|---|---|
| CANDIDATE | Intake pobre/licensing desconocido | Remediation antes de review |
| UNDER_REVIEW | Gate incompleto | Bloquear avance y nombrar gaps |
| VALIDATED | Decisión diferida/impacto no revisado | Review trigger |
| CANONICAL | Consumers implícitos, defectos, source roto | Registrar consumers/defects; review_required |
| DEPRECATED | Migración incompleta | No archivar hasta condiciones |
| ARCHIVED/REJECTED | Historia perdida | Preservación inmutable |

## Scenarios

| Caso | Resultado |
|---|---|
| LabOS-Shared sin consumers, dataset externo | Nivel 1 + licensing override ELEVATED |
| Public con licencia no verificada | Publicación bloqueada |
| Canonical con Product core futuro | Nivel 3/CRITICAL dependency; impact obligatorio; no Product creado |
| AI-assisted low-risk document | AI no reduce gates ni adquiere authority |

## Validación

| Control | Resultado |
|---|---|
| Base exposure + override | PASS |
| risk_level usado como lifecycle | No |
| Licensing/customer/safety | Cubiertos |
| Falsa precisión probabilística | 0 |
| Implementation claim | 0 |

# ASSET-3 Candidate Content — Template de journal de experimentación cuantitativa

## Estado y boundary

| Campo | Valor |
|---|---|
| Candidate ID | `ASSET-3` |
| Tipo | Template |
| content_state | `borrador` |
| estado_lifecycle | `VALIDATED` — `FD-ASSET-3-VALIDATED-001`; not CANONICAL |
| Asset_Owner | Joel Diaz / Lab Founder |
| Originating Lab | `LABOS-REF-LAB-0001` — Crypto Scalping Core |
| Reuse | `PROJECTED_REUSE`; no demonstrated cross-context reuse |
| Value | `PROYECTADO`; no economic claim |
| Sensitivity | Estructura LOW; no incorporar contenido de instancias privadas |
| Canonical status | `NOT_CANONICAL` |

Este archivo es el contenido gobernado propuesto del Candidate. Fue extraído de la estructura común directamente verificada en 19 journals del branch `main` de Crypto Scalping Core. No copia resultados, parámetros, datasets ni conclusiones de trading.

## Template copiable

```markdown
# Experiment

## Objective

<Qué pregunta se busca responder y por qué importa>

## Hypothesis

<Afirmación falsable y resultado esperado>

## Dataset

- Reference: <source/evidence reference>
- Scope: <coverage>
- Restrictions: <licensing/sensitivity/usage restrictions>

## Strategy

<Método, intervención o procedimiento evaluado>

## Timeframe

<Período o ventana de observación>

## Parameter Grid

<Configuraciones comparadas o NOT_APPLICABLE con justificación>

## Results

<Resultados observados, incluyendo resultados negativos>

## Best Configuration

<Configuración seleccionada y criterio, o NONE/NOT_APPLICABLE>

## Lessons Learned

<Qué se aprendió; separar hechos, hipótesis y decisiones>

## Recommended Next Experiments

<Siguiente prueba, trigger o decisión de detener>
```

## Provenance y reglas de uso

- Evidence source: `remote GitHub main/research/journal/EXP-000001.md` a `EXP-000019.md`.
- Governance source: [remediation register](./crypto-scalping-core-asset-remediation-register.md).
- Package 001 conserva autoridad sobre Research y Evidence; el template no redefine metodología.
- Package 003 conserva autoridad sobre lifecycle, qualification y promoción.
- El campo Dataset siempre debe declarar restricciones; nunca supone licencia ni redistribución.
- Una instancia completada es Artifact/Research evidence; no se convierte automáticamente en Asset ni demuestra reuse cross-context.

## Intended reuse — Forma B

[Hipótesis] Dominio destino: un LabOS Lab distinto del origen que ejecute investigación estructurada bajo Package 001. Escenario concreto: registrar objetivo, hipótesis, fuente de evidencia, configuración, resultado negativo o positivo y siguiente decisión de un experimento no relacionado con trading cuantitativo.

Si alguna autoridad futura lo lleva a CANONICAL usando Forma B, debe registrar `review_required` a 90 días. La transición a `VALIDATED` no autoriza ni ejecuta CANONICAL.

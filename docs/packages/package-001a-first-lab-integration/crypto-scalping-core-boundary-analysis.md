# Análisis de Boundaries — Crypto Scalping Core

## Propósito

Este documento define los límites operativos de Crypto Scalping Core como Lab dentro del ecosistema LabOS. [Decisión] Los boundaries fueron PROPUESTOS inicialmente y CONFIRMADOS por el fundador el 2025-07-23.

---

## Confirmación del Fundador (2025-07-23)

El fundador confirmó el modelo de ownership con las siguientes precisiones: [Hecho]

| Clasificación | Contenido confirmado | Etiqueta |
|---------------|---------------------|----------|
| Lab-Private | Código de investigación, estrategias, parámetros, lógica de entrada/salida, configuraciones de riesgo, resultados no validados, experimentos en progreso, credenciales, API keys, cuentas, balances, datos financieros personales | [Decisión] |
| Lab-Published (por autorización) | Reportes de investigación, metodología, hallazgos generales — solo cuando el fundador autoriza explícitamente | [Decisión] |
| LabOS-Shared (tras promoción) | Solo KOs y Assets promovidos explícitamente | [Decisión] |
| Externo | Exchanges, proveedores de datos de mercado (no se poseen) | [Hecho] |
| Datasets | Proveniencia externa, NO propiedad automática. Artefactos procesados/derivados SÍ son propiedad. Datos crudos restringidos hasta verificar licencia. | [Decisión] |
| Exclusión corporativa | BYMA, NRTC, SentinelOps, información del empleador = ABSOLUTAMENTE excluidos del Lab y de LabOS | [Decisión] |
| Autonomía | CSC es operacionalmente independiente de LabOS. LabOS = gobernanza, NO runtime. Integraciones futuras opcionales. | [Decisión] |

---

## Boundary Propuesto: DENTRO del Lab (Lab-Private)

Los siguientes elementos se proponen como pertenecientes exclusivamente a Crypto Scalping Core: [Decisión]

> **CONFIRMADO POR FUNDADOR (2025-07-23):** Estrategias, parámetros, lógica de entrada/salida y configuraciones de riesgo son EXPLÍCITAMENTE Lab-Private. [Decisión]

### Código y Herramientas

| Elemento | Clasificación | Justificación |
|----------|--------------|---------------|
| Código de estrategias de trading | Lab-Private | Ventaja competitiva del Lab. No compartible por defecto. [Decisión] |
| Scripts de backtesting | Lab-Private | Específicos al dominio y metodología del Lab. [Decisión] |
| Configuración de parámetros (tuning) | Lab-Private | Datos sensibles de performance del Lab. [Decisión] |
| Bots o ejecutores de trades | Lab-Private | Lógica operativa core del Lab. [Decisión] |

### Datos

| Elemento | Clasificación | Justificación |
|----------|--------------|---------------|
| Datasets de market data recolectados | Lab-Private (restringido) | Proveniencia externa — restringido hasta verificar licencia. Artefactos derivados SÍ son propiedad del Lab. [Decisión] |
| Resultados de backtesting | Lab-Private | Performance data sensible. [Decisión] |
| Logs de operaciones (paper trading o real) | Lab-Private | Historial financiero privado. [Decisión] |
| Métricas de estrategias (Sharpe, drawdown, etc.) | Lab-Private | Datos de performance competitivos. [Decisión] |

### Conocimiento

| Elemento | Clasificación | Justificación |
|----------|--------------|---------------|
| Hallazgos de microestructura de mercado | Lab-Private | Conocimiento competitivo directo. [Decisión] |
| Reglas de entrada/salida de estrategias | Lab-Private | IP core del Lab. [Decisión] |
| Análisis de timing y ventanas óptimas | Lab-Private | Ventaja informacional. [Decisión] |

### Investigación

| Elemento | Clasificación | Justificación |
|----------|--------------|---------------|
| Experimentos de estrategia | Lab-Private | Proceso de descubrimiento propietario. [Decisión] |
| Análisis de exchanges específicos | Lab-Private | Datos operativos del Lab. [Decisión] |
| Evaluación de pares y mercados | Lab-Private | Decisiones tácticas. [Decisión] |

---

## Boundary Propuesto: FUERA del Lab

### Pertenece a LabOS (LabOS-Shared)

| Elemento | Justificación |
|----------|---------------|
| Templates de investigación | Infraestructura compartida — el Lab los consume, no los posee. [Hecho] |
| Metodología de research (Package 001) | Framework genérico aplicable a todos los Labs. [Hecho] |
| Arquitectura de conocimiento (Package 002) | Estructura de KOs compartida. [Hecho] |
| Steering files y convenciones | Gobernanza transversal. [Hecho] |
| Quality gate definitions | Estándar de calidad ecosistémico. [Hecho] |
| Framework de validación de Labs | Herramienta de evaluación genérica. [Hecho] |

### Pertenece al Mundo Externo (fuera de LabOS)

| Elemento | Justificación |
|----------|---------------|
| Exchanges de criptomonedas (Binance, etc.) | Servicios externos no controlados por el Lab ni por LabOS. [Hecho] |
| Credenciales de exchanges | Propiedad personal del fundador, NO del Lab. [Decisión] |
| Cuentas de brokerage | Activo personal, no activo del Lab. [Decisión] |
| Finanzas personales del fundador | Completamente fuera del alcance de LabOS. [Decisión] |
| Sistemas del empleador del fundador | Separación corporativa/personal absoluta. [Decisión] |
| Regulación financiera aplicable | Contexto externo — el Lab debe cumplirla pero no la posee. [Hecho] |
| Market data público en tiempo real | Servicio externo consumido, no producido. [Hecho] |

---

## Interfaces Propuestas

### Inputs (lo que entra al Lab)

| Input | Origen | Clasificación | Estatus |
|-------|--------|--------------|---------|
| Market data (OHLCV, orderbook, trades) | Exchanges / proveedores de datos | Externo | EVIDENCE_REQUIRED — no se sabe qué fuentes usa. [Hecho] |
| Templates de investigación | LabOS | LabOS-Shared | VALIDATED — existen en Package 001. [Hecho] |
| Metodología de research | LabOS (Package 001) | LabOS-Shared | VALIDATED — Package 001 completado. [Hecho] |
| Arquitectura de conocimiento | LabOS (Package 002) | LabOS-Shared | VALIDATED — Package 002 completado. [Hecho] |
| Conocimiento de finanzas | Atlas Wealth Labs (potencial) | Cross-Lab | HYPOTHESIS — no hay evidencia de esta interacción. [Hipótesis] |

### Outputs (lo que sale del Lab)

| Output | Destino | Clasificación | Estatus |
|--------|---------|--------------|---------|
| Hallazgos de investigación (metodología genérica) | LabOS / otros Labs | Lab-Published (potencial) | HYPOTHESIS — no hay outputs producidos. [Hipótesis] |
| Frameworks de evaluación de estrategias | LabOS shared assets | Lab-Published (potencial) | HYPOTHESIS — no existe aún. [Hipótesis] |
| Datasets curados (si se anonimizan) | LabOS assets | Lab-Published (potencial) | HYPOTHESIS — no hay datasets. [Hipótesis] |
| Lecciones de gestión de riesgo | Ecosistema LabOS | Lab-Published (potencial) | HYPOTHESIS — conocimiento futuro. [Hipótesis] |

### Interfaces con LabOS Knowledge Architecture

| Interfaz | Dirección | Descripción |
|----------|-----------|-------------|
| KO Registration | Lab → LabOS | El Lab registra Knowledge Objects siguiendo el contrato de Package 002. [Decisión] |
| KO → Asset Handoff | Lab interno | El Lab puede convertir KOs en Assets per protocolo de handoff. [Decisión] |
| Asset Sharing | Lab → LabOS | Assets publicados explícitamente se comparten vía Asset_Sharing_Protocol. [Decisión] |

---

## Zonas de Sensibilidad Especial

| Zona | Nivel de sensibilidad | Motivo |
|------|----------------------|--------|
| Estrategias de trading (parámetros, reglas) | ALTA | Ventaja competitiva directa. Exposición = pérdida de edge. [Decisión] |
| Resultados de performance | ALTA | Información financiera privada del fundador. [Decisión] |
| Credenciales de exchanges | CRÍTICA | Acceso a fondos reales. NUNCA en repositorio. [Decisión] |
| Capital invertido / P&L | CRÍTICA | Información financiera personal. [Decisión] |
| Market data recolectado | MEDIA | Inversión de tiempo, pero reproducible por terceros. [Decisión] |
| Metodología genérica de evaluación | BAJA | Compartible sin riesgo competitivo. [Decisión] |

---

## Boundary con Atlas Wealth Labs

Existe potencial solapamiento con Atlas Wealth Labs (dominio: Finanzas). Delimitación propuesta: [Decisión]

| Aspecto | Crypto Scalping Core | Atlas Wealth Labs |
|---------|---------------------|-------------------|
| Enfoque | Trading activo algorítmico (corto plazo) | Análisis financiero, wealth management (largo plazo) |
| Instrumentos | Criptomonedas | Múltiples (acciones, ETFs, crypto, etc.) |
| Horizonte temporal | Segundos a minutos (scalping) | Meses a años |
| Tipo de decisión | Automatizada (algoritmo) | Informada (análisis para humano) |

La separación es clara por horizonte temporal y tipo de decisión. [Hecho] No hay solapamiento funcional actual. [Hecho]

---

## Validación del Boundary

| Criterio | Estatus | Nota |
|----------|---------|------|
| ¿Están documentadas las inclusiones? | VALIDATED | Confirmadas por el fundador (2025-07-23). [Hecho] |
| ¿Están documentadas las exclusiones? | VALIDATED | Confirmadas por el fundador, incluyendo exclusión corporativa absoluta. [Hecho] |
| ¿Se identifican las interfaces? | PARTIALLY_VALIDATED | Interfaces propuestas pero no verificadas contra repositorio real. [Hecho] |
| ¿Se clasifican las sensibilidades? | VALIDATED | Clasificación confirmada por el fundador. [Hecho] |
| ¿Se delimita vs. Labs similares? | VALIDATED | Delimitación vs. Atlas Wealth Labs documentada. [Hecho] |
| ¿Se confirma autonomía? | VALIDATED | CSC opera independientemente de LabOS. [Hecho] |
| ¿Se confirma modelo de ownership? | VALIDATED | Lab-Private por defecto, Lab-Published solo por autorización explícita. [Hecho] |
| ¿Se documentan restricciones de datos? | VALIDATED | Datasets externos restringidos hasta verificar licencia. [Hecho] |

---

## Cross-references

- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisiones que confirman estos boundaries
- [lab-boundaries.md](./lab-boundaries.md) — 4 clasificaciones de boundary canónicas
- [crypto-scalping-core-lab-profile.md](./crypto-scalping-core-lab-profile.md) — Perfil factual
- [crypto-scalping-core-readiness-assessment.md](./crypto-scalping-core-readiness-assessment.md) — Evaluación de readiness
- [Package 002 — knowledge-boundaries.md](../package-002-knowledge-architecture/knowledge-boundaries.md) — Boundaries de conocimiento
- [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md) — Compartibilidad de activos por tipo

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 24       | 36%        |
| [Hipótesis]   | 5        | 8%         |
| [Decisión]    | 37       | 56%        |
| [Visión]      | 0        | 0%         |

> **Nota**: Alto porcentaje de decisiones porque los boundaries son definiciones de ownership. Las hipótesis corresponden a outputs potenciales no realizados. Boundaries confirmados por el fundador el 2025-07-23.

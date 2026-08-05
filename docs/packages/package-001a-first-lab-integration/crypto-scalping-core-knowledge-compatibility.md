# Compatibilidad con Knowledge Architecture — Crypto Scalping Core

## Propósito

Este documento evalúa si Crypto Scalping Core es conceptualmente compatible con la arquitectura de conocimiento de LabOS (Package 002) para producir Knowledge Objects válidos. [Decisión] La evaluación es sobre compatibilidad de diseño, NO sobre producción actual de KOs (que no existe).

---

## Estado Actual de Knowledge Objects

| Aspecto | Valor |
|---------|-------|
| KOs producidos por el Lab | 0 [Hecho] |
| KOs en cualquier estado del lifecycle | 0 [Hecho] |
| Investigaciones documentadas que podrían generar KOs | 0 [Hecho] |
| Evidencia de actividad de síntesis de conocimiento | Ninguna en el workspace. [Hecho] |

---

## Compatibilidad por Diseño

### ¿El dominio puede producir los 6 tipos de Knowledge Object?

| Tipo de KO | ¿Aplicable a Trading Cuantitativo? | Ejemplo conceptual |
|------------|-------------------------------------|--------------------|
| `finding` | ✅ Sí | "El spread de BTC/USDT en Binance se ensancha 40% entre 02:00-04:00 UTC." [Hipótesis] |
| `methodology` | ✅ Sí | "Para evaluar una estrategia de scalping, usar backtest con slippage realista sobre ≥1000 trades simulados." [Hipótesis] |
| `decision-context` | ✅ Sí | "Los fees de maker en Binance (0.02%) vs Coinbase (0.05%) hacen que Binance sea preferible para scalping de baja frecuencia." [Hipótesis] |
| `market-insight` | ✅ Sí | "El volumen de BTC en horario asiático representa 35% del volumen diario — ventana de liquidez relevante." [Hipótesis] |
| `technical-insight` | ✅ Sí | "WebSocket de Binance desconecta tras 24h — requiere reconnection logic con backoff exponencial." [Hipótesis] |
| `operational` | ✅ Sí | "Ejecutar backtests durante fin de semana reduce contención por market data en tiempo real." [Hipótesis] |

**Resultado: 6/6 tipos aplicables.** [Hecho] El dominio de trading cuantitativo es naturalmente prolífico en generación de conocimiento sintetizable.

---

### ¿Los campos obligatorios del KO Contract son poblables?

| Campo KO | ¿Poblable por un Lab de trading? | Nota |
|----------|----------------------------------|------|
| `knowledge_id` | ✅ Sí | Formato KO-CSC-NNN. [Decisión] |
| `title` | ✅ Sí | Hallazgos de trading son titulables en ≤80 chars. |
| `summary` | ✅ Sí | Findings cuantitativos son autocontenidos por naturaleza. |
| `type` | ✅ Sí | Los 6 tipos son aplicables (ver arriba). |
| `domain` | ✅ Sí | "Crypto Scalping Core" — nombre canónico del Lab. |
| `confidence` | ✅ Sí | Trading cuantitativo produce confianza basada en datos (sample size, p-values, períodos). |
| `status` | ✅ Sí | Lifecycle estándar aplicable. |
| `source_reference` | ✅ Sí | Backtests, datasets y notebooks son referenciables. |
| `created_date` | ✅ Sí | Fechable. |
| `validity_window` | ✅ Sí — con nota | Mercados crypto cambian rápido → validity_window probablemente corto (30-90 días). [Hipótesis] |

**Resultado: 10/10 campos poblables.** [Hecho]

---

### ¿El dominio se beneficia de las capas de conocimiento?

| Capa | Aplicabilidad | Ejemplo |
|------|--------------|---------|
| Capa 1 — Capturado | ✅ Alta | Observaciones de market data, resultados preliminares de backtest. [Hipótesis] |
| Capa 2 — Validado | ✅ Alta | Hallazgos confirmados con datos de múltiples períodos/condiciones. [Hipótesis] |
| Capa 3 — Canónico | ✅ Moderada | Principios estables de microestructura que persisten entre condiciones de mercado. [Hipótesis] |

**Nota sobre Capa 3:** En trading cuantitativo, el conocimiento "canónico" es raro — los mercados cambian y las edge decaen. [Hipótesis] La mayoría del conocimiento operará en Capas 1-2 con validity_window corto.

---

### ¿El handoff KO → Asset es viable?

Evaluación contra mapping KO types → Asset types (per [knowledge-to-asset-handoff.md](../package-002-knowledge-architecture/knowledge-to-asset-handoff.md)):

| Tipo de KO | Asset natural resultante | Viabilidad |
|------------|-------------------------|------------|
| `finding` → | Dataset, Documento | ✅ Viable — findings cuantitativos se empaquetan bien en datasets curados o reportes. [Hipótesis] |
| `methodology` → | Framework, Playbook, Template | ✅ Viable — metodologías de evaluación de estrategias son reutilizables. [Hipótesis] |
| `decision-context` → | Documento | ✅ Viable — guías de decisión para selección de exchanges/pares. [Hipótesis] |
| `market-insight` → | Dataset, Documento | ✅ Viable — insights de mercado con datos de soporte. [Hipótesis] |
| `technical-insight` → | Herramienta, Documento | ✅ Viable — scripts y guías técnicas de infraestructura. [Hipótesis] |
| `operational` → | Playbook | ✅ Viable — procedimientos operativos estandarizados. [Hipótesis] |

**Resultado: Handoff viable para todos los tipos.** [Hecho]

---

## Consideraciones Específicas del Dominio

### Validity Window Corto

El dominio de trading cuantitativo tiene una particularidad: el conocimiento sobre condiciones de mercado caduca más rápido que en otros dominios. [Hipótesis]

| Tipo de conocimiento | Validity window estimado |
|---------------------|-------------------------|
| Condiciones de mercado actuales | 7-30 días [Hipótesis] |
| Comportamiento de exchanges | 30-90 días [Hipótesis] |
| Metodologías de evaluación | 180-365 días [Hipótesis] |
| Principios de microestructura | 90-180 días [Hipótesis] |

**Implicación:** El Lab probablemente producirá más KOs en Capa 1-2 con revalidación frecuente que KOs en Capa 3 de larga duración. [Hipótesis] Esto es compatible con la arquitectura — el framework no requiere durabilidad mínima.

### Sensibilidad del Conocimiento

La mayoría del conocimiento de trading tiene valor competitivo directo. [Decisión] Esto implica:

- La mayoría de KOs serán `lab-private` por defecto. [Decisión]
- KOs compartibles serían solo metodologías genéricas y observaciones no-actionables. [Decisión]
- El Lab generará poco conocimiento `labos-shared` comparado con Labs menos competitivos. [Hipótesis]

Esto es compatible — la arquitectura permite Labs con baja contribución al ecosistema compartido. [Hecho]

---

## Veredicto de Compatibilidad

### **COMPATIBLE POR DISEÑO — SIN EVIDENCIA OPERATIVA**

| Aspecto | Resultado |
|---------|-----------|
| Tipos de KO aplicables | 6/6 ✅ |
| Campos obligatorios poblables | 10/10 ✅ |
| Capas de conocimiento aplicables | 3/3 ✅ |
| Handoff KO → Asset viable | 6/6 ✅ |
| KOs producidos actualmente | 0 ❌ |
| Evidencia operativa de producción | Ninguna ❌ |

**Conclusión:** La arquitectura de conocimiento de Package 002 es plenamente compatible con un Lab de trading cuantitativo. [Hecho] No hay restricción de diseño que impida a Crypto Scalping Core producir KOs válidos. [Hecho] Sin embargo, la compatibilidad teórica no sustituye la producción real — hasta que el Lab esté en estado `explorando` y produzca su primer KO, esta evaluación es prospectiva. [Decisión]

---

## Cross-references

- [Package 002 — knowledge-object-contract.md](../package-002-knowledge-architecture/knowledge-object-contract.md) — Contrato de KO
- [Package 002 — knowledge-to-asset-handoff.md](../package-002-knowledge-architecture/knowledge-to-asset-handoff.md) — Protocolo de handoff
- [crypto-scalping-core-lab-profile.md](./crypto-scalping-core-lab-profile.md) — Perfil factual del Lab
- [crypto-scalping-core-asset-readiness.md](./crypto-scalping-core-asset-readiness.md) — Readiness de activos
- [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md) — Tipos de activos canónicos

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 12       | 30%        |
| [Hipótesis]   | 20       | 50%        |
| [Decisión]    | 8        | 20%        |
| [Visión]      | 0        | 0%         |

> **Nota**: Alto porcentaje de hipótesis porque este documento proyecta capacidades futuras basadas en el dominio. Los hechos son sobre el estado actual (no hay KOs) y sobre la compatibilidad estructural del framework. Las decisiones son sobre clasificación de sensitivity.

# Clasificación del Conocimiento

## Propósito

Este documento define los DOS ejes de clasificación de Knowledge Objects: tipo funcional y sensibilidad. [Decisión] Ambos ejes son independientes entre sí y de otras dimensiones (confianza, freshness, capa, estado del lifecycle).

---

## Eje A: Tipo de Knowledge Object (clasificación funcional)

### Los 6 tipos definidos

Referencia: campo `type` en [knowledge-object-contract.md](./knowledge-object-contract.md). [Hecho]

| Tipo | Definición | Ejemplo (EJEMPLO: Crypto Scalping Core) |
|------|-----------|----------------------------------------|
| `finding` | Hallazgo factual derivado de investigación o análisis. [Decisión] | "El spread BTC/USDT en Binance se ensancha 40-60% entre 02:00-04:00 UTC." |
| `methodology` | Método o proceso probado que puede reutilizarse. [Decisión] | "Para evaluar latencia, usar TCP ping al WebSocket endpoint desde 3 regiones." |
| `decision-context` | Contexto que informa una decisión sin ser la decisión misma. [Decisión] | "Fees de maker: Binance 0.02% vs Coinbase 0.05% — factor para elección de exchange." |
| `market-insight` | Comprensión sobre comportamiento de mercado o usuarios. [Decisión] | "70% del volumen crypto LATAM se concentra en BTC y ETH." |
| `technical-insight` | Comprensión técnica sobre herramientas o infraestructura. [Decisión] | "WebSocket de Binance desconecta tras 24h — requiere reconexión con backoff." |
| `operational` | Conocimiento de trabajo diario, observaciones repetidas. [Decisión] | "Los deploys de viernes generan 3x más incidentes." |

### Por qué 6 tipos son suficientes

Estos 6 tipos cubren TODO el espectro funcional del conocimiento producido en LabOS: [Decisión]

| Pregunta que responde | Tipo que la cubre |
|-----------------------|-------------------|
| ¿Qué descubrimos? | `finding` |
| ¿Cómo hacemos algo? | `methodology` |
| ¿Qué información informa una elección? | `decision-context` |
| ¿Qué entendemos del mercado/usuarios? | `market-insight` |
| ¿Qué sabemos de herramientas/infra? | `technical-insight` |
| ¿Qué observamos en operación diaria? | `operational` |

Si un Knowledge Object no encaja en ninguno de estos 6 tipos, probablemente no es conocimiento sino evidencia (Package 001) o una decisión formal (ADR). [Decisión]

### Diferenciación con otros sistemas de clasificación

Los 6 tipos funcionales son DISTINTOS de y no reemplazan: [Decisión]

| Sistema | Qué clasifica | Relación con tipos funcionales |
|---------|--------------|-------------------------------|
| **Clasificación epistémica** ([Hecho]/[Hipótesis]/[Visión]/[Decisión]) | Certeza y naturaleza de la afirmación. | Ortogonal. Un `finding` puede ser [Hecho] o [Hipótesis]. Una `methodology` puede ser [Decisión]. |
| **Estados del lifecycle** (captured, validated, canonical...) | Madurez y estado operativo del KO. | Ortogonal. Un `finding` puede estar en cualquier estado. |
| **Capas** (1-Capturado, 2-Validado, 3-Canónico) | Nivel de validación. | Ortogonal. Todos los tipos pueden existir en cualquier capa. |
| **Confianza** (alto/medio/bajo) | Cuán segura es la afirmación. | Ortogonal. Un `market-insight` puede tener confianza alta o baja. |

**Los 6 tipos responden: ¿PARA QUÉ sirve este conocimiento?** Las otras clasificaciones responden preguntas diferentes (¿cuán cierto? ¿cuán maduro? ¿cuán validado? ¿cuán confiable?). [Decisión]

---

## Eje B: Sensibilidad

### Modelo simplificado de 2 niveles (activo)

Per [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) y [knowledge-boundaries.md](./knowledge-boundaries.md), el modelo de sensibilidad activo es binario: [Decisión]

| Nivel | Definición | Quién accede | Default para |
|-------|-----------|-------------|--------------|
| **PRIVATE** | No compartible sin autorización explícita del fundador. [Decisión] | Solo el Lab propietario. | Lab-Private knowledge (per [knowledge-boundaries.md](./knowledge-boundaries.md)). |
| **PUBLIC** | Compartible sin restricción dentro del ecosistema LabOS. [Decisión] | Cualquier Lab/agente del ecosistema. | LabOS-Shared knowledge. |

### Regla por defecto

**Todo conocimiento es PRIVATE por defecto.** [Decisión] La publicación es un acto explícito (cambiar campo `sensitivity` + agregar summary ≤300 caracteres). Esta regla protege conocimiento sensible sin requerir clasificación explícita en cada captura — el fundador solo necesita actuar cuando QUIERE compartir.

### Reglas de acceso por nivel

| Nivel | Lectura | Modificación | Publicación |
|-------|---------|-------------|-------------|
| PRIVATE | Solo Lab propietario. | Solo Lab propietario. | Requiere decisión explícita del fundador para hacer PUBLIC. [Decisión] |
| PUBLIC | Cualquier Lab del ecosistema. | Solo Lab propietario o LabOS (si fue promovido). | Ya es público — referenciable libremente. [Decisión] |

### Restricciones de compartición

- Conocimiento PUBLIC puede ser referenciado libremente por cualquier Lab. [Decisión]
- Conocimiento PRIVATE requiere publicación explícita antes de ser referenciado por otro Lab. [Decisión]
- Referenciar ≠ copiar. Solo se referencia, nunca se duplica contenido (per Principio 2). [Decisión]

### Material externo con licencia

| Tipo de licencia | Clasificación resultante | Justificación |
|-----------------|------------------------|---------------|
| CC-BY, MIT, Apache | PUBLIC factible | Licencia permite redistribución. [Decisión] |
| Propietario, paywalled | PRIVATE obligatorio | Licencia prohíbe redistribución sin autorización. [Decisión] |
| CC-NC (No Commercial) | PRIVATE por defecto | Uso comercial potencial de LabOS requiere precaución. [Decisión] |

### Exclusiones absolutas (NO son Knowledge Objects)

| Tipo de información | Tratamiento | Referencia |
|--------------------|-------------|-----------|
| **Información personal** (datos personales del fundador) | NUNCA entra al sistema de KO. Siempre PRIVATE fuera del sistema. [Decisión] | Protección de privacidad personal. |
| **Credenciales y secretos** (API keys, passwords, tokens) | NO son Knowledge Objects. No se almacenan en documentos de conocimiento. [Decisión] | [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — definición de qué NO es un KO. |
| **Información corporativa/empleador** | NUNCA entra al LabOS personal. Invariante arquitectónica. [Decisión] | Información de SentinelOps, BYMA, NRTC o cualquier empleador está explícitamente excluida. |
| **Estrategia de negocio no publicada** | PRIVATE hasta decisión explícita de publicar por el fundador. [Decisión] | Protección de ventaja competitiva. |

---

## Modelo de 4 niveles (dormido — expansión futura)

El modelo binario se expandirá a 4 niveles cuando se active alguno de estos triggers: [Decisión]

| Trigger de activación |
|----------------------|
| Primer Lab que maneja datos de terceros. |
| Primer usuario externo al ecosistema. |
| Primera API pública expuesta. |

### Mapping de expansión

| Modelo actual | Modelo expandido | Cuándo aplica |
|---------------|-----------------|---------------|
| PUBLIC | PUBLIC | Conocimiento abierto, compartible sin restricción. |
| PRIVATE | INTERNAL | No sensible pero solo para consumo interno del ecosistema. |
| PRIVATE | CONFIDENTIAL | Sensible — acceso solo para Labs autorizados explícitamente. |
| PRIVATE | SECRET | Altamente sensible — acceso solo para el fundador/owner. |

**Hasta que se active un trigger, el modelo de 2 niveles prevalece.** [Decisión] La expansión no requiere migración de KOs existentes: todo lo PRIVATE se mapea a INTERNAL por defecto al activarse, con reclasificación manual solo para lo que requiera CONFIDENTIAL o SECRET.

---

## Matriz tipo × sensibilidad

Todos los tipos pueden tener cualquier nivel de sensibilidad. Algunas combinaciones son más comunes: [Hecho]

| Tipo | Más común como... | Razón |
|------|------------------|-------|
| `finding` | PRIVATE | Hallazgos suelen ser ventaja competitiva del Lab. |
| `methodology` | PUBLIC (tras validación) | Métodos suelen ser útiles cross-lab. |
| `decision-context` | PRIVATE | Contexto de decisiones suele ser sensible. |
| `market-insight` | PRIVATE | Insights de mercado son ventaja competitiva. |
| `technical-insight` | PUBLIC (frecuentemente) | Insights técnicos sobre tools públicas son compartibles. |
| `operational` | PRIVATE | Procesos operativos son específicos del Lab. |

Estas son tendencias, no reglas. [Hecho] El fundador decide la sensibilidad de cada KO individualmente.

---

## Ejemplo de clasificación completa

**(EJEMPLO: Crypto Scalping Core)**

```text
KO-CSC-017:
  type: finding
  sensitivity: lab-private (PRIVATE)
  
  Justificación de tipo: Es un hallazgo factual derivado de análisis
  de datos de mercado (no es una metodología ni un insight técnico).
  
  Justificación de sensibilidad: PRIVATE porque el timing específico
  de ensanchamiento de spread es ventaja competitiva directa para
  estrategias de scalping del Lab.

KO-CSC-025:
  type: methodology
  sensitivity: lab-published (PUBLIC)
  
  Justificación de tipo: Es un método reutilizable para evaluar
  latencia de exchanges.
  
  Justificación de sensibilidad: PUBLIC porque la metodología de
  medición de latencia es útil para Atlas Wealth Labs y no revela
  estrategias específicas del Lab.
```

---

## Cross-references

- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campos `type` y `sensitivity`
- [knowledge-boundaries.md](./knowledge-boundaries.md) — Boundaries Lab-Private, Lab-Published, LabOS-Shared
- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 7 (compartido por diseño, protegido por excepción)
- [knowledge-ownership.md](./knowledge-ownership.md) — Relación ownership↔sensibilidad
- [knowledge-layers.md](./knowledge-layers.md) — Capas como dimensión ortogonal
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Estados como dimensión ortogonal
- [knowledge-confidence-model.md](./knowledge-confidence-model.md) — Confianza como dimensión ortogonal
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Taxonomía, gobernanza SOLO
- [ADR-0001](../../decisions/0001-terminology-hierarchy.md) — Jerarquía terminológica

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 4        | 9%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 38       | 91%        |
| [Visión]      | 0        | 0%         |

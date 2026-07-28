# Modelo de Confianza del Conocimiento

## Propósito

Este documento define cómo se evalúa y asigna la confianza a Knowledge Objects. [Decisión] Se construye SOBRE la clasificación epistémica existente (Hecho/Hipótesis/Visión/Decisión) como dimensión ortogonal — no la reemplaza.

---

## Tipo epistémico vs confianza: dimensiones ortogonales

La clasificación epistémica y la confianza son dos ejes INDEPENDIENTES: [Decisión]

- **Tipo epistémico** = QUÉ clase de afirmación es (hecho, hipótesis, visión, decisión). [Hecho]
- **Confianza** = CUÁN CIERTOS estamos de que la afirmación es precisa. [Hecho]

Estas dimensiones son ortogonales porque: [Decisión]

- Un [Hecho] puede tener confianza BAJA si la verificación fue débil.
- Una [Hipótesis] puede tener confianza ALTA si hay evidencia fuerte que la soporta.
- Una [Decisión] puede tener confianza MEDIA si se tomó con información incompleta.
- Una [Visión] generalmente no requiere confianza (es aspiracional, no verificable).

### Ejemplos de la interacción tipo × confianza

| Tipo epistémico | Confianza | Ejemplo (EJEMPLO: Crypto Scalping Core) | Explicación |
|----------------|-----------|----------------------------------------|-------------|
| [Hecho] | BAJA | "El spread promedio en Binance es 0.02%" | Etiquetado como hecho pero basado en datos de solo 3 días — evidencia insuficiente para certeza. |
| [Hipótesis] | ALTA | "Estrategias de scalping <5m necesitan <50ms latencia para rentabilidad consistente" | Es hipótesis (no demostrada formalmente) pero la evidencia de 6 meses de operación la soporta fuertemente. |
| [Decisión] | MEDIA | "Usar Binance como exchange principal para scalping" | Decisión tomada con evidencia parcial sobre fees y liquidez, sin evaluar todas las alternativas. |
| [Visión] | N/A | "Ser el sistema de trading algorítmico más eficiente en LATAM" | La confianza no aplica a aspiraciones — no son verificables contra la realidad. |

---

## Niveles de confianza

| Nivel | Definición | Implicación operativa |
|-------|-----------|----------------------|
| **ALTO** | Múltiples fuentes independientes coinciden, evidencia reproducida, reciente, procedencia fuerte. [Decisión] | Se puede actuar directamente basándose en este KO. |
| **MEDIO** | 1-2 fuentes creíbles, parcialmente reproducido o analogizado, procedencia razonable. [Decisión] | Se puede usar para decisiones con consciencia de limitaciones. |
| **BAJO** | Fuente única, no reproducido, procedencia indirecta, o datos antiguos. [Decisión] | Usar con precaución. Priorizar validación antes de decisiones de alto impacto. |
| **UNKNOWN** | Recién capturado, no evaluado aún. [Decisión] | Requiere evaluación antes de uso operativo. Estado transitorio. |

**Nota sobre precisión:** No se usan porcentajes (e.g., "75% seguro") porque generan precisión ficticia. [Decisión] La diferencia entre "70% seguro" y "75% seguro" es indistinguible en la práctica. Los 3 niveles + UNKNOWN son suficientes para decisiones operativas de un fundador solo.

---

## Criterios de evaluación de confianza

Los siguientes criterios guían la asignación de confianza. No todos aplican a cada KO — se evalúan los relevantes: [Decisión]

| Criterio | ALTO | MEDIO | BAJO |
|----------|------|-------|------|
| **Calidad de fuentes** | Fuentes evaluadas y de alta calidad (per Package 001). | Fuentes creíbles pero no evaluadas formalmente. | Fuentes sin evaluar o de calidad desconocida. |
| **Cantidad de evidencia** | Múltiples fuentes independientes (≥3). | 1-2 fuentes que se complementan. | Fuente única sin corroboración. |
| **Consistencia** | Sin contradicciones conocidas con otro conocimiento del sistema. | Algunas tensiones menores pero no contradicciones directas. | Contradicciones activas o información conflictiva. |
| **Reproducibilidad** | Observación repetida en múltiples contextos o tiempos. | Observación repetida en un contexto o período limitado. | Observación única, no reproducida. |
| **Recencia** | Dentro de la ventana de validez, datos actuales. | Dentro de validez pero acercándose a expiración. | Fuera de ventana de validez o datos potencialmente obsoletos. |
| **Procedencia** | COMPLETE (ref: [knowledge-provenance.md](./knowledge-provenance.md)). | PARTIAL o INDIRECT con gaps documentados. | UNVERIFIED o BROKEN. |
| **Expertise del autor** | Experto en el dominio con track record. | Conocedor del tema pero sin expertise profunda. | Sin expertise demostrada en el dominio. |
| **Contradicciones activas** | Ninguna conocida. | Tensiones menores identificadas. | Disputas activas o evidencia contradictoria sin resolver. |

---

## Formato de registro de confianza

El campo `confidence` en el Knowledge Object Contract tiene dos componentes obligatorios: [Decisión]

```text
confidence:
  level: alto | medio | bajo | unknown
  justification: "≥1 oración explicando POR QUÉ se asignó este nivel"
```

La justificación es OBLIGATORIA. [Decisión] Un nivel sin justificación no es válido. La justificación debe ser honesta y falsificable — no una racionalización post-hoc.

Ejemplos de justificación válida:
- "Alto — basado en 30 días de datos cuantitativos de API, consistente con documentación oficial de Binance."
- "Medio — basado en 2 artículos de 2024 y experiencia personal limitada (3 trades)."
- "Bajo — fuente única (post de blog sin peer review), no reproducido."
- "Unknown — recién capturado, pendiente evaluación de fuentes."

Ejemplos de justificación INVÁLIDA:
- "Alto" (sin justificación).
- "Me parece correcto" (no es falsificable).
- "Muchas fuentes lo dicen" (no específica cuáles ni cuántas).

---

## Cuándo SUBIR confianza

La confianza se upgradea cuando nueva información FORTALECE la afirmación: [Decisión]

| Trigger | De → A | Condición |
|---------|--------|-----------|
| Nueva evidencia confirmatoria | BAJO → MEDIO | Segunda fuente independiente confirma la afirmación. |
| Reproducción en otro contexto | MEDIO → ALTO | La afirmación se verifica en contexto diferente al original. |
| Estabilidad temporal | MEDIO → ALTO | La afirmación se mantiene válida tras ≥2 ciclos de revisión sin cambio. |
| Procedencia mejorada | BAJO → MEDIO | Gaps de procedencia se llenan con fuentes verificadas. |
| Evaluación inicial completada | UNKNOWN → BAJO/MEDIO/ALTO | Primer assessment formal de confianza. |

---

## Cuándo BAJAR confianza

La confianza se downgradea cuando nueva información DEBILITA la afirmación: [Decisión]

| Trigger | De → A | Condición |
|---------|--------|-----------|
| Evidencia contradictoria | ALTO → MEDIO | Nueva evidencia parcialmente contradice sin invalidar completamente. |
| Fuente invalidada | MEDIO/ALTO → BAJO | Fuente original retractada, actualizada con datos opuestos, o desacreditada. |
| Ventana de validez expirada | Cualquier nivel | Freshness STALE o EXPIRED → flag para revisión y posible downgrade (ref: [knowledge-freshness.md](./knowledge-freshness.md)). |
| Procedencia rota | MEDIO/ALTO → BAJO | Fuente principal ya no es accesible y no hay alternativa. |
| Contradicción con KO de mayor confianza | MEDIO → BAJO | Otro KO con procedencia más fuerte afirma lo contrario. |

**Nota importante:** Expiración de freshness NO degrada confianza automáticamente. [Decisión] Solo la flag para revisión. Un KO STALE en un dominio estable (e.g., metodología) puede mantener confianza ALTA tras revisión. La freshness es sobre TIEMPO; la confianza es sobre calidad de EVIDENCIA. Ver relación detallada en [knowledge-freshness.md](./knowledge-freshness.md).

---

## Confianza por capa

| Capa | Confianza mínima esperada | Justificación |
|------|--------------------------|---------------|
| Capa 1 — Capturado | UNKNOWN o BAJO | Recién capturado, aún no evaluado. [Decisión] |
| Capa 2 — Validado | MEDIO o ALTO | La validación requiere confianza explícita con justificación sólida. [Decisión] |
| Capa 3 — Canónico | ALTO (sostenido) | Solo conocimiento de alta confianza merece status canónico. [Decisión] |

---

## Confianza y decisiones

La confianza informa cómo un KO debe usarse para tomar decisiones: [Decisión]

| Confianza | Uso en decisiones |
|-----------|------------------|
| ALTO | Se puede actuar directamente. Base para decisiones arquitectónicas o de inversión. |
| MEDIO | Se puede usar para decisiones operativas reversibles. Para decisiones de alto impacto, buscar confirmación adicional. |
| BAJO | Solo para exploración o como input para investigación adicional. No usar como base de decisiones irreversibles. |
| UNKNOWN | No usar para decisiones. Evaluar primero. |

---

## Proceso de evaluación (overhead mínimo)

Para mantener el overhead ≤5 minutos por KO (per [knowledge-object-contract.md](./knowledge-object-contract.md)): [Decisión]

1. Al capturar un KO: asignar nivel provisional (puede ser UNKNOWN). ~30 segundos.
2. Al validar (transición a Capa 2): evaluar 3-4 criterios relevantes + escribir justificación. ~2-3 minutos.
3. Al promover a canónico: verificar que confianza ALTO es sostenible + actualizar justificación si necesario. ~2 minutos.

No se requiere evaluar los 8 criterios para cada KO. [Decisión] Evaluar los que apliquen según el tipo y dominio del conocimiento.

---

## Cross-references

- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 3 (Confianza explícita)
- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campo `confidence` (nivel + justificación)
- [knowledge-provenance.md](./knowledge-provenance.md) — Procedencia como input a confianza
- [knowledge-freshness.md](./knowledge-freshness.md) — Relación freshness↔confianza
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Confianza como criterio de transición
- [knowledge-layers.md](./knowledge-layers.md) — Confianza mínima por capa
- [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md) — Confianza como criterio de resolución
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-01 (Clasificación epistémica universal)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 2        | 5%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 38       | 95%        |
| [Visión]      | 0        | 0%         |

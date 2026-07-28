# Principios de Arquitectura del Conocimiento

## Propósito

Este documento define los principios que gobiernan la gestión del conocimiento dentro de LabOS. [Decisión] Cada principio incluye: declaración, racional, indicador de cumplimiento y ejemplo de violación.

---

## Principio 1: Conocimiento es evidencia sintetizada, no datos crudos

**Declaración:** El conocimiento no es la acumulación de datos ni evidencia bruta. Es el resultado de sintetizar, contextualizar y validar evidencia para producir una afirmación útil con nivel de confianza asignado. [Decisión]

**Racional:** Sin este umbral, todo registro de investigación sería "conocimiento" y el concepto perdería valor discriminatorio. La síntesis fuerza al operador a extraer significado de los datos, no solo a almacenarlos.

**Indicador de cumplimiento:** Todo Knowledge Object tiene al menos una afirmación clasificada epistémicamente ([Hecho], [Hipótesis], [Decisión], [Visión]) con nivel de confianza (alto/medio/bajo) y referencia a la evidencia que la soporta.

**Ejemplo de violación:** Un fundador registra 15 enlaces a artículos sobre "market making en crypto" como Knowledge Object sin sintetizar qué aprendió, qué confianza tiene en cada hallazgo, ni qué conclusión se extrae del conjunto.

---

## Principio 2: Fuente única, referencia múltiple

**Declaración:** Cada pieza de conocimiento tiene exactamente un documento como fuente de verdad. Otros documentos que la necesiten deben referenciarla, nunca copiarla ni reformularla. [Decisión]

**Racional:** La duplicación de conocimiento crea divergencia silenciosa. Cuando se actualiza una copia pero no la otra, el sistema pierde integridad. La referencia preserva la trazabilidad y reduce overhead de mantenimiento — crítico para un operador solo.

**Indicador de cumplimiento:** No existen dos documentos en el ecosistema que afirmen la misma información sustantiva sin que uno sea una referencia explícita al otro.

**Ejemplo de violación:** El Lab Crypto Scalping Core documenta "el spread mínimo en Binance para BTC/USDT es 0.01%" en su research journal Y en un knowledge object separado, sin que uno referencie al otro. Seis meses después, Binance cambia el spread; solo uno se actualiza.

---

## Principio 3: Confianza explícita, nunca implícita

**Declaración:** Todo conocimiento debe declarar explícitamente su nivel de confianza y la base sobre la cual se asigna. Conocimiento sin confianza declarada se trata como no validado. [Decisión]

**Racional:** La confianza implícita produce decisiones basadas en certeza falsa. Un operador que consume conocimiento sin saber cuán confiable es puede sobre-invertir en una dirección soportada solo por hipótesis. Declarar confianza fuerza honestidad intelectual y permite priorizar validación.

**Indicador de cumplimiento:** Todo Knowledge Object tiene un campo `confidence` con valor alto/medio/bajo y una justificación de ≥1 oración que explica por qué se asignó ese nivel.

**Ejemplo de violación:** Un knowledge object afirma "las estrategias de scalping en timeframe 1m son más rentables que en 5m" sin indicar si esto es un hecho medido, una hipótesis de un paper, o una opinión leída en un foro.

---

## Principio 4: El conocimiento tiene fecha de caducidad

**Declaración:** Todo conocimiento tiene una ventana de validez implícita o explícita. Conocimiento no revisado dentro de su ventana se marca como potencialmente obsoleto y requiere revalidación antes de usarse para decisiones. [Decisión]

**Racional:** El conocimiento en dominios dinámicos (crypto, IA, mercados) se degrada rápidamente. Tratar conocimiento antiguo como vigente produce decisiones basadas en información superada. El costo de revalidar es menor que el costo de actuar sobre conocimiento obsoleto.

**Indicador de cumplimiento:** Todo Knowledge Object tiene un campo `validity_window` (en días) y la última fecha de revisión es verificable contra esa ventana.

**Ejemplo de violación:** Un knowledge object sobre "mejores exchanges para scalping" fue creado en enero 2024 con datos de diciembre 2023. En julio 2025, se usa para decidir en qué exchange operar sin verificar si las condiciones (fees, liquidez, latencia) siguen siendo válidas.

---

## Principio 5: Procedencia trazable

**Declaración:** Todo conocimiento debe tener una cadena de procedencia verificable que conecte la afirmación con la fuente original de la cual se derivó. Conocimiento sin procedencia es conocimiento sin credibilidad. [Decisión]

**Racional:** La trazabilidad permite auditar la calidad del conocimiento, detectar cuando una fuente es invalidada (y por tanto el conocimiento derivado de ella pierde soporte), y actualizar conocimiento cuando las fuentes evolucionan. Un solo operador necesita trazabilidad aún más que un equipo — porque no puede confiar en memoria humana a largo plazo.

**Indicador de cumplimiento:** Todo Knowledge Object referencia al menos una investigación (Research_ID) o fuente documentada que soporta su contenido.

**Ejemplo de violación:** Un knowledge object afirma "el volumen de negociación en LATAM crece 30% anual" sin indicar de qué reporte, investigación o fuente proviene ese dato.

---

## Principio 6: Proporcionalidad de esfuerzo

**Declaración:** El esfuerzo invertido en gestionar conocimiento debe ser proporcional al valor esperado de ese conocimiento. No se justifica el mismo rigor para conocimiento operativo temporal que para conocimiento canónico de larga vida. [Decisión]

**Racional:** INV-05 establece proporcionalidad de proceso a etapa. Aplicado a conocimiento: un operador solo con 20-25h/semana no puede dedicar tiempo significativo a catalogar cada insight. El sistema debe distinguir entre conocimiento de alto valor (que justifica rigor completo) y conocimiento operativo (que solo necesita registro mínimo).

**Indicador de cumplimiento:** El overhead mensual de gestión del conocimiento no excede 1-2 horas para el operador. El conocimiento con classification "operacional" requiere solo campos obligatorios mínimos.

**Ejemplo de violación:** Un fundador dedica 4 horas semanales manteniendo metadatos de conocimiento que solo se consulta una vez al mes. El costo de mantenimiento supera el valor de consulta.

---

## Principio 7: Conocimiento compartido por diseño, protegido por excepción

**Declaración:** El estado por defecto del conocimiento dentro de un Lab es Lab-Private. El conocimiento se publica al ecosistema solo cuando el Lab lo decide explícitamente. Pero el diseño del sistema debe facilitar la publicación, no dificultarla. [Decisión]

**Racional:** La privacidad por defecto protege conocimiento sensible (estrategias de trading, datos propietarios). Pero el valor del ecosistema LabOS crece cuando el conocimiento fluye entre Labs. El sistema debe hacer la publicación tan fácil como un cambio de clasificación — no una burocracia que disuada.

**Indicador de cumplimiento:** Publicar un knowledge object al ecosistema requiere cambiar un campo de visibilidad y agregar un resumen de ≤300 caracteres. No requiere reformateo ni aprobación formal en nivel SOLO.

**Ejemplo de violación:** Un fundador tiene conocimiento útil sobre "evaluación de APIs de exchanges" que beneficiaría al Lab Atlas Wealth Labs, pero no lo publica porque el proceso requiere reformatear el documento completo a un template diferente.

---

## Resumen de principios

| # | Principio | Palabras clave |
|---|-----------|---------------|
| 1 | Conocimiento es evidencia sintetizada | Síntesis, no acumulación |
| 2 | Fuente única, referencia múltiple | No duplicar, referenciar |
| 3 | Confianza explícita | Declarar nivel, justificar |
| 4 | Fecha de caducidad | Ventana de validez, revalidar |
| 5 | Procedencia trazable | Cadena a fuente original |
| 6 | Proporcionalidad de esfuerzo | Overhead ≤2h/mes |
| 7 | Compartido por diseño, protegido por excepción | Privado por defecto, fácil publicar |

---

## Trazabilidad a invariantes

| Principio | Invariante relacionada |
|-----------|----------------------|
| P2 (Fuente única) | INV-04 (Fuente de verdad única por concepto) |
| P3 (Confianza) | INV-01 (Clasificación epistémica universal) |
| P5 (Procedencia) | INV-06 (Documentation-first) |
| P6 (Proporcionalidad) | INV-05 (Proporcionalidad de proceso a etapa) |
| P7 (Compartido por diseño) | INV-04 (Fuente de verdad única) |

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 0        | 0%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 9        | 100%       |
| [Visión]      | 0        | 0%         |

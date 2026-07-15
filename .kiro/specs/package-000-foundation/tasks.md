# Implementation Plan: Package 000 — Foundation

## Overview

Plan de implementación para crear los 16 documentos fundacionales de LabOS en `docs/packages/package-000-foundation/`. Cada tarea produce uno o dos documentos siguiendo el DAG de dependencias definido en el diseño. Todas las tareas son documentales (markdown); no hay código, APIs ni infraestructura.

## Tasks

- [x] 1. Actualizar README del package
  - [x] 1.1 Expandir `docs/packages/package-000-foundation/README.md` con estructura completa
    - Reescribir el README existente para incluir las 4 secciones obligatorias: propósito (párrafo descriptivo), lista de los 16 documentos (número + archivo + descripción ≤120 chars), glosario del package (≥5 términos clave: Package, LabOS, Lab, Activo, Hipótesis, Hecho, Visión, Asset_First_Model, Revenue_Thesis, Portfolio_Model, Clasificación_Epistémica), y estado actual (`en progreso`)
    - Incluir tabla epistémica al final del documento
    - Verificar: H1 presente, ≥1 H2, ≥100 palabras prosa, glosario con ≥5 términos, lista completa de 16 docs con descripción ≤120 chars cada una
    - _Requirements: 17.1, 17.5, 18.1, 18.2, 18.3, 18.4_

- [x] 2. Crear visión y misión
  - [x] 2.1 Crear `docs/packages/package-000-foundation/001-company-vision.md`
    - Declaración de visión clasificada como [Visión], horizonte 3+ años, máximo 300 palabras
    - Sin superlativos ni promesas de mercado sin evidencia ("revolucionario", "disruptivo", "líder", "el mejor", "único")
    - Cross-link saliente a `002-mission.md` para diferenciación visión/misión
    - Tabla epistémica al final con conteo de [Hecho], [Hipótesis], [Visión]
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + ≤300 palabras + clasificación [Visión] + tabla epistémica + sin superlativos + cross-link a 002
    - _Requirements: 3.1, 3.3, 3.5, 2.1, 2.5, 18.3_

  - [x] 2.2 Crear `docs/packages/package-000-foundation/002-mission.md`
    - Declaración de misión clasificada como [Hecho], máximo 200 palabras, sin capacidades no implementadas
    - Incluir 1-3 indicadores de progreso a 90 días (nombre, línea base, valor objetivo, método de medición)
    - Cross-link saliente a `010-success-metrics.md`
    - Cross-link entrante desde `001-company-vision.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + ≤200 palabras + clasificación [Hecho] + 1-3 indicadores con 4 campos + tabla epistémica + distinguible de visión (presente operativo vs futuro aspiracional)
    - _Requirements: 3.2, 3.4, 3.5, 2.1, 2.5, 18.3_

- [x] 3. Crear problem statement y startup thesis
  - [x] 3.1 Crear `docs/packages/package-000-foundation/003-problem-statement.md`
    - Definir problema central con: (a) segmento de usuario (rol + contexto + tamaño mercado), (b) consecuencia observable (tiempo/dinero/oportunidad perdida), (c) ≥2 alternativas existentes identificadas por nombre con razón de insuficiencia
    - Clasificar existencia del problema como [Hecho] con fuente verificable o [Hipótesis] con plan de validación
    - Cross-link saliente a `004-startup-thesis.md` y `009-revenue-thesis.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + segmento específico (no genérico) + ≥2 alternativas nombradas + clasificación epistémica correcta + tabla epistémica
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 2.1, 2.5, 18.3_

  - [x] 3.2 Crear `docs/packages/package-000-foundation/004-startup-thesis.md`
    - Secciones obligatorias: etapa actual, composición del equipo, fuentes de financiamiento, modelo de operación
    - Atributos como [Hecho]: pre-revenue, pre-product, documentation-first
    - Aspiraciones futuras etiquetadas como [Visión] o [Hipótesis], diferenciadas visualmente del estado actual
    - Cross-link saliente a `007-company-model.md` y `014-assumptions.md`
    - Cross-link entrante desde `003-problem-statement.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + 4 secciones presentes + pre-revenue/pre-product/doc-first como [Hecho] + afirmaciones futuras como [Visión]/[Hipótesis] + no declara ingresos/empleados/inversión sin evidencia + tabla epistémica
    - _Requirements: 1.1, 1.2, 1.4, 1.5, 2.1, 2.3, 2.5, 18.3_

- [x] 4. Crear manifesto y operating principles
  - [x] 4.1 Crear `docs/packages/package-000-foundation/005-manifesto.md`
    - 3-10 declaraciones de principio, cada una con: principio en una oración + anti-patrón (comportamiento observable que viola el principio)
    - Si un principio no tiene anti-patrón, marcar con [INCOMPLETO] al inicio de la entrada
    - Cada principio debe describir comportamiento observable/medible (no lenguaje aspiracional sin criterio de verificación)
    - Cross-link saliente a `006-operating-principles.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + 3-10 principios + cada uno con anti-patrón + sin lenguaje aspiracional vacío + tabla epistémica
    - _Requirements: 5.1, 5.3, 5.4, 5.5, 2.1, 2.5, 18.3_

  - [x] 4.2 Crear `docs/packages/package-000-foundation/006-operating-principles.md`
    - 5-15 reglas operativas, cada una con: condición de aplicación + acción esperada + ejemplo concreto (situación, acción, resultado observable)
    - Incluir principio de prioridad de ingresos: actividades generadoras de ingreso > infraestructura sin ingreso en 90 días
    - Si una regla no tiene los 3 campos requeridos, marcar con [INCOMPLETO]
    - No prescribir acciones mutuamente excluyentes con 005-manifesto.md para la misma condición
    - Cross-link saliente a `008-business-model.md`; cross-link entrante desde `005-manifesto.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + 5-15 reglas con 3 campos c/u + principio de prioridad ingresos presente + sin contradicciones con 005 + tabla epistémica
    - _Requirements: 5.2, 5.3, 5.4, 14.3, 2.1, 2.5, 18.3_

- [x] 5. Crear company model y portfolio model
  - [x] 5.1 Crear `docs/packages/package-000-foundation/007-company-model.md`
    - Estructura organizativa explícita: 1 fundador operador, 0 empleados, sin inversión externa, sin contratos activos
    - Definir Asset_First_Model: investigación >4h produce ≥1 activo reutilizable
    - Taxonomía de 7 tipos de activos (documento, template, dataset, herramienta, componente, framework, playbook) con descripción ≤2 oraciones c/u
    - Criterio mínimo de activo: nombre (≤80 chars) + tipo + descripción (1-3 oraciones) + hipótesis de uso (usuario + contexto) + estado (borrador/validado/productizado)
    - Hipótesis de monetización por activo: segmento + formato entrega + modelo ingreso
    - Transiciones de estado: borrador→validado (revisión owner + campos completos), validado→productizado (evidencia uso real)
    - Nota de cierre si investigación no produce activo: motivo + lecciones ≤5 oraciones
    - Cross-links salientes a `008-business-model.md`, `012-portfolio-model.md`, `014-assumptions.md`
    - Cross-link entrante desde `004-startup-thesis.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + estructura org (1/0/sin/sin) + taxonomía 7 tipos + criterio mínimo 5 campos + transiciones 2 definidas + tabla epistémica
    - _Requirements: 1.3, 1.5, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 2.1, 2.5, 18.3_

  - [x] 5.2 Crear `docs/packages/package-000-foundation/012-portfolio-model.md`
    - Lista de labs con 5 campos: nombre, dominio, hipótesis de producto, estado actual, criterio de avance (evidencia observable)
    - Estados válidos: idea → explorando → validando → operando (secuencial) + pausado (desde cualquier estado)
    - Cada transición con criterio observable y verificable
    - Reglas de priorización: validación demanda primero > flujo caja inmediato > señal demanda más reciente
    - Si >5 labs activos simultáneo: justificación capacidad (horas semanales + asignación por lab)
    - Cross-link saliente a `013-risk-register.md`; cross-link entrante desde `007-company-model.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + labs con 5 campos + 5 estados con transiciones + reglas priorización + justificación capacidad si >5 activos + tabla epistémica
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 2.1, 2.5, 18.3_

- [x] 6. Crear business model y revenue thesis
  - [x] 6.1 Crear `docs/packages/package-000-foundation/008-business-model.md`
    - 3 etapas temporales: inmediato (0-30d), corto plazo (30-90d), mediano plazo (90-365d)
    - Cada mecanismo de monetización clasificado como [Hipótesis] con criterio de validación (métrica observable + valor objetivo numérico + fecha límite ≤ duración de etapa)
    - Etapa inmediata aparece primero con mayor peso de asignación de esfuerzo
    - ≥2 rutas de flujo de caja inmediato (<30 días) con campos: acción a ejecutar + recurso requerido (horas + presupuesto) + ingreso estimado (rango min-max) + plazo evaluación (≤30d) + criterio éxito/fracaso (métrica + umbral numérico)
    - ≥1 fuente de ingreso activable en <30d sin dependencias externas ni desarrollo de producto completo
    - Clasificación por tipo de flujo: caja inmediata / recurrencia / escalabilidad
    - Cross-links salientes a `009-revenue-thesis.md`, `014-assumptions.md`
    - Cross-links entrantes desde `007-company-model.md`, `006-operating-principles.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + 3 etapas + cada mecanismo [Hipótesis] + ≥2 rutas caja inmediata con 5 campos + ≥1 operador-único <30d + clasificación flujo + tabla epistémica
    - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5, 14.1, 14.2, 14.4, 14.5, 2.1, 2.2, 2.5, 18.3_

  - [x] 6.2 Crear `docs/packages/package-000-foundation/009-revenue-thesis.md`
    - Para cada fuente de ingreso: fuente + mecanismo captura de valor + precio (rango min-max) + segmento objetivo + criterio de validación (métrica observable)
    - Toda la Revenue_Thesis clasificada como [Hipótesis] hasta transacción real documentada
    - Precio justificado con ≥1 referencia de mercado (nombre fuente + fecha consulta) o evidencia de disposición a pagar
    - Experimento mínimo por fuente: acción concreta + métrica pass/fail con umbral numérico + plazo máximo ≤90d
    - Si menciona ingresos proyectados, calificar explícitamente como "hipótesis no validada"
    - Cross-links salientes a `010-success-metrics.md`, `014-assumptions.md`
    - Cross-links entrantes desde `008-business-model.md`, `003-problem-statement.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + toda sección [Hipótesis] + precios con referencia + experimento por fuente (3 campos) + sin proyecciones no calificadas + tabla epistémica
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5, 2.1, 2.2, 2.5, 18.3_

- [x] 7. Crear success metrics
  - [x] 7.1 Crear `docs/packages/package-000-foundation/010-success-metrics.md`
    - 3 categorías de métricas: package (entregables completados), operativas (30d), negocio (90d) con ≥2 métricas por categoría
    - Cada métrica con: nombre + definición operativa + método de medición + valor objetivo (numérico, porcentaje o binario) + frecuencia (semanal/quincenal/mensual) + línea base (valor actual o "0")
    - ≥1 métrica de salud del portfolio alineada con business-principles (activos generados, hipótesis documentadas, o validaciones en curso)
    - Sin valores objetivo genéricos ("mejorar", "aumentar", "optimizar") — todo cuantificado
    - Cross-link saliente a `016-foundation-review.md`
    - Cross-links entrantes desde `009-revenue-thesis.md`, `002-mission.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + 3 categorías con ≥2 c/u + 6 campos por métrica + ≥1 salud portfolio + sin objetivos genéricos + línea base en todas + tabla epistémica
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 2.1, 2.5, 18.3_

- [x] 8. Crear scope, boundaries y assumptions
  - [x] 8.1 Crear `docs/packages/package-000-foundation/011-scope-and-boundaries.md`
    - Sección "Alcance incluido" con ≥3 ítems
    - Sección "Exclusiones explícitas" con ≥5 ítems: no es SaaS, no tiene usuarios externos, no define arquitectura técnica final, no modifica otros packages, no promete liderazgo de mercado
    - Sección "Límites de propiedad intelectual" con 3 categorías exactas: propiedad exclusiva del fundador, open source, licenciable a terceros
    - Marcos regulatorios por jurisdicción: protección datos personales + PI + IA generativa
    - Obligación de privacidad para labs que manejen datos de terceros: regulación + tipo datos + obligaciones + acción
    - Política PI por origen: fundador / IA / terceros con derechos + restricciones + atribución
    - Límite temporal: "Package 000 — Foundation", expansión requiere documento decisión en `docs/decisions/`
    - Cross-link saliente a `013-risk-register.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + ≥3 incluidos + ≥5 exclusiones + 3 categorías PI + marcos regulatorios + política PI por origen + límite temporal + tabla epistémica
    - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 15.1, 15.2, 15.4, 15.5, 2.1, 2.5, 18.3_

  - [x] 8.2 Crear `docs/packages/package-000-foundation/014-assumptions.md`
    - Cada supuesto con: enunciado atómico + nivel confianza (alto/medio/bajo) + método validación (acción + métrica éxito) + horizonte temporal (≤90d) + referencia documento impactado ("utilizado en: NNN-nombre.md")
    - Criterios de confianza: alto = evidencia externa/dato cuantitativo, medio = experiencia directa/analogías, bajo = intuición/deseo
    - 4 categorías obligatorias: existencia demanda, disposición a pagar, capacidad fundador único, viabilidad asset-first
    - Supuestos con confianza "bajo" sin plan → etiqueta "🔴 Riesgo Abierto" + sección resumen de riesgos abiertos al final
    - Cross-link saliente a `016-foundation-review.md`
    - Cross-links entrantes desde `004-startup-thesis.md`, `008-business-model.md`, `009-revenue-thesis.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + supuestos con 5 campos + 4 categorías presentes + criterios confianza aplicados + 🔴 en los de baja sin plan + sección resumen riesgos abiertos + tabla epistémica
    - _Requirements: 13.1, 13.2, 13.3, 13.4, 13.5, 2.1, 2.5, 18.3_

- [x] 9. Crear risk register
  - [x] 9.1 Crear `docs/packages/package-000-foundation/013-risk-register.md`
    - Registro con ≥8 riesgos, cada uno con: descripción (≤200 chars) + probabilidad (alta/media/baja) + impacto (crítico/alto/medio/bajo) + categoría (operativo/financiero/legal/técnico/personal) + mitigación concreta ejecutable + owner (fundador por defecto)
    - Riesgos con probabilidad alta + impacto crítico/alto → marcados como prioritarios con plan de acción inmediato
    - Riesgos obligatorios: bus factor=1 (con ≥2 acciones mitigación), privacidad (≥2 riesgos datos en labs), PI (≥3: IA generativa + licencias terceros + titularidad), financiero (≥1: ausencia ingresos validados)
    - Riesgo uso IA en productos comercializables con estado legislación por jurisdicción + fecha última revisión
    - Frecuencia de revisión definida (mensual/trimestral/por evento) + fecha próxima revisión programada
    - Cross-link saliente a `016-foundation-review.md`
    - Cross-links entrantes desde `011-scope-and-boundaries.md`, `012-portfolio-model.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + ≥8 riesgos con 6 campos + bus factor + ≥2 privacidad + ≥3 PI + ≥1 financiero + frecuencia revisión + fecha próxima + tabla epistémica
    - _Requirements: 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 15.3, 15.5, 2.1, 2.5, 18.3_

- [x] 10. Crear package summary
  - [x] 10.1 Crear `docs/packages/package-000-foundation/015-package-summary.md`
    - Listar para cada documento del package las decisiones registradas (marcadas como "Decisión")
    - Declarar explícitamente que no existen contradicciones entre documentos, O identificar las contradicciones pendientes de resolución
    - Si hay contradicciones: identificar documentos y afirmaciones en conflicto
    - Cross-link saliente a `016-foundation-review.md`
    - Cross-links entrantes: todos los documentos del package (lee decisiones de cada uno)
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + lista decisiones por documento + declaración consistencia explícita + tabla epistémica
    - _Requirements: 17.3, 17.4, 2.1, 2.5, 18.3_

- [x] 11. Ejecutar revisión crítica
  - [x] 11.1 Crear `docs/packages/package-000-foundation/016-foundation-review.md`
    - Checklist de aprobación con ítems binarios (pasa/no pasa) y referencia al documento que lo evidencia
    - 6 criterios evaluados: (a) sin contradicciones inter-documento, (b) alcance explícito incluido/excluido, (c) portfolio completo con estado e hipótesis, (d) riesgos con mitigación viable, (e) revenue thesis falsificable ≤90d, (f) hipótesis con método de validación
    - Matriz de trazabilidad: vincular cada requisito (1-18) con documento específico + sección/párrafo que lo satisface
    - Proceso de revisión: auto-revisión del fundador con fecha + resultado por criterio + justificación de "no pasa"
    - Cross-links entrantes desde `015-package-summary.md`, `013-risk-register.md`, `014-assumptions.md`, `010-success-metrics.md`
    - Tabla epistémica al final
    - Verificar: H1 + ≥1 H2 + ≥100 palabras + checklist 6 criterios (a)-(f) con resultado binario + matriz trazabilidad 18 requisitos + proceso revisión definido + tabla epistémica
    - _Requirements: 16.1, 16.2, 16.3, 16.4, 16.5, 2.1, 2.5, 18.3_

- [x] 12. Verificación de cross-links y consistencia
  - [x] 12.1 Verificar cross-links entre todos los documentos del package
    - Recorrer cada documento y confirmar que todos los cross-links salientes/entrantes definidos en el diseño existen y apuntan a archivos reales con rutas relativas correctas (`./NNN-nombre.md`)
    - Verificar que no hay links rotos (archivos referenciados que no existen)
    - Verificar que las rutas relativas son correctas (dentro de `docs/packages/package-000-foundation/`)
    - Verificar que no se duplica contenido entre documentos (solo referencia, no copia)
    - Archivos a verificar: los 16 documentos + README.md
    - _Requirements: 17.1, 17.2, 17.4, 18.1_

  - [x] 12.2 Verificar consistencia terminológica
    - Confirmar que cada término del glosario (README.md) se usa con la misma grafía y significado en todos los documentos
    - Confirmar que términos de dominio en su primera mención incluyen referencia al glosario o definición local
    - Confirmar que no se introducen sinónimos para conceptos ya definidos
    - Si un documento introduce un término nuevo no en glosario → agregarlo al glosario de README.md
    - Archivos a verificar: README.md + los 15 documentos numerados
    - _Requirements: 17.1, 17.2, 17.5_

  - [x] 12.3 Verificar coherencia inter-documento
    - Confirmar que 005-manifesto.md y 006-operating-principles.md no prescriben acciones mutuamente excluyentes para la misma condición
    - Confirmar que la estructura organizativa en 004-startup-thesis.md y 007-company-model.md es consistente (mismo número personas, misma etapa)
    - Confirmar que las fuentes de ingreso en 008-business-model.md y 009-revenue-thesis.md son coherentes
    - Confirmar que los labs en 012-portfolio-model.md son consistentes con steering `portfolio-model.md`
    - Confirmar que métricas en 010-success-metrics.md se alinean con indicadores de 002-mission.md
    - Documentar contradicciones encontradas en 015-package-summary.md si existen
    - _Requirements: 5.3, 16.2(a), 16.4, 17.3, 17.4_

- [x] 13. Corregir inconsistencias encontradas
  - [x] 13.1 Resolver contradicciones detectadas en tarea 12
    - Para cada contradicción identificada: decidir cuál documento es source of truth (según tabla del diseño), actualizar el documento no-autoritativo para alinearlo
    - Si la contradicción requiere decisión no trivial: crear documento de decisión en `docs/decisions/` con formato `NNNN-titulo.md`
    - Actualizar 015-package-summary.md para reflejar resolución de contradicciones
    - Actualizar 016-foundation-review.md: marcar criterio (a) como "pasa" si se resolvieron todas, o documentar pendientes con justificación
    - Archivos potencialmente modificados: cualquier documento del package + `docs/decisions/` + `015-package-summary.md` + `016-foundation-review.md`
    - Verificar: 015 declara "sin contradicciones" o lista todas las resueltas + 016 criterio (a) con resultado
    - _Requirements: 16.4, 17.3, 17.4_

  - [x] 13.2 Completar campos faltantes detectados en validación
    - Si algún documento no cumple estructura mínima (H1 + H2 + ≥100 palabras): completar
    - Si alguna afirmación declarativa carece de clasificación epistémica: agregar [Hecho]/[Hipótesis]/[Visión]
    - Si alguna hipótesis con proyección no tiene criterio de validación: agregar métrica + umbral + plazo
    - Si algún documento no tiene tabla epistémica al final: agregar
    - Actualizar 016-foundation-review.md indicando archivos corregidos
    - Verificar: todos los 16 documentos pasan validación transversal (H1 + H2 + ≥100 palabras + tabla epistémica + clasificación completa)
    - _Requirements: 2.1, 2.2, 2.4, 2.5, 2.6, 18.3, 18.5_

- [x] 14. Actualizar índices raíz y marcar estado
  - [x] 14.1 Actualizar `docs/README.md`
    - Asegurar que la entrada de `package-000-foundation` refleja el estado actual del package
    - Verificar que el link al package directory es correcto: `packages/package-000-foundation/`
    - Verificar: entrada presente con descripción y estado actualizado
    - _Requirements: 18.1_

  - [x] 14.2 Actualizar `README.md` raíz del proyecto
    - Asegurar que la sección de documentación referencia correctamente el package 000
    - Verificar que no hay información desactualizada sobre el estado del package
    - Verificar: referencia al package presente y consistente con estado real
    - _Requirements: 18.1_

  - [x] 14.3 Marcar estado de aprobación en `docs/packages/package-000-foundation/README.md`
    - Si todos los criterios (a)-(f) en 016-foundation-review.md son "pasa": cambiar estado a `completo`
    - Si algún criterio es "no pasa": mantener estado `en progreso` y documentar qué falta
    - Actualizar la sección "Estado" del README del package
    - Verificar: estado coherente entre README del package y resultado de 016-foundation-review.md
    - _Requirements: 16.2, 18.2_

- [x] 15. Checkpoint final
  - Verificar que los 16 archivos existen en `docs/packages/package-000-foundation/` con nombres exactos según Requisito 18.1
  - Verificar que README.md del package tiene estado coherente con resultado de revisión
  - Verificar que no hay términos huérfanos (usados sin estar en glosario)
  - Verificar que la matriz de trazabilidad en 016 cubre los 18 requisitos
  - Preguntar al usuario si hay observaciones o si desea aprobar el package
  - Ensure all validations pass, ask the user if questions arise.

## Notes

- Este package es exclusivamente documental. No produce código, APIs, bases de datos ni infraestructura.
- Todos los documentos se crean en `docs/packages/package-000-foundation/`.
- Contenido en español, nombres de archivo en inglés kebab-case.
- Cada documento requiere: H1, ≥1 H2, ≥100 palabras prosa, tabla epistémica al final, toda afirmación clasificada [Hecho]/[Hipótesis]/[Visión].
- Cross-links entre documentos usan rutas relativas: `./NNN-nombre.md`.
- Source of truth por concepto según tabla del diseño — no duplicar contenido, solo referenciar.
- Property-based testing NO aplica (no hay código ejecutable).
- Tareas 12 y 13 son de verificación y corrección; pueden modificar cualquier documento previo.
- El package se considera aprobado solo cuando los 6 criterios (a)-(f) en 016-foundation-review.md son "pasa".

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["2.1"] },
    { "id": 2, "tasks": ["2.2"] },
    { "id": 3, "tasks": ["3.1"] },
    { "id": 4, "tasks": ["3.2"] },
    { "id": 5, "tasks": ["4.1"] },
    { "id": 6, "tasks": ["4.2"] },
    { "id": 7, "tasks": ["5.1"] },
    { "id": 8, "tasks": ["5.2", "6.1"] },
    { "id": 9, "tasks": ["6.2"] },
    { "id": 10, "tasks": ["7.1", "8.1"] },
    { "id": 11, "tasks": ["8.2", "9.1"] },
    { "id": 12, "tasks": ["10.1"] },
    { "id": 13, "tasks": ["11.1"] },
    { "id": 14, "tasks": ["12.1", "12.2", "12.3"] },
    { "id": 15, "tasks": ["13.1", "13.2"] },
    { "id": 16, "tasks": ["14.1", "14.2", "14.3"] }
  ]
}
```

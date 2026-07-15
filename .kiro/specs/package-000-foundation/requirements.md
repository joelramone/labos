# Requirements Document

## Introduction

Este documento define los requisitos para el Package 000 — Foundation de LabOS. El package establece la constitución inicial de LabOS como startup, su metodología y su sistema operativo para empresas de conocimiento asistidas por IA. Es exclusivamente documental: no produce código de aplicación.

El entregable es un conjunto de 16 documentos en `docs/packages/package-000-foundation/` que definen visión, misión, problema central, tesis de startup, principios operativos, modelo de empresa, modelo de negocio, tesis de ingresos, métricas, alcance, portfolio, riesgos, supuestos y criterios de aprobación.

## Glossary

- **Package**: Unidad discreta de trabajo con entregables concretos y criterios de aceptación.
- **LabOS**: Sistema operativo documental y metodológico para empresas de conocimiento asistidas por IA.
- **Lab**: Vertical de negocio independiente dentro del portafolio LabOS, con hipótesis de producto propia.
- **Activo**: Artefacto reutilizable producido por investigación o trabajo (documento, template, dataset, herramienta, componente).
- **Fundador**: Persona que opera LabOS en esta etapa inicial; único stakeholder con capacidad de decisión.
- **Hipótesis**: Suposición explícita que requiere validación con evidencia antes de tratarse como hecho.
- **Hecho**: Información verificada o verificable con evidencia existente.
- **Visión**: Aspiración a largo plazo, no comprometida ni garantizada.
- **Revenue_Thesis**: Modelo documentado que describe cómo y por qué se espera generar ingresos, clasificado como hipótesis hasta validación.
- **Asset_First_Model**: Enfoque donde toda investigación produce un activo reutilizable antes de considerar productización.
- **Portfolio_Model**: Estructura organizativa donde múltiples labs operan bajo infraestructura compartida de LabOS.
- **Package_Foundation**: Conjunto de 16 documentos que constituyen la definición fundacional de LabOS.
- **Clasificación_Epistémica**: Sistema de etiquetado que diferencia hechos, hipótesis, visiones y decisiones en cada documento.

## Requirements

### Requisito 1: Definición de LabOS como Startup

**User Story:** Como fundador, quiero una definición precisa y acotada de qué es LabOS hoy, para que cualquier stakeholder comprenda su naturaleza actual sin confundirla con una aspiración futura.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir un documento `004-startup-thesis.md` que defina LabOS como startup en etapa pre-revenue con un único fundador operador, incluyendo como mínimo las siguientes secciones: etapa actual, composición del equipo, fuentes de financiamiento y modelo de operación.
2. WHEN el documento `004-startup-thesis.md` es revisado, THE Package_Foundation SHALL contener una declaración que indique explícitamente cada uno de estos atributos de etapa actual: estado de ingresos (pre-revenue), estado de producto (pre-product) y enfoque operativo (documentación-first), cada uno clasificado con la etiqueta "Hecho" según los estándares de documentación.
3. THE Package_Foundation SHALL definir en `007-company-model.md` la estructura organizativa actual declarando explícitamente: número de personas involucradas (1 fundador operador), número de empleados (0), fuentes de inversión externa (ninguna) y relaciones contractuales activas (ninguna).
4. IF algún documento del package declara ingresos existentes, empleados contratados, inversión externa recibida, clientes activos o producto lanzado al mercado sin evidencia verificable que lo respalde, THEN THE Package_Foundation SHALL ser rechazado en revisión.
5. WHEN el documento `004-startup-thesis.md` o `007-company-model.md` incluye afirmaciones sobre estado futuro o aspiraciones, THE Package_Foundation SHALL clasificar dichas afirmaciones con la etiqueta "Visión" o "Hipótesis" según corresponda, diferenciándolas visualmente de las afirmaciones de estado actual.

---

### Requisito 2: Clasificación Epistémica de Contenido

**User Story:** Como fundador técnico, quiero que cada afirmación en el package esté clasificada como hecho, hipótesis o visión, para poder tomar decisiones informadas sobre qué requiere validación.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL etiquetar cada afirmación declarativa (enunciados sobre estado, capacidad, proyección o intención, excluyendo encabezados, etiquetas estructurales y metadatos) en todos los documentos con una Clasificación_Epistémica: `[Hecho]`, `[Hipótesis]` o `[Visión]`.
2. WHEN un documento contiene una proyección de ingresos, demanda o adopción, THE Package_Foundation SHALL clasificarla como `[Hipótesis]` e incluir un criterio de validación que especifique: la métrica observable a medir, el umbral de éxito o fracaso, y el plazo máximo de validación en días.
3. WHEN un documento describe el estado actual de LabOS, THE Package_Foundation SHALL clasificar esas afirmaciones como `[Hecho]` únicamente si la información es verificable contra una fuente observable (código existente en el repositorio, documento publicado, configuración desplegada o dato registrado con fecha).
4. IF un documento presenta una hipótesis sin etiquetar o la presenta como hecho, THEN THE Package_Foundation SHALL ser considerado no conforme con los estándares de documentación.
5. THE Package_Foundation SHALL incluir al final de cada documento una tabla resumen que indique la cantidad absoluta y el porcentaje de afirmaciones clasificadas como `[Hecho]`, `[Hipótesis]` y `[Visión]` respectivamente.
6. IF una afirmación no puede clasificarse inequívocamente como `[Hecho]` por ausencia de fuente verificable, THEN THE Package_Foundation SHALL clasificarla como `[Hipótesis]` hasta que se documente la evidencia que la respalde.

---

### Requisito 3: Visión y Misión

**User Story:** Como fundador, quiero documentar la visión y misión de LabOS de forma que sean distinguibles, medibles en progreso y no contengan promesas de mercado sin evidencia.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `001-company-vision.md` con una declaración de visión clasificada como `[Visión]` que describa un estado futuro aspiracional en un horizonte de 3 años o más, con una extensión máxima de 300 palabras.
2. THE Package_Foundation SHALL producir `002-mission.md` con una declaración de misión clasificada como `[Hecho]` que describa la intención operativa actual del sistema sin referir capacidades no implementadas ni resultados no obtenidos, con una extensión máxima de 200 palabras.
3. WHEN la visión o la misión son documentadas, THE Package_Foundation SHALL verificar que el texto no contiene afirmaciones de liderazgo de mercado, dominancia, inevitabilidad ni superlativos sin evidencia (e.g., "revolucionario", "disruptivo", "líder", "el mejor", "único en el mercado").
4. THE Package_Foundation SHALL incluir en `002-mission.md` entre 1 y 3 indicadores de progreso hacia la misión en un horizonte de 90 días, donde cada indicador especifica: nombre de la métrica, valor actual o línea base, valor objetivo, y método de medición.
5. WHEN ambos documentos están producidos, THE Package_Foundation SHALL garantizar que la visión y la misión son distinguibles: la visión describe exclusivamente un estado futuro aspiracional no comprometido, y la misión describe exclusivamente la intención operativa verificable en el presente.

---

### Requisito 4: Problema Central

**User Story:** Como inversionista pre-seed evaluando la tesis, quiero entender qué problema resuelve LabOS con suficiente especificidad para evaluar si existe demanda real.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `003-problem-statement.md` que describa el problema central incluyendo: (a) quién lo tiene, definido como al menos un segmento de usuario con rol y contexto operativo, (b) qué pierde, expresado en al menos una consecuencia observable (tiempo, dinero, oportunidad perdida, o conocimiento no capitalizado), y (c) por qué al menos 2 alternativas actuales identificadas por nombre no lo resuelven para ese segmento.
2. WHEN el problema es documentado, THE Package_Foundation SHALL identificar al menos un segmento de usuario definido por rol profesional, contexto de trabajo y tamaño aproximado de mercado (orden de magnitud), de modo que no pueda confundirse con una categoría genérica como "empresas" o "profesionales".
3. IF existe evidencia propia (experimento realizado, dato recolectado) o de terceros (fuente publicada con autor, fecha y URL o referencia verificable) que respalde la existencia del problema, THEN THE Package_Foundation SHALL clasificar la existencia del problema como `[Hecho]` citando al menos una fuente; de lo contrario SHALL clasificarla como `[Hipótesis]` indicando qué validación se requiere para promoverla a `[Hecho]`.
4. IF el documento `003-problem-statement.md` describe el problema sin mencionar al menos 2 alternativas existentes (herramientas, procesos o soluciones) que el segmento identificado ya utiliza, incluyendo por qué cada una resulta insuficiente, THEN THE Package_Foundation SHALL ser considerado incompleto y no podrá avanzar a estado "terminado" en el tracking del package.

---

### Requisito 5: Manifiesto y Principios Operativos

**User Story:** Como operador de startup, quiero principios operativos concretos y accionables que guíen decisiones diarias sin ser aspiracionales vacíos.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `005-manifesto.md` con un mínimo de 3 y un máximo de 10 declaraciones de principio, donde cada declaración incluya: el principio en una oración, y un anti-patrón asociado que describa un comportamiento observable que viola el principio.
2. THE Package_Foundation SHALL producir `006-operating-principles.md` con un mínimo de 5 y un máximo de 15 reglas operativas, donde cada regla incluya: condición de aplicación (situación concreta en la que aplica), acción esperada (qué debe hacer el operador), y ejemplo concreto (escenario con situación, acción tomada y resultado observable).
3. WHEN un principio operativo es definido, THE Package_Foundation SHALL verificar que no prescriba una acción mutuamente excluyente con otro principio para la misma condición, tanto dentro de `005-manifesto.md` y `006-operating-principles.md` como entre ambos documentos.
4. IF un principio en `005-manifesto.md` no tiene un anti-patrón asociado, o una regla en `006-operating-principles.md` no tiene los tres campos requeridos (condición de aplicación, acción esperada, ejemplo concreto), THEN THE Package_Foundation SHALL incluir la etiqueta `[INCOMPLETO]` visible al inicio de la entrada correspondiente.
5. IF una declaración de principio en `005-manifesto.md` no describe un comportamiento observable o medible y en su lugar usa lenguaje aspiracional sin criterio de verificación, THEN THE Package_Foundation SHALL rechazar la declaración hasta que se reformule con un anti-patrón que permita identificar una violación concreta.

---

### Requisito 6: Modelo de Negocio por Etapas

**User Story:** Como fundador con urgencia de flujo de caja, quiero un modelo de negocio que priorice la generación de ingresos inmediatos mientras construye activos de largo plazo.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `008-business-model.md` que defina al menos tres etapas temporales con mecanismo de monetización diferenciado: inmediato (0-30 días), corto plazo (30-90 días) y mediano plazo (90-365 días).
2. WHEN una etapa del modelo de negocio es documentada, THE Package_Foundation SHALL clasificar cada mecanismo de monetización como `[Hipótesis]` y asociarlo a un criterio de validación que incluya: métrica observable, valor objetivo numérico y fecha límite de evaluación no mayor a la duración de la etapa correspondiente.
3. WHILE Package_Foundation se encuentra en etapa pre-revenue, THE Package_Foundation SHALL documentar en `008-business-model.md` la prioridad de flujo de caja inmediato sobre ingreso recurrente futuro mediante un ordenamiento explícito donde los mecanismos de la etapa inmediata (0-30 días) aparezcan primero y con mayor peso de asignación de esfuerzo.
4. IF el modelo de negocio no incluye al menos una fuente de ingreso activable en menos de 30 días sin requerir desarrollo de producto completo ni dependencias de terceros no controlables, THEN THE Package_Foundation SHALL ser considerado incompleto para aprobación.
5. WHEN una etapa del modelo de negocio es documentada, THE Package_Foundation SHALL incluir al menos un mecanismo de monetización por etapa, clasificado según tipo de flujo: caja inmediata, recurrencia o escalabilidad.

---

### Requisito 7: Revenue Thesis

**User Story:** Como fundador y potencial inversionista, quiero una tesis de ingresos que sea verificable, con métricas claras y sin asumir validación inexistente.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `009-revenue-thesis.md` que documente la Revenue_Thesis con, para cada fuente de ingreso propuesta: fuente de ingreso, mecanismo de captura de valor, precio estimado expresado como rango (mínimo y máximo), segmento objetivo y criterio de validación con métrica observable.
2. THE Package_Foundation SHALL clasificar toda la Revenue_Thesis como `[Hipótesis]` hasta que exista al menos una transacción real documentada con fecha, monto, segmento del cliente y fuente de ingreso asociada.
3. WHEN la Revenue_Thesis describe un precio, THE Package_Foundation SHALL justificar el rango con al menos 1 referencia identificable a mercado comparable (con nombre de fuente y fecha de consulta) o evidencia de disposición a pagar estimada (encuesta, entrevista o benchmark público), no con cifras sin respaldo.
4. IF la Revenue_Thesis menciona ingresos proyectados sin calificarlos explícitamente como hipótesis no validada, THEN THE Package_Foundation SHALL ser rechazado.
5. THE Package_Foundation SHALL documentar en `009-revenue-thesis.md` el experimento mínimo para validar cada fuente de ingreso propuesta, incluyendo: acción concreta a ejecutar, métrica de éxito con umbral numérico de pass/fail, y plazo máximo de ejecución no mayor a 90 días.

---

### Requisito 8: Asset-First Model

**User Story:** Como product manager, quiero que el modelo asset-first esté definido con suficiente claridad para que cualquier investigación tenga un entregable reutilizable concreto.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL definir en `007-company-model.md` el Asset_First_Model: toda investigación (definida como cualquier actividad exploratoria con duración mayor a 4 horas acumuladas) produce al menos un activo reutilizable documentado.
2. WHEN el Asset_First_Model es documentado, THE Package_Foundation SHALL incluir una taxonomía de tipos de activos válidos (documento, template, dataset, herramienta, componente, framework, playbook) con una descripción de no más de 2 oraciones por tipo que permita clasificar sin ambigüedad.
3. THE Package_Foundation SHALL definir el criterio mínimo para que un artefacto califique como activo: nombre (máximo 80 caracteres), tipo (uno de la taxonomía definida), descripción (entre 1 y 3 oraciones indicando qué problema resuelve), hipótesis de uso (indicando al menos un usuario objetivo y un contexto de aplicación) y estado (borrador, validado, productizado).
4. IF un activo no tiene hipótesis de monetización documentada (que incluya al menos: segmento objetivo, formato de entrega propuesto y modelo de ingreso candidato), THEN THE Package_Foundation SHALL clasificar ese activo como incompleto para efectos de portfolio.
5. THE Package_Foundation SHALL definir las condiciones de transición entre estados del activo: de borrador a validado (requiere al menos una revisión por el owner y confirmación de que cumple los campos mínimos del criterio 3), y de validado a productizado (requiere evidencia de al menos un uso real o prueba con usuario objetivo).
6. IF una investigación concluye sin producir un artefacto que cumpla los criterios mínimos del activo, THEN THE Package_Foundation SHALL requerir el registro de una nota de cierre que documente el motivo y las lecciones aprendidas en no más de 5 oraciones.

---

### Requisito 9: Portfolio Model

**User Story:** Como operador de portafolio, quiero una estructura clara que defina cómo se organizan los labs, sus estados posibles y las reglas de priorización entre ellos.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `012-portfolio-model.md` que documente el Portfolio_Model con: lista de labs, estado actual de cada uno, y regla de transición entre estados.
2. WHEN un lab es incluido en el portfolio, THE Package_Foundation SHALL documentar: nombre, dominio, hipótesis de producto, estado actual y criterio para avanzar al siguiente estado, donde el criterio de avance incluye al menos un tipo de evidencia observable requerida.
3. THE Package_Foundation SHALL definir los estados válidos de un lab: `idea`, `explorando`, `validando`, `operando`, `pausado`, donde las transiciones son secuenciales (idea → explorando → validando → operando) con excepción de `pausado` que puede alcanzarse desde cualquier estado, y cada transición tiene al menos un criterio observable y verificable.
4. THE Package_Foundation SHALL documentar las reglas de priorización: labs con validación de demanda primero; labs con flujo de caja inmediato antes que labs de largo plazo. WHEN dos labs tienen el mismo nivel de validación, THE Package_Foundation SHALL priorizar aquel con señal de demanda más reciente.
5. IF el portfolio documenta más de 5 labs en estado activo (definido como `explorando`, `validando` u `operando`) simultáneo, THEN THE Package_Foundation SHALL incluir una justificación que indique la capacidad disponible del fundador único en horas semanales y la asignación estimada por lab.

---

### Requisito 10: Métricas de Éxito

**User Story:** Como fundador técnico, quiero métricas específicas y medibles para evaluar si el Package 000 cumplió su propósito y si LabOS avanza en la dirección correcta.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `010-success-metrics.md` con métricas organizadas en tres categorías: métricas del package (entregables completados), métricas operativas (evaluadas a 30 días) y métricas de negocio (evaluadas a 90 días), con un mínimo de 2 métricas por categoría.
2. WHEN una métrica es definida, THE Package_Foundation SHALL especificar: nombre, definición operativa (descripción de qué se observa y cómo se determina cumplimiento), método de medición (herramienta o proceso usado para obtener el dato), valor objetivo expresado como umbral numérico, porcentaje o condición binaria (sí/no), y frecuencia de revisión (semanal, quincenal o mensual).
3. THE Package_Foundation SHALL incluir al menos una métrica de salud del portfolio alineada con las definidas en business-principles: activos generados, hipótesis con monetización documentada, o validaciones en curso.
4. IF una métrica tiene un valor objetivo no cuantificado numéricamente o sin umbral específico (e.g., "mejorar", "aumentar", "optimizar"), THEN THE Package_Foundation SHALL marcarla como no conforme y excluirla del documento hasta que se reformule con un valor objetivo medible.
5. WHEN una métrica operativa o de negocio es definida, THE Package_Foundation SHALL incluir un valor de línea base (valor actual o "0" si no existe dato previo) contra el cual se medirá el progreso hacia el valor objetivo.

---

### Requisito 11: Alcance y Límites

**User Story:** Como responsable de riesgos, quiero límites explícitos que eviten scope creep y comprometan solo lo que es alcanzable con los recursos actuales.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `011-scope-and-boundaries.md` que contenga como mínimo tres secciones: "Alcance incluido" con al menos 3 items, "Exclusiones explícitas" con al menos 5 items, y "Límites de propiedad intelectual".
2. THE Package_Foundation SHALL documentar en la sección "Exclusiones explícitas" de `011-scope-and-boundaries.md` al menos 5 exclusiones: no es SaaS todavía, no tiene usuarios externos, no define arquitectura técnica final, no modifica otros packages, no promete liderazgo de mercado.
3. IF el contenido de `011-scope-and-boundaries.md` aborda manejo de datos personales, propiedad intelectual de terceros o licenciamiento, THEN THE Package_Foundation SHALL incluir una referencia a la jurisdicción aplicable para cada límite regulatorio identificado.
4. THE Package_Foundation SHALL definir en `011-scope-and-boundaries.md` los límites de propiedad intelectual clasificando cada tipo de activo en exactamente una de tres categorías: propiedad exclusiva del fundador, open source, o licenciable a terceros.
5. IF el documento `011-scope-and-boundaries.md` no incluye la sección "Exclusiones explícitas" con al menos 5 items o no incluye la sección "Alcance incluido" con al menos 3 items, THEN THE Package_Foundation SHALL ser considerado incompleto y no podrá avanzar a revisión de cierre del package.
6. THE Package_Foundation SHALL definir en `011-scope-and-boundaries.md` el límite temporal del alcance como "Package 000 — Foundation" e indicar que cualquier expansión de alcance requiere un documento de decisión separado en `docs/decisions/`.

---

### Requisito 12: Gestión de Riesgos

**User Story:** Como responsable de riesgos y fundador, quiero un registro de riesgos que identifique las amenazas críticas para la supervivencia del proyecto, incluyendo dependencia del fundador.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `013-risk-register.md` con un registro de al menos 8 riesgos clasificados por: probabilidad (alta/media/baja), impacto (crítico/alto/medio/bajo) y categoría (operativo, financiero, legal, técnico, personal), donde cada combinación de probabilidad alta e impacto crítico o alto se marca como riesgo prioritario que requiere plan de acción inmediato.
2. WHEN un riesgo es documentado, THE Package_Foundation SHALL incluir: descripción del riesgo en máximo 200 caracteres, probabilidad, impacto, categoría, al menos una acción de mitigación concreta y ejecutable por el owner (no una reafirmación del riesgo ni una intención genérica), y owner asignado (fundador por defecto).
3. THE Package_Foundation SHALL incluir como riesgo explícito la dependencia del fundador único (bus factor = 1) con estrategia de mitigación documentada que incluya al menos 2 acciones concretas (por ejemplo: documentación de procesos críticos, identificación de roles delegables, o plan de contingencia temporal).
4. THE Package_Foundation SHALL documentar al menos 2 riesgos de privacidad asociados al manejo de datos en los labs del portfolio que procesen información de usuarios o datos personales.
5. THE Package_Foundation SHALL documentar al menos 3 riesgos de propiedad intelectual cubriendo como mínimo: uso de herramientas de IA para generación de contenido, licencias de terceros incorporadas en activos, y titularidad del contenido generado con asistencia de IA.
6. IF el registro de riesgos no incluye al menos un riesgo financiero relacionado con la ausencia de ingresos validados, THEN THE Package_Foundation SHALL ser considerado incompleto.
7. THE Package_Foundation SHALL incluir en el registro de riesgos una frecuencia de revisión definida (mensual, trimestral o por evento) y una fecha de próxima revisión programada.

---

### Requisito 13: Supuestos y Dependencias

**User Story:** Como inversionista pre-seed, quiero ver explícitamente qué supone el fundador que es verdad sin haberlo validado, para evaluar el riesgo de la tesis.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `014-assumptions.md` que liste los supuestos fundacionales del proyecto, cada uno con: enunciado atómico del supuesto, nivel de confianza (alto/medio/bajo), método de validación propuesto describiendo la acción concreta y la métrica de éxito, y horizonte temporal de validación expresado en días (máximo 90 días).
2. WHEN un supuesto es documentado, THE Package_Foundation SHALL incluir una referencia explícita al nombre del documento del package donde ese supuesto se utiliza o impacta (e.g., "utilizado en: 008-business-model.md").
3. THE Package_Foundation SHALL incluir al menos un supuesto documentado para cada una de las siguientes categorías obligatorias: existencia de demanda, disposición a pagar, capacidad del fundador único, y viabilidad del modelo asset-first.
4. IF un supuesto con nivel de confianza "bajo" no tiene un plan de validación con horizonte temporal definido, THEN THE Package_Foundation SHALL marcarlo con la etiqueta "🔴 Riesgo Abierto" visible en el documento e incluirlo en una sección resumen de riesgos abiertos al final del archivo.
5. THE Package_Foundation SHALL asignar el nivel de confianza de cada supuesto según los siguientes criterios: "alto" si existe evidencia externa verificable o dato cuantitativo que lo respalde, "medio" si se basa en experiencia directa del fundador o analogías documentadas, "bajo" si no tiene respaldo más allá de intuición o deseo.

---

### Requisito 14: Generación Urgente de Flujo de Caja

**User Story:** Como fundador sin runway externo, quiero que el package priorice explícitamente las rutas más rápidas hacia el primer ingreso documentándolas como acción inmediata.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL documentar en `008-business-model.md` al menos dos rutas para generar flujo de caja en menos de 30 días, clasificadas como `[Hipótesis]`, donde cada ruta se considera documentada si contiene todos los campos requeridos por el criterio 2.
2. WHEN una ruta de flujo de caja inmediato es documentada, THE Package_Foundation SHALL incluir: acción a ejecutar (describiendo la actividad y el entregable resultante), recurso requerido (expresado en horas de dedicación y presupuesto monetario si aplica), ingreso estimado (rango mínimo-máximo en moneda local), plazo de evaluación (máximo 30 días calendario desde inicio de ejecución), y criterio de éxito/fracaso (métrica observable con umbral numérico que determine si la ruta se valida o se descarta al cumplirse el plazo).
3. THE Package_Foundation SHALL establecer en `006-operating-principles.md` un principio operativo que nombre las actividades generadoras de ingreso como prioridad superior a las actividades de infraestructura que no contribuyen directamente a generar ingresos en los próximos 90 días.
4. IF el package no documenta al menos una acción generadora de ingreso que un solo operador pueda iniciar en menos de 30 días con los recursos declarados como disponibles en el propio documento, THEN THE Package_Foundation SHALL ser considerado incompleto para la etapa actual.
5. WHEN una ruta de flujo de caja es documentada, THE Package_Foundation SHALL clasificarla en una de las siguientes categorías de flujo: servicios/consulting (pagan hoy), suscripciones/membresías (pagan mensualmente), o productos digitales/licencias (escalan sin esfuerzo lineal).

---

### Requisito 15: Límites Regulatorios y Privacidad

**User Story:** Como responsable de riesgos, quiero que los límites regulatorios relevantes estén documentados antes de que cualquier lab maneje datos de terceros o genere propiedad intelectual derivada.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL documentar en `011-scope-and-boundaries.md` los marcos regulatorios aplicables según jurisdicción del fundador y mercados objetivo potenciales, incluyendo como mínimo: protección de datos personales, propiedad intelectual, y uso de IA generativa para cada jurisdicción identificada.
2. IF un lab del portfolio maneja o declara intención de manejar datos de terceros (datos personales, datos comerciales con licencia, o contenido con derechos de autor), THEN THE Package_Foundation SHALL documentar en `011-scope-and-boundaries.md` la obligación de privacidad correspondiente, especificando: regulación aplicable, tipo de datos afectados, obligaciones del responsable, y acción de cumplimiento requerida antes de que el lab procese dichos datos.
3. THE Package_Foundation SHALL documentar en `013-risk-register.md` el riesgo de uso de contenido generado por IA en productos comercializables, incluyendo estado de la legislación aplicable en cada jurisdicción documentada en el criterio 1, con fecha de última revisión.
4. THE Package_Foundation SHALL definir en `011-scope-and-boundaries.md` la política de propiedad intelectual clasificando cada activo en una de tres categorías (producido por el fundador, generado por IA, derivado de fuentes de terceros) y documentando para cada categoría: derechos de uso, restricciones de comercialización, y requisitos de atribución.
5. WHEN la fecha de última revisión de la documentación regulatoria en `011-scope-and-boundaries.md` o `013-risk-register.md` supera 90 días, THE Package_Foundation SHALL marcar la sección como pendiente de actualización.

---

### Requisito 16: Criterios de Aprobación del Package

**User Story:** Como fundador y revisor, quiero criterios de aprobación objetivos que permitan determinar sin ambigüedad si el Package 000 está completo y es internamente consistente.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir `016-foundation-review.md` que defina los criterios de aprobación del package como un checklist donde cada ítem tiene resultado binario (pasa / no pasa) y referencia al documento o sección que lo evidencia.
2. IF todos los criterios del checklist de aprobación tienen resultado "pasa", THEN THE Package_Foundation SHALL marcar el package como aprobado. Los criterios evaluados son: (a) no existen afirmaciones contradictorias entre documentos del package sobre un mismo concepto, (b) el alcance declara explícitamente qué está incluido y qué está excluido del package, (c) el portfolio model enumera cada lab con su estado y su hipótesis de monetización, (d) los riesgos con impacto en la viabilidad del package están documentados con al menos una acción de mitigación cada uno, (e) existe al menos una revenue thesis formulada como hipótesis falsificable con condición de validación y plazo no mayor a 90 días, y (f) las hipótesis que requieren validación están listadas con su método de validación propuesto.
3. WHEN el package es sometido a revisión, THE Package_Foundation SHALL incluir en `016-foundation-review.md` una matriz de trazabilidad que vincule cada requisito del package con el documento específico que lo satisface, indicando sección o párrafo.
4. IF existen afirmaciones contradictorias entre documentos del package sobre un mismo concepto detectadas durante revisión, THEN THE Package_Foundation SHALL documentar cada contradicción identificando los documentos y afirmaciones en conflicto, y resolverla con una decisión documentada antes de aprobación.
5. THE Package_Foundation SHALL definir en `016-foundation-review.md` el proceso de revisión como: auto-revisión del fundador evaluando cada criterio del checklist con resultado "pasa" o "no pasa", fecha de revisión, y listado de ítems que no pasan con justificación.

---

### Requisito 17: Consistencia Inter-Documentos

**User Story:** Como product manager, quiero garantizar que los 16 documentos del package no se contradigan entre sí y usen terminología consistente.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL usar cada término definido en el glosario del package (`README.md` del package o `docs/glossary/README.md`) con la misma grafía y significado en todos los documentos del package, sin introducir sinónimos ni redefiniciones para el mismo concepto.
2. WHEN un término listado en el glosario del package o un término de dominio no coloquial es usado por primera vez en un documento, THE Package_Foundation SHALL incluir una referencia explícita al glosario o una definición local en el mismo documento antes de su primer uso en contexto.
3. THE Package_Foundation SHALL producir un `015-package-summary.md` que liste, para cada documento del package, las decisiones registradas (aquellas marcadas como "Decisión" según los documentation standards) y declare explícitamente que no existen contradicciones entre documentos, o identifique las contradicciones pendientes de resolución.
4. IF dos documentos del package asignan definiciones diferentes al mismo término, establecen reglas mutuamente excluyentes para el mismo proceso, o declaran estados incompatibles para el mismo artefacto, THEN THE Package_Foundation SHALL ser considerado no apto para aprobación hasta que se resuelva la inconsistencia actualizando uno o ambos documentos para eliminar la contradicción.
5. IF un documento del package introduce un término de dominio que no existe en el glosario del package, THEN THE Package_Foundation SHALL agregar dicho término al glosario antes de considerar el documento como completo.

---

### Requisito 18: Estructura Documental del Package

**User Story:** Como operador del sistema, quiero que el package produzca exactamente los 16 documentos especificados con nombres y estructura predefinidos.

#### Criterios de Aceptación

1. THE Package_Foundation SHALL producir exactamente 16 archivos markdown en `docs/packages/package-000-foundation/` con los nombres: README.md, 001-company-vision.md, 002-mission.md, 003-problem-statement.md, 004-startup-thesis.md, 005-manifesto.md, 006-operating-principles.md, 007-company-model.md, 008-business-model.md, 009-revenue-thesis.md, 010-success-metrics.md, 011-scope-and-boundaries.md, 012-portfolio-model.md, 013-risk-register.md, 014-assumptions.md, 015-package-summary.md, 016-foundation-review.md.
2. THE Package_Foundation SHALL incluir en el README.md del package las siguientes secciones: propósito (párrafo descriptivo), lista de los 16 documentos donde cada entrada incluye número, nombre de archivo y descripción de máximo 120 caracteres, glosario del package con un mínimo de 5 términos clave definidos, y estado actual con un valor entre: `pendiente`, `en progreso` o `completo`.
3. WHEN el package es completado, THE Package_Foundation SHALL verificar que cada uno de los 16 archivos cumple con: un título H1, al menos una sección H2, y un mínimo de 100 palabras de contenido en prosa (excluyendo encabezados y metadatos), antes de considerar el entregable como completo.
4. THE Package_Foundation SHALL seguir las convenciones de nombres definidas en el steering del proyecto: archivos en kebab-case inglés, contenido en español.
5. IF alguno de los 16 archivos no existe, tiene 0 bytes, o no alcanza el mínimo de 100 palabras de contenido en prosa, THEN THE Package_Foundation SHALL reportar el archivo como incompleto indicando cuál requisito estructural falta.

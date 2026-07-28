# 021 — Research Ethics and Safety

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R20.1, R20.2, R20.3, R20.4, R20.5, R21.1, R21.2, R21.3, R21.4, R21.5, R22.1, R22.2, R22.3, R22.4, R22.5, R22.6

## Propósito

Este documento define las reglas de ética, privacidad, propiedad intelectual y uso responsable de IA que aplican a toda investigación dentro de LabOS. Establece obligaciones, prohibiciones y procesos que garantizan que la actividad investigativa respeta los derechos de terceros, cumple con regulaciones aplicables, y produce outputs confiables y honestos. [Decisión]

---

## Tabla de contenidos

1. [Privacy y manejo de datos](#1-privacy-y-manejo-de-datos)
2. [Propiedad intelectual](#2-propiedad-intelectual)
3. [Uso responsable de IA](#3-uso-responsable-de-ia)
4. [Reglas para dominios regulados](#4-reglas-para-dominios-regulados)
5. [Prohibiciones explícitas](#5-prohibiciones-explícitas)
6. [Proceso de compliance](#6-proceso-de-compliance)
7. [Trazabilidad](#7-trazabilidad)

---

## 1. Privacy y manejo de datos

### 1.1 Documentación obligatoria antes de recopilar datos personales

Si una investigación involucra datos personales, se debe completar la siguiente documentación **antes** de iniciar cualquier recopilación: [Decisión]

| # | Campo | Definición | Ejemplo |
|---|-------|------------|---------|
| 1 | **Data type** | Clasificación del tipo de dato personal involucrado. | PII (nombre, email), datos de comportamiento, datos financieros, datos de salud. |
| 2 | **Collection method** | Cómo se obtienen los datos. | Encuesta directa, scraping público, entrega voluntaria, observación, API de terceros. |
| 3 | **Storage location** | Dónde se almacenan los datos durante la investigación. | Deepnote (workspace privado), GitHub (repositorio privado), local (disco cifrado). |
| 4 | **Access control** | Quién tiene acceso a los datos y bajo qué condiciones. | Solo Fundador; acceso mediante autenticación; no compartido con terceros. |
| 5 | **Retention period** | Tiempo máximo que los datos se conservan. Máximo 365 días salvo obligación regulatoria documentada. | 90 días post-conclusión; 365 días si regulación lo requiere (citar regulación específica). |
| 6 | **Deletion procedure** | Cómo se eliminan los datos al cumplir el periodo de retención. | Eliminación de archivos + vaciado de papelera + confirmación en research journal. |

### 1.2 Reglas de almacenamiento

Datos clasificados como confidenciales (sujetos a NDA, restricción contractual, o que contengan PII de terceros) están **prohibidos** en: [Decisión]

- Repositorios públicos de GitHub
- Ubicaciones sin cifrado
- Herramientas sin control de acceso verificable
- Documentos compartidos sin restricción de audiencia

### 1.3 Anonimización

Cuando una investigación produce outputs que referencian individuos identificables: [Decisión]

1. Se debe aplicar **anonimización** antes de almacenar o compartir el output.
2. Anonimización = eliminación o reemplazo de todos los atributos que permitan identificación directa o indirecta (nombre, email, dirección, identificadores únicos, combinaciones de atributos que permitan re-identificación).
3. Alternativa: documentación de **consentimiento explícito** del individuo, con fecha, alcance del consentimiento, y medio de registro.

### 1.4 Dominios regulados y privacy

Si la investigación involucra dominios regulados (finance, health, legal, u otro dominio sujeto a regulación jurisdiccional documentada en Package 000 scope-and-boundaries), se deben documentar las **restricciones regulatorias aplicables** y las **medidas de compliance** antes de procesar datos. Ver [Sección 4](#4-reglas-para-dominios-regulados) para requisitos específicos. [Decisión]

### 1.5 Suspensión por incumplimiento

Si se identifica que una actividad investigativa carece de la documentación de privacy requerida (campos 1-6), se debe: [Decisión]

1. **Suspender** el procesamiento de datos de esa actividad inmediatamente.
2. Completar la documentación faltante.
3. Obtener revisión del Fundador.
4. Solo entonces reanudar el procesamiento.

---

## 2. Propiedad intelectual

### 2.1 Registro de licensing de fuentes

Cuando una fuente se utiliza en investigación, el Source_Register debe incluir (además de los campos estándar de evaluación): [Decisión]

| # | Campo IP | Definición | Ejemplo |
|---|----------|------------|---------|
| 1 | **Source name** | Nombre de la fuente o recurso. | "Designing Data-Intensive Applications" |
| 2 | **Author / rights holder** | Persona u organización que posee los derechos. | Martin Kleppmann / O'Reilly Media |
| 3 | **License type** | Tipo de licencia bajo la cual se puede usar la fuente. | MIT, Apache 2.0, CC BY 4.0, All Rights Reserved, Proprietary, Unknown |
| 4 | **Permitted uses** | Usos permitidos por la licencia. | Referencia académica, cita breve, reproducción parcial con atribución, uso comercial derivativo. |
| 5 | **Attribution requirements** | Requisitos específicos de atribución que la licencia impone. | Citar autor + título + año; incluir aviso de copyright; link a licencia original. |

### 2.2 Verificación para uso comercial

Antes de marcar un asset como listo para distribución comercial, se debe verificar que **todas** las fuentes incorporadas tienen licencia documentada que permite uso comercial. [Decisión]

**Proceso de verificación:**

1. Listar todas las fuentes incorporadas en el asset (directa o indirectamente).
2. Para cada fuente, verificar que `license_type` y `permitted_uses` permiten uso comercial.
3. Si todas las fuentes permiten uso comercial → asset puede avanzar a distribución.
4. Si alguna fuente no permite uso comercial → remover la fuente o reemplazar con alternativa compatible antes de avanzar.

### 2.3 Reglas de atribución

Cuando se incorpora contenido de terceros en outputs de investigación, la atribución debe incluir: [Decisión]

| Campo de atribución | Requerido |
|--------------------|-----------|
| Autor original o rights holder | Sí |
| Título de la fuente o identificador | Sí |
| Tipo de licencia | Sí |
| Año de publicación (si disponible) | Sí |

La atribución debe aparecer en **todos** los outputs donde el contenido de terceros se utilice.

### 2.4 Fuentes con licencia indeterminada

Si una fuente carece de licencia explícita, tiene información de licencia conflictiva, o el Fundador no puede determinar si el uso comercial está permitido: [Decisión]

1. Documentar la incertidumbre específica (qué no se pudo determinar y por qué).
2. Marcar el contenido afectado como **"IP-unresolved"**.
3. **Restringir uso comercial** de outputs que contengan ese contenido hasta que se resuelva la determinación.
4. Registrar en el Decision Log la acción pendiente para resolver el estado de IP.

### 2.5 Fuentes con licencia incompatible

Cuando los términos de licencia de una fuente prohíben el uso previsto del output de investigación: [Decisión]

1. **Remover** la fuente del output, o
2. **Reemplazar** con una alternativa que tenga licencia compatible.

No se permite publicar ni distribuir outputs que contengan fuentes con licencia incompatible con el uso previsto.

---

## 3. Uso responsable de IA

### 3.1 Clasificación: AI_Generated_Content

Todo contenido sustantivo producido por herramientas de IA (ChatGPT, NotebookLM, Copilot, Claude, o cualquier sistema de IA) durante la investigación se clasifica como **AI_Generated_Content**. [Decisión]

**Incluye** (contenido sustantivo que requiere clasificación):
- Resúmenes generados por IA
- Claims factuales producidos por IA
- Explicaciones y análisis generados por IA
- Síntesis de múltiples fuentes realizadas por IA
- Código generado por IA que constituye hallazgo de investigación

**Excluye** (ediciones menores que no requieren clasificación):
- Corrección ortográfica o gramatical
- Reformateo de texto existente
- Autocompletado de código trivial

**Regla fundamental:** AI_Generated_Content **no es Primary_Evidence**. Nunca. Sin excepciones. [Decisión]

### 3.2 Verificación obligatoria

Antes de que contenido generado por IA pueda soportar una conclusión de investigación, se requiere **verificación**: [Decisión]

| Paso | Acción | Resultado |
|------|--------|-----------|
| 1 | Identificar el claim factual en el output de IA. | Claim aislado y articulado. |
| 2 | Localizar de forma independiente la fuente primaria citada. | Fuente accedida directamente (no a través de la misma herramienta IA). |
| 3 | Confirmar que el claim específico existe en la fuente primaria. | Verificación positiva o negativa. |
| 4 | Registrar el resultado de la verificación. | `verified`, `unverified`, o `source-not-found`. |

**Restricción:** La verificación no se puede realizar usando la misma herramienta de IA que produjo el claim. Se requiere acceso directo e independiente a la fuente. [Decisión]

### 3.3 Labeling obligatorio

Cuando un output de IA se incorpora en hallazgos de investigación, se debe etiquetar con: [Decisión]

| Campo de labeling | Definición | Ejemplo |
|-------------------|------------|---------|
| **Tool name** | Nombre de la herramienta que generó el contenido. | ChatGPT-4, NotebookLM, Claude 3.5 |
| **Generation date** | Fecha en que se generó el contenido. | 2024-03-15 |
| **Query intent** | Descripción del intent de la consulta (máximo 200 caracteres). | "Comparar frameworks de orquestación de microservicios para sistemas event-driven" |
| **Verification status** | Estado de verificación del contenido. | `verified` \| `unverified` \| `source-not-found` |

### 3.4 Prohibición de claims no verificados como evidencia

Si una herramienta de IA proporciona un claim factual y la fuente primaria subyacente **no ha sido localizada y verificada independientemente** por el investigador: [Decisión]

- El claim **no puede** citarse como evidencia en ninguna conclusión de investigación.
- El claim puede registrarse como punto de partida para búsqueda, pero con `verified_by: "unverified"` y confidence ≤ 2.

### 3.5 Uso permitido de IA como herramienta analítica

Se **permite** el uso de IA como herramienta de análisis y síntesis, con las siguientes condiciones: [Decisión]

1. Toda conclusión presentada como hallazgo de investigación debe descansar en **al menos una fuente primaria verificada**, no exclusivamente en el output de IA.
2. El output de IA es un **medio** para el análisis, no un **resultado** por sí mismo.
3. Si IA se usa para >50% de los pasos analíticos, se activa human review obligatorio (ver Sección 4).

### 3.6 Verificación fallida

Si el investigador intenta verificar un claim de IA y la fuente citada **no puede localizarse** o **no contiene** la información reclamada: [Decisión]

1. **Descartar** el claim como no soportado.
2. Registrar el intento de verificación fallido en el research journal con:
   - Fecha del intento
   - Fuente buscada
   - Resultado: "source not found" o "claim not present in source"
3. El claim queda con `verification_status: source-not-found` y **no puede** usarse como evidencia.

### 3.7 Confidence ceiling para AI_Generated_Content

El contenido clasificado como AI_Generated_Content tiene un **ceiling de confianza de nivel 3** mientras permanezca sin verificación contra fuente primaria. [Decisión]

| Estado de verificación | Confidence máximo |
|-----------------------|-------------------|
| `verified` | Sin ceiling adicional (aplican reglas estándar del Evidence Framework) |
| `unverified` | 2 (regla de evidencia no verificada, Sección 4.2 del Evidence Framework) |
| `source-not-found` | No puede usarse como evidencia |

---

## 4. Reglas para dominios regulados

### 4.1 Dominios con requisitos adicionales

Los siguientes dominios requieren revisión y documentación adicional por la naturaleza regulatoria o el impacto potencial en personas: [Decisión]

| Dominio | Razón de tratamiento especial | Ejemplos de regulación aplicable |
|---------|-------------------------------|----------------------------------|
| **Finance** | Regulaciones financieras, responsabilidad fiduciaria, riesgo de pérdida económica. | Regulaciones de valores, anti-lavado, disclaimer de no-consejo financiero. |
| **Health** | Datos sensibles de salud, riesgo de daño por recomendaciones incorrectas. | HIPAA (referencia), regulación de datos de salud, ética médica. |
| **Legal** | Privilegio profesional, riesgo de consejo legal no autorizado. | Regulaciones de práctica legal, confidencialidad abogado-cliente. |

### 4.2 Requisitos para investigación en dominios regulados

Toda investigación que produzca hallazgos que **informarán decisiones** en dominios regulados debe cumplir: [Decisión]

| Requisito | Descripción |
|-----------|-------------|
| **Human review obligatorio** | Revisión humana documentada con: identidad del revisor, fecha, lista de hallazgos revisados, decisión de aprobación, condiciones o caveats. |
| **Disclaimer explícito** | Declaración de que el output no constituye consejo profesional (financiero, médico, legal según aplique). |
| **Documentación regulatoria previa** | Antes de procesar datos: documentar regulaciones aplicables y medidas de compliance. |
| **Verificación de fuentes reforzada** | Fuentes deben ser oficiales o de autoridad reconocida en el dominio. |
| **AI review reforzado** | Si >50% del análisis usa herramientas IA, cada hallazgo que soporte la conclusión requiere verificación human contra fuente primaria. |

### 4.3 Declaraciones obligatorias por dominio

| Dominio | Declaración requerida en outputs |
|---------|----------------------------------|
| Finance | "Este análisis no constituye consejo financiero. No es una recomendación de inversión. Past performance no garantiza resultados futuros." |
| Health | "Este contenido no constituye consejo médico. Consultar con un profesional de salud antes de aplicar cualquier hallazgo." |
| Legal | "Este análisis no constituye consejo legal. No reemplaza la consulta con un abogado calificado en la jurisdicción relevante." |

---

## 5. Prohibiciones explícitas

Las siguientes prácticas están **explícitamente prohibidas** en toda investigación LabOS, sin excepciones: [Decisión]

### 5.1 Lista de prohibiciones

| # | Prohibición | Razón | Detección |
|---|-------------|-------|-----------|
| 1 | **Credenciales en documentos** — No almacenar tokens, API keys, passwords, secrets, o cualquier credencial de acceso en documentos de investigación, repositorios, o herramientas compartidas. | Riesgo de seguridad: exposición de acceso no autorizado a sistemas. | Revisión en quality gate de publicación; herramientas de secret scanning. |
| 2 | **Datos sin anonimizar** — No almacenar ni compartir datos personales identificables sin anonimización previa o consentimiento documentado. | Violación de privacidad; riesgo legal; daño a terceros. | Checklist de privacy en Research_Brief; revisión antes de exportación. |
| 3 | **AI sin verificar como evidencia** — No citar output de IA como evidencia verificada en conclusiones sin haber localizado y confirmado el claim contra fuente primaria independiente. | Riesgo epistémico: alucinaciones de IA presentadas como hechos; pérdida de integridad investigativa. | Campo `verified_by` en Evidence Record; quality gate de conclusión. |
| 4 | **AI presentado como investigación original** — No presentar contenido generado por IA como resultado de investigación propia sin disclosure. | Deshonestidad epistémica; viola principio de trazabilidad. | Labeling obligatorio (Sección 3.3); human review. |
| 5 | **Datos regulados en repositorios públicos** — No almacenar datos sujetos a regulación (health, finance, legal) en ubicaciones de acceso público o sin cifrado. | Incumplimiento regulatorio; riesgo legal. | Checklist de privacy; revisión de repositorio antes de push. |
| 6 | **Copiar conversaciones IA completas a GitHub** — No exportar chats completos de herramientas IA a fuente de verdad; solo exportar decisiones y conclusiones verificadas. | Contenido no verificado contaminando fuente de verdad; ruido sobre señal. | Regla de handoff (009-tooling-workflow); human review. |

### 5.2 Consecuencia de violación

Si se detecta una violación de cualquier prohibición: [Decisión]

1. Suspender la actividad afectada inmediatamente.
2. Documentar la violación en el Research Journal.
3. Ejecutar remediation (eliminar credencial, anonimizar datos, reclasificar evidencia).
4. Registrar en Decision Log la acción correctiva tomada.
5. Verificar que no hay otras instancias de la misma violación en la investigación.

---

## 6. Proceso de compliance

### 6.1 Checklist de ethics y safety integrado en lifecycle

El compliance con este documento se verifica en los siguientes puntos del research lifecycle: [Decisión]

| Lifecycle stage | Verificación requerida |
|----------------|----------------------|
| **Intake** | Si la investigación involucra datos personales → documentar los 6 campos de privacy (Sección 1.1) en el Research_Brief. |
| **Source Collection** | Para cada fuente → registrar los 5 campos de IP (Sección 2.1) en Source_Register. |
| **Evidence Evaluation** | Todo AI_Generated_Content → clasificar y etiquetar (Sección 3.1, 3.3). Verificar antes de usar como soporte de conclusión (Sección 3.2). |
| **Conclusion** | Ningún claim AI no verificado como evidencia. Privacy checklist satisfecho. IP compliance verificado. |
| **Review** | Human review con checklist de ethics completo. Dominios regulados → revisión reforzada (Sección 4.2). |
| **Publication/Archive** | Verificar: no credenciales, no datos sin anonimizar, atribución completa, licencias compatibles con uso previsto. |

### 6.2 Responsabilidad

El **Fundador** es responsable de: [Decisión]

- Completar la documentación de privacy antes de recopilar datos.
- Verificar licensing de fuentes antes de uso comercial.
- Asegurar que AI_Generated_Content está etiquetado y verificado.
- Ejecutar human review en dominios regulados.
- Remediar violaciones detectadas.

---

## 7. Trazabilidad

| Sección del documento | Requirements cubiertos |
|-----------------------|-----------------------|
| Sección 1.1 (Campos de privacy) | R20.1 |
| Sección 1.2 (Almacenamiento confidencial) | R20.2 |
| Sección 1.3 (Anonimización) | R20.3 |
| Sección 1.4 (Dominios regulados y privacy) | R20.4 |
| Sección 1.5 (Suspensión por incumplimiento) | R20.5 |
| Sección 2.1 (Registro de licensing) | R21.1 |
| Sección 2.2 (Verificación comercial) | R21.2 |
| Sección 2.3 (Reglas de atribución) | R21.3 |
| Sección 2.4 (Licencia indeterminada) | R21.4 |
| Sección 2.5 (Licencia incompatible) | R21.5 |
| Sección 3.1 (Clasificación AI_Generated_Content) | R22.1 |
| Sección 3.2 (Verificación obligatoria) | R22.2 |
| Sección 3.3 (Labeling obligatorio) | R22.3 |
| Sección 3.4 (Prohibición claims no verificados) | R22.4 |
| Sección 3.5 (Uso permitido como herramienta) | R22.5 |
| Sección 3.6 (Verificación fallida) | R22.6 |

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | 0 | 0% |
| [Decisión] | 26 | 100% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 0 | 0% |

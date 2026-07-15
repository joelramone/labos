# Alcance y Límites

## Alcance incluido

El presente documento define los límites del Package 000 — Foundation. Los siguientes elementos están dentro del alcance de este package: [Hecho]

1. **Definición fundacional de LabOS**: documentación de visión, misión, problema central, tesis de startup, principios operativos, modelos de empresa y negocio, métricas y portfolio. [Hecho]
2. **Establecimiento de estándares documentales**: convenciones de nomenclatura, clasificación epistémica, estructura de cross-links y mecanismos de validación interna entre documentos. [Hecho]
3. **Marco de gobernanza inicial**: registro de riesgos, supuestos con planes de validación, criterios de aprobación y proceso de revisión del package. [Hecho]
4. **Política de propiedad intelectual y regulación base**: clasificación de activos por origen, marcos regulatorios por jurisdicción y obligaciones de privacidad para labs que manejen datos de terceros. [Hecho]

## Exclusiones explícitas

Los siguientes elementos están explícitamente fuera del alcance del Package 000 — Foundation: [Hecho]

1. **No es un SaaS ni producto de software desplegado.** LabOS en esta etapa es un sistema documental y metodológico; no existe aplicación web, backend, base de datos ni infraestructura técnica en producción. [Hecho]
2. **No tiene usuarios externos.** No existe onboarding, cuentas, interfaces de usuario ni métricas de adopción externa. El único operador es el fundador. [Hecho]
3. **No define arquitectura técnica final.** Este package no prescribe stack tecnológico, lenguajes de programación, frameworks ni plataformas de despliegue para productos futuros. Las decisiones técnicas se documentarán en packages posteriores cuando exista una necesidad concreta validada. [Hecho]
4. **No modifica otros packages.** El Package 000 es autocontenido. No altera, redefine ni invalida entregables de packages 001 en adelante. Si un package posterior requiere ajustes al fundamento, deberá gestionarse mediante un documento de decisión en `docs/decisions/`. [Hecho]
5. **No promete liderazgo de mercado.** Ninguna afirmación en este package declara dominancia, posición competitiva privilegiada ni inevitabilidad de adopción. Toda proyección de mercado se clasifica como [Hipótesis] con criterio de validación. [Hecho]
6. **No compromete capital ni contrataciones.** Este package no autoriza inversión económica, contratación de personal ni adquisición de herramientas de pago sin un documento de decisión separado. [Hecho]

## Límites de propiedad intelectual

La propiedad intelectual generada en el contexto de LabOS se clasifica en exactamente tres categorías: [Hecho]

### 1. Propiedad exclusiva del fundador

| Aspecto | Detalle |
|---------|---------|
| **Derechos de uso** | El fundador retiene todos los derechos patrimoniales y morales sobre activos creados directamente por él sin asistencia de herramientas de IA ni incorporación de material de terceros. [Hecho] |
| **Restricciones** | Ninguna restricción interna. El fundador puede comercializar, licenciar, transferir o destruir estos activos sin aprobación adicional. [Hecho] |
| **Requisitos de atribución** | No aplica atribución interna. Para distribución externa, se atribuye a LabOS o al fundador según el contexto comercial. [Hecho] |

### 2. Open source

| Aspecto | Detalle |
|---------|---------|
| **Derechos de uso** | Activos publicados bajo licencia open source pueden ser usados, modificados y redistribuidos según los términos de la licencia seleccionada (por definir: MIT, Apache 2.0 u otra según el activo). [Hecho] |
| **Restricciones** | La licencia específica determina las restricciones. No se puede revocar una licencia open source ya publicada. Los activos open source no pueden contener secretos comerciales, datos personales ni material con restricciones de terceros incompatibles. [Hecho] |
| **Requisitos de atribución** | Según la licencia seleccionada. Mínimo: copyright notice del fundador/LabOS en cada archivo fuente y LICENSE en la raíz del repositorio. [Hecho] |

### 3. Licenciable a terceros

| Aspecto | Detalle |
|---------|---------|
| **Derechos de uso** | El fundador retiene la propiedad y otorga licencias de uso limitadas bajo términos comerciales definidos caso por caso (por tiempo, territorio, exclusividad o volumen). [Hecho] |
| **Restricciones** | El licenciatario no adquiere derechos de propiedad ni de sublicenciamiento salvo acuerdo escrito explícito. Los activos licenciados no pueden redistribuirse fuera del alcance del acuerdo. [Hecho] |
| **Requisitos de atribución** | Definidos en cada contrato de licencia. Por defecto: mención de LabOS como origen del activo en cualquier uso público derivado. [Hecho] |

## Marcos regulatorios por jurisdicción

Los marcos regulatorios relevantes para LabOS se determinan por la jurisdicción del fundador (Colombia) y los mercados objetivo potenciales (Estados Unidos, Unión Europea, Latinoamérica). [Hecho]

> **Última revisión**: julio 2025. Si han transcurrido más de 90 días desde esta fecha, esta sección debe marcarse como [PENDIENTE DE ACTUALIZACIÓN].

### Colombia (jurisdicción del fundador)

| Área | Marco regulatorio | Estado |
|------|-------------------|--------|
| **Protección de datos personales** | Ley 1581 de 2012 (Habeas Data) + Decreto 1377 de 2013. Autoridad: Superintendencia de Industria y Comercio (SIC). Requiere autorización previa, finalidad específica y derechos ARCO. [Hecho] | Vigente |
| **Propiedad intelectual** | Ley 23 de 1982 (Derechos de autor) + Decisión Andina 351. El autor persona natural es titular originario. Obras generadas exclusivamente por IA no tienen titular definido en la legislación actual. [Hecho] | Vigente, sin regulación específica para IA |
| **IA generativa** | No existe legislación específica para IA generativa en Colombia a julio 2025. [Hecho] Se aplican principios generales de responsabilidad civil y derechos de autor. El CONPES 3975 (2019) establece lineamientos de política para IA sin carácter vinculante directo. [Hecho] | En evolución |

### Unión Europea (mercado objetivo)

| Área | Marco regulatorio | Estado |
|------|-------------------|--------|
| **Protección de datos personales** | GDPR (Reglamento 2016/679). Requiere base legal para tratamiento, derechos del interesado, DPIA para alto riesgo, y representante en la UE si se ofrecen servicios a residentes. [Hecho] | Vigente |
| **Propiedad intelectual** | Directiva 2001/29/CE (InfoSoc) + legislación nacional por estado miembro. Obras requieren creación intelectual humana para protección. Contenido generado exclusivamente por IA puede no ser protegible. [Hecho] | Vigente |
| **IA generativa** | EU AI Act (Reglamento 2024/1689). Clasifica sistemas de IA por riesgo. Modelos de propósito general (GPAI) tienen obligaciones de transparencia. Aplica a proveedores que comercialicen en la UE. [Hecho] | Vigente (aplicación escalonada 2024-2027) |

### Estados Unidos (mercado objetivo)

| Área | Marco regulatorio | Estado |
|------|-------------------|--------|
| **Protección de datos personales** | Sin ley federal integral. Regulación sectorial (HIPAA, COPPA, CCPA/CPRA en California). Si se atienden residentes de California: derechos de acceso, eliminación y opt-out de venta de datos. [Hecho] | Fragmentado por estado |
| **Propiedad intelectual** | Copyright Act (17 U.S.C.). La USCO ha establecido que obras generadas por IA sin intervención humana creativa significativa no son registrables. Obras con asistencia de IA pueden tener protección parcial (componentes humanos). [Hecho] | Vigente, jurisprudencia en evolución |
| **IA generativa** | Sin legislación federal integral a julio 2025. [Hecho] Existen propuestas legislativas y órdenes ejecutivas (EO 14110, oct 2023). Algunos estados tienen regulaciones parciales. Autorregulación predomina. [Hecho] | En evolución |

### Latinoamérica (otros mercados LatAm)

| Área | Marco regulatorio | Estado |
|------|-------------------|--------|
| **Protección de datos personales** | Varía por país. Referentes: LGPD (Brasil), Ley 25.326 (Argentina), Ley 19.628 (Chile, reformada). Principios comunes: consentimiento, finalidad, seguridad. [Hecho] | Vigente, heterogéneo |
| **Propiedad intelectual** | Convenio de Berna + legislación local. Coincidencia regional: titularidad humana como requisito para protección autoral. [Hecho] | Vigente |
| **IA generativa** | Sin regulación específica consolidada en la mayoría de países LatAm a julio 2025. [Hecho] Brasil tiene el PL 2338/2023 en trámite como marco general de IA. [Hecho] | En evolución |

## Obligación de privacidad para labs

Cuando un lab del portfolio maneje o declare intención de manejar datos de terceros, aplican las siguientes obligaciones antes de que el lab procese dichos datos: [Hecho]

| Lab / Escenario | Regulación aplicable | Tipo de datos | Obligaciones del responsable | Acción de cumplimiento requerida |
|-----------------|---------------------|---------------|------------------------------|----------------------------------|
| Labs que procesen datos personales de residentes colombianos | Ley 1581/2012 + Decreto 1377/2013 | Datos personales (nombre, email, comportamiento, financieros) | Obtener autorización previa e informada, garantizar derechos ARCO, registrar bases de datos ante SIC, implementar medidas de seguridad. [Hecho] | Antes de recolectar datos: (1) redactar política de privacidad conforme a Ley 1581, (2) implementar mecanismo de autorización, (3) registrar base de datos en RNBD de la SIC. [Hecho] |
| Labs que ofrezcan servicios a residentes de la UE | GDPR (Reglamento 2016/679) | Datos personales según Art. 4 GDPR | Identificar base legal (Art. 6), informar al interesado (Arts. 13-14), garantizar derechos del interesado (Arts. 15-22), realizar DPIA si alto riesgo (Art. 35). [Hecho] | Antes de procesar datos: (1) documentar base legal para cada tratamiento, (2) publicar aviso de privacidad conforme a Art. 13, (3) designar representante en UE si no hay establecimiento (Art. 27), (4) evaluar necesidad de DPIA. [Hecho] |
| Labs que procesen datos de residentes de California | CCPA/CPRA | Información personal según §1798.140 | Proveer notice at collection, honrar opt-out de venta/sharing, responder solicitudes de acceso/eliminación en 45 días. [Hecho] | Antes de recolectar datos: (1) publicar privacy notice conforme a CCPA, (2) implementar mecanismo "Do Not Sell/Share", (3) establecer proceso de respuesta a solicitudes. [Hecho] |
| Labs que manejen contenido con derechos de autor de terceros | Ley 23/1982 (CO) + Copyright Act (US) + InfoSoc (UE) | Obras protegidas (texto, imagen, audio, código con licencia restrictiva) | Verificar licencia antes de incorporar, respetar condiciones de la licencia, no sublicenciar sin autorización. [Hecho] | Antes de incorporar material de terceros: (1) verificar licencia y compatibilidad con uso comercial, (2) documentar fuente y licencia en metadata del activo, (3) obtener autorización escrita si la licencia no permite uso comercial explícitamente. [Hecho] |

## Política de propiedad intelectual por origen

Cada activo generado en LabOS se clasifica por su origen de creación con implicaciones diferenciadas para su comercialización: [Hecho]

### Activos producidos por el fundador (creación humana directa)

| Aspecto | Detalle |
|---------|---------|
| **Derechos de uso** | Protección plena bajo legislación de derechos de autor aplicable (Ley 23/1982 CO, Copyright Act US, InfoSoc UE). Registrable ante autoridades nacionales. Comercializable sin restricción de titularidad. [Hecho] |
| **Restricciones de comercialización** | Ninguna derivada del origen. Las únicas restricciones provienen de compromisos contractuales previos del fundador (e.g., cláusulas de no competencia, acuerdos de confidencialidad laborales vigentes). [Hecho] |
| **Requisitos de atribución** | Atribución al fundador o a LabOS según contexto comercial. No existe obligación legal de atribución para obras propias, pero se recomienda por consistencia de marca. [Hecho] |

### Activos generados por IA (con o sin intervención humana)

| Aspecto | Detalle |
|---------|---------|
| **Derechos de uso** | Protección autoral incierta para outputs puramente generados por IA. [Hipótesis] Obras con contribución creativa humana significativa (selección, disposición, edición sustancial) pueden tener protección parcial. [Hecho] Se recomienda maximizar la intervención humana creativa documentable para fortalecer reclamos de titularidad. [Hecho] |
| **Restricciones de comercialización** | Verificar términos de servicio (ToS) de cada herramienta de IA utilizada — algunos proveedores retienen derechos o imponen restricciones de uso comercial. [Hecho] No declarar como "obra original del fundador" sin intervención humana sustancial documentada. [Hecho] |
| **Requisitos de atribución** | Según ToS del proveedor de IA. Como práctica interna: documentar en metadata del activo la herramienta utilizada, el grado de intervención humana y la fecha de generación. [Hecho] |

### Activos derivados de fuentes de terceros

| Aspecto | Detalle |
|---------|---------|
| **Derechos de uso** | Determinados por la licencia del material fuente. Solo se incorporan materiales con licencia que permita uso comercial o derivados (Creative Commons compatibles, MIT, Apache 2.0, dominio público). [Hecho] |
| **Restricciones de comercialización** | Respetar condiciones de la licencia de origen: copyleft (GPL) impide relicenciamiento propietario sin autorización, share-alike requiere mantener la misma licencia en derivados, no-comercial prohíbe monetización directa. [Hecho] |
| **Requisitos de atribución** | Obligatoria según términos de la licencia fuente. Mínimo: autor original, nombre de la licencia, URL de la fuente, fecha de incorporación. Documentar en metadata del activo y en archivo NOTICE o ATTRIBUTION si se distribuye. [Hecho] |

## Límite temporal

El alcance de este documento está circunscrito a **Package 000 — Foundation**. [Hecho]

Cualquier expansión de alcance — incluyendo pero no limitado a: adición de nuevas categorías de PI, incorporación de nuevas jurisdicciones, modificación de exclusiones o ampliación de obligaciones regulatorias — requiere un documento de decisión separado en `docs/decisions/` con formato `NNNN-titulo.md` que justifique el cambio y documente el impacto en otros documentos del package. [Hecho]

Este documento no se extiende a packages posteriores (001+) ni prescribe obligaciones que no estén directamente vinculadas a la operación fundacional documentada en este package. [Hecho]

---

## Cross-links

- **Riesgos regulatorios y de PI**: Los riesgos asociados a privacidad, propiedad intelectual e IA generativa se detallan en [013-risk-register.md](./013-risk-register.md).
- **Entrante**: Este documento es referenciado desde el README del package como fuente de verdad para alcance, exclusiones y regulación.

---

## Tabla epistémica

| Clasificación  | Cantidad | Porcentaje |
| -------------- | -------- | ---------- |
| [Hecho]        | 43       | 96%        |
| [Hipótesis]    | 1        | 2%         |
| [Visión]       | 0        | 0%         |
| Sin clasificar | 1        | 2%         |

> **Nota**: La única hipótesis corresponde a la protección autoral de outputs generados exclusivamente por IA, cuyo estatus jurídico permanece incierto en todas las jurisdicciones documentadas. El ítem sin clasificar es un enunciado de recomendación operativa.

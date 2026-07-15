# Principios Operativos

## Propósito

Este documento traduce los principios declarados en [005-manifesto.md](./005-manifesto.md) a reglas operativas concretas con condiciones de aplicación, acciones esperadas y ejemplos observables. Cada regla describe un escenario específico y prescribe un comportamiento determinista que permite evaluar cumplimiento sin ambigüedad.

Las reglas aquí definidas gobiernan la priorización diaria de actividades y la toma de decisiones operativas del fundador. La priorización de flujo de caja y su relación con el modelo de negocio se detalla en [008-business-model.md](./008-business-model.md).

---

## Reglas Operativas

### Regla 1: Prioridad de ingresos sobre infraestructura

**Condición de aplicación:** Cuando existe una decisión entre invertir tiempo en una actividad de infraestructura (documentación interna, templates, refactoring, automatización sin usuario) y una actividad generadora de ingreso ejecutable en los próximos 90 días. [Decisión]

**Acción esperada:** Priorizar la actividad generadora de ingreso. Las actividades de infraestructura que no contribuyen directamente a generar ingresos en los próximos 90 días se posponen o se ejecutan en tiempo residual.

**Ejemplo concreto:**
- *Situación:* El fundador tiene 4 horas disponibles y debe elegir entre mejorar el template de specs de LabOS o crear una landing page para vender servicios de configuración de agentes IA.
- *Acción tomada:* Elige crear la landing page porque genera señal de demanda y potencial ingreso en menos de 30 días.
- *Resultado observable:* Landing publicada, primeras visitas registradas, al menos 1 formulario de contacto recibido en 14 días (o ruta descartada si no hay señal).

---

### Regla 2: Documentar antes de construir

**Condición de aplicación:** Antes de iniciar la implementación de cualquier feature, producto, automatización o componente que requiera más de 2 horas de desarrollo. [Decisión]

**Acción esperada:** Crear un spec, blueprint o documento de decisión que defina: qué se construye, por qué, qué resultado se espera, y cuál es el criterio de éxito. No iniciar código ni configuración hasta que el documento exista.

**Ejemplo concreto:**
- *Situación:* El fundador quiere desarrollar un bot de trading con estrategia de scalping.
- *Acción tomada:* Antes de escribir código, crea un spec en `.kiro/specs/crypto-scalping-bot/` con requirements (estrategia, par, exchange), design (arquitectura, dependencias) y tasks (pasos de implementación).
- *Resultado observable:* Scope definido en documento, esfuerzo estimable antes de iniciar, criterios de éxito documentados que permiten evaluar si el bot funciona o no.

---

### Regla 3: Registrar toda investigación mayor a 4 horas como activo

**Condición de aplicación:** Al completar una actividad de investigación o exploración que consumió más de 4 horas acumuladas de esfuerzo, independientemente de si el resultado fue positivo o negativo. [Decisión]

**Acción esperada:** Crear un registro de activo con los campos mínimos: nombre (≤80 caracteres), tipo (de la taxonomía definida en 007-company-model.md), descripción (1-3 oraciones), hipótesis de uso (usuario objetivo + contexto de aplicación) y estado (borrador).

**Ejemplo concreto:**
- *Situación:* El fundador invierte 6 horas investigando frameworks de agentes IA (LangChain, CrewAI, AutoGen) para seleccionar stack del lab SoftwareFactoryAgentsAI.
- *Acción tomada:* Crea un activo tipo playbook llamado "agent-frameworks-comparison" con descripción del análisis, hipótesis de uso para selección de stack y recomendación fundamentada.
- *Resultado observable:* Activo registrado en `assets/knowledge/` con estado borrador, reutilizable por cualquier operador que necesite elegir framework de agentes sin repetir la investigación.

---

### Regla 4: Validar demanda antes de desarrollar producto

**Condición de aplicación:** Cuando existe una idea de producto que requiere más de 1 semana-persona de desarrollo para alcanzar un MVP funcional. [Decisión]

**Acción esperada:** Ejecutar al menos un experimento de validación de demanda antes de iniciar desarrollo completo. Experimentos válidos: landing page con formulario, entrevistas de descubrimiento (≥3), pre-venta directa, o publicación de oferta en canal relevante.

**Ejemplo concreto:**
- *Situación:* El fundador tiene la idea de construir un SaaS de gestión de comunidades con IA para el lab CommunityManagerBotCrew.
- *Acción tomada:* En lugar de construir el SaaS completo, publica una landing page con propuesta de valor y formulario de interés, distribuye en 3 comunidades relevantes, y mide registros durante 2 semanas.
- *Resultado observable:* 15 registros en 14 días confirman interés → se procede con MVP. Si <5 registros → se pivota la propuesta de valor o se descarta la ruta.

---

### Regla 5: Revisar riesgos mensualmente

**Condición de aplicación:** Al inicio de cada mes calendario, o inmediatamente cuando ocurre un evento que modifica el perfil de riesgos (pérdida de cliente, cambio regulatorio, falla técnica crítica, agotamiento de runway). [Decisión]

**Acción esperada:** Revisar el registro de riesgos (013-risk-register.md), actualizar probabilidades e impactos según evidencia nueva, agregar riesgos identificados durante el mes, y ajustar prioridades de mitigación si algún riesgo cambió de categoría.

**Ejemplo concreto:**
- *Situación:* El 1 de marzo, el fundador realiza la revisión mensual y detecta que han pasado 45 días sin validar ninguna ruta de ingreso.
- *Acción tomada:* Actualiza el riesgo "ausencia prolongada de ingresos" de probabilidad media a alta, documenta la evidencia (45 días sin validación), y escala la prioridad de las actividades de la Regla 1.
- *Resultado observable:* Registro de riesgos actualizado con fecha, nuevo nivel de riesgo documentado, y al menos una acción de mitigación asignada para las próximas 2 semanas.

---

### Regla 6: Un commit, un propósito

**Condición de aplicación:** Al preparar un commit, pull request, o cualquier entregable para revisión en el repositorio. [Decisión]

**Acción esperada:** Asegurar que el cambio aborda una sola preocupación (un bug, una feature, un documento, una corrección) y es revisable por un humano en menos de 15 minutos. Si el cambio toca más de un propósito, separar en entregas independientes.

**Ejemplo concreto:**
- *Situación:* El fundador termina una sesión de trabajo donde actualizó documentación del manifesto, corrigió un error en el README y agregó un nuevo principio operativo.
- *Acción tomada:* Separa en 3 commits: (1) corrección README, (2) actualización manifesto, (3) nuevo principio operativo.
- *Resultado observable:* Cada commit revisable independientemente, historial de git navegable por propósito, rollback posible sin afectar cambios no relacionados.

---

### Regla 7: Clasificar antes de avanzar

**Condición de aplicación:** Al escribir una afirmación sobre estado, capacidad, proyección, demanda o intención en cualquier documento del repositorio. [Decisión]

**Acción esperada:** Clasificar inmediatamente la afirmación como [Hecho] (con fuente verificable), [Hipótesis] (con método de validación), [Visión] (con horizonte temporal) o [Decisión] (con fecha y contexto). No avanzar en la redacción sin asignar la clasificación.

**Ejemplo concreto:**
- *Situación:* Al documentar el modelo de negocio, el fundador escribe "el mercado de agentes IA crecerá 40% anual en los próximos 3 años".
- *Acción tomada:* Clasifica como [Hipótesis], agrega la fuente del estimado (reporte X, fecha Y), define método de validación (comparar con datos reales en 12 meses) y documenta el impacto si la hipótesis es incorrecta.
- *Resultado observable:* El lector distingue inmediatamente que es una suposición y sabe cómo verificarla, en lugar de tratarla como dato confirmado para tomar decisiones.

---

## Relación con el Manifiesto

Cada regla operativa implementa uno o más principios del [manifesto](./005-manifesto.md):

| Regla | Principio del Manifesto |
|-------|------------------------|
| 1. Prioridad de ingresos | 3. Hipótesis antes de inversión + 4. Vender antes de construir |
| 2. Documentar antes de construir | 1. No empezar por código |
| 3. Investigación como activo | 2. Toda investigación produce un activo |
| 4. Validar demanda | 4. Vender antes de construir |
| 5. Revisar riesgos | 6. Hechos y hipótesis, no opiniones |
| 6. Un commit, un propósito | 5. Cambios pequeños y revisables |
| 7. Clasificar antes de avanzar | 6. Hechos y hipótesis, no opiniones + 7. Documentación es producto |

---

## Tabla Epistémica

| Clasificación | Cantidad | Notas |
|---------------|----------|-------|
| [Hecho]       | 0        | —     |
| [Hipótesis]   | 0        | —     |
| [Visión]      | 0        | —     |
| [Decisión]    | 7        | Las 7 reglas operativas son decisiones activas del fundador |

Fecha de última revisión: 2025-01-XX (pendiente revisión formal)

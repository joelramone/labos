# Modelo de Negocio

## Propósito

Este documento define los mecanismos de monetización de LabOS organizados por etapa temporal, clasificados por tipo de flujo de caja y presentados como hipótesis con criterios de validación explícitos. Ningún mecanismo aquí descrito se considera validado hasta que cumpla su criterio de éxito dentro del plazo establecido.

La estructura sigue el principio operativo de prioridad de ingresos sobre infraestructura definido en [006-operating-principles.md](./006-operating-principles.md), y complementa el Asset_First_Model documentado en [007-company-model.md](./007-company-model.md).

---

## Clasificación por tipo de flujo de caja

Todos los mecanismos de monetización se clasifican en exactamente una de tres categorías: [Decisión]

| Categoría | Tipo | Características | Ejemplos |
| --------- | ---- | --------------- | -------- |
| **Caja inmediata** | Servicios / Consulting | Ingreso por proyecto, cobro al entregar, no requiere producto terminado | Configuración de agentes IA, consulting técnico, implementaciones a medida |
| **Recurrencia** | Suscripciones / Membresías | Ingreso mensual predecible, requiere retención activa | Membresía de comunidad, acceso a herramientas, soporte recurrente |
| **Escalabilidad** | Productos digitales / Licencias | Ingreso desacoplado del tiempo invertido, crece sin proporción lineal de esfuerzo | Templates, playbooks, cursos, APIs, licencias de software |

---

## Etapa 1: Inmediato (0–30 días)

> **Peso de esfuerzo: 60%** — La mayor parte del esfuerzo se concentra en esta etapa para generar señal de demanda y flujo de caja lo antes posible. [Decisión]

### Ruta 1: Servicios de configuración de agentes IA

**Tipo de flujo:** Caja inmediata (servicios/consulting) [Hipótesis]

| Campo | Detalle |
| ----- | ------- |
| **Acción a ejecutar** | Ofrecer servicios de configuración y deployment de agentes IA a empresas pequeñas. Entregable: agente funcional configurado y documentado en el entorno del cliente. |
| **Recurso requerido** | 20 horas/semana de tiempo del fundador + $0 presupuesto adicional (herramientas gratuitas o ya disponibles). |
| **Ingreso estimado** | $500–$2,000 USD por proyecto. |
| **Plazo de evaluación** | 30 días desde inicio de prospección activa. |
| **Criterio de éxito/fracaso** | ≥1 cliente pagando dentro de 30 días. Si 0 clientes en 30 días → evaluar pivote de oferta o canal. |

**Validación:** Métrica observable = número de clientes que pagaron. Umbral numérico = 1. Deadline = 30 días. [Hipótesis]

**Justificación:** Esta ruta es activable por un solo operador en <30 días porque: (1) no requiere producto terminado — se entrega como servicio personalizado, (2) no depende de terceros incontrolables — el fundador ejecuta directamente, (3) utiliza habilidades existentes del fundador sin capacitación adicional. [Hecho]

---

### Ruta 2: Templates y playbooks para fundadores técnicos

**Tipo de flujo:** Escalabilidad (productos digitales) [Hipótesis]

| Campo | Detalle |
| ----- | ------- |
| **Acción a ejecutar** | Producir y publicar un pack de templates para documentación de startups (specs, blueprints, decision logs). Entregable: pack descargable en plataforma de venta (Gumroad, Lemon Squeezy o equivalente). |
| **Recurso requerido** | 15 horas one-time de producción + $50 USD para plataforma de venta y dominio. |
| **Ingreso estimado** | $20–$100 USD por venta × N ventas/mes. |
| **Plazo de evaluación** | 30 días post-publicación. |
| **Criterio de éxito/fracaso** | ≥3 ventas en 30 días post-publicación. Si <3 ventas → evaluar pricing, posicionamiento o canal de distribución. |

**Validación:** Métrica observable = número de ventas completadas. Umbral numérico = 3. Deadline = 30 días post-publicación. [Hipótesis]

**Justificación:** Esta ruta es activable por un solo operador en <30 días porque: (1) los templates ya se están produciendo como parte de LabOS — es empaquetar lo existente, (2) la publicación en plataforma de venta es un proceso de horas, no semanas, (3) no requiere dependencias de terceros para crear el producto. [Hecho]

---

### Ruta 3: Micro-consulting por sesión (validación rápida)

**Tipo de flujo:** Caja inmediata (servicios) [Hipótesis]

| Campo | Detalle |
| ----- | ------- |
| **Acción a ejecutar** | Ofrecer sesiones de consulting de 60–90 minutos sobre arquitectura de agentes IA, documentación técnica o setup de portafolios de productos. Entregable: sesión completada + resumen de recomendaciones por escrito. |
| **Recurso requerido** | 5 horas/semana + $0 presupuesto (calendar + video call gratuitos). |
| **Ingreso estimado** | $100–$300 USD por sesión. |
| **Plazo de evaluación** | 30 días. |
| **Criterio de éxito/fracaso** | ≥2 sesiones pagadas en 30 días. Si <2 → evaluar si el problema es la oferta, el canal o el precio. |

**Validación:** Métrica observable = número de sesiones pagadas. Umbral numérico = 2. Deadline = 30 días. [Hipótesis]

---

## Etapa 2: Corto plazo (30–90 días)

> **Peso de esfuerzo: 25%** — Actividades que requieren validación previa de la etapa inmediata o mayor tiempo de preparación. [Decisión]

### Ruta 4: Suscripción a comunidad de fundadores técnicos

**Tipo de flujo:** Recurrencia (membresía) [Hipótesis]

| Campo | Detalle |
| ----- | ------- |
| **Acción a ejecutar** | Crear y lanzar una comunidad paga (Discord/Slack) con acceso a templates premium, sesiones grupales mensuales y canal de soporte asíncrono. Entregable: comunidad operativa con al menos 1 ciclo de contenido mensual completado. |
| **Recurso requerido** | 10 horas/semana + $30/mes plataforma. |
| **Ingreso estimado** | $20–$50 USD/mes × N miembros. |
| **Plazo de evaluación** | 90 días desde lanzamiento. |
| **Criterio de éxito/fracaso** | ≥10 miembros pagando al día 90. Retención ≥60% al segundo mes. Si <10 miembros o retención <60% → evaluar propuesta de valor o formato. |

**Validación:** Métrica observable = miembros activos pagando + tasa de retención. Umbral numérico = 10 miembros, 60% retención. Deadline = 90 días. [Hipótesis]

---

### Ruta 5: Automatizaciones de agentes IA como producto empaquetado

**Tipo de flujo:** Escalabilidad (producto digital / licencia) [Hipótesis]

| Campo | Detalle |
| ----- | ------- |
| **Acción a ejecutar** | Productizar las configuraciones de agentes IA validadas en la Ruta 1 como paquetes replicables con documentación y setup guiado. Entregable: ≥2 agentes empaquetados con documentación de instalación y uso. |
| **Recurso requerido** | 15 horas/semana + $100 infraestructura. |
| **Ingreso estimado** | $200–$1,000 USD por licencia/implementación. |
| **Plazo de evaluación** | 90 días. |
| **Criterio de éxito/fracaso** | ≥3 ventas de paquetes en 60 días post-lanzamiento. Si <3 → evaluar si el servicio personalizado (Ruta 1) tiene más demanda que el producto empaquetado. |

**Validación:** Métrica observable = ventas de paquetes. Umbral numérico = 3. Deadline = 60 días post-lanzamiento (dentro del plazo de 90 días de la etapa). [Hipótesis]

---

## Etapa 3: Mediano plazo (90–365 días)

> **Peso de esfuerzo: 15%** — Solo se activan si las etapas anteriores generaron evidencia de demanda. [Decisión]

### Ruta 6: SaaS de herramientas para fundadores técnicos

**Tipo de flujo:** Recurrencia (SaaS) [Hipótesis]

| Campo | Detalle |
| ----- | ------- |
| **Acción a ejecutar** | Desarrollar una herramienta web basada en los templates y procesos validados en etapas anteriores. Entregable: MVP funcional con ≥1 workflow automatizado. |
| **Recurso requerido** | 20 horas/semana + $200/mes infraestructura cloud. |
| **Ingreso estimado** | $30–$100 USD/mes × N usuarios. |
| **Plazo de evaluación** | 365 días (con checkpoint a 180 días). |
| **Criterio de éxito/fracaso** | ≥20 usuarios pagando al mes 12. MRR ≥$600 USD. Si <20 usuarios o MRR <$600 al checkpoint de 180 días → reevaluar viabilidad. |

**Validación:** Métrica observable = usuarios pagando + MRR. Umbral numérico = 20 usuarios, $600 MRR. Deadline = 365 días (checkpoint 180 días). [Hipótesis]

**Prerrequisito:** Solo iniciar desarrollo si las Rutas 1, 2 o 5 validaron demanda con ≥5 clientes/ventas combinadas. [Decisión]

---

### Ruta 7: Licenciamiento del framework LabOS

**Tipo de flujo:** Escalabilidad (licencia) [Hipótesis]

| Campo | Detalle |
| ----- | ------- |
| **Acción a ejecutar** | Empaquetar LabOS como framework licenciable para otros fundadores técnicos u organizaciones pequeñas. Entregable: documentación completa + onboarding guide + soporte básico incluido. |
| **Recurso requerido** | 10 horas/semana + $50/mes distribución. |
| **Ingreso estimado** | $500–$2,000 USD por licencia anual. |
| **Plazo de evaluación** | 365 días. |
| **Criterio de éxito/fracaso** | ≥5 licencias vendidas en 12 meses. Si <5 → mantener como open source con servicios de implementación. |

**Validación:** Métrica observable = licencias vendidas. Umbral numérico = 5. Deadline = 365 días. [Hipótesis]

**Prerrequisito:** Solo ofrecer licenciamiento si LabOS ha sido operado internamente por ≥6 meses con resultados documentados. [Decisión]

---

## Resumen de asignación por etapa

| Etapa | Plazo | Peso de esfuerzo | Rutas | Tipo dominante |
| ----- | ----- | ----------------- | ----- | -------------- |
| **Inmediato** | 0–30 días | 60% | Rutas 1, 2, 3 | Caja inmediata + Escalabilidad |
| **Corto plazo** | 30–90 días | 25% | Rutas 4, 5 | Recurrencia + Escalabilidad |
| **Mediano plazo** | 90–365 días | 15% | Rutas 6, 7 | Recurrencia + Escalabilidad |

---

## Reglas de gobierno del modelo

1. **Ninguna ruta se considera validada hasta cumplir su criterio de éxito.** Todas son hipótesis hasta que la evidencia demuestre lo contrario. [Decisión]
2. **No invertir en etapa 3 sin validación en etapas 1-2.** El desarrollo de producto completo solo se justifica con señal de demanda previa. [Decisión]
3. **Revisión mensual obligatoria.** Cada ruta activa se revisa contra su criterio de éxito. Las que no muestran progreso en su plazo se pausan o pivotan. [Decisión]
4. **Priorizar caja inmediata.** Ante conflicto de tiempo entre rutas de caja inmediata y rutas de escalabilidad/recurrencia, priorizar lo que genera ingreso hoy. [Decisión]

---

## Cross-links

- **Tesis de ingresos**: Las hipótesis de revenue a nivel portfolio y su relación con los labs se detallan en [009-revenue-thesis.md](./009-revenue-thesis.md).
- **Supuestos**: Los supuestos que subyacen a este modelo (capacidad del fundador, tamaño de mercado, pricing) se documentan y validan en [014-assumptions.md](./014-assumptions.md).
- **Entrante desde Company Model**: Este documento es referenciado desde [007-company-model.md](./007-company-model.md) como fuente de verdad de mecanismos de monetización por etapa.
- **Entrante desde Operating Principles**: Este documento es referenciado desde [006-operating-principles.md](./006-operating-principles.md) en la Regla 1 (prioridad de ingresos) como detalle de la estrategia de flujo de caja.

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
| ------------- | -------- | ---------- |
| [Hecho]       | 2        | 6%         |
| [Hipótesis]   | 21       | 64%        |
| [Decisión]    | 10       | 30%        |
| [Visión]      | 0        | 0%         |

> **Nota**: El alto porcentaje de hipótesis es intencional y esperado — este documento describe mecanismos de monetización no validados. Las decisiones corresponden a reglas de gobierno y asignación de esfuerzo. Los hechos se limitan a justificaciones de activabilidad basadas en capacidades actuales verificables del fundador.

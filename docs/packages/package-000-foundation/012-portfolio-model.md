# Modelo de Portfolio

## Lista de labs

El portafolio de LabOS se compone de 11 labs, cada uno representando una vertical de negocio independiente con hipótesis de producto propia. [Hecho] Todos los labs comparten infraestructura operativa, steering, blueprints y automatizaciones a través de LabOS como sistema transversal. [Hecho]

| # | Lab | Dominio | Hipótesis de producto | Estado actual | Criterio de avance |
|---|-----|---------|-----------------------|---------------|-------------------|
| 1 | **LabOS** | Sistema transversal | Un sistema operativo documental y metodológico permite a un equipo mínimo operar múltiples líneas de negocio con rigor y sin pérdida de contexto. [Hipótesis] | explorando | Evidencia de que al menos 2 labs utilizan activamente infraestructura compartida de LabOS para sus operaciones (templates, steering, automatizaciones). |
| 2 | **SoftwareFactoryAgentsAI** | Agentes de IA | Existe demanda pagada por agentes de IA personalizados para automatización de procesos empresariales. [Hipótesis] | explorando | Al menos 1 prospecto identificado que exprese interés verificable (reunión, mensaje o solicitud documentada) en contratar un agente de IA. |
| 3 | **CommunityManagerBotCrew** | Contenido y distribución | La automatización de contenido y gestión de comunidades mediante bots genera engagement medible y reducción de carga operativa para creadores. [Hipótesis] | idea | Documentar hipótesis de monetización completa (segmento, formato, modelo de ingreso) y al menos 1 señal de demanda externa (búsqueda, pregunta o solicitud). |
| 4 | **Mindzers** | Productización | Profesionales del conocimiento pagarían por herramientas y productos digitales que sistematicen su expertise en formatos vendibles. [Hipótesis] | idea | Documentar hipótesis de monetización completa y realizar al menos 1 experimento de validación de demanda (landing page, encuesta o pre-venta). |
| 5 | **SentinelOps** | AIOps | Equipos de operaciones necesitan soluciones de monitoreo inteligente que reduzcan alertas falsas y automaticen respuestas a incidentes. [Hipótesis] | idea | Documentar hipótesis de monetización completa y obtener al menos 1 señal de demanda verificable del segmento objetivo. |
| 6 | **Crypto Scalping Core** | Trading cuantitativo | Estrategias algorítmicas de scalping pueden generar retornos consistentes con gestión de riesgo automatizada. [Hipótesis] | idea | Documentar estrategia con backtest sobre datos históricos que muestre expectativa positiva en al menos 100 operaciones simuladas. |
| 7 | **Atlas Wealth Labs** | Finanzas | Existe demanda por herramientas de análisis financiero personal que integren múltiples fuentes de datos y provean recomendaciones accionables. [Hipótesis] | idea | Documentar hipótesis de monetización completa y validar al menos 1 segmento objetivo con señal de interés documentada. |
| 8 | **Human Performance Lab** | Rendimiento humano | Profesionales del conocimiento pagarían por un sistema integrado de optimización personal basado en datos (hábitos, nutrición, sueño, productividad). [Hipótesis] | idea | Documentar protocolo de auto-experimentación con al menos 1 métrica medible durante 30 días y resultado observable. |
| 9 | **Photography Lab** | Fotografía | La producción fotográfica sistematizada con workflows de edición y monetización genera ingresos recurrentes a través de stock, prints o servicios. [Hipótesis] | idea | Publicar al menos 1 activo fotográfico en una plataforma de venta y documentar métricas de visibilidad o ingreso durante 30 días. |
| 10 | **Music Lab** | Música | La producción musical distribuida en plataformas digitales genera ingresos pasivos escalables con inversión de tiempo acotada. [Hipótesis] | idea | Publicar al menos 1 track en una plataforma de distribución y documentar streams o ingresos durante 30 días. |
| 11 | **English Learning Lab** | Idiomas | Existe demanda por contenido y herramientas de aprendizaje de inglés que combinen IA y metodologías de adquisición basadas en evidencia. [Hipótesis] | idea | Documentar hipótesis de monetización completa y validar interés con al menos 1 experimento de contenido (post, video o recurso) con métricas de engagement. |

---

## Estados válidos y transiciones

Los labs transitan entre estados de madurez de forma secuencial, con excepción del estado `pausado` que puede alcanzarse desde cualquier otro estado. [Hecho]

```text
idea → explorando → validando → operando
         ↕              ↕           ↕
       pausado        pausado     pausado
```

### Definición de estados

| Estado | Significado |
|--------|-------------|
| **idea** | Lab con hipótesis documentada pero sin inversión activa de tiempo ni recursos. [Hecho] |
| **explorando** | Lab con investigación activa, producción de activos o experimentación en curso. [Hecho] |
| **validando** | Lab con al menos una señal de demanda externa verificable y experimento de validación en ejecución. [Hecho] |
| **operando** | Lab con al menos una fuente de ingreso recurrente documentada y proceso repetible establecido. [Hecho] |
| **pausado** | Lab detenido temporalmente por decisión del fundador; conserva documentación y puede reactivarse. [Hecho] |

### Criterios de transición

| Transición | Criterio observable requerido |
|------------|-------------------------------|
| **idea → explorando** | (1) Hipótesis de monetización documentada con los 3 campos mínimos (segmento, formato, modelo de ingreso). (2) Asignación de al menos 2 horas semanales durante la primera semana. [Hecho] |
| **explorando → validando** | (1) Al menos 1 señal de demanda externa verificable (mensaje, reunión, solicitud, búsqueda documentada). (2) Experimento de validación diseñado con métrica de éxito definida y plazo ≤30 días. [Hecho] |
| **validando → operando** | (1) Al menos 1 transacción real documentada (fecha, monto, cliente, fuente de ingreso). (2) Proceso repetible documentado para generar la siguiente transacción. [Hecho] |
| **cualquier estado → pausado** | (1) Decisión explícita del fundador documentada con motivo y fecha. (2) Condición de reactivación definida (qué debe ocurrir para retomar). [Hecho] |
| **pausado → estado anterior** | (1) Se cumple la condición de reactivación documentada al momento de pausar. (2) Existe capacidad disponible (horas semanales) para retomar sin comprometer labs activos. [Hecho] |

---

## Reglas de priorización

Las siguientes reglas determinan la asignación de tiempo y recursos entre labs cuando existe competencia por la atención del fundador: [Hecho]

1. **Validación de demanda primero**: Labs con señales de demanda externa verificable (estado `validando` o superior) tienen prioridad sobre labs en exploración o idea. [Hecho]
2. **Flujo de caja inmediato sobre largo plazo**: Labs que pueden generar ingreso en menos de 30 días tienen prioridad sobre labs cuya monetización requiere desarrollo extenso o validación prolongada. [Hecho]
3. **Señal de demanda más reciente como desempate**: Cuando dos labs tienen el mismo nivel de validación y tipo de flujo de caja, se prioriza aquel cuya señal de demanda más reciente tiene menor antigüedad (fecha más cercana al presente). [Hecho]
4. **LabOS como habilitador, no como prioridad autónoma**: La infraestructura de LabOS se desarrolla en función de las necesidades reales de los labs activos, nunca de forma especulativa. [Hecho]

---

## Justificación de capacidad

Actualmente el portafolio tiene 2 labs en estado `explorando` (LabOS y SoftwareFactoryAgentsAI) y 9 labs en estado `idea`. [Hecho] Solo los labs en estado `explorando`, `validando` u `operando` se consideran activos para efectos de carga operativa. [Hecho]

### Capacidad disponible del fundador

| Concepto | Valor |
|----------|-------|
| Horas semanales totales disponibles para LabOS (fuera de empleo u obligaciones) | 20-25 horas/semana [Hipótesis] |
| Horas asignadas a LabOS (infraestructura) | 8-10 horas/semana [Hipótesis] |
| Horas asignadas a SoftwareFactoryAgentsAI | 8-10 horas/semana [Hipótesis] |
| Horas disponibles para exploración de nuevos labs | 2-5 horas/semana [Hipótesis] |

Con 2 labs activos, la carga actual es manejable dentro de la capacidad estimada. [Hipótesis] Si un tercer lab transiciona a `explorando`, se requerirá reasignar horas de exploración general o reducir la dedicación a uno de los labs activos existentes. [Hipótesis]

La justificación de más de 5 labs simultáneos no aplica actualmente porque solo 2 están activos. [Hecho] Si en el futuro más de 5 labs alcanzan estado activo simultáneamente, este documento deberá actualizarse con una redistribución explícita de horas que demuestre viabilidad operativa. [Hecho]

---

## Cross-links

- **Riesgos del portfolio**: Los riesgos asociados a la dispersión del portafolio y capacidad del fundador se documentan en [013-risk-register.md](./013-risk-register.md).
- **Entrante**: Este documento es referenciado desde [007-company-model.md](./007-company-model.md) como fuente de verdad del Portfolio_Model.

---

## Tabla epistémica

| Clasificación  | Cantidad | Porcentaje |
| -------------- | -------- | ---------- |
| [Hecho]        | 22       | 65%        |
| [Hipótesis]    | 12       | 35%        |
| [Visión]       | 0        | 0%         |
| Sin clasificar | 0        | 0%         |

> **Nota**: Las hipótesis corresponden mayoritariamente a las hipótesis de producto de cada lab (ninguna validada) y a las estimaciones de capacidad del fundador. Los hechos corresponden a estados actuales documentados, definiciones de estados y reglas operativas establecidas.

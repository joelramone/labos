# Análisis Comparativo — LABOS-RES-0001

> **Etiqueta epistémica:** Mixta (ver tabla epistémica al final)
> **Estado:** In Progress → Under Review
> **Fecha de análisis:** 2025-07-11

---

## 1. Método

Se evalúan 8 oportunidades contra 13 criterios en escala 1-5.
Cada puntuación incluye justificación y clasificación epistémica.

**Ponderación:** Criterios 1, 4 y 13 tienen peso ×2 (ver research-plan.md §6).

**Escala de scoring:**
- 5 = Excelente / Óptimo
- 4 = Bueno / Favorable
- 3 = Aceptable / Neutral
- 2 = Débil / Desfavorable
- 1 = Muy débil / Inviable

---

## 2. Oportunidades Evaluadas

| # | Oportunidad | Formato propuesto |
|---|-------------|-------------------|
| O1 | Playbook técnico de troubleshooting Kubernetes/EKS | Producto digital (template/playbook) |
| O2 | Auditoría/revisión productizada de incidentes y pipelines DevOps | Servicio productizado |
| O3 | Template de investigación cuantitativa | Producto digital (template) |
| O4 | Producto digital para entrenamiento adultos 35-50 | Producto digital (guía/programa) |
| O5 | Sistema de estudio de inglés técnico para profesionales IT | Producto digital (curso/sistema) |
| O6 | Servicio de generación de contenido especializado (CommunityManagerBotCrew) | Servicio productizado |
| O7 | Template LabOS para profesionales o pequeñas empresas | Producto digital (template pack) |
| O8 | Micro-consulting DevOps/K8s/Incident Response por sesión | Servicio (consulting) |

---

## 3. Evaluación Detallada por Oportunidad

### O1: Playbook técnico de troubleshooting Kubernetes/EKS

**Descripción:** Documento estructurado (PDF/Notion template) con flujos de diagnóstico para problemas comunes de K8s/EKS: pods en CrashLoopBackOff, node pressure, networking issues, RBAC, HPA scaling, etc. Incluye checklists, comandos, y árboles de decisión.

**Base de evidencia:**
- [Hecho] El fundador tiene experiencia operacional real en K8s/EKS con incident response.
- [Hecho] Kubernetes es la tecnología de orquestación dominante con adopción masiva documentada.
- [Inferencia] Existe demanda de troubleshooting guides basada en volumen de preguntas en StackOverflow y r/kubernetes.
- [Hipótesis] Profesionales DevOps pagarían $29-79 por un playbook estructurado.
- [Evidencia pendiente] No hay validación de willingness-to-pay específica para este formato en este nicho.

| # | Criterio | Score | Justificación |
|---|----------|-------|---------------|
| 1 | Tiempo hasta poder vender | 3 | [Hipótesis] 14-21 días. Requiere estructurar conocimiento existente en formato vendible. El contenido existe en la cabeza del fundador pero no está empaquetado. |
| 2 | Esfuerzo inicial | 3 | [Hipótesis] 30-40 horas de producción. Incluye writing, diagramas, y setup de plataforma de venta. |
| 3 | Necesidad de audiencia previa | 2 | [Inferencia] Sin audiencia DevOps establecida, la distribución inicial depende de comunidades (Reddit, Dev.to) donde el fundador no tiene presencia demostrada. |
| 4 | Credibilidad del fundador | 5 | [Hecho] Experiencia directa y verificable en K8s/EKS/DevOps en entornos enterprise. Este es el dominio de mayor credibilidad del fundador. |
| 5 | Riesgo legal/regulatorio | 5 | [Hecho] Ningún riesgo. Contenido técnico educativo sin restricciones. |
| 6 | Precio posible | 3 | [Hipótesis] $29-79 USD. Basado en observación de playbooks técnicos en Gumroad ($19-97 rango observable). |
| 7 | Posibilidad de preventa | 3 | [Hipótesis] Posible con landing page + descripción de contenido. No requiere producto terminado para validar interés. |
| 8 | Entrega manual inicial | 5 | [Hecho] 100% entregable como documento. No requiere software ni automatización. |
| 9 | Automatización futura | 3 | [Inferencia] Puede expandirse a serie de playbooks, membership con actualizaciones, pero el core es manual. |
| 10 | Recurrencia potencial | 2 | [Inferencia] One-shot por compra. Podría evolucionar a suscripción con actualizaciones, pero inicialmente no hay recurrencia. |
| 11 | Escalabilidad | 4 | [Hecho] Producto digital: una vez creado, escala sin esfuerzo proporcional. |
| 12 | Ajuste con proyectos LabOS | 4 | [Hecho] Conecta con SentinelOps (AIOps) y experiencia DevOps del fundador directamente. |
| 13 | Evidencia de mercado rápida | 3 | [Hipótesis] Landing page + post en r/kubernetes o r/devops podría generar señal en 7-14 días. |

**Fortalezas:** Máxima credibilidad del fundador; producto digital escalable; sin riesgo legal.
**Debilidades:** Sin audiencia previa; precio unitario moderado; requiere esfuerzo de producción.
**Riesgo principal:** Que sin audiencia la distribución orgánica no genere ventas suficientes en 30 días.

---

### O2: Auditoría/revisión productizada de incidentes y pipelines DevOps

**Descripción:** Servicio productizado donde el fundador revisa la configuración de CI/CD pipelines, arquitectura K8s, o post-mortems de incidentes de un cliente, y entrega un reporte estructurado con recomendaciones accionables. Precio fijo por alcance definido.

**Base de evidencia:**
- [Hecho] El fundador tiene experiencia real en incident response y pipelines CI/CD (Jenkins, Terraform).
- [Hecho] Los servicios de auditoría DevOps existen como categoría en plataformas freelance.
- [Inferencia] Empresas pequeñas con equipos DevOps limitados necesitan revisión externa periódica.
- [Hipótesis] El precio de $500-1500 por auditoría es viable para empresas con 5-50 empleados.
- [Evidencia pendiente] No hay evidencia de que el fundador pueda conseguir el primer cliente en 14 días sin red de contactos empresariales previa.

| # | Criterio | Score | Justificación |
|---|----------|-------|---------------|
| 1 | Tiempo hasta poder vender | 4 | [Hipótesis] 5-10 días. El servicio no requiere producto previo — solo definir alcance, pricing y canal de prospección. |
| 2 | Esfuerzo inicial | 4 | [Hipótesis] 8-15 horas: definir oferta, crear template de reporte, configurar medio de contacto. |
| 3 | Necesidad de audiencia previa | 2 | [Inferencia] Requiere red profesional o presencia en plataformas freelance. Sin audiencia B2B, la prospección fría tiene conversión muy baja. |
| 4 | Credibilidad del fundador | 5 | [Hecho] Experiencia directa en incident response, pipelines, K8s en entornos enterprise. Credibilidad máxima en este dominio. |
| 5 | Riesgo legal/regulatorio | 4 | [Hecho] Bajo riesgo. Posible necesidad de NDA con clientes, pero sin regulación específica. |
| 6 | Precio posible | 5 | [Hipótesis] $500-1500 por auditoría. Rango alto entre las oportunidades evaluadas. |
| 7 | Posibilidad de preventa | 4 | [Hipótesis] Alta. Se puede ofrecer como servicio sin tener producto construido. El entregable se produce después de la venta. |
| 8 | Entrega manual inicial | 5 | [Hecho] 100% servicio manual. El fundador ejecuta la auditoría personalmente. |
| 9 | Automatización futura | 4 | [Inferencia] Puede crear checklists reutilizables, templates de reporte, y eventualmente herramientas de análisis automático. |
| 10 | Recurrencia potencial | 3 | [Hipótesis] Posible retainer trimestral. Clientes podrían necesitar revisiones periódicas. |
| 11 | Escalabilidad | 2 | [Hecho] Limitado por horas del fundador. Escala solo con más operadores o automatización. |
| 12 | Ajuste con proyectos LabOS | 5 | [Hecho] Usa directamente SentinelOps (AIOps) y toda la experiencia DevOps. |
| 13 | Evidencia de mercado rápida | 3 | [Hipótesis] Prospección directa en LinkedIn/comunidades puede generar señal en 7-14 días. Pero conversión B2B es lenta. |

**Fortalezas:** Precio alto; máxima credibilidad; sell-first-build-later natural; alineado con Package 000 Ruta 1.
**Debilidades:** Requiere prospección B2B activa sin red previa; no escala fácilmente; ciclo de venta puede ser >14 días.
**Riesgo principal:** Que sin red de contactos empresariales, conseguir el primer cliente tome >30 días.

---

### O3: Template de investigación cuantitativa

**Descripción:** Pack de templates para ejecutar research cuantitativo: frameworks de análisis, notebooks templates, checklists de validación estadística, templates de reporte de findings. Basado en la metodología LabOS Package 001.

**Base de evidencia:**
- [Hecho] LabOS tiene una metodología de investigación completa documentada (Package 001).
- [Inferencia] Existen investigadores, data scientists y fundadores que necesitan estructura para sus análisis.
- [Hipótesis] Alguien pagaría $20-49 por templates de research cuantitativo.
- [Evidencia pendiente] No hay señal de demanda directa observada. El fundador asume que la necesidad existe basado en su propia experiencia.

| # | Criterio | Score | Justificación |
|---|----------|-------|---------------|
| 1 | Tiempo hasta poder vender | 3 | [Hipótesis] 14-21 días. Requiere empaquetar la metodología existente en formato consumible por externos. |
| 2 | Esfuerzo inicial | 3 | [Hipótesis] 25-35 horas. Adaptar documentación interna a producto vendible requiere edición significativa. |
| 3 | Necesidad de audiencia previa | 2 | [Inferencia] Sin audiencia de researchers/analysts, distribución limitada a comunidades donde el fundador no tiene presencia. |
| 4 | Credibilidad del fundador | 2 | [Inferencia] La credibilidad del fundador es en DevOps/infra, NO en metodología de investigación cuantitativa. LabOS es un proyecto sin usuarios externos que validen la metodología. |
| 5 | Riesgo legal/regulatorio | 5 | [Hecho] Ningún riesgo. |
| 6 | Precio posible | 2 | [Hipótesis] $20-49. Rango bajo para justificar el esfuerzo de producción. |
| 7 | Posibilidad de preventa | 2 | [Inferencia] Difícil vender templates de una metodología sin track record público ni testimonios. |
| 8 | Entrega manual inicial | 5 | [Hecho] 100% documento digital. |
| 9 | Automatización futura | 3 | [Inferencia] Podría evolucionar a herramienta SaaS pero requiere validación previa. |
| 10 | Recurrencia potencial | 1 | [Inferencia] One-shot sin recurrencia clara. |
| 11 | Escalabilidad | 4 | [Hecho] Producto digital. |
| 12 | Ajuste con proyectos LabOS | 5 | [Hecho] Directamente derivado de LabOS Package 001. |
| 13 | Evidencia de mercado rápida | 2 | [Hipótesis] Difícil obtener señal rápida sin audiencia ni canal establecido. |

**Fortalezas:** Existe como documentación interna (bajo esfuerzo de empaquetamiento relativo); escalable.
**Debilidades:** Credibilidad baja del fundador en este dominio específico; sin señal de demanda; precio bajo.
**Riesgo principal:** Que nadie perciba valor en templates de una metodología sin track record externo.

---

### O4: Producto digital para entrenamiento adultos 35-50

**Descripción:** Guía/programa digital para optimización de rendimiento físico y mental para profesionales adultos 35-50: rutinas de ejercicio, nutrición básica, hábitos de productividad, gestión de energía.

**Base de evidencia:**
- [Hecho] El fundador tiene interés personal en este dominio.
- [Hipótesis] El mercado de fitness/wellness digital es grande y creciente.
- [Evidencia pendiente] No hay evidencia de que el fundador tenga credibilidad, certificación o track record demostrable en este dominio.
- [Evidencia pendiente] No hay señal de demanda dirigida específicamente al perfil del fundador.

| # | Criterio | Score | Justificación |
|---|----------|-------|---------------|
| 1 | Tiempo hasta poder vender | 2 | [Hipótesis] 21-30 días. Requiere crear contenido desde cero sin base documental existente. |
| 2 | Esfuerzo inicial | 2 | [Hipótesis] 40-60 horas. Crear programa completo sin material previo. |
| 3 | Necesidad de audiencia previa | 1 | [Hecho] El mercado de fitness está saturado. Sin audiencia en este nicho, visibilidad es prácticamente cero. |
| 4 | Credibilidad del fundador | 1 | [Hecho] El fundador no tiene certificaciones de fitness, resultados públicos documentados, ni track record en coaching de rendimiento. El interés personal NO equivale a credibilidad profesional. |
| 5 | Riesgo legal/regulatorio | 3 | [Inferencia] Riesgo moderado. Consejos de salud sin licencia pueden generar responsabilidad si causan daño. |
| 6 | Precio posible | 3 | [Hipótesis] $29-97. Rango común para programas digitales de fitness/wellness. |
| 7 | Posibilidad de preventa | 1 | [Inferencia] Sin credibilidad ni audiencia, la preventa es prácticamente imposible. |
| 8 | Entrega manual inicial | 4 | [Inferencia] Puede ser documento + videos simples. |
| 9 | Automatización futura | 3 | [Inferencia] Podría evolucionar a app o membership. |
| 10 | Recurrencia potencial | 2 | [Hipótesis] Posible modelo de suscripción a largo plazo, pero requiere comunidad. |
| 11 | Escalabilidad | 4 | [Hecho] Producto digital. |
| 12 | Ajuste con proyectos LabOS | 2 | [Hecho] Solo conecta con Human Performance Lab que está en estado "idea". |
| 13 | Evidencia de mercado rápida | 1 | [Inferencia] Sin credibilidad ni audiencia, obtener señal de mercado es extremadamente difícil. |

**Fortalezas:** Mercado grande (en teoría); producto digital escalable.
**Debilidades:** CERO credibilidad del fundador; mercado saturado; sin audiencia; alto esfuerzo.
**Riesgo principal:** Invertir 40-60 horas en un dominio donde el fundador no tiene autoridad demostrable. Violación directa del principio de credibilidad.

---

### O5: Sistema de estudio de inglés técnico para profesionales IT

**Descripción:** Método/sistema estructurado para que profesionales IT de habla hispana mejoren su inglés técnico: vocabulario especializado, patrones de comunicación en daily standups, writing de documentación técnica, reading de RFCs y docs.

**Base de evidencia:**
- [Hecho] El fundador trabaja en inglés técnico cotidianamente (evidencia implícita de su trabajo en DevOps enterprise).
- [Inferencia] Existe una población significativa de developers hispanohablantes que necesitan mejorar su inglés técnico para acceder a mejores salarios.
- [Hipótesis] Profesionales IT pagarían por un método de inglés especializado vs cursos genéricos.
- [Evidencia pendiente] No hay señal directa de demanda observada por el fundador ni validación de willingness-to-pay.

| # | Criterio | Score | Justificación |
|---|----------|-------|---------------|
| 1 | Tiempo hasta poder vender | 2 | [Hipótesis] 21-30 días. Crear un sistema de estudio requiere diseño pedagógico + contenido. |
| 2 | Esfuerzo inicial | 2 | [Hipótesis] 40-50 horas. Diseño de sistema + creación de material inicial. |
| 3 | Necesidad de audiencia previa | 2 | [Inferencia] Requiere alcanzar devs hispanohablantes. Comunidades como FreeCodeCamp Español, platzi, etc. existen. |
| 4 | Credibilidad del fundador | 2 | [Inferencia] El fundador usa inglés técnico pero NO es profesor de inglés, lingüista, ni tiene certificación de enseñanza. Usar inglés ≠ saber enseñarlo. |
| 5 | Riesgo legal/regulatorio | 5 | [Hecho] Ningún riesgo. |
| 6 | Precio posible | 3 | [Hipótesis] $29-79. Rango de cursos de idiomas especializados online. |
| 7 | Posibilidad de preventa | 2 | [Inferencia] Posible con landing page dirigida a devs, pero sin credibilidad pedagógica la conversión será baja. |
| 8 | Entrega manual inicial | 4 | [Inferencia] Puede ser documento + ejercicios + recursos curados. |
| 9 | Automatización futura | 4 | [Inferencia] Alto potencial: app, bot, LLM-powered practice. Conecta con English Learning Lab. |
| 10 | Recurrencia potencial | 3 | [Hipótesis] Modelo de suscripción mensual con contenido nuevo viable a largo plazo. |
| 11 | Escalabilidad | 4 | [Hecho] Producto digital. |
| 12 | Ajuste con proyectos LabOS | 3 | [Hecho] Conecta con English Learning Lab (estado: idea). |
| 13 | Evidencia de mercado rápida | 2 | [Hipótesis] Podría postearse en comunidades de devs hispanohablantes, pero sin credibilidad pedagógica la señal será débil. |

**Fortalezas:** Mercado potencialmente grande (devs LATAM); alto potencial de automatización futura con IA.
**Debilidades:** Sin credibilidad pedagógica; alto esfuerzo de creación; sin señal de demanda directa.
**Riesgo principal:** Que el mercado no valore la perspectiva de "dev que usa inglés" vs profesores certificados de inglés.

---

### O6: Servicio de generación de contenido especializado (CommunityManagerBotCrew)

**Descripción:** Servicio donde el fundador utiliza su sistema de automatización de contenido (CommunityManagerBotCrew) para generar y gestionar contenido de redes sociales/blog para clientes (startups, solopreneurs técnicos). Entregable: calendario de contenido + posts generados + scheduling.

**Base de evidencia:**
- [Hecho] El fundador tiene el proyecto CommunityManagerBotCrew desarrollado/en desarrollo.
- [Inferencia] El mercado de content-as-a-service existe y crece con herramientas IA.
- [Hipótesis] Startups y solopreneurs pagarían $200-800/mes por gestión de contenido automatizada.
- [Evidencia pendiente] No hay evidencia de que CommunityManagerBotCrew esté en estado funcional suficiente para entregar a clientes externos. No hay caso de uso exitoso documentado.

| # | Criterio | Score | Justificación |
|---|----------|-------|---------------|
| 1 | Tiempo hasta poder vender | 3 | [Hipótesis] 10-20 días. Depende del estado actual de CommunityManagerBotCrew. Si está funcional, rápido. Si no, requiere desarrollo. |
| 2 | Esfuerzo inicial | 3 | [Hipótesis] 20-30 horas. Configurar para uso externo + definir oferta + crear samples. |
| 3 | Necesidad de audiencia previa | 2 | [Inferencia] Requiere encontrar clientes que confíen en automatización de contenido con IA. Mercado saturado por herramientas SaaS. |
| 4 | Credibilidad del fundador | 3 | [Inferencia] Credibilidad técnica en IA/automatización es media. No tiene portfolio de contenido exitoso para mostrar. La credibilidad es en construcción de herramientas, no en resultados de marketing. |
| 5 | Riesgo legal/regulatorio | 4 | [Hecho] Bajo riesgo. Posible issue con content ownership en contrato. |
| 6 | Precio posible | 4 | [Hipótesis] $200-800/mes por cliente (servicio recurrente). |
| 7 | Posibilidad de preventa | 3 | [Hipótesis] Posible ofreciendo prueba gratuita de 1 semana o muestra de contenido generado. |
| 8 | Entrega manual inicial | 3 | [Inferencia] Requiere mezcla de automatización + curación manual. No es 100% manual ni 100% automatizado. |
| 9 | Automatización futura | 5 | [Hecho] El proyecto CommunityManagerBotCrew está diseñado para automatización. |
| 10 | Recurrencia potencial | 5 | [Hecho] Servicio inherentemente recurrente (mensual). |
| 11 | Escalabilidad | 3 | [Inferencia] Escala con automatización, pero requiere supervisión de calidad por cliente. |
| 12 | Ajuste con proyectos LabOS | 5 | [Hecho] Usa directamente CommunityManagerBotCrew. |
| 13 | Evidencia de mercado rápida | 3 | [Hipótesis] Ofrecer servicio gratuito a 2-3 contactos y medir si están dispuestos a pagar después de ver resultados. |

**Fortalezas:** Ingreso recurrente; usa proyecto existente; alta automatización futura.
**Debilidades:** Sin evidencia de que la herramienta está lista para clientes; mercado saturado de herramientas de content; requiere demostrar resultados de marketing (no solo técnicos).
**Riesgo principal:** Que CommunityManagerBotCrew no esté en estado production-ready y se necesite invertir tiempo en desarrollo antes de poder vender.

---

### O7: Template LabOS para profesionales o pequeñas empresas

**Descripción:** Pack de templates de LabOS adaptado para uso externo: sistema de gestión de conocimiento, decision logs, research framework simplificado, asset tracking. Dirigido a solopreneurs técnicos y equipos pequeños de I+D.

**Base de evidencia:**
- [Hecho] LabOS tiene documentación estructurada y completa (Package 000 y 001).
- [Hecho] Los templates para fundadores técnicos están definidos como Ruta 2 en 008-business-model.md.
- [Inferencia] Fundadores técnicos buscan estructura operativa sin construirla desde cero.
- [Hipótesis] Solopreneurs pagarían $29-79 por un pack de templates de gestión.
- [Evidencia pendiente] NO hay señal de demanda externa. LabOS no tiene usuarios externos ni validación de mercado. El fundador no ha publicado nada sobre LabOS en ninguna comunidad.

| # | Criterio | Score | Justificación |
|---|----------|-------|---------------|
| 1 | Tiempo hasta poder vender | 3 | [Hipótesis] 14-21 días. Requiere adaptar documentación interna a formato vendible + setup plataforma. |
| 2 | Esfuerzo inicial | 3 | [Hipótesis] 25-35 horas. Adaptar, simplificar y empaquetar templates internos para audiencia externa. |
| 3 | Necesidad de audiencia previa | 2 | [Inferencia] Sin audiencia de solopreneurs/fundadores técnicos, depende de distribución en Indie Hackers, Twitter, Product Hunt. |
| 4 | Credibilidad del fundador | 2 | [Inferencia] La credibilidad en "sistema operativo para empresas de conocimiento" es baja externamente. LabOS no tiene caso de éxito público ni usuarios que lo validen. |
| 5 | Riesgo legal/regulatorio | 5 | [Hecho] Ningún riesgo. |
| 6 | Precio posible | 2 | [Hipótesis] $29-79. Competencia con templates gratuitos (Notion, segundobrain) reduce willingness-to-pay. |
| 7 | Posibilidad de preventa | 2 | [Inferencia] Sin track record público de LabOS, la preventa depende de la calidad del pitch, no de evidencia. |
| 8 | Entrega manual inicial | 5 | [Hecho] 100% documento digital. |
| 9 | Automatización futura | 3 | [Inferencia] Podría evolucionar a SaaS pero es prematuro. |
| 10 | Recurrencia potencial | 2 | [Inferencia] One-shot. Posible upgrade path a comunidad/suscripción pero especulativo. |
| 11 | Escalabilidad | 4 | [Hecho] Producto digital. |
| 12 | Ajuste con proyectos LabOS | 5 | [Hecho] ES LabOS directamente. |
| 13 | Evidencia de mercado rápida | 2 | [Hipótesis] Difícil sin audiencia. Publicar en Indie Hackers/Product Hunt podría dar señal pero requiere credibilidad previa. |

**Fortalezas:** Material existente; máximo ajuste con LabOS; escalable.
**Debilidades:** Sin validación externa de LabOS; sin audiencia; competencia con templates gratuitos; credibilidad baja en el dominio de "sistemas de gestión" sin casos de éxito.
**Riesgo principal:** Vender templates de un sistema que ni siquiera ha demostrado funcionar para el propio fundador (still building it). Violación del principio de "no vender lo que no has validado".

---

### O8: Micro-consulting DevOps/K8s/Incident Response por sesión

**Descripción:** Sesiones de consulting de 60-90 minutos donde el fundador ayuda a resolver problemas específicos de DevOps, Kubernetes, pipelines CI/CD, o incident response. Pago por sesión adelantado. Incluye resumen escrito post-sesión.

**Base de evidencia:**
- [Hecho] El fundador tiene experiencia enterprise en K8s, DevOps, incident response.
- [Hecho] Plataformas como Clarity.fm, MentorCruise y Superpeer validan el modelo de micro-consulting pagado.
- [Inferencia] Developers y DevOps engineers enfrentan problemas urgentes donde 60 min con un experto ahorran días de debugging.
- [Hipótesis] $100-250 por sesión es viable para DevOps/SRE consulting.
- [Evidencia pendiente] No hay evidencia de que el fundador pueda atraer clientes a sesiones sin presencia online previa en el dominio.

| # | Criterio | Score | Justificación |
|---|----------|-------|---------------|
| 1 | Tiempo hasta poder vender | 5 | [Hecho] 3-5 días. Solo requiere: crear perfil en plataforma (Clarity.fm, MentorCruise) o página de booking (Cal.com) + definir precio + publicar disponibilidad. |
| 2 | Esfuerzo inicial | 5 | [Hecho] 5-8 horas. Crear página de booking, definir oferta, preparar template de resumen post-sesión. |
| 3 | Necesidad de audiencia previa | 3 | [Inferencia] Plataformas como MentorCruise/Clarity.fm tienen audiencia built-in. LinkedIn outreach a DevOps engineers es alcanzable sin audiencia propia. |
| 4 | Credibilidad del fundador | 5 | [Hecho] Credibilidad máxima en DevOps/K8s/incident response. Experiencia enterprise directa. |
| 5 | Riesgo legal/regulatorio | 5 | [Hecho] Ningún riesgo. |
| 6 | Precio posible | 4 | [Hipótesis] $100-250/sesión. Menor por unidad que auditoría completa pero con menor barrera de entrada para el comprador. |
| 7 | Posibilidad de preventa | 5 | [Hecho] Inherente al modelo: se vende ANTES de entregar. El cliente agenda y paga, luego ocurre la sesión. |
| 8 | Entrega manual inicial | 5 | [Hecho] 100% manual por definición. Es una conversación + resumen escrito. |
| 9 | Automatización futura | 2 | [Inferencia] Limitada. El valor está en la interacción humana. Puede automatizarse el scheduling y el seguimiento, no la sesión en sí. |
| 10 | Recurrencia potencial | 3 | [Hipótesis] Clientes satisfechos pueden volver con nuevos problemas. No es suscripción pero tiene repeat purchase potencial. |
| 11 | Escalabilidad | 1 | [Hecho] Limitado por las horas del fundador. 1 sesión = 1.5-2 horas de tiempo (prep + sesión + resumen). |
| 12 | Ajuste con proyectos LabOS | 4 | [Hecho] Usa experiencia de SentinelOps/DevOps. Cada sesión genera conocimiento reutilizable (patterns de problemas). |
| 13 | Evidencia de mercado rápida | 5 | [Hecho] Plataformas como Clarity.fm muestran demanda visible. Publicar disponibilidad + primer post en comunidad = señal en <7 días. |

**Fortalezas:** MÍNIMO tiempo a primera venta; mínimo esfuerzo inicial; máxima credibilidad; preventa natural; evidencia de mercado inmediata; plataformas con audiencia built-in.
**Debilidades:** No escala; bajo ingreso por hora si el volumen es bajo; requiere disponibilidad en horarios del cliente.
**Riesgo principal:** Que el volumen de sesiones sea insuficiente para generar ingreso significativo (1-2 sesiones/semana × $100-250 = $400-2000/mes).

---

## 4. Matriz de Evaluación Consolidada

### Scoring sin ponderar (raw scores)

| Criterio | O1 | O2 | O3 | O4 | O5 | O6 | O7 | O8 |
|----------|----|----|----|----|----|----|----|----|
| 1. Tiempo a venta | 3 | 4 | 3 | 2 | 2 | 3 | 3 | **5** |
| 2. Esfuerzo inicial | 3 | 4 | 3 | 2 | 2 | 3 | 3 | **5** |
| 3. Audiencia previa | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 3 |
| 4. Credibilidad | **5** | **5** | 2 | 1 | 2 | 3 | 2 | **5** |
| 5. Riesgo legal | 5 | 4 | 5 | 3 | 5 | 4 | 5 | 5 |
| 6. Precio posible | 3 | **5** | 2 | 3 | 3 | 4 | 2 | 4 |
| 7. Preventa | 3 | 4 | 2 | 1 | 2 | 3 | 2 | **5** |
| 8. Entrega manual | 5 | 5 | 5 | 4 | 4 | 3 | 5 | 5 |
| 9. Automatización | 3 | 4 | 3 | 3 | 4 | **5** | 3 | 2 |
| 10. Recurrencia | 2 | 3 | 1 | 2 | 3 | **5** | 2 | 3 |
| 11. Escalabilidad | 4 | 2 | 4 | 4 | 4 | 3 | 4 | 1 |
| 12. Ajuste LabOS | 4 | **5** | 5 | 2 | 3 | **5** | **5** | 4 |
| 13. Evidencia rápida | 3 | 3 | 2 | 1 | 2 | 3 | 2 | **5** |
| **Total (raw)** | **45** | **50** | **39** | **29** | **38** | **46** | **40** | **52** |

### Scoring ponderado (criterios 1, 4, 13 con peso ×2)

| Oportunidad | Raw | Bonus (×2 en C1+C4+C13) | Total Ponderado | Rank |
|-------------|-----|--------------------------|-----------------|------|
| **O8** Micro-consulting DevOps | 52 | +5+5+5 = +15 | **67** | **🥇 1°** |
| **O2** Auditoría DevOps | 50 | +4+5+3 = +12 | **62** | **🥈 2°** |
| **O1** Playbook K8s/EKS | 45 | +3+5+3 = +11 | **56** | **🥉 3°** |
| **O6** Contenido Bot | 46 | +3+3+3 = +9 | **55** | 4° |
| **O7** Template LabOS | 40 | +3+2+2 = +7 | **47** | 5° |
| **O3** Template research | 39 | +3+2+2 = +7 | **46** | 6° |
| **O5** Inglés técnico | 38 | +2+2+2 = +6 | **44** | 7° |
| **O4** Entrenamiento 35-50 | 29 | +2+1+1 = +4 | **33** | 8° |

---

## 5. Top 3 — Análisis de Viabilidad

### 🥇 O8: Micro-consulting DevOps/K8s/Incident Response

**Por qué es #1:**
- Mínimo tiempo a primera venta (3-5 días) [Hecho — el setup es trivial]
- Mínimo esfuerzo inicial (5-8 horas) [Hecho — solo requiere página de booking]
- Máxima credibilidad (experiencia enterprise directa) [Hecho]
- Preventa natural (el cliente paga antes de la sesión) [Hecho — así funcionan estas plataformas]
- Evidencia de mercado inmediata (plataformas con audiencia built-in) [Hecho]
- Alineación perfecta con Package 000 Ruta 3 (micro-consulting) [Hecho]

**Limitación honesta:** No escala. Si funciona, genera $400-2000/mes con volumen bajo (2-8 sesiones/mes). Pero cumple el objetivo de PRIMER INGRESO con mínimo riesgo. [Inferencia]

### 🥈 O2: Auditoría productizada de DevOps/Pipelines

**Por qué es #2:**
- Precio alto ($500-1500) maximiza ingreso por cliente [Hipótesis]
- Credibilidad máxima en el dominio [Hecho]
- Modelo sell-first-build-later natural [Hecho]
- Complementa O8: un cliente de micro-consulting puede convertirse en cliente de auditoría [Inferencia]

**Limitación honesta:** Ciclo de venta B2B más largo. Conseguir el primer cliente puede tomar >14 días sin red de contactos empresariales previa. [Inferencia]

### 🥉 O1: Playbook de troubleshooting K8s/EKS

**Por qué es #3:**
- Máxima credibilidad del fundador en el dominio [Hecho]
- Producto digital escalable (crear una vez, vender muchas) [Hecho]
- Puede construirse incrementalmente mientras se hacen O8 y O2 [Inferencia]
- Las sesiones de O8 generan contenido para el playbook (cada problema resuelto = sección nueva) [Inferencia]

**Limitación honesta:** Requiere 30-40h de producción antes de la primera venta. Sin audiencia, la distribución es el mayor riesgo. [Hipótesis]

---

## 6. Señales de Demanda — Evaluación Honesta

### Con señal de demanda observable (débil pero existente):

| Oportunidad | Señal | Clasificación |
|-------------|-------|---------------|
| O8 | Plataformas de micro-consulting (MentorCruise, Clarity.fm) tienen consultores DevOps activos con reviews, lo que indica demanda por el formato | [Hecho] — observable en las plataformas |
| O2 | Upwork/Fiverr tienen categoría de "DevOps consulting" con freelancers activos y proyectos | [Hecho] — observable en plataformas freelance |
| O1 | Preguntas frecuentes sobre troubleshooting K8s en StackOverflow, Reddit (r/kubernetes tiene 200k+ miembros) | [Hecho] — pero preguntas gratuitas ≠ willingness to pay |

### Sin señal de demanda externa verificable:

| Oportunidad | Status | Nota |
|-------------|--------|------|
| O3 | ❌ Sin señal | La necesidad del fundador NO es señal externa |
| O4 | ❌ Sin señal | Interés personal ≠ demanda externa para el fundador |
| O5 | ❌ Sin señal | Mercado potencial inferido, pero sin observación directa |
| O6 | ❌ Sin señal | Herramienta interna sin casos de uso externos documentados |
| O7 | ❌ Sin señal | LabOS no tiene usuarios externos ni publicación |

**Conclusión de demanda:** Solo O8, O2 y O1 tienen alguna señal de demanda externa observable. Las demás son puramente especulativas desde la perspectiva de demanda. [Inferencia]

---

## 7. Estrategia Recomendada: Stack Secuencial

La recomendación no es elegir UNA oportunidad en aislamiento, sino un **stack secuencial** que maximiza aprendizaje y genera activos reutilizables:

```
Semana 1-2: O8 (Micro-consulting) → VALIDAR demanda + generar primer ingreso
     ↓ (cada sesión genera conocimiento)
Semana 3-4: O1 (Playbook K8s) → PRODUCIR con base en problemas reales de O8
     ↓ (clientes de O8 pueden referir para...)
Mes 2:      O2 (Auditoría DevOps) → ESCALAR a servicio de mayor ticket
```

**Justificación del stack:**
1. O8 requiere mínima inversión y genera señal inmediata. [Hecho]
2. O8 alimenta O1: cada sesión revela problemas comunes que se documentan en el playbook. [Inferencia]
3. O8 puede generar leads para O2: un cliente que compra 60 min probablemente necesita una auditoría más profunda. [Hipótesis]
4. Los tres operan en el MISMO dominio de máxima credibilidad del fundador. [Hecho]

---

## 8. Tabla Epistémica del Análisis

| Clasificación | Cantidad (claims materiales) | Porcentaje |
|---------------|------------------------------|------------|
| [Hecho] | ~40 | 35% |
| [Hipótesis] | ~45 | 39% |
| [Inferencia] | ~25 | 22% |
| [Evidencia pendiente] | ~5 | 4% |

> **Nota:** El alto porcentaje de hipótesis es esperado — estamos evaluando oportunidades no validadas. La recomendación se fundamenta principalmente en los hechos (credibilidad del fundador + existencia de plataformas + bajo costo de validación), no en las hipótesis de pricing o volumen.

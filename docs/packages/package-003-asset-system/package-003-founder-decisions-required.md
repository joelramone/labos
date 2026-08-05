# Decisiones del Fundador Requeridas — Package 003

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Founder Decisions Required |
| **Package** | 003 — Asset System |
| **Fecha** | 2025-07-31 |
| **Autor** | Principal Architect (LabOS) |
| **Estado** | READY_FOR_FOUNDER_REVIEW |

---

## Resumen

La revisión del Principal Architect (v1.2) no identificó decisiones de fundador bloqueantes que requieran resolución antes de aprobar los requerimientos. Las correcciones C9–C12 aplicadas en esta revisión resolvieron las 4 ambigüedades que hubieran requerido decisión.

**Decisiones de fundador pendientes identificadas: 0 (cero bloqueantes)**

Las siguientes son **decisiones opcionales** que el fundador puede tomar en algún momento, pero que no bloquean la aprobación del documento de requerimientos ni el inicio del diseño.

---

## Decisión Opcional 1: Techo de escala para el ciclo de métricas

| Campo | Valor |
|-------|-------|
| **Question ID** | OD-001 |
| **Decisión exacta** | ¿A partir de cuántos Assets CANONICAL activos el límite de 60 min/ciclo del ciclo de métricas (R11.3) debe revisarse? |
| **Recomendación** | Aplicar el límite de 60 min hasta 20 Assets CANONICAL activos. Más allá de ese número, revisar el proceso de métricas para priorizar solo assets con reutilización activa. |
| **Alternativas** | (a) No definir techo — el fundador ajusta según su criterio en cada ciclo. (b) Definir techo en 30 o 50 Assets. |
| **Trade-offs** | Sin techo: más flexible pero sin señal de alerta. Con techo: más predecible y genera trigger de revisión. |
| **Requerimientos afectados** | R11.3 |
| **Estado de bloqueo** | No bloqueante — puede decidirse en operación cuando el número de Assets sea relevante |

---

## Decisión Opcional 2: Notificación de defectos en contexto SOLO

| Campo | Valor |
|-------|-------|
| **Question ID** | OD-002 |
| **Decisión exacta** | ¿Debe R9.5 (obligación del consumidor de notificar defectos en 7 días) aplicarse en contexto SOLO donde el fundador es simultáneamente consumidor y Asset_Owner? |
| **Recomendación** | Convertir en recomendación con nota: "En contexto SOLO, esta obligación se convierte en práctica recomendada. Se vuelve obligatoria cuando haya consumidores externos activos." |
| **Alternativas** | (a) Mantener como obligación incluso en SOLO (auto-notificación). (b) Eliminar completamente. |
| **Trade-offs** | Mantener crea burocracia contra uno mismo. Eliminar deja un gap cuando haya consumidores externos futuros. La recomendación es la opción de bajo costo. |
| **Requerimientos afectados** | R9.5 |
| **Estado de bloqueo** | No bloqueante |

---

## Decisión Opcional 3: Tipo canónico fijo vs modificable

| Campo | Valor |
|-------|-------|
| **Question ID** | OD-003 |
| **Decisión exacta** | ¿Puede el tipo canónico de un Asset cambiar después de su primera promoción a CANONICAL? Si sí, ¿bajo qué condiciones? |
| **Recomendación** | El tipo canónico es fijo al momento de la primera promoción a CANONICAL. Un cambio de tipo solo se permite creando un nuevo Asset (con nuevo asset_id y provenance que referencia el original), o mediante una versión MAJOR acompañada de justificación documentada de por qué el tipo original era incorrecto. |
| **Alternativas** | (a) Permitir cambio de tipo libremente (sin restricciones). (b) Prohibir cambio de tipo absolutamente. |
| **Trade-offs** | Libre: flexible pero rompe la identidad del Asset. Prohibición absoluta: puede crear rigidez cuando el tipo fue mal asignado inicialmente. La recomendación equilibra ambas. |
| **Requerimientos afectados** | R2 |
| **Estado de bloqueo** | No bloqueante |

---

## Confirmación de Decisiones Previas Satisfechas

Las siguientes preguntas críticas del enunciado de revisión tienen respuesta explícita en el documento actualizado y no requieren decisión adicional del fundador:

| Pregunta | Respuesta | Fuente |
|----------|-----------|--------|
| ¿Qué condición convierte un Artefacto en Asset Candidate? | Cumplir 5 campos mínimos + señal documentada de potencial de reutilización | R1.2, R3.2 |
| ¿Qué condición convierte un Candidate en Canonical? | Superar quality gates de R5 + aprobación explícita del Fundador | R3.4-5, R18.1 |
| ¿Puede un Asset ser canonical y Lab-private? | Sí — son dimensiones ortogonales | R3.1 (C6, C9) |
| ¿Es "shared" un estado, scope o relación? | Atributo/scope ortogonal al lifecycle state | R3.1, Glosario |
| ¿Es "product_attachment" un estado? | No — es asociación externa | R3.1, Glosario |
| ¿Es "rejected" terminal? | Sí — sin retorno sin nuevo registro | R3.12 |
| ¿Cómo se representan Assets derivados? | Nuevo asset_id, provenance que referencia original | R8.7 (C8) |
| ¿Cómo difiere un fork de una nueva versión? | Fork = nuevo asset_id, desarrollo independiente; versión = mismo asset_id | R8.7 (C8) |
| ¿Puede un Asset tener múltiples owners? | No — exactamente un Asset_Owner; R6.8 para transferencia | R14.1, R6.8 |
| ¿Quién es Canonical Authority post cross-Lab? | El originating_Lab retiene autoridad hasta ADR de co-governance | R6.9 (C12) |
| ¿Cómo se manejan componentes externos licenciados? | Se registran como referencias con licencia original, no se reclasifican como Assets | R6.5 |
| ¿Qué ocurre cuando el KO fuente es disputed? | Review flag informativo sin invalidar lifecycle state | R20.7 (C7) |
| ¿Qué evidencia mínima se requiere para reutilización? | Forma A (1 uso documentado) o Forma B (declaración diseñada-para-reuso) | R4.1 (C2) |
| ¿Cómo se demuestra reutilización antes del primer uso? | Forma B — declaración escrita con Lab/dominio destino específico | R4.1 (C2) |
| ¿Puede un Asset ser valioso sin cross-Lab reuse? | Sí — Assets Lab-Private tienen valor local documentable | R11.4 (C3), R10 |
| ¿Puede un Product depender de un Asset no canonical? | No — product_attachment requiere estado CANONICAL explícito | R14.1 |
| ¿Qué condiciones bloquean publicación externa? | Ver R5.2 (gates para Cross-Lab/Public), R4.3, R18.1 | R5.2, R18 |
| ¿Cómo se retira un Asset sin romper Products? | Período de gracia, plan de migración, notificación previa | R9.6, R12.3, R14.4 |
| ¿Cuánto overhead genera el sistema para 1 fundador? | LIGHTWEIGHT-MODERATE; ningún workflow HEAVY en operación continua | Sección 14 del Review |

---

## Acción Requerida del Fundador

La única acción requerida del fundador es:

**Revisar y aprobar el documento requirements.md v1.2** con las correcciones C9–C12 aplicadas.

Una vez aprobado, el fundador puede autorizar el inicio de la fase de Diseño (Design document) de Package 003.


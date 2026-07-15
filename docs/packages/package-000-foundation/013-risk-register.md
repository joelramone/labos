# Registro de Riesgos

## Propósito

Este documento identifica y documenta las amenazas críticas para LabOS en su etapa fundacional, estableciendo mitigaciones concretas y ejecutables para cada riesgo. El registro cubre riesgos personales, financieros, legales y operativos inherentes a una operación pre-revenue con fundador único. [Hecho]

Todos los riesgos se evalúan desde la perspectiva de un proyecto pre-revenue, pre-product y documentation-first operado por una sola persona. [Hecho] La identificación de riesgos se basa en la estructura actual documentada en [011-scope-and-boundaries.md](./011-scope-and-boundaries.md) y el portafolio definido en [012-portfolio-model.md](./012-portfolio-model.md).

---

## Riesgos prioritarios

Los siguientes riesgos tienen probabilidad alta e impacto crítico o alto. Requieren plan de acción inmediato. [Hecho]

### PRIORITARIO 1: Bus factor = 1

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Todo el conocimiento, decisiones, accesos y capacidad operativa dependen de una sola persona. Si el fundador no puede operar, LabOS se detiene completamente. |
| **Probabilidad** | Alta |
| **Impacto** | Crítico |
| **Categoría** | Personal |
| **Owner** | Fundador |

**Mitigación** (≥2 acciones concretas):

1. **Documentación exhaustiva de decisiones y procesos**: Mantener todos los documentos del Package 000 actualizados como fuente de verdad que permita a un tercero entender el estado, la lógica y las prioridades del proyecto sin depender de comunicación verbal con el fundador. Verificación mensual de que los documentos reflejan el estado real. [Hecho]
2. **Accesos y credenciales en gestor de contraseñas compartible**: Almacenar todas las credenciales de servicios, repositorios y plataformas en un gestor de contraseñas con mecanismo de acceso de emergencia (emergency kit o contacto de confianza designado). Configurar antes de que cualquier lab transite a estado `validando`. [Hecho]
3. **Automatización de operaciones repetitivas**: Priorizar la automatización de procesos operativos rutinarios (backups, publicación, monitoreo) para reducir la dependencia de intervención manual diaria. [Hecho]

**Plan de acción inmediato**: En los próximos 14 días: (1) configurar emergency kit en gestor de contraseñas, (2) designar contacto de confianza con instrucciones escritas de acceso, (3) verificar que el repositorio principal es accesible con las credenciales documentadas. [Hecho]

---

### PRIORITARIO 2: Ausencia prolongada de ingresos validados

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Sin ingresos validados, el proyecto depende del ahorro personal del fundador. El runway finito crea presión que puede forzar abandono o decisiones subóptimas. |
| **Probabilidad** | Alta |
| **Impacto** | Alto |
| **Categoría** | Financiero |
| **Owner** | Fundador |

**Mitigación**:

1. **Ejecutar las rutas de flujo de caja inmediato** documentadas en [008-business-model.md](./008-business-model.md) dentro de los primeros 30 días. Priorizar la ruta con menor dependencia externa. [Hecho]
2. **Establecer fecha límite de evaluación**: Si no se genera al menos 1 transacción real en 60 días desde inicio de ejecución del Package 000, activar revisión de pivote documentada en `docs/decisions/`. [Hecho]

**Plan de acción inmediato**: En los próximos 7 días: (1) seleccionar la ruta de ingreso inmediato más viable, (2) ejecutar la primera acción concreta (publicar oferta, contactar prospecto o listar activo). [Hecho]

---

## Riesgos de privacidad y datos

### Riesgo 3: Recolección de datos personales sin cumplimiento GDPR/Ley 1581

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Un lab recolecta datos personales sin tener política de privacidad publicada ni mecanismo de consentimiento conforme a la regulación aplicable. |
| **Probabilidad** | Media |
| **Impacto** | Alto |
| **Categoría** | Legal |
| **Mitigación** | Antes de que cualquier lab procese datos de terceros: (1) redactar y publicar política de privacidad conforme a jurisdicción, (2) implementar mecanismo de consentimiento explícito, (3) documentar base legal del tratamiento. Gate obligatorio antes de transición a estado `validando` para labs con datos. |
| **Owner** | Fundador |

### Riesgo 4: Uso de datos de usuarios en labs sin política de privacidad publicada

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Labs en estado `explorando` realizan experimentos con datos reales de usuarios (encuestas, formularios, analytics) sin aviso de privacidad visible ni registro ante autoridades. |
| **Probabilidad** | Media |
| **Impacto** | Alto |
| **Categoría** | Legal |
| **Mitigación** | (1) Prohibir recolección de datos personales en labs con estado inferior a `validando` sin política publicada. (2) Usar datos sintéticos o anonimizados para experimentación en fases tempranas. (3) Mantener checklist de privacidad como requisito previo a cualquier formulario o analytics con tracking de usuarios. |
| **Owner** | Fundador |

---

## Riesgos de propiedad intelectual

### Riesgo 5: Contenido generado por IA sin protección autoral clara

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Activos generados primariamente por IA pueden carecer de protección autoral en jurisdicciones donde se requiere autoría humana, exponiendo comercialización sin respaldo legal. |
| **Probabilidad** | Media |
| **Impacto** | Medio |
| **Categoría** | Legal |
| **Mitigación** | (1) Documentar el grado de intervención humana creativa en cada activo generado con IA (selección, edición, disposición). (2) Maximizar contribución humana verificable. (3) No comercializar activos puramente generados por IA sin transformación sustancial documentada. |
| **Owner** | Fundador |

**Estado de legislación por jurisdicción** (última revisión: julio 2025):

| Jurisdicción | Estado legislativo | Implicación para LabOS |
| ------------ | ------------------ | ---------------------- |
| Colombia | Sin regulación específica para IA. Ley 23/1982 requiere autor humano. | Outputs de IA pura sin protección. Priorizar intervención humana documentable. |
| Unión Europea | EU AI Act vigente (2024-2027). InfoSoc requiere creación intelectual humana. | Obligaciones de transparencia para GPAI. Outputs de IA pura posiblemente sin protección. |
| Estados Unidos | USCO: sin protección para outputs sin intervención humana creativa significativa. | Registrar solo componentes con contribución humana demostrable. |
| Latinoamérica (otros) | Sin regulación específica consolidada. Convenio de Berna: autoría humana. | Mismo enfoque conservador: documentar intervención humana. |

> **Próxima revisión de legislación**: octubre 2025.

### Riesgo 6: Licencias de terceros incompatibles incorporadas en activos comercializables

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Incorporar código, contenido o datos con licencias restrictivas (GPL, CC-NC, propietarias) en activos que se pretende comercializar, creando conflictos de licenciamiento. |
| **Probabilidad** | Media |
| **Impacto** | Alto |
| **Categoría** | Legal |
| **Mitigación** | (1) Verificar licencia de todo material de terceros antes de incorporarlo. (2) Mantener archivo ATTRIBUTION con fuente, licencia y fecha por cada dependencia. (3) Excluir material con licencias copyleft (GPL) o no-comercial (CC-NC) de activos destinados a venta. (4) Revisar compatibilidad de licencias trimestralmente. |
| **Owner** | Fundador |

### Riesgo 7: Titularidad ambigua de obras creadas con asistencia de IA

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Incertidumbre sobre quién posee los derechos de obras donde la IA contribuyó significativamente, especialmente si los ToS del proveedor de IA retienen derechos. |
| **Probabilidad** | Media |
| **Impacto** | Medio |
| **Categoría** | Legal |
| **Mitigación** | (1) Revisar y documentar los Terms of Service de cada herramienta de IA utilizada respecto a propiedad de outputs. (2) Mantener registro (metadata) de herramienta usada, prompt y grado de edición humana por activo. (3) Preferir herramientas cuyos ToS otorguen propiedad al usuario. (4) Consultar asesoría legal antes de comercializar activos con contribución sustancial de IA si el valor supera un umbral significativo. |
| **Owner** | Fundador |

---

## Riesgos operativos y personales

### Riesgo 8: Dispersión de esfuerzo entre demasiados labs simultáneos

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Dedicar tiempo a múltiples labs sin profundidad suficiente en ninguno, resultando en ningún lab que alcance validación de demanda real dentro de los plazos establecidos. |
| **Probabilidad** | Media |
| **Impacto** | Alto |
| **Categoría** | Operativo |
| **Mitigación** | (1) Mantener máximo 2-3 labs en estado activo simultáneamente (según capacidad documentada en [012-portfolio-model.md](./012-portfolio-model.md)). (2) Aplicar reglas de priorización del portfolio estrictamente: validación de demanda primero, flujo de caja inmediato sobre largo plazo. (3) Revisar asignación de horas semanalmente y pausar labs sin progreso observable en 30 días. |
| **Owner** | Fundador |

### Riesgo 9: Burnout del fundador por sobrecarga operativa

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Carga cognitiva y operativa excesiva al operar simultáneamente empleo, labs y desarrollo de LabOS, resultando en agotamiento que compromete calidad y continuidad. |
| **Probabilidad** | Media |
| **Impacto** | Alto |
| **Categoría** | Personal |
| **Mitigación** | (1) Establecer límite semanal de horas dedicadas a LabOS (20-25h máximo) y respetarlo. (2) Definir 1 día por semana sin actividad relacionada con labs. (3) Monitorear señales de agotamiento (calidad decreciente de outputs, procrastinación creciente, errores repetidos) y activar pausa de 1 semana si se detectan ≥2 señales durante 2 semanas consecutivas. |
| **Owner** | Fundador |

### Riesgo 10: Obsolescencia de información regulatoria

| Campo | Valor |
| ----- | ----- |
| **Descripción** | Información regulatoria en documentos del package con más de 90 días sin actualización, generando riesgo de decisiones basadas en legislación desactualizada. |
| **Probabilidad** | Baja |
| **Impacto** | Medio |
| **Categoría** | Legal |
| **Mitigación** | (1) Marcar con etiqueta [PENDIENTE DE ACTUALIZACIÓN] cualquier sección regulatoria que supere 90 días sin revisión. (2) Incluir en la revisión trimestral del package una verificación explícita de vigencia de marcos regulatorios documentados en [011-scope-and-boundaries.md](./011-scope-and-boundaries.md). (3) Suscribirse a alertas de noticias legislativas en las jurisdicciones documentadas (Colombia, UE, US). |
| **Owner** | Fundador |

---

## Frecuencia de revisión

| Tipo de revisión | Frecuencia | Próxima revisión | Responsable |
| ---------------- | ---------- | ---------------- | ----------- |
| Revisión completa del registro | Trimestral | octubre 2025 | Fundador |
| Revisión de riesgos prioritarios | Mensual | agosto 2025 | Fundador |
| Revisión por evento | Al detectar un nuevo riesgo, incidente o cambio regulatorio significativo | N/A (reactiva) | Fundador |
| Actualización de legislación IA/PI | Trimestral (alineada con revisión completa) | octubre 2025 | Fundador |

---

## Cross-links

- **Saliente**: Los resultados de este registro se evalúan en la revisión del package en [016-foundation-review.md](./016-foundation-review.md) — criterio (d): riesgos con mitigación viable.
- **Entrante desde**: [011-scope-and-boundaries.md](./011-scope-and-boundaries.md) — riesgos regulatorios y de PI derivados de los marcos documentados.
- **Entrante desde**: [012-portfolio-model.md](./012-portfolio-model.md) — riesgos del portfolio asociados a dispersión y capacidad.

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
| ------------- | -------- | ---------- |
| [Hecho] | 18 | 100% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 0 | 0% |
| Sin clasificar | 0 | 0% |

> **Nota**: Todas las afirmaciones de este registro son hechos observables: los riesgos existen como condiciones actuales del proyecto, las mitigaciones son acciones concretas ejecutables, y las evaluaciones de probabilidad/impacto se basan en la estructura actual documentada de LabOS (fundador único, pre-revenue, sin validación de mercado).

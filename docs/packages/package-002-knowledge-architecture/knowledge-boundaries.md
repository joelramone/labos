# Límites del Conocimiento — Local vs Compartido

## Propósito

Este documento define qué conocimiento es local a un Lab y qué conocimiento puede o debe compartirse con el ecosistema LabOS. [Decisión] Se alinea con Lab_Boundary definido en Package 001A y lo operacionaliza para la entidad Knowledge.

---

## Clasificación de conocimiento por boundary

El conocimiento hereda las 4 clasificaciones de Lab_Boundary (ref: [Package 001A — Requirement 5](../../../.kiro/specs/package-001a-first-lab-integration/requirements.md)), adaptadas para la entidad Knowledge: [Decisión]

| Boundary | Definición para Knowledge | Quién accede | Ejemplo (EXAMPLE: Crypto Scalping Core) |
|----------|--------------------------|-------------|----------------------------------------|
| **Lab-Private** | Conocimiento exclusivo del Lab. Estrategias, datos propietarios, insights competitivos. | Solo el Lab de origen. | Parámetros específicos de una estrategia de scalping rentable. |
| **Lab-Published** | Conocimiento del Lab publicado voluntariamente al ecosistema. Otros Labs pueden leer, no modificar. | Todos los Labs (lectura). | "Evaluación de latencia de 5 exchanges para trading algorítmico" — methodology y resultados generales. |
| **LabOS-Shared** | Conocimiento que LabOS mantiene como infraestructura transversal. | Todos los Labs (lectura). | Principios de investigación, Evidence Framework, convenciones de documentación. |
| **Cross-Lab** | Conocimiento co-creado entre Labs con acuerdo de co-propiedad documentado. | Labs participantes. | Investigación conjunta entre Crypto Scalping Core y Atlas Wealth Labs sobre correlación crypto-commodities. |

---

## Regla por defecto

**Todo conocimiento generado por un Lab es Lab-Private por defecto.** [Decisión]

La publicación es un acto explícito del Lab. Ningún mecanismo automático extrae conocimiento de un Lab sin consentimiento. Esta regla protege:

- Ventaja competitiva del Lab (e.g., estrategias de trading). [Hecho]
- Información sensible no clasificada formalmente aún. [Hecho]
- Autonomía del Lab per Lab_Boundary. [Hecho]

---

## Criterios para publicar conocimiento

Un Lab PUEDE publicar conocimiento al ecosistema cuando cumple TODOS los siguientes criterios: [Decisión]

1. **Aplicabilidad cross-lab:** El conocimiento es útil para ≥1 Lab adicional en el portafolio.
2. **No sensibilidad:** El conocimiento no contiene datos clasificados como Confidencial o Secret (ref: Security_Policy, Package 001A — Requirement 9).
3. **Autoría documentada:** El Lab de origen está identificado como propietario.
4. **Estado mínimo:** El conocimiento tiene estado `validated` o superior en el lifecycle.

---

## Criterios para que conocimiento sea LabOS-Shared

El conocimiento se promueve a LabOS-Shared cuando: [Decisión]

1. **Universalidad:** Aplica a TODOS los Labs del portafolio sin adaptación.
2. **Estabilidad:** Es conocimiento estable que no cambia con frecuencia (<1 cambio/trimestre).
3. **Metodológico o infraestructural:** Describe cómo operar (procesos, métodos, convenciones), no qué se encontró (resultados de dominio).

Ejemplos de LabOS-Shared: methodology de investigación, convenciones de documentación, framework de evidencia. [Hecho]

Ejemplos que NO son LabOS-Shared: resultados de una investigación de mercado, comparativas de herramientas específicas de un dominio. [Hecho]

---

## Flujo de reclasificación

```text
Lab-Private → Lab-Published → LabOS-Shared
     │                              ▲
     │                              │ (solo si cumple criterios
     │                              │  de universalidad)
     └──────────────────────────────┘
              (raro: directo solo si
               es metodológico desde origen)
```

### Proceso de publicación (Lab-Private → Lab-Published)

1. El Lab cambia el campo `visibility` del Knowledge Object a `published`. [Decisión]
2. El Lab agrega un `summary` de ≤300 caracteres. [Decisión]
3. LabOS registra el Knowledge Object en el índice compartido dentro de 7 días. [Decisión]
4. El Lab mantiene la versión canónica. Otros Labs solo referencian.

### Proceso de promoción (Lab-Published → LabOS-Shared)

1. El Fundador identifica que el conocimiento cumple criterios de universalidad. [Decisión]
2. Se crea una versión LabOS-owned del conocimiento (transferencia de propiedad). [Decisión]
3. La versión del Lab original se mantiene como referencia histórica con link al documento LabOS.

---

## Restricciones de boundary

| Restricción | Regla | Referencia |
|-------------|-------|-----------|
| No copiar | Compartir es referenciar, nunca duplicar contenido. | Principio 2, Knowledge_Sharing_Protocol (001A, R6) |
| No forzar formato | Un Lab no necesita reformatear su conocimiento para publicarlo. Solo agregar metadata mínima. | Principio 6, Documentation_Policy (001A, R8) |
| No acceso sin consentimiento | Conocimiento Lab-Private no se accede sin autorización explícita del Lab. | Lab_Boundary (001A, R5) |
| Retractabilidad | Un Lab puede retractar conocimiento publicado en cualquier momento actualizando el índice compartido. | Knowledge_Sharing_Protocol (001A, R6.5) |

---

## Relación con Security_Policy

La clasificación de boundary NO reemplaza la clasificación de seguridad. Son ortogonales: [Decisión]

| Security level | Compatible con boundary |
|---------------|----------------------|
| Public | Lab-Private, Lab-Published, LabOS-Shared, Cross-Lab |
| Internal | Lab-Private, Lab-Published (con restricción), LabOS-Shared |
| Confidential | Lab-Private ÚNICAMENTE |
| Secret | Lab-Private ÚNICAMENTE |

Conocimiento clasificado como Confidential o Secret NUNCA puede ser Lab-Published ni LabOS-Shared. [Decisión]

---

## Cross-references

- [Package 001A — Requirement 5: Lab Boundaries](../../../.kiro/specs/package-001a-first-lab-integration/requirements.md)
- [Package 001A — Requirement 6: Knowledge Sharing](../../../.kiro/specs/package-001a-first-lab-integration/requirements.md)
- [knowledge-sharing.md](./knowledge-sharing.md)
- [knowledge-classification.md](./knowledge-classification.md)
- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 5        | 25%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 15       | 75%        |
| [Visión]      | 0        | 0%         |

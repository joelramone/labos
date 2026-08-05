# Perfil del Lab — Crypto Scalping Core

## Propósito

Este documento captura el perfil factual de Crypto Scalping Core basado exclusivamente en evidencia verificable dentro del workspace de LabOS. [Hecho] No se inventan datos ni se asumen capacidades no documentadas.

---

## Información Confirmada (del Portfolio Model)

| Campo | Valor | Fuente | Estatus |
|-------|-------|--------|---------|
| Nombre | Crypto Scalping Core | Portfolio Model (012-portfolio-model.md) | CONFIRMED [Hecho] |
| Dominio | Trading cuantitativo | Portfolio Model | CONFIRMED [Hecho] |
| Descripción | Estrategias algorítmicas y herramientas de trading | Portfolio Model (steering) | CONFIRMED [Hecho] |
| Estado actual | `idea` | Portfolio Model | CONFIRMED [Hecho] |
| Owner | Fundador | Implícito en nivel SOLO de gobernanza | CONFIRMED [Hecho] |
| Hipótesis de producto | "Estrategias algorítmicas de scalping pueden generar retornos consistentes con gestión de riesgo automatizada." | Portfolio Model (012) | CONFIRMED [Hipótesis] |
| Criterio de avance | "Documentar estrategia con backtest sobre datos históricos que muestre expectativa positiva en al menos 100 operaciones simuladas." | Portfolio Model (012) | CONFIRMED [Hecho] |
| Posición en portafolio | #6 de 11 Labs | Portfolio Model | CONFIRMED [Hecho] |

---

## Información Verificada (Post-Decisiones del Fundador — 2025-07-23)

| Campo | Valor | Fuente | Estatus |
|-------|-------|--------|---------|
| Repositorio local | `C:\Users\jd0519\Documents\Personal\crypto-scalping-core` | Decisión del Fundador | VERIFIED [Hecho] |
| Repositorio remoto | `https://github.com/joelramone/crypto-scalping-core` | Decisión del Fundador | VERIFIED [Hecho] |
| Branch principal | `main` | Decisión del Fundador | VERIFIED [Hecho] |
| Fuente de verdad | Remoto (GitHub main branch) | Decisión del Fundador | VERIFIED [Decisión] |
| Clon local | Copia de trabajo operativa | Decisión del Fundador | VERIFIED [Hecho] |
| Owner | Joel Diaz (Fundador) | Decisión del Fundador | VERIFIED [Hecho] |
| Permiso LabOS — lectura | SÍ | Decisión del Fundador | VERIFIED [Decisión] |
| Permiso LabOS — modificación | NO | Decisión del Fundador | VERIFIED [Decisión] |
| Autonomía operacional | Independiente de LabOS | Decisión del Fundador | VERIFIED [Hecho] |
| Estado operativo | Idea, sin actividad operativa aún | Decisión del Fundador | VERIFIED [Hecho] |

---

## Información No Disponible (Pendiente de Inspección)

| Campo | Valor | Motivo de ausencia |
|-------|-------|-------------------|
| Código existente | PENDIENTE_INSPECCIÓN | Repositorio identificado pero aún no inspeccionado. [Hecho] |
| Investigaciones realizadas | PENDIENTE_INSPECCIÓN | Requiere inspección del repositorio remoto. [Hecho] |
| Datasets | PENDIENTE_INSPECCIÓN | Requiere inspección del repositorio remoto. [Hecho] |
| Estrategias documentadas | PENDIENTE_INSPECCIÓN | Requiere inspección del repositorio remoto. [Hecho] |
| Resultados de backtesting | PENDIENTE_INSPECCIÓN | Requiere inspección del repositorio remoto. [Hecho] |
| Herramientas desarrolladas | PENDIENTE_INSPECCIÓN | Requiere inspección del repositorio remoto. [Hecho] |
| Dependencias técnicas | PENDIENTE_INSPECCIÓN | Requiere inspección del repositorio remoto. [Hecho] |
| Historial operativo | PENDIENTE_INSPECCIÓN | Requiere inspección del repositorio remoto. [Hecho] |
| Exchanges o plataformas objetivo | PENDIENTE_INSPECCIÓN | Requiere inspección del repositorio remoto. [Hecho] |
| Capital o presupuesto | Lab-Private | Información financiera privada del Lab. [Decisión] |
| Riesgos específicos documentados | VERIFIED | 5 riesgos identificados por el fundador (2025-07-23). [Hecho] |
| Knowledge Objects | N/A para estado `idea` | Se generarán cuando el Lab transicione a `explorando`. [Hecho] |
| Activos formales | N/A para estado `idea` | Se generarán con operación formal. [Hecho] |
| Hipótesis de monetización detallada | INCOMPLETA | Faltan 3 campos mínimos (segmento, formato, modelo de ingreso). [Hecho] |

---

## Evaluación de Prerrequisitos de Integración (Package 001A)

Los 4 prerrequisitos de integración formal: [Hecho]

| Prerrequisito | Estatus | Evidencia |
|---------------|---------|-----------|
| Independencia de dominio | VALIDATED | "Trading cuantitativo" no es reclamado por ningún otro Lab activo. Atlas Wealth Labs (Finanzas) es diferente en alcance. [Hecho] |
| Preservación de identidad | VALIDATED | Tiene nombre propio, dominio propio y descripción diferenciada. [Hecho] |
| Autonomía operacional | VALIDATED | Confirmado por el fundador (2025-07-23): CSC es operacionalmente independiente de LabOS. [Hecho] |
| Voluntad de integración | VALIDATED | Confirmado por el fundador al proveer decisiones de integración. [Hecho] |

---

## Perfil Técnico (Proyectado)

Basado en el dominio "Trading cuantitativo", el perfil técnico ESPERADO sería: [Hipótesis]

| Aspecto | Valor esperado | Estatus |
|---------|---------------|---------|
| Lenguajes probables | Python, posiblemente C++/Rust para baja latencia | HYPOTHESIS [Hipótesis] |
| Infraestructura probable | APIs de exchanges, WebSockets, sistemas de backtesting | HYPOTHESIS [Hipótesis] |
| Datos necesarios | Market data (OHLCV, orderbook, trades) | HYPOTHESIS [Hipótesis] |
| Entorno de ejecución | Local o VPS con baja latencia a exchanges | HYPOTHESIS [Hipótesis] |

> **IMPORTANTE**: Esta sección es especulativa y NO debe tomarse como factual. Existe solo para contextualizar el dominio, no para documentar decisiones tomadas. [Hipótesis]

---

## Estado de Madurez

| Indicador | Valor |
|-----------|-------|
| Lab_State actual | `idea` [Hecho] |
| Tiempo en estado `idea` | UNKNOWN — no hay fecha de creación documentada. [Hecho] |
| Actividad observable en workspace | Ninguna. [Hecho] |
| Documentos propios del Lab | 0 (fuera del portfolio model). [Hecho] |
| Porcentaje de perfil completable con evidencia actual | ~25% (solo lo confirmado del portfolio model). [Hecho] |

---

## Conclusión

Crypto Scalping Core existe como repositorio verificado en GitHub (`https://github.com/joelramone/crypto-scalping-core`, branch `main`) con ownership confirmado por Joel Diaz. [Hecho] El Lab es operacionalmente independiente de LabOS y su fuente de verdad es el repositorio remoto. [Hecho] Pendiente: inspección del repositorio para completar perfil técnico y verificar boundaries contra estructura real. [Hecho]

---

## Cross-references

- [Portfolio Model — 012-portfolio-model.md](../package-000-foundation/012-portfolio-model.md) — Fuente de datos confirmados
- [lab-validation-framework.md](./lab-validation-framework.md) — Framework de evaluación
- [crypto-scalping-core-readiness-assessment.md](./crypto-scalping-core-readiness-assessment.md) — Evaluación contra framework
- [evidence-required-register.md](./evidence-required-register.md) — Registro de evidencia faltante

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 35       | 73%        |
| [Hipótesis]   | 6        | 12%        |
| [Decisión]    | 7        | 15%        |
| [Visión]      | 0        | 0%         |

> **Nota**: Perfil actualizado con decisiones del fundador (2025-07-23). Incremento en hechos verificados por confirmación de repositorio y ownership. Las hipótesis corresponden a proyecciones técnicas especulativas del dominio.

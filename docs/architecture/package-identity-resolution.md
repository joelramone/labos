# Resolución de Identidad de Packages

## Propósito

Este documento resuelve cualquier ambigüedad de identidad entre packages aprobados en el roadmap y su existencia en el repositorio. [Hecho]

---

## Packages Existentes y Paths

| Package Name | Repositorio Path (docs) | Repositorio Path (spec) | Estado |
|---|---|---|---|
| Package 000 — Foundation | `docs/packages/package-000-foundation/` | `.kiro/specs/package-000-foundation/` | Completo |
| Package 001 — Research Methodology | `docs/packages/package-001-research-methodology/` | `.kiro/specs/package-001-research-methodology/` | Completo |
| Package 001A — First Lab Integration | (sin carpeta en docs/) | `.kiro/specs/package-001a-first-lab-integration/` | Requirements definidos |
| Package 002 — Knowledge Architecture | `docs/packages/package-002-knowledge-architecture/` | (sin spec) | Solo README placeholder |
| Package 002A — Architecture Review | `docs/packages/package-002a-architecture-review/` | `.kiro/specs/package-002a-architecture-review/` | Completo (consolidación) |
| Package 003-009 | `docs/packages/package-003-asset-system/` ... `package-009-scaling/` | (sin specs) | Dormidos |

---

## Nombres Aprobados según Roadmap

| # | Nombre Canónico | Path de Ejecución | Tipo |
|---|---|---|---|
| 001A | First Lab Integration | `docs/packages/package-001a-first-lab-integration/` | Fundacional |
| 002 | Knowledge Architecture | `docs/packages/package-002-knowledge-architecture/` | Fundacional |

---

## Colisiones Detectadas

**No se detectan colisiones de numeración.** [Hecho]

- "Package 002" se refiere únicamente a Knowledge Architecture en todo el repositorio.
- "Package 001A" se refiere únicamente a First Lab Integration.
- No existe ambigüedad entre conceptos ni paths.

---

## Convención de Naming No-Destructiva

Para esta ejecución: [Decisión]

1. **Track A** (Lab Integration) produce documentos en: `docs/packages/package-001a-first-lab-integration/`
2. **Track B** (Knowledge Architecture) produce documentos en: `docs/packages/package-002-knowledge-architecture/`
3. Los specs existentes en `.kiro/specs/package-001a-first-lab-integration/` se PRESERVAN como referencia. Los documentos finales se producen en docs/.
4. Ningún path existente se renombra ni se destruye.

---

## Separación Corporativa/Personal

**Invariante de separación:** [Decisión]

- SentinelOps es un proyecto corporativo/laboral. NO se utiliza como caso de estudio operativo.
- SentinelOps permanece como referencia histórica en documentos ya versionados pero NO se usa en trabajo nuevo.
- El primer Lab operativo para validar la integración es: **Crypto Scalping Core** (proyecto personal).
- No se inspecciona, importa, copia ni infiere de: repositorios corporativos, documentos de employer, información de BYMA o NRTC.

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---|---|---|
| [Hecho] | 5 | 42% |
| [Decisión] | 7 | 58% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 0 | 0% |

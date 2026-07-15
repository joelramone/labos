# Project Structure — LabOS

## Organización por packages

El proyecto se organiza en packages numerados secuencialmente. Cada package representa una unidad de trabajo con entregables concretos.

```
packages/
  000-foundation/
  001-<nombre>/
  ...
```

## Ubicaciones clave

| Propósito | Ruta |
|-----------|------|
| Documentación general | `docs/` |
| Decisiones arquitectónicas | `docs/decisions/` |
| Investigación y evidencia | `research/` |
| Activos reutilizables | `assets/` |
| Productos (blueprints) | `products/` |
| Automatizaciones y agentes | `agents/` |
| Tests y validaciones | `tests/` |
| Packages de trabajo | `packages/` |
| Steering de Kiro | `.kiro/steering/` |
| Specs de Kiro | `.kiro/specs/` |

## Convenciones de nombres

- Carpetas y archivos: `kebab-case` en inglés.
- Documentos internos en español; títulos y nombres técnicos en inglés cuando corresponda.
- Packages: `NNN-nombre-descriptivo/` (e.g., `000-foundation`).
- Decisiones: `docs/decisions/NNNN-titulo.md` (e.g., `0001-stack-selection.md`).
- Specs: `.kiro/specs/<feature-name>/` con `requirements.md`, `design.md`, `tasks.md`.

## Regla general

No crear carpetas vacías. Cada directorio debe contener al menos un archivo con propósito claro (puede ser un `README.md` explicativo).

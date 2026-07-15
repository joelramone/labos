# Contribución a LabOS

## Principios

1. **Documentar antes de construir.** Todo cambio debe tener contexto documentado.
2. **Cambios pequeños y revisables.** Cada PR debe ser revisable en menos de 15 minutos.
3. **Preservar decisiones existentes.** No reescribir sin documentar el motivo.
4. **Revisión humana obligatoria** para decisiones que afecten múltiples packages.

## Proceso

1. Crear un branch descriptivo: `feature/NNN-nombre` o `docs/NNN-nombre`.
2. Seguir las convenciones de nombres definidas en `.kiro/steering/project-structure.md`.
3. Incluir documentación actualizada con cada cambio.
4. Clasificar contenido como: Hecho, Hipótesis, Visión o Decisión.

## Idioma

- Documentación: español.
- Nombres de archivos, carpetas y código: inglés.
- Términos técnicos sin traducción forzada.

## Prohibiciones

- No inventar clientes, ingresos o validación.
- No presentar hipótesis como hechos.
- No agregar dependencias sin justificación.
- No hacer commits masivos con múltiples cambios no relacionados.

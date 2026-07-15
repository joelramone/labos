# Engineering Principles — LabOS

## Principios fundamentales

1. **No empezar por código.** Antes de implementar, debe existir un blueprint, spec o decisión documentada que justifique el trabajo.

2. **Preservar decisiones existentes.** No reescribir ni descartar decisiones previas sin documentar el motivo del cambio y obtener revisión humana.

3. **Cambios pequeños y revisables.** Cada commit, PR o entregable debe ser lo suficientemente pequeño para que un humano pueda revisarlo en menos de 15 minutos.

4. **Documentación como parte del producto.** Código sin documentación actualizada no se considera terminado.

5. **Seguridad y privacidad desde el diseño.** No almacenar secretos en repositorios. No exponer datos sensibles. Considerar implicaciones de privacidad antes de implementar.

6. **Revisión humana para decisiones relevantes.** Decisiones arquitectónicas, de negocio o que afecten múltiples packages requieren aprobación explícita del owner.

7. **Evidence-driven.** Las decisiones técnicas deben respaldarse con datos, benchmarks, pruebas de concepto o referencias, no con opiniones.

## Enfoque del proyecto

- **Documentation-first**: documentar antes de construir.
- **Blueprint-first**: diseñar antes de implementar.
- **Package-driven**: organizar trabajo en unidades discretas con entregables claros.
- **AI-native**: diseñar pensando en que agentes de IA operarán y extenderán el sistema.
- **Spec-driven**: usar specs formales (Kiro) para features y bugfixes.

## Anti-patterns a evitar

- Construir features completas sin spec ni blueprint.
- Commits masivos con múltiples cambios no relacionados.
- Código "por si acaso" sin hipótesis de uso.
- Dependencias innecesarias o no auditadas.
- Automatización prematura sin proceso manual validado.

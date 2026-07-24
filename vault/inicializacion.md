---
fecha: 2026-07-24
tags: [inicializacion, protocolo, memoria]
---

# Inicialización de sesión — HVAC Laboratorio Brinsa (P2437)

## Propósito

Este vault de Obsidian (`vault/`) es la **memoria permanente** del proyecto. Su
objetivo es que cualquier sesión posterior pueda recuperar el contexto técnico,
las decisiones de diseño, los bloqueos y los workflows sin necesidad de releer
todo el repositorio ni de reconstruir la historia desde cero.

`contexto.md` (en la raíz) es el **resumen rápido** de la última sesión.  
`vault/inicializacion.md` (esta nota) es el **protocolo de arranque**.

## Protocolo de lectura al iniciar sesión

Seguir este orden. No leer notas que no sean relevantes para la tarea actual.

1. **[[../contexto]]** — resumen rápido de la última sesión y próximas tareas.
2. **[[00_Inicio]]** — índice del vault y mapa de notas.
3. **[[01_Estado actual]]** — dónde está el proyecto hoy.
4. **[[02_Bases de diseño congeladas]]** — supuestos que no se revisan sin aprobación.
5. **[[05_Preguntas abiertas]]** — bloqueos y datos pendientes del cliente.
6. Según la tarea solicitada, leer solo las notas enlazadas relevantes:
   - Decisiones de diseño en `vault/03_Decisiones/`.
   - Bitácora de sesiones recientes en `vault/04_Bitácora/`.
   - Archivos clave y workflows en [[06_Archivos clave]] y [[07_Workflows]].
   - Estructura del proyecto en [[estructuraproyecto]].

## Reglas de economía de tokens

- **No leer el vault completo.** Leer únicamente las notas directamente
  relacionadas con la tarea en curso.
- **No transcribir contenido largo.** Referenciar archivos (`Latex/...`,
  `Investigacion/...`, `memoriadecalculo.xlsx`) en lugar de copiar tablas o
  párrafos extensos.
- **Priorizar fuentes canónicas:**
  - Datos numéricos → `Latex/00_bases_diseno/bases_diseno.yaml`.
  - Entregables emitidos → `Emisiones/` (regenerados por `scripts/emitir.py`).
  - Código fuente → leer solo los archivos que la tarea implique modificar.

## Al cerrar sesión

Antes de terminar, actualizar la memoria del proyecto:

1. Actualizar `../contexto.md` (estado, próxima tarea, fecha).
2. Actualizar [[01_Estado actual]].
3. Crear o actualizar la bitácora del día en `vault/04_Bitácora/YYYY-MM-DD.md`.
4. Actualizar [[05_Preguntas abiertas]] con nuevos bloqueos o resueltos.
5. Si hubo decisiones de diseño, crear nota en `vault/03_Decisiones/` y enlazarla
   desde [[00_Inicio]].
6. Si cambiaron archivos clave o workflows, actualizar [[06_Archivos clave]] y
   [[07_Workflows]].
7. Si cambió la estructura de carpetas, actualizar [[estructuraproyecto]].
8. Si se modificaron fuentes de entregables (`Latex/02_informe_tex/`,
   `generar_excel.py`, `Investigacion/Sistemas/`, `scripts/generar_*.py`),
   ejecutar `python scripts/emitir.py` para regenerar `Emisiones/`.
9. Hacer commit y push a GitHub.

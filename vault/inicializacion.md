---
fecha: 2026-07-24
tags: [inicializacion, protocolo, memoria, runbook]
---

# Inicialización de sesión — HVAC Laboratorio Brinsa (P2437)

## Comando de activación

Cuando el usuario diga **"ejecuta inicializacion.md"** (o inicie una nueva sesión
en este proyecto), el agente debe ejecutar el protocolo de recuperación de
contexto descrito a continuación. No iniciar trabajo técnico hasta completar
este protocolo.

## Objetivo

Este vault de Obsidian (`vault/`) es la **memoria permanente** del proyecto. El
protocolo permite recuperar el contexto técnico, las decisiones de diseño, los
bloqueos y los workflows sin releer todo el repositorio.

`contexto.md` (raíz) es el **resumen rápido**.  
`vault/inicializacion.md` (esta nota) es el **runbook de arranque**.

## Protocolo de recuperación de contexto

### Paso 1 — Resumen rápido

Leer el archivo `contexto.md` en la raíz del proyecto.

- Extraer: última tarea completada, próximas tareas pendientes, fecha de última
  actualización.
- No transcribir el archivo completo; identificar el estado general y la tarea
  lógica a retomar.

### Paso 2 — Índice del vault

Leer `vault/00_Inicio.md`.

- Confirmar las secciones del vault y los wikilinks disponibles.
- No leer notas enlazadas todavía; solo identificar cuáles son relevantes para
  la tarea actual.

### Paso 3 — Estado actual detallado

Leer `vault/01_Estado actual.md`.

- Extraer: última tarea completada, tareas previas, próxima tarea pendiente,
  fecha de actualización.
- Comparar con `contexto.md` y resolver cualquier inconsistencia antes de
  continuar.

### Paso 4 — Bases de diseño congeladas

Leer `vault/02_Bases de diseño congeladas.md`.

- Extraer los valores clave: sitio, altitud, presión atmosférica, densidad del
  aire, caudal, presión del ventilador, potencia/motor, velocidades, filtración,
  ambiente corrosivo.
- Recordar: estos valores **no se revisan sin aprobación explícita**.

### Paso 5 — Preguntas abiertas y bloqueos

Leer `vault/05_Preguntas abiertas.md`.

- Extraer: bloqueos activos y resueltos recientemente.
- Identificar si alguno de los bloqueos afecta la tarea que el usuario va a
  solicitar.

### Paso 6 — Notas específicas según la tarea

Según la tarea que el usuario indique (o según las próximas tareas pendientes),
leer **solo** las notas directamente relacionadas:

| Tema posible | Notas a leer |
|---|---|
| CFD / pressure outlet | `vault/03_Decisiones/2026-07-22_cfd-pressure-outlet.md` |
| Presurización / damper de alivio | `vault/03_Decisiones/2026-07-22_presurizacion-damper-alivio.md` |
| Recálculo sitio Cajicá / densidad | `vault/03_Decisiones/2026-07-23_recalculo-sitio-cajica.md` |
| Filtración MERV / sin HEPA | `vault/03_Decisiones/2026-07-23_sin-hepa-laboratorio-industrial.md` |
| Disponibilidad comercial de equipos | `Investigacion/Sistemas/listado_equipos.md`, `Investigacion/Sistemas/informe_investigacion.md` |
| Documentación / entregables / workflows | `vault/06_Archivos clave.md`, `vault/07_Workflows.md`, `vault/estructuraproyecto.md` |
| Bitácora de sesiones recientes | `vault/04_Bitácora/2026-07-24.md` (y anteriores si es necesario) |

**Regla:** si el usuario no ha dicho todavía qué tarea quiere, leer solo las
notas de las próximas tareas pendientes en `vault/05_Preguntas abiertas.md`.

## Entrega al usuario

Al completar el protocolo, presentar un resumen estructurado (sin transcribir
tablas extensas):

1. **Estado actual:** última tarea completada y contexto inmediato.
2. **Bases de diseño congeladas relevantes:** 3-5 valores clave.
3. **Preguntas abiertas / bloqueos:** activos y resueltos recientes.
4. **Próxima tarea lógica:** la pendiente de mayor prioridad según el vault.
5. **Pregunta:** "¿Qué tarea quieres retomar?"

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

1. Actualizar `contexto.md` (estado, próxima tarea, fecha).
2. Actualizar `vault/01_Estado actual.md`.
3. Crear o actualizar la bitácora del día en `vault/04_Bitácora/YYYY-MM-DD.md`.
4. Actualizar `vault/05_Preguntas abiertas.md` con nuevos bloqueos o resueltos.
5. Si hubo decisiones de diseño, crear nota en `vault/03_Decisiones/` y enlazarla
   desde `vault/00_Inicio.md`.
6. Si cambiaron archivos clave o workflows, actualizar `vault/06_Archivos clave.md`
   y `vault/07_Workflows.md`.
7. Si cambió la estructura de carpetas, actualizar `vault/estructuraproyecto.md`.
8. Si se modificaron fuentes de entregables (`Latex/02_informe_tex/`,
   `generar_excel.py`, `Investigacion/Sistemas/`, `scripts/generar_*.py`),
   ejecutar `python scripts/emitir.py` para regenerar `Emisiones/`.
9. Hacer commit y push a GitHub.

---
name: obsidian-vault
description: Mantiene el vault de Obsidian del proyecto (vault/) como memoria a largo plazo — contexto, decisiones de diseño, bitácora de sesiones y preguntas abiertas
type: prompt
whenToUse: Al iniciar una sesión de trabajo en este proyecto, al tomar una decisión de diseño, y al cerrar la sesión para dejar memoria persistente
---

# Skill: Vault de Obsidian — memoria persistente del proyecto

El vault de Obsidian es **la raíz del proyecto** (`Calculos/`): Obsidian indexa todo
el repo. La carpeta `vault/` es el subsistema de memoria a largo plazo que esta skill
mantiene; `contexto.md` sigue siendo el resumen rápido de la sesión.
Ambos deben quedar coherentes al cerrar la sesión.

## Al inicio de sesión

1. Lee `contexto.md` (resumen rápido) y `vault/00_Inicio.md` (índice del vault).
2. Según la tarea pedida, lee solo las notas enlazadas relevantes (decisiones del tema,
   bases de diseño, preguntas abiertas). No leas el vault completo.

## Durante la sesión

- Al tomar una decisión de diseño (elección de correlación, material, configuración,
  escenario de cálculo), crea o actualiza una nota en `vault/03_Decisiones/` usando
  `vault/99_Plantillas/plantilla_decision.md`: motivo, alternativas descartadas y
  referencia a norma/correlación.
- Nombra las notas de decisión como `YYYY-MM-DD_tema-corto.md`.

## Al cierre de sesión

Ejecuta estos pasos junto con la actualización de `contexto.md` (exigida por `AGENTS.md`):

1. Actualiza `vault/01_Estado actual.md` (última tarea, próxima tarea, fecha).
2. Crea o actualiza la nota del día `vault/04_Bitácora/YYYY-MM-DD.md` con
   `vault/99_Plantillas/plantilla_bitacora.md`: qué se hizo, cómo se verificó, pendientes.
3. En `vault/05_Preguntas abiertas.md`: marca resueltas y agrega las nuevas.
4. Registra las decisiones nuevas en `vault/03_Decisiones/` y enlázalas desde
   `vault/00_Inicio.md`.
5. Si cambiaron archivos clave o workflows, actualiza `vault/06_Archivos clave.md` y
   `vault/07_Workflows.md`.
6. Si cambió la estructura de carpetas o se crearon/eliminaron archivos relevantes,
   actualiza el árbol en `vault/estructuraproyecto.md`.
7. Si la sesión modificó fuentes de entregables (`Latex/02_informe_tex/`,
   `generar_excel.py`, `Investigacion/Sistemas/`), ejecuta
   `python scripts/emitir.py` para regenerar `Emisiones/` (Excel + informes PDF +
   copias codificadas + manifiesto). Las fuentes se editan; las emisiones se
   regeneran, nunca se editan a mano.

## Reglas del vault

- Español técnico, wikilinks `[[...]]` entre notas, una idea por nota.
- Frontmatter YAML mínimo: `fecha` y `tags` (la plantilla de decisión añade `estado`).
- No dupliques tablas de datos grandes: referencia el archivo fuente
  (p. ej. `Latex/00_bases_diseno/bases_diseno.yaml`, `memoriadecalculo.xlsx`).
- Las notas `.md` se versionan en git; `/.obsidian/` y `vault/.obsidian/` están
  ignorados (config local de Obsidian).

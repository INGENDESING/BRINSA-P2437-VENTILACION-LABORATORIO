---
fecha: 2026-07-23
tags: [archivos]
---

# Archivos clave y su propósito

- `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex` / `.pdf` — informe técnico DML
  (documento canónico; incluye la memoria descriptiva). El antiguo
  `memoriadescriptiva.*` se eliminó el 2026-07-23 por redundancia.
- `generar_excel.py` — generador openpyxl de la memoria (7 hojas, fórmulas vivas,
  incluye "Escenarios Filtración").
- `memoriadecalculo.xlsx` — memoria de cálculo técnica con fórmulas vivas.
- `Latex/00_bases_diseno/bases_diseno.yaml` — fuente única de verdad
  (datos + escenarios + normas).
- `docs/index.html` — dashboard web interactivo (GitHub Pages).
- `HojasDatos/P2437-PR-DT-001.xlsx` — hoja de datos del equipo.
- `resultado simulaciones/` — capturas de resultados CFD (Case 1, Case 2).
- `Investigacion/Sistemas/` — informe de investigación del sistema, listado de
  equipos y hojas de datos (HD-VENT-001, HD-FILT-001, HD-REJ-001, HD-INST-001).
- `Codificacion/codificacion.md` — codificación GP-N-09 de los documentos del
  proyecto (listado de códigos, desviaciones y códigos reservados).
- `Latex/02_informe_tex/P2437-HV-INF-002 REV0.tex` — informe de investigación del
  sistema (formato DML; secciones en `sections_inf002/`).
- `Emisiones/` — entregables codificados (copias generadas; no editar a mano).
- `scripts/emitir.py` — regenera Excel, compila INF-001/002 y copia a `Emisiones/`.
- `task/todo.md` — plan de tareas de la sesión (fase 1 de `AGENTS.md`).
- `contexto.md` — resumen rápido de sesión; el detalle vive en este vault.
- `.agents/skills/obsidian-vault/SKILL.md` — skill que mantiene este vault.

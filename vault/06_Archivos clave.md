---
fecha: 2026-07-27
tags: [archivos]
---

# Archivos clave y su propósito

- `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex` / `.pdf` — informe técnico DML
  (documento canónico; incluye la memoria descriptiva). Se emite como REV1 por
  cambio de alcance el 2026-07-27.
- `Latex/02_informe_tex/P2437-HV-INF-002 REV0.tex` / `.pdf` — informe de investigación del
  sistema (formato DML; secciones en `sections_inf002/`). Se emite como REV1 el
  2026-07-27.
- `generar_excel.py` — generador openpyxl de la memoria (fórmulas vivas, sin
  presurización a partir de REV1).
- `memoriadecalculo.xlsx` — memoria de cálculo técnica con fórmulas vivas.
- `Latex/00_bases_diseno/bases_diseno.yaml` — fuente única de verdad
  (datos + escenarios + normas). Actualizado a REV1 (sin presurización, axial).
- `docs/index.html` — dashboard web interactivo (GitHub Pages). Actualizado a REV1.
- `resultado simulaciones/` — capturas de resultados CFD (Case 1 … Case 4); fuente de las figuras del informe INF-001.
- `Latex/02_informe_tex/figures/` — figuras del informe técnico, incluidas las 4 vistas CFD (`cfd_streamlines_3d.png`, `cfd_vectores_3d.png`, `cfd_planta_horizontal.png`, `cfd_vectores_corte.png`).
- `Investigacion/Sistemas/` — informe de investigación del sistema, listado de
  equipos y hojas de datos (HD-VENT-001, HD-FILT-001, HD-REJ-001). La hoja de
  datos HD-INST-001 quedó eliminada en REV1 por desaparición de la instrumentación
  de presión diferencial.
- `Codificacion/codificacion.md` — codificación GP-N-09 de los documentos del
  proyecto (listado de códigos, desviaciones y códigos reservados).
- `Emisiones/` — entregables codificados REV1 (copias generadas por
  `scripts/emitir.py`; no editar a mano).
- `scripts/generar_dts.py` — genera las hojas de datos DTS-001/002/003 en Excel
  corporativo (sin IC-DTS a partir de REV1).
- `scripts/generar_img_dts001.py` — genera la curva ilustrativa y el placeholder
  de la hoja DTS-001 (axial a partir de REV1).
- `scripts/pdf_dts001.py` — genera el PDF alternativo de `P2437-HV-DTS-001 REV1`
  desde el markdown fuente usando reportlab (REV1).
- `scripts/generar_lis.py` — genera el listado de equipos BOQ en Excel corporativo.
- `scripts/emitir.py` — regenera Excel, DTS, LIS, compila INF-001/002 y copia a
  `Emisiones/` con nombres REV1.
- `task/todo.md` — plan de tareas de la sesión (fase 1 de `AGENTS.md`).
- `contexto.md` — resumen rápido de sesión; el detalle vive en este vault.
- `.agents/skills/obsidian-vault/SKILL.md` — skill que mantiene este vault.

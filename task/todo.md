# Plan: Auditoría y corrección de referencias y Apéndice D en INF-001

## Contexto
- **Objetivo:** Corregir los nombres de archivo, códigos de documento y rutas citadas en la bibliografía y el Apéndice D de `P2437-HV-INF-001 REV0` para que cumplan la codificación GP-N-09 y coincidan con los entregables emitidos en `Emisiones/`.
- **Cliente / Proyecto:** P2437 — HVAC Laboratorio BRINSA, Cajicá.
- **Normas aplicables:** GP-N-09 (codificación DML), ASHRAE 170, RETIE / NTC 2050.

## Auditoría detectada

1. **Bibliografía (`references/bibliografia.bib`)**
   - Las entradas `dml_informe_investigacion_2026`, `dml_listado_equipos_2026`, `dml_hd_vent_001`, `dml_hd_filt_001`, `dml_hd_rej_001` y `dml_hd_inst_001` citaban rutas de fuentes de trabajo (`Investigacion/Sistemas/*.md`) y códigos internos (`HD-VENT-001`, etc.).
   - Los documentos oficiales ya están codificados GP-N-09 y emitidos en `Emisiones/` como `.pdf` (INF) o `.xlsx` (DTS, LIS, CAL).
   - Faltaba una entrada para la memoria de cálculo `P2437-HV-CAL-001`.

2. **Apéndice D (`sections/13_anexos.tex`)**
   - El texto introductorio indicaba que los documentos se conservan en `Investigacion/Sistemas/`.
   - La tabla `tab:project_docs` usaba códigos internos (`--`, `HD-VENT-001`, …) en lugar de códigos GP-N-09.
   - No incluía la memoria de cálculo `P2437-HV-CAL-001`.

3. **Referencias en el cuerpo del informe**
   - Las claves de cita (`dml_hd_vent_001`, etc.) se mantuvieron para minimizar cambios; el contenido bibliográfico fue el corregido.

## Supuestos clave
- [x] El código oficial para gestión y entrega es GP-N-09 (`P2437-<ESP>-<TIPO>-<consecutivo>`), según `Codificacion/codificacion.md`.
- [x] La ubicación canónica de los entregables es `Emisiones/`, regenerada por `scripts/emitir.py`.
- [x] Las fuentes de trabajo (`Investigacion/Sistemas/*.md`) permanecen como soporte interno, pero no son el documento de entrega.
- [x] No se renombraron archivos físicos; solo se corrigieron las citas textuales.

## Tareas
- [x] **T1. Actualizar bibliografía.** En `Latex/02_informe_tex/references/bibliografia.bib`:
  - Renombrar títulos a códigos GP-N-09.
  - Actualizar `note` con la ruta de emisión.
  - Añadir entrada `@misc{dml_cal_001, ...}` para `P2437-HV-CAL-001`.
- [x] **T2. Actualizar Apéndice D.** En `Latex/02_informe_tex/sections/13_anexos.tex`:
  - Cambiar el texto introductorio para indicar `Emisiones/`.
  - Actualizar la tabla `tab:project_docs` con códigos GP-N-09.
  - Añadir fila para `P2437-HV-CAL-001`.
- [x] **T3. Verificar coherencia de citas.** Revisar que todas las `\cite{...}` del informe sigan resolviéndose correctamente.
- [x] **T4. Recompilar y emitir.** Ejecutar pdflatex + bibtex + pdflatex ×2 y `python scripts/emitir.py`.
- [x] **T5. Actualizar memoria del proyecto.** Actualizar `contexto.md`, `vault/01_Estado actual.md`, `vault/04_Bitácora/2026-07-24.md` y `task/todo.md`.

## Riesgos / Puntos de verificación
- [x] **Referencias cruzadas:** BibTeX resolvió los nuevos `note` sin errores.
- [x] **Consistencia con INF-002:** INF-002 no cita documentos de INF-001 con rutas obsoletas.
- [x] **Cumplimiento GP-N-09:** los códigos mostrados en el Apéndice D coinciden con los nombres de archivo en `Emisiones/`.
- [x] **No editar manualmente Emisiones/:** los cambios se hicieron en fuentes y se regeneraron con `emitir.py`.

## Revisión

- **Resumen:** se corrigió la bibliografía y el Apéndice D de `P2437-HV-INF-001 REV0` para que citen códigos GP-N-09 y rutas de `Emisiones/`. Se añadió la memoria de cálculo `P2437-HV-CAL-001` a ambos lugares. La recompilación fue exitosa (0 errores, 0 citas sin resolver) y la emisión generó 8 entregables.
- **Desviaciones respecto al plan:** ninguna.
- **Limitaciones conocidas:** las claves BibTeX (`dml_*`) se mantuvieron para minimizar cambios; los nombres visibles al lector son los códigos GP-N-09.
- **Trabajo futuro recomendado:** generar manualmente el PDF de `P2437-HV-DTS-001 REV0.xlsx`; confirmar disponibilidad comercial de equipos; validar presión diferencial en campo.
- **Archivos entregables y rutas:**
  - `Latex/02_informe_tex/references/bibliografia.bib`
  - `Latex/02_informe_tex/sections/13_anexos.tex`
  - `Latex/02_informe_tex/P2437-HV-INF-001 REV0.pdf`
  - `Emisiones/1.0 HV-INFORMES/P2437-HV-INF-001 REV0.pdf`
  - `Emisiones/MANIFIESTO_EMISION.md`
  - `contexto.md`, `vault/01_Estado actual.md`, `vault/04_Bitácora/2026-07-24.md`, `task/todo.md`.

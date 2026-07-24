# Plan: Mejora estética y de layout en DTS-002, DTS-003 e IC-DTS-001

## Contexto
- **Objetivo:** Corregir el desfase entre las tablas Markdown y el encabezado corporativo, separar las notas numeradas juntas (ej. 6.1, 6.2, 6.3) en párrafos individuales y mejorar la estética general de las hojas de datos DTS-002, DTS-003 e IC-DTS-001.
- **Cliente / Proyecto:** P2437 — HVAC Laboratorio BRINSA, Cajicá.
- **Normas aplicables:** GP-N-09, ASHRAE 52.2, ASHRAE 70, AMCA 500-D, RETIE / NTC 2050.

## Diagnóstico

1. **Ancho de tablas:** la plantilla `DTS.xlsx` usa 15 columnas (A:O) en el encabezado corporativo, pero `generar_dts.py` generaba las tablas en A:F (`N_COLS = 6`). Esto dejaba un hueco a la derecha y desalineaba el contenido.
2. **Notas numeradas juntas:** en varios `.md` hay secuencias como `6.1. ... 6.2. ... 6.3. ...` en la misma línea; el parser las trataba como un solo párrafo y quedaban visualmente confusas.
3. **Estética:** los párrafos de notas no se diferenciaban del texto principal; no había separación visual entre subpuntos de una sección.

## Supuestos clave
- [x] Todas las tablas Markdown tienen ≤ 6 columnas, por lo que caben en el nuevo layout A:O (15 columnas) con distribución automática.
- [x] Las notas numeradas que deben separarse siguen el patrón `N.N. ` (ej. `6.1. `, `5.2. `) dentro de la misma línea de texto.
- [x] No se modificaron los archivos `.md` fuente; las mejoras se hicieron en el generador.

## Tareas
- [x] **T1. Ampliar layout de tablas a A:O.** `N_COLS` cambiado de 6 a 15; `spans_tabla()` actualizada para distribución automática (base + residuo).
- [x] **T2. Separar notas numeradas.** Añadida función `dividir_notas_numeradas()` y lógica en `parrafo()` para escribir cada nota como párrafo independiente.
- [x] **T3. Mejorar estética de notas.** Añadido estilo `nota_font` (cursiva, gris oscuro `#404040`) para párrafos que empiecen con `\d+\.\d+\.`.
- [x] **T4. Ajustar imágenes DTS-001.** Verificado que `insertar_graficos_dts001` sigue funcionando (las imágenes se insertan en columna A, sin depender de `N_COLS`).
- [x] **T5. Recompilar y emitir.** `python scripts/generar_dts.py` OK; `python scripts/emitir.py` OK, 8 entregables actualizados.
- [x] **T6. Verificación visual.** Confirmado con openpyxl que las tablas ocupan A:O y que las notas están separadas (7/7/9 notas numeradas en DTS-002/003/IC).
- [x] **T7. Actualizar memoria.** `contexto.md`, `vault/01_Estado actual.md`, `vault/04_Bitácora/2026-07-24.md` y `task/todo.md` actualizados.

## Riesgos / Puntos de verificación
- [x] **Tablas de 2 columnas:** la distribución automática en 15 columnas funciona; el texto con `wrap_text` se ve correcto.
- [x] **Regresión en DTS-001:** DTS-001 se regeneró correctamente con sus imágenes de referencia gráfica intactas.
- [x] **No editar manualmente Emisiones/:** los cambios se hicieron en el generador y se regeneraron con `emitir.py`.

## Revisión

- **Resumen:** se mejoró el generador `scripts/generar_dts.py` para que las tablas Markdown ocupen el ancho completo A:O (coincidente con el encabezado corporativo), separar las notas numeradas en párrafos individuales y aplicar estilo cursivo/gris a las notas. Las 4 hojas de datos (DTS-001…003 e IC-DTS-001) se regeneraron y emitieron correctamente.
- **Desviaciones respecto al plan:** ninguna.
- **Limitaciones conocidas:** la estimación de filas para párrafos es aproximada; algunos párrafos muy largos podrían requerir ajuste fino de altura en una revisión posterior.
- **Trabajo futuro recomendado:** revisar visualmente los Excel generados para ajustar alturas de fila si es necesario; completar el PDF manual de DTS-001.
- **Archivos entregables y rutas:**
  - `scripts/generar_dts.py` (actualizado)
  - `build/dts/P2437-HV-DTS-001 REV0.xlsx`
  - `build/dts/P2437-HV-DTS-002 REV0.xlsx`
  - `build/dts/P2437-HV-DTS-003 REV0.xlsx`
  - `build/dts/P2437-IC-DTS-001 REV0.xlsx`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/` (4 archivos actualizados)
  - `contexto.md`, `vault/01_Estado actual.md`, `vault/04_Bitácora/2026-07-24.md`, `task/todo.md`.

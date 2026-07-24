# Plan: Actualización del informe INF-001 con resultados CFD (pressure outlet)

## Contexto
- **Objetivo:** Integrar las 4 gráficas nuevas de Autodesk CFD (`resultado simulaciones/Case {1..4}.png`) en el informe LaTeX `P2437-HV-INF-001 REV0.tex`, actualizando condiciones de contorno a `pressure outlet` 0 Pa gauge, metodología, resultados, análisis, conclusiones, recomendaciones, alcance y resumen.
- **Cliente / Proyecto:** P2437 — HVAC Laboratorio BRINSA, Cajicá (Cundinamarca).
- **Normas aplicables:** ASHRAE 170, ASHRAE 52.2, ASHRAE Handbook Fundamentals (`C_d`), ISO 16890, RETIE / NTC 2050.

## Supuestos clave
- [x] Las 4 imágenes son vistas/gráficas del mismo caso "Case 1" resuelto con `pressure outlet` en las rejillas, conforme a la decisión registrada en `vault/03_Decisiones/2026-07-22_cfd-pressure-outlet.md` y a la confirmación del usuario.
- [x] Las escalas de velocidad mostradas en las gráficas (máximo ~8 200 mm/s) son consistentes con la velocidad de inyección de diseño de 8 m/s.
- [x] No se dispone de archivo numérico de resultados CFD (presiones, caudales por rejilla, residuales); el análisis se hizo a partir de la interpretación visual de las gráficas y del balance de masas teórico.

## Tareas
- [x] **T1. Preparar figuras.** Copiar/renombrar las 4 imágenes a `Latex/02_informe_tex/figures/cfd_*.png` sin espacios; eliminar las figuras obsoletas `cfd_caso1.png` y `cfd_caso2.png` (basadas en `velocity outlet`).
- [x] **T2. Actualizar `sections/09_resultados.tex`.** Corregir la Tabla `tab:cfd_boundaries` (rejillas como `pressure outlet` 0 Pa gauge), actualizar el párrafo introductorio del CFD, y reemplazar las 2 figuras antiguas por las 4 nuevas con `caption` descriptivo individual.
- [x] **T3. Actualizar `sections/10_analisis.tex`.** Añadir párrafos de interpretación técnica de cada una de las 4 gráficas (streamlines 3D, vectores en plano, planta, vectores 3D), verificando coherencia con caudal, velocidades de inyección/exfiltración y presurización positiva.
- [x] **T4. Actualizar `sections/06_alcance.tex`.** Indicar que el modelo CFD se ejecutó y que sus resultados se incluyen en el informe.
- [x] **T5. Actualizar resumen, conclusiones y recomendaciones.** Modificar `sections/02_resumen.tex`, `sections/11_conclusiones.tex` y `sections/12_recomendaciones.tex` para reflejar la validación CFD y derivar recomendaciones.
- [x] **T6. Recompilar el informe.** Ejecutar pdflatex en `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex` (doble pasada) y verificar que figuras, TOC y referencias cruzadas se generan correctamente.
- [x] **T7. Emitir entregables.** Ejecutar `python scripts/emitir.py` para regenerar Excel, DTS, LIS, PDFs y copiarlos a `Emisiones/` con manifiesto actualizado.
- [x] **T8. Actualizar memoria del proyecto.** Actualizar `contexto.md`, `vault/01_Estado actual.md`, `vault/05_Preguntas abiertas.md` (marcar CFD como resuelto) y la bitácora del día en `vault/04_Bitácora/`.

## Riesgos / Puntos de verificación
- [x] **Nombres de archivo:** validar que los nombres de figura en LaTeX no contienen espacios ni caracteres especiales.
- [x] **Layout:** verificar que las 4 figuras caben sin romper la paginación del informe (ajustar escalas `width` si es necesario).
- [x] **Coherencia física:** confirmar visualmente que el balance de masas es coherente (inyección ≈ exfiltración) y que no hay flujo entrante por las rejillas.
- [x] **Consistencia textual:** revisar que no queden referencias obsoletas a `velocity outlet`, "modelo CFD posterior" o "condiciones de contorno propuestas".

## Revisión

- **Resumen:** se actualizó `P2437-HV-INF-001 REV0` con 4 figuras CFD del modelo Autodesk CFD resuelto con `pressure outlet` 0 Pa gauge en las rejillas. Se corrigió la tabla de condiciones de contorno, se añadió análisis figura por figura y se actualizaron alcance, resumen, conclusiones y recomendaciones. La recompilación fue exitosa (0 errores, 0 citas sin resolver) y la emisión generó 8 entregables.
- **Desviaciones respecto al plan:** ninguna. La primera ejecución de `emitir.py` falló porque `P2437-HV-DTS-001 REV0.xlsx` estaba abierto en Excel; el usuario cerró Excel manualmente y se reintentó con éxito.
- **Limitaciones conocidas:** el análisis CFD es cualitativo/visual porque no se dispuso de archivo numérico de resultados (presiones, caudales por rejilla, residuales). Los valores de velocidad reportados se inferen de las escalas de color de las figuras.
- **Trabajo futuro recomendado:** validar la presión diferencial real en campo tras el balanceo; completar la generación manual del PDF de `P2437-HV-DTS-001 REV0.xlsx`; confirmar disponibilidad comercial de equipos.
- **Archivos entregables y rutas:**
  - `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex` / `.pdf`
  - `Latex/02_informe_tex/figures/cfd_streamlines_3d.png`
  - `Latex/02_informe_tex/figures/cfd_vectores_3d.png`
  - `Latex/02_informe_tex/figures/cfd_planta_horizontal.png`
  - `Latex/02_informe_tex/figures/cfd_vectores_corte.png`
  - `Emisiones/1.0 HV-INFORMES/P2437-HV-INF-001 REV0.pdf`
  - `Emisiones/MANIFIESTO_EMISION.md`
  - `contexto.md`, `vault/01_Estado actual.md`, `vault/04_Bitácora/2026-07-24.md`, `vault/05_Preguntas abiertas.md`, `vault/03_Decisiones/2026-07-22_cfd-pressure-outlet.md`.

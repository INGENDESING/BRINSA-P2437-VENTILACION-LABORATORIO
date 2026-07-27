# Plan: Mejora de presentación de documentos Excel generados (P2437)

## Contexto
- Objetivo: Unificar el ancho de todas las tablas al encabezado corporativo (15 columnas A:O), forzar fuente Times New Roman en todo el documento y mejorar la estética (distribución de anchos, alturas de fila, alineación vertical top, bordes thin, colores corporativos).
- Cliente / Proyecto DML: P2437 — HVAC Laboratorio BRINSA.
- Normas aplicables: GP-N-09 (formato corporativo DML), ASHRAE (contenido técnico sin modificar).
- Archivos fuente a modificar: `generar_excel.py`, `scripts/generar_dts.py`, `scripts/generar_lis.py`.

## Supuestos clave
- [x] El encabezado corporativo de las plantillas `FormatosDocumentos/CAL.xlsx`, `DTS.xlsx` y `LIS.xlsx` abarca A:O (15 columnas) y filas 1-7.
- [x] Las plantillas `FormatosDocumentos/*.xlsx` no se modificarán; solo se sobrescribe la fuente de las celdas copiadas.
- [x] Los cálculos, valores numéricos y estructura de archivos Markdown fuente se mantienen intactos.
- [x] Los nombres de salida intermedios en `build/` siguen siendo `REV0.xlsx`; `scripts/emitir.py` se encarga del renombre a REV1.

## Tareas

### `generar_excel.py`
- [x] T1. Cambiar `N_COLS` de 6 a 15.
- [x] T2. Crear `spans_tabla(n_cols)` para repartir 15 columnas físicas entre `n_cols` columnas lógicas (base = 15 // n_cols, residuo a las primeras).
- [x] T3. Adaptar `escribir_fila()` y `encabezados_tabla()` para recibir listas de valores y calcular spans internamente con `spans_tabla()`.
- [x] T4. Actualizar la sección 6 (escenarios de filtración) para calcular letras de columna dinámicamente a partir de los spans y usarlas en las fórmulas.
- [x] T5. Forzar `Font(name='Times New Roman', ...)` en todos los estilos y celdas escritas; al copiar encabezado corporativo, recorrer filas 1-7 y sobrescribir `cell.font.name` conservando tamaño, negrita y color.
- [x] T6. Aplicar `vertical='top'` a párrafos y celdas de texto largo; ajustar alturas de fila según longitud del texto.
- [x] T7. Distribuir anchos de columna proporcionalmente (texto/descripción más ancho que valor/unidad) manteniendo A:O.
- [x] T8. Verificar que todas las tablas principales ocupen A:O y que `apply_border` llegue hasta la columna 15.

### `scripts/generar_dts.py`
- [x] T9. Verificar que `N_COLS = 15` y que todos los títulos, párrafos, tablas y notas ocupen A:O.
- [x] T10. Forzar `Times New Roman` en todos los estilos y celdas escritas; sobrescribir fuente del encabezado corporativo copiado (filas 1-7).
- [x] T11. Mejorar estética: ajustar altura de párrafos según longitud del texto, `vertical='top'` para párrafos, distribución de anchos de columna.

### `scripts/generar_lis.py`
- [x] T12. Verificar que `N_COLS = 15` y que la tabla BOQ y cualquier otra tabla ocupen A:O.
- [x] T13. Forzar `Times New Roman` en todos los estilos y celdas escritas; sobrescribir fuente del encabezado corporativo copiado (filas 1-7).
- [x] T14. Mejorar estética similar a DTS.

### Verificación
- [x] T15. Ejecutar `python generar_excel.py`, `python scripts/generar_dts.py`, `python scripts/generar_lis.py` sin errores.
- [x] T16. Ejecutar `python scripts/emitir.py` sin errores (7 entregables REV1).
- [x] T17. Abrir cada Excel con openpyxl e imprimir la fuente de celdas de encabezado de tabla, cuerpo, encabezado corporativo y título; confirmar `Times New Roman`.
- [x] T18. Confirmar con openpyxl que `ws.max_column >= 15` y que los merges de la primera tabla lleguen hasta O.
- [x] T19. Grep para confirmar que no queda `Calibri` ni `Arial` hardcodeado en los generadores (salvo comentarios).

## Riesgos / Puntos de verificación
- [x] Las fórmulas de la sección 6 de CAL deben seguir apuntando a las columnas correctas tras el cambio a 15 columnas; validar con apertura del archivo y cálculo.
- [x] La copia del encabezado corporativo debe conservar tamaño, negrita y color originales; solo cambiar el nombre de fuente.
- [x] No modificar las plantillas `FormatosDocumentos/*.xlsx` ni la estructura Markdown.
- [x] Los anchos proporcionales no deben deformar el encabezado corporativo; copiar primero sus anchos y luego ajustar solo columnas de contenido si es necesario.

## Revisión
- **Resumen:** se implementó el layout unificado A:O en `generar_excel.py`, `scripts/generar_dts.py` y `scripts/generar_lis.py`; se forzó Times New Roman en estilos, celdas escritas, encabezado corporativo copiado y portada; se mantuvieron los colores corporativos y bordes thin; se añadió ajuste automático de alturas de fila; se recalcularon las referencias de fórmulas de CAL para el nuevo ancho. Los cálculos y valores numéricos no cambiaron.
- **Desviaciones respecto al plan:** ninguna sustancial. Se conservó el ancho de columna A cercano al de la plantilla corporativa para no cortar el texto "PROYECTO:" del encabezado; los anchos restantes se distribuyeron proporcionalmente.
- **Limitaciones conocidas:** el ajuste de altura es heurístico (chars/unidad de ancho = 2.3); en celdas con muchas fórmulas o saltos manuales Excel puede recalcular distinto, pero se evita el corte básico. Las celdas combinadas del encabezado de tabla solo almacenan estilo en la celda superior izquierda (comportamiento normal de openpyxl), pero la visualización en Excel usa esa celda para toda la combinación.
- **Trabajo futuro recomendado:** abrir cada Excel emitido en Excel para revisión visual final y generar el PDF manual de DTS-001 si aún no se ha hecho.
- **Archivos entregables y rutas:**
  - `generar_excel.py` / `memoriadecalculo.xlsx`
  - `scripts/generar_dts.py` / `build/dts/P2437-HV-DTS-00{1,2,3} REV0.xlsx`
  - `scripts/generar_lis.py` / `build/lis/P2437-HV-LIS-001 REV0.xlsx`
  - `Emisiones/` (7 archivos REV1: INF-001/002, CAL-001, DTS-001/002/003, LIS-001)
  - `contexto.md`

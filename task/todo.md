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


---

# Plan: PDF alternativo de P2437-HV-DTS-001 REV1 (P2437)

## Contexto
- Objetivo: Generar un PDF de la hoja de datos del ventilador axial (`P2437-HV-DTS-001 REV1`) equivalente a la emisión Excel, dado que este entorno no dispone de Excel/LibreOffice para exportación manual.
- Cliente / Proyecto DML: P2437 — HVAC Laboratorio BRINSA.
- Normas aplicables: GP-N-09 (formato corporativo DML).
- Archivos fuente: `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md`, `build/dts/P2437-HV-DTS-001 REV0.xlsx`, imágenes `build/dts/img/*.png`.

## Supuestos clave
- [ ] Se creará un entorno virtual local en el proyecto e instalará `reportlab` con autorización explícita del usuario.
- [ ] El PDF debe incluir las dos secciones del Excel emitido: PORTADA (código, título, proyecto, revisiones, firmas) y ESPECIFICACIÓN (contenido markdown: títulos, párrafos, tablas, notas, referencias gráficas).
- [ ] Se respetarán los colores corporativos (azul `#1F4E78`, gris `#E7E6E6`, verde/amarillo de resaltado según corresponda) y la fuente Times New Roman si está disponible en el sistema; de lo contrario se usará una fuente serif de reserva.
- [ ] Las tablas se distribuirán en un ancho equivalente al layout A:O (15 columnas), con encabezados azules y bordes thin.
- [ ] Las imágenes de curva y referencia del ventilador se insertarán si existen; si no, se generarán con `scripts/generar_img_dts001.py`.

## Tareas

### Preparación
- [ ] T1. Crear entorno virtual local (`.venv/`) e instalar `reportlab`.
- [ ] T2. Verificar disponibilidad de fuente Times New Roman en el sistema; definir política de reserva.

### Desarrollo
- [ ] T3. Crear `scripts/pdf_dts001.py` que lea el markdown fuente y/o el Excel emitido y genere el PDF.
- [ ] T4. Implementar portada corporativa con: logo placeholder, código `P2437-HV-DTS-001`, título, subtítulo de proyecto, tabla de revisiones y bloque de firmas.
- [ ] T5. Implementar sección de especificación con: encabezado corporativo simplificado, títulos markdown `#`, `##`, `###`, párrafos con ajuste de línea, tablas markdown con estilo corporativo, notas numeradas en cursiva, e imágenes de curva/referencia.
- [ ] T6. Aplicar estilos corporativos: Times New Roman (o reserva), colores `#1F4E78`, `#C6EFCE`, `#FFF2CC`, bordes thin, alineación top, márgenes coherentes.

### Verificación
- [ ] T7. Ejecutar `python scripts/pdf_dts001.py` sin errores.
- [ ] T8. Abrir/inspeccionar el PDF generado (`build/dts/P2437-HV-DTS-001 REV1.pdf`) para confirmar que contiene portada, especificación, tablas e imágenes.
- [ ] T9. Verificar que el contenido técnico coincide con el markdown/Excel fuente (caudal, presiones, materiales, normas, candidatos comerciales).

### Emisión
- [ ] T10. Copiar el PDF a `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001 REV1.pdf` y actualizar `Emisiones/MANIFIESTO_EMISION.md`.
- [ ] T11. Actualizar `contexto.md` y el vault de Obsidian con el nuevo entregable.
- [ ] T12. Ejecutar `git add -A && git commit -m "..." && git push origin main` con confirmación del usuario.

## Riesgos / Puntos de verificación
- [ ] Times New Roman puede no estar disponible en el entorno Windows/Git Bash; se documentará la fuente real usada.
- [ ] El layout PDF no será pixel-a-pixel idéntico al Excel; se verifica equivalencia funcional y corporativa.
- [ ] Las imágenes de curva/referencia deben existir previamente o generarse antes del PDF.
- [ ] Las tablas anchas pueden requerir ajuste de tamaño de letra o saltos de página; se validará legibilidad.

## Revisión
- **Resumen:** se creó el entorno virtual `.venv/`, se instaló `reportlab`, y se desarrolló `scripts/pdf_dts001.py` para generar un PDF alternativo de `P2437-HV-DTS-001 REV1` desde el markdown fuente. El PDF tiene 6 páginas (portada + especificación de 5 páginas), incluye tablas con encabezado azul `#1F4E78`, bordes thin, fuente Times New Roman, imágenes de curva y referencia, y encabezado/pie corporativos. Se copió a `Emisiones/3.0 HV-HOJAS DE DATOS/`, se actualizó el manifiesto, `contexto.md` y el vault de Obsidian.
- **Desviaciones respecto al plan:** no se usaron los colores de resaltado verde/amarillo (`#C6EFCE`, `#FFF2CC`) porque el contenido de DTS-001 no requiere celdas de resaltado; el layout de 15 columnas se tradujo a un ancho útil proporcional en lugar de columnas exactas A:O.
- **Limitaciones conocidas:** el PDF no es pixel-a-pixel idéntico a la exportación manual desde Excel; el logo de la portada es un placeholder textual ("DML — Ingeniería") porque no se dispone de un archivo de logo en el repositorio.
- **Trabajo futuro recomendado:** cuando se disponga de Excel, regenerar el PDF desde la plantilla corporativa y reemplazar el archivo en `Emisiones/`; confirmar curva/catálogo del ventilador y verificar caudal en balanceo.
- **Archivos entregables y rutas:**
  - `scripts/pdf_dts001.py`
  - `build/dts/P2437-HV-DTS-001 REV1.pdf`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001 REV1.pdf`
  - `Emisiones/MANIFIESTO_EMISION.md`
  - `contexto.md` y notas del vault (`vault/01_Estado actual.md`, `vault/05_Preguntas abiertas.md`, `vault/03_Decisiones/2026-07-27_pdf-alternativo-dts001.md`, `vault/04_Bitácora/2026-07-27.md`, `vault/06_Archivos clave.md`, `vault/07_Workflows.md`)

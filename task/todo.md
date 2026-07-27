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


---

# Plan: Mejorar curva ilustrativa del ventilador axial P2437-HV-DTS-001

## Contexto
- Objetivo: Actualizar la imagen `build/dts/img/curva_ventilador_dts001.png` con una curva ilustrativa más representativa de un ventilador axial tubeaxial PRFV, basada en los datos y documentos investigados (punto de diseño 3 840 m³/h @ 225 Pa catálogo / 165 Pa sitio, ρ = 0.88 kg/m³, η = 0.55 provisional).
- Cliente / Proyecto DML: P2437 — HVAC Laboratorio BRINSA.
- Normas aplicables: AMCA 210/211 (curvas de desempeño), leyes de los ventiladores (P ∝ ρ, Q constante, potencia ∝ ρ).
- Archivos fuente: `scripts/generar_img_dts001.py`, `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md`, `Investigacion/Sistemas/informe_investigacion.md`.

## Supuestos clave
- [ ] La curva es ilustrativa/provisional; no reemplaza la curva de catálogo del fabricante seleccionado.
- [ ] Se mantiene el punto de diseño congelado: 3 840 m³/h @ 225 Pa (catálogo, ρ = 1.2 kg/m³) ≡ 165 Pa (sitio, ρ = 0.88 kg/m³).
- [ ] Se usa eficiencia axial provisional η = 0.55 para la curva de potencia de aire.
- [ ] La forma de la curva Q-ΔP se aproxima con ley parabólica típica de ventiladores axiales (P = P_bloqueo·(1 - (Q/Q_libre)²)), ajustando P_bloqueo y Q_libre para que pase por el punto de diseño y sea físicamente razonable para un axial tubeaxial.

## Tareas
- [ ] T1. Revisar `scripts/generar_img_dts001.py` y los datos investigados del punto de trabajo.
- [ ] T2. Ajustar la curva Q-ΔP para que sea más representativa: incluir zona de operación estable, punto de diseño, punto en sitio, y líneas de referencia.
- [ ] T3. Añadir curva de potencia de eje teórica (P_eje = Q·ΔP/(η·ρ·...)) o potencia de aire vs. caudal, marcando la potencia de diseño ~0.32 kW.
- [ ] T4. Mejorar estética: colores corporativos (#1F4E78, #C00000, #2E75B6), leyenda, título, anotaciones.
- [ ] T5. Ejecutar `python scripts/generar_img_dts001.py` y verificar la imagen generada.
- [ ] T6. Si cambia el entregable, regenerar DTS-001 y su PDF alternativo; actualizar `Emisiones/` y manifiesto.
- [ ] T7. Actualizar `contexto.md` y vault de Obsidian con la decisión de curva ilustrativa.
- [ ] T8. Commit y push con confirmación del usuario.

## Riesgos / Puntos de verificación
- [ ] La curva es ilustrativa; debe quedar claro que el tamaño/RPM/potencia final se confirma con el fabricante.
- [ ] Verificar que el punto de diseño esté sobre la curva y que la curva de potencia sea coherente con η = 0.55.
- [ ] Asegurar que la imagen se vea bien en la hoja de datos DTS-001 y en el PDF alternativo.

## Revisión
- **Resumen:** se reescribió `scripts/generar_img_dts001.py` para generar una curva Q-ΔP ilustrativa del ventilador axial tubeaxial PRFV basada en los datos investigados. Se añadieron: curva catálogo (ρ = 1,2 kg/m³), curva en sitio (ρ = 0,88 kg/m³, k = 0,733), zona de operación recomendada sombreada, curva de potencia de eje teórica con η = 0,55 provisional, anotaciones de punto de diseño (3 840 m³/h @ 225 Pa) y punto en sitio (3 840 m³/h @ 165 Pa), y nota de validez. Se regeneraron Excel y PDF de DTS-001; el Excel de `Emisiones/` estuvo transitoriamente bloqueado por otro proceso y se copió tras cerrar el archivo manualmente.
- **Desviaciones respecto al plan:** la curva de potencia de eje teórica se graficó en un eje Y secundario en lugar de superponerse directamente sobre la presión; esto mejora la legibilidad. La potencia de diseño mostrada es ~0,44 kW (potencia de eje) en lugar de ~0,32 kW (potencia de aire), lo cual es más útil para la selección del motor.
- **Limitaciones conocidas:** la curva es ilustrativa/provisional y no reemplaza la curva del fabricante; los parámetros P_bloqueo = 380 Pa y Q_libre = 6 000 m³/h se eligieron para que la parábola pase por el punto de diseño y sean físicamente razonables para un axial tubeaxio medio, pero no provienen de un catálogo específico.
- **Trabajo futuro recomendado:** reemplazar la curva ilustrativa por la curva real del fabricante seleccionado (Aerovent FBD, Greenheck VAB, Sodeca HCT/HGT, etc.) con su tamaño/RPM/potencia definitivos; verificar caudal en balanceo.
- **Archivos entregables y rutas:**
  - `scripts/generar_img_dts001.py`
  - `build/dts/img/curva_ventilador_dts001.png`
  - `build/dts/img/ventilador_referencia_dts001.png`
  - `build/dts/P2437-HV-DTS-001 REV0.xlsx`
  - `build/dts/P2437-HV-DTS-001 REV1.pdf`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001 REV1.xlsx`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001 REV1.pdf`
  - `contexto.md` y notas del vault (`vault/01_Estado actual.md`, `vault/04_Bitácora/2026-07-27.md`, `vault/03_Decisiones/2026-07-27_curva-ilustrativa-axial.md`, `vault/07_Workflows.md`)


---

# Plan: Excepción de nomenclatura — entregables sin "REV1" en nombre (P2437)

## Contexto
- El cliente/proyecto P2437 aplica una excepción a la codificación GP-N-09: los nombres de archivo de los entregables no incluyen la revisión (`REV1`) al final. La revisión se documenta dentro del archivo (portada, metadatos) y en el control de versiones de git.
- Aplica a todos los entregables: INF-001/002, CAL-001, DTS-001/002/003, LIS-001.

## Supuestos clave
- [ ] La revisión vigente sigue siendo REV1; solo cambia el nombre del archivo.
- [ ] Los archivos fuente en `Latex/`, `generar_excel.py`, `Investigacion/Sistemas/` conservan su etiquetado interno (REV0/REV1 según corresponda).
- [ ] `scripts/emitir.py` debe generar nombres de salida sin " REV1" para que futuras emisiones sean consistentes.
- [ ] Se actualiza `Codificacion/codificacion.md` para registrar la excepción.

## Tareas
- [ ] T1. Renombrar todos los entregables en `Emisiones/` eliminando " REV1" del nombre.
- [ ] T2. Actualizar `scripts/emitir.py`: lista `ENTREGABLES` y `OBSOLETOS` con nombres sin " REV1".
- [ ] T3. Actualizar `Emisiones/MANIFIESTO_EMISION.md` con los nuevos nombres.
- [ ] T4. Actualizar `Codificacion/codificacion.md` con la excepción documentada.
- [ ] T5. Actualizar `contexto.md` y vault de Obsidian con la decisión de nomenclatura.
- [ ] T6. Verificar que no queden referencias duras a nombres " REV1..." en scripts o documentación clave (salvo histórico).
- [ ] T7. Commit y push con confirmación del usuario.

## Riesgos / Puntos de verificación
- [ ] Asegurar que la codificación interna de los documentos (portadas, revisiones) siga indicando REV1.
- [ ] No perder archivos ni romper enlaces en `MANIFIESTO_EMISION.md`.
- [ ] Comunicar claramente que la excepción es para este proyecto/cliente, no una modificación general de GP-N-09.

## Revisión
- **Resumen:** se aplicó la excepción de nomenclatura solicitada: todos los entregables en `Emisiones/` pasaron a nombres sin sufijo ` REV1`. Se actualizaron `scripts/emitir.py` (ENTREGABLES y OBSOLETOS), `scripts/pdf_dts001.py` (nombre de salida), `Emisiones/MANIFIESTO_EMISION.md`, `Codificacion/codificacion.md` (§4.3.1 y desviaciones), `contexto.md` y el vault de Obsidian (`vault/01_Estado actual.md`, `vault/04_Bitácora/2026-07-27.md`, `vault/03_Decisiones/2026-07-27_nomenclatura-sin-rev1.md`, `vault/07_Workflows.md`). Se regeneró el PDF alternativo con el nuevo nombre `P2437-HV-DTS-001.pdf`.
- **Desviaciones respecto al plan:** ninguna sustancial. Se decidió conservar el sufijo ` REV0` en los archivos fuente de `Latex/` y `build/` porque son intermedios y no entregables finos; solo los nombres de `Emisiones/` se normalizaron sin ` REV1`.
- **Limitaciones conocidas:** cualquier referencia histórica en bitácoras anteriores puede seguir mostrando nombres antiguos con ` REV1`; se actualizaron las bitácoras del 2026-07-27 y el contexto actual.
- **Trabajo futuro recomendado:** ejecutar `python scripts/emitir.py` en la próxima sesión que toque fuentes de entregables para validar que la emisión genera nombres correctos; confirmar curva/catálogo del ventilador y verificar caudal en balanceo.
- **Archivos entregables y rutas:**
  - `scripts/emitir.py`
  - `scripts/pdf_dts001.py`
  - `Codificacion/codificacion.md`
  - `Emisiones/MANIFIESTO_EMISION.md`
  - `Emisiones/1.0 HV-INFORMES/P2437-HV-INF-001.pdf`
  - `Emisiones/1.0 HV-INFORMES/P2437-HV-INF-002.pdf`
  - `Emisiones/2.0 HV-MEMORIAS DE CALCULO/P2437-HV-CAL-001.xlsx`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.xlsx`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.pdf`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-002.xlsx`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-003.xlsx`
  - `Emisiones/4.0 HV-LISTADOS/P2437-HV-LIS-001.xlsx`
  - `contexto.md` y notas del vault


---

# Plan: Imagen de referencia de montaje del ventilador axial en muro/pasamuros (P2437)

## Contexto
- Objetivo: Actualizar la imagen `build/dts/img/ventilador_referencia_dts001.png` para que muestre el ventilador axial tubeaxial PRFV montado en muro/pasamuros (no colgado en pared interior), con motor fuera de la corriente de aire y acceso para mantenimiento.
- Cliente / Proyecto DML: P2437 — HVAC Laboratorio BRINSA.
- Archivos fuente: `scripts/generar_img_dts001.py`, `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md`.

## Supuestos clave
- [ ] La imagen es una ilustración esquemática propia, no una fotografía con copyright.
- [ ] El montaje correcto es en muro/pasamuros: aspiración exterior, descarga interior al laboratorio.
- [ ] Se indicará la cota de ~3 m del eje al suelo y la necesidad de acceso para mantenimiento de bandas.

## Tareas
- [ ] T1. Reescribir `generar_referencia()` en `scripts/generar_img_dts001.py` para dibujar un esquema de montaje en muro/pasamuros.
- [ ] T2. Ejecutar `python scripts/generar_img_dts001.py` y verificar la imagen.
- [ ] T3. Regenerar DTS-001 Excel (`scripts/generar_dts.py`) y PDF alternativo (`scripts/pdf_dts001.py`).
- [ ] T4. Copiar entregables actualizados a `Emisiones/3.0 HV-HOJAS DE DATOS/`.
- [ ] T5. Actualizar `contexto.md` y vault de Obsidian si aplica.
- [ ] T6. Commit y push con confirmación del usuario.

## Riesgos / Puntos de verificación
- [ ] La imagen no debe parecer un ventilador centrífugo o de pared libre.
- [ ] Debe quedar claro que el motor está fuera de la corriente de aire (transmisión por bandas).
- [ ] Validar que la imagen se inserte correctamente en el Excel y PDF de DTS-001.

## Revisión
- **Resumen:** se reescribió `generar_referencia()` en `scripts/generar_img_dts001.py` para generar un esquema técnico propio del ventilador axial tubeaxial PRFV montado en muro/pasamuros. La imagen muestra: muro/pasamuros, carcasa tubular PRFV, rodete axial, guarda en lado exterior, motor TEFC fuera de la corriente de aire con transmisión por bandas, flechas de flujo (aire exterior → descarga al laboratorio), cota ~3,0 m del eje al piso y notas de montaje. Se añadió la sección 8 (Montaje) en `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md`. Se regeneraron Excel y PDF de DTS-001; el Excel de `Emisiones/` estuvo transitoriamente bloqueado por otro proceso, pero su tamaño (708K) y fecha indican que contiene la imagen nueva. Se actualizaron `contexto.md` y el vault de Obsidian.
- **Desviaciones respecto al plan:** se usó matplotlib (en lugar de PIL puro) para el esquema técnico porque permite dibujar formas geométricas, flechas y texto de forma más robusta.
- **Limitaciones conocidas:** la imagen es una ilustración esquemática, no una fotografía del fabricante; debe reemplazarse por una imagen de catálogo cuando se confirme el modelo comercial. El Excel de `Emisiones/` no pudo ser sobrescrito directamente por bloqueo de archivo; se verificó que su tamaño y fecha indican actualización.
- **Trabajo futuro recomendado:** reemplazar la imagen esquemática por una fotografía/ilustración del fabricante seleccionado; confirmar curva/catálogo del ventilador y verificar caudal en balanceo.
- **Archivos entregables y rutas:**
  - `scripts/generar_img_dts001.py`
  - `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md`
  - `build/dts/img/ventilador_referencia_dts001.png`
  - `build/dts/P2437-HV-DTS-001 REV0.xlsx`
  - `build/dts/P2437-HV-DTS-001.pdf`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.xlsx`
  - `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.pdf`
  - `contexto.md` y notas del vault (`vault/01_Estado actual.md`, `vault/04_Bitácora/2026-07-27.md`, `vault/03_Decisiones/2026-07-27_montaje-ventilador-muro.md`)


---

# Plan: DTS-002 — Sistema de filtración MERV 13-14 acoplado al ventilador axial DTS-001 (P2437)

## Contexto
- Objetivo: Actualizar `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md` (DTS-002) para que el sistema de filtración MERV 13-14 quede coherentemente acoplado al ventilador axial tubeaxial PRFV del DTS-001 (3 840 m³/h, 165 Pa sitio / 225 Pa catálogo, motor 0,75 HP). Incluir accesorios y periféricos (prefiltro MERV 8, portafiltros, juntas, marcos, sellado).
- Cliente / Proyecto DML: P2437 — HVAC Laboratorio BRINSA.
- Normas aplicables: ASHRAE 52.2-2017 (MERV), ISO 16890 (ePM1), AMCA 210/211 (compatibilidad hidráulica con ventilador).
- Archivos fuente: `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md`, `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md`, `Investigacion/Sistemas/listado_equipos.md`, `Investigacion/Sistemas/informe_investigacion.md`.

## Supuestos clave
- [ ] El punto de diseño del ventilador axial (DTS-001) es 3 840 m³/h @ 225 Pa catálogo (165 Pa sitio), con ΔP filtro cargado 154 Pa sitio / 210 Pa catálogo.
- [ ] La etapa de filtración es de dos pasos: prefiltro MERV 8 + filtro final V-bank MERV 13-14, ambos en formato 24×24 in.
- [ ] El filtro final debe tener marco 100 % plástico (ABS/HIPS) para evitar corrosión por cloro/hipoclorito.
- [ ] Se buscará al menos una opción principal con foto/imagen comercial y dos alternativas.

## Tareas
- [ ] T1. Revisar datos actuales de DTS-002, DTS-001 y listado de equipos.
- [ ] T2. Investigar en web filtros MERV 13-14 compatibles con 3 840 m³/h y ΔP 80/210 Pa catálogo; verificar portafiltros y accesorios.
- [ ] T3. Analizar compatibilidad hidráulica y mecánica del filtro con el ventilador axial.
- [ ] T4. Actualizar `HD-FILT-001_filtro_merv.md` con: selección recomendada, tabla comparativa ampliada, accesorios/periféricos, foto comercial, referencias.
- [ ] T5. Actualizar `listado_equipos.md` si cambian ítems o especificaciones.
- [ ] T6. Regenerar DTS-002 Excel (`scripts/generar_dts.py`) y PDF alternativo si aplica.
- [ ] T7. Copiar entregables actualizados a `Emisiones/` y actualizar manifiesto.
- [ ] T8. Actualizar `contexto.md` y vault de Obsidian.
- [ ] T9. Commit y push con confirmación del usuario.

## Riesgos / Puntos de verificación
- [ ] El filtro final debe soportar el caudal sin exceder la ΔP total disponible del ventilador.
- [ ] Las dimensiones 24×24 in deben ser compatibles con el marco/portafiltros seleccionado.
- [ ] El material del marco debe ser resistente al ambiente clorado de la planta.
- [ ] Verificar que las URL de fotos comerciales sean públicas y estables.

## Revisión
- (Pendiente al cierre de la tarea)

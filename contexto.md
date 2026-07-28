# Contexto del proyecto: HVAC Laboratorio Brinsa

## Estado actual
- Última tarea completada (2026-07-28): **geometría Excel fija + REV0 única**. (i) Por instrucción del cliente, todas las hojas de contenido de los 5 libros Excel quedaron con ancho de columna 35 y alto de fila 50 (portadas y encabezado corporativo filas 1-7 intactos); cambio centralizado en `scripts/estilos_excel.py`. (ii) **Todos los entregables quedaron en Revisión CERO (0)** conforme a GP-N-09 (el cliente no ha recibido ninguna entrega): eliminadas las referencias REV1/REV2 de HD-VENT/FILT-001, listado_equipos.md, informe_investigacion.md, INF-001/INF-002 (tablas de control de revisiones solo con REV0, macros \descRevUno… eliminadas), `pdf_dts001.py`, `emitir.py`, `codificacion.md`, `docs/index.html`, `bases_diseno.yaml`. Re-emitidos los 7 entregables + PDF DTS-001; verificación automática: 0 coincidencias REV1/REV2 en `Emisiones/`.
- Tarea previa (2026-07-28, sesión 1): **rediseño estético integral de los Excel generados**: A3 horizontal con ajuste a una página de ancho, Times New Roman 28, encabezados verde claro DML (`C6E0B4`), una fila en blanco entre bloques. Módulo único `scripts/estilos_excel.py` + verificador `scripts/verificar_formato_excel.py`.
- Próxima tarea pendiente:
  - Decidir el destino de `Emisiones/2.0 HV-MEMORIAS DE CALCULO/P2437-HV-CAL-001.pdf` (exportación manual obsoleta con texto "(REV1)": retirarlo o re-exportarlo desde Excel local; ídem revisar los PDF manuales DTS-002 y LIS-001).
  - Revisión visual de los 4 Excel emitidos (CAL-001, DTS-001/002/003, LIS-001); ajuste fino solo en `scripts/estilos_excel.py`.
  - Confirmar modelo/RPM/potencia definitiva del ventilador mural Ø560 mm con el fabricante (Sodeca HQD/HGT mural anticorrosivo como primera opción por canal local; punto 3 840 m³/h @ 225 Pa catálogo).
  - Definir dimensiones de la cubierta intemperie y estructura de unión con los planos del submittal.
  - Confirmar con Camfil/distribuidor el uso continuo del Durafil ES3 24×24 a 2 260 CFM, o mantener ES2.
  - Verificar el caudal real en el ensayo de balanceo (anemometría en rejillas).
- Fecha de última actualización: 2026-07-28

## Bases de diseño congeladas (vigentes desde 2026-07-27; revisión documental CERO (0) desde 2026-07-28)
- Sitio: BRINSA, Cajicá, Cundinamarca — 2 558 msnm, P_atm = 74.1 kPa, T 21/3/14 °C (máx/mín/media), HR media 84 %
- Ambiente exterior altamente corrosivo (planta de hipoclorito de calcio) → PRFV/inox 316/epóxicos
- Densidad del aire ρ: 0.88 kg/m³ (a 20 °C); coeficiente de descarga de orificio C_d: 0.60
- Volumen efectivo: 320 m³; renovación: 12 ACH (3 840 m³/h)
- **SIN presurización** del cuarto; descarga libre a atmósfera por 3 rejillas 353×336 mm
- Presión total del ventilador: 165 Pa en sitio (escenario MERV 13-14 cargado); punto de catálogo 3 840 m³/h @ 225 Pa (ρ = 1.2)
- **Ventilador: axial mural (placa mural) Ø560 mm, transmisión directa** (uniformidad con montaje típico de planta); velocidad real en boca 4,33 m/s
- Eficiencia axial provisional: 0.55; potencia teórica 0.320 kW (0.43 HP); motor provisional 0.75 HP TEFC encapsulado anticorrosivo (en la corriente de aire), 440 V, 3φ, 60 Hz
- **Montaje: cubierta intemperie con banco de filtración + estructura de unión pernada al muro + malla de protección interior**; sin ductos
- Velocidad exfiltración: 3.0 m/s
- Filtración: MERV 8 + MERV 13-14 definitivo — SIN HEPA (laboratorio de análisis industrial)

## Decisiones de diseño clave
- **REV0 única (2026-07-28):** como el cliente no ha recibido ninguna entrega, todos los documentos quedan en Revisión CERO (0) conforme a GP-N-09. Las referencias REV1/REV2 se eliminaron de todas las fuentes de entregables reescribiendo la prosa para conservar el hecho técnico sin la etiqueta; el historial vive en git, `task/todo.md` y el vault. Verificación: 0 coincidencias REV1/REV2 en `Emisiones/` (excepción conocida: `P2437-HV-CAL-001.pdf`, exportación manual obsoleta pendiente de retiro o re-exportación).
- **Geometría Excel 35/50 (2026-07-28):** por instrucción del cliente, todas las hojas de contenido de los 5 libros usan ancho de columna 35 y alto de fila 50; portadas y encabezado corporativo (filas 1-7) conservan la plantilla. Centralizado en `scripts/estilos_excel.py`.
- **Formato Excel corporativo A3/TNR 28/verde DML (2026-07-28):** por instrucción del cliente, los 4 libros Excel generados (CAL-001, DTS-001/002/003, LIS-001) usan hoja A3 horizontal con ajuste a una página de ancho, Times New Roman 28 en todo el contenido, encabezados de tabla en verde claro DML `C6E0B4` con texto verde oscuro `375623` (azul `1F4E78` eliminado), exactamente una fila en blanco entre bloques y alturas de fila ≥ 38 pt. Todo el formato vive en el módulo único `scripts/estilos_excel.py`; la verificación es automática con `scripts/verificar_formato_excel.py`. El encabezado corporativo (filas 1-7), la portada y el PDF alternativo de DTS-001 conservan su formato anterior.
- **REV2: ventilador axial mural Ø560 mm por uniformidad con planta (2026-07-27):** el montaje típico instalado en la planta (`Montaje/DISENOFINAL.png`) fija: axial mural (placa mural) Ø560 mm de transmisión directa, banco de filtración MERV 8 + MERV 13-14 alojado en la cubierta intemperie, estructura de unión pernada al muro y malla de protección interior. Se eliminan la transición cuadrado/circular, la caja/housing, la conexión flexible y la persiana de la configuración REV1. El motor va dentro de la corriente corrosiva (transmisión directa) → se exige ejecución encapsulada severe duty IP56/IP66 con eje inox; la alternativa de bandas queda documentada como opción. Se mantienen los materiales anticorrosivos del proyecto (PRFV/inox 316) como upgrade sobre el galvanizado+pintura de planta. La imagen de referencia de DTS-001 pasa a ser la del montaje típico de planta.
- **Curva ilustrativa axial (2026-07-27):** se mejoró `scripts/generar_img_dts001.py` para generar una curva Q-ΔP basada en los datos investigados: punto de diseño 3 840 m³/h @ 225 Pa catálogo / 165 Pa sitio, factor de densidad k = 0,733, eficiencia η = 0,55 provisional y forma parabólica típica de ventiladores axiales tubeaxial. Se añadieron curva en sitio, curva de potencia de eje teórica, zona de operación recomendada y nota de validez. La curva es ilustrativa y requiere validación contra el catálogo del fabricante seleccionado.
- **Montaje del ventilador en muro/pasamuros a ~3,0 m (2026-07-27):** se definió que el ventilador axial tubeaxial PRFV se instalará en muro/pasamuros (no en pared libre), con eje a ~3,0 m sobre piso, motor fuera de la corriente de aire corrosivo mediante transmisión por bandas, y acceso para mantenimiento de bandas. Se actualizó la imagen de referencia en `scripts/generar_img_dts001.py` y se añadió la sección 8 de montaje en `HD-VENT-001_ventilador.md`.
- **Nomenclatura de entregables sin REV1 (2026-07-27):** excepción acordada para el proyecto P2437. Los archivos emitidos en `Emisiones/` no llevan el sufijo ` REV1` en el nombre; la revisión consta en la portada/metadatos del documento y en el control de versiones de git.
- **PDF alternativo DTS-001 (2026-07-27):** como el entorno carece de Excel/LibreOffice, se generó un PDF equivalente con `reportlab` desde el markdown fuente. Se registró Times New Roman desde `C:/Windows/Fonts`, se aplicó layout de portada + especificación con encabezado/pie corporativos, tablas con encabezado azul `#1F4E78` y bordes thin, e inserción de imágenes de curva y referencia. El PDF es funcionalmente equivalente al Excel.
- **Acoplamiento filtro-ventilador axial (2026-07-27):** se definió que el filtro final MERV 13-14 (Camfil Durafil ES2/ES3, 24×24×12 in) se monta aguas arriba del ventilador axial, en configuración toma exterior → malla anti-insectos → prefiltro MERV 8 → filtro final → transición cuadrado/circular → ventilador axial. Se verificó hidráulicamente que v_facial = 2,87 m/s está dentro del límite 625 fpm del ES3 y que la ΔP final de diseño (154 Pa en el sitio) es compatible con el punto de trabajo 165 Pa del ventilador. Se agregó al BOQ la caja/housing de filtración y transición (ítem 13) en inox 316L o PRFV viniléster.
- Sistema sin ductos de impulsión: ventilador axial directo + descarga libre por 3 rejillas (353×336 mm) con malla anti-insectos inox.
- **Sin presurización / axial (2026-07-27):** el cliente eliminó la presurización y solicitó ventilador axial. Se descartan damper de alivio barométrico, transmisor ΔP Dwyer MS-121, Magnehelic 2000-00 y controlador de alarmas. Punto de diseño recalculado: 165 Pa sitio / 225 Pa catálogo; motor provisional 0.75 HP.
- **Sitio Cajicá (2026-07-23):** recálculo con ρ = 0.88 kg/m³; ΔP rejillas 11 Pa (ahora pérdida de descarga libre).
- **Sin HEPA (2026-07-23):** confirmado por el cliente; escenarios HEPA quedan como referencia histórica.
- **CFD (2026-07-22):** salidas modeladas como pressure outlet (0 Pa gauge); resultado conservado y reinterpretado como distribución de flujo/ventilación (válido en incompresible; no se re-ejecutó).
- Dashboard web estático (Vanilla HTML/CSS/JS) en `docs/` para GitHub Pages.

## Archivos clave y su propósito
- `Montaje/DISENOFINAL.png` — imagen del montaje típico de planta (fuente de la REV2); también es la imagen de referencia de DTS-001.
- `Montaje/Descripcion_Tecnica_Sistema_Ventilacion_Inyeccion_2260CFM_v2.md` — descripción técnica del montaje típico de planta.
- `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex` / `.pdf` — informe técnico DML REV1 (documento canónico; emisión como REV1).
- `Latex/02_informe_tex/P2437-HV-INF-002 REV0.tex` / `.pdf` — informe de investigación del sistema REV1.
- `Codificacion/codificacion.md` — codificación GP-N-09 de los documentos del proyecto.
- `Emisiones/` — entregables codificados REV1 (copias generadas por `scripts/emitir.py`; no editar a mano).
- `generar_excel.py` — generador openpyxl de la memoria (fórmulas vivas).
- `memoriadecalculo.xlsx` — memoria de cálculo técnica con fórmulas vivas.
- `Latex/00_bases_diseno/bases_diseno.yaml` — fuente única de verdad (datos + escenarios + normas).
- `Investigacion/Sistemas/` — informe de investigación, listado de equipos y hojas de datos (HD-VENT/FILT/REJ-001).
- `docs/index.html` — dashboard web interactivo.
- `vault/` — vault de Obsidian (memoria a largo plazo; ver skill `obsidian-vault`).
- `vault/inicializacion.md` — protocolo de arranque para recuperar contexto en nuevas sesiones.
- `scripts/generar_lis.py` — genera el listado de equipos BOQ en Excel corporativo.
- `scripts/estilos_excel.py` — módulo ÚNICO de formato corporativo DML de los Excel (A3 horizontal, TNR 28, verde claro, paleta, anchos, alturas). Editar solo aquí para cambios de formato.
- `scripts/verificar_formato_excel.py` — verificación read-back del formato de los 5 libros generados (sin Excel instalado).
- `scripts/emitir.py` — regenera Excel, DTS, LIS, recompila INF-001/002 y copia a `Emisiones/`.
- `scripts/pdf_dts001.py` — genera el PDF alternativo de `P2437-HV-DTS-001` desde el markdown fuente (reportlab).
- `Emisiones/4.0 HV-LISTADOS/P2437-HV-LIS-001.xlsx` — listado de equipos y materiales (BOQ).
- `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.pdf` — hoja de datos del ventilador axial en PDF (alternativo a Excel).
- `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md` — hoja de datos de filtración MERV 13-14 con acoplamiento al ventilador axial y foto comercial.
- `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-002.xlsx` — hoja de datos DTS-002 emitida (REV0 en metadatos, sin sufijo en nombre).

## Preguntas abiertas / bloqueos
- [ ] Decidir el destino de `Emisiones/2.0 HV-MEMORIAS DE CALCULO/P2437-HV-CAL-001.pdf`: exportación manual del 2026-07-27, obsoleta (contiene "(REV1)" y la geometría anterior a 35/50). Retirarlo o re-exportarlo desde Excel local. Ídem revisar los PDF manuales `P2437-HV-DTS-002.pdf` y `P2437-HV-LIS-001.pdf`.
- [ ] Confirmar modelo/RPM/potencia definitiva del ventilador mural Ø560 mm con el fabricante (Sodeca HQD/HGT mural anticorrosivo primera opción; Greenheck mural, Aerovent/Twin City mural FRP, NYB FRP mural alternativas). Punto: 3 840 m³/h @ 225 Pa catálogo. Plazo máx. ~3 meses (dato cliente, 2026-07-23).
- [ ] Definir dimensiones de la cubierta intemperie y de la estructura de unión con los planos del submittal del ventilador.
- [ ] Confirmar con Camfil/distribuidor local (ITECO, RGD Aire, Filter Tech) que el Durafil ES3 24×24×12 in soporta 2 260 CFM de forma continua, o mantener ES2 como referencia principal.
- [x] ~~Generar PDF de `P2437-HV-DTS-001.xlsx`~~ → Resuelto 2026-07-27: se generó PDF alternativo con `scripts/pdf_dts001.py` y se copió a `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.pdf`. Puede reemplazarse por exportación manual desde Excel cuando se disponga de Excel local.
- [ ] Verificar el caudal real en el ensayo de balanceo mediante anemometría en las tres rejillas de descarga.
- [x] ~~Confirmar si el laboratorio requiere HEPA~~ → Resuelto 2026-07-23: NO requiere (análisis industrial).
- [x] ~~Tensión/fases del motor~~ → 440 V, 3φ, 60 Hz (cliente, 2026-07-23).
- [x] ~~Plazos de entrega de equipos~~ → máximo ~3 meses (cliente, 2026-07-23).
- [x] ~~Push a GitHub~~ → Completado 2026-07-24, commit `2bc5b65`.
- [x] ~~Lectura de presión diferencial real tras ensayo de balanceo~~ → Ya no aplica (REV1: sistema sin presurización, sin instrumentación ΔP).

## Comandos / workflows útiles
- Regenerar Excel: `python generar_excel.py`
- Verificar formato de los 5 libros Excel generados (read-back, sin Excel): `python scripts/verificar_formato_excel.py`
- Cambios de formato de Excel: editar SOLO `scripts/estilos_excel.py` (paleta, `ANCHO_COLUMNAS`, `CHAR_POR_UNIDAD_ANCHO`, `ALTURA_LINEA`) y regenerar.
- Compilar informe DML (doble pasada para TOC/referencias; con bibtex si cambian citas): `cd Latex/02_informe_tex && pdflatex "P2437-HV-INF-001 REV0.tex"` (×2). Motor **pdflatex**, tipografía **NewTX**, `microtype`, `siunitx`. Si quedan restos de xelatex (`.toc` con `\xpg@aux`), borrar `.aux`/`.toc`/`.out` y recompilar.
- **Emitir entregables (recomendado):** `python scripts/emitir.py` — regenera Excel, DTS, LIS, recompila INF-001 e INF-002 y copia todo a `Emisiones/` con nombres GP-N-09 + manifiesto. Ejecutar al cierre de cualquier sesión que toque fuentes de entregables. Si falla con WinError 1224, hay un archivo de `Emisiones/` abierto: cerrarlo y reintentar.
- Despliegue GitHub Pages: Settings > Pages > Deploy from branch (`master` o `main`) > carpeta `/docs`.

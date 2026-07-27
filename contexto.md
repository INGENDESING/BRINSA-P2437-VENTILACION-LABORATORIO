# Contexto del proyecto: HVAC Laboratorio Brinsa

## Estado actual
- Última tarea completada (2026-07-27): priorización de DTS-002 — adaptación del sistema de filtración MERV 13-14 al ventilador axial DTS-001. Se actualizó `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md` con verificación hidráulica (v_facial = 2,87 m/s, ΔP inicial/final compatibles), lista de accesorios/periféricos (portafiltros, housing, transición cuadrado/circular, conexión flexible, clips, malla anti-insectos), análisis de incongruencias y foto comercial del filtro Camfil Durafil ES. Se actualizó el BOQ en `Investigacion/Sistemas/listado_equipos.md` (ítem 13: caja/housing de filtración y transición) y se regeneraron DTS-002 y LIS-001. La emisión parcial dejó `P2437-HV-DTS-003.xlsx` bloqueado por Excel; requiere reejecutar `scripts/emitir.py` tras cerrarlo.
- Tarea previa (2026-07-27): imagen de referencia de montaje del ventilador axial en muro/pasamuros a ~3,0 m de altura.
- Tarea previa (2026-07-27): excepción de nomenclatura para entregables sin ` REV1` en nombre de archivo.
- Tarea previa (2026-07-27): mejora de la curva ilustrativa del ventilador axial y regeneración de Excel/PDF de DTS-001.
- Tarea previa (2026-07-27): generación de PDF alternativo de `P2437-HV-DTS-001` con `scripts/pdf_dts001.py`.
- Tarea previa (2026-07-27): mejora de presentación de los documentos Excel generados y emisión REV1.
- Próxima tarea pendiente:
  - Confirmar disponibilidad comercial local del ventilador axial seleccionado (Aerovent FBD / alternativas Greenheck, Sodeca, NYB) y fijar tamaño/RPM/potencia definitiva con la curva de catálogo; obtener diámetro de boca para dimensionar la transición filtro-ventilador.
  - Confirmar con Camfil (o distribuidor local) que el Durafil ES3 24×24×12 soporta 2 260 CFM de forma continua, o mantener ES2 como referencia principal.
  - Verificar el caudal real en el ensayo de balanceo (anemometría en rejillas).
- Fecha de última actualización: 2026-07-27

## Bases de diseño congeladas (actualizadas 2026-07-27 — REV1)
- Sitio: BRINSA, Cajicá, Cundinamarca — 2 558 msnm, P_atm = 74.1 kPa, T 21/3/14 °C (máx/mín/media), HR media 84 %
- Ambiente exterior altamente corrosivo (planta de hipoclorito de calcio) → PRFV/inox 316/epóxicos
- Densidad del aire ρ: 0.88 kg/m³ (a 20 °C); coeficiente de descarga de orificio C_d: 0.60
- Volumen efectivo: 320 m³; renovación: 12 ACH (3 840 m³/h)
- **SIN presurización** del cuarto; descarga libre a atmósfera por 3 rejillas 353×336 mm
- Presión total del ventilador: 165 Pa en sitio (escenario MERV 13-14 cargado); punto de catálogo 3 840 m³/h @ 225 Pa (ρ = 1.2)
- Eficiencia axial provisional: 0.55; potencia teórica 0.320 kW (0.43 HP); motor provisional 0.75 HP TEFC anticorrosivo, 440 V, 3φ, 60 Hz (confirmar con catálogo)
- Velocidad inyección: 8.0 m/s; velocidad exfiltración: 3.0 m/s
- Filtración: MERV 13-14 definitivo — SIN HEPA (laboratorio de análisis industrial)

## Decisiones de diseño clave
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
- `scripts/emitir.py` — regenera Excel, DTS, LIS, recompila INF-001/002 y copia a `Emisiones/`.
- `scripts/pdf_dts001.py` — genera el PDF alternativo de `P2437-HV-DTS-001` desde el markdown fuente (reportlab).
- `Emisiones/4.0 HV-LISTADOS/P2437-HV-LIS-001.xlsx` — listado de equipos y materiales (BOQ).
- `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.pdf` — hoja de datos del ventilador axial en PDF (alternativo a Excel).
- `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md` — hoja de datos de filtración MERV 13-14 con acoplamiento al ventilador axial y foto comercial.
- `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-002.xlsx` — hoja de datos DTS-002 emitida (REV1 en metadatos, sin sufijo en nombre).

## Preguntas abiertas / bloqueos
- [ ] Confirmar disponibilidad comercial local del ventilador axial seleccionado (Aerovent FBD vía importación, Greenheck VAB/VAD vía Prime Lines, Sodeca HCT/HGT, NYB FRP). Fijar tamaño/RPM/potencia definitiva con curva de catálogo y obtener diámetro de boca para dimensionar la transición filtro-ventilador. Plazo máximo de entrega presupuestado: ~3 meses (dato cliente, 2026-07-23).
- [ ] Confirmar con Camfil/distribuidor local (ITECO, RGD Aire, Filter Tech) que el Durafil ES3 24×24×12 in soporta 2 260 CFM de forma continua, o mantener ES2 como referencia principal.
- [ ] Resolver bloqueo de `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-003.xlsx` (archivo abierto en Excel) y reejecutar `python scripts/emitir.py` para sincronizarlo.
- [x] ~~Generar PDF de `P2437-HV-DTS-001.xlsx`~~ → Resuelto 2026-07-27: se generó PDF alternativo con `scripts/pdf_dts001.py` y se copió a `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.pdf`. Puede reemplazarse por exportación manual desde Excel cuando se disponga de Excel local.
- [ ] Verificar el caudal real en el ensayo de balanceo mediante anemometría en las tres rejillas de descarga.
- [x] ~~Confirmar si el laboratorio requiere HEPA~~ → Resuelto 2026-07-23: NO requiere (análisis industrial).
- [x] ~~Tensión/fases del motor~~ → 440 V, 3φ, 60 Hz (cliente, 2026-07-23).
- [x] ~~Plazos de entrega de equipos~~ → máximo ~3 meses (cliente, 2026-07-23).
- [x] ~~Push a GitHub~~ → Completado 2026-07-24, commit `2bc5b65`.
- [x] ~~Lectura de presión diferencial real tras ensayo de balanceo~~ → Ya no aplica (REV1: sistema sin presurización, sin instrumentación ΔP).

## Comandos / workflows útiles
- Regenerar Excel: `python generar_excel.py`
- Compilar informe DML (doble pasada para TOC/referencias; con bibtex si cambian citas): `cd Latex/02_informe_tex && pdflatex "P2437-HV-INF-001 REV0.tex"` (×2). Motor **pdflatex**, tipografía **NewTX**, `microtype`, `siunitx`. Si quedan restos de xelatex (`.toc` con `\xpg@aux`), borrar `.aux`/`.toc`/`.out` y recompilar.
- **Emitir entregables (recomendado):** `python scripts/emitir.py` — regenera Excel, DTS, LIS, recompila INF-001 e INF-002 y copia todo a `Emisiones/` con nombres GP-N-09 + manifiesto. Ejecutar al cierre de cualquier sesión que toque fuentes de entregables.
- Despliegue GitHub Pages: Settings > Pages > Deploy from branch (`master` o `main`) > carpeta `/docs`.

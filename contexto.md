# Contexto del proyecto: HVAC Laboratorio Brinsa

## Estado actual
- Última tarea completada (2026-07-24):
  1. Mejora estética y de layout en las 4 hojas de datos DTS: `scripts/generar_dts.py` actualizado para que las tablas ocupen el ancho A:O (coincidente con el encabezado corporativo), separar notas numeradas en párrafos individuales y aplicar estilo cursivo/gris a las notas. Emisión OK con 8 entregables.
  2. Inserción de imagen de referencia y curva de operación en `P2437-HV-DTS-001`: se creó `scripts/generar_img_dts001.py` y se modificó `scripts/generar_dts.py` para añadir una sección "Referencia gráfica" al final de la hoja ESPECIFICACIÓN. La curva marca el punto de diseño (3 840 m³/h @ 260 Pa catálogo / 190 Pa en sitio). Emisión OK con 8 entregables.
  3. Corrección de referencias y Apéndice D de `P2437-HV-INF-001 REV0`: bibliografía actualizada con códigos GP-N-09 (`P2437-HV-INF-002`, `P2437-HV-LIS-001`, `P2437-HV-DTS-001…003`, `P2437-IC-DTS-001`, `P2437-HV-CAL-001`) y rutas de emisión en `Emisiones/`; Apéndice D actualizado con los mismos códigos y adición de la memoria de cálculo. Recompilación OK; emisión OK con 8 entregables.
  4. Actualización del informe técnico `P2437-HV-INF-001 REV0` con los resultados del modelo CFD (`pressure outlet` 0 Pa gauge en las rejillas): 4 figuras nuevas integradas en `Latex/02_informe_tex/figures/`, tabla de condiciones de contorno corregida, análisis gráfico figura por figura, y secciones de alcance, resumen, conclusiones y recomendaciones actualizadas. Recompilación OK; emisión OK con 8 entregables.
  5. Generación del listado de equipos en Excel corporativo
     (`P2437-HV-LIS-001 REV0.xlsx`) a partir de `listado_equipos.md`, usando la
     plantilla `FormatosDocumentos/LIS.xlsx` con exactamente 2 hojas (PORTADA + LISTA).
     Se creó `scripts/generar_lis.py` y se actualizó `scripts/emitir.py`; emisión OK
     con 8 entregables y retiro del `.md` obsoleto de `Emisiones/4.0 HV-LISTADOS/`.
  6. Creación de `vault/inicializacion.md` como protocolo de arranque para futuras
     sesiones, reforzando el vault de Obsidian como memoria permanente del proyecto.
- Tarea previa (2026-07-24): push del repositorio a GitHub (`origin/main`,
  commit `2bc5b65`, 138 archivos).
- Tarea previa (2026-07-23): estructura de emisión `Emisiones/`, informes
  **P2437-HV-INF-001/002**, memoria Excel corporativo, investigación de sistemas,
  vault de Obsidian y codificación GP-N-09.
- Próxima tarea pendiente:
  - El usuario generará manualmente el PDF de `P2437-HV-DTS-001 REV0.xlsx` (ambas
    hojas: PORTADA + ESPECIFICACIÓN) desde Excel para conservar la plantilla
    corporativa idéntica; comunicarlo para registrarlo en el vault y `Emisiones/`.
  - Confirmar disponibilidad comercial de los equipos seleccionados.
  - Confirmar la lectura de presión diferencial real tras el ensayo de balanceo.
- Fecha de última actualización: 2026-07-24

## Bases de diseño congeladas (actualizadas 2026-07-23 — sitio real)
- Sitio: BRINSA, Cajicá, Cundinamarca — 2 558 msnm, P_atm = 74.1 kPa, T 21/3/14 °C (máx/mín/media), HR media 84 %
- Ambiente exterior altamente corrosivo (planta de hipoclorito de calcio) → PRFV/inox 316/epóxicos
- Densidad del aire ρ: 0.88 kg/m³ (a 20 °C); coeficiente de descarga de orificio C_d: 0.60
- Volumen efectivo: 320 m³; renovación: 12 ACH (3 840 m³/h)
- Presión total del ventilador: 190 Pa en sitio (escenario MERV 13-14 cargado); punto de catálogo 3 840 m³/h @ 260 Pa (ρ = 1.2)
- Eficiencia ventilador: 0.60; potencia teórica 0.338 kW (0.45 HP); motor 1.0 HP TEFC anticorrosivo, 440 V, 3φ, 60 Hz (confirmado por el cliente 2026-07-23)
- Velocidad inyección: 8.0 m/s; velocidad exfiltración: 3.0 m/s
- Filtración: MERV 13-14 definitivo — SIN HEPA (laboratorio de análisis industrial)

## Decisiones de diseño clave
- Sistema sin ductos de impulsión: ventilador directo + exfiltración distribuida por 3 rejillas (353×336 mm) con malla anti-insectos inox.
- **Sitio Cajicá (2026-07-23):** recálculo con ρ = 0.88 kg/m³: ΔP rejillas 15→11 Pa; ΔP diseño 250→190 Pa; potencia 0.444→0.338 kW; config sin damper (4 m/s) solo sostiene 19.6 Pa → **damper de alivio pasa a componente obligatorio** del loop de control (+25 Pa, mínimo +12.5 Pa).
- **Sin HEPA (2026-07-23):** confirmado por el cliente; escenarios HEPA quedan como referencia histórica.
- **Selección preliminar de equipos (2026-07-23):** ventilador centrífugo PRFV viniléster (Greenheck BCSW-FRP primera opción); prefiltro MERV 8 + filtro V-bank MERV 13-14 marco plástico; rejillas eggcrate inox 316L + malla inox; Magnehelic 2000-00 + transmisor Dwyer MS-121. Detalle en `Investigacion/Sistemas/`.
- **CFD (2026-07-22):** salidas modeladas como pressure outlet (0 Pa gauge).
- Dashboard web estático (Vanilla HTML/CSS/JS) en `docs/` para GitHub Pages.

## Archivos clave y su propósito
- `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex` / `.pdf` — informe técnico DML (documento canónico; incluye la memoria descriptiva y las bases de diseño).
- `Latex/02_informe_tex/P2437-HV-INF-002 REV0.tex` / `.pdf` — informe de investigación del sistema (formato DML).
- `Codificacion/codificacion.md` — codificación GP-N-09 de los documentos del proyecto.
- `Emisiones/` — entregables codificados (copias generadas por `scripts/emitir.py`; no editar a mano).
- `generar_excel.py` — generador openpyxl de la memoria (fórmulas vivas).
- `memoriadecalculo.xlsx` — memoria de cálculo técnica con fórmulas vivas.
- `Latex/00_bases_diseno/bases_diseno.yaml` — fuente única de verdad (datos + escenarios + normas).
- `Investigacion/Sistemas/` — informe de investigación, listado de equipos y hojas de datos (HD-VENT/FILT/REJ/INST-001).
- `docs/index.html` — dashboard web interactivo.
- `vault/` — vault de Obsidian (memoria a largo plazo; ver skill `obsidian-vault`).
- `vault/inicializacion.md` — protocolo de arranque para recuperar contexto en nuevas sesiones.
- `scripts/generar_lis.py` — genera el listado de equipos BOQ en Excel corporativo.
- `scripts/emitir.py` — regenera Excel, DTS, LIS, recompila INF-001/002 y copia a `Emisiones/`.
- `Emisiones/4.0 HV-LISTADOS/P2437-HV-LIS-001 REV0.xlsx` — listado de equipos y materiales (BOQ).

## Preguntas abiertas / bloqueos
- [x] ~~Confirmar si el laboratorio requiere HEPA~~ → Resuelto 2026-07-23: NO requiere (análisis industrial).
- [ ] Confirmar disponibilidad comercial local de los equipos seleccionados (Greenheck vía Prime Lines, Dwyer, rejillas fabricación local). Plazo máximo de entrega presupuestado: ~3 meses (dato cliente, 2026-07-23).
- [ ] Confirmar la lectura de presión diferencial real tras el ensayo de balanceo.
- [ ] El usuario generará manualmente el PDF de `P2437-HV-DTS-001 REV0.xlsx` (ambas
  hojas) desde Excel y lo comunicará para registrarlo en el vault y `Emisiones/`.
- [x] ~~Conectar el origen remoto para GitHub y ejecutar el `push`~~ → Resuelto 2026-07-24: commit `2bc5b65`, 138 archivos, push a `origin/main` OK.

## Comandos / workflows útiles
- Regenerar Excel: `python generar_excel.py`
- Compilar informe DML (doble pasada para TOC/referencias; con bibtex si cambian citas): `cd Latex/02_informe_tex && pdflatex "P2437-HV-INF-001 REV0.tex"` (×2). Motor **pdflatex**, tipografía **NewTX**, `microtype`, `siunitx`. Si quedan restos de xelatex (`.toc` con `\xpg@aux`), borrar `.aux`/`.toc`/`.out` y recompilar.
- **Emitir entregables (recomendado):** `python scripts/emitir.py` — regenera Excel, DTS, LIS, recompila INF-001 e INF-002 y copia todo a `Emisiones/` con nombres GP-N-09 + manifiesto. Ejecutar al cierre de cualquier sesión que toque fuentes de entregables.
- Despliegue GitHub Pages: Settings > Pages > Deploy from branch (`master` o `main`) > carpeta `/docs`.

# Contexto del proyecto: HVAC Laboratorio Brinsa

## Estado actual
- Última tarea completada (2026-07-27): cambio de alcance del cliente — se eliminó la presurización del cuarto (+25 Pa, damper de alivio barométrico, instrumentación ΔP) y se cambió el ventilador de centrífugo a axial tubeaxial PRFV. Se actualizaron las fuentes (`Latex/00_bases_diseno/bases_diseno.yaml`, `generar_excel.py`, `Investigacion/Sistemas/`, `Latex/02_informe_tex/`, `docs/index.html`, `scripts/emitir.py`) y se emitieron 7 entregables como REV1: P2437-HV-INF-001/002, CAL-001, DTS-001/002/003 y LIS-001.
- Tarea previa (2026-07-24): mejora DTS, curva DTS-001, corrección INF-001, integración CFD, LIS Excel, vault; push a GitHub.
- Próxima tarea pendiente:
  - Confirmar disponibilidad comercial local del ventilador axial seleccionado (Aerovent FBD / alternativas Greenheck, Sodeca, NYB) y fijar tamaño/RPM/potencia definitiva con la curva de catálogo.
  - Generar manualmente el PDF de `P2437-HV-DTS-001 REV1.xlsx` (ambas hojas) desde Excel para conservar la plantilla corporativa idéntica; comunicarlo para registrarlo en el vault y `Emisiones/`.
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
- `Emisiones/4.0 HV-LISTADOS/P2437-HV-LIS-001 REV1.xlsx` — listado de equipos y materiales (BOQ).

## Preguntas abiertas / bloqueos
- [ ] Confirmar disponibilidad comercial local del ventilador axial seleccionado (Aerovent FBD vía importación, Greenheck VAB/VAD vía Prime Lines, Sodeca HCT/HGT, NYB FRP). Fijar tamaño/RPM/potencia definitiva con curva de catálogo. Plazo máximo de entrega presupuestado: ~3 meses (dato cliente, 2026-07-23).
- [ ] El usuario generará manualmente el PDF de `P2437-HV-DTS-001 REV1.xlsx` (ambas hojas: PORTADA + ESPECIFICACIÓN) desde Excel para mantener la plantilla corporativa idéntica. Una vez generado, comunicarlo para registrarlo en el vault y copiarlo a `Emisiones/3.0 HV-HOJAS DE DATOS/`.
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

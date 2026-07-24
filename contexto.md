# Contexto del proyecto: HVAC Laboratorio Brinsa

## Estado actual
- Última tarea completada (2026-07-23): Estructura de emisión `Emisiones/` (4 subcarpetas GP-N-09 + manifiesto) con script `scripts/emitir.py` que regenera Excel, recompila informes y copia entregables codificados; nuevo informe **P2437-HV-INF-002** (investigación del sistema, formato DML, 25 pp., 0 errores); bases de diseño completadas como sección de INF-001; codificación GP-N-09 de todos los documentos.
- Tarea previa: Investigación exhaustiva del sistema (`Investigacion/Sistemas/`) y **recálculo completo para el sitio real Cajicá, Cundinamarca** (2 558 msnm, ρ = 0.88 kg/m³). El documento `memoriadescriptiva.*` fue eliminado (2026-07-23): su contenido vive en el informe DML, que es el documento canónico.
- Tarea previa: Migración a `AGENTS.md` como único archivo director + vault de Obsidian en `vault/` con skill `obsidian-vault`.
- Próxima tarea pendiente: Ejecutar el modelo CFD con las nuevas BC (pressure outlet); confirmar disponibilidad comercial de los equipos seleccionados.
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

## Preguntas abiertas / bloqueos
- [x] ~~Confirmar si el laboratorio requiere HEPA~~ → Resuelto 2026-07-23: NO requiere (análisis industrial).
- [ ] Confirmar disponibilidad comercial local de los equipos seleccionados (Greenheck vía Prime Lines, Dwyer, rejillas fabricación local). Plazo máximo de entrega presupuestado: ~3 meses (dato cliente, 2026-07-23).
- [ ] Confirmar la lectura de presión diferencial real tras el ensayo de balanceo.
- [x] ~~Conectar el origen remoto para GitHub y ejecutar el `push`~~ → Resuelto 2026-07-24: commit `2bc5b65`, 138 archivos, push a `origin/main` OK.

## Comandos / workflows útiles
- Regenerar Excel: `python generar_excel.py`
- Compilar informe DML (doble pasada para TOC/referencias; con bibtex si cambian citas): `cd Latex/02_informe_tex && pdflatex "P2437-HV-INF-001 REV0.tex"` (×2). Motor **pdflatex**, tipografía **NewTX**, `microtype`, `siunitx`. Si quedan restos de xelatex (`.toc` con `\xpg@aux`), borrar `.aux`/`.toc`/`.out` y recompilar.
- **Emitir entregables (recomendado):** `python scripts/emitir.py` — regenera Excel, recompila INF-001 e INF-002 y copia todo a `Emisiones/` con nombres GP-N-09 + manifiesto. Ejecutar al cierre de cualquier sesión que toque fuentes de entregables.
- Despliegue GitHub Pages: Settings > Pages > Deploy from branch (`master` o `main`) > carpeta `/docs`.

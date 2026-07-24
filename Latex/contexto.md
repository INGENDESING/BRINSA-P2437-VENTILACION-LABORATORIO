# Contexto del proyecto: P2437-HV-INF-001 — Sistema de ventilación y presurización del laboratorio BRINSA

## Estado actual
- Última tarea completada: Recálculo con condiciones reales del sitio Cajicá, Cundinamarca (2026-07-23): ρ aire = 0.88 kg/m³ a 2 558 msnm; ΔP de diseño 250→190 Pa en sitio (equivalente catálogo 3 840 m³/h @ 260 Pa); rejillas sostienen 11 Pa; potencia 0.444→0.338 kW (0.45 HP); decisión HEPA cerrada (no requiere, laboratorio de análisis industrial); damper de alivio pasa a componente obligatorio del loop de control; criterio de materiales anticorrosivos (PRFV/inox 316/epóxicos, motor TEFC) por planta de hipoclorito de calcio. Memoria descriptiva (.tex/.md) e informe LaTeX actualizados y recompilados sin errores.
- Próxima tarea pendiente: Actualización del modelo CFD con las condiciones del sitio (ρ = 0.88 kg/m³) y verificación del campo de presión (11 Pa natural, 25 Pa con damper). Decisión sobre migración de la memoria Excel a la plantilla corporativa DML (`plantilla_dml.py`).
- Fecha de última actualización: 2026-07-23.

## Bases de diseño congeladas
- Sitio: BRINSA, Cajicá, Cundinamarca. Altitud 2 558 msnm; P_atm = 74.1 kPa; T máx/mín/media = 21/3/14 °C; HR media 84 %; ρ aire = 0.88 kg/m³.
- Volumen efectivo del laboratorio: 320 m³.
- Renovaciones de aire: 12 ACH (sustentado en ASHRAE 170, WHO BSL-2/BSL-3, NIH DRM).
- Estrategia: Ventilador de impulsión directa (sin ductos) + 3 rejillas de exfiltración + damper de alivio (obligatorio).
- Caudal de diseño: 64.0 m³/min = 3 840 m³/h = 2 260 CFM.
- Potencia teórica del ventilador en sitio: 0.338 kW (0.45 HP, η = 0.60, ΔP = 190 Pa); motor instalado: 1.0 HP TEFC anticorrosivo.
- Punto de selección de catálogo (ρ = 1.2 kg/m³): 3 840 m³/h @ 260 Pa.
- Área de impulsión: 0.1333 m² (diámetro 412 mm, radio 206.0 mm) a 8 m/s (presión dinámica 28 Pa).
- Rejillas de exfiltración: 3 unidades de 353.2 mm × 335.5 mm a 3.0 m/s (ΔP por orificio 11 Pa en sitio).
- Presión diferencial objetivo: +12.5 a +25 Pa.
- Filtración definitiva: MERV 13-14, sin HEPA (laboratorio de análisis industrial, no biocontención). Escenarios HEPA descartados (referencia histórica).
- Ambiente exterior altamente corrosivo (planta de hipoclorito de calcio): materiales PRFV/inox 316/recubrimientos epóxicos.
- Normas: ASHRAE 170-2021, ASHRAE 62.1-2022, NFPA 99-2021, OSHA 29 CFR 1910.1450, WHO Laboratory Biosafety Manual 2004, NIH DRM 2023.

## Decisiones de diseño clave
- **Opción A seleccionada (2026-07-15):** ventilador de impulsión directa sin ductos y rejillas de exfiltración controladas, por requerimiento explícito del cliente.
- **12 ACH (2026-07-15):** valor dentro del rango BSL-2 superior y umbral BSL-3, con margen de seguridad respecto al mínimo general de 6 ACH.
- **Velocidad de exfiltración 3.0 m/s (2026-07-15):** compromiso entre mantenimiento de presión positiva y control de ruido.
- **Compilación con pdflatex (2026-07-15):** se respetó la configuración corporativa de la plantilla DML (`tgtermes`, `inputenc[T1]`).
- **Volumen 320 m³ y 3 rejillas (2026-07-16):** actualización de bases de diseño por cambio de alcance; recálculo de caudal (64.0 m³/min), potencia (0.444 kW), boca de impulsión (radio 206.0 mm) y rejillas (353.2 mm × 335.5 mm).
- **Cierre presión–caudal (2026-07-22):** las rejillas a 3 m/s sostienen ~15 Pa por la ecuación de orificio (ρ=1.2, C_d=0.60); el set-point de +25 Pa se garantiza con damper de alivio calibrable + sensor de presión diferencial (loop de control). Alternativa sin damper: 4 m/s / 300×295 mm (cierra en ~26.6 Pa).
- **Filtración y motor (2026-07-22):** escenario de diseño = MERV 13-14 cargado (ΔP vent 250 Pa, motor 1.0 HP). Si se confirma HEPA H13, motor pasa a 2.0 HP y ΔP vent total a ~640 Pa.
- **BC CFD (2026-07-22):** salidas como pressure outlet (0 Pa gauge) en lugar de velocity outlet, para no sobreespecificar el problema.
- **Recálculo sitio Cajicá (2026-07-23):** condiciones reales del sitio (2 558 msnm, ρ = 0.88 kg/m³) reemplazan los valores supuestos de Valle del Cauca (960 msnm, ρ = 1.2 kg/m³). Consecuencias: ΔP rejillas 15→11 Pa; ΔP diseño MERV cargado 250→190 Pa en sitio (260 Pa equivalente catálogo); potencia 0.444→0.338 kW (0.45 HP); config 4 m/s solo sostiene 19.6 Pa (antes 26.6 Pa).
- **HEPA descartado (2026-07-23):** laboratorio de análisis industrial, no biocontención; filtración definitiva MERV 13-14. Se mantiene motor 1.0 HP.
- **Damper de alivio obligatorio (2026-07-23):** a ρ = 0.88 kg/m³ las rejillas a 3 m/s sostienen solo 11 Pa (< 12.5 Pa mínimo); sin damper harían falta rejillas de 0.079 m² (~280×281 mm) a 4.5 m/s. El damper + sensor ΔP es componente obligatorio del loop de control.
- **Materiales anticorrosivos (2026-07-23):** ambiente exterior altamente corrosivo (hipoclorito de calcio); equipos expuestos en PRFV/inox 316/epóxicos y motor TEFC anticorrosivo.

## Archivos clave y su propósito
- `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex` — informe técnico maestro LaTeX (documento canónico; el antiguo `Calculos/memoriadescriptiva.*` se eliminó el 2026-07-23 por redundancia).
- `Latex/02_informe_tex/P2437-HV-INF-001 REV0.pdf` — informe final en PDF (20 páginas).
- `Latex/02_informe_tex/config/datos_proyecto.tex` — metadatos centralizados (código, cliente, firmas, fechas).
- `Latex/00_bases_diseno/bases_diseno.yaml` — fuente única de verdad con datos del proyecto HVAC.
- `Latex/02_informe_tex/sections/*.tex` — secciones modulares del informe.
- `Latex/02_informe_tex/references/bibliografia.bib` — referencias bibliográficas.
- `Calculos/memoriadecalculo.xlsx` — memoria de cálculo Excel funcional con fórmulas vivas.
- `Calculos/generar_excel.py` — script generador de la memoria Excel.

## Preguntas abiertas / bloqueos
- [ ] ¿Migrar la memoria de cálculo Excel existente a la plantilla corporativa DML (`plantilla_dml.py`)?
- [ ] ¿Requiere el cliente ejecutar el modelo CFD o solo las condiciones de contorno entregadas?
- [ ] ¿Se dispone de los planos del laboratorio para ubicar ventilador y rejillas en la etapa de ingeniería de detalle?

## Comandos / workflows útiles
- `cd Latex/02_informe_tex && pdflatex "P2437-HV-INF-001 REV0.tex"` — compilar informe.
- `cd Latex/02_informe_tex && pdflatex "P2437-HV-INF-001 REV0.tex" && pdflatex "P2437-HV-INF-001 REV0.tex"` — compilar informe resolviendo referencias cruzadas.
- `python Calculos/generar_excel.py` — regenerar memoria de cálculo Excel.

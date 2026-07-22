# Contexto del proyecto: P2437-HV-INF-001 — Sistema de ventilación y presurización del laboratorio BRINSA

## Estado actual
- Última tarea completada: Actualización de bases de diseño — volumen 320 m³ (antes 274 m³) y 3 rejillas de exfiltración (antes 2); recálculo integral y actualización de informe LaTeX, memoria descriptiva, memoria Excel y bases YAML (2026-07-16).
- Próxima tarea pendiente: Actualización del modelo CFD con las nuevas condiciones de contorno (en curso por parte del cliente) y decisión sobre migración de la memoria Excel a la plantilla corporativa DML (`plantilla_dml.py`).
- Fecha de última actualización: 2026-07-16.

## Bases de diseño congeladas
- Volumen efectivo del laboratorio: 320 m³.
- Renovaciones de aire: 12 ACH (sustentado en ASHRAE 170, WHO BSL-2/BSL-3, NIH DRM).
- Estrategia: Ventilador de impulsión directa (sin ductos) + 3 rejillas de exfiltración.
- Caudal de diseño: 64.0 m³/min = 3 840 m³/h = 2 260 CFM.
- Potencia teórica del ventilador: 0.444 kW; motor instalado recomendado: 1.0 HP.
- Área de impulsión: 0.1333 m² (diámetro 412 mm, radio 206.0 mm) a 8 m/s.
- Rejillas de exfiltración: 3 unidades de 353.2 mm × 335.5 mm a 3.0 m/s.
- Presión diferencial objetivo: +12.5 a +25 Pa.
- Filtración mínima: MERV 13-14; HEPA H13/H14 según riesgo biológico.
- Normas: ASHRAE 170-2021, ASHRAE 62.1-2022, NFPA 99-2021, OSHA 29 CFR 1910.1450, WHO Laboratory Biosafety Manual 2004, NIH DRM 2023.

## Decisiones de diseño clave
- **Opción A seleccionada (2026-07-15):** ventilador de impulsión directa sin ductos y rejillas de exfiltración controladas, por requerimiento explícito del cliente.
- **12 ACH (2026-07-15):** valor dentro del rango BSL-2 superior y umbral BSL-3, con margen de seguridad respecto al mínimo general de 6 ACH.
- **Velocidad de exfiltración 3.0 m/s (2026-07-15):** compromiso entre mantenimiento de presión positiva y control de ruido.
- **Compilación con pdflatex (2026-07-15):** se respetó la configuración corporativa de la plantilla DML (`tgtermes`, `inputenc[T1]`).
- **Volumen 320 m³ y 3 rejillas (2026-07-16):** actualización de bases de diseño por cambio de alcance; recálculo de caudal (64.0 m³/min), potencia (0.444 kW), boca de impulsión (radio 206.0 mm) y rejillas (353.2 mm × 335.5 mm).

## Archivos clave y su propósito
- `Plantilla/02_informe_tex/P2437-HV-INF-001 REV0.tex` — informe técnico maestro LaTeX.
- `Plantilla/02_informe_tex/P2437-HV-INF-001 REV0.pdf` — informe final en PDF (18 páginas).
- `Plantilla/02_informe_tex/config/datos_proyecto.tex` — metadatos centralizados (código, cliente, firmas, fechas).
- `Plantilla/00_bases_diseno/bases_diseno.yaml` — fuente única de verdad con datos del proyecto HVAC.
- `Plantilla/02_informe_tex/sections/*.tex` — secciones modulares del informe.
- `Plantilla/02_informe_tex/references/bibliografia.bib` — referencias bibliográficas.
- `Calculos/memoriadescriptiva.md` — memoria descriptiva actualizada (Opción A).
- `Calculos/memoriadecalculo.xlsx` — memoria de cálculo Excel funcional con fórmulas vivas.
- `Calculos/generar_excel.py` — script generador de la memoria Excel.

## Preguntas abiertas / bloqueos
- [ ] ¿Migrar la memoria de cálculo Excel existente a la plantilla corporativa DML (`plantilla_dml.py`)?
- [ ] ¿Requiere el cliente ejecutar el modelo CFD o solo las condiciones de contorno entregadas?
- [ ] ¿Se dispone de los planos del laboratorio para ubicar ventilador y rejillas en la etapa de ingeniería de detalle?

## Comandos / workflows útiles
- `cd Plantilla/02_informe_tex && pdflatex "P2437-HV-INF-001 REV0.tex"` — compilar informe.
- `cd Plantilla/02_informe_tex && pdflatex "P2437-HV-INF-001 REV0.tex" && pdflatex "P2437-HV-INF-001 REV0.tex"` — compilar informe resolviendo referencias cruzadas.
- `python Calculos/generar_excel.py` — regenerar memoria de cálculo Excel.

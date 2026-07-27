---
fecha: 2026-07-27
tags: [decision, axial, presurizacion, rev1]
estado: congelado
---

# Decisión 2026-07-27: sin presurización y ventilador axial

## Contexto
El cliente (BRINSA) decidió el 2026-07-27 que **no se presurizará el cuarto** del laboratorio y que el sistema utilizará un **ventilador axial** en lugar del centrífugo previamente estudiado. Se mantienen: caudal 3 840 m³/h (12 ACH), filtración MERV 8 + MERV 13-14, 3 rejillas de descarga 353×336 mm, estrategia sin ductos de impulsión y sitio Cajicá (ρ = 0.88 kg/m³).

## Decisión
1. Eliminar por completo: presurización +25 Pa, damper de alivio barométrico, transmisor de presión diferencial Dwyer MS-121, Magnehelic 2000-00, controlador/alarmas de ΔP y toma de referencia exterior.
2. Cambiar el ventilador de centrífugo (Greenheck BCSW-FRP) a **axial tubeaxial PRFV con transmisión por bandas** (Aerovent FBD como primera opción de referencia; alternativas Greenheck VAB/VAD, Sodeca HCT/HGT, New York Blower FRP).
3. Recalcular el punto de trabajo sin el offset de 25 Pa: 165 Pa en sitio (154 Pa filtro cargado + 11 Pa pérdida de descarga en rejillas), equivalente a 225 Pa en catálogo (ρ = 1.2).
4. Motor provisional 0.75 HP TEFC anticorrosivo, 440 V, 3φ, 60 Hz, con margen de servicio 1.5; potencia definitiva a confirmar con la curva del axial seleccionado.

## Justificación técnica
- Sin presurización, el damper de alivio y la instrumentación ΔP no tienen función.
- El punto de catálogo baja de 260 Pa a 225 Pa, rango plenamente cubierto por axiales tubulares en PRFV (hasta ~370 Pa en catálogos consultados). En el estudio REV0 los axiales se descartaron con 260 Pa + presurización; el nuevo alcance los hace viables.
- La transmisión por bandas mantiene el motor fuera de la corriente corrosiva y permite ajustar RPM en balanceo.
- La eficiencia axial provisional (0.55) es conservadora frente a 0.60 del centrífugo; la potencia teórica apenas cambia (0.320 kW vs. 0.338 kW anterior).

## Alternativas descartadas
- Mantener centrífugo: técnicamente válido pero contraria a la decisión expresa del cliente.
- Mantener presurización con axial: no solicitado; el axial a 225 Pa no tiene margen para sostener +25 Pa adicionales de forma robusta.
- Presurización sin damper: la configuración sin damper solo sostenía ~11 Pa en REV0; insuficiente para +25 Pa.

## Referencias
- `Latex/00_bases_diseno/bases_diseno.yaml` — punto de trabajo 165/225 Pa, η = 0.55, motor 0.75 HP provisional.
- `Investigacion/Sistemas/informe_investigacion.md` — comparativa de axiales candidatos y selección recomendada.
- `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex` / `P2437-HV-INF-002 REV0.tex` — informes REV1 con el nuevo alcance.

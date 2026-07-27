---
fecha: 2026-07-27
estado: vigente
tags: [decision, ventilador, axial, curva, dts001]
---

# Decisión: Curva ilustrativa del ventilador axial tubeaxial PRFV

## Decisión

Se mejoró la curva característica ilustrativa de `P2437-HV-DTS-001` para reflejar los datos investigados del proyecto: punto de diseño 3 840 m³/h @ 225 Pa catálogo / 165 Pa sitio, factor de densidad k = 0,733, eficiencia axial provisional η = 0,55 y forma parabólica típica de ventiladores axiales tubeaxial.

## Motivo

- La curva anterior era una parábola genérica que pasaba por el punto de diseño pero no mostraba explícitamente la corrección por densidad ni la potencia de eje.
- Los documentos investigados (`informe_investigacion.md`, `HD-VENT-001_ventilador.md`) establecen el punto de trabajo, el factor de densidad y la eficiencia provisional; la curva debe visualizarlos de forma coherente.
- La hoja de datos DTS-001 requiere una curva característica ilustrativa hasta que se disponga de la curva real del fabricante seleccionado.

## Alternativas consideradas

- **Mantener curva parabólica simple:** descartado porque no comunicaba la corrección por densidad ni la potencia de eje.
- **Esperar curva de catálogo real:** descartado porque dejaba el entregable REV1 incompleto; la curva ilustrativa provisional es aceptable mientras se confirma el fabricante.
- **Incluir curva de eficiencia:** descartado porque η = 0,55 es un valor provisional constante; no aportaría información adicional hasta tener datos reales.

## Referencias

- `scripts/generar_img_dts001.py`
- `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md` §3
- `Investigacion/Sistemas/informe_investigacion.md` §3.2
- Twin City Fan, *Fan Engineering FE-1600 — Temperature & Altitude Effects on Fans*: http://eu.tcf.com/wp-content/uploads/sites/4/2018/06/Temperature-Altitude-Effects-on-Fans-FE-1600-1.pdf

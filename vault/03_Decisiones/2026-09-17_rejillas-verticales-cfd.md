---
fecha: 2026-09-17
estado: vigente
tags: [decision]
---

# Decisión: rejillas de exfiltración apiladas verticalmente (disposición BRINSA) validada por CFD

## Decisión

Las tres rejillas de exfiltración de 353×336 mm se instalan apiladas
verticalmente, una sobre otra, en la pared opuesta a la inyección del
ventilador. La disposición fue definida por BRINSA y validada con una nueva
corrida del modelo CFD (Autodesk CFD, "Case 1", 2026-09-17).

## Motivo

Requisito explícito del cliente (BRINSA) sobre la ubicación de las rejillas.
El resto del diseño no cambia: caudal 3 840 m³/h, rejillas 353×336 mm a
3 m/s, ΔP de descarga 11 Pa, punto de trabajo 165 Pa en sitio.

## Resultado de la validación CFD

El chorro de inyección (8 m/s) queda alineado a altura media con la rejilla
central; las celdas de recirculación superior e inferior distribuyen el caudal
hacia las rejillas de los extremos; las tres rejillas descargan con velocidades
faciales del orden de 3 m/s y no se observan retornos hacia la inyección ni
zonas de estancamiento severo. Figuras: `Latex/02_informe_tex/figures/cfd_*.png`
(8 figuras, 4 variables × 2 vistas).

## Alternativas consideradas

- Rejillas distribuidas en paredes opuestas o perpendiculares a la impulsión
  (configuración anterior del informe): descartada por instrucción del cliente.

## Referencias

- `Latex/02_informe_tex/sections/09_resultados.tex` (subsección CFD, Figuras
  de resultados) y `sections/10_analisis.tex`.
- `Latex/00_bases_diseno/bases_diseno.yaml` (`rejillas_exfiltracion.ubicacion`).
- `Investigacion/Sistemas/hojas_datos/HD-REJ-001_rejillas.md` §1.2.

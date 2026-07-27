---
fecha: 2026-07-27
estado: vigente
tags: [decision, ventilador, montaje, muro, dts001]
---

# Decisión: Montaje del ventilador axial en muro/pasamuros a ~3,0 m

## Decisión

El ventilador axial tubeaxial PRFV (VENT-001) se instalará en **muro/pasamuros**, con el eje horizontal y a una cota aproximada de **3,0 m sobre el piso terminado** del laboratorio. El sentido de flujo es aspiración de aire exterior filtrado y descarga directa al interior del recinto.

## Motivo

- El cliente indicó que el ventilador debe ir en la pared a 3 m del suelo.
- Un axial tubeaxial está diseñado para montaje en ducto o muro/pasamuros, no para quedar expuesto como ventilador de pared libre. El montaje en muro/pasamuros es el único técnicamente coherente con este tipo de máquina.
- La transmisión por bandas permite ubicar el motor fuera de la corriente de aire corrosivo, cumpliendo el requisito de materiales para ambiente clorado.

## Alternativas consideradas

- **Ventilador centrífugo de pared:** descartado en REV1 por decisión del cliente de usar axial.
- **Axial colgado libremente sobre la pared interior:** descartado porque generaría cortocircuito de aire, pérdidas de descarga no calculadas y carga estructural no prevista.
- **Montaje a menor altura:** descartado porque el cliente fijó la cota de 3,0 m.

## Referencias

- `scripts/generar_img_dts001.py`
- `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md` §8
- `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.pdf`

---
fecha: 2026-07-27
estado: vigente
tags: [decision, filtracion, ventilador]
---

# Decisión: Acoplamiento del filtro MERV 13-14 al ventilador axial DTS-001

## Decisión

El filtro final MERV 13-14 se mantiene como **V-bank 24×24×12 in (610×610×298 mm)**
con referencia principal **Camfil Durafil ES2** (o equivalente ES3), montado
**aguas arriba del ventilador axial tubeaxial**. La configuración de flujo es:
toma exterior → malla anti-insectos → prefiltro MERV 8 → filtro final →
transición cuadrado/circular → conexión flexible → ventilador axial → descarga
al recinto. Se agregó al BOQ un **ítem 13 (caja/housing de filtración y
transición)** para materializar el acoplamiento.

## Motivo

- El punto de trabajo del ventilador (3 840 m³/h a 165 Pa en el sitio) ya incluye
  la ΔP del filtro cargado (154 Pa) y las rejillas (11 Pa). La velocidad facial
  en el filtro 24×24 in resulta 2,87 m/s (565 fpm), dentro del límite 625 fpm del
  Durafil ES3 y muy por debajo del caudal nominal del ES2.
- El ventilador axial tiene boca circular; el filtro V-bank es cuadrado. Se
  requiere una caja de filtración con transición cuadrado/circular y longitud
  mínima ~1,5 D para recuperar el perfil de velocidad sin agregar pérdidas no
  contabilizadas.
- El sentido de aspiración del ventilador axial mantiene el filtro asentado
  contra el portafiltros, reduciendo bypass. Todos los materiales siguen el
  criterio anticorrosivo del proyecto (inox 316L o PRFV viniléster).

## Alternativas consideradas

- **Filtro de bolsa o cartucho:** descartado porque eleva la velocidad facial o
  requiere mayor profundidad; el V-bank 24×24 es el formato estándar que ya se
  había especificado y que ofrece baja ΔP y alta capacidad de polvo.
- **Colocar el filtro aguas abajo del ventilador (descarga):** descartado porque
  expone el filtro al aire impulsado a mayor velocidad y temperatura, y porque
  el empuje positivo tende a desasentar el filtro del portafiltros, aumentando
  bypass.
- **Cambiar a filtro 20×24 in o múltiples celdas:** descartado por ahora porque
  mantiene la especificación congelada 24×24 in y permite segunda fuente; solo
  se reconsideraría si el diámetro de boca del ventilador exigiera mayor área
  facial.

## Referencias

- `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md` §7.
- `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md` §3 y §8.
- `Investigacion/Sistemas/listado_equipos.md` ítem 13.
- [Camfil — Product Sheet Durafil ES3 (PDF)](https://www.camfil.com/dam/files/290/1590002/Product-Sheet-Durafil-ES3-ENG-US.pdf)
- [Camfil — Drawing Durafil ES3 (PDF)](https://www.camfil.com/dam/files/1165/1676816/Drawing-Durafil-ES3.pdf)
- [Capris — Durafil ES2 855080-009 24×24×12 MERV-14/14A](https://www.capris.cr/es/camfil-855080009-filtro-tipo-v-4v-con-cejilla-merv-14-14a-24u0022x24u0022x12u0022-durafil-es2-k50086.html)

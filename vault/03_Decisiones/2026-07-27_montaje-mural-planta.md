---
fecha: 2026-07-27
estado: vigente
tags: [decision, ventilador, montaje]
---

# Decisión: Ventilador axial mural Ø560 mm por uniformidad con el montaje típico de planta (REV2)

## Decisión

Se adopta la configuración del montaje típico instalado en la planta
(`Montaje/DISENOFINAL.png` y `Montaje/Descripcion_Tecnica_Sistema_Ventilacion_Inyeccion_2260CFM_v2.md`)
como configuración de diseño del sistema P2437:

- Ventilador **axial mural (placa mural) Ø560 mm, transmisión directa**, inyección exterior → interior.
- Banco de filtración **MERV 8 + MERV 13-14 alojado dentro de la cubierta intemperie** (módulo 24×24 in).
- **Estructura de unión** (perfiles ASTM A36 galvanizados + pintura epóxica) pernada al muro con anclajes inox 316 (A4).
- **Malla de protección interior** desmontable en la descarga.
- Cota de montaje ~3,0 m sobre piso terminado (sin cambio).

Se eliminan de la configuración REV1: transición cuadrado/circular, caja/housing de filtración,
conexión flexible de hipalón y persiana de gravedad.

## Motivo

- Uniformidad con los equipos ya instalados en la planta (criterio del cliente): misma secuencia
  de montaje, mismos accesorios y misma logística de mantenimiento y repuestos.
- El punto de trabajo no cambia: 3 840 m³/h @ 165 Pa sitio (225 Pa catálogo), cubierto por un
  mural Ø560 mm; velocidad real en boca 4,33 m/s.
- La filtración se mantiene (MERV 8 + MERV 13-14, marco plástico, ΔP 80/210 Pa catálogo); solo
  cambia su alojamiento (cubierta intemperie en vez de caja/housing separada).

## Riesgo asumido y mitigación

La transmisión directa ubica el **motor dentro de la corriente de aire corrosivo**. Mitigación:
motor encapsulado TEFC severe duty, clase F (H preferible), IP56 mínimo (IP66 preferible), pintura
epóxica, eje inox, calentador anticondensación, inspección semestral. La alternativa de transmisión
por bandas (motor fuera de la corriente) queda documentada como opción si la vida del motor en
servicio resulta insuficiente.

## Alternativas consideradas

- **Tubeaxial PRFV con transmisión por bandas (REV1):** protege mejor el motor pero rompe la
  uniformidad con la planta y exige transición cuadrado/circular y caja de filtración separada.
  Descartada por criterio de uniformidad del cliente; queda documentada como opción de respaldo.
- **Copiar también los materiales de planta (galvanizado + pintura electrostática):** descartado;
  se eleva la especificación a PRFV/inox 316 por la atmósfera clorada del sitio (decisión ya
  congelada en bases de diseño).

## Referencias

- `Montaje/DISENOFINAL.png`; `Montaje/Descripcion_Tecnica_Sistema_Ventilacion_Inyeccion_2260CFM_v2.md`.
- `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md` (REV2).
- `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md` (REV2) §7.
- `Investigacion/Sistemas/listado_equipos.md` (REV2).
- `Latex/00_bases_diseno/bases_diseno.yaml` (revisión 2).

---
fecha: 2026-07-23
estado: vigente
tags: [decision, sitio, recalculo]
---

# Decisión: recálculo del sistema para el sitio real Cajicá

## Decisión

Las bases de diseño se recalcularon para el sitio real: **Cajicá, Cundinamarca
(2 558 msnm, P_atm = 74.1 kPa, ρ = 0.88 kg/m³)**, reemplazando los valores supuestos
de Valle del Cauca (960 msnm, ρ = 1.2 kg/m³).

## Motivo

El cliente confirmó la ubicación real de la planta BRINSA. La densidad del aire a
2 558 msnm es 27 % menor que la estándar, lo que afecta presiones y potencias.

## Consecuencias del recálculo

| Magnitud | Antes (ρ = 1.2) | Ahora (ρ = 0.88) |
| --- | --- | --- |
| ΔP rejillas (orificio, 3 m/s) | 15 Pa | 11 Pa |
| ΔP total diseño (MERV cargado) | 250 Pa | 190 Pa en sitio (260 Pa catálogo) |
| Potencia teórica | 0.444 kW | 0.338 kW (0.45 HP) |
| Config sin damper 4 m/s | 26.6 Pa | 19.6 Pa (ya no alcanza 25 Pa) |
| Motor instalado | 1.0 HP | 1.0 HP TEFC anticorrosivo (sin cambio) |

Consecuencia clave: el **damper de alivio pasa de alternativa a componente
obligatorio** del loop de control de presurización (+25 Pa).

## Referencias

- Investigación climática: [[informe_investigacion]] §3
  (fuentes: DB-City, ASHRAE 2009 El Dorado, Weather Atlas, METAR SKBO).
- Actualizados: `bases_diseno.yaml`, `memoriadecalculo.xlsx`, `memoriadescriptiva`,
  `Latex/02_informe_tex`, `docs/index.html`.

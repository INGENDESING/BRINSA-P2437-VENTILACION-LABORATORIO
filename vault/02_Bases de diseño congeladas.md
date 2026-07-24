---
fecha: 2026-07-23
tags: [bases-de-diseno]
---
uNA CORRECCION
# Bases de diseño congeladas

Estos valores NO se revisan sin aprobación explícita. Fuente única de verdad:
`Latex/00_bases_diseno/bases_diseno.yaml`.

**Actualizadas el 2026-07-23 al sitio real (Cajicá, Cundinamarca)** — ver
[[2026-07-23_recalculo-sitio-cajica]].

| Parámetro | Valor | Fuente |
| --- | --- | --- |
| Sitio | BRINSA, Cajicá, Cundinamarca | Cliente |
| Altitud | 2 558 msnm | DB-City, validado vs. SKGY |
| Presión atmosférica | 74.1 kPa | ISA, validado vs. METAR SKBO |
| Temperatura diseño (máx/mín/media) | 21 / 3 / 14 °C | ASHRAE 2009 El Dorado; Alcaldía |
| Humedad relativa media | 84 % | Weather Atlas Cajicá |
| Densidad del aire ρ | 0.88 kg/m³ (20 °C) | Gas ideal + ISA |
| Volumen efectivo | 320 m³ | — |
| Tasa de renovación | 12 ACH (3 840 m³/h) | ASHRAE 170 (referencia) |
| Presión total del ventilador | 190 Pa en sitio (260 Pa catálogo) | Escenario MERV 13-14 cargado |
| Eficiencia del ventilador | 0.60 | — |
| Potencia teórica / motor | 0.338 kW (0.45 HP) / 1.0 HP TEFC, 440 V 3φ 60 Hz | Recálculo 2026-07-23; tensión confirmada por el cliente |
| Velocidad de inyección | 8.0 m/s | — |
| Velocidad de exfiltración | 3.0 m/s | — |
| Coeficiente de descarga C_d | 0.60 | ASHRAE Handbook Fundamentals |
| Filtración | MERV 13-14 — SIN HEPA | Laboratorio de análisis industrial |
| Ambiente exterior | Altamente corrosivo (hipoclorito de calcio) | Cliente → PRFV/inox 316 |

Configuración base: sistema sin ductos de impulsión — ventilador directo + exfiltración
distribuida por 3 rejillas de 353×336 mm con malla anti-insectos; presurización +25 Pa
garantizada con damper de alivio (obligatorio) + sensor de presión diferencial.

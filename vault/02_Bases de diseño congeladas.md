---
fecha: 2026-07-27
tags: [bases-de-diseno]
---

# Bases de diseño congeladas

Estos valores NO se revisan sin aprobación explícita. Fuente única de verdad:
`Latex/00_bases_diseno/bases_diseno.yaml`.

**Revisión documental vigente: CERO (0) en todos los entregables** (decisión
2026-07-28; ver [[2026-07-28_rev0-unica-revision-cero]]). Configuración técnica
actualizada el 2026-07-27 por cambio de alcance del cliente: sin presurización,
ventilador axial mural. Ver [[2026-07-27_sin-presurizacion-ventilador-axial]] y
[[2026-07-27_montaje-mural-planta]].

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
| Presión total del ventilador | 165 Pa en sitio (225 Pa catálogo) | Escenario MERV 13-14 cargado, sin presurización |
| Eficiencia del ventilador | 0.55 (provisional) | Axial típico; confirmar con catálogo |
| Potencia teórica / motor | 0.320 kW (0.43 HP) / 0.75 HP TEFC, 440 V 3φ 60 Hz | Recálculo 2026-07-27; tensión confirmada por el cliente |
| Velocidad de inyección | 8.0 m/s | — |
| Velocidad de exfiltración | 3.0 m/s | — |
| Coeficiente de descarga C_d | 0.60 | ASHRAE Handbook Fundamentals |
| Filtración | MERV 13-14 — SIN HEPA | Laboratorio de análisis industrial |
| Ambiente exterior | Altamente corrosivo (hipoclorito de calcio) | Cliente → PRFV/inox 316 |
| Presurización | SIN presurización; descarga libre a atmósfera | Decisión cliente 2026-07-27 |
| Instrumentación ΔP | NINGUNA (eliminada) | Decisión cliente 2026-07-27 |
| Damper de alivio | NINGUNO (eliminado) | Decisión cliente 2026-07-27 |

Configuración base: sistema sin ductos de impulsión — ventilador axial mural (placa mural) Ø560 mm de transmisión directa, con banco de filtración en cubierta intemperie, estructura de unión pernada al muro y malla de protección interior (uniformidad con montaje típico de planta, REV2) + descarga libre por 3 rejillas de 353×336 mm con malla anti-insectos.

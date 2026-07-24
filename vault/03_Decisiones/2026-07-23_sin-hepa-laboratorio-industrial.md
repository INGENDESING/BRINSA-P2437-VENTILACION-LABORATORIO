---
fecha: 2026-07-23
estado: vigente
tags: [decision, filtracion]
---

# Decisión: laboratorio sin HEPA — filtración MERV 13-14 definitiva

## Decisión

El laboratorio **NO requiere filtros HEPA**: es un laboratorio de análisis industrial,
no de biocontención. El escenario de diseño queda definitivamente en **MERV 13-14
cargado** (ΔP filtro 154 Pa en sitio, motor 1.0 HP).

## Motivo

Confirmación del cliente (2026-07-23). Cierra la pregunta abierta del 2026-07-22.

## Consecuencias

- Los escenarios HEPA de `bases_diseno.yaml` quedan como referencia histórica
  ("descartado — no aplica").
- La filtración se especifica en dos etapas: prefiltro MERV 8 + filtro final
  V-bank MERV 13-14 con marco plástico (compatibilidad con ambiente corrosivo).
- Objetivo del sistema: presión positiva y exclusión de insectos, objetos extraños
  y polvo ambiental.

## Referencias

- [[2026-07-22_escenarios-filtracion-merv-hepa]] (antecedente).
- [[HD-FILT-001_filtro_merv]].
- [[listado_equipos]] (BOQ completo del sistema).

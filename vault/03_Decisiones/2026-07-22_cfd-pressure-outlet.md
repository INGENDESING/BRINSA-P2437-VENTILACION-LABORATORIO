---
fecha: 2026-07-22
estado: vigente
tags: [decision, cfd]
---

# Decisión: salidas CFD como pressure outlet

## Decisión

Las salidas del modelo CFD se modelan como **pressure outlet (0 Pa gauge)**.

## Motivo

Antes eran velocity outlet, lo que sobreespecificaba el problema (imponer caudal y
presión a la vez). Con pressure outlet el caudal de exfiltración lo determina la
solución, coherente con el cierre presión–caudal por orificio.

## Pendiente

- Ejecutar el modelo CFD con las nuevas BC. Resultados preliminares en
  `resultado simulaciones/` (Case 1 y Case 2).

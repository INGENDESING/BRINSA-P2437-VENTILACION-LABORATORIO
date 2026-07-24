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

## Ejecución

- Modelo CFD resuelto en Autodesk CFD con inyección como `velocity inlet` a 8 m/s
  y las tres rejillas de exfiltración como `pressure outlet` a 0 Pa gauge.
- Resultados integrados en el informe `P2437-HV-INF-001 REV0` (Secciones 5 y 6):
  cuatro vistas/gráficas del campo de velocidad, con análisis figura por figura.
- El balance de masas visual y el campo de velocidades confirman velocidades
  faciales del orden de 3 m/s en las rejillas y ausencia de flujo entrante.

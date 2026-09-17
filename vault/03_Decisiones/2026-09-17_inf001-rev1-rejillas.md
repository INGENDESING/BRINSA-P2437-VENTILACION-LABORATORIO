---
fecha: 2026-09-17
estado: vigente
tags: [decision]
---

# Decisión: INF-001 emitido en Revisión 1 (REV1) por reubicación de rejillas

## Decisión

El informe **P2437-HV-INF-001** pasa de REV0 a **REV1** con fecha 10/09/2026,
a causa del cambio de disposición de las rejillas de exfiltración (apiladas
verticalmente en la pared opuesta a la inyección) y la actualización de la
simulación CFD. Los demás entregables permanecen en REV0.

## Motivo

El cambio de posición de las rejillas es una modificación de diseño solicitada
por BRINSA que afecta el contenido técnico del informe (figuras CFD, análisis,
conclusiones y recomendaciones); conforme a GP-N-09, amerita una nueva revisión
documental. Ver [[2026-09-17_rejillas-verticales-cfd]].

## Implementación

- `config/datos_proyecto.tex`: macros `\fechaRevUno` (10/09/2026) y
  `\descRevUno`; fechas de firma a 10/09/2026.
- `P2437-HV-INF-001 REV0.tex`: `\docRevision{1}`, `\docFecha{10/09/2026}`
  (el nombre del archivo fuente conserva el sufijo REV0 por ser intermedio;
  el emitido no lleva sufijo, conforme a la excepción de nomenclatura).
- `sections/00_hojafirmas.tex` y `sections/00_portada.tex`: fila REV1
  **condicional** (`\ifnum\docRevision>0`) porque ambos archivos son
  compartidos con INF-002, que permanece en REV0.
- `Codificacion/codificacion.md`: INF-001 marcado como Rev. 1.

## Alternativas consideradas

- Mantener REV0: descartada; el cliente ya recibiría el documento con un
  cambio de diseño respecto a la emisión inicial, lo que exige trazabilidad
  de revisión.
- Pasar todos los entregables a REV1: descartada; el cambio solo afecta el
  contenido de INF-001 (y la nota de disposición en DTS-003, que permanece
  en REV0 por no haber sido emitido formalmente).

## Referencias

- GP-N-09 (control de revisiones); [[2026-07-28_rev0-unica-revision-cero]]
  (parcialmente superada por esta decisión); [[codificacion]].

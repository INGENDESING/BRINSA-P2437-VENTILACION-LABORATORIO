---
fecha: 2026-07-28
estado: vigente
tags: [decision]
---

# Decisión: Revisión CERO (0) única en todos los entregables

## Decisión

Todos los documentos del proyecto quedan en **Revisión CERO (0)**, conforme a
GP-N-09 (todo documento inicia en Revisión CERO). Se eliminaron todas las
referencias a REV1/REV2 de las fuentes de entregables, reescribiendo las frases
para conservar el hecho técnico sin la etiqueta de revisión. La excepción de
nomenclatura se mantiene: los archivos emitidos en `Emisiones/` no llevan
sufijo de revisión en el nombre.

## Motivo

El cliente no ha recibido ninguna entrega formal; llevar los documentos a REV1
o REV2 sin emisión previa contradice GP-N-09 y genera confusión en el control
documental. El historial de cambios queda en la memoria interna del proyecto
(`task/todo.md`, `vault/04_Bitácora/`) y en git, no en los entregables.

## Alcance aplicado (2026-07-28)

- Metadatos y notas de revisión de HD-VENT-001, HD-FILT-001,
  `listado_equipos.md`, `informe_investigacion.md` → Revisión 0, sin notas.
- INF-001: `\docRevision{0}`, tabla de control de revisiones solo con REV0
  (`00_hojafirmas.tex`, `00_portada.tex`), sección «Nota de Revisión» eliminada.
- INF-002: `\docRevision{0}`, sin `\descRevUno`; prosa de secciones 10/11
  neutralizada.
- `config/datos_proyecto.tex`: eliminadas las macros huérfanas
  `\fechaRevUno…\descRevCuatro`.
- `pdf_dts001.py`, `emitir.py` (comentarios), `codificacion.md`,
  `docs/index.html`, `bases_diseno.yaml`, `generar_img_dts001.py`.
- Verificación: 0 coincidencias REV1/REV2 en `Emisiones/` (excepción conocida:
  `P2437-HV-CAL-001.pdf`, exportación manual obsoleta pendiente de retiro o
  re-exportación).

Relacionado: [[2026-07-28]], [[inicializacion]], [[codificacion]]

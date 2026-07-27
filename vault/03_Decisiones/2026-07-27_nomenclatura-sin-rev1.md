---
fecha: 2026-07-27
estado: vigente
tags: [decision, codificacion, gp-n-09, entregables]
---

# Decisión: Nombres de entregables sin sufijo de revisión REV1

## Decisión

Para el proyecto P2437 se aplica una excepción a la codificación GP-N-09: los archivos emitidos en `Emisiones/` no llevan el sufijo ` REV1` al final del nombre. El código del documento se conserva como `P2437-<ESPECIALIDAD>-<TIPO>-<consecutivo>`; la revisión vigente se documenta en la portada/metadatos del archivo y en el control de versiones de git.

## Motivo

- Solicitud explícita del cliente/proyecto para simplificar los nombres de archivo de los entregables.
- La revisión sigue siendo rastreable dentro del documento (portada, encabezado, registro de revisiones) y en el historial de git.

## Alternativas consideradas

- **Mantener ` REV1` en el nombre conforme a GP-N-09:** descartado porque el cliente requirió la excepción.
- **Usar solo el consecutivo sin especialidad/tipo:** descartado porque rompería la trazabilidad y la organización por carpetas de GP-N-09.

## Referencias

- `Codificacion/codificacion.md` §4.3.1
- `scripts/emitir.py`
- `Emisiones/MANIFIESTO_EMISION.md`
- GP-N-09 — Normalización de la documentación de los proyectos (DML Ingenieros Consultores S.A.S.)

---
fecha: 2026-07-27
estado: vigente
tags: [decision, excel, formato]
---

# Decisión: presentación unificada de Excel entregables (A:O, Times New Roman)

## Decisión

Todas las tablas de los documentos Excel generados (`CAL`, `DTS`, `LIS`) se extienden exactamente hasta la columna O (15 columnas físicas), igual que el encabezado corporativo de las plantillas. Se fuerza la fuente Times New Roman en todo el documento, se mantienen los colores corporativos y se añade ajuste automático de alturas de fila.

## Motivo

Requisito del usuario para alinear la presentación de los entregables Excel con el ancho del encabezado corporativo, mejorar legibilidad y cumplir la identidad visual DML sin modificar las plantillas originales.

## Alternativas consideradas

- Dejar `N_COLS = 6` en CAL: descartado porque generaba tablas más angostas que el encabezado y huecos visuales.
- Solo cambiar la fuente sin ajustar anchos: descartado porque no resolvía el desalineamiento de tablas.

## Referencias

- Plantillas corporativas: `FormatosDocumentos/CAL.xlsx`, `FormatosDocumentos/DTS.xlsx`, `FormatosDocumentos/LIS.xlsx`.
- Generadores modificados: `generar_excel.py`, `scripts/generar_dts.py`, `scripts/generar_lis.py`.

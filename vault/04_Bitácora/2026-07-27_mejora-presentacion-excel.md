---
fecha: 2026-07-27
tags: [bitacora]
---

# Bitácora — 2026-07-27

## Qué se hizo

- Se actualizó `generar_excel.py`:
  - `N_COLS` de 6 a 15.
  - Funciones `spans_tabla()`, `col_inicio()`, `col_letra()` para repartir columnas lógicas en A:O.
  - `escribir_fila()` y `encabezados_tabla()` adaptadas a listas de valores con spans dinámicos.
  - Recálculo de referencias de fórmulas para el layout de 15 columnas (sección 3 y sección 6).
  - Fuente Times New Roman forzada en estilos, celdas escritas, encabezado corporativo copiado y portada.
  - Ajuste automático de alturas de fila según longitud de texto y ancho de celda combinada.
  - Distribución proporcional de anchos de columna A:O.
- Se actualizaron `scripts/generar_dts.py` y `scripts/generar_lis.py`:
  - Times New Roman en todos los estilos y celdas escritas.
  - Forzado de Times New Roman en encabezado corporativo (filas 1-7) y portada.
  - Anchos proporcionales A:O y ajuste de alturas de fila.
  - Verificación de que todas las tablas principales ocupan A:O.
- Se ejecutó `python scripts/emitir.py` para regenerar y emitir 7 entregables REV1.

## Verificación

- `python generar_excel.py`, `python scripts/generar_dts.py`, `python scripts/generar_lis.py` y `python scripts/emitir.py` ejecutados sin errores.
- openpyxl confirmó `max_column = 15` en todos los libros emitidos.
- Fuentes detectadas: Times New Roman en títulos, encabezados de tabla, cuerpo y encabezado corporativo.
- Primeras tablas principales abarcan A:O (merges verificados).
- `grep` sobre los tres generadores no encontró `Calibri` ni `Arial` hardcodeado.
- Los informes LaTeX se recompilaron con 0 errores.

## Pendientes

- Revisión visual final de los Excel en Microsoft Excel.
- Generación manual del PDF de `P2437-HV-DTS-001 REV1.xlsx` si aún no se ha hecho.

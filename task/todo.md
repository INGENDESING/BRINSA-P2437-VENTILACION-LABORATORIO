# Plan: Generar listado de equipos (LIS) en Excel corporativo

## Contexto
- Objetivo: Convertir `Investigacion/Sistemas/listado_equipos.md` (fuente canónica del BOQ) a un libro Excel con la plantilla corporativa `FormatosDocumentos/LIS.xlsx`, exactamente con 2 hojas: PORTADA y LISTA. El entregable emitido será `Emisiones/4.0 HV-LISTADOS/P2437-HV-LIS-001 REV0.xlsx`, reemplazando al `.md` actual.
- Cliente / Proyecto DML: BRINSA — P2437-HV-LIS-001.
- Normas / estándares: Plantilla corporativa DML (`LIS.xlsx`), codificación GP-N-09, patrón `scripts/generar_dts.py`.

## Supuestos clave
- [ ] La fuente del listado es `Investigacion/Sistemas/listado_equipos.md` (idem al `.md` ya emitido).
- [ ] El Excel resultante debe tener exactamente 2 hojas: PORTADA y LISTA.
- [ ] El layout de la hoja LISTA sigue el patrón DTS: encabezado corporativo en filas 1-7 (copiado de la hoja ENCABEZADO de la plantilla) y contenido Markdown desde la fila 9.
- [ ] La tabla BOQ tiene 7 columnas Markdown; se mapean a columnas A:G en Excel, aplicando el estilo corporativo azul 1F4E78 con bordes thin.
- [ ] `scripts/emitir.py` orquestará la generación y copia del LIS, retirando el `.md` obsoleto de `Emisiones/4.0 HV-LISTADOS/`.

## Tareas
- [ ] T1. Crear `scripts/generar_lis.py` a partir del patrón `scripts/generar_dts.py`, adaptado a 7 columnas (A:G) y a la plantilla `LIS.xlsx`. Salida: `build/lis/P2437-HV-LIS-001 REV0.xlsx`.
- [ ] T2. Actualizar `scripts/emitir.py`: añadir paso `[x/5]` para ejecutar `generar_lis.py`, cambiar la fuente del LIS en `ENTREGABLES` al `.xlsx`, y añadir el `.md` obsoleto a `OBSOLETOS`.
- [ ] T3. Ejecutar `python scripts/generar_lis.py` y verificar visualmente el Excel generado (PORTADA + LISTA, 7 columnas, estilos, encabezado corporativo).
- [ ] T4. Ejecutar `python scripts/emitir.py` completo y verificar que el entregable aparezca en `Emisiones/4.0 HV-LISTADOS/P2437-HV-LIS-001 REV0.xlsx` y que el manifiesto lo registre correctamente.
- [ ] T5. Actualizar `contexto.md`, vault (`01_Estado actual.md`, `04_Bitácora/2026-07-24.md`, `06_Archivos clave.md`) y hacer push a GitHub.

## Riesgos / Puntos de verificación
- [ ] Validación dimensional: la tabla Markdown tiene 7 columnas; el layout Excel debe ser A:G sin perder contenido.
- [ ] Validación de estilos: encabezado corporativo, títulos Markdown, tabla BOQ y notas deben verse uniformes.
- [ ] Validación de `emitir.py`: el `.md` debe retirarse de `Emisiones/4.0 HV-LISTADOS/` y no quedar huérfano.
- [ ] Validación final: working tree limpio y push exitoso.

## Revisión

- Resumen: se creó `scripts/generar_lis.py` para convertir `Investigacion/Sistemas/listado_equipos.md`
  en un libro Excel corporativo (`P2437-HV-LIS-001 REV0.xlsx`) con exactamente 2 hojas
  (PORTADA + LISTA). Se actualizó `scripts/emitir.py` para orquestar la generación,
  emitir el `.xlsx` a `Emisiones/4.0 HV-LISTADOS/` y retirar el `.md` obsoleto. La
  emisión completa fue exitosa (8 entregables, 0 errores LaTeX).
- Desviaciones respecto al plan: ninguna; el layout A:G para 7 columnas BOQ fue el
  previsto.
- Limitaciones: los anchos de columna se heredan de la plantilla `LIS.xlsx`; el
  contenido largo se visualiza con `wrap_text`, pero no se autoajustan filas
  combinadas (misma limitación documentada para los DTS).
- Entregables:
  - `scripts/generar_lis.py`
  - `scripts/emitir.py` (actualizado)
  - `build/lis/P2437-HV-LIS-001 REV0.xlsx`
  - `Emisiones/4.0 HV-LISTADOS/P2437-HV-LIS-001 REV0.xlsx`
  - `Emisiones/MANIFIESTO_EMISION.md`
  - `contexto.md` y vault actualizados.

---
fecha: 2026-07-27
estado: vigente
tags: [decision, dts001, pdf, entregable]
---

# Decisión: PDF alternativo de P2437-HV-DTS-001 REV1

## Decisión

Dado que el entorno de trabajo no dispone de Excel ni LibreOffice para exportar manualmente la hoja de datos `P2437-HV-DTS-001.xlsx` a PDF, se generó un PDF alternativo con `reportlab` desde el markdown fuente `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md`.

## Motivo

- El pendiente original requería generar el PDF desde Excel para mantener la plantilla corporativa idéntica.
- Este entorno (Windows/Git Bash) no tiene instalado Excel, LibreOffice ni `win32com`; instalar LibreOffice solo para una exportación no era práctico.
- `reportlab` permite reproducir portada, especificación, tablas con estilo corporativo, fuente Times New Roman e imágenes de curva/referencia de forma programática.

## Alternativas consideradas

- **Esperar a tener Excel disponible:** descartado porque dejaba un entregable REV1 incompleto.
- **Generar HTML e imprimir a PDF:** descartado porque el usuario pidió explícitamente un PDF generado con Python.
- **Usar `matplotlib.backend_pdf`:** descartado porque reportlab ofrece mejor control de layouts, tablas y fuentes.

## Referencias

- `scripts/pdf_dts001.py`
- `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md`
- `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001 REV1.pdf`
- `Emisiones/MANIFIESTO_EMISION.md`

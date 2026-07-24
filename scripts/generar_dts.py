#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generar_dts.py — Convierte las hojas de datos Markdown (Investigacion/Sistemas/
hojas_datos/*.md) a libros Excel con la plantilla corporativa
FormatosDocumentos/DTS.xlsx.

Cada libro resultante tiene EXACTAMENTE 2 hojas:
  - PORTADA: portada corporativa diligenciada (BO1 = código, Z5 = título).
  - ESPECIFICACIÓN: encabezado corporativo (filas 1-7, logos y fórmulas
    =PORTADA!...) y el contenido del .md apilado desde la fila 9, con todas
    las tablas en el layout unificado A:F (encabezado azul 1F4E78, bordes
    thin, alineación por rol), igual que en la memoria de cálculo.

Salida: build/dts/<código> REV0.xlsx (intermedios que scripts/emitir.py copia
a Emisiones/3.0 HV-HOJAS DE DATOS/).

Uso:  python scripts/generar_dts.py
"""

import math
import re
from copy import copy, deepcopy
from io import BytesIO
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.drawing.image import Image as XLImage
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from PIL import Image as PILImage

ROOT = Path(__file__).resolve().parent.parent
PLANTILLA = ROOT / "FormatosDocumentos" / "DTS.xlsx"
SALIDA = ROOT / "build" / "dts"
FILA_INICIO = 9  # contenido tras encabezado corporativo (1-7) y fila 8 libre
N_COLS = 6       # layout unificado: todas las tablas abarcan A:F

# (archivo .md fuente, código del documento, título para PORTADA!Z5)
DOCUMENTOS = [
    ("Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md",
     "P2437-HV-DTS-001",
     "HOJA DE DATOS Y ESPECIFICACIONES TÉCNICAS DEL VENTILADOR CENTRÍFUGO PRFV"),
    ("Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md",
     "P2437-HV-DTS-002",
     "HOJA DE DATOS Y ESPECIFICACIONES TÉCNICAS DEL SISTEMA DE FILTRACIÓN MERV 13-14"),
    ("Investigacion/Sistemas/hojas_datos/HD-REJ-001_rejillas.md",
     "P2437-HV-DTS-003",
     "HOJA DE DATOS Y ESPECIFICACIONES TÉCNICAS DE LAS REJILLAS DE EXFILTRACIÓN"),
    ("Investigacion/Sistemas/hojas_datos/HD-INST-001_instrumentos_presion.md",
     "P2437-IC-DTS-001",
     "HOJA DE DATOS Y ESPECIFICACIONES TÉCNICAS DE LOS INSTRUMENTOS DE PRESIÓN DIFERENCIAL"),
]

# ===================== ESTILOS (idénticos a la memoria de cálculo) =====================
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(color="FFFFFF", bold=True, size=11)
title_font = Font(bold=True, size=14, color="1F4E78")        # títulos #
section_font = Font(bold=True, size=12, color="1F4E78")      # títulos ##
subtitle_font = Font(bold=True, size=11, color="1F4E78")     # títulos ###
caption_font = Font(bold=True, size=11)                      # leyendas **Tabla N.**
thin_border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)
AL_TEXTO = Alignment(horizontal='left', vertical='center', wrap_text=True)
AL_HEADER = Alignment(horizontal='center', vertical='center', wrap_text=True)
AL_PARRAFO = Alignment(horizontal='left', vertical='top', wrap_text=True)


# ===================== PARSEO MARKDOWN =====================
def limpiar_md(texto):
    """Quita sintaxis markdown: **negrita**, [texto](url) -> 'texto (url)', `código`."""
    texto = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', texto)
    return texto.replace('**', '').replace('`', '').strip()


def es_separador_tabla(celdas):
    return all(re.fullmatch(r':?-{2,}:?', c.strip()) for c in celdas if c.strip()) \
        and any(c.strip() for c in celdas)


def parsear_linea_tabla(linea):
    return [limpiar_md(c) for c in linea.strip().strip('|').split('|')]


def spans_tabla(n_cols):
    """Distribuye n_cols columnas markdown en el layout A:F: las primeras
    n_cols-1 ocupan 1 columna y la última se extiende hasta F."""
    if n_cols > N_COLS:
        raise ValueError(f"Tabla con {n_cols} columnas supera el layout A:F")
    return [1] * (n_cols - 1) + [N_COLS - n_cols + 1]


# ===================== CONSTRUCCIÓN DE LA HOJA =====================
class HojaDTS:
    def __init__(self, ws):
        self.ws = ws
        self.r = FILA_INICIO

    def _combinar(self, r1, r2, c2=N_COLS):
        self.ws.merge_cells(start_row=r1, start_column=1, end_row=r2, end_column=c2)

    def titulo(self, texto, nivel):
        if self.r > FILA_INICIO:
            self.r += 1  # fila en blanco antes de cada título
        cell = self.ws.cell(row=self.r, column=1, value=texto)
        cell.font = {1: title_font, 2: section_font}.get(nivel, subtitle_font)
        cell.alignment = Alignment(vertical='center', wrap_text=True)
        self._combinar(self.r, self.r)
        self.r += 1

    def parrafo(self, texto, negrita=False):
        # Filas estimadas para el texto con wrap en el ancho A:F (~90 caracteres)
        n = min(max(1, math.ceil(len(texto) / 80)), 15)
        cell = self.ws.cell(row=self.r, column=1, value=texto)
        cell.alignment = AL_PARRAFO
        if negrita:
            cell.font = caption_font
        if n > 1:
            self._combinar(self.r, self.r + n - 1)
        self.r += n

    def tabla(self, filas):
        spans = spans_tabla(len(filas[0]))
        hdr = self.r
        # Encabezado unificado
        col = 1
        for texto, n in zip(filas[0], spans):
            self.ws.cell(row=self.r, column=col, value=texto)
            if n > 1:
                self.ws.merge_cells(start_row=self.r, start_column=col,
                                    end_row=self.r, end_column=col + n - 1)
            # Estilo DESPUÉS de combinar (persiste en MergedCell)
            for cc in range(col, col + n):
                cell = self.ws.cell(row=self.r, column=cc)
                cell.fill = header_fill
                cell.font = header_font
                cell.alignment = AL_HEADER
            col += n
        self.r += 1
        # Cuerpo
        for fila in filas[1:]:
            col = 1
            for texto, n in zip(fila, spans):
                cell = self.ws.cell(row=self.r, column=col, value=texto)
                cell.alignment = AL_TEXTO
                if n > 1:
                    self.ws.merge_cells(start_row=self.r, start_column=col,
                                        end_row=self.r, end_column=col + n - 1)
                col += n
            self.r += 1
        # Bordes thin en todo el rango A:F (incluye MergedCell, persiste al guardar)
        for row in self.ws.iter_rows(min_row=hdr, max_row=self.r - 1, min_col=1, max_col=N_COLS):
            for cell in row:
                cell.border = thin_border
        self.r += 1  # fila en blanco tras la tabla


def construir_especificacion(ws, md):
    hoja = HojaDTS(ws)
    lineas = md.split('\n')
    i = 0
    while i < len(lineas):
        ln = lineas[i].strip()
        i += 1
        if not ln or ln == '---':
            continue
        if ln.startswith('|'):
            bloque = [ln]
            while i < len(lineas) and lineas[i].strip().startswith('|'):
                bloque.append(lineas[i].strip())
                i += 1
            filas = [parsear_linea_tabla(l) for l in bloque]
            filas = [f for f in filas if not es_separador_tabla(f)]
            hoja.tabla(filas)
        elif ln.startswith('#'):
            nivel = len(ln) - len(ln.lstrip('#'))
            hoja.titulo(limpiar_md(ln.lstrip('#')), nivel)
        else:
            hoja.parrafo(limpiar_md(ln), negrita=ln.startswith('**Tabla'))


def insertar_encabezado(ws, ws_enc, imagenes):
    """Replica el bloque corporativo de ENCABEZADO (filas 1-7) en `ws`."""
    for rr in range(1, 8):
        ws.row_dimensions[rr].height = ws_enc.row_dimensions[rr].height
        for cc in range(1, 16):
            src = ws_enc.cell(row=rr, column=cc)
            dst = ws.cell(row=rr, column=cc)
            dst.value = src.value
            dst._style = copy(src._style)
    for m in ws_enc.merged_cells.ranges:
        if m.min_row <= 7:
            ws.merge_cells(str(m))
    for cc in range(1, 16):
        letra = get_column_letter(cc)
        ws.column_dimensions[letra].width = ws_enc.column_dimensions[letra].width
    for blob, anchor in imagenes:
        img = XLImage(PILImage.open(BytesIO(blob)))
        img.anchor = deepcopy(anchor)
        ws.add_image(img)


def generar_libro(md_rel, codigo, titulo):
    md_path = ROOT / md_rel
    md = md_path.read_text(encoding='utf-8')

    wb = load_workbook(PLANTILLA)
    ws_enc = wb["ENCABEZADO"]
    imagenes = [(im._data(), deepcopy(im.anchor)) for im in ws_enc._images]

    # PORTADA: solo código y título; firmas/fecha/revisión quedan de la plantilla
    ws_portada = wb["PORTADA"]
    assert ws_portada["Z3"].value == "SISTEMA HVAC LABORATORIO BRINSA", ws_portada["Z3"].value
    assert ws_portada["N6"].value == "P2437", ws_portada["N6"].value
    ws_portada["BO1"] = codigo
    ws_portada["Z5"] = titulo

    ws = wb.create_sheet("ESPECIFICACIÓN")
    construir_especificacion(ws, md)
    insertar_encabezado(ws, ws_enc, imagenes)

    wb.remove(ws_enc)  # orden final: PORTADA, ESPECIFICACIÓN
    wb.calculation.calcMode = "auto"
    wb.calculation.fullCalcOnLoad = True

    SALIDA.mkdir(parents=True, exist_ok=True)
    out = SALIDA / f"{codigo} REV0.xlsx"
    wb.save(out)
    return out


def main():
    print("== GENERACIÓN DE HOJAS DE DATOS (DTS) ==")
    for md_rel, codigo, titulo in DOCUMENTOS:
        out = generar_libro(md_rel, codigo, titulo)
        print(f"  {codigo}  <-  {md_rel}")
        print(f"       ->  {out.relative_to(ROOT)}")
    print("OK: 4 libros DTS generados en build/dts/")


if __name__ == "__main__":
    main()

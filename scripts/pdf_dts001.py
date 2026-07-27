#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pdf_dts001.py — Genera un PDF alternativo de P2437-HV-DTS-001
(ventilador axial mural Ø560 mm, transmisión directa) a partir del markdown
fuente.

Dado que este entorno no dispone de Excel/LibreOffice para la exportación
manual, este script produce un PDF con layout corporativo DML equivalente:
portada + especificación (títulos, párrafos, tablas, notas e imágenes).

Uso:  .venv/Scripts/python scripts/pdf_dts001.py
Salida: build/dts/P2437-HV-DTS-001.pdf
"""

import math
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent.parent
MD_FUENTE = ROOT / "Investigacion" / "Sistemas" / "hojas_datos" / "HD-VENT-001_ventilador.md"
IMG_DIR = ROOT / "build" / "dts" / "img"
SALIDA = ROOT / "build" / "dts" / "P2437-HV-DTS-001.pdf"

# Colores corporativos
AZUL = colors.HexColor("#1F4E78")
GRIS = colors.HexColor("#E7E6E6")
BLANCO = colors.white
NEGRO = colors.black
GRIS_OSCURO = colors.HexColor("#404040")

# Fuentes
FONT_DIR = Path("C:/Windows/Fonts")
FONT_NAMES = {
    "regular": "TimesNewRoman",
    "bold": "TimesNewRomanBold",
    "italic": "TimesNewRomanItalic",
    "bolditalic": "TimesNewRomanBoldItalic",
}


def registrar_fuentes():
    """Registra Times New Roman en reportlab si existe; de lo contrario Helvetica."""
    mapping = [
        (FONT_NAMES["regular"], "times.ttf"),
        (FONT_NAMES["bold"], "timesbd.ttf"),
        (FONT_NAMES["italic"], "timesi.ttf"),
        (FONT_NAMES["bolditalic"], "timesbi.ttf"),
    ]
    ok = True
    for name, file in mapping:
        path = FONT_DIR / file
        if path.exists():
            pdfmetrics.registerFont(TTFont(name, str(path)))
        else:
            ok = False
            break
    if not ok:
        print("Advertencia: Times New Roman no completo; usando Helvetica como reserva.")
        return {
            "regular": "Helvetica",
            "bold": "Helvetica-Bold",
            "italic": "Helvetica-Oblique",
            "bolditalic": "Helvetica-BoldOblique",
        }
    return FONT_NAMES


FONTS = registrar_fuentes()


def estilos():
    """Construye el diccionario de estilos de párrafo corporativos."""
    base = {
        "fontName": FONTS["regular"],
        "fontSize": 11,
        "leading": 14,
        "spaceAfter": 6,
    }
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="PortadaCodigo", fontName=FONTS["bold"], fontSize=14, textColor=AZUL,
                         alignment=TA_CENTER, spaceAfter=12, leading=18))
    s.add(ParagraphStyle(name="PortadaTitulo", fontName=FONTS["bold"], fontSize=18, textColor=AZUL,
                         alignment=TA_CENTER, spaceAfter=18, leading=22))
    s.add(ParagraphStyle(name="PortadaSub", fontName=FONTS["regular"], fontSize=12,
                         alignment=TA_CENTER, spaceAfter=30, leading=16))
    s.add(ParagraphStyle(name="Titulo1", fontName=FONTS["bold"], fontSize=16, textColor=AZUL,
                         alignment=TA_LEFT, spaceBefore=18, spaceAfter=10, leading=20))
    s.add(ParagraphStyle(name="Titulo2", fontName=FONTS["bold"], fontSize=14, textColor=AZUL,
                         alignment=TA_LEFT, spaceBefore=14, spaceAfter=8, leading=18))
    s.add(ParagraphStyle(name="Titulo3", fontName=FONTS["bold"], fontSize=12, textColor=AZUL,
                         alignment=TA_LEFT, spaceBefore=10, spaceAfter=6, leading=16))
    s.add(ParagraphStyle(name="Cuerpo", **base, alignment=TA_JUSTIFY))
    s.add(ParagraphStyle(name="Nota", fontName=FONTS["italic"], fontSize=10, textColor=GRIS_OSCURO,
                         alignment=TA_JUSTIFY, leading=13, spaceAfter=6, leftIndent=8))
    s.add(ParagraphStyle(name="TablaHeader", fontName=FONTS["bold"], fontSize=10, textColor=BLANCO,
                         alignment=TA_CENTER, leading=13))
    s.add(ParagraphStyle(name="TablaCelda", fontName=FONTS["regular"], fontSize=9,
                         alignment=TA_LEFT, leading=12))
    s.add(ParagraphStyle(name="TablaCeldaCenter", fontName=FONTS["regular"], fontSize=9,
                         alignment=TA_CENTER, leading=12))
    s.add(ParagraphStyle(name="Pie", fontName=FONTS["regular"], fontSize=8, textColor=GRIS_OSCURO,
                         alignment=TA_CENTER, leading=10))
    s.add(ParagraphStyle(name="EncabezadoPie", fontName=FONTS["regular"], fontSize=9, textColor=NEGRO,
                         alignment=TA_CENTER, leading=11))
    return s


ESTILOS = estilos()


def limpiar_md(texto):
    """Quita negrita markdown y enlaces; mantiene el texto legible."""
    texto = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', texto)
    return texto.replace('**', '').replace('`', '').strip()


def escapar_html(texto):
    """Escapa caracteres XML para Paragraph de reportlab."""
    return (texto
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;'))


def es_separador_tabla(celdas):
    return all(re.fullmatch(r':?-{2,}:?', c.strip()) for c in celdas if c.strip()) \
        and any(c.strip() for c in celdas)


def parsear_linea_tabla(linea):
    return [limpiar_md(c) for c in linea.strip().strip('|').split('|')]


def es_nota_numerada(texto):
    return bool(re.match(r'^\d+\.\d+\.\s', texto))


def dividir_notas_numeradas(texto):
    partes = re.split(r'(?=\b\d+\.\d+\.\s)', texto)
    return [p.strip() for p in partes if p.strip()]


def generar_imagenes():
    """Ejecuta generar_img_dts001.py si faltan las imágenes."""
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    curva = IMG_DIR / "curva_ventilador_dts001.png"
    ref = IMG_DIR / "ventilador_referencia_dts001.png"
    if not curva.exists() or not ref.exists():
        script = ROOT / "scripts" / "generar_img_dts001.py"
        r = subprocess.run([sys.executable, str(script)], cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr)
            raise RuntimeError("generar_img_dts001.py falló")
        print(r.stdout)


# ===================== CONSTRUCCIÓN DEL DOCUMENTO =====================

class PDFDTS001:
    def __init__(self, md_texto):
        self.md = md_texto
        self.elements = []

    def agregar_titulo(self, texto, nivel):
        estilo = {1: "Titulo1", 2: "Titulo2"}.get(nivel, "Titulo3")
        self.elements.append(Paragraph(escapar_html(texto), ESTILOS[estilo]))

    def agregar_parrafo(self, texto, negrita=False, nota=False):
        if nota or es_nota_numerada(texto):
            for nota_texto in dividir_notas_numeradas(texto):
                self.elements.append(Paragraph(escapar_html(nota_texto), ESTILOS["Nota"]))
            return
        estilo = "Cuerpo"
        if negrita:
            # Párrafos tipo leyenda de tabla en negrita
            txt = f"<b>{escapar_html(texto)}</b>"
            self.elements.append(Paragraph(txt, ESTILOS["Cuerpo"]))
        else:
            self.elements.append(Paragraph(escapar_html(texto), ESTILOS[estilo]))

    def agregar_tabla(self, filas):
        if not filas:
            return
        # Calcular anchos proporcionales según número de columnas lógicas
        n_cols = len(filas[0])
        available_width = 17 * cm  # ancho útil en carta con márgenes 2cm
        base = available_width / n_cols
        # Primera columna más ancha si es tabla de 2 columnas (Campo|Valor)
        if n_cols == 2:
            col_widths = [available_width * 0.45, available_width * 0.55]
        else:
            col_widths = [base] * n_cols

        data = []
        for i, fila in enumerate(filas):
            row = []
            for j, celda in enumerate(fila):
                style = "TablaCelda" if i > 0 else "TablaHeader"
                # Centrar celdas cortas de encabezado
                if i == 0 and len(celda) < 25:
                    style = "TablaHeader"
                elif i > 0 and len(celda) < 15:
                    style = "TablaCeldaCenter"
                row.append(Paragraph(escapar_html(str(celda)), ESTILOS[style]))
            data.append(row)

        table = Table(data, colWidths=col_widths, repeatRows=1)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), AZUL),
            ('TEXTCOLOR', (0, 0), (-1, 0), BLANCO),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 0), FONTS["bold"]),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('TOPPADDING', (0, 0), (-1, 0), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#BFBFBF")),
            ('BACKGROUND', (0, 1), (-1, -1), BLANCO),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ])
        table.setStyle(style)
        self.elements.append(Spacer(1, 6))
        self.elements.append(table)
        self.elements.append(Spacer(1, 10))

    def agregar_imagenes(self):
        """Inserta curva y referencia del ventilador al final de la especificación."""
        curva = IMG_DIR / "curva_ventilador_dts001.png"
        ref = IMG_DIR / "ventilador_referencia_dts001.png"
        if not curva.exists() or not ref.exists():
            return
        self.elements.append(PageBreak())
        self.elements.append(Paragraph("Referencia gráfica", ESTILOS["Titulo2"]))
        self.elements.append(Spacer(1, 8))
        for img_path, caption in [(curva, "Figura 1. Curva característica ilustrativa."),
                                   (ref, "Figura 2. Montaje típico de planta — ventilador axial mural Ø560 mm (inyección 2 260 CFM).")]:
            with PILImage.open(img_path) as im:
                w, h = im.size
            max_width = 16 * cm
            scale = min(max_width / w, 10 * cm / h)
            img = Image(str(img_path), width=w * scale, height=h * scale)
            self.elements.append(img)
            self.elements.append(Paragraph(f"<i>{caption}</i>", ESTILOS["Pie"]))
            self.elements.append(Spacer(1, 12))

    def construir_especificacion(self):
        """Parsea el markdown y construye el flujo de la especificación."""
        lineas = self.md.split('\n')
        i = 0
        # Saltar metadatos iniciales hasta el primer título
        while i < len(lineas) and not lineas[i].strip().startswith('#'):
            i += 1
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
                if filas:
                    self.agregar_tabla(filas)
            elif ln.startswith('#'):
                nivel = len(ln) - len(ln.lstrip('#'))
                self.agregar_titulo(limpiar_md(ln.lstrip('#')), nivel)
            else:
                self.agregar_parrafo(limpiar_md(ln), negrita=ln.startswith('**Tabla'))
        self.agregar_imagenes()

    def portada(self):
        """Construye la página de portada."""
        portada = []
        portada.append(Spacer(1, 2 * cm))
        # Logo placeholder
        portada.append(Paragraph("<b>DML</b> — Ingeniería", ESTILOS["PortadaCodigo"]))
        portada.append(Spacer(1, 1.5 * cm))
        portada.append(Paragraph("P2437-HV-DTS-001", ESTILOS["PortadaCodigo"]))
        portada.append(Paragraph("HOJA DE DATOS Y ESPECIFICACIONES TÉCNICAS", ESTILOS["PortadaTitulo"]))
        portada.append(Paragraph("DEL VENTILADOR AXIAL TUBEAXIAL PRFV", ESTILOS["PortadaTitulo"]))
        portada.append(Spacer(1, 0.5 * cm))
        portada.append(Paragraph("SISTEMA HVAC LABORATORIO BRINSA", ESTILOS["PortadaSub"]))
        portada.append(Paragraph("Cajicá, Cundinamarca — Proyecto P2437", ESTILOS["PortadaSub"]))
        portada.append(Spacer(1, 2 * cm))

        # Tabla de revisiones
        rev_data = [
            [Paragraph("Revisión", ESTILOS["TablaHeader"]),
             Paragraph("Fecha", ESTILOS["TablaHeader"]),
             Paragraph("Descripción", ESTILOS["TablaHeader"])],
            [Paragraph("REV1", ESTILOS["TablaCeldaCenter"]),
             Paragraph("2026-07-27", ESTILOS["TablaCeldaCenter"]),
             Paragraph("Cambio de alcance: sistema sin presurización, ventilador axial, sin instrumentación ΔP.",
                       ESTILOS["TablaCelda"])],
        ]
        rev_table = Table(rev_data, colWidths=[3 * cm, 3 * cm, 10 * cm])
        rev_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), AZUL),
            ('TEXTCOLOR', (0, 0), (-1, 0), BLANCO),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#BFBFBF")),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
        ]))
        portada.append(rev_table)
        portada.append(Spacer(1, 2 * cm))

        # Firmas
        firmas_data = [
            ["_________________________", "_________________________", "_________________________"],
            ["Elaboró", "Revisó", "Aprobó"],
        ]
        firmas = Table(firmas_data, colWidths=[5.5 * cm, 5.5 * cm, 5.5 * cm])
        firmas.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, -1), FONTS["regular"]),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 1), (-1, 1), 6),
        ]))
        portada.append(firmas)
        portada.append(Spacer(1, 1 * cm))
        portada.append(Paragraph(f"Documento generado el {datetime.now().strftime('%d/%m/%Y')}", ESTILOS["Pie"]))
        return portada

    def build(self):
        generar_imagenes()
        doc = SimpleDocTemplate(
            str(SALIDA),
            pagesize=letter,
            rightMargin=2 * cm,
            leftMargin=2 * cm,
            topMargin=2.5 * cm,
            bottomMargin=2 * cm,
        )
        self.elements.extend(self.portada())
        self.elements.append(PageBreak())
        self.construir_especificacion()
        doc.build(self.elements, onFirstPage=self._encabezado_pie, onLaterPages=self._encabezado_pie)
        print(f"PDF generado: {SALIDA.relative_to(ROOT)}")

    @staticmethod
    def _encabezado_pie(canvas, doc):
        canvas.saveState()
        canvas.setFont(FONTS["regular"], 8)
        canvas.setFillColor(GRIS_OSCURO)
        # Línea superior
        canvas.setStrokeColor(AZUL)
        canvas.setLineWidth(1)
        canvas.line(2 * cm, letter[1] - 1.5 * cm, letter[0] - 2 * cm, letter[1] - 1.5 * cm)
        # Encabezado
        canvas.drawCentredString(letter[0] / 2, letter[1] - 1.2 * cm,
                                 "P2437-HV-DTS-001 — HOJA DE DATOS VENTILADOR AXIAL TUBEAXIAL PRFV")
        # Pie
        canvas.drawCentredString(letter[0] / 2, 1 * cm,
                                 f"Página {doc.page} — Documento generado automáticamente — REV1")
        canvas.restoreState()


def main():
    if not MD_FUENTE.exists():
        raise FileNotFoundError(f"No se encontró la fuente: {MD_FUENTE}")
    md = MD_FUENTE.read_text(encoding='utf-8')
    pdf = PDFDTS001(md)
    pdf.build()


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generar_img_dts001.py — Genera las imágenes auxiliares para la hoja de datos
P2437-HV-DTS-001 (ventilador): curva característica ilustrativa y referencia
del equipo.

Salida: build/dts/img/curva_ventilador_dts001.png
        build/dts/img/ventilador_referencia_dts001.png

Uso:  python scripts/generar_img_dts001.py
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "build" / "dts" / "img"
IMG_DIR.mkdir(parents=True, exist_ok=True)


def generar_curva():
    """Curva característica ilustrativa de un ventilador centrífugo."""
    Q = list(range(0, 6201, 100))
    Q_max = 6000
    P_max = 420  # Pa
    P = [P_max * (1 - (q / Q_max) ** 2) for q in Q]

    Q_d = 3840
    P_d_catalogo = 260
    P_d_sitio = 190

    fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
    ax.plot(Q, P, color="#1F4E78", lw=2.5, label="Curva característica (ilustrativa)")
    ax.axvline(Q_d, color="#999999", ls="--", lw=0.8)
    ax.axhline(P_d_catalogo, color="#999999", ls="--", lw=0.8)
    ax.plot(Q_d, P_d_catalogo, "o", color="#C00000", ms=8)
    ax.annotate(
        f"Punto de diseño (catálogo)\n{Q_d:,} m³/h @ {P_d_catalogo} Pa",
        xy=(Q_d, P_d_catalogo),
        xytext=(Q_d + 300, P_d_catalogo + 60),
        arrowprops=dict(arrowstyle="->", color="#C00000"),
        fontsize=9,
        color="#C00000",
    )
    ax.plot(Q_d, P_d_sitio, "s", color="#2E75B6", ms=7)
    ax.annotate(
        f"Punto en sitio\n{Q_d:,} m³/h @ {P_d_sitio} Pa",
        xy=(Q_d, P_d_sitio),
        xytext=(Q_d + 300, P_d_sitio - 60),
        arrowprops=dict(arrowstyle="->", color="#2E75B6"),
        fontsize=9,
        color="#2E75B6",
    )
    ax.set_xlim(0, 6200)
    ax.set_ylim(0, 450)
    ax.set_xlabel("Caudal $Q$ [m³/h]")
    ax.set_ylabel("Presión total $\\Delta P$ [Pa]")
    ax.set_title("Curva característica ilustrativa del ventilador\n(punto de selección 3 840 m³/h @ 260 Pa catálogo)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    out = IMG_DIR / "curva_ventilador_dts001.png"
    fig.savefig(out)
    plt.close(fig)
    return out


def generar_referencia():
    """Imagen de referencia del ventilador (placeholder)."""
    W, H = 600, 400
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 2, W - 3, H - 3], outline="#1F4E78", width=3)

    try:
        font_title = ImageFont.truetype("arial.ttf", 28)
        font_sub = ImageFont.truetype("arial.ttf", 20)
        font_note = ImageFont.truetype("arial.ttf", 16)
    except OSError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_note = ImageFont.load_default()

    def centrar(texto, y, fuente, color="#1F4E78"):
        bbox = draw.textbbox((0, 0), texto, font=fuente)
        w = bbox[2] - bbox[0]
        draw.text(((W - w) / 2, y), texto, font=fuente, fill=color)

    centrar("VENTILADOR CENTRÍFUGO PRFV", 120, font_title)
    centrar("Greenheck BCSW-FRP (primera opción)", 170, font_sub, "#000000")
    centrar("3 840 m³/h @ 260 Pa catálogo", 210, font_sub, "#000000")
    centrar("Imagen de referencia por confirmar con proveedor", 310, font_note, "#666666")

    out = IMG_DIR / "ventilador_referencia_dts001.png"
    img.save(out)
    return out


def main():
    print("== GENERACIÓN DE IMÁGENES DTS-001 ==")
    curva = generar_curva()
    print(f"  {curva.relative_to(ROOT)}")
    ref = generar_referencia()
    print(f"  {ref.relative_to(ROOT)}")
    print("OK: imágenes generadas en build/dts/img/")


if __name__ == "__main__":
    main()

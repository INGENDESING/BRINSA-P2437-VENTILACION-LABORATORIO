#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generar_img_dts001.py — Genera las imágenes auxiliares para la hoja de datos
P2437-HV-DTS-001 (ventilador axial tubeaxial PRFV): curva característica
ilustrativa y referencia del equipo.

Salida: build/dts/img/curva_ventilador_dts001.png
        build/dts/img/ventilador_referencia_dts001.png

Uso:  python scripts/generar_img_dts001.py
"""

import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "build" / "dts" / "img"
IMG_DIR.mkdir(parents=True, exist_ok=True)


def generar_curva():
    """Curva característica ilustrativa de un ventilador axial tubular.

    Basada en los datos investigados del proyecto P2437:
      - Punto de selección (catálogo, ρ = 1.2 kg/m³): 3 840 m³/h @ 225 Pa
      - Punto equivalente en sitio (ρ = 0.88 kg/m³): 3 840 m³/h @ 165 Pa
      - Eficiencia axial provisional: η = 0.55
      - Forma parabólica típica de ventiladores axiales tubeaxial:
        ΔP(Q) = ΔP_bloqueo · (1 - (Q/Q_libre)²)

    Se ajustan ΔP_bloqueo y Q_libre para que la curva pase por el punto de
    catálogo y sea físicamente representativa de un axial PRFV de tamaño
    medio (presión de bloqueo ≈ 1,7× presión de diseño; caudal libre ≈ 1,6×
    caudal de diseño). La curva es ilustrativa y debe validarse contra el
    catálogo del fabricante seleccionado.
    """
    Q_d = 3840          # m³/h, caudal de diseño
    P_d_cat = 225       # Pa, presión total de diseño en catálogo (ρ = 1.2)
    P_d_sitio = 165     # Pa, presión total equivalente en sitio (ρ = 0.88)
    eta = 0.55          # eficiencia axial provisional
    k_rho = 0.733       # factor de densidad sitio/catálogo = 0.88/1.20

    # Parámetros de la parábola ilustrativa (ajustados al punto de diseño)
    Q_libre = 6000      # m³/h, caudal a presión nula
    P_bloqueo = 380     # Pa, presión a caudal nulo
    # Verificación: P(3840) = 380*(1-(3840/6000)^2) ≈ 224 Pa ≈ 225 Pa

    Q = list(range(0, 6201, 100))
    P_cat = [P_bloqueo * (1 - (q / Q_libre) ** 2) for q in Q]
    P_sitio = [k_rho * p for p in P_cat]

    # Potencia de eje teórica vs. caudal (catálogo) en kW
    # P_eje = Q[m³/s] · ΔP[Pa] / η
    P_eje_kw = [(q / 3600) * p / eta / 1000 for q, p in zip(Q, P_cat)]

    fig, ax1 = plt.subplots(figsize=(9, 5.5), dpi=120)

    # Curvas de presión
    ax1.plot(Q, P_cat, color="#1F4E78", lw=2.5,
             label=f"Curva catálogo (ρ = 1,2 kg/m³)")
    ax1.plot(Q, P_sitio, color="#2E75B6", lw=2.0, ls="--",
             label=f"Curva en sitio (ρ = 0,88 kg/m³, k = {k_rho:.3f})")

    # Zona de operación recomendada (60 % - 110 % del caudal de diseño)
    ax1.axvspan(0.6 * Q_d, 1.10 * Q_d, color="#E7E6E6", alpha=0.4,
                label="Zona de operación recomendada")

    # Líneas de referencia en el punto de diseño
    ax1.axvline(Q_d, color="#999999", ls=":", lw=0.8)
    ax1.axhline(P_d_cat, color="#999999", ls=":", lw=0.8)

    # Punto de diseño (catálogo)
    ax1.plot(Q_d, P_d_cat, "o", color="#C00000", ms=8, zorder=5)
    ax1.annotate(
        f"Punto de diseño (catálogo)\n{Q_d:,} m³/h @ {P_d_cat} Pa",
        xy=(Q_d, P_d_cat),
        xytext=(Q_d + 350, P_d_cat + 50),
        arrowprops=dict(arrowstyle="->", color="#C00000"),
        fontsize=9,
        color="#C00000",
    )

    # Punto en sitio
    ax1.plot(Q_d, P_d_sitio, "s", color="#70AD47", ms=7, zorder=5)
    ax1.annotate(
        f"Punto en sitio\n{Q_d:,} m³/h @ {P_d_sitio} Pa",
        xy=(Q_d, P_d_sitio),
        xytext=(Q_d + 350, P_d_sitio - 60),
        arrowprops=dict(arrowstyle="->", color="#70AD47"),
        fontsize=9,
        color="#70AD47",
    )

    ax1.set_xlim(0, 6200)
    ax1.set_ylim(0, 450)
    ax1.set_xlabel("Caudal $Q$ [m³/h]")
    ax1.set_ylabel("Presión total $\\Delta P$ [Pa]", color="#1F4E78")
    ax1.tick_params(axis="y", labelcolor="#1F4E78")
    ax1.set_title("Curva característica ilustrativa del ventilador axial tubeaxial PRFV\n"
                  "(punto de selección 3 840 m³/h @ 225 Pa catálogo, η = 0,55 provisional)")
    ax1.grid(True, alpha=0.3)

    # Eje secundario: potencia de eje teórica
    ax2 = ax1.twinx()
    ax2.plot(Q, P_eje_kw, color="#C00000", lw=1.8, ls="-.",
             label="Potencia de eje teórica (catálogo)")
    # Potencia de diseño
    P_d_eje = (Q_d / 3600) * P_d_cat / eta / 1000
    ax2.plot(Q_d, P_d_eje, "o", color="#C00000", ms=6, zorder=5)
    ax2.annotate(
        f"P ≈ {P_d_eje:.2f} kW",
        xy=(Q_d, P_d_eje),
        xytext=(Q_d - 1200, P_d_eje + 0.10),
        arrowprops=dict(arrowstyle="->", color="#C00000"),
        fontsize=8,
        color="#C00000",
    )
    ax2.set_ylim(0, 0.8)
    ax2.set_ylabel("Potencia de eje teórica $P$ [kW]", color="#C00000")
    ax2.tick_params(axis="y", labelcolor="#C00000")

    # Leyendas combinadas
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", fontsize=8)

    # Nota de validez
    fig.text(0.5, 0.01,
             "Curva ilustrativa/provisional. El tamaño/RPM/potencia final se confirma con el catálogo del fabricante seleccionado.",
             ha="center", fontsize=8, style="italic", color="#666666")

    fig.tight_layout(rect=[0, 0.04, 1, 1])
    out = IMG_DIR / "curva_ventilador_dts001.png"
    fig.savefig(out)
    plt.close(fig)
    return out


def generar_referencia():
    """Esquema de referencia del ventilador axial tubeaxial PRFV montado en
    muro/pasamuros, con motor fuera de la corriente de aire (transmisión por
    bandas). La imagen es una ilustración técnica propia, no una fotografía."""

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=120)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Colores corporativos
    azul = "#1F4E78"
    gris = "#E7E6E6"
    rojo = "#C00000"
    verde = "#70AD47"

    # Muro / pared (grueso)
    muro_x = 4.0
    muro_ancho = 0.6
    muro_altura = 4.5
    muro = Rectangle((muro_x, 0.5), muro_ancho, muro_altura,
                     facecolor=gris, edgecolor="#666666", linewidth=1.5, hatch="//")
    ax.add_patch(muro)
    ax.text(muro_x + muro_ancho / 2, 0.25, "MURO/PASAMUROS", ha="center",
            va="top", fontsize=9, color="#333333")

    # Carcasa tubular del ventilador (PRFV)
    carcasa_y = 2.8
    carcasa_largo = 2.2
    carcasa_diam = 0.9
    carcasa = FancyBboxPatch(
        (muro_x - carcasa_largo / 2 + muro_ancho / 2, carcasa_y - carcasa_diam / 2),
        carcasa_largo, carcasa_diam,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        facecolor="#B4C6E7", edgecolor=azul, linewidth=2.5
    )
    ax.add_patch(carcasa)

    # Rodete axial (lado interior)
    rodete_x = muro_x + muro_ancho / 2 + 0.35
    rodete = Circle((rodete_x, carcasa_y), 0.28, facecolor=azul, edgecolor="white", linewidth=1)
    ax.add_patch(rodete)
    # Álabes
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        x1 = rodete_x + 0.10 * math.cos(rad)
        y1 = carcasa_y + 0.10 * math.sin(rad)
        x2 = rodete_x + 0.26 * math.cos(rad)
        y2 = carcasa_y + 0.26 * math.sin(rad)
        ax.plot([x1, x2], [y1, y2], color="white", lw=1.5)

    # Guarda de seguridad (lado exterior)
    guarda_x = muro_x - carcasa_largo / 2 + muro_ancho / 2 - 0.15
    guarda = Circle((guarda_x, carcasa_y), 0.42, fill=False,
                    edgecolor=azul, linewidth=2, linestyle="--")
    ax.add_patch(guarda)
    ax.text(guarda_x, carcasa_y + 0.55, "Guarda", ha="center",
            fontsize=8, color=azul)

    # Motor fuera de la corriente de aire (arriba, con bandas)
    motor_x = muro_x + muro_ancho / 2 + 0.35
    motor_y = carcasa_y + 1.1
    motor = FancyBboxPatch(
        (motor_x - 0.35, motor_y - 0.20), 0.70, 0.40,
        boxstyle="round,pad=0.02,rounding_size=0.05",
        facecolor="#FFC000", edgecolor="#333333", linewidth=1.5
    )
    ax.add_patch(motor)
    ax.text(motor_x, motor_y, "MOTOR\nTEFC", ha="center", va="center",
            fontsize=8, color="#333333")

    # Poleas y bandas
    polea_motor = Circle((motor_x, motor_y - 0.30), 0.08, facecolor="#666666")
    polea_vent = Circle((motor_x, carcasa_y + 0.45), 0.08, facecolor="#666666")
    ax.add_patch(polea_motor)
    ax.add_patch(polea_vent)
    ax.plot([motor_x, motor_x], [motor_y - 0.30, carcasa_y + 0.45],
            color="#333333", lw=2)
    ax.text(motor_x + 0.25, carcasa_y + 0.75, "Bandas", fontsize=8, color="#333333")

    # Eje del ventilador
    ax.plot([muro_x + muro_ancho / 2 - 0.3, motor_x],
            [carcasa_y, carcasa_y], color="#333333", lw=3)

    # Flechas de flujo de aire
    # Exterior → interior
    ax.annotate("", xy=(rodete_x - 0.6, carcasa_y),
                xytext=(muro_x - 1.8, carcasa_y),
                arrowprops=dict(arrowstyle="->", color=verde, lw=2))
    ax.text(muro_x - 1.3, carcasa_y + 0.25, "Aire exterior", fontsize=9,
            color=verde, ha="center")

    ax.annotate("", xy=(muro_x + muro_ancho + 1.2, carcasa_y),
                xytext=(rodete_x + 0.3, carcasa_y),
                arrowprops=dict(arrowstyle="->", color=rojo, lw=2))
    ax.text(muro_x + muro_ancho + 0.8, carcasa_y + 0.25, "Descarga al\nlaboratorio",
            fontsize=9, color=rojo, ha="center")

    # Indicación de altura ~3 m
    ax.annotate("", xy=(muro_x + muro_ancho + 2.3, carcasa_y),
                xytext=(muro_x + muro_ancho + 2.3, 0.5),
                arrowprops=dict(arrowstyle="<->", color="#333333", lw=1))
    ax.text(muro_x + muro_ancho + 2.4, carcasa_y / 2 + 0.4,
            "~3,0 m\n(eje a piso)", fontsize=9, color="#333333", va="center")

    # Línea de piso
    ax.plot([0, 9], [0.5, 0.5], color="#333333", lw=1.5)

    # Título y notas
    ax.set_title("Esquema de montaje referencial — Ventilador axial tubeaxial PRFV\n"
                 "Aerovent FBD / equivalente (transmisión por bandas, motor fuera del aire corrosivo)",
                 fontsize=12, color=azul, pad=15)

    notas = (
        "Notas: 1) Montaje en muro/pasamuros; no en pared libre. "
        "2) El acceso para mantenimiento de bandas debe garantizarse a ~3,0 m de altura. "
        "3) Imagen ilustrativa; confirmar detalles con el fabricante seleccionado."
    )
    fig.text(0.5, 0.02, notas, ha="center", fontsize=8,
             style="italic", color="#666666")

    fig.tight_layout(rect=[0, 0.06, 1, 1])
    out = IMG_DIR / "ventilador_referencia_dts001.png"
    fig.savefig(out)
    plt.close(fig)
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

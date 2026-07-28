#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generar_img_dts001.py — Genera las imágenes auxiliares para la hoja de datos
P2437-HV-DTS-001 (ventilador axial mural Ø560 mm, transmisión directa):
curva característica ilustrativa y referencia del equipo.

La referencia del equipo es la imagen del montaje típico de planta
(Montaje/DISENOFINAL.png), copiada a build/dts/img/; la curva se genera con
matplotlib a partir del punto de diseño del proyecto.

Salida: build/dts/img/curva_ventilador_dts001.png
        build/dts/img/ventilador_referencia_dts001.png

Uso:  python scripts/generar_img_dts001.py
"""

import shutil
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "build" / "dts" / "img"
IMG_DIR.mkdir(parents=True, exist_ok=True)
DISENO_FINAL = ROOT / "Montaje" / "DISENOFINAL.png"


def generar_curva():
    """Curva característica ilustrativa de un ventilador axial tubular.

    Basada en los datos investigados del proyecto P2437:
      - Punto de selección (catálogo, ρ = 1.2 kg/m³): 3 840 m³/h @ 225 Pa
      - Punto equivalente en sitio (ρ = 0.88 kg/m³): 3 840 m³/h @ 165 Pa
      - Eficiencia axial provisional: η = 0.55
      - Forma parabólica típica de ventiladores axiales (murales/tubulares):
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
    ax1.set_title("Curva característica ilustrativa del ventilador axial mural Ø560 mm\n"
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
    """Copia la imagen del montaje típico de planta (Montaje/DISENOFINAL.png)
    como referencia del equipo para DTS-001 (ventilador axial mural
    Ø560 mm, transmisión directa, cubierta intemperie con banco de filtración,
    estructura de unión y malla de protección interior)."""

    out = IMG_DIR / "ventilador_referencia_dts001.png"
    if not DISENO_FINAL.exists():
        raise FileNotFoundError(
            f"No se encontró la imagen del montaje típico de planta: {DISENO_FINAL}"
        )
    shutil.copy2(DISENO_FINAL, out)
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

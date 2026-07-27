#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generar_curva_filtro_dts002.py — Curva ilustrativa ΔP vs. caudal del filtro
Camfil Durafil ES3 MERV-14/14A 24×24×12 in (DTS-002).

Fuente de datos: Camfil Drawing Durafil ES3 — ΔP inicial 0,31 in c.a. @ 500 fpm
(2 000 CFM) para MERV 14, 24×24 in. La curva se construye con ley cuadrática
ΔP ∝ Q² (flujo turbulento a través de medio poroso pleatado) y se corrige por
densidad del sitio (ρ = 0,88 kg/m³, k = 0,733).

Salida: build/dts/img/curva_filtro_dts002.png
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "build" / "dts" / "img" / "curva_filtro_dts002.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

# Factores de conversión
IN_WG_TO_PA = 249.088
CFM_TO_M3H = 1.69901

# Dato de catálogo: Durafil ES3 MERV 14, 24x24 in
Q_rated_cfm = 2000.0          # CFM @ 500 fpm
dp_init_inwg = 0.31           # in c.a. inicial
k_density = 0.733             # ρ_sitio / ρ_cat = 0.88 / 1.2

# Rango de caudal: 0 a 2500 CFM (máximo usable ~625 fpm × 4 ft²)
Q_cfm = np.linspace(0, 2600, 300)
Q_m3h = Q_cfm * CFM_TO_M3H

# Curva limpia catálogo y sitio (ley cuadrática)
dp_cat_inwg = dp_init_inwg * (Q_cfm / Q_rated_cfm) ** 2
dp_sitio_inwg = dp_cat_inwg * k_density

dp_cat_pa = dp_cat_inwg * IN_WG_TO_PA
dp_sitio_pa = dp_sitio_inwg * IN_WG_TO_PA

# Punto de diseño
Q_design_cfm = 2260.0
Q_design_m3h = Q_design_cfm * CFM_TO_M3H
dp_design_cat_pa = dp_init_inwg * (Q_design_cfm / Q_rated_cfm) ** 2 * IN_WG_TO_PA
dp_design_sitio_pa = dp_design_cat_pa * k_density

# Final de diseño congelado
dp_final_cat_pa = 210.0
dp_final_sitio_pa = dp_final_cat_pa * k_density

fig, ax1 = plt.subplots(figsize=(9, 6))

# Eje X inferior: CFM
ax1.set_xlabel("Caudal (CFM)", fontsize=11)
ax1.set_xlim(0, 2600)
ax1.set_xticks(np.arange(0, 2601, 500))

# Eje Y izquierdo: Pa
ax1.set_ylabel("Caída de presión ΔP (Pa)", color="tab:blue", fontsize=11)
ax1.plot(Q_cfm, dp_cat_pa, "b-", linewidth=2, label="Catálogo (ρ = 1,2 kg/m³)")
ax1.plot(Q_cfm, dp_sitio_pa, "r-", linewidth=2, label="Sitio Cajicá (ρ = 0,88 kg/m³, k = 0,733)")
ax1.axhline(dp_final_cat_pa, color="b", linestyle="--", alpha=0.6, label=f"ΔP final diseño catálogo = {dp_final_cat_pa:.0f} Pa")
ax1.axhline(dp_final_sitio_pa, color="r", linestyle="--", alpha=0.6, label=f"ΔP final diseño sitio = {dp_final_sitio_pa:.0f} Pa")
ax1.plot(Q_design_cfm, dp_design_cat_pa, "bo", markersize=8)
ax1.plot(Q_design_cfm, dp_design_sitio_pa, "ro", markersize=8)
ax1.annotate(f"Diseño\n{Q_design_m3h:.0f} m³/h\n{dp_design_sitio_pa:.0f} Pa sitio",
             xy=(Q_design_cfm, dp_design_sitio_pa),
             xytext=(Q_design_cfm - 450, dp_design_sitio_pa + 40),
             arrowprops=dict(arrowstyle="->", color="red"),
             fontsize=9)
ax1.tick_params(axis="y", labelcolor="tab:blue")
ax1.set_ylim(0, 260)
ax1.grid(True, linestyle="--", alpha=0.5)
ax1.legend(loc="upper left", fontsize=9)

# Eje X superior: m³/h
ax2 = ax1.twiny()
ax2.set_xlim(0, 2600 * CFM_TO_M3H)
ax2.set_xticks(np.arange(0, 2601, 500) * CFM_TO_M3H)
ax2.set_xticklabels([f"{x:.0f}" for x in np.arange(0, 2601, 500) * CFM_TO_M3H])
ax2.set_xlabel("Caudal (m³/h)", fontsize=11)

# Eje Y derecho: in c.a.
ax3 = ax1.twinx()
ax3.set_ylabel("ΔP (in c.a.)", color="tab:green", fontsize=11)
ax3.set_ylim(0, 260 / IN_WG_TO_PA)
ax3.tick_params(axis="y", labelcolor="tab:green")

plt.title("Curva ilustrativa ΔP vs. caudal — Filtro Camfil Durafil ES3 MERV-14/14A\n24×24×12 in (DTS-002)", fontsize=12)
plt.tight_layout()
plt.savefig(OUT, dpi=150)
print(f"Curva guardada en: {OUT}")

"""Memoria de cálculo MC-001 — PLANTILLA.

Flujo de uso:
    1. Leer bases de diseño desde ``00_bases_diseno/bases_diseno.yaml``.
    2. Ejecutar los cálculos.
    3. Exportar a Excel DML en ``05_memorias_excel/`` y figuras a ``02_informe_tex/assets/``.

Ejecutar:
    uv run 01_calculos/memorias/MC-001_template.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "01_calculos"))

from src import bases, hidraulica, propiedades  # noqa: E402


def main() -> None:
    bd = bases.load()
    fluido = bd["fluidos"][0]["coolprop_id"]

    # Ejemplo: caída de presión en tubería de 100 m, DN 100
    T_K = 25 + 273.15
    P_Pa = 2e5
    v = 2.0
    D = 0.1
    L = 100.0
    epsilon = 4.6e-5  # acero comercial, Crane TP-410

    rho = propiedades.densidad(fluido, T_K, P_Pa)
    mu = propiedades.viscosidad(fluido, T_K, P_Pa)
    Re = hidraulica.reynolds(rho, v, D, mu)
    f = hidraulica.factor_friccion_churchill(Re, epsilon / D)
    dp = hidraulica.perdida_carga(f, L, D, rho, v)

    print(f"Fluido          : {fluido}")
    print(f"Re              : {Re:.3e}")
    print(f"f (Darcy)       : {f:.4f}")
    print(f"ΔP (100 m)      : {dp/1e3:.2f} kPa")


if __name__ == "__main__":
    main()

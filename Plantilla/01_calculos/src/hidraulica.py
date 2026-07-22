"""Cálculos hidráulicos — pérdidas por fricción y régimen de flujo.

Referencias:
- Darcy–Weisbach: Crane TP-410 (2018).
- Colebrook–White: J. Inst. Civ. Eng. 11:133–156 (1939).
- Churchill (explícito, todo régimen): Chem. Eng. 84(24):91–92 (1977).
"""
from __future__ import annotations

import math


def reynolds(rho: float, v: float, D: float, mu: float) -> float:
    """Número de Reynolds [-]. Inputs en SI (kg/m³, m/s, m, Pa·s)."""
    return rho * v * D / mu


def factor_friccion_churchill(Re: float, epsilon_D: float) -> float:
    """Factor de fricción de Darcy — correlación de Churchill (1977).

    Válida en todo el rango Re (laminar, transición y turbulento).
    ``epsilon_D`` = rugosidad relativa (ε/D) [-].
    """
    A = (2.457 * math.log(1.0 / ((7.0 / Re) ** 0.9 + 0.27 * epsilon_D))) ** 16
    B = (37530.0 / Re) ** 16
    return 8.0 * ((8.0 / Re) ** 12 + 1.0 / (A + B) ** 1.5) ** (1.0 / 12.0)


def perdida_carga(
    f: float, L: float, D: float, rho: float, v: float
) -> float:
    """Caída de presión por fricción [Pa] — Darcy–Weisbach."""
    return f * (L / D) * (rho * v**2 / 2.0)

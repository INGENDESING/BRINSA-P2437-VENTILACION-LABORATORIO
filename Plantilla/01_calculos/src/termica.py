"""Transferencia de calor — coeficientes convectivos y balances.

Referencias:
- Dittus–Boelter: Univ. Calif. Publ. Eng. 2:443 (1930).
- Gnielinski: Int. Chem. Eng. 16:359–368 (1976).
- TEMA 10ª ed. (2019) para diseño de intercambiadores de casco y tubo.
"""
from __future__ import annotations


def nusselt_dittus_boelter(Re: float, Pr: float, *, calentando: bool = True) -> float:
    """Nu para flujo turbulento en tubo (Re > 10 000, 0.7 < Pr < 160, L/D > 10).

    Exponente n = 0.4 si el fluido se calienta, 0.3 si se enfría.
    """
    n = 0.4 if calentando else 0.3
    return 0.023 * Re**0.8 * Pr**n


def nusselt_gnielinski(Re: float, Pr: float, f: float) -> float:
    """Nu de Gnielinski — más precisa que Dittus–Boelter (3000 < Re < 5e6)."""
    return (f / 8.0) * (Re - 1000.0) * Pr / (1.0 + 12.7 * (f / 8.0) ** 0.5 * (Pr ** (2 / 3) - 1.0))


def coeficiente_pelicula(Nu: float, k: float, D: float) -> float:
    """h = Nu·k/D [W/(m²·K)]."""
    return Nu * k / D

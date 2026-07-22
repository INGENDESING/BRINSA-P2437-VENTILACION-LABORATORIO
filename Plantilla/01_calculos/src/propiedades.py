"""Propiedades termofísicas — wrapper sobre CoolProp con unidades SI.

Todas las funciones reciben y devuelven magnitudes en SI (K, Pa, kg/m³, J/kg·K, Pa·s).
Fuente primaria: CoolProp 6.x (Bell et al., 2014, Ind. Eng. Chem. Res. 53:2498).
Para fluidos fuera del alcance de CoolProp, consultar DIPPR/NIST y citar explícitamente.
"""
from __future__ import annotations

from CoolProp.CoolProp import PropsSI


def densidad(fluido: str, T_K: float, P_Pa: float) -> float:
    """Densidad [kg/m³]."""
    return PropsSI("D", "T", T_K, "P", P_Pa, fluido)


def viscosidad(fluido: str, T_K: float, P_Pa: float) -> float:
    """Viscosidad dinámica [Pa·s]."""
    return PropsSI("V", "T", T_K, "P", P_Pa, fluido)


def cp(fluido: str, T_K: float, P_Pa: float) -> float:
    """Capacidad calorífica a presión constante [J/(kg·K)]."""
    return PropsSI("C", "T", T_K, "P", P_Pa, fluido)


def conductividad(fluido: str, T_K: float, P_Pa: float) -> float:
    """Conductividad térmica [W/(m·K)]."""
    return PropsSI("L", "T", T_K, "P", P_Pa, fluido)


def presion_saturacion(fluido: str, T_K: float) -> float:
    """Presión de saturación [Pa]."""
    return PropsSI("P", "T", T_K, "Q", 0, fluido)

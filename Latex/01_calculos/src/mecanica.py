"""Diseño mecánico — recipientes a presión (ASME VIII Div.1).

Referencias:
- ASME BPVC Sec. VIII Div.1, ed. 2023, UG-27 (cáscara cilíndrica).
- ASME BPVC Sec. VIII Div.1, UG-32 (cabezales).
"""
from __future__ import annotations


def espesor_casco_cilindrico(P_MPa: float, R_mm: float, S_MPa: float, E: float = 1.0) -> float:
    """Espesor mínimo por presión interna (ASME VIII Div.1, UG-27(c)(1)) [mm].

    t = P·R / (S·E − 0.6·P). Válido para t < R/2 y P < 0.385·S·E.
    """
    denom = S_MPa * E - 0.6 * P_MPa
    if denom <= 0:
        raise ValueError("Presión supera el rango de validez de UG-27(c)(1). Usar UG-27(c)(2) o Div.2.")
    return P_MPa * R_mm / denom


def espesor_cabeza_toriesferica(P_MPa: float, D_mm: float, S_MPa: float, E: float = 1.0, M: float = 1.54) -> float:
    """Espesor de cabezal toriesférico (ASME VIII Div.1, UG-32(e)) [mm].

    ``M`` = factor por geometría (1.54 para relación L/r = 16.67, típico F&D).
    """
    return P_MPa * D_mm * M / (2.0 * S_MPa * E - 0.2 * P_MPa)

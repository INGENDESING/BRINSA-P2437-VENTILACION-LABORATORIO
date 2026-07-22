"""Verificación hidráulica — benchmarks Crane TP-410."""
import pytest

from src.hidraulica import factor_friccion_churchill, perdida_carga, reynolds


def test_reynolds_simple():
    # v=2 m/s, D=0.1 m, ρ=1000, μ=1e-3 → Re=2e5
    assert reynolds(1000, 2.0, 0.1, 1e-3) == pytest.approx(2e5)


def test_churchill_vs_colebrook_turbulento():
    # Re=1e5, ε/D=0.001 → f ≈ 0.0225 (Moody)
    f = factor_friccion_churchill(1e5, 1e-3)
    assert f == pytest.approx(0.0225, rel=3e-2)


def test_perdida_carga_dimensional():
    # ΔP = f·(L/D)·ρv²/2, unidades SI → Pa
    dp = perdida_carga(0.02, 100.0, 0.1, 1000.0, 2.0)
    # 0.02·1000·1000·4/2 = 40 000 Pa
    assert dp == pytest.approx(40_000)

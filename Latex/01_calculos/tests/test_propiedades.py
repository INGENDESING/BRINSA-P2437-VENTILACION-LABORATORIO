"""Verificación de propiedades contra valores tabulados NIST."""
import pytest

from src.propiedades import cp, densidad, viscosidad


def test_densidad_agua_25C_1atm():
    # NIST WebBook: ρ(25 °C, 101.325 kPa) = 997.05 kg/m³
    rho = densidad("Water", 298.15, 101_325)
    assert rho == pytest.approx(997.05, rel=1e-3)


def test_viscosidad_agua_25C():
    # NIST: μ = 8.9e-4 Pa·s
    mu = viscosidad("Water", 298.15, 101_325)
    assert mu == pytest.approx(8.9e-4, rel=2e-2)


def test_cp_agua_25C():
    # NIST: cp ≈ 4181 J/(kg·K)
    assert cp("Water", 298.15, 101_325) == pytest.approx(4181, rel=1e-2)

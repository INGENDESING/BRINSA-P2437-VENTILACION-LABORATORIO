"""Generador de dashboards HTML autocontenidos (Plotly + Jinja2).

Uso:
    uv run 03_dashboards_html/build_dashboard.py

Produce un HTML offline con KPIs y figuras Plotly embebidas, aplicando identidad DML.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import plotly.graph_objects as go
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "01_calculos"))

from src import bases  # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = HERE / "resultados_parametricos.html"


def _fig_to_json(fig: go.Figure) -> dict[str, str]:
    as_dict = fig.to_plotly_json()
    return {"data": json.dumps(as_dict["data"]), "layout": json.dumps(as_dict.get("layout", {}))}


def render() -> Path:
    bd = bases.load()
    env = Environment(loader=FileSystemLoader(HERE / "templates"), autoescape=True)
    tpl = env.get_template("dashboard.html.j2")

    # Figura ejemplo — reemplazar por resultados reales
    fig = go.Figure(
        data=[go.Scatter(x=[0, 1, 2, 3], y=[0, 1, 4, 9], mode="lines+markers", name="Ejemplo")]
    )
    fig.update_layout(title="Figura ejemplo", xaxis_title="x", yaxis_title="y")

    html = tpl.render(
        titulo="Dashboard de resultados",
        proyecto_codigo=bd["proyecto"]["codigo"],
        cliente=bd["proyecto"]["cliente"],
        revision=bd["proyecto"]["revision"],
        fecha=date.today().isoformat(),
        kpis=[
            {"label": "ΔP tubería", "valor": "— kPa"},
            {"label": "Re", "valor": "—"},
            {"label": "Espesor casco", "valor": "— mm"},
        ],
        figuras=[_fig_to_json(fig)],
    )
    OUT.write_text(html, encoding="utf-8")
    return OUT


if __name__ == "__main__":
    path = render()
    print(f"Dashboard generado: {path}")

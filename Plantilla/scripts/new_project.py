"""Bootstrap de un proyecto DML a partir de la plantilla MASTER.

Uso:
    python scripts/new_project.py P2601 "Bavaria" "Rediseño línea CIP tanque T-101"

Clona la plantilla a ``../P2601-BAV-REDISENO_CIP/``, reemplaza códigos en LaTeX/YAML
y pre-pobla ``bases_diseno.yaml`` y ``contexto.md`` con los metadatos.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

PLANTILLA = Path(__file__).resolve().parents[1]
EXCLUDE = {".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "06_entregables"}


def _copy_tree(src: Path, dst: Path) -> None:
    def _ignore(_d: str, names: list[str]) -> list[str]:
        return [n for n in names if n in EXCLUDE or n.endswith((".aux", ".log", ".out", ".toc"))]

    shutil.copytree(src, dst, ignore=_ignore)


def _slug(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9\s]+", "", s).strip()
    return re.sub(r"\s+", "_", s).upper()[:30]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("codigo", help="Código DML (ej. P2601)")
    ap.add_argument("cliente", help="Cliente (ej. Bavaria)")
    ap.add_argument("proyecto", help="Nombre del proyecto")
    ap.add_argument("--dest", type=Path, default=None, help="Carpeta destino (default: ../)")
    args = ap.parse_args()

    slug = f"{args.codigo}-{_slug(args.cliente)[:3]}-{_slug(args.proyecto)}"
    dest = (args.dest or PLANTILLA.parent) / slug
    if dest.exists():
        print(f"ERROR: {dest} ya existe.", file=sys.stderr)
        return 1

    _copy_tree(PLANTILLA, dest)

    # Reemplazos clave
    yaml_path = dest / "00_bases_diseno" / "bases_diseno.yaml"
    txt = yaml_path.read_text(encoding="utf-8")
    txt = txt.replace('codigo: "P25XX"', f'codigo: "{args.codigo}"')
    txt = txt.replace('nombre: "PLANTILLA MASTER"', f'nombre: "{args.proyecto}"')
    txt = txt.replace('cliente: "CLIENTE"', f'cliente: "{args.cliente}"')
    txt = txt.replace('fecha_emision: "AAAA-MM-DD"', f'fecha_emision: "{date.today().isoformat()}"')
    yaml_path.write_text(txt, encoding="utf-8")

    # contexto.md inicial
    ctx = dest / "contexto.md"
    ctx.write_text(
        f"""# Contexto del proyecto: {args.codigo} — {args.proyecto}

## Estado actual
- Cliente: {args.cliente}
- Última tarea completada: Bootstrap de plantilla.
- Próxima tarea pendiente: Completar `00_bases_diseno/bases_diseno.yaml`.
- Fecha de última actualización: {date.today().isoformat()}

## Bases de diseño congeladas
Pendiente — ver `00_bases_diseno/bases_diseno.yaml`.

## Decisiones de diseño clave
(Por documentar)

## Archivos clave
- `00_bases_diseno/bases_diseno.yaml` — fuente única de propiedades y condiciones.
- `01_calculos/memorias/` — memorias ejecutables.
- `02_informe_tex/` — informe técnico LaTeX.
- `03_dashboards_html/` — dashboards interactivos.

## Preguntas abiertas
- [ ] (pendiente)

## Comandos útiles
- `uv sync` — instalar dependencias Python.
- `uv run pytest` — ejecutar tests.
- `uv run 03_dashboards_html/build_dashboard.py` — regenerar dashboard.
""",
        encoding="utf-8",
    )

    print(f"Proyecto creado en: {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

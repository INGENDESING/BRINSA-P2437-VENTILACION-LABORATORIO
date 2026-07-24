"""Carga centralizada de bases de diseño desde YAML."""
from __future__ import annotations

from functools import lru_cache
from typing import Any

import yaml

from . import BASES_YAML


@lru_cache(maxsize=1)
def load() -> dict[str, Any]:
    with BASES_YAML.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def get(path: str, default: Any = None) -> Any:
    """Accede a claves anidadas por ruta separada por puntos: ``get('operacion.presion_diseno_barg')``."""
    node: Any = load()
    for key in path.split("."):
        if not isinstance(node, dict) or key not in node:
            return default
        node = node[key]
    return node

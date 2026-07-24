#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
emitir.py — Genera/actualiza la carpeta Emisiones/ del proyecto P2437.

En una sola orden:
  1. Regenera la memoria de cálculo Excel (generar_excel.py).
  2. Genera las hojas de datos DTS en Excel (scripts/generar_dts.py -> build/dts/).
  3. Recompila los informes LaTeX INF-001 e INF-002 (pdflatex -> bibtex -> pdflatex x2).
  4. Copia los entregables a Emisiones/ con nombres codificados GP-N-09 y retira obsoletos.
  5. Escribe Emisiones/MANIFIESTO_EMISION.md con la trazabilidad de la emisión.

Regla de flujo: las FUENTES se editan (Latex/02_informe_tex, generar_excel.py,
Investigacion/Sistemas); las EMISIONES se regeneran con este script. Nunca editar
a mano los archivos dentro de Emisiones/.

Uso:  python scripts/emitir.py
"""

import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEX_DIR = ROOT / "Latex" / "02_informe_tex"
EMISIONES = ROOT / "Emisiones"

# (origen relativo a ROOT, subcarpeta de Emisiones, nombre emitido)
ENTREGABLES = [
    ("Latex/02_informe_tex/P2437-HV-INF-001 REV0.pdf", "1.0 HV-INFORMES", "P2437-HV-INF-001 REV0.pdf"),
    ("Latex/02_informe_tex/P2437-HV-INF-002 REV0.pdf", "1.0 HV-INFORMES", "P2437-HV-INF-002 REV0.pdf"),
    ("memoriadecalculo.xlsx", "2.0 HV-MEMORIAS DE CALCULO", "P2437-HV-CAL-001 REV0.xlsx"),
    ("build/dts/P2437-HV-DTS-001 REV0.xlsx", "3.0 HV-HOJAS DE DATOS", "P2437-HV-DTS-001 REV0.xlsx"),
    ("build/dts/P2437-HV-DTS-002 REV0.xlsx", "3.0 HV-HOJAS DE DATOS", "P2437-HV-DTS-002 REV0.xlsx"),
    ("build/dts/P2437-HV-DTS-003 REV0.xlsx", "3.0 HV-HOJAS DE DATOS", "P2437-HV-DTS-003 REV0.xlsx"),
    ("build/dts/P2437-IC-DTS-001 REV0.xlsx", "3.0 HV-HOJAS DE DATOS", "P2437-IC-DTS-001 REV0.xlsx"),
    ("Investigacion/Sistemas/listado_equipos.md", "4.0 HV-LISTADOS", "P2437-HV-LIS-001 REV0.md"),
]

# Versiones antiguas en formato .md que deben retirarse de la emisión
OBSOLETOS = [
    ("3.0 HV-HOJAS DE DATOS", "P2437-HV-DTS-001 REV0.md"),
    ("3.0 HV-HOJAS DE DATOS", "P2437-HV-DTS-002 REV0.md"),
    ("3.0 HV-HOJAS DE DATOS", "P2437-HV-DTS-003 REV0.md"),
    ("3.0 HV-HOJAS DE DATOS", "P2437-IC-DTS-001 REV0.md"),
]

INFORMES = ["P2437-HV-INF-001 REV0", "P2437-HV-INF-002 REV0"]

errores = []


def run(cmd, cwd):
    print(f"  $ {' '.join(cmd)}")
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r


def compilar_informe(jobname):
    """Secuencia pdflatex -> bibtex (si hay citas) -> pdflatex x2. Exige 0 errores."""
    print(f"[LaTeX] {jobname}")
    base = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", jobname]
    r = run(base, TEX_DIR)
    if r.returncode != 0:
        errores.append(f"pdflatex falló en {jobname} (primera pasada)")
        return
    aux = TEX_DIR / f"{jobname}.aux"
    if aux.exists() and "\\citation" in aux.read_text(encoding="utf-8", errors="ignore"):
        run(["bibtex", jobname], TEX_DIR)
    for _ in range(2):
        r = run(base, TEX_DIR)
        if r.returncode != 0:
            errores.append(f"pdflatex falló en {jobname} (pasadas finales)")
            return
    log = TEX_DIR / f"{jobname}.log"
    if log.exists():
        contenido = log.read_text(encoding="utf-8", errors="ignore")
        n_errores = len(re.findall(r"^!", contenido, flags=re.M))
        citas = re.findall(r"Citation .* undefined", contenido)
        if n_errores:
            errores.append(f"{jobname}: {n_errores} errores en el log")
        if citas:
            errores.append(f"{jobname}: {len(set(citas))} citas sin resolver")
        print(f"  -> 0 errores forzados, {n_errores} en log, citas sin resolver: {len(set(citas))}")


def main():
    print("== EMISIÓN DE ENTREGABLES P2437 ==")

    # 1. Regenerar Excel
    print("[1/5] Regenerando memoria de cálculo Excel")
    r = run([sys.executable, "generar_excel.py"], ROOT)
    if r.returncode != 0:
        errores.append("generar_excel.py falló")
        print(r.stdout[-2000:])

    # 2. Generar hojas de datos DTS (build/dts/*.xlsx desde los .md)
    print("[2/5] Generando hojas de datos DTS")
    r = run([sys.executable, "scripts/generar_dts.py"], ROOT)
    if r.returncode != 0:
        errores.append("generar_dts.py falló")
        print(r.stdout[-2000:])

    # 3. Compilar informes
    print("[3/5] Compilando informes LaTeX")
    for job in INFORMES:
        if (TEX_DIR / f"{job}.tex").exists():
            compilar_informe(job)
        else:
            print(f"  (omito {job}: no existe el .tex)")

    # 4. Copiar entregables
    print("[4/5] Copiando entregables a Emisiones/")
    copiados = []
    for src_rel, sub, nombre in ENTREGABLES:
        src = ROOT / src_rel
        dst_dir = EMISIONES / sub
        dst_dir.mkdir(parents=True, exist_ok=True)
        if not src.exists():
            errores.append(f"Fuente no encontrada: {src_rel}")
            continue
        shutil.copy2(src, dst_dir / nombre)
        copiados.append((sub, nombre, src_rel))
        print(f"  {sub}/{nombre}")

    # Retirar versiones obsoletas (.md reemplazados por .xlsx)
    for sub, nombre in OBSOLETOS:
        viejo = EMISIONES / sub / nombre
        if viejo.exists():
            viejo.unlink()
            print(f"  (retirado obsoleto: {sub}/{nombre})")

    # 5. Manifiesto
    print("[5/5] Escribiendo manifiesto")
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M")
    lineas = [
        "# Manifiesto de emisión — Proyecto P2437",
        "",
        f"Fecha de emisión: {ahora}",
        "Generado automáticamente por `scripts/emitir.py`. No editar a mano.",
        "",
        "| Carpeta | Archivo emitido | Fuente |",
        "| --- | --- | --- |",
    ]
    for sub, nombre, src_rel in copiados:
        lineas.append(f"| {sub} | {nombre} | `{src_rel}` |")
    lineas += [
        "",
        "Regla de flujo: las fuentes se editan; las emisiones se regeneran con",
        "`python scripts/emitir.py`. Los archivos de esta carpeta son copias.",
    ]
    (EMISIONES / "MANIFIESTO_EMISION.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")

    print()
    if errores:
        print("EMISIÓN CON ERRORES:")
        for e in errores:
            print(f"  - {e}")
        sys.exit(1)
    print(f"EMISIÓN OK: {len(copiados)} entregables actualizados.")


if __name__ == "__main__":
    main()

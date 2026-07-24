#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generar_lis_pdf.py — Genera una versión PDF del listado de equipos BOQ a partir
de `Investigacion/Sistemas/listado_equipos.md`.

Usa LaTeX (pdflatex) para compilar una tabla larga (`longtable`) en formato
horizontal (landscape), replicando el contenido del Excel LIS con un estilo
limpio y profesional.

Salida: build/lis/P2437-HV-LIS-001 REV0.pdf

Uso:  python scripts/generar_lis_pdf.py
"""

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD_FUENTE = ROOT / "Investigacion" / "Sistemas" / "listado_equipos.md"
SALIDA = ROOT / "build" / "lis"
CODIGO = "P2437-HV-LIS-001"
TITULO = "LISTADO DE EQUIPOS Y MATERIALES (BOQ)"
SUBTITULO = "Sistema de ventilación y presurización positiva — Laboratorio de análisis industrial BRINSA, Cajicá (Cundinamarca)"


def limpiar_tex(texto):
    """Escapa caracteres LaTeX, convierte markdown básico y traduce caracteres
    Unicode no soportados por pdflatex a comandos LaTeX."""
    # Enlaces [texto](url) -> texto (url)
    texto = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', texto)
    # Negritas markdown
    texto = texto.replace('**', '')
    # Código inline
    texto = texto.replace('`', '')
    # Caracteres Unicode -> comandos LaTeX
    reemplazos = {
        'ρ': r'$\rho$',
        '³': r'\textsuperscript{3}',
        '²': r'\textsuperscript{2}',
        '≡': r'$\equiv$',
        'Δ': r'$\Delta$',
        'δ': r'$\delta$',
        '×': r'$\times$',
        '°': r'$^\circ$',
        '≤': r'$\leq$',
        '≥': r'$\geq$',
        '±': r'$\pm$',
        '–': r'--',
        '—': r'---',
        '’': r"'",
        '‘': r"'",
        '“': r'``',
        '”': r"''",
        '…': r'\ldots{}',
        'Á': r"\\'A",
        'É': r"\\'E",
        'Í': r"\\'I",
        'Ó': r"\\'O",
        'Ú': r"\\'U",
        'á': r"\\'a",
        'é': r"\\'e",
        'í': r"\\'i",
        'ó': r"\\'o",
        'ú': r"\\'u",
        'ñ': r"\\~n",
        'Ñ': r"\\~N",
        'ü': r"\\\"u",
        'Ü': r"\\\"U",
    }
    for k, v in reemplazos.items():
        texto = texto.replace(k, v)
    # Caracteres reservados de LaTeX (escapar backslash primero con marcador)
    texto = texto.replace('\\', '\x00BACKSLASH\x00')
    reservados = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    for k, v in reservados.items():
        texto = texto.replace(k, v)
    texto = texto.replace('\x00BACKSLASH\x00', r'\textbackslash{}')
    return texto.strip()


def es_separador_tabla(celdas):
    return all(re.fullmatch(r':?-{2,}:?', c.strip()) for c in celdas if c.strip()) \
        and any(c.strip() for c in celdas)


def parsear_linea_tabla(linea):
    return [limpiar_tex(c) for c in linea.strip().strip('|').split('|')]


def extraer_tabla(md):
    """Extrae el bloque de tabla BOQ del markdown."""
    lineas = md.splitlines()
    bloque = []
    en_tabla = False
    for ln in lineas:
        if ln.strip().startswith('|'):
            celdas = ln.strip().strip('|').split('|')
            if es_separador_tabla(celdas):
                continue
            bloque.append(parsear_linea_tabla(ln))
            en_tabla = True
        elif en_tabla:
            break
    return bloque


def extraer_notas(md):
    """Extrae los párrafos de notas (sección 3)."""
    lineas = md.splitlines()
    notas = []
    en_notas = False
    for ln in lineas:
        if ln.strip().startswith('## 3.'):
            en_notas = True
            continue
        if en_notas:
            if ln.strip().startswith('##'):
                break
            if ln.strip():
                notas.append(limpiar_tex(ln.strip()))
    return notas


def construir_tex(filas, notas):
    encabezado = " & ".join(filas[0]) if filas else ""
    cuerpo = r" \\" + "\n" + r"\midrule" + "\n"
    cuerpo = cuerpo.join(
        " & ".join(celdas) for celdas in filas[1:]
    )
    notas_tex = "\n\n".join(f"\\noindent \\textbf{{{i+1}.}} {n}" for i, n in enumerate(notas))

    tex = r"""\documentclass[11pt,a4paper,landscape]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish]{babel}
\usepackage{geometry}
\geometry{left=1.5cm, right=1.5cm, top=2cm, bottom=2cm}
\usepackage{longtable}
\usepackage{array}
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage{colortbl}
\usepackage{hyperref}
\usepackage{xurl}
\usepackage{fancyhdr}
\usepackage{lastpage}

\definecolor{headerblue}{RGB}{31,78,120}
\definecolor{lightgray}{RGB}{245,245,245}

\hypersetup{colorlinks=true, linkcolor=blue, urlcolor=blue}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{""" + CODIGO + r"""}
\fancyhead[C]{""" + TITULO + r"""}
\fancyhead[R]{P\'{a}g. \thepage\ de \pageref{LastPage}}
\renewcommand{\headrulewidth}{0.4pt}

\begin{document}

\begin{center}
{\Large\bfseries """ + TITULO + r"""}\\[0.3em]
{\large """ + SUBTITULO + r"""}\\[0.5em]
\textbf{C\'{o}digo:} """ + CODIGO + r""" \quad \textbf{Revisi\'{o}n:} 0 \quad \textbf{Fecha:} 2026-07-24
\end{center}

\vspace{0.5cm}

\renewcommand{\arraystretch}{1.3}
\begin{longtable}{|
    >{\centering\arraybackslash}p{0.6cm}|
    >{\raggedright\arraybackslash}p{2.2cm}|
    >{\raggedright\arraybackslash}p{4.5cm}|
    >{\raggedright\arraybackslash}p{3.2cm}|
    >{\centering\arraybackslash}p{1.0cm}|
    >{\raggedright\arraybackslash}p{4.5cm}|
    >{\raggedright\arraybackslash}p{4.5cm}|
}
\hline
\rowcolor{headerblue}
\textcolor{white}{\textbf{""" + filas[0][0] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][1] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][2] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][3] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][4] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][5] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][6] + r"""}} \\
\hline
\endfirsthead
\hline
\rowcolor{headerblue}
\textcolor{white}{\textbf{""" + filas[0][0] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][1] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][2] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][3] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][4] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][5] + r"""}} &
\textcolor{white}{\textbf{""" + filas[0][6] + r"""}} \\
\hline
\endhead
\midrule
""" + cuerpo + r"""
\\\midrule
\end{longtable}

\vspace{0.5cm}

\section*{Notas de suministro}
""" + notas_tex + r"""

\end{document}
"""
    return tex


def main():
    print("== GENERACIÓN DE PDF DEL LISTADO DE EQUIPOS (LIS) ==")
    md = MD_FUENTE.read_text(encoding='utf-8')
    filas = extraer_tabla(md)
    if not filas or len(filas) < 2:
        raise ValueError("No se encontró la tabla BOQ en el markdown fuente")
    notas = extraer_notas(md)

    tex = construir_tex(filas, notas)
    SALIDA.mkdir(parents=True, exist_ok=True)
    tex_path = SALIDA / f"{CODIGO} REV0.tex"
    pdf_path = SALIDA / f"{CODIGO} REV0.pdf"
    tex_path.write_text(tex, encoding='utf-8')

    r = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", str(tex_path.name)],
        cwd=SALIDA,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0:
        log_path = SALIDA / f"{CODIGO} REV0.log"
        log_path.write_text(
            (r.stdout or "") + "\n--- STDERR ---\n" + (r.stderr or ""),
            encoding="utf-8",
            errors="replace",
        )
        print(f"  ERROR: pdflatex falló. Log guardado en {log_path.relative_to(ROOT)}")
        raise RuntimeError("pdflatex falló al compilar el PDF del LIS")

    # Segunda pasada por si hay referencias
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", str(tex_path.name)],
        cwd=SALIDA,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if not pdf_path.exists():
        raise RuntimeError("El PDF no fue generado")

    print(f"  TEX  -> {tex_path.relative_to(ROOT)}")
    print(f"  PDF  -> {pdf_path.relative_to(ROOT)}")
    print("OK: PDF del LIS generado.")


if __name__ == "__main__":
    main()

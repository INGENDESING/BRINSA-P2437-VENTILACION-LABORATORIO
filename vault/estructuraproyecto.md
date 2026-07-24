---
fecha: 2026-07-23
tags: [estructura]
---

# Estructura del proyecto

Árbol de archivos y carpetas de `Calculos/` (raíz del proyecto HVAC Laboratorio Brinsa).
Se omiten `.git/`, `vault/.obsidian/` y artefactos de compilación LaTeX
(`*.aux`, `*.log`, `*.out`, `*.toc`, `*.lof`, `*.lot`, `*.spl`, `*.bbl`, `*.blg`).

```
Calculos/
├── AGENTS.md                        # Archivo director del agente (rol, fases, estándares)
├── contexto.md                      # Resumen rápido de sesión (el detalle vive en vault/)
├── .gitignore
├── generar_excel.py                 # Generador openpyxl de la memoria de cálculo
├── memoriadecalculo.xlsx            # Memoria de cálculo con fórmulas vivas
│                                     # (el informe canónico es Latex/02_informe_tex)
│
├── .agents/
│   └── skills/
│       └── obsidian-vault/SKILL.md  # Skill que mantiene este vault
│
├── vault/                           # Vault de Obsidian — memoria a largo plazo
│   ├── 00_Inicio.md                 # Índice (MOC)
│   ├── 01_Estado actual.md
│   ├── 02_Bases de diseño congeladas.md
│   ├── 03_Decisiones/               # Una nota por decisión de diseño
│   ├── 04_Bitácora/                 # Una nota por sesión de trabajo
│   ├── 05_Preguntas abiertas.md
│   ├── 06_Archivos clave.md
│   ├── 07_Workflows.md
│   ├── estructuraproyecto.md        # Este documento
│   └── 99_Plantillas/               # Plantillas de decisión y bitácora
│
├── docs/                            # Dashboard web estático (GitHub Pages)
│   ├── index.html
│   ├── app.js
│   └── styles.css
│
├── HojasDatos/
│   └── P2437-PR-DT-001.xlsx         # Hoja de datos del equipo
│
├── resultado simulaciones/          # Capturas de resultados CFD
│   ├── Case 1.png
│   └── Case 2.png
│
├── task/
│   └── todo.md                      # Plan de tareas de la sesión (fase 1 de AGENTS.md)
│
├── Codificacion/
│   ├── GP-N-09.docx                 # Norma DML de normalización/codificación
│   └── codificacion.md              # Codificación GP-N-09 de los documentos P2437
│
├── Emisiones/                       # Entregables codificados (copias generadas
│   ├── 1.0 HV-INFORMES/             #   por scripts/emitir.py — no editar a mano)
│   ├── 2.0 HV-MEMORIAS DE CALCULO/
│   ├── 3.0 HV-HOJAS DE DATOS/
│   ├── 4.0 HV-LISTADOS/
│   └── MANIFIESTO_EMISION.md
│
├── scripts/
│   ├── emitir.py                    # Orquesta la emisión completa a Emisiones/
│   └── generar_dts.py               # Convierte las HD .md a Excel corporativo (build/dts/)
│
├── build/
│   └── dts/                         # Intermedios .xlsx de las hojas de datos
│
├── FormatosDocumentos/              # Plantillas corporativas obligatorias
│   ├── CAL.xlsx                     #   (memorias de cálculo)
│   └── DTS.xlsx                     #   (hojas de datos)
│
├── Investigacion/                   # Investigación de sistemas (2026-07-23)
│   └── Sistemas/
│       ├── informe_investigacion.md # Informe: sistema, componentes, normas, selección
│       ├── listado_equipos.md       # BOQ: 17 ítems con candidatos comerciales
│       └── hojas_datos/
│           ├── HD-VENT-001_ventilador.md
│           ├── HD-FILT-001_filtro_merv.md
│           ├── HD-REJ-001_rejillas.md
│           └── HD-INST-001_instrumentos_presion.md
│
└── Latex/                           # Plantilla maestra DML de proyectos de ingeniería
    ├── contexto.md                  # Contexto del subproyecto informe DML
    ├── pyproject.toml
    ├── 00_bases_diseno/
    │   ├── bases_diseno.yaml        # Fuente única de verdad (datos + escenarios + normas)
    │   ├── datasheets/
    │   └── normas/
    ├── 01_calculos/
    │   ├── memorias/                # MC-001_template.py
    │   ├── notebooks/
    │   ├── src/                     # bases, propiedades, termica, hidraulica, mecanica
    │   └── tests/                   # test_hidraulica, test_propiedades
    ├── 02_informe_tex/
    │   ├── P2437-HV-INF-001 REV0.tex/.pdf  # Informe técnico maestro (documento canónico)
    │   ├── P2437-HV-INF-002 REV0.tex/.pdf  # Informe de investigación del sistema
    │   ├── config/                  # preamble, header, datos_proyecto, membrete
    │   ├── sections/                # INF-001: 00_portada … 13_anexos (modular)
    │   ├── sections_inf002/         # INF-002: secciones del informe de investigación
    │   ├── references/              # bibliografia.bib (INF-001) + bibliografia_inf002.bib
    │   ├── figures/                 # cfd_caso1.png, cfd_caso2.png
    │   └── logos/
    ├── 03_dashboards_html/
    │   ├── build_dashboard.py
    │   └── templates/dashboard.html.j2
    ├── 04_planos_svg/
    ├── 05_memorias_excel/
    │   └── templates/plantilla_dml.py
    ├── 06_entregables/REV0/
    ├── 07_comunicaciones/
    ├── scripts/new_project.py
    └── task/todo.md
```

## Notas

- La carpeta `Latex/` era la antigua `Plantilla/` (renombrada el 2026-07-23); se
  eliminó su `.claude/` en la migración a `AGENTS.md`.
- El vault de Obsidian es la **raíz del proyecto** (`Calculos/`); `vault/` es el
  subsistema de memoria. Config local ignorada: `/.obsidian/` y `vault/.obsidian/`.
- Mapa de propósito de cada archivo clave: [[06_Archivos clave]].
- Comandos de compilación y regeneración: [[07_Workflows]].

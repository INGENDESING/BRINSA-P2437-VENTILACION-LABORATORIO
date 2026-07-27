---
fecha: 2026-07-23
tags: [workflows]
---

# Workflows / comandos útiles

Solo los no triviales que toman tiempo redescubrir.

## Regenerar la memoria de cálculo Excel

```bash
python generar_excel.py
```

## Emitir entregables (Excel + informes + copias a Emisiones/)

```bash
python scripts/emitir.py
```

Regenera `memoriadecalculo.xlsx` (formato corporativo CAL.xlsx, 2 hojas),
convierte las hojas de datos .md a Excel corporativo (`scripts/generar_dts.py`
→ `build/dts/`), genera el listado de equipos (`scripts/generar_lis.py` →
`build/lis/`), recompila INF-001 e INF-002 (pdflatex → bibtex → pdflatex ×2) y
copia los entregables a `Emisiones/` con sus nombres GP-N-09, dejando trazabilidad
en `Emisiones/MANIFIESTO_EMISION.md`.
**Regla:** al cierre de cualquier sesión que modifique fuentes de entregables
(`Latex/02_informe_tex/`, `generar_excel.py`, `Investigacion/Sistemas/`), ejecutar
este script. Las fuentes se editan; las emisiones se regeneran — nunca editar a
mano un archivo de `Emisiones/`.

## Compilar el informe DML (doble pasada para TOC/referencias)

```bash
cd Latex/02_informe_tex && pdflatex "P2437-HV-INF-001 REV0.tex"   # ×2
```

Si cambian las citas bibliográficas: `pdflatex` → `bibtex` → `pdflatex` ×2.

Motor **pdflatex**, tipografía **NewTX** (`newtxtext` + `newtxmath`), `microtype`,
`siunitx`. El informe DML es el documento canónico (incluye la memoria descriptiva).

Si quedan restos de una compilación xelatex previa (`.toc` con `\xpg@aux`), borrar
los `.aux` / `.toc` / `.out` y recompilar.

## Generar imágenes auxiliares de DTS-001

```bash
. .venv/Scripts/activate
python scripts/generar_img_dts001.py
```

Salida: `build/dts/img/curva_ventilador_dts001.png` y
`build/dts/img/ventilador_referencia_dts001.png`.

## Generar PDF alternativo de DTS-001

Requiere el entorno virtual `.venv/` con `reportlab` instalado.

```bash
. .venv/Scripts/activate
python scripts/pdf_dts001.py
```

Salida: `build/dts/P2437-HV-DTS-001.pdf`. Copiar manualmente a
`Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-001.pdf` y actualizar
`Emisiones/MANIFIESTO_EMISION.md`.

**Nota:** por excepción de nomenclatura del proyecto, los entregables no llevan
sufijo ` REV1` en el nombre de archivo.

## Despliegue del dashboard (GitHub Pages)

Settings → Pages → Deploy from branch (`master` o `main`) → carpeta `/docs`.

---
fecha: 2026-07-23
tags: [indice]
---
s
# Vault — HVAC Laboratorio Brinsa

El vault de Obsidian es la **raíz del proyecto** (`Calculos/`): todo el repo es
navegable en Obsidian. Esta carpeta `vault/` es el subsistema de memoria a largo
plazo; el resumen rápido de sesión vive en `../contexto.md`.

## Inicio de sesión

Siempre comenzar por [[inicializacion]]: protocolo de lectura del vault para
recuperar contexto sin gastar tokens innecesarios.

## Secciones

- [[01_Estado actual]] — dónde está el proyecto hoy
- [[02_Bases de diseño congeladas]] — lo que NO se revisa sin aprobación
- [[05_Preguntas abiertas]] — bloqueos y datos pendientes del cliente
- [[06_Archivos clave]] — mapa de archivos del proyecto
- [[07_Workflows]] — comandos no triviales
- [[estructuraproyecto]] — árbol de archivos y carpetas del proyecto
- [[codificacion]] — codificación GP-N-09 de los documentos del proyecto

## Decisiones de diseño

- [[2026-07-22_presurizacion-damper-alivio]]
- [[2026-07-22_escenarios-filtracion-merv-hepa]]
- [[2026-07-22_cfd-pressure-outlet]]

## Decisiones de diseño (2026-07-28)

- [[2026-07-28_formato-excel-a3-tnr28-verde]] — formato Excel: A3 horizontal, TNR 28, verde claro DML, módulo único `estilos_excel.py`

## Decisiones de diseño (2026-07-27)

- [[2026-07-27_montaje-mural-planta]] — REV2: ventilador axial mural Ø560 mm por uniformidad con planta
- [[2026-07-27_sin-presurizacion-ventilador-axial]]
- [[2026-07-27_presentacion-excel-a-o-times-new-roman]]
- [[2026-07-27_filtro-ventilador-axial]] — acoplamiento del filtro MERV 13-14 al ventilador axial (superada parcialmente por REV2)

## Bitácora

- [[2026-07-28]] — rediseño estético de los Excel: A3 horizontal, TNR 28, verde claro DML, módulo único de formato; emisión de 7 entregables
- [[2026-07-27_rev2_montaje_mural]] — REV2: actualización integral al montaje típico de planta
- [[2026-07-27_dts002_filtro_axial]] — priorización de DTS-002: adaptación del filtro MERV 13-14 al ventilador axial
- [[2026-07-27_mejora-presentacion-excel]] — mejora de presentación Excel: A:O, Times New Roman, colores y bordes corporativos; emisión REV1
- [[2026-07-27]] — cambio de alcance: sin presurización, ventilador axial, sin instrumentación ΔP; emisión REV1
- [[2026-07-23]] — creación del vault, skill `obsidian-vault`, migración a AGENTS.md,
  investigación del sistema y recálculo para sitio Cajicá

## Decisiones de diseño (2026-07-23)

- [[2026-07-23_recalculo-sitio-cajica]]
- [[2026-07-23_sin-hepa-laboratorio-industrial]]

## Plantillas

- `99_Plantillas/plantilla_decision.md`
- `99_Plantillas/plantilla_bitacora.md`

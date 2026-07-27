# Plan: Cambio de alcance — sin presurización, ventilador axial, sin instrumentación ΔP (REV1)

## Contexto

- Objetivo: eliminar la presurización (+25 Pa, damper de alivio, lazo de control e instrumentación ΔP), cambiar el ventilador de centrífugo a **axial**, y reemitir los entregables afectados como **REV1**. Se mantienen: caudal 3 840 m³/h (12 ACH, 320 m³), filtración MERV 8 + MERV 13-14, 3 rejillas 353×336 mm, estrategia sin ductos de impulsión, sitio Cajicá (ρ = 0.88 kg/m³) y motor 440 V 3φ 60 Hz.
- Cliente / Proyecto DML: P2437 — HVAC Laboratorio BRINSA.
- Normas aplicables: ASHRAE (Fundamentals, 62.1, 170 ref.), AMCA 210, GP-N-09. AMCA 500-D y referencias de dampers/instrumentos quedan fuera.
- Decisiones del usuario (2026-07-27): entregables corregidos se emiten como **REV1**; el CFD existente **no se re-ejecuta** — se reformula su interpretación como distribución de flujo/ventilación (válido en incompresible; la BC pressure outlet 0 Pa representa mejor la nueva realidad sin back-pressure).

## Nuevo punto de diseño (recálculo)

- ΔP sistema sin offset de presurización: ΔP_filtro cargado 154 Pa + ΔP_rejillas 11 Pa = **165 Pa en sitio** (antes 190 Pa).
- Equivalente catálogo (ρ = 1.2): 165 × 1.2/0.88 ≈ **225 Pa** (antes 260 Pa). Filtro limpio: 59 + 11 = 70 Pa sitio ≈ 95 Pa catálogo.
- Potencia teórica: P = 1.067 m³/s × 165 Pa / (η × 1000). Con η_axial = 0.55 (provisional): ≈ 0.32 kW (0.43 HP). Motor tentativo 0.75–1.0 HP TEFC 440 V 3φ 60 Hz — fijar tras selección de catálogo.
- Candidatos axiales anticorrosivos: vaneaxial/tubeaxial PRFV o PP (Greenheck, Sodeca HCT/HGT FRP, NYB, Plastec, S&P). Criterio: 3 840 m³/h @ ~225 Pa catálogo, motor TEFC 440 V 3φ 60 Hz.

## Supuestos clave

- [ ] ΔP_filtro cargado MERV 13-14 = 154 Pa se mantiene (bases congeladas; solo se retira el offset de 25 Pa).
- [ ] ΔP_rejillas = 11 Pa a 3 m/s con C_d = 0.60 se mantiene como pérdida de descarga (ASHRAE Fundamentals).
- [ ] η_axial = 0.55 provisional hasta selección de catálogo (documentar con fuente del fabricante).
- [ ] El damper de alivio queda eliminado por completo (sin presurización no tiene función).
- [ ] Tensión 440 V 3φ 60 Hz se mantiene (cliente, 2026-07-23).

## Tareas

### Fase A — Recálculo y fuente única de verdad
- [ ] T1. `Latex/00_bases_diseno/bases_diseno.yaml`: retirar presurización; ventilador axial (165 Pa sitio, η 0.55, 225/95 Pa catálogo); escenarios sin +25 Pa; título sin presurización.
- [ ] T2. `generar_excel.py` → `memoriadecalculo.xlsx`: quitar ΔP_pos/25 Pa, pasos 17-18; fórmula `=B{i}+25+11` → `=B{i}+11`; η/motor nuevos; títulos sin presurización.

### Fase B — Investigación y selección del axial
- [ ] T3. `Investigacion/Sistemas/informe_investigacion.md`: reescribir §6.1 (axial viable), eliminar §5.2/5.3 y §6.4/6.5, actualizar §1, §8.2, §9.
- [ ] T4. `Investigacion/Sistemas/listado_equipos.md`: ítem 1 axial, ítem 2 motor, eliminar ítems 8-12, revisar 16-17, título.
- [ ] T5. `hojas_datos/HD-VENT-001`: reescritura total (axial). Eliminar `HD-INST-001`. Revisar encuadre de HD-REJ-001.

### Fase C — Scripts y entregables Excel
- [ ] T6. `scripts/generar_img_dts001.py`: curva ilustrativa axial, punto 3 840 m³/h @ 225 Pa catálogo / 165 Pa sitio.
- [ ] T7. `scripts/generar_dts.py`: título DTS-001 axial; eliminar IC-DTS-001 de DOCUMENTOS; borrar salida previa.
- [ ] T8. `scripts/generar_lis.py`: título sin presurización.

### Fase D — Informes LaTeX (REV1)
- [ ] T9. INF-001: frontmatter/resumen/introducción/objetivos/alcance sin presurización; tablas de bases/resultados recalculadas; CFD reformulado; conclusiones/recomendaciones sin damper/sensor; REV1.
- [ ] T10. INF-002: título sin presurización; §7.1 axial; eliminar §6.2/6.3 y §8.2/8.3; depurar bib; REV1.
- [ ] T11. Recompilar (pdflatex ×2, bibtex INF-002) + grep de control (presurización, damper, Magnehelic, MS-121, SEBR, BCSW-FRP, 25/190/260 Pa, IC-DTS).

### Fase E — Dashboard, emisión y memoria
- [ ] T12. `docs/index.html`: sin "Presurización", sin +25 Pa, potencia/ΔP nuevos.
- [ ] T13. `scripts/emitir.py`: quitar IC-DTS-001; nombres REV1; ejecutar y verificar manifiesto (7 entregables).
- [ ] T14. Cierre: `contexto.md`, vault (estado, bases congeladas, preguntas, bitácora, nota decisión 2026-07-27), sin commit sin autorización.

## Riesgos / Puntos de verificación

- [ ] Viabilidad del axial a 225 Pa catálogo con curvas reales de fabricante; si no existe, detener y reportar.
- [ ] Validación dimensional en cada recálculo; consistencia YAML ↔ Excel ↔ informes.
- [ ] Revisión cruzada: potencia ≈ 0.32 kW vs. 0.338 kW anterior.
- [ ] Grep final: solo menciones históricas deliberadas (nota REV1).
- [ ] PDF manual de DTS-001: generarse con el REV1 nuevo.

## Revisión

- **Resumen:** se aplicó el cambio de alcance del cliente (REV1): sin presurización, ventilador axial tubeaxial PRFV, sin instrumentación ΔP ni damper de alivio. Se actualizaron la fuente única de verdad (`bases_diseno.yaml`), la memoria Excel (`generar_excel.py`), la investigación del sistema y el BOQ, las hojas de datos (DTS-001 axial; IC-DTS-001 eliminada), ambos informes LaTeX, el dashboard web, `scripts/emitir.py` y el vault.
- **Desviaciones respecto al plan:** ninguna sustancial. Se optó por eliminar el candidato Plastec de la tabla comparativa de axiales en INF-002 porque la fuente disponible apunta a ventiladores centrífugos, no axiales.
- **Limitaciones conocidas:** el motor de 0.75 HP y la eficiencia 0.55 son provisionales; la potencia definitiva depende de la curva del axial seleccionado. El PDF de DTS-001 REV1 debe generarse manualmente desde Excel.
- **Trabajo futuro recomendado:** confirmar disponibilidad comercial del axial (Aerovent FBD/Greenheck/Sodeca/NYB), fijar tamaño/RPM/potencia, generar PDF manual de DTS-001 y verificar caudal en balanceo.
- **Archivos entregables y rutas:**
  - `Latex/00_bases_diseno/bases_diseno.yaml`
  - `generar_excel.py` / `memoriadecalculo.xlsx`
  - `Investigacion/Sistemas/informe_investigacion.md`, `listado_equipos.md`, `hojas_datos/HD-VENT-001_ventilador.md` (HD-INST-001 eliminada)
  - `scripts/generar_img_dts001.py`, `scripts/generar_dts.py`, `scripts/generar_lis.py`
  - `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex/pdf`, `P2437-HV-INF-002 REV0.tex/pdf`
  - `docs/index.html`
  - `scripts/emitir.py`
  - `Emisiones/` (7 archivos REV1: INF-001/002, CAL-001, DTS-001/002/003, LIS-001)
  - `contexto.md`, `vault/` (estado, bases, preguntas, bitácora 2026-07-27, decisión 2026-07-27, archivos clave)

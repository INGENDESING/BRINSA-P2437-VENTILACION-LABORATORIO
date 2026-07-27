---
fecha: 2026-07-27
tags: [bitacora, ventilador, rev2]
---

# Bitácora — 2026-07-27: REV2 ventilador axial mural Ø560 mm (uniformidad planta)

## Qué se hizo

- Se analizó `Montaje/DISENOFINAL.png` y `Montaje/Descripcion_Tecnica_Sistema_Ventilacion_Inyeccion_2260CFM_v2.md`
  (montaje típico instalado en la planta) y se actualizó TODO el proyecto para uniformidad:
- `HD-VENT-001_ventilador.md` REV2: axial mural Ø560 mm, transmisión directa, montaje con
  estructura de unión + cubierta intemperie + malla de protección interior; motor encapsulado en
  la corriente; candidatos ajustados a mural (Sodeca HQD/HGT primera opción).
- `HD-FILT-001_filtro_merv.md` REV2: §7 reescrita — banco de filtración dentro de la cubierta
  intemperie; eliminadas caja/housing, transición cuadrado/circular y conexión flexible.
- `listado_equipos.md` REV2: nuevos ítems cubierta intemperie (9), estructura de unión (8) y malla
  de protección interior (10); eliminados flexible y caja/housing.
- `bases_diseno.yaml` (revisión 2): tipo mural, Ø560 mm, v_boca real 4,33 m/s, descripción de montaje.
- `generar_excel.py`: estrategia y nota de motor; filas de ventilador seleccionado (Ø560, área real,
  velocidad real) en secciones 4 y 7 con fórmulas vivas.
- INF-001 (`07_bases_disenio`, `12_recomendaciones`, `02_resumen`, `13_anexos`, `01_frontmatter`)
  e INF-002 (`10_ventilador_filtracion`, `14_recomendaciones`, `02_resumen`, `01_frontmatter`,
  `05_objetivos`, `13_conclusiones`, `11_rejillas_accesorios`) actualizados.
- `scripts/generar_img_dts001.py`: la referencia de DTS-001 ahora copia `Montaje/DISENOFINAL.png`;
  curva retitulada a mural.
- `docs/index.html`: axial mural Ø560 y datos reales de boca.
- Emisión completa: `python scripts/emitir.py` OK (7 entregables) + PDF alternativo DTS-001
  (`scripts/pdf_dts001.py` con `.venv`).
- Plan y revisión en `task/todo.md`; decisión en `vault/03_Decisiones/2026-07-27_montaje-mural-planta.md`.

## Verificación

- Chequeo dimensional: Q = 1,0667 m³/s, A_boca(Ø560) = π·0,28² = 0,2463 m² → v = 4,33 m/s (coherente
  en memoria, bases de diseño, INF-001 y dashboard).
- ΔP total se mantiene: filtro 154 Pa + rejillas 11 Pa = 165 Pa sitio (225 Pa catálogo).
- Compilación LaTeX INF-001 (26 páginas) e INF-002 con 0 errores y 0 citas sin resolver.
- Grep cruzado: no quedan "tubeaxial" ni "transmisión por bandas" salvo notas históricas REV1 marcadas.
- `scripts/emitir.py` completo: EMISIÓN OK, 7 entregables; manifiesto actualizado.

## Pendientes

- Confirmar modelo/RPM/potencia definitiva del mural Ø560 mm con el fabricante (punto 3 840 m³/h @ 225 Pa).
- Dimensiones de cubierta intemperie y estructura de unión según submittal.
- Confirmar uso continuo del Durafil ES3 24×24 a 2 260 CFM (o mantener ES2).
- Ensayo de balanceo: verificar caudal real por anemometría en las tres rejillas.

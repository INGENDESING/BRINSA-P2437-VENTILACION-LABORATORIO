---
fecha: 2026-07-27
tags: [preguntas, bloqueos]
---

# Preguntas abiertas / bloqueos

- [ ] Confirmar modelo/RPM/potencia definitiva del ventilador mural Ø560 mm con el fabricante
      (Sodeca HQD/HGT mural anticorrosivo primera opción por canal local; Greenheck mural,
      Aerovent/Twin City mural FRP, NYB FRP mural alternativas). Punto de selección: 3 840 m³/h
      @ 225 Pa catálogo. Plazo máximo de entrega presupuestado: ~3 meses (dato cliente,
      2026-07-23). Ver [[listado_equipos]] y [[2026-07-27_montaje-mural-planta]].
- [ ] Definir dimensiones de la cubierta intemperie y de la estructura de unión con los planos
      del submittal del ventilador.
- [ ] Confirmar con Camfil o distribuidor local (ITECO, RGD Aire, Filter Tech) que el filtro
      **Durafil ES3 24×24×12 in, MERV-14/14A** soporta **2 260 CFM** (3 840 m³/h) de forma
      continua. El caudal nominal (rated airflow) del ES3 es 2 000 CFM, aunque la velocidad
      máxima usable (625 fpm) permite hasta ~2 500 CFM. Si el fabricante no valida uso continuo
      a 2 260 CFM, se mantendrá el **Durafil ES2** como referencia principal (3 000 CFM nominal).
      Ver [[2026-07-27_filtro-ventilador-axial]].
- [ ] Verificar el caudal real en el ensayo de balanceo mediante anemometría en
      las tres rejillas de descarga (ya no hay presión diferencial que medir).

## Resueltas

- [x] ~~Adaptar DTS-002 al ventilador axial~~ → **Resuelto 2026-07-27**: se
      verificó compatibilidad hidráulica y mecánica, se definieron accesorios y
      periféricos, se agregó foto comercial y se regeneró el Excel. Ver
      [[2026-07-27_filtro-ventilador-axial]].
- [x] ~~Generar PDF de `P2437-HV-DTS-001 REV1`~~ → **Resuelto 2026-07-27**: se
      generó PDF alternativo con `scripts/pdf_dts001.py` (reportlab) y se copió a
      `Emisiones/3.0 HV-HOJAS DE DATOS/`. Puede reemplazarse por exportación manual
      desde Excel cuando se disponga de Excel local. Ver
      [[2026-07-27_pdf-alternativo-dts001]].
- [x] ~~Ejecutar el modelo CFD con BC pressure outlet~~ → **Resuelto 2026-07-24**:
      modelo ejecutado en Autodesk CFD; 4 gráficas integradas en `P2437-HV-INF-001`
      REV0/REV1 con análisis figura por figura. Ver
      [[2026-07-22_cfd-pressure-outlet]].
- [x] ¿El laboratorio requiere HEPA? → **No** (2026-07-23, laboratorio de análisis
      industrial). Ver [[2026-07-23_sin-hepa-laboratorio-industrial]].
- [x] Condiciones ambientales del sitio → Cajicá, Cundinamarca (2 558 msnm,
      ρ = 0.88 kg/m³). Ver [[2026-07-23_recalculo-sitio-cajica]].
- [x] Tensión/fases del motor → **440 V, 3φ, 60 Hz** (cliente, 2026-07-23).
- [x] Plazos de entrega de equipos → máximo ~3 meses (cliente, 2026-07-23).
- [x] Push a GitHub → **Completado** (2026-07-24, commit `2bc5b65`, 138 archivos,
      push a `origin/main` OK).
- [x] ~~Lectura de presión diferencial real tras ensayo de balanceo~~ → **Ya no aplica**
      (2026-07-27, REV1: sistema sin presurización ni instrumentación ΔP). La
      verificación se hará por anemometría de caudal en rejillas.

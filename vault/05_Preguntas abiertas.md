---
fecha: 2026-07-27
tags: [preguntas, bloqueos]
---

# Preguntas abiertas / bloqueos

- [ ] Confirmar disponibilidad comercial local del ventilador axial seleccionado
      (Aerovent FBD vía importación, Greenheck VAB/VAD vía Prime Lines, Sodeca
      HCT/HGT, New York Blower FRP). Fijar tamaño, RPM y potencia definitiva con
      la curva de catálogo del fabricante. Plazo máximo de entrega presupuestado:
      ~3 meses (dato cliente, 2026-07-23). Ver [[listado_equipos]] y
      [[2026-07-27_sin-presurizacion-ventilador-axial]].
- [ ] Verificar el caudal real en el ensayo de balanceo mediante anemometría en
      las tres rejillas de descarga (ya no hay presión diferencial que medir).

## Resueltas

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

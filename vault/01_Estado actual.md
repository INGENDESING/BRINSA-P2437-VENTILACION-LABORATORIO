---
fecha: 2026-07-27
tags: [estado]
---

# Estado actual

- **Última tarea completada (2026-07-27):** priorización de DTS-002 — adaptación del sistema de filtración MERV 13-14 al ventilador axial DTS-001. Se actualizó `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md` con verificación hidráulica (v_facial = 2,87 m/s, ΔP inicial/final compatibles), lista de accesorios/periféricos (portafiltros, housing, transición cuadrado/circular, conexión flexible, clips, malla anti-insectos), análisis de incongruencias y foto comercial del filtro Camfil Durafil ES. Se actualizó el BOQ en `Investigacion/Sistemas/listado_equipos.md` (ítem 13: caja/housing de filtración y transición) y se regeneraron DTS-002 y LIS-001. La emisión parcial dejó `P2437-HV-DTS-003.xlsx` bloqueado por Excel; requiere reejecutar `scripts/emitir.py` tras cerrarlo.
- **Tarea previa (2026-07-27):** imagen de referencia de montaje del ventilador axial en muro/pasamuros a ~3,0 m de altura.
- **Tarea previa (2026-07-27):** excepción de nomenclatura para entregables sin ` REV1` en nombre de archivo.
- **Tarea previa (2026-07-27):** mejora de la curva ilustrativa del ventilador axial y regeneración de Excel/PDF de DTS-001.
- **Tarea previa (2026-07-27):** generación de PDF alternativo de `P2437-HV-DTS-001` con `scripts/pdf_dts001.py`.
- **Tarea previa (2026-07-27):** mejora de presentación de los documentos Excel generados y emisión REV1 con `scripts/emitir.py`.
- **Tarea previa (2026-07-27):** cambio de alcance del cliente — sin presurización, ventilador axial tubeaxial PRFV, sin instrumentación ΔP; emisión REV1.
- **Próxima tarea pendiente:**
  - Confirmar disponibilidad comercial local del ventilador axial seleccionado (Aerovent FBD / alternativas Greenheck, Sodeca, NYB) y fijar tamaño/RPM/potencia definitiva con la curva de catálogo; obtener diámetro de boca para dimensionar la transición filtro-ventilador.
  - Confirmar con Camfil/distribuidor local (ITECO, RGD Aire, Filter Tech) que el Durafil ES3 24×24×12 in soporta 2 260 CFM de forma continua, o mantener ES2 como referencia principal.
  - Resolver bloqueo de `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-003.xlsx` (archivo abierto en Excel) y reejecutar `python scripts/emitir.py` para sincronizarlo.
  - Verificar el caudal real en el ensayo de balanceo mediante anemometría en las tres rejillas de descarga.
- **Fecha de última actualización:** 2026-07-27

Relacionado: [[inicializacion]], [[02_Bases de diseño congeladas]],
[[05_Preguntas abiertas]], [[2026-07-27_sin-presurizacion-ventilador-axial]],
[[2026-07-27_presentacion-excel-a-o-times-new-roman]], [[2026-07-27_mejora-presentacion-excel]],
[[2026-07-27_pdf-alternativo-dts001]], [[2026-07-27_curva-ilustrativa-axial]],
[[2026-07-27_nomenclatura-sin-rev1]], [[2026-07-27_montaje-ventilador-muro]],
[[2026-07-27_filtro-ventilador-axial]]

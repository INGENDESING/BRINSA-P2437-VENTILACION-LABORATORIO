---
fecha: 2026-07-23
tags: [estado]
---

# Estado actual

- **Última tarea completada (2026-07-24):**
  1. Corrección de referencias y Apéndice D de `P2437-HV-INF-001 REV0`: bibliografía actualizada con códigos GP-N-09 (`P2437-HV-INF-002`, `P2437-HV-LIS-001`, `P2437-HV-DTS-001…003`, `P2437-IC-DTS-001`, `P2437-HV-CAL-001`) y rutas de emisión en `Emisiones/`; Apéndice D actualizado con los mismos códigos y adición de la memoria de cálculo. Recompilación OK (0 errores, 0 citas sin resolver); emisión OK con 8 entregables.
  2. Actualización del informe técnico `P2437-HV-INF-001 REV0` con los resultados del modelo CFD (`pressure outlet` 0 Pa gauge en las rejillas): 4 figuras nuevas integradas en `Latex/02_informe_tex/figures/`, tabla de condiciones de contorno corregida, análisis gráfico figura por figura, y secciones de alcance, resumen, conclusiones y recomendaciones actualizadas. Recompilación OK; emisión OK con 8 entregables.
  3. Generación del listado de equipos en Excel corporativo
     (`P2437-HV-LIS-001 REV0.xlsx`) a partir de `Investigacion/Sistemas/listado_equipos.md`,
     usando la plantilla `FormatosDocumentos/LIS.xlsx` con exactamente 2 hojas
     (PORTADA + LISTA). Se creó `scripts/generar_lis.py` y se actualizó
     `scripts/emitir.py`; emisión OK con 8 entregables y retiro del `.md` obsoleto
     de `Emisiones/4.0 HV-LISTADOS/`.
  4. Creación de `vault/inicializacion.md` como protocolo de arranque para futuras
     sesiones, reforzando el vault de Obsidian como memoria permanente del proyecto.
- **Tarea previa (2026-07-24):** push del repositorio a GitHub (`origin/main`,
  commit `2bc5b65`, 138 archivos).
- **Tarea previa (2026-07-23):** estructura de emisión `Emisiones/`, informes
  **P2437-HV-INF-001/002**, memoria Excel corporativo, investigación de sistemas,
  vault de Obsidian y codificación GP-N-09.
- **Próxima tarea pendiente:**
  - El usuario generará manualmente el PDF de `P2437-HV-DTS-001 REV0.xlsx` (ambas
    hojas) desde Excel y lo comunicará para registrarlo en el vault y `Emisiones/`.
  - Confirmar disponibilidad comercial de los equipos seleccionados (plazo máx.
    ~3 meses según cliente).
  - Confirmar la lectura de presión diferencial real tras el ensayo de balanceo.
- **Fecha de última actualización:** 2026-07-24

Relacionado: [[inicializacion]], [[02_Bases de diseño congeladas]],
[[05_Preguntas abiertas]], [[2026-07-23_recalculo-sitio-cajica]],
[[2026-07-23_sin-hepa-laboratorio-industrial]]

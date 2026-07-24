---
fecha: 2026-07-23
tags: [preguntas, bloqueos]
---

# Preguntas abiertas / bloqueos

- [ ] Confirmar disponibilidad comercial local de los equipos seleccionados
      (Greenheck BCSW-FRP vía Prime Lines, instrumentos Dwyer, rejillas fabricación
      local). Plazo máximo de entrega presupuestado: ~3 meses (dato cliente,
      2026-07-23). Ver [[listado_equipos]].
- [ ] Confirmar la lectura de presión diferencial real tras el ensayo de balanceo
      (validar el supuesto de rejillas como vía dominante). Ver
      [[2026-07-22_presurizacion-damper-alivio]].
- [ ] El usuario generará manualmente el PDF de `P2437-HV-DTS-001 REV0.xlsx`
      (ambas hojas: PORTADA + ESPECIFICACIÓN) desde Excel para mantener la
      plantilla corporativa idéntica. Una vez generado, comunicarlo para
      registrarlo en el vault y copiarlo a `Emisiones/3.0 HV-HOJAS DE DATOS/`.

## Resueltas

- [x] ~~Ejecutar el modelo CFD con BC pressure outlet~~ → **Resuelto 2026-07-24**:
      modelo ejecutado en Autodesk CFD; 4 gráficas integradas en `P2437-HV-INF-001
      REV0` con análisis figura por figura. Ver
      [[2026-07-22_cfd-pressure-outlet]].
- [x] ¿El laboratorio requiere HEPA? → **No** (2026-07-23, laboratorio de análisis
      industrial). Ver [[2026-07-23_sin-hepa-laboratorio-industrial]].
- [x] Condiciones ambientales del sitio → Cajicá, Cundinamarca (2 558 msnm,
      ρ = 0.88 kg/m³). Ver [[2026-07-23_recalculo-sitio-cajica]].
- [x] Tensión/fases del motor → **440 V, 3φ, 60 Hz** (cliente, 2026-07-23).
- [x] Plazos de entrega de equipos → máximo ~3 meses (cliente, 2026-07-23).
- [x] Push a GitHub → **Completado** (2026-07-24, commit `2bc5b65`, 138 archivos,
      push a `origin/main` OK).

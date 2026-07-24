# Plan: Investigación exhaustiva + recálculo del sistema para sitio Cajicá y actualización del proyecto Latex

## Contexto
- Objetivo: (1) investigación web (fuentes comerciales y académicas) en `Investigacion/Sistemas/` para especificar completamente el sistema de ventilación y presurización positiva del laboratorio de análisis industrial de BRINSA, Cajicá (Cundinamarca), y (2) recalcular todo el sistema con las condiciones reales del sitio y actualizar los entregables del proyecto, incluido `Latex/02_informe_tex`.
- Cliente / Proyecto DML: BRINSA — P2437-HV-INF-001.
- Normas aplicables: ASHRAE 62.1/170 (ref.), RETIE, NTC 2050, OSHA 29 CFR 1910.1450, ISO 12944/NACE (corrosión), AGENTS.md.

## Cambios de bases de diseño aprobados por el cliente (se recalcula en esta etapa)
1. Sitio: Cajicá, Cundinamarca (~2 550 msnm) — ρ ≈ 0.95 kg/m³, P_atm ≈ 75 kPa (a confirmar en T2).
2. Sin HEPA — laboratorio de análisis industrial: diseño = MERV 13-14 cargado. Escenarios HEPA quedan como referencia.
3. Ambiente altamente corrosivo (hipoclorito de calcio): criterio de materiales PRFV/inox 316/epóxico transversal.
4. Objetivo: presión positiva (+25 Pa), exclusión de insectos, objetos extraños y polvo ambiental.

## Tareas

### Etapa A — Investigación
- [x] T1. Crear estructura `Investigacion/Sistemas/` y `hojas_datos/`.
- [x] T2. Condiciones ambientales de Cajicá (IDEAM, ASHRAE climatic, estaciones proxy) y densidad corregida. Con cita y fecha.
- [x] T3. Investigación web por componente: ventilador PRFV/corrosivo, filtro MERV 13-14, rejillas ~353×336 mm con malla anti-insectos, damper de alivio barométrico, instrumentos ΔP (Dwyer/Setra/Siemens), accesorios inox 316.
- [x] T4. Redactar `informe_investigacion.md` (estructura AGENTS.md, tablas comparativas, referencias URL + fecha).
- [x] T5. Redactar `listado_equipos.md` (BOQ con candidatos comerciales y fuentes).

### Etapa B — Recálculo con condiciones de Cajicá
- [x] T6. Recalcular: densidad, ΔP orificio, potencia ventilador, corrección por altitud de curva de catálogo, escenarios MERV (sin HEPA). Verificación dimensional.
- [x] T7. Actualizar `Latex/00_bases_diseno/bases_diseno.yaml` (ambiente, aire, recinto, ventilador, rejillas, nota sin-HEPA).

### Etapa C — Actualización de entregables
- [x] T8. Actualizar `generar_excel.py` y regenerar `memoriadecalculo.xlsx`; verificar fórmulas vivas.
- [x] T9. Actualizar `memoriadescriptiva.md`/`.tex` y recompilar PDF (pdflatex ×2, 0 errores).
- [x] T10. Actualizar `Latex/02_informe_tex/` (07, 09, 10, 12 y secciones que citen densidad/potencia/HEPA) y recompilar `P2437-HV-INF-001 REV0.pdf`.
- [x] T11. Hojas de datos HD-VENT-001, HD-FILT-001, HD-REJ-001, HD-INST-001 (Markdown, valores recalculados).
- [x] T12. Actualizar dashboard `docs/` solo si cambian sus valores base.

### Etapa D — Verificación y cierre
- [x] T13. Verificación cruzada: órdenes de magnitud, consistencia YAML/Excel/memoria/Latex/HD.
- [x] T14. Cierre: sección Revisión aquí, `contexto.md`, vault (estado, bitácora, decisiones, `estructuraproyecto.md`).

## Supuestos clave
- [ ] Altitud Cajicá ~2 550 msnm a confirmar con fuente (T2); P_atm ≈ 75 kPa, ρ ≈ 0.95 kg/m³ provisionales.
- [ ] Hojas de datos en Markdown; Excel corporativo solo si se solicita.
- [ ] El caudal (12 ACH, 3 840 m³/h) no cambia: el recálculo afecta presiones, potencias y selección.
- [ ] Dashboard web solo si cambian sus números base.

## Riesgos / Puntos de verificación
- [ ] ¿1.0 HP sigue siendo la selección con ρ = 0.95? → justificar en hojas de datos.
- [ ] Verificar que el ventilador de catálogo entregue el ΔP a 2 550 msnm.
- [ ] Disponibilidad local de ventiladores PRFV → listar importadores/equivalentes.
- [x] Toda cifra de catálogo cita URL y fecha de consulta.
- [ ] Recompilaciones LaTeX limpias (0 errores, overfulls ≤ 5 pt).

## Revisión

- Resumen: investigación web exhaustiva (5 frentes) documentada en `Investigacion/Sistemas/` (informe + BOQ de 17 ítems + 4 hojas de datos); recálculo completo para el sitio real Cajicá (2 558 msnm, ρ = 0.88 kg/m³) propagado a YAML, Excel, memoria descriptiva, informe DML y dashboard; filtración cerrada en MERV 13-14 (sin HEPA).
- Valores clave nuevos: ΔP rejillas 11 Pa, ΔP diseño 190 Pa en sitio (260 Pa catálogo), potencia 0.338 kW (0.45 HP), motor 1.0 HP TEFC, damper de alivio obligatorio.
- Desviaciones respecto al plan: en `memoriadescriptiva` y el informe DML el escenario alto de 350 Pa se reemplazó por 285 Pa (+50 % sobre diseño) para conservar la estructura de 3 filas de la tabla de potencias.
- Limitaciones: tensión/fases del motor por confirmar con el cliente; tamaño/RPM exactos del ventilador dependen del software del fabricante (CAPS Greenheck); valores ASHRAE de la edición 2009 (la tabla 2021/2025 no es extraíble por vía programática); disponibilidad y plazos comerciales por confirmar.
- Verificación: valores derivados comprobados con Python; consistencia cruzada YAML ↔ Excel ↔ memorias ↔ hojas de datos; ambas compilaciones pdflatex con 0 errores.
- Entregables: `Investigacion/Sistemas/informe_investigacion.md`, `Investigacion/Sistemas/listado_equipos.md`, `Investigacion/Sistemas/hojas_datos/HD-*.md`, `Latex/00_bases_diseno/bases_diseno.yaml`, `memoriadecalculo.xlsx`, `memoriadescriptiva.pdf`, `Latex/02_informe_tex/P2437-HV-INF-001 REV0.pdf`, `docs/index.html`, `contexto.md`, vault actualizado.

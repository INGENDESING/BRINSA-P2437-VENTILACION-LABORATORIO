# Plan: Adaptación de Memoria Descriptiva a Plantilla Corporativa DML

## Contexto
- **Objetivo:** Adaptar el contenido técnico de `memoriadescriptiva.md` (sistema de ventilación y presurización del laboratorio HVAC, volumen 274 m³, 12 ACH) al formato de informe técnico corporativo DML definido en `Plantilla/02_informe_tex/`.
- **Cliente / Proyecto DML:** P2437-HV-INF-001 — Laboratorio Brinsa.
- **Normas aplicables:** ASHRAE 170-2021, ASHRAE 62.1-2022, NFPA 99-2021, OSHA 29 CFR 1910.1450, WHO Laboratory Biosafety Manual, NIH DRM 2023.

## Supuestos clave
- [x] El informe conservará la Opción A de configuración: ventilador de impulsión directa (sin ductos) + 2 rejillas de exfiltración de 400 mm × 380 mm.
- [x] Los cálculos actuales (caudal 1 935 CFM, potencia 0.38 kW, área de impulsión 0.114 m², radio 190.5 mm) se mantienen como base de diseño congelada.
- [x] La plantilla LaTeX se compilará con `pdflatex` (no `xelatex`) para respetar la configuración corporativa actual (`tgtermes`, `inputenc[T1]`).

## Tareas
- [x] T1. Recopilar metadatos del proyecto (cliente, título, firmas, fechas) y actualizar `Plantilla/02_informe_tex/config/datos_proyecto.tex`.
- [x] T2. Crear copia del informe maestro con código `P2437-HV-INF-001 REV0.tex` en `Plantilla/02_informe_tex/`.
- [x] T3. Actualizar `00_bases_diseno/bases_diseno.yaml` con datos del proyecto HVAC (condiciones ambientales, caudales, velocidades, normas aplicables).
- [x] T4. Redactar secciones corporativas (`04_introduccion.tex`, `05_objetivos.tex`, `06_alcance.tex`, `08_metodologia.tex`).
- [x] T5. Adaptar `07_bases_disenio.tex` con tablas estilo Elsevier: condiciones ambientales, datos del laboratorio, criterios de diseño, normativas.
- [x] T6. Adaptar `09_resultados.tex` con tablas de resultados de ventilación, potencia, áreas y datos para CFD.
- [x] T7. Redactar `10_analisis.tex`, `11_conclusiones.tex`, `12_recomendaciones.tex` y anexos `13_anexos.tex` con cálculos detallados.
- [x] T8. Actualizar `references/bibliografia.bib` con las normas y referencias citadas.
- [x] T9. Compilar el informe con `pdflatex` y verificar que no haya errores ni advertencias críticas.
- [ ] T10. Generar memoria de cálculo Excel corporativa con `plantilla_dml.py` (opcional, pendiente de decisión del cliente).

## Riesgos / Puntos de verificación
- [x] Validación dimensional de todas las ecuaciones y unidades.
- [x] Consistencia entre `bases_diseno.yaml`, secciones LaTeX y memoria Excel existente en `Calculos/memoriadecalculo.xlsx`.
- [x] Verificación de que el membrete corporativo renderice correctamente con los nuevos metadatos.
- [x] Confirmación de que las tablas cumplen el estilo Elsevier (sin viñetas, líneas superior/inferior y bajo encabezado).

---

## Preguntas al cliente para congelar metadatos

1. **Cliente y título:** ¿El cliente es "Brinsa" y el título del informe es "Diseño del Sistema de Ventilación y Presurización del Laboratorio"? **Respuesta: Sí, confirmado.**
2. **Equipo de firmas:** ¿Las firmas son: elaboró J. Arboleda, revisó H. Rosero y aprobó F. Navia (como en la plantilla), o deben cambiarse por otros nombres? **Respuesta: Sí, confirmado.**
3. **Fecha de emisión:** ¿La fecha del informe es 15 de julio de 2026, o se debe usar otra fecha específica? **Respuesta: Sí, confirmado.**

---

## Revisión Final

**Resumen de cambios:**
1. Se actualizó `config/datos_proyecto.tex` con el código P2437-HV-INF-001, cliente BRINSA, título del informe y firmas confirmadas.
2. Se creó el informe maestro `P2437-HV-INF-001 REV0.tex` dentro de `Plantilla/02_informe_tex/`.
3. Se actualizó `00_bases_diseno/bases_diseno.yaml` con los datos del proyecto HVAC.
4. Se redactaron todas las secciones corporativas del informe siguiendo el estilo Elsevier/DML: introducción, objetivos, alcance, bases de diseño, metodología, resultados, análisis, conclusiones, recomendaciones y anexos.
5. Se eliminaron las viñetas del documento cliente y se reemplazaron por tablas estilo Elsevier y párrafos numerados.
6. Se actualizó `references/bibliografia.bib` con las normas ASHRAE, NFPA, OSHA, WHO, NIH y referencias técnicas.
7. Se compiló el informe con `pdflatex` generando un PDF de 18 páginas sin errores críticos.
8. Se verificó la consistencia dimensional: balance de masas entrada/salida = 0.912 m³/s en ambos lados, discrepancia < 0.1 %.

**Desviaciones respecto al plan original:**
- No se generó la memoria de cálculo Excel corporativa con `plantilla_dml.py` porque ya existe una memoria de cálculo funcional (`Calculos/memoriadecalculo.xlsx`). Se deja pendiente de decisión del cliente si desea migrarla a la plantilla corporativa DML.

**Limitaciones conocidas:**
- El documento presenta advertencias menores de `Overfull \vbox` en las páginas de portada y frontmatter, heredadas de la plantilla base. No afectan la legibilidad ni la estructura del informe.
- El modelo CFD no se ejecuta en este informe; únicamente se entregan las condiciones de contorno.

**Archivos entregables y sus rutas:**
- `Plantilla/02_informe_tex/P2437-HV-INF-001 REV0.tex` — archivo maestro LaTeX.
- `Plantilla/02_informe_tex/P2437-HV-INF-001 REV0.pdf` — informe técnico final en PDF (18 páginas).
- `Plantilla/02_informe_tex/config/datos_proyecto.tex` — metadatos centralizados del proyecto.
- `Plantilla/00_bases_diseno/bases_diseno.yaml` — bases de diseño en YAML.
- `Plantilla/02_informe_tex/sections/*.tex` — secciones modulares del informe.
- `Plantilla/02_informe_tex/references/bibliografia.bib` — referencias bibliográficas.
- `Calculos/memoriadescriptiva.md` — memoria descriptiva actualizada (Opción A).
- `Calculos/memoriadecalculo.xlsx` — memoria de cálculo Excel funcional.


---

# Plan: Actualización de bases de diseño — Volumen 320 m³ y 3 rejillas (2026-07-16)

## Contexto
- **Objetivo:** Actualizar el diseño del sistema de ventilación por cambio del volumen efectivo del laboratorio (274 → 320 m³) y del número de rejillas de exfiltración (2 → 3), manteniendo 12 ACH y los criterios de velocidad (8 m/s impulsión, 3.0 m/s exfiltración).
- **Cliente / Proyecto DML:** P2437-HV-INF-001 — Laboratorio Brinsa.
- **Normas aplicables:** sin cambios (ASHRAE 170-2021, ASHRAE 62.1-2022, NFPA 99-2021, OSHA 29 CFR 1910.1450, WHO LBM 2004, NIH DRM 2023).
- **Nota:** ejecutado con aprobación explícita del cliente («continua», 2026-07-16) para entregar de inmediato las condiciones de contorno CFD actualizadas y trabajar en paralelo.

## Supuestos clave
- [x] Se mantienen los criterios de velocidad: 8 m/s en boca del ventilador y 3.0 m/s facial en rejillas.
- [x] Se mantiene ΔP total = 250 Pa y η = 0.60; el motor recomendado sigue siendo 1.0 HP (potencia teórica 0.596 HP).
- [x] Las rejillas se dimensionan con proporción ancho/alto = 0.95 (353.2 mm × 335.5 mm), normalizables a 350 mm × 340 mm.

## Tareas
- [x] T1. Entregar condiciones de contorno CFD actualizadas (radio 206.0 mm; 3 rejillas de 353.2 mm × 335.5 mm).
- [x] T2. Actualizar `generar_excel.py` (V = 320, n_rej = 3) y regenerar `memoriadecalculo.xlsx`.
- [x] T3. Actualizar `memoriadescriptiva.md` y `memoriadescriptiva.tex`; recompilar PDF (xelatex, 10 páginas, 0 errores).
- [x] T4. Actualizar `Plantilla/00_bases_diseno/bases_diseno.yaml`.
- [x] T5. Actualizar secciones del informe (01, 02, 04, 05, 07, 09, 10, 11, 12, 13) y recompilar `P2437-HV-INF-001 REV0.pdf` (pdflatex, 18 páginas, 0 errores).
- [x] T6. Actualizar `Plantilla/contexto.md`.

## Riesgos / Puntos de verificación
- [x] Validación dimensional de las ecuaciones actualizadas.
- [x] Balance de masas: entrada 1.0667 m³/s vs salida 1.0665 m³/s (discrepancia 0.02 % < 0.1 %).
- [x] Barrido de valores obsoletos en fuentes (274, 54.8, 3 288, 1 935, 0.913, 0.912, 0.114, 190.5, 381, 0.304, 0.152, «dos rejillas», 400 × 380): sin ocurrencias fuera del histórico.

## Revisión

**Resumen de cambios:**
1. Bases de diseño: volumen 320 m³ y 3 rejillas de exfiltración.
2. Caudal: 64.0 m³/min = 3 840 m³/h = 2 260 CFM (1.0667 m³/s).
3. Potencia teórica del ventilador: 0.444 kW (0.596 HP); motor recomendado 1.0 HP.
4. Boca de impulsión: 0.1333 m², D = 412 mm, r = 206.0 mm a 8 m/s.
5. Rejillas: 3 × 0.1185 m² → 353.2 mm × 335.5 mm a 3.0 m/s (normalizables a 350 × 340 mm).
6. Actualizados: `generar_excel.py`, `memoriadecalculo.xlsx`, `memoriadescriptiva.md/.tex/.pdf`, `bases_diseno.yaml`, 10 secciones del informe, `P2437-HV-INF-001 REV0.pdf` y `contexto.md`.

**Desviaciones respecto al plan original:**
- Se mantuvo la denominación REV0 en metadatos y nombre de archivo. El control de documentos sugiere emitir REV1 con fechas de firma actualizadas; pendiente de confirmación del cliente.

**Limitaciones conocidas:**
- El informe conserva la denominación REV0 aunque las bases de diseño cambiaron (ver desviación anterior).
- Las imágenes CFD en `resultado simulaciones/` corresponden al diseño anterior (274 m³, 2 rejillas); serán regeneradas por el cliente con las nuevas condiciones de contorno.

**Archivos entregables y sus rutas:**
- `Calculos/memoriadecalculo.xlsx` — memoria de cálculo Excel (V = 320 m³, 3 rejillas).
- `Calculos/memoriadescriptiva.md/.tex/.pdf` — memoria descriptiva actualizada.
- `Plantilla/00_bases_diseno/bases_diseno.yaml` — fuente única de verdad actualizada.
- `Plantilla/02_informe_tex/P2437-HV-INF-001 REV0.pdf` — informe recompilado (18 páginas).
- `Plantilla/contexto.md` — contexto del proyecto actualizado.

---
fecha: 2026-07-27
tags: [bitacora, filtracion, dts002]
---

# Bitácora — 2026-07-27: DTS-002 adaptada al ventilador axial

## Qué se hizo

- Se priorizó la hoja de datos **DTS-002** para que el sistema de filtración
  MERV 13-14 quede adaptado al ventilador axial **DTS-001**.
- Se investigó en web el filtro **Camfil Durafil ES2/ES3** 24×24×12 in MERV-14/14A
  y se obtuvo foto comercial desde el sitio de Camfil.
- Se actualizó `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md`:
  - Nueva sección 7 con verificación hidráulica (v_facial = 2,87 m/s, ΔP
    inicial/final compatible con 165 Pa sitio del ventilador).
  - Tabla de accesorios y periféricos (portafiltros, housing, transición
    cuadrado/circular, conexión flexible, clips, malla anti-insectos, soportes,
    guarda).
  - Análisis de incongruencias: diámetro de boca del ventilador, altura de
    montaje 3,0 m, peso del filtro, sentido de flujo.
  - Sección 8 con foto comercial y enlace al distribuidor Capris (SKU
    855080-009).
- Se actualizó `Investigacion/Sistemas/listado_equipos.md` agregando el ítem 13
  (caja/housing de filtración y transición cuadrado/circular).
- Se regeneraron los entregables con `scripts/emitir.py`:
  - `build/dts/P2437-HV-DTS-002 REV0.xlsx` y copia en
    `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-002.xlsx`.
  - `build/lis/P2437-HV-LIS-001 REV0.xlsx` y copia manual en
    `Emisiones/4.0 HV-LISTADOS/P2437-HV-LIS-001.xlsx` (DTS-003 quedó bloqueado).
- Se actualizaron `contexto.md` y el vault (`01_Estado actual`,
  `05_Preguntas abiertas`, decisión y bitácora).

## Verificación

- Chequeo dimensional: 3 840 m³/h / (0,610 m × 0,610 m) = 2,87 m/s.
- Escalado de ΔP: ΔP_cat @ 500 fpm = 0,31 in c.a. (ES3 MERV 14) → 98 Pa @
  565 fpm → 72 Pa en el sitio (k = 0,733). El valor congelado de diseño 80/210 Pa
  catálogo es conservador y compatible.
- Caudal: 2 260 CFM. ES3 rated airflow = 2 000 CFM, máximo usable ≈2 500 CFM.
  ES2 rated airflow = 3 000 CFM. Se deja pendiente confirmación de uso continuo
  del ES3 a 2 260 CFM.
- Compilación LaTeX de INF-001 e INF-002 sin errores.

## Pendientes

- Confirmar con Camfil/distribuidor si ES3 24×24×12 soporta 2 260 CFM continuo
  o mantener ES2 como referencia principal.
- Obtener del fabricante del ventilador el diámetro de boca para dimensionar la
  transición cuadrado/circular.
- Cerrar `Emisiones/3.0 HV-HOJAS DE DATOS/P2437-HV-DTS-003.xlsx` en Excel y
  reejecutar `python scripts/emitir.py` para sincronizarlo.

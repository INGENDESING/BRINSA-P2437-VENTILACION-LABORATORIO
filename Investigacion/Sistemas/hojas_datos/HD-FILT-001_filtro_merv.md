# Hoja de datos: etapa de filtración (prefiltro MERV 8 + filtro final MERV 13-14)

| Campo | Valor |
|---|---|
| Código | HD-FILT-001 |
| Revisión | 1 |
| Fecha | 2026-07-27 |
| Proyecto | P2437-HV-INF-001 — BRINSA, laboratorio de análisis industrial, Cajicá |
| Etiqueta de equipo | FILT-001 (banco de filtración de la impulsión) |

---

## 1. Servicio

1.1. Filtración del aire exterior de impulsión (3 840 m³/h) para exclusión de polvo, insectos y objetos extraños, aguas arriba del laboratorio. No es un servicio de biocontención: no se requiere HEPA. Ambiente exterior corrosivo (atmósfera clorada de planta de hipoclorito de calcio, HR media 84 %).

## 2. Especificación de eficiencia

**Tabla 1.** Clases de eficiencia exigidas (consulta 2026-07-23).

| Etapa | ASHRAE 52.2 | ISO 16890 | EN 779:2012 (referencia) | Eficiencia mínima por rango |
|---|---|---|---|---|
| Etapa 1 (prefiltro) | MERV 8 | ISO Coarse / ePM10 (dato típico de equivalencia) | G4 | Fracción gruesa: polvo, fibras, insectos |
| Etapa 2 (filtro final) | MERV 13-14 | ePM1 50-70 % | F7-F8 | MERV 13: E2 ≥ 90 %, E3 ≥ 90 %; MERV 14 añade E1 ≥ 75 % |

Fuentes: [ANSI/ASHRAE 52.2-2017 (PDF)](https://www.ashrae.org/File%20Library/Technical%20Resources/COVID-19/52_2_2017_COVID-19_20200401.pdf); equivalencias MERV ↔ ePM1 confirmadas en la ficha del fabricante ([Camfil Durafil ES2 (PDF)](https://cdn.lsicloud.net/pandhwhsal/documents/855080-003.pdf): MERV 13 → ePM1 60 %, MERV 14 → ePM1 70 %). Se exige informe de ensayo según la norma citada.

2.1. Justificación de la clase: MERV 13-14 garantiza E3 ≥ 90 % (polen, polvo grueso, esporas) y E2 ≥ 90 % (polvo fino), con amplio margen sobre el objetivo funcional. MERV 14 se prefiere sobre MERV 13 por la carga de polvo de la planta de hipoclorito.

## 3. Caídas de presión de diseño

**Tabla 2.** ΔP de la etapa final MERV 13-14 (valores congelados de la memoria de cálculo).

| Condición | Estándar de catálogo (ρ = 1.2 kg/m³) | En el sitio (ρ = 0.88 kg/m³, k = 0.733) |
|---|---|---|
| Filtro limpio | 80 Pa | 59 Pa |
| Filtro cargado (final de diseño) | 210 Pa | 154 Pa |

3.1. El ΔP final de diseño de 210 Pa estándar es conservador frente a los límites de catálogo (Camfil: 375 Pa máx. con criterio «cambiar al duplicar ΔP inicial»; AAF: 500 Pa máx.; clase F de EN 779: 450 Pa recomendados — fuentes en Tabla 4), lo que alarga la vida útil real del elemento. El prefiltro MERV 8 aporta 50-75 Pa limpio y 250 Pa final (catálogo; [Camfil 30/30 (PDF)](https://cdn.lsicloud.net/pandhwhsal/documents/406331002-SPS.pdf), consulta 2026-07-23).

3.2. Velocidad frontal: con un módulo 24×24 in (610×610 mm) a 3 840 m³/h resulta ≈2.87 m/s (565 fpm), ligeramente superior al punto de catálogo de 500 fpm (2.54 m/s); el ΔP real será ~13-15 % superior al tabulado (dato típico, escalado aproximadamente cuadrático), efecto parcialmente compensado por la corrección de densidad del sitio. Verificar con la curva del fabricante seleccionado.

## 4. Dimensiones y construcción

**Tabla 3.** Requisitos de construcción.

| Característica | Especificación |
|---|---|
| Dimensiones | Módulo pleno 24×24 in (610×610 mm); profundidad según línea V-bank (292 mm dato típico) |
| Tipo etapa final | V-bank / casete compacto de minipleat |
| Marco del filtro | 100 % plástico (ABS/poliestireno/HIPS), sin componentes metálicos; paquete sellado con poliuretano |
| Junta | Poliuretano o EPDM continua, en cabezal |
| Portafiltros (holding frames) | Inox 304/316 con junta continua de poliuretano; galvanizado descartado por el ambiente clorado |
| Fijación prefiltro | Espaciador/clip frontal integrado al filtro final (configuración estándar de los candidatos) |
| Marco del prefiltro | Cartón hidrófugo; la rejilla soporte galvanizada se acepta con inspección de corrosión programada en el primer año |

## 5. Candidatos comerciales

**Tabla 4.** Filtros finales candidatos (500 fpm = 2.54 m/s; consulta 2026-07-23).

| Fabricante / modelo | Clase | Marco | ΔP inicial catálogo | ΔP final máx. | Fuente |
|---|---|---|---|---|---|
| Camfil Durafil ES2 (referencia de diseño) | MERV 14 / ePM1 70 | Plástico ABS/poliestireno | ≤ 0.32 in c.a. ≈ 80 Pa | 375 Pa | [Ficha (PDF)](https://cdn.lsicloud.net/pandhwhsal/documents/855080-003.pdf) |
| AAF VariCel VXL | MERV 14 | Plástico HIPS + ABS, sin metal | ≈ 100-112 Pa (dato típico, de curva) | 500 Pa | [AAF AFP-1-162 (PDF)](https://aafterms.aafintl.com/-/media/files/aaf/commercial-and-industrial/us-products/box-filters/varicel-vxl/varicel-vxl_prod_mark_sht_afp-1-162.pdf) |
| Freudenberg Viledon MaxiPleat MX 85 | F8 / ePM1 65 % (≈ MERV 14) | Plástico, paquete fundido estanco | 135-180 Pa (familia) | ≈ 450 Pa (dato típico) | [Ficha (PDF)](https://menardifilters.se/wp-content/uploads/MaxiPleat_DS_02-CC-038-EN_low.pdf) |
| Koch Multi-Pleat Green13 | MERV 13 | Cartón + rejilla galvanizada | ≈ 75-100 Pa (dato típico plisados MERV 13) | ≈ 250 Pa (dato típico) | [Ficha (PDF)](https://www.airfilterplus.com/wp-content/uploads/2022/03/Multi-Pleat-Green-13-2021.pdf) |

**Tabla 5.** Prefiltros candidatos y portafiltros (consulta 2026-07-23).

| Ítem | Candidato | Dato clave | Fuente |
|---|---|---|---|
| Prefiltro MERV 8 | Camfil 30/30 / Dual 9 | ΔP inicial ≤ 67-75 Pa @ 500 fpm | [Ficha (PDF)](https://cdn.lsicloud.net/pandhwhsal/documents/406331002-SPS.pdf) |
| Prefiltro MERV 8 | Koch Multi-Pleat XL8 | ΔP inicial ~50-62 Pa (dato típico, de curva) | [Ficha (PDF)](https://fsifiltration.com/wp-content/uploads/2020/08/Pleated-MERV8.pdf) |
| Portafiltros | Camfil MagnaFrame II | Galvanizado 14 ga, opción inox 304; junta PU | [Camfil](https://www.camfil.com/en-ca/products/housings-frames--louvers/filter-holding-frames/filter-holding-frames/magnaframe-ii-gasket-seal-_-47771) |
| Portafiltros | Camfil Universal Holding Frame | Disponible inox o galvanizado; junta PU continua opcional | [Camfil](https://www.camfil.com/en-sg/products/housings-frames--louvers/filter-holding-frames/filter-holding-frames/universal-filter-holding-frame-_-46512) |

## 6. Suministro y repuestos (Colombia)

6.1. Canales identificados (consulta 2026-07-23): AAF/Flanders vía [Filter Tech S.A.S.](https://filtrosdeaireacondicionado.com/) y [Air Solutions Colombia](https://www.airsolutionscolombia.com/productos); Camfil vía [ITECO](https://www.iteco.com.co/nuestras-marcas/) y [RGD Aire](https://rgdaire.com/index.php/servicio-filtros/); reemplazos compatibles de fabricación nacional [CARVEL S.A./Workclean](https://carvel.com.co/catalogo-workclean/filtros-de-aire-acondicionado-tipo-cartucho-fdcjm/).

6.2. La especificación se congela en términos MERV 13-14 / ePM1 50-70 % + 24×24 in para habilitar segunda fuente. Se incluye en la compra inicial un juego de repuestos (un prefiltro y un filtro final). Cantidades y plazos: por confirmar con proveedor.

## 7. Normas aplicables

7.1. ANSI/ASHRAE 52.2-2017 (ensayo y clasificación MERV); ISO 16890 (ePM1, exigible como informe alternativo); EN 779:2012 (referencia heredada F7/F8). El estado de carga del filtro se sigue por programa de mantenimiento basado en la ΔP esperada (59 Pa limpio / 154 Pa cargado en el sitio) y en la carga de polvo observada en operación (dato típico de operación).

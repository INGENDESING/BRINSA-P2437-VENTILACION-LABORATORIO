
# Informe de investigación: sistema de ventilación y presurización positiva del laboratorio de análisis industrial

**Proyecto:** P2437-HV-INF-001 — BRINSA, planta Cajicá (Cundinamarca, Colombia)
**Documento:** informe_investigacion.md — Revisión 0
**Fecha de consulta de fuentes:** 2026-07-23

---

## 1. Objetivo

1.1. Seleccionar y documentar, con base en investigación de mercado y fuentes técnicas trazables, los equipos y componentes del sistema de ventilación por presurización positiva del laboratorio de análisis industrial de BRINSA en Cajicá: ventilador de impulsión directa, etapa de filtración MERV 13-14, rejillas de exfiltración con malla anti-insectos, damper de alivio barométrico e instrumentación de presión diferencial, con set-point de +25 Pa y mínimo admisible de +12.5 Pa.

1.2. La función del sistema es doble: mantener el recinto en presión positiva respecto al exterior y excluir insectos, objetos extraños y polvo del ambiente del laboratorio. No se trata de un sistema de biocontención; por tanto se descarta expresamente la filtración HEPA.

## 2. Alcance

2.1. El informe cubre la investigación y selección de componentes del sistema completo de impulsión filtrada (3 840 m³/h, 12 renovaciones/h sobre 320 m³), la exfiltración controlada por tres rejillas de 353×336 mm y un damper de alivio barométrico calibrable, y el lazo de medición y alarma de presión diferencial. Incluye las bases de diseño del sitio, la corrección de densidad por altitud, el análisis comparativo de opciones comerciales por componente, el marco normativo aplicable y la selección recomendada.

2.2. Quedan fuera del alcance el diseño estructural de soportes, el cálculo eléctrico de acometidas (se limita a requisitos RETIE/NTC 2050), y la ingeniería de detalle de la obra civil de pasamuros.

## 3. Bases de diseño

### 3.1. Condiciones ambientales del sitio — Cajicá, Cundinamarca

**Tabla 1.** Condiciones ambientales de diseño del sitio (consulta 2026-07-23).

| Parámetro | Valor de diseño | Fuente |
|---|---|---|
| Altitud (casco urbano Cajicá) | 2 558 msnm | [DB-City](https://en.db-city.com/Colombia--Cundinamarca--Cajic%C3%A1); validado contra aeródromo Guaymaral SKGY (8 389 ft, a ~7 km) |
| Presión atmosférica | 74.1 kPa | Modelo de atmósfera estándar ISA a 2 558 m; validado contra QNH de METAR SKBO ([FlightAware](https://es.flightaware.com/resources/airport/SKBO/weather)) |
| Temperatura de diseño verano | 21 °C (condición 0.4 %, bulbo seco) | [ASHRAE 2009, estación Bogotá/El Dorado WMO 802220, vía CaptiveAire (PDF)](https://www.captiveaire.com/catalogcontent/fans/sup_mpu/doc/winter_summer_design_temps_us.pdf) |
| Temperatura de diseño invierno | 3 °C (condición 99.6 %) | Ídem ASHRAE 2009 |
| Temperatura media anual | 14 °C | [Alcaldía de Cajicá — Aspectos generales (PDF)](https://www.cajica.gov.co/docdown/archi/2022/Cartografia/1.1.%20ASPECTOS%20GENERALES.pdf) |
| Humedad relativa media anual | 84 % (rango mensual 80-89 %) | [Weather Atlas — Cajicá](https://www.weather-atlas.com/en/colombia/cajica-climate) |
| Punto de rocío de diseño | 14.2 °C | ASHRAE 2009 (condición de deshumidificación 0.4 %) |
| Densidad del aire | 0.88 kg/m³ a 20 °C; 0.87 kg/m³ en condición 0.4 % | Ecuación de gas ideal con P_atm = 74.1 kPa (cálculo propio verificado) |

3.1.1. La presión de estación real es 74.1 kPa; los valores de 1 024-1 029 hPa publicados en portales meteorológicos son presión reducida a nivel del mar (QNH) y no deben usarse en el diseño. Confundir ambas introduce un error del 28 % en la densidad del aire y en la selección del ventilador ([tutiempo Cajicá](https://en.tutiempo.net/cajica.html?data=last-24-hours), consulta 2026-07-23).

3.1.2. Los valores ASHRAE citados corresponden a la edición 2009 (única tabla extraíble de la fuente); la edición 2021/2025 puede diferir en ±0.5 °C, diferencia irrelevante para un sistema de ventilación sin climatización. La estación proxy (El Dorado, 2 546 msnm) está prácticamente a la cota del sitio.

### 3.2. Corrección de densidad y su impacto en la selección

3.2.1. Las curvas de catálogo de ventiladores están publicadas a densidad estándar (1.2 kg/m³; 70 °F, 29.92 in Hg), condición declarada explícitamente por los fabricantes ([Twin City Fan, Fan Engineering FE-1600](http://eu.tcf.com/wp-content/uploads/sites/4/2018/06/Temperature-Altitude-Effects-on-Fans-FE-1600-1.pdf), consulta 2026-07-23). A tamaño y velocidad constantes, el caudal volumétrico no cambia con la densidad, mientras que la presión y la potencia absorbida son proporcionales a ella.

3.2.2. El factor de densidad del sitio es k = 0.88/1.20 = 0.733. En consecuencia, todo equipo seleccionado por catálogo a densidad estándar entregará en el sitio la misma presión estática reducida en ese factor, y las caídas de presión de filtros, rejillas y accesorios tabuladas a densidad estándar deben multiplicarse por 0.733 para obtener el valor en el sitio.

3.2.3. Impacto cuantificado sobre el punto de trabajo (valores congelados de la memoria de cálculo):

**Tabla 2.** Punto de trabajo del sistema en el sitio y equivalente de catálogo.

| Magnitud | En el sitio (ρ = 0.88 kg/m³) | Equivalente de catálogo (ρ = 1.2 kg/m³) |
|---|---|---|
| Caudal | 3 840 m³/h (1.0667 m³/s; 2 260 CFM) | 3 840 m³/h (sin cambio) |
| ΔP filtro MERV 13-14 cargado (diseño) | 154 Pa | 210 Pa |
| ΔP filtro MERV 13-14 limpio | 59 Pa | 80 Pa |
| Offset de presurización | 25 Pa | 34 Pa |
| ΔP rejillas (3 m/s, C_d = 0.60) | 11 Pa | 15 Pa |
| **ΔP total escenario cargado (selección)** | **190 Pa** | **260 Pa** |
| ΔP total escenario limpio | 95 Pa | 130 Pa |
| Potencia teórica de aire (η = 0.60) | 0.338 kW (0.45 HP) | — |

3.2.4. Consecuencia sobre la exfiltración: la configuración alternativa sin damper (rejillas a 4 m/s) ya no alcanza los 25 Pa de consigna a esta altitud (solo 19.6 Pa); para cerrar el balance en 25 Pa sin damper se requeriría un área total de 0.236 m² (0.079 m² por rejilla, aproximadamente 280×281 mm, a 4.5 m/s). En consecuencia, el damper de alivio barométrico pasa de opción a componente obligatorio del sistema.

3.2.5. Sobre el motor: la potencia teórica corregida al sitio es 0.338 kW (0.45 HP); se instala un motor de 1.0 HP TEFC con tratamiento anticorrosivo, lo que deja un margen superior al 100 % sobre el eje, suficiente para absorber el derateo por altitud (regla práctica NEMA MG-1: 3 % por cada 500 m sobre 1 000 msnm, es decir ≈9 % a 2 558 msnm; [NEMA MG-1 citado en motorsatwork.com](https://www.motorsatwork.com/from-the-blog/the-six-times-to-derate-your-motor-to-save-its-life-part-2/), consulta 2026-07-23) y el factor de servicio exigido por el ambiente corrosivo.

### 3.3. Corrosividad del ambiente exterior

3.3.1. El laboratorio se ubica dentro de una planta de hipoclorito de calcio; la atmósfera exterior combina Cl₂ y ClO⁻ (oxidantes fuertes), polvo de Ca(ClO)₂ y humedad alta (84 % media). La jerarquía de materiales documentada para este servicio es: PRFV con resina viniléster como primera opción (las resinas Derakane se especifican expresamente para cloro e hipoclorito; [INEOS — Derakane Resin Selection Guide](http://www.ineos.com/globalassets/ineos-group/businesses/ineos-composites/markets/corrosion/derakane-resin-selection-guide.pdf), consulta 2026-07-23), polipropileno como alternativa sólida a temperatura ambiente, acero con recubrimiento epóxico solo como opción presupuestal con inspección programada, y acero galvanizado descartado. El acero inoxidable 304/316 en la corriente de cloro sufre picadura y agrietamiento por corrosión bajo tensión, por lo que no es primera opción para carcasa de ventilador, aunque se acepta inox 316L en elementos de baja solicitación química directa (rejillas, mallas, ferretería) por disponibilidad y fabricación local ([SysTech — Ventilation of Corrosive Environments](https://www.systech-design.com/industrial-ventilation/ventilation-of-corrosive-environments/), consulta 2026-07-23).

3.3.2. Regla de especificación adoptada para todo el sistema: PRFV viniléster o PP en la máquina de impulsión; marcos de filtro plásticos y portafiltros inox 304/316; rejillas y malla anti-insectos en inox 316L; damper de alivio en aluminio extruido 6063-T5 o línea severe-environment; ferretería y soportes inox 316 (A4) con aislamiento dieléctrico frente a estructura galvanizada; sellantes de silicona RTV neutra; conexión flexible de hipalón; instrumentos en gabinete IP66 cuando se monten hacia el exterior.

## 4. Metodología de investigación

4.1. La investigación se estructuró en cinco frentes ejecutados en paralelo con consulta web el 2026-07-23: (i) condiciones climáticas de diseño del sitio (IDEAM/ASHRAE/proxies aeroportuarios y verificación de densidad por gas ideal); (ii) ventiladores para ambiente corrosivo (Greenheck, Hartzell, New York Blower, Plastec, Sodeca, Soler & Palau, Systemair); (iii) filtros MERV 13-14 y equivalencias ISO 16890/EN 779 (Camfil, AAF, Koch, Freudenberg y canal colombiano); (iv) rejillas de exfiltración, dampers barométricos de alivio y mallas anti-insectos (Greenheck, Ruskin, Nailor, TROX, Halton, Titus, fabricantes nacionales); y (v) instrumentación de presión diferencial y accesorios de montaje (Dwyer, Setra, Siemens, Honeywell).

4.2. Criterios de aceptación de fuentes: se privilegiaron fichas y catálogos de fabricante con datos de desempeño ensayados (AMCA 210/500-D, ASHRAE 52.2, ASHRAE 70); toda cifra comercial se cita con URL y fecha de consulta. Las magnitudes sin fuente de catálogo concreta se marcan como «dato típico» y las pendientes de validación comercial como «por confirmar con proveedor». El punto de selección del ventilador se definió en condiciones de catálogo (3 840 m³/h @ 260 Pa, ρ = 1.2 kg/m³) aplicando el método del Ejemplo 3 de FE-1600, de modo que la selección exacta de tamaño y RPM se realice con el software del fabricante (CAPS de Greenheck o equivalente).

## 5. Descripción funcional del sistema

5.1. Secuencia de operación. Un ventilador centrífugo de impulsión toma aire exterior, lo hace atravesar una etapa de filtración de dos niveles (prefiltro MERV 8 + filtro final MERV 13-14) y lo inyecta directamente al laboratorio a 8 m/s (presión dinámica de inyección de 28 Pa en el sitio), sin red de ductos de distribución. El aporte continuo de 3 840 m³/h (12 renovaciones/h) eleva la presión interior por encima de la exterior; el aire sale del recinto por tres rejillas de exfiltración de 353×336 mm provistas de malla anti-insectos y por las infiltraciones de la envolvente.

5.2. Control de presurización. El set-point es +25 Pa con mínimo admisible de +12.5 Pa. El elemento final de control es un damper de alivio barométrico con contrapeso calibrable: permanece cerrado mientras el diferencial interior-exterior sea inferior al ajuste y abre progresivamente cuando lo supera, descargando el exceso de caudal y estabilizando la presión de sala. Dado que el contrapeso actúa sobre un diferencial de presión y no sobre caudal, el ajuste a +25 Pa es válido a cualquier altitud; la posición de equilibrio de apertura sí cambia con la densidad, por lo que la calibración final se ejecuta en comisionamiento con micromanómetro (práctica documentada por [Halton BRD](https://www.halton.com/app/uploads/2020/08/Halton-BRD-datasheet-2024.pdf), consulta 2026-07-23). Con filtro limpio (ΔP total 95 Pa en el sitio) el ventilador entrega más presión de la necesaria y el damper trabaja más abierto; a medida que el filtro se carga hasta su ΔP final (190 Pa en el sitio), el damper cierra y mantiene la consigna. Esta compensación pasiva es la razón por la que el damper es obligatorio y no opcional (ver §3.2.4).

5.3. Lazo de medición y alarma. Un transmisor de presión diferencial (4-20 mA, rango 0-62.5 Pa) mide interior contra una referencia exterior protegida del viento y del ambiente clorado; sus relés (o el PLC/BMS del cliente) generan alarma baja a +12.5 Pa (pérdida de presurización: riesgo de ingreso de insectos, polvo y cloro) y alarma alta a +40 Pa (damper atascado), con retardo de 30-60 s para evitar falsas alarmas por apertura de puerta (dato típico de diseño). Un manómetro diferencial de lectura local (Magnehelic 0-60 Pa) en la puerta o pared del laboratorio permite verificación visual sin instrumentación auxiliar. El esquema corresponde al lazo documentado para presurización de edificios comerciales: sensor diferencial interior-exterior cuya señal supervisa el elemento de alivio ([Trane Engineers Newsletter ADM-APN003](https://www.trane.com/content/dam/Trane/Commercial/global/products-systems/education-training/engineers-newsletters/airside-design/admapn003en_0502.pdf), consulta 2026-07-23).

5.4. Exclusiones de insectos y polvo. La barrera es triple: presión positiva permanente (flujo neto hacia afuera por cualquier abertura), filtración MERV 13-14 del aire de impulsión (E3 ≥ 90 % para partículas de 3-10 µm según ASHRAE 52.2) y malla anti-insectos inox 316 de 18×18 (abertura ≈1 mm) en las rejillas de exfiltración, que impide el ingreso por las bocas de salida cuando el sistema está detenido.

## 6. Análisis por componente

### 6.1. Ventilador de impulsión

6.1.1. Punto de selección: 3 840 m³/h (2 260 CFM) @ 260 Pa a densidad estándar (equivalente a 190 Pa en el sitio, escenario filtro cargado). El punto exige centrífugo de álabes curvados hacia atrás: los axiales de PRFV son máquinas de baja presión (<1 in c.a. en la mayoría de líneas) y quedan descartados con la carga de un MERV 13-14; los centrífugos de álabes hacia atrás ofrecen eficiencia alta, potencia no sobrecargante y mejor comportamiento frente al ensuciamiento progresivo del filtro.

**Tabla 3.** Comparativa de ventiladores candidatos (consulta 2026-07-23).

| Fabricante / línea | Tipo y material | Pros | Contras | Fuente |
|---|---|---|---|---|
| Greenheck BCSW-FRP | Centrífugo álabes curvados atrás, PRFV poliéster ignífugo, opción velo Nexus para oxidantes; AMCA Spark A; ASTM C582/D4167 | Certificación AMCA; representante oficial en Bogotá (Prime Lines HVAC); amplio rango (300-150 000 CFM) | Selección exacta vía software CAPS (por confirmar tamaño/RPM con proveedor) | [Catálogo BCSW-FRP](https://content.greenheck.com/public/DAMProd/Original/10002/BCSWFRP_catalog.pdf); [rep. Colombia](https://www.greenheck.com/find-my-rep/2973_southamerica_colombia) |
| New York Blower FRP Fume Exhauster | Centrífugo BI, rueda viniléster PRFV, buje/eje encapsulados | La rueda de viniléster es la especificación ideal para cloro; sello AMCA | Sin filial en Colombia; importación (plazo máx. ~3 meses, dato cliente 2026-07-23) | [NYB FRP Fume Exhauster](https://www.nyb.com/frp-fume-exhauster/) |
| Hartzell Series 41 FRP | Centrífugo curvado atrás, rueda FA de PRFV de una pieza | Sin juntas que atrapen corrosivos; guía de selección anticorrosiva del fabricante | Sobredimensionado en gama; sin canal local confirmado | [Catálogo Hartzell Fiberglass (PDF)](https://hartzellairmovement.com/wp-content/uploads/2023/05/25377-Hartzell-Fiberglass-Ventilators_Centrifugal-Exhausters-Catalog-RA.pdf) |
| Sodeca CPV | Centrífugo simple aspiración, envolvente y turbina PP | Filial Sodeca Colombia con catálogo 60 Hz local; plazos y repuestos simples | PP inferior al viniléster en oxidantes fuertes; verificar curva en el punto | [Sodeca CPV](https://www.sodeca.com/es/sistemas-de-ventilacion-extraccion/cpv-p1000000071); [catálogo Colombia](https://www.sodeca.co/files/catalogs/es/SODECA_CT18_catalogo_resumen_CO.pdf) |
| Plastec 25/30 | Centrífugo PP directo, sin metal en la corriente | «Polypropylene has the best resistance against acids and corrosion»; despacho 48 h desde EE. UU. | Álabes hacia adelante = mayor ruido; sin canal local | [Plastec Series](https://www.plastecventilation.com/collections/plastec-series) |
| Soler & Palau línea PP | Centrífugo PP anticorrosivo | Filial S&P Colombia; vida útil declarada 3-4 veces la del metálico | Modelo exacto por confirmar con la filial | [S&P Catálogo Industrial (PDF)](https://www.solerpalau.mx/ASW/recursos/cata/Industrial.pdf) |
| Acero + epóxico (p. ej. Greenheck USF/CSW) | Centrífugo acero con polvo epóxico horneado | Opción económica | El cloro ataca cualquier defecto del recubrimiento; solo segunda línea con inspección programada | [Greenheck USF/CSW catalog (PDF)](https://z1.grr.object.ussignal.com/AMCA_PROD/CRP/26743.2/Catalog/USFD%20USF%20CSW%20%2000.CVI.1033%20R4%2011-2018.pdf) |

6.1.2. Motor: 1.0 HP TEFC, 1 800 RPM (4 polos, 60 Hz), clase de aislamiento F, IP55 mínimo, ejecución severe duty con pintura epóxica y protección interna anticorrosiva (referencias de especificación: [Leeson/Regal Severe Duty (PDF)](https://www.regalrexnord.com/-/media/documents/brands/literature/industries/leeson_product_catalog_1050.pdf); [Baldor-Reliance IEEE 841XL](https://www.baldor.com/mvc/DownloadCenter/Files/9AKK108319), consulta 2026-07-23). El motor se monta fuera de la corriente de aire, configuración estándar en todos los centrífugos PRFV citados. Tensión y fases: 440 V, 3φ, 60 Hz (confirmado por el cliente, 2026-07-23).

### 6.2. Filtración

6.2.1. La clasificación MERV de ASHRAE 52.2 se basa en la eficiencia mínima compuesta en tres rangos: E1 (0.3-1.0 µm), E2 (1-3 µm), E3 (3-10 µm) ([ASHRAE 52.2-2017 (PDF)](https://www.ashrae.org/File%20Library/Technical%20Resources/COVID-19/52_2_2017_COVID-19_20200401.pdf), consulta 2026-07-23). MERV 13 exige E2 ≥ 90 % y E3 ≥ 90 %; MERV 14 añade E1 ≥ 75 %. Para el objetivo declarado (insectos, objetos extraños, polvo) MERV 13 basta; MERV 14 da margen ante la carga de polvo de la planta. Equivalencias aproximadas: MERV 13 ≡ ePM1 50-60 % (ISO 16890) ≡ F7 (EN 779); MERV 14 ≡ ePM1 60-70 % ≡ F8, confirmadas por la ficha del propio fabricante ([Camfil Durafil ES2 (PDF)](https://cdn.lsicloud.net/pandhwhsal/documents/855080-003.pdf), consulta 2026-07-23).

**Tabla 4.** Comparativa de filtros finales MERV 13-14 (velocidad frontal de catálogo 500 fpm = 2.54 m/s; consulta 2026-07-23).

| Fabricante / modelo | Clase | Marco | ΔP inicial catálogo | ΔP final recomendada | Fuente |
|---|---|---|---|---|---|
| Camfil Durafil ES2 | MERV 14 / ePM1 70 | 100 % plástico (ABS/poliestireno), junta en cabezal | ≤ 0.32 in c.a. ≈ 80 Pa | 375 Pa máx. (cambiar al duplicar ΔP inicial) | [Ficha Camfil 855080-003 (PDF)](https://cdn.lsicloud.net/pandhwhsal/documents/855080-003.pdf) |
| AAF VariCel VXL | MERV 14 | Plástico HIPS + ABS, sin metal | ≈ 0.40-0.45 in c.a. ≈ 100-112 Pa (dato típico, leído de curva) | 500 Pa máx. | [AAF AFP-1-162 (PDF)](https://aafterms.aafintl.com/-/media/files/aaf/commercial-and-industrial/us-products/box-filters/varicel-vxl/varicel-vxl_prod_mark_sht_afp-1-162.pdf) |
| Freudenberg Viledon MaxiPleat MX 85 | F8 / ePM1 65 % (≈ MERV 14) | Plástico, paquete fundido estanco | 135-180 Pa (familia MaxiPleat) | ≈ 450 Pa (dato típico clase F) | [Ficha MaxiPleat (PDF)](https://menardifilters.se/wp-content/uploads/MaxiPleat_DS_02-CC-038-EN_low.pdf) |
| Koch Multi-Pleat Green13 | MERV 13 | Cartón hidrófugo + rejilla acero galvanizado | ≈ 0.30-0.40 in c.a. (dato típico plisados MERV 13) | ≈ 250 Pa (dato típico) | [Koch Green13 (PDF)](https://www.airfilterplus.com/wp-content/uploads/2022/03/Multi-Pleat-Green-13-2021.pdf) |

6.2.2. Decisión de diseño: etapa 1, prefiltro plisado MERV 8 (ΔP limpio 50-75 Pa, final 250 Pa; referencia [Camfil 30/30 (PDF)](https://cdn.lsicloud.net/pandhwhsal/documents/406331002-SPS.pdf), consulta 2026-07-23); etapa 2, filtro final V-bank MERV 13-14 con marco plástico. Los valores de diseño congelados para la etapa final son ΔP limpio 80 Pa estándar (59 Pa en el sitio) y ΔP final 210 Pa estándar (154 Pa en el sitio), coherentes con el Durafil ES2 y conservadores frente al criterio de 375 Pa de catálogo. El prefiltro retiene la fracción gruesa (polvo, insectos, fibras) y multiplica la vida útil del filtro final; los V-bank citados integran fijación frontal para el prefiltro. Se evita el marco galvanizado en la corriente (Koch Green13) y se especifican portafiltros inox 304/316 con junta continua de poliuretano (referencia [Camfil MagnaFrame II](https://www.camfil.com/en-ca/products/housings-frames--louvers/filter-holding-frames/filter-holding-frames/magnaframe-ii-gasket-seal-_-47771), consulta 2026-07-23).

6.2.3. Disponibilidad local: AAF/Flanders vía Filter Tech S.A.S. y Air Solutions Colombia (Bogotá); Camfil vía ITECO y RGD Aire; fabricación nacional de reemplazos compatibles por CARVEL S.A./Workclean ([filtrosdeaireacondicionado.com](https://filtrosdeaireacondicionado.com/); [airsolutionscolombia.com](https://www.airsolutionscolombia.com/productos); [iteco.com.co](https://www.iteco.com.co/nuestras-marcas/); [carvel.com.co](https://carvel.com.co/catalogo-workclean/filtros-de-aire-acondicionado-tipo-cartucho-fdcjm/), consulta 2026-07-23). Conviene congelar la especificación en términos MERV/ePM1 + dimensiones 24×24 in para poder alternar proveedores de repuestos.

### 6.3. Rejillas de exfiltración

6.3.1. Tres rejillas de 353×336 mm (área facial unitaria 0.1187 m²) descargan el caudal a velocidad facial de 3 m/s con ΔP de 11 Pa en el sitio (cierre de orificio, C_d = 0.60). El tipo indicado para máxima área libre es eggcrate (panal) ½×½×½ in, con área libre de ≈90 % según catálogo ([Airfoil RC-FCR5](https://airfoil.com.au/product/removable-core-fixing-clip-eggcrate-grille-rc-fcr5/), consulta 2026-07-23); la malla anti-insectos inox 316 de 18×18 aporta ≈48-51 % de área abierta ([tabla de especificaciones Industrial Metal Mesh](https://www.industrialmetalmesh.com/sale-54819921-micron-304-316l-stainless-steel-wire-mesh-screen-filter-mesh.html), consulta 2026-07-23). El área neta combinada (≈45 % del área facial, dato típico) es la base del cálculo de la memoria.

**Tabla 5.** Comparativa de rejillas candidatas (consulta 2026-07-23).

| Producto | Tipo | Área libre | Materiales | Pros / contras | Fuente |
|---|---|---|---|---|---|
| Titus 50F / 50R | Eggcrate retorno ½ in | «Highest free area of any return grille» (~90 %, dato típico de la categoría) | Aluminio; versión íntegramente inox disponible | Única con ejecución inox de fábrica; importación | [Titus 50F (PDF)](https://www.titus-hvac.com/file/1228/50F_50Rrprod_specialized_2017.pdf) |
| Krueger EGC5 | Eggcrate ½ in | «Maximizes the free area» | Aluminio | Amplia gama de tamaños; no inox | [Krueger EGC5](https://www.krueger-hvac.com/Catalog%20Home/Grilles/Grilles%20-%20Return/EGC5) |
| Laminaire (Colombia) | Rejillas y difusores a pedido | Según diseño | Aluminio; fabricación local a medida | Permite 353×336 exacto y marco para malla; confirmar ejecución inox | [laminaire.net](https://laminaire.net/) |
| ProAire S.A.S (Bogotá) | Rejillas con corte láser a medida | Según diseño | Inox 316 fabricable bajo pedido | Vía más robusta para inox 316L local | [proairecolombia.com](https://www.proairecolombia.com/productos/rejillas-y-difusores.html) |

6.3.2. Decisión: rejilla eggcrate inox 316L (o aluminio anodizado como alternativa interior) con malla anti-insectos inox 316 18×18 montada en marco desmontable para limpieza; aislamiento del par galvánico malla-inox/marco-aluminio si se mezclan materiales (dato típico de ingeniería).

### 6.4. Damper de alivio barométrico

6.4.1. El damper barométrico es un backdraft damper con presión de inicio de apertura ajustable por contrapeso; es la solución pasiva estándar para controlar presurización positiva sin controles activos ([Greenheck, Backdraft & Pressure Relief Dampers (PDF)](https://content.greenheck.com/public/DAMProd/Original/10002/BackdraftDampers_catalog.pdf), consulta 2026-07-23). El set-point de +25 Pa ≈ 0.10 in c.a. cae dentro del rango de ajuste de los candidatos.

**Tabla 6.** Comparativa de dampers de alivio (consulta 2026-07-23).

| Fabricante / modelo | Rango de ajuste start-open | Materiales | Pros / contras | Fuente |
|---|---|---|---|---|
| Greenheck BR-40/41/42 y SEBR-10 (severe environment) | Seleccionable 0.05-0.30 in c.a. (12-75 Pa) — cubre +25 Pa | SEBR: construcción ambiente severo | Línea severe-environment pertinente para hipoclorito; canal Greenheck en Bogotá | [SEBR-10 submittal (PDF)](https://content.greenheck.com/public/DAMProd/Original/10002/SEBR10Series_submittal.pdf) |
| Ruskin CBD6 / BD6 | Control de presión estática hasta 0.25 in c.a. (62 Pa) | Aluminio extruido 6063-T5 «corrosion resistant» | Todo aluminio, idóneo para cloro; el set-point queda cerca del límite inferior del rango | [Ruskin BD6](https://www.ruskin.com/model/bd6) |
| Nailor 1390CB | Contrapeso externo 360°, «pressure relief at extremely low pressure differentials» | Opción aluminio extruido 6063-T5; sellos neopreno | Rodamientos de bolas: máxima sensibilidad a bajos diferenciales; importación | [Nailor 1390CB (PDF)](https://nailor.com/sites/default/files/documents/1390CB_B_0_0.pdf) |
| Halton BRD | Apertura mínima 30-200 Pa; ajustable hasta 300 Pa | Construcción marina | Sobrespecificado en presión; el mínimo de 30 Pa excede el set-point de 25 Pa | [Halton BRD (PDF)](https://www.halton.com/app/uploads/2020/08/Halton-BRD-datasheet-2024.pdf) |

6.4.2. Decisión: damper barométrico con contrapeso ajustable en el rango 12-75 Pa, construcción aluminio extruido 6063-T5 o línea severe-environment (Greenheck SEBR-10 como primera opción por canal local; Ruskin CBD6 y Nailor 1390CB-EAF como alternativas), con ensayos AMCA 500-D y calibración final en comisionamiento. Se descartan marcos galvanizados estándar. El damper se dimensiona para el caudal de alivio de diseño con velocidad facial ≤ 2.5 m/s (dato típico, baja pérdida y sin ruido).

### 6.5. Instrumentación de presión diferencial

**Tabla 7.** Comparativa de instrumentos candidatos (consulta 2026-07-23).

| Instrumento | Rango / salida | Precisión / protección | Pros / contras | Fuente |
|---|---|---|---|---|
| Dwyer Magnehelic 2000-00 (indicador local) | 0-0.25 in c.a. (0-62 Pa) | ±2 % FS; caja aluminio con ensayo niebla salina 168 h; opción bisel inox | Estándar de facto; set-point +25 Pa al 40 % de escala; distribuidores en Colombia | [Skilltech — tabla serie 2000](https://skilltech.com.br/produto/manometro-para-pressao-diferencial-magnehelic-serie-2000/) |
| Dwyer MS-121(-LCD) Magnesense (transmisor) | 0.1/0.25/0.5 in c.a. seleccionables (25/62.5/125 Pa); 4-20 mA 2 hilos | ±1 % FS; NEMA 4X (IP66); constante de tiempo ajustable 0.5-15 s | Primera opción: protección IP66 crítica en ambiente clorado; amortigua ráfagas de viento | [Catálogo MS (PDF)](https://www.transcat.com/media/pdf/MS_cat.pdf) |
| Setra 264 (transmisor alternativo) | 0-0.25 in c.a. (0-62 Pa); 4-20 mA | ±0.25/±0.4/±1 % FS; sobrepresión 10 psi | Elemento capacitivo inox, alta estabilidad; suministro por importación (por confirmar stock) | [Datasheet Setra 264 (PDF)](https://www.setra.com/hubfs/Product_Data_Sheets/Setra_Model_264_Data_Sheet.pdf) |
| Siemens QBM2130-1U (transmisor alternativo) | 0-100 Pa; 4-20 mA | IP42 | Viable si el BMS es Siemens; IP42 exige gabinete adicional | [Siemens Industry Mall](https://mall.industry.siemens.com/mall/en/WW/Catalog/Products/10510770) |
| Dwyer Photohelic 3000MR-00AV (indicador + alarmas) | 0-0.25 in c.a.; 2 relés SPDT | Repetibilidad switch 1 % | Genera alarma alta/baja sin PLC si el cliente no tiene BMS | [Northeast Controls](https://nciweb.net/pressure1.htm) |

6.5.1. Arquitectura del lazo (detalle en HD-INST-001): transmisor MS-121 entre el interior y una referencia exterior protegida (caja estática de pared orientada a sotavento), alarma baja +12.5 Pa, alarma alta +40 Pa, retardo 30-60 s; Magnehelic 2000-00 de lectura local; damper barométrico como elemento final pasivo. El lazo activo con variador de frecuencia solo se justifica si hay aperturas frecuentes de puerta o exigencia de registro BMS (dato típico de ingeniería; referencia de método [AIVC airbase_7469 (PDF)](https://www.aivc.org/sites/default/files/airbase_7469.pdf), consulta 2026-07-23). Disponibilidad Dwyer en Colombia: Vía Industrial (Bogotá/Cali), RS Importaciones y Suministros, SICO Global ([viaindustrial.com](https://www.viaindustrial.com/dwyer/marca/), consulta 2026-07-23).

### 6.6. Accesorios de montaje

6.6.1. Ferretería y soportes: inox AISI 316 / clase A4 como mínimo (el molibdeno mejora la resistencia a picadura y corrosión por rendija frente a cloruros; [Marsh Fasteners](https://marshfasteners.com/304-vs-316-stainless-steel-bolts/), consulta 2026-07-23), con aislamiento dieléctrico frente a estructura galvanizada. Los soportes estándar zincados de los instrumentos se sustituyen por fabricación local en inox 316; los cuerpos de aluminio fundido de los instrumentos no se montan a la intemperie.

6.6.2. Sellantes: silicona RTV neutra como primera opción (compatible con hipoclorito según [Chemical Resistance of RTV Silicone Sealants (PDF)](https://irp.cdn-website.com/63168859/files/uploaded/Chemical%20Resistance%20of%20RTV%20Silicone%20Sealants%20Chart.pdf), consulta 2026-07-23); se evita la silicona acetoxi (libera ácido acético corrosivo) y el poliuretano en exposición directa a cloro gaseoso (clasificación «X» en [Apache Pipeline — tabla PU (PDF)](https://www.apachepipe.com/assets/chemical-resistance-table.pdf), consulta 2026-07-23).

6.6.3. Conexión flexible del ventilador: hipalón (CSM), material recomendado para exterior por resistencia química, ozono y envejecimiento ([Hardcast Hypalon Flexible Duct Connectors (PDF)](https://6c2bd45d09da3c66a408-2b16a407535c695c8a76f8b06a56f342.ssl.cf2.rackcdn.com/GWB%20%20eCatalog%2006-25-16.pdf), consulta 2026-07-23), con bandas de amarre inox 316 en lugar del galvanizado estándar.

## 7. Marco normativo

7.1. Ventilación y renovaciones de aire: ANSI/ASHRAE 62.1 como referencia de calidad de aire interior y ANSI/ASHRAE 170 (ventilación de instalaciones de salud) como referencia de tasas de renovación y niveles de presurización; las 12 renovaciones/h adoptadas superan holgadamente los mínimos de ambas para el uso previsto (dato típico de aplicación).

7.2. Filtración: ANSI/ASHRAE 52.2-2017 (clasificación MERV, base de la especificación) e ISO 16890 (equivalencia ePM1 exigible en informes de ensayo de proveedores internacionales); EN 779:2012 como referencia heredada (F7/F8).

7.3. Ventiladores y dampers: AMCA 210/211 (ensayo y certificación de desempeño), AMCA 500-D (caída de presión y fuga de dampers), AMCA 99 (construcción Spark A), ASTM C582 y ASTM D4167 (laminados PRFV), ASHRAE 70 (medición de rejillas y difusores).

7.4. Instalación eléctrica: RETIE (Reglamento Técnico de Instalaciones Eléctricas, Colombia) y NTC 2050 (Código Eléctrico Colombiano) para acometida, protecciones, puesta a tierra y certificación de la instalación del motor y el tablero de control; NEMA MG-1 / IEC 60034-1 para derateo del motor por altitud; IEEE 841 como referencia de ejecución severe duty.

7.5. Seguridad ocupacional: OSHA 29 CFR 1910.1450 (exposición ocupacional a químicos peligrosos en laboratorios) como referencia de buena práctica de ventilación de laboratorios, complementada por la Resolución 0312 de 2019 (estándares mínimos de seguridad y salud en el trabajo, Colombia).

7.6. Protección anticorrosiva: ISO 12944 (pinturas y recubrimientos; el ambiente corresponde a categoría de corrosividad alta, C5, por la combinación cloro/humedad — dato típico de clasificación) y prácticas NACE/AMPP para selección de materiales en servicio clorado.

## 8. Conclusiones y selección recomendada

8.1. La corrección de densidad por altitud (k = 0.733) es el factor que gobierna el diseño: reduce la presión disponible del ventilador y la ΔP de todos los elementos, convierte al damper de alivio en componente obligatorio (la configuración sin damper solo alcanza 19.6 Pa) y obliga a seleccionar el ventilador en el punto equivalente de catálogo 3 840 m³/h @ 260 Pa.

8.2. Selección recomendada: (i) ventilador centrífugo PRFV de álabes curvados hacia atrás, Greenheck BCSW-FRP (canal local Prime Lines HVAC, Bogotá) con NYB FRP Fume Exhauster y Sodeca CPV-PP como alternativas, motor 1.0 HP TEFC severe duty epóxico; (ii) filtración en dos etapas, prefiltro MERV 8 + filtro final V-bank MERV 13-14 de marco plástico (Camfil Durafil ES2 MERV 14 como referencia de diseño; AAF VariCel VXL y Freudenberg MaxiPleat MX 85 como alternativas), portafiltros inox 304/316; (iii) tres rejillas eggcrate inox 316L de 353×336 mm con malla anti-insectos inox 316 18×18 desmontable, fabricación local a medida (ProAire/Laminaire); (iv) damper barométrico de alivio Greenheck SEBR-10 (rango 12-75 Pa) calibrado a +25 Pa en comisionamiento, con Ruskin CBD6 y Nailor 1390CB-EAF como alternativas; (v) transmisor Dwyer MS-121 (0-62.5 Pa, 4-20 mA, NEMA 4X) con alarmas +12.5/+40 Pa y Magnehelic 2000-00 de lectura local; (vi) ferretería inox 316, sellante silicona RTV neutra y conexión flexible de hipalón.

8.3. Puntos pendientes de confirmación comercial (marcados «por confirmar con proveedor» en las hojas de datos): tamaño y RPM exactos del ventilador (software del fabricante) y curvas ΔP-caudal específicas del filtro final seleccionado. La tensión de la red (440 V, 3φ, 60 Hz) y el plazo máximo de entrega (~3 meses) fueron confirmados por el cliente el 2026-07-23.

## 9. Referencias

Todas las URL fueron consultadas el 2026-07-23.

1. Twin City Fan, *Fan Engineering FE-1600 — Temperature & Altitude Effects on Fans*: http://eu.tcf.com/wp-content/uploads/sites/4/2018/06/Temperature-Altitude-Effects-on-Fans-FE-1600-1.pdf
2. CaptiveAire, *Design Conditions for Selected Locations, ASHRAE 2009* (Bogotá/El Dorado): https://www.captiveaire.com/catalogcontent/fans/sup_mpu/doc/winter_summer_design_temps_us.pdf
3. Alcaldía de Cajicá, *Aspectos generales* (PDF): https://www.cajica.gov.co/docdown/archi/2022/Cartografia/1.1.%20ASPECTOS%20GENERALES.pdf
4. Weather Atlas, clima de Cajicá: https://www.weather-atlas.com/en/colombia/cajica-climate
5. INEOS Composites, *Derakane Resin Selection Guide*: http://www.ineos.com/globalassets/ineos-group/businesses/ineos-composites/markets/corrosion/derakane-resin-selection-guide.pdf
6. SysTech Design, *Ventilation of Corrosive Environments*: https://www.systech-design.com/industrial-ventilation/ventilation-of-corrosive-environments/
7. Greenheck, catálogo BCSW-FRP: https://content.greenheck.com/public/DAMProd/Original/10002/BCSWFRP_catalog.pdf
8. New York Blower, FRP Fume Exhauster: https://www.nyb.com/frp-fume-exhauster/
9. Hartzell, *Fiberglass Ventilators & Centrifugal Exhausters*: https://hartzellairmovement.com/wp-content/uploads/2023/05/25377-Hartzell-Fiberglass-Ventilators_Centrifugal-Exhausters-Catalog-RA.pdf
10. Sodeca, CPV: https://www.sodeca.com/es/sistemas-de-ventilacion-extraccion/cpv-p1000000071
11. Plastec Ventilation, Plastec Series: https://www.plastecventilation.com/collections/plastec-series
12. Soler & Palau, Catálogo Industrial (México): https://www.solerpalau.mx/ASW/recursos/cata/Industrial.pdf
13. Greenheck, representante Colombia (Prime Lines HVAC): https://www.greenheck.com/find-my-rep/2973_southamerica_colombia
14. ANSI/ASHRAE 52.2-2017 (texto oficial): https://www.ashrae.org/File%20Library/Technical%20Resources/COVID-19/52_2_2017_COVID-19_20200401.pdf
15. Camfil, ficha Durafil ES2: https://cdn.lsicloud.net/pandhwhsal/documents/855080-003.pdf
16. AAF, VariCel VXL AFP-1-162: https://aafterms.aafintl.com/-/media/files/aaf/commercial-and-industrial/us-products/box-filters/varicel-vxl/varicel-vxl_prod_mark_sht_afp-1-162.pdf
17. Freudenberg, MaxiPleat (ficha Menardi): https://menardifilters.se/wp-content/uploads/MaxiPleat_DS_02-CC-038-EN_low.pdf
18. Camfil, portafiltros MagnaFrame II: https://www.camfil.com/en-ca/products/housings-frames--louvers/filter-holding-frames/filter-holding-frames/magnaframe-ii-gasket-seal-_-47771
19. Greenheck, *Backdraft & Pressure Relief Dampers* (mar. 2023): https://content.greenheck.com/public/DAMProd/Original/10002/BackdraftDampers_catalog.pdf
20. Greenheck, SEBR-10 submittal: https://content.greenheck.com/public/DAMProd/Original/10002/SEBR10Series_submittal.pdf
21. Ruskin, BD6: https://www.ruskin.com/model/bd6
22. Nailor, 1390CB: https://nailor.com/sites/default/files/documents/1390CB_B_0_0.pdf
23. Halton, BRD datasheet 2024: https://www.halton.com/app/uploads/2020/08/Halton-BRD-datasheet-2024.pdf
24. Titus, 50F/50R: https://www.titus-hvac.com/file/1228/50F_50Rrprod_specialized_2017.pdf
25. Industrial Metal Mesh, tabla malla inox (área abierta): https://www.industrialmetalmesh.com/sale-54819921-micron-304-316l-stainless-steel-wire-mesh-screen-filter-mesh.html
26. Building Science Corp., BA-0006 *Discussion of the Use of Transfer Grilles*: https://buildingscience.com/sites/default/files/migrate/pdf/BA-0006_Discuss_transfer_grilles.pdf
27. Dwyer/Transcat, catálogo serie MS Magnesense: https://www.transcat.com/media/pdf/MS_cat.pdf
28. Setra, Model 264 datasheet: https://www.setra.com/hubfs/Product_Data_Sheets/Setra_Model_264_Data_Sheet.pdf
29. Siemens, QBM2130-1U (Industry Mall): https://mall.industry.siemens.com/mall/en/WW/Catalog/Products/10510770
30. Skilltech, tabla Magnehelic serie 2000: https://skilltech.com.br/produto/manometro-para-pressao-diferencial-magnehelic-serie-2000/
31. Trane, Engineers Newsletter ADM-APN003 *Managing Commercial Building Pressurization*: https://www.trane.com/content/dam/Trane/Commercial/global/products-systems/education-training/engineers-newsletters/airside-design/admapn003en_0502.pdf
32. AIVC, airbase_7469 (control de presión diferencial): https://www.aivc.org/sites/default/files/airbase_7469.pdf
33. Vía Industrial, marca Dwyer Colombia: https://www.viaindustrial.com/dwyer/marca/
34. Hardcast, Hypalon Flexible Duct Connectors: https://6c2bd45d09da3c66a408-2b16a407535c695c8a76f8b06a56f342.ssl.cf2.rackcdn.com/GWB%20%20eCatalog%2006-25-16.pdf
35. Apache Pipeline, tabla de resistencia química de poliuretano: https://www.apachepipe.com/assets/chemical-resistance-table.pdf
36. *Chemical Resistance of RTV Silicone Sealants* (tabla): https://irp.cdn-website.com/63168859/files/uploaded/Chemical%20Resistance%20of%20RTV%20Silicone%20Sealants%20Chart.pdf
37. Marsh Fasteners, 304 vs 316 stainless bolts: https://marshfasteners.com/304-vs-316-stainless-steel-bolts/
38. ASHRAE/Silvertip, *High Altitude HVAC Design Considerations* (2023): https://silvertipconsultants.com/wp-content/uploads/2023/04/ASHRAE_High_Alt_Des_2023_04_28-Handout.pdf
39. Laminaire (fabricante colombiano de rejillas): https://laminaire.net/
40. ProAire S.A.S (Bogotá, rejillas y difusores): https://www.proairecolombia.com/productos/rejillas-y-difusores.html


# Informe de investigación: sistema de ventilación del laboratorio de análisis industrial

**Proyecto:** P2437-HV-INF-001 — BRINSA, planta Cajicá (Cundinamarca, Colombia)
**Documento:** informe_investigacion.md — Revisión 2
**Fecha de consulta de fuentes:** 2026-07-23 (REV0); revisión 1 emitida el 2026-07-27; revisión 2 emitida el 2026-07-27

**Nota de revisión REV2 — 2026-07-27:** actualización por uniformidad con el montaje típico instalado en la planta (`Montaje/DISENOFINAL.png`): ventilador axial mural (placa mural) Ø560 mm de transmisión directa, banco de filtración alojado en la cubierta intemperie, estructura de unión pernada al muro y malla de protección interior; se eliminan la caja/housing con transición, la conexión flexible y la persiana de REV1.

**Nota de revisión REV1 — 2026-07-27:** cambio de alcance del cliente — sistema sin presurización, ventilador axial, sin instrumentación de presión diferencial.

---

## 1. Objetivo

1.1. Seleccionar y documentar, con base en investigación de mercado y fuentes técnicas trazables, los equipos y componentes del sistema de ventilación del laboratorio de análisis industrial de BRINSA en Cajicá: ventilador axial de impulsión directa a través de muro, etapa de filtración MERV 13-14 y rejillas de descarga con malla anti-insectos.

1.2. La función del sistema es ventilar el recinto a 12 renovaciones/h (3 840 m³/h sobre 320 m³) con aire exterior filtrado, excluyendo polvo, objetos extraños e insectos del aire de impulsión. No se trata de un sistema de biocontención; por tanto se descarta expresamente la filtración HEPA.

## 2. Alcance

2.1. El informe cubre la investigación y selección de componentes del sistema completo de impulsión filtrada (3 840 m³/h, 12 renovaciones/h sobre 320 m³) y la descarga libre a la atmósfera por tres rejillas de 353×336 mm provistas de malla anti-insectos. Incluye las bases de diseño del sitio, la corrección de densidad por altitud, el análisis comparativo de opciones comerciales por componente, el marco normativo aplicable y la selección recomendada.

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
| ΔP rejillas (3 m/s, C_d = 0.60) | 11 Pa | 15 Pa |
| **ΔP total escenario cargado (selección)** | **165 Pa** | **225 Pa** |
| ΔP total escenario limpio | 70 Pa | 95 Pa |
| Potencia teórica de aire (η = 0.55) | 0.320 kW (0.43 HP) | — |

3.2.4. La pérdida en rejillas de 11 Pa a 3 m/s (cierre de orificio, C_d = 0.60) es una pérdida de descarga libre a la atmósfera: el aire sale del recinto por las tres rejillas sin que exista consigna de presión interior. En consecuencia, la ΔP total del sistema es la suma de la etapa filtrante y la descarga por rejillas (165 Pa en el sitio, escenario filtro cargado).

3.2.5. Sobre el motor: la potencia teórica corregida al sitio es 0.320 kW (0.43 HP) con eficiencia de ventilador axial provisional η = 0.55; aplicando un margen de servicio de 1.5 y redondeando al tamaño comercial se adopta provisionalmente un motor de 0.75 HP TEFC con tratamiento anticorrosivo, a confirmar contra la curva de catálogo de la selección final. El margen resultante absorbe el derateo por altitud (regla práctica NEMA MG-1: 3 % por cada 500 m sobre 1 000 msnm, es decir ≈9 % a 2 558 msnm; [NEMA MG-1 citado en motorsatwork.com](https://www.motorsatwork.com/from-the-blog/the-six-times-to-derate-your-motor-to-save-its-life-part-2/), consulta 2026-07-23) y el factor de servicio exigido por el ambiente corrosivo.

### 3.3. Corrosividad del ambiente exterior

3.3.1. El laboratorio se ubica dentro de una planta de hipoclorito de calcio; la atmósfera exterior combina Cl₂ y ClO⁻ (oxidantes fuertes), polvo de Ca(ClO)₂ y humedad alta (84 % media). La jerarquía de materiales documentada para este servicio es: PRFV con resina viniléster como primera opción (las resinas Derakane se especifican expresamente para cloro e hipoclorito; [INEOS — Derakane Resin Selection Guide](http://www.ineos.com/globalassets/ineos-group/businesses/ineos-composites/markets/corrosion/derakane-resin-selection-guide.pdf), consulta 2026-07-23), polipropileno como alternativa sólida a temperatura ambiente, acero con recubrimiento epóxico solo como opción presupuestal con inspección programada, y acero galvanizado descartado. El acero inoxidable 304/316 en la corriente de cloro sufre picadura y agrietamiento por corrosión bajo tensión, por lo que no es primera opción para carcasa de ventilador, aunque se acepta inox 316L en elementos de baja solicitación química directa (rejillas, mallas, ferretería) por disponibilidad y fabricación local ([SysTech — Ventilation of Corrosive Environments](https://www.systech-design.com/industrial-ventilation/ventilation-of-corrosive-environments/), consulta 2026-07-23).

3.3.2. Regla de especificación adoptada para todo el sistema: PRFV viniléster o PP en la máquina de impulsión; marcos de filtro plásticos y portafiltros inox 304/316; rejillas y malla anti-insectos en inox 316L; ferretería y soportes inox 316 (A4) con aislamiento dieléctrico frente a estructura galvanizada; sellantes de silicona RTV neutra; conexión flexible de hipalón.

## 4. Metodología de investigación

4.1. La investigación se estructuró en cuatro frentes ejecutados en paralelo con consulta web el 2026-07-23 (ampliada el 2026-07-27 para ventiladores axiales): (i) condiciones climáticas de diseño del sitio (IDEAM/ASHRAE/proxies aeroportuarios y verificación de densidad por gas ideal); (ii) ventiladores axiales para ambiente corrosivo (Aerovent/Twin City Fan, Greenheck, New York Blower, Plastec, Sodeca); (iii) filtros MERV 13-14 y equivalencias ISO 16890/EN 779 (Camfil, AAF, Koch, Freudenberg y canal colombiano); y (iv) rejillas de descarga y mallas anti-insectos (Titus, Krueger, fabricantes nacionales) con accesorios de montaje.

4.2. Criterios de aceptación de fuentes: se privilegiaron fichas y catálogos de fabricante con datos de desempeño ensayados (AMCA 210, ASHRAE 52.2, ASHRAE 70); toda cifra comercial se cita con URL y fecha de consulta. Las magnitudes sin fuente de catálogo concreta se marcan como «dato típico» y las pendientes de validación comercial como «por confirmar con proveedor». El punto de selección del ventilador se definió en condiciones de catálogo (3 840 m³/h @ 225 Pa, ρ = 1.2 kg/m³) aplicando el método del Ejemplo 3 de FE-1600, de modo que la selección exacta de tamaño y RPM se realice con el software de selección del fabricante.

## 5. Descripción funcional del sistema

5.1. Secuencia de operación. Un ventilador axial tubular de impulsión toma aire exterior, lo hace atravesar una etapa de filtración de dos niveles (prefiltro MERV 8 + filtro final MERV 13-14) y lo inyecta directamente al laboratorio, sin red de ductos de distribución. El aporte continuo de 3 840 m³/h (12 renovaciones/h) recorre el recinto y sale por tres rejillas de descarga de 353×336 mm provistas de malla anti-insectos y por las infiltraciones de la envolvente, descargando libremente a la atmósfera. El sistema no mantiene consigna de presión interior: la ΔP de las rejillas (11 Pa en el sitio) es únicamente la pérdida de la descarga.

5.2. Exclusión de polvo e insectos. La barrera es doble: filtración MERV 13-14 del aire de impulsión (E3 ≥ 90 % para partículas de 3-10 µm según ASHRAE 52.2), que retiene polvo, objetos extraños e insectos del caudal de entrada, y malla anti-insectos inox 316 de 18×18 (abertura ≈1 mm) en las rejillas de descarga, que impide el ingreso por las bocas de salida cuando el sistema está detenido.

## 6. Análisis por componente

### 6.1. Ventilador de impulsión

6.1.1. Punto de selección: 3 840 m³/h (2 260 CFM) @ 225 Pa a densidad estándar (equivalente a 165 Pa en el sitio, escenario filtro cargado). El punto corresponde a ≈0.9 in c.a., plenamente cubierto por ventiladores axiales murales y tubulares de PRFV (el catálogo 185 de Aerovent cubre 355-1 525 mm y hasta 370 Pa estática en su línea tubular de referencia; [Aerovent Catálogo 185 (PDF)](https://www.aerovent.com/wp-content/uploads/sites/2/2024/07/Fiberglass-Fans-Axial-Flow-Model-FBD-FDP-FRV-TFBD-VTFBD-Catalog-185.pdf), consulta 2026-07-27). En REV0, con el punto anterior más exigente, los axiales quedaron descartados frente al centrífugo de álabes curvados hacia atrás; el cambio de alcance del cliente reduce la presión de selección y hace viable el axial. En REV2 (2026-07-27) el tipo se concreta por uniformidad con el montaje típico instalado en la planta (`Montaje/DISENOFINAL.png`): **axial mural (placa mural) Ø560 mm de transmisión directa**, con el banco de filtración alojado en la cubierta intemperie, estructura de unión pernada al muro y malla de protección interior; ventajas: menor costo de equipo e instalación (montaje directo en muro, sin ductos), mantenimiento simple y uniformidad de repuestos con la planta. La contrapartida —menor eficiencia (η provisional 0.55), mayor sensibilidad de la curva a la carga del filtro y motor dentro de la corriente corrosiva (mitigado con ejecución encapsulada severe duty)— es aceptable dada la potencia involucrada (0.320 kW teóricos); la configuración de transmisión por bandas evaluada en REV1 queda documentada como alternativa.

**Tabla 3.** Comparativa de ventiladores axiales candidatos (consulta 2026-07-23, ampliada 2026-07-27; ajustada a tipo mural en REV2).

| Fabricante / línea | Tipo y material | Pros | Contras | Fuente |
|---|---|---|---|---|
| Sodeca HQD/HGT mural anticorrosivo — primera opción | Axial mural (placa mural) PRFV/epóxico, transmisión directa | Filial Sodeca Colombia con catálogo 60 Hz local; uniformidad con el montaje típico de la planta; plazos y repuestos simples | Verificar curva en el punto 3 840 m³/h @ 225 Pa y la ejecución anticorrosiva | [Sodeca](https://www.sodeca.com); [catálogo Colombia (PDF)](https://www.sodeca.co/files/catalogs/es/SODECA_CT18_catalogo_resumen_CO.pdf) |
| Greenheck mural (línea industrial) | Axial mural, acero con recubrimiento epóxico, transmisión directa | Representante oficial en Bogotá (Prime Lines HVAC); línea industrial amplia; certificación AMCA | Recubrimiento epóxico = segunda línea en ambiente clorado (inspección programada) | [Greenheck](https://www.greenheck.com); [rep. Colombia](https://www.greenheck.com/find-my-rep/2973_southamerica_colombia) |
| Aerovent / Twin City Fan (línea mural FRP) | Mural PRFV | Línea FRP anticorrosiva amplia (la línea tubular de referencia cubre 355-1 525 mm y hasta 370 Pa estática); laminado PRFV idóneo para cloro | Canal local por confirmar; importación | [Aerovent Catálogo 185 (PDF)](https://www.aerovent.com/wp-content/uploads/sites/2/2024/07/Fiberglass-Fans-Axial-Flow-Model-FBD-FDP-FRV-TFBD-VTFBD-Catalog-185.pdf) |
| New York Blower FRP mural | Mural PRFV viniléster | Experiencia consolidada del fabricante en laminados PRFV; sello AMCA | Sin filial en Colombia; importación (plazo máx. ~3 meses, dato cliente 2026-07-23) | [NYB](https://www.nyb.com/) |
| Plastec | Axial de polipropileno | «Polypropylene has the best resistance against acids and corrosion»; despacho 48 h desde EE. UU. | Verificar curva en el punto; sin canal local | [Plastec Series](https://www.plastecventilation.com/collections/plastec-series) |

6.1.2. Motor: 0.75 HP TEFC encapsulado (provisional, a confirmar con la curva de la selección final), clase de aislamiento F (H preferible), IP56 mínimo (IP66 preferible), ejecución severe duty con pintura epóxica, protección interna anticorrosiva y eje inox (referencias de especificación: [Leeson/Regal Severe Duty (PDF)](https://www.regalrexnord.com/-/media/documents/brands/literature/industries/leeson_product_catalog_1050.pdf); [Baldor-Reliance IEEE 841XL](https://www.baldor.com/mvc/DownloadCenter/Files/9AKK108319), consulta 2026-07-23). Con la transmisión directa el motor va en el cubo del impulsor, dentro de la corriente de aire, de ahí la ejecución encapsulada reforzada. Tensión y fases: 440 V, 3φ, 60 Hz (confirmado por el cliente, 2026-07-23).

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

### 6.3. Rejillas de descarga

6.3.1. Tres rejillas de 353×336 mm (área facial unitaria 0.1187 m²) descargan el caudal a velocidad facial de 3 m/s con ΔP de 11 Pa en el sitio (cierre de orificio, C_d = 0.60), como pérdida de descarga libre a la atmósfera. El tipo indicado para máxima área libre es eggcrate (panal) ½×½×½ in, con área libre de ≈90 % según catálogo ([Airfoil RC-FCR5](https://airfoil.com.au/product/removable-core-fixing-clip-eggcrate-grille-rc-fcr5/), consulta 2026-07-23); la malla anti-insectos inox 316 de 18×18 aporta ≈48-51 % de área abierta ([tabla de especificaciones Industrial Metal Mesh](https://www.industrialmetalmesh.com/sale-54819921-micron-304-316l-stainless-steel-wire-mesh-screen-filter-mesh.html), consulta 2026-07-23). El área neta combinada (≈45 % del área facial, dato típico) es la base del cálculo de la memoria.

**Tabla 5.** Comparativa de rejillas candidatas (consulta 2026-07-23).

| Producto | Tipo | Área libre | Materiales | Pros / contras | Fuente |
|---|---|---|---|---|---|
| Titus 50F / 50R | Eggcrate retorno ½ in | «Highest free area of any return grille» (~90 %, dato típico de la categoría) | Aluminio; versión íntegramente inox disponible | Única con ejecución inox de fábrica; importación | [Titus 50F (PDF)](https://www.titus-hvac.com/file/1228/50F_50Rrprod_specialized_2017.pdf) |
| Krueger EGC5 | Eggcrate ½ in | «Maximizes the free area» | Aluminio | Amplia gama de tamaños; no inox | [Krueger EGC5](https://www.krueger-hvac.com/Catalog%20Home/Grilles/Grilles%20-%20Return/EGC5) |
| Laminaire (Colombia) | Rejillas y difusores a pedido | Según diseño | Aluminio; fabricación local a medida | Permite 353×336 exacto y marco para malla; confirmar ejecución inox | [laminaire.net](https://laminaire.net/) |
| ProAire S.A.S (Bogotá) | Rejillas con corte láser a medida | Según diseño | Inox 316 fabricable bajo pedido | Vía más robusta para inox 316L local | [proairecolombia.com](https://www.proairecolombia.com/productos/rejillas-y-difusores.html) |

6.3.2. Decisión: rejilla eggcrate inox 316L (o aluminio anodizado como alternativa interior) con malla anti-insectos inox 316 18×18 montada en marco desmontable para limpieza; aislamiento del par galvánico malla-inox/marco-aluminio si se mezclan materiales (dato típico de ingeniería).

### 6.4. Accesorios de montaje

6.4.1. Ferretería y soportes: inox AISI 316 / clase A4 como mínimo (el molibdeno mejora la resistencia a picadura y corrosión por rendija frente a cloruros; [Marsh Fasteners](https://marshfasteners.com/304-vs-316-stainless-steel-bolts/), consulta 2026-07-23), con aislamiento dieléctrico frente a estructura galvanizada.

6.4.2. Sellantes: silicona RTV neutra como primera opción (compatible con hipoclorito según [Chemical Resistance of RTV Silicone Sealants (PDF)](https://irp.cdn-website.com/63168859/files/uploaded/Chemical%20Resistance%20of%20RTV%20Silicone%20Sealants%20Chart.pdf), consulta 2026-07-23); se evita la silicona acetoxi (libera ácido acético corrosivo) y el poliuretano en exposición directa a cloro gaseoso (clasificación «X» en [Apache Pipeline — tabla PU (PDF)](https://www.apachepipe.com/assets/chemical-resistance-table.pdf), consulta 2026-07-23).

6.4.3. Montaje del ventilador (REV2): sigue el montaje típico de la planta — estructura de unión en perfiles ASTM A36 galvanizados en caliente con pintura epóxica, pernada al muro con anclajes inox 316 (A4) y aislamiento dieléctrico; cubierta intemperie en PRFV o galvanizado G90 con pintura electrostática epóxica, embridada directamente a la placa mural del ventilador, que aloja el banco de filtración y dispone de acceso frontal para cambio de filtros; y malla de protección interior desmontable en la descarga. La conexión flexible de hipalón especificada en REV1 ([Hardcast Hypalon (PDF)](https://6c2bd45d09da3c66a408-2b16a407535c695c8a76f8b06a56f342.ssl.cf2.rackcdn.com/GWB%20%20eCatalog%2006-25-16.pdf)) ya no aplica: la cubierta se embrida directamente al ventilador.

## 7. Marco normativo

7.1. Ventilación y renovaciones de aire: ANSI/ASHRAE 62.1 como referencia de calidad de aire interior; las 12 renovaciones/h adoptadas superan holgadamente los mínimos aplicables al uso previsto (dato típico de aplicación).

7.2. Filtración: ANSI/ASHRAE 52.2-2017 (clasificación MERV, base de la especificación) e ISO 16890 (equivalencia ePM1 exigible en informes de ensayo de proveedores internacionales); EN 779:2012 como referencia heredada (F7/F8).

7.3. Ventiladores: AMCA 210/211 (ensayo y certificación de desempeño), AMCA 99 (construcción Spark A), ASTM C582 y ASTM D4167 (laminados PRFV), ASHRAE 70 (medición de rejillas y difusores).

7.4. Instalación eléctrica: RETIE (Reglamento Técnico de Instalaciones Eléctricas, Colombia) y NTC 2050 (Código Eléctrico Colombiano) para acometida, protecciones, puesta a tierra y certificación de la instalación del motor y su tablero; NEMA MG-1 / IEC 60034-1 para derateo del motor por altitud; IEEE 841 como referencia de ejecución severe duty.

7.5. Seguridad ocupacional: OSHA 29 CFR 1910.1450 (exposición ocupacional a químicos peligrosos en laboratorios) como referencia de buena práctica de ventilación de laboratorios, complementada por la Resolución 0312 de 2019 (estándares mínimos de seguridad y salud en el trabajo, Colombia).

7.6. Protección anticorrosiva: ISO 12944 (pinturas y recubrimientos; el ambiente corresponde a categoría de corrosividad alta, C5, por la combinación cloro/humedad — dato típico de clasificación) y prácticas NACE/AMPP para selección de materiales en servicio clorado.

## 8. Conclusiones y selección recomendada

8.1. La corrección de densidad por altitud (k = 0.733) sigue siendo el factor que gobierna la selección: reduce la presión disponible del ventilador y la ΔP de todos los elementos, y obliga a seleccionar en el punto equivalente de catálogo 3 840 m³/h @ 225 Pa. Ese punto, ≈0.9 in c.a., queda dentro del rango de los axiales murales y tubulares de PRFV, lo que habilita la configuración adoptada por el cliente en REV2 por uniformidad con la planta: ventilador axial mural Ø560 mm de transmisión directa montado directamente en el muro, sin ductos de impulsión.

8.2. Selección recomendada: (i) ventilador axial mural (placa mural) Ø560 mm PRFV/epóxico de transmisión directa, Sodeca HQD/HGT mural anticorrosivo como primera opción por canal local, con Greenheck mural, Aerovent/Twin City mural FRP, NYB FRP mural y Plastec PP como alternativas, motor 0.75 HP TEFC encapsulado severe duty epóxico en la corriente (provisional); (ii) filtración en dos etapas alojada en la cubierta intemperie, prefiltro MERV 8 + filtro final V-bank MERV 13-14 de marco plástico (Camfil Durafil ES2/ES3 MERV 14 como referencia de diseño; AAF VariCel VXL y Freudenberg MaxiPleat MX 85 como alternativas), portafiltros inox 304/316; (iii) tres rejillas eggcrate inox 316L de 353×336 mm con malla anti-insectos inox 316 18×18 desmontable, fabricación local a medida (ProAire/Laminaire); (iv) estructura de unión ASTM A36 galvanizada + pintura epóxica con ferretería inox 316, malla de protección interior y sellante silicona RTV neutra.

8.3. Puntos pendientes de confirmación comercial (marcados «por confirmar con proveedor» en las hojas de datos): tamaño y RPM exactos del ventilador (software de selección del fabricante), potencia final del motor contra la curva seleccionada, y curvas ΔP-caudal específicas del filtro final. La tensión de la red (440 V, 3φ, 60 Hz) y el plazo máximo de entrega (~3 meses) fueron confirmados por el cliente el 2026-07-23.

## 9. Referencias

Las URL de REV0 fueron consultadas el 2026-07-23; las incorporadas en REV1, el 2026-07-27.

1. Twin City Fan, *Fan Engineering FE-1600 — Temperature & Altitude Effects on Fans*: http://eu.tcf.com/wp-content/uploads/sites/4/2018/06/Temperature-Altitude-Effects-on-Fans-FE-1600-1.pdf
2. CaptiveAire, *Design Conditions for Selected Locations, ASHRAE 2009* (Bogotá/El Dorado): https://www.captiveaire.com/catalogcontent/fans/sup_mpu/doc/winter_summer_design_temps_us.pdf
3. Alcaldía de Cajicá, *Aspectos generales* (PDF): https://www.cajica.gov.co/docdown/archi/2022/Cartografia/1.1.%20ASPECTOS%20GENERALES.pdf
4. Weather Atlas, clima de Cajicá: https://www.weather-atlas.com/en/colombia/cajica-climate
5. INEOS Composites, *Derakane Resin Selection Guide*: http://www.ineos.com/globalassets/ineos-group/businesses/ineos-composites/markets/corrosion/derakane-resin-selection-guide.pdf
6. SysTech Design, *Ventilation of Corrosive Environments*: https://www.systech-design.com/industrial-ventilation/ventilation-of-corrosive-environments/
7. Aerovent (Twin City Fan), *Catálogo 185 — Fiberglass Axial Flow Fans FBD/FDP/FRV/TFBD/VTFBD* (abr. 2024): https://www.aerovent.com/wp-content/uploads/sites/2/2024/07/Fiberglass-Fans-Axial-Flow-Model-FBD-FDP-FRV-TFBD-VTFBD-Catalog-185.pdf
8. Greenheck, *Vane Axial Fans VAB/VAD*: https://content.greenheck.com/public/DAMProd/Original/10003/vane_axial_catalog.pdf
9. Greenheck, representante Colombia (Prime Lines HVAC): https://www.greenheck.com/find-my-rep/2973_southamerica_colombia
10. Sodeca: https://www.sodeca.com ; catálogo resumen Colombia: https://www.sodeca.co/files/catalogs/es/SODECA_CT18_catalogo_resumen_CO.pdf
11. New York Blower: https://www.nyb.com/
12. Plastec Ventilation, Plastec Series: https://www.plastecventilation.com/collections/plastec-series
13. ANSI/ASHRAE 52.2-2017 (texto oficial): https://www.ashrae.org/File%20Library/Technical%20Resources/COVID-19/52_2_2017_COVID-19_20200401.pdf
14. Camfil, ficha Durafil ES2: https://cdn.lsicloud.net/pandhwhsal/documents/855080-003.pdf
15. AAF, VariCel VXL AFP-1-162: https://aafterms.aafintl.com/-/media/files/aaf/commercial-and-industrial/us-products/box-filters/varicel-vxl/varicel-vxl_prod_mark_sht_afp-1-162.pdf
16. Freudenberg, MaxiPleat (ficha Menardi): https://menardifilters.se/wp-content/uploads/MaxiPleat_DS_02-CC-038-EN_low.pdf
17. Camfil, portafiltros MagnaFrame II: https://www.camfil.com/en-ca/products/housings-frames--louvers/filter-holding-frames/filter-holding-frames/magnaframe-ii-gasket-seal-_-47771
18. Titus, 50F/50R: https://www.titus-hvac.com/file/1228/50F_50Rrprod_specialized_2017.pdf
19. Industrial Metal Mesh, tabla malla inox (área abierta): https://www.industrialmetalmesh.com/sale-54819921-micron-304-316l-stainless-steel-wire-mesh-screen-filter-mesh.html
20. Building Science Corp., BA-0006 *Discussion of the Use of Transfer Grilles*: https://buildingscience.com/sites/default/files/migrate/pdf/BA-0006_Discuss_transfer_grilles.pdf
21. Hardcast, Hypalon Flexible Duct Connectors: https://6c2bd45d09da3c66a408-2b16a407535c695c8a76f8b06a56f342.ssl.cf2.rackcdn.com/GWB%20%20eCatalog%2006-25-16.pdf
22. Apache Pipeline, tabla de resistencia química de poliuretano: https://www.apachepipe.com/assets/chemical-resistance-table.pdf
23. *Chemical Resistance of RTV Silicone Sealants* (tabla): https://irp.cdn-website.com/63168859/files/uploaded/Chemical%20Resistance%20of%20RTV%20Silicone%20Sealants%20Chart.pdf
24. Marsh Fasteners, 304 vs 316 stainless bolts: https://marshfasteners.com/304-vs-316-stainless-steel-bolts/
25. ASHRAE/Silvertip, *High Altitude HVAC Design Considerations* (2023): https://silvertipconsultants.com/wp-content/uploads/2023/04/ASHRAE_High_Alt_Des_2023_04_28-Handout.pdf
26. Laminaire (fabricante colombiano de rejillas): https://laminaire.net/
27. ProAire S.A.S (Bogotá, rejillas y difusores): https://www.proairecolombia.com/productos/rejillas-y-difusores.html

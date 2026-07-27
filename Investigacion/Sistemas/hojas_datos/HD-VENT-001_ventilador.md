# Hoja de datos: ventilador axial de impulsión

| Campo | Valor |
|---|---|
| Código | HD-VENT-001 |
| Revisión | 1 |
| Fecha | 2026-07-27 |
| Proyecto | P2437-HV-INF-001 — BRINSA, laboratorio de análisis industrial, Cajicá |
| Etiqueta de equipo | VENT-001 (ventilador axial de impulsión) |

**Nota de revisión REV1 — 2026-07-27:** cambio de alcance del cliente — sistema sin presurización, ventilador axial en lugar de centrífugo, sin instrumentación de presión diferencial.

---

## 1. Servicio

1.1. Impulsión de aire exterior filtrado (MERV 13-14) al laboratorio de análisis industrial para ventilación general a 12 renovaciones/h (3 840 m³/h sobre 320 m³), con exclusión de polvo, insectos y objetos extraños del aire de impulsión. Descarga directa al recinto a través del muro, sin red de ductos de distribución; el aire sale del recinto por rejillas de descarga libre a la atmósfera. El sistema no mantiene consigna de presión interior. Operación continua.

1.2. Ambiente de instalación: exterior o semi-cubierto dentro de planta de hipoclorito de calcio; atmósfera con Cl₂/ClO⁻, polvo de Ca(ClO)₂ y humedad relativa media 84 %. Servicio clasificado como altamente corrosivo.

## 2. Condiciones de sitio

**Tabla 1.** Condiciones ambientales de diseño (fuentes en informe_investigacion.md §3.1; consulta 2026-07-23).

| Parámetro | Valor |
|---|---|
| Altitud | 2 558 msnm |
| Presión atmosférica | 74.1 kPa |
| Temperatura de diseño verano / invierno / media | 21 °C / 3 °C / 14 °C |
| Humedad relativa media anual | 84 % |
| Densidad del aire de diseño | 0.88 kg/m³ a 20 °C (0.87 kg/m³ en condición 0.4 %) |
| Factor de densidad k (vs. catálogo 1.2 kg/m³) | 0.733 |

## 3. Punto de trabajo

**Tabla 2.** Punto de trabajo en el sitio y punto equivalente de selección en catálogo.

| Magnitud | En el sitio (ρ = 0.88 kg/m³) | Equivalente catálogo (ρ = 1.2 kg/m³) |
|---|---|---|
| Caudal | 3 840 m³/h = 64 m³/min = 1.0667 m³/s = 2 260 CFM | Sin cambio (máquina de volumen constante) |
| ΔP total, escenario de diseño (filtro cargado) | 165 Pa | 225 Pa |
| ΔP total, escenario filtro limpio | 70 Pa | 95 Pa |
| Composición ΔP diseño | Filtro 154 Pa + rejillas 11 Pa | Filtro 210 Pa + 15 Pa |
| Potencia teórica de aire (η = 0.55) | 0.320 kW = 0.43 HP | — |

3.1. La selección se efectúa sobre catálogo a densidad estándar en el punto 3 840 m³/h @ 225 Pa, aplicando las leyes de los ventiladores (P ∝ ρ, potencia ∝ ρ, Q constante) según [Twin City Fan FE-1600](http://eu.tcf.com/wp-content/uploads/sites/4/2018/06/Temperature-Altitude-Effects-on-Fans-FE-1600-1.pdf) (consulta 2026-07-23). Tamaño y RPM exactos: por confirmar con proveedor mediante su software de selección.

3.2. El ventilador seleccionado entregará en el sitio el mismo caudal a las mismas RPM, con presión y potencia reducidas en el factor 0.733; la eficiencia mínima exigible es 0.55 (dato provisional, a verificar contra la curva de la selección final). El margen sobre la potencia de eje (motor provisional 0.75 HP vs. 0.43 HP teóricos, con margen de servicio 1.5) absorbe el derateo por altitud de NEMA MG-1 (≈9 % a 2 558 msnm) y el factor de servicio; la potencia final del motor se confirma con la curva de catálogo de la selección.

## 4. Tipo y materiales de construcción

**Tabla 3.** Requisitos de construcción.

| Componente | Especificación |
|---|---|
| Tipo | Axial tubeaxial, transmisión por bandas (motor fuera de la corriente de aire, ajuste de RPM por poleas); montaje directo en muro/pasamuros |
| Carcasa y rodete | PRFV con resina viniléster, laminado según ASTM C582/D4167; velo superficial para oxidantes fuertes donde el fabricante lo ofrezca |
| Elementos metálicos en la corriente | Ninguno (transmisión por bandas con motor fuera de la corriente de aire) |
| Eje, buje y componentes de transmisión | Encapsulados/protegidos contra la atmósfera clorada; bandas en compartimento ventilado y sellado |
| Construcción contra chispa | AMCA 99 Spark A (dato típico de especificación para PRFV) |
| Certificación de desempeño | AMCA 210/211 (sello AMCA exigible) |
| Descartado | Acero inoxidable en la corriente (picadura por cloruros); acero galvanizado; acero con epóxico solo como segunda línea con inspección programada (alternativa Greenheck VAB) |

Justificación de materiales: las resinas viniléster tipo Derakane se especifican expresamente para cloro e hipoclorito ([INEOS — Derakane Resin Selection Guide](http://www.ineos.com/globalassets/ineos-group/businesses/ineos-composites/markets/corrosion/derakane-resin-selection-guide.pdf), consulta 2026-07-23); el polipropileno ofrece alta resistencia a cloruros e hipoclorito a temperatura ambiente ([Plastec](https://www.plastecventilation.com/collections/plastec-series), consulta 2026-07-23).

## 5. Motor

**Tabla 4.** Especificación del motor.

| Parámetro | Valor |
|---|---|
| Potencia instalada | 0.75 HP (provisional; confirmar con la curva de la selección final) |
| Ejecución | TEFC, severe duty, pintura epóxica, protección interna anticorrosiva, sellos de eje en ambos extremos (referencia IEEE 841 o equivalente) |
| Velocidad | 1 800 RPM (4 polos, 60 Hz) — dato típico |
| Aislamiento / protección | Clase F / IP55 mínimo (IP56 preferible) |
| Tensión / fases / frecuencia | 440 V, 3φ, 60 Hz (confirmado por el cliente, 2026-07-23) |
| Derateo por altitud | ≈9 % (NEMA MG-1); absorbido por el margen de selección (§3.2) |
| Accesorios | Calentador anticondensación si hay paradas largas (dato típico de buena práctica); caja de conexiones sellada, prensaestopas niquelados |

Referencias de especificación: [Leeson/Regal Severe Duty (PDF)](https://www.regalrexnord.com/-/media/documents/brands/literature/industries/leeson_product_catalog_1050.pdf); [Baldor-Reliance IEEE 841XL](https://www.baldor.com/mvc/DownloadCenter/Files/9AKK108319) (consulta 2026-07-23).

## 6. Accesorios

6.1. Conexión flexible de descarga en hipalón (CSM) con bandas inox 316 ([Hardcast Hypalon (PDF)](https://6c2bd45d09da3c66a408-2b16a407535c695c8a76f8b06a56f342.ssl.cf2.rackcdn.com/GWB%20%20eCatalog%2006-25-16.pdf), consulta 2026-07-23). 6.2. Persiana de gravedad de cierre automático en inox o PRFV (opcional), para sellar la abertura cuando el equipo está detenido. 6.3. Guarda de seguridad en el lado de aspiración/descarga accesible, según configuración final de montaje. 6.4. Bancada y soportes con ferretería inox 316 (A4) y aislamiento dieléctrico frente a estructura galvanizada. 6.5. Toma de aire ubicada a sotavento y alejada de las fuentes de cloro de la planta (recomendación de la investigación). 6.6. Guardamotor y tablero conforme a RETIE (ver listado_equipos.md, ítems 11-12).

## 7. Candidatos comerciales

**Tabla 5.** Candidatos (consulta 2026-07-23, ampliada 2026-07-27); modelo de referencia, tamaño/RPM final por confirmar con proveedor.

| Fabricante / línea | Material | Canal en Colombia | Fuente |
|---|---|---|---|
| Aerovent FBD (Twin City Fan / Aerovent) — primera opción | PRFV, tubeaxial de bandas (Catálogo 185: 355-1 525 mm, hasta 370 Pa estática) | Por confirmar representante/canal local | [Catálogo 185 (PDF)](https://www.aerovent.com/wp-content/uploads/sites/2/2024/07/Fiberglass-Fans-Axial-Flow-Model-FBD-FDP-FRV-TFBD-VTFBD-Catalog-185.pdf) |
| Greenheck VAB (vaneaxial de bandas) | Acero con recubrimiento epóxico | Prime Lines HVAC, Bogotá (representante oficial) | [Catálogo VAB/VAD (PDF)](https://content.greenheck.com/public/DAMProd/Original/10003/vane_axial_catalog.pdf); [rep.](https://www.greenheck.com/find-my-rep/2973_southamerica_colombia) |
| Sodeca HCT/HGT versión anticorrosiva | PRFV | Sodeca Colombia (filial, catálogo 60 Hz) | [Sodeca](https://www.sodeca.com); [catálogo Colombia (PDF)](https://www.sodeca.co/files/catalogs/es/SODECA_CT18_catalogo_resumen_CO.pdf) |
| New York Blower FRP tubeaxial | PRFV | Importación (plazo máx. ~3 meses, dato cliente 2026-07-23) | [NYB](https://www.nyb.com/) |
| Plastec | Polipropileno | Importación directa (despacho 48 h declarado) | [Plastec](https://www.plastecventilation.com/collections/plastec-series) |

## 8. Montaje

8.1. El ventilador se instalará en **muro/pasamuros**, con el eje horizontal y a una cota aproximada de **3,0 m sobre el piso terminado** del laboratorio. El sentido de flujo es: aspiración de aire exterior filtrado, descarga directa al interior del recinto.

8.2. La transmisión por bandas ubica el **motor fuera de la corriente de aire corrosivo**. La altura de 3,0 m exige garantizar el acceso para mantenimiento periódico de bandas, lubricación e inspección del motor (plataforma fija o escalera industrial).

8.3. La carcasa tubular se apoyará en una bancada/soporte anclado a la estructura del muro con ferretería inox 316 (A4) y aislamiento dieléctrico frente a estructuras galvanizadas. El pasamuros se sellará con silicona RTV neutra.

8.4. La toma de aire exterior debe ubicarse a sotavento y alejada de las fuentes de cloro de la planta, conforme a la recomendación de la investigación del sistema.

## 9. Normas aplicables

9.1. AMCA 210/211 (desempeño y certificación), AMCA 99 (Spark A), ASTM C582 y ASTM D4167 (laminados PRFV), NEMA MG-1 / IEC 60034-1 (motores y derateo por altitud), IEEE 841 (ejecución severe duty de referencia), RETIE y NTC 2050 (instalación eléctrica), ISO 12944 / prácticas NACE-AMPP (protección anticorrosiva del entorno de instalación).

# Hoja de datos: ventilador de impulsión

| Campo | Valor |
|---|---|
| Código | HD-VENT-001 |
| Revisión | 0 |
| Fecha | 2026-07-23 |
| Proyecto | P2437-HV-INF-001 — BRINSA, laboratorio de análisis industrial, Cajicá |
| Etiqueta de equipo | VENT-001 (ventilador de impulsión / presurización) |

---

## 1. Servicio

1.1. Impulsión de aire exterior filtrado (MERV 13-14) al laboratorio de análisis industrial para mantener presurización positiva de +25 Pa (mínimo +12.5 Pa) y excluir insectos, objetos extraños y polvo. Descarga directa al recinto, sin red de ductos de distribución. Operación continua.

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
| ΔP total, escenario de diseño (filtro cargado) | 190 Pa | 260 Pa |
| ΔP total, escenario filtro limpio | 95 Pa | 130 Pa |
| Composición ΔP diseño | Filtro 154 Pa + presurización 25 Pa + rejillas 11 Pa | Filtro 210 Pa + 34 Pa + 15 Pa |
| Velocidad de inyección | 8 m/s (presión dinámica 28 Pa en el sitio) | — |
| Potencia teórica al freno (η = 0.60) | 0.338 kW = 0.45 HP | — |

3.1. La selección se efectúa sobre catálogo a densidad estándar en el punto 3 840 m³/h @ 260 Pa, aplicando las leyes de los ventiladores (P ∝ ρ, potencia ∝ ρ, Q constante) según [Twin City Fan FE-1600](http://eu.tcf.com/wp-content/uploads/sites/4/2018/06/Temperature-Altitude-Effects-on-Fans-FE-1600-1.pdf) (consulta 2026-07-23). Tamaño y RPM exactos: por confirmar con proveedor mediante su software de selección.

3.2. El ventilador seleccionado entregará en el sitio el mismo caudal a las mismas RPM, con presión y potencia reducidas en el factor 0.733; el margen sobre la potencia de eje (motor 1.0 HP vs. 0.45 HP teóricos) absorbe el derateo por altitud de NEMA MG-1 (≈9 % a 2 558 msnm) y el factor de servicio.

## 4. Tipo y materiales de construcción

**Tabla 3.** Requisitos de construcción.

| Componente | Especificación |
|---|---|
| Tipo | Centrífugo, álabes curvados hacia atrás, simple aspiración, transmisión directa o por bandas (dato típico según línea seleccionada) |
| Carcasa y rueda | PRFV con resina viniléster, laminado según ASTM C582/D4167 (primera opción) o polipropileno (alternativa); velo superficial para oxidantes fuertes donde el fabricante lo ofrezca |
| Elementos metálicos en la corriente | Ninguno (motor fuera de la corriente de aire) |
| Eje y buje | Encapsulados/protegidos contra la atmósfera clorada |
| Construcción contra chispa | AMCA 99 Spark A (dato típico de especificación para PRFV) |
| Certificación de desempeño | AMCA 210/211 (sello AMCA exigible) |
| Descartado | Axial PRFV (presión insuficiente con MERV 13-14); acero inoxidable en la corriente (picadura por cloruros); acero galvanizado |

Justificación de materiales: las resinas viniléster tipo Derakane se especifican expresamente para cloro e hipoclorito ([INEOS — Derakane Resin Selection Guide](http://www.ineos.com/globalassets/ineos-group/businesses/ineos-composites/markets/corrosion/derakane-resin-selection-guide.pdf), consulta 2026-07-23); el polipropileno ofrece alta resistencia a cloruros e hipoclorito a temperatura ambiente ([Plastec](https://www.plastecventilation.com/collections/plastec-series), consulta 2026-07-23).

## 5. Motor

**Tabla 4.** Especificación del motor.

| Parámetro | Valor |
|---|---|
| Potencia instalada | 1.0 HP |
| Ejecución | TEFC, severe duty, pintura epóxica, protección interna anticorrosiva, sellos de eje en ambos extremos (referencia IEEE 841 o equivalente) |
| Velocidad | 1 800 RPM (4 polos, 60 Hz) — dato típico |
| Aislamiento / protección | Clase F / IP55 mínimo (IP56 preferible) |
| Tensión / fases / frecuencia | 440 V, 3φ, 60 Hz (confirmado por el cliente, 2026-07-23) |
| Derateo por altitud | ≈9 % (NEMA MG-1); absorbido por el margen de selección (§3.2) |
| Accesorios | Calentador anticondensación si hay paradas largas (dato típico de buena práctica); caja de conexiones sellada, prensaestopas niquelados |

Referencias de especificación: [Leeson/Regal Severe Duty (PDF)](https://www.regalrexnord.com/-/media/documents/brands/literature/industries/leeson_product_catalog_1050.pdf); [Baldor-Reliance IEEE 841XL](https://www.baldor.com/mvc/DownloadCenter/Files/9AKK108319) (consulta 2026-07-23).

## 6. Accesorios

6.1. Conexión flexible de descarga en hipalón (CSM) con bandas inox 316 ([Hardcast Hypalon (PDF)](https://6c2bd45d09da3c66a408-2b16a407535c695c8a76f8b06a56f342.ssl.cf2.rackcdn.com/GWB%20%20eCatalog%2006-25-16.pdf), consulta 2026-07-23). 6.2. Bancada y soportes con ferretería inox 316 (A4) y aislamiento dieléctrico frente a estructura galvanizada. 6.3. Toma de aire ubicada a sotavento y alejada de las fuentes de cloro de la planta (recomendación de la investigación). 6.4. Guardamotor y tablero conforme a RETIE (ver listado_equipos.md, ítems 16-17).

## 7. Candidatos comerciales

**Tabla 5.** Candidatos (consulta 2026-07-23); tamaño/RPM final por confirmar con proveedor.

| Fabricante / línea | Material | Canal en Colombia | Fuente |
|---|---|---|---|
| Greenheck BCSW-FRP (primera opción) | PRFV poliéster ignífugo, opción velo Nexus | Prime Lines HVAC, Bogotá (representante oficial) | [Catálogo](https://content.greenheck.com/public/DAMProd/Original/10002/BCSWFRP_catalog.pdf); [rep.](https://www.greenheck.com/find-my-rep/2973_southamerica_colombia) |
| New York Blower FRP Fume Exhauster | Rueda viniléster PRFV | Importación (plazo máx. ~3 meses, dato cliente 2026-07-23) | [NYB](https://www.nyb.com/frp-fume-exhauster/) |
| Sodeca CPV | Polipropileno | Sodeca Colombia (filial, catálogo 60 Hz) | [CPV](https://www.sodeca.com/es/sistemas-de-ventilacion-extraccion/cpv-p1000000071) |
| Plastec 25/30 | Polipropileno, sin metal en corriente | Importación directa (despacho 48 h declarado) | [Plastec](https://www.plastecventilation.com/collections/plastec-series) |
| Soler & Palau línea PP | Polipropileno | S&P Colombia (filial); modelo por confirmar | [Catálogo Industrial (PDF)](https://www.solerpalau.mx/ASW/recursos/cata/Industrial.pdf) |

## 8. Normas aplicables

8.1. AMCA 210/211 (desempeño y certificación), AMCA 99 (Spark A), ASTM C582 y ASTM D4167 (laminados PRFV), NEMA MG-1 / IEC 60034-1 (motores y derateo por altitud), IEEE 841 (ejecución severe duty de referencia), RETIE y NTC 2050 (instalación eléctrica), ISO 12944 / prácticas NACE-AMPP (protección anticorrosiva del entorno de instalación).

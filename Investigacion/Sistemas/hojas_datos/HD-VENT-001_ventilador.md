# Hoja de datos: ventilador axial mural de inyección

| Campo | Valor |
|---|---|
| Código | HD-VENT-001 |
| Revisión | 2 |
| Fecha | 2026-07-27 |
| Proyecto | P2437-HV-INF-001 — BRINSA, laboratorio de análisis industrial, Cajicá |
| Etiqueta de equipo | VENT-001 (ventilador axial mural de inyección) |

**Nota de revisión REV2 — 2026-07-27:** actualización por uniformidad con el montaje típico instalado en la planta (`Montaje/DISENOFINAL.png` y `Montaje/Descripcion_Tecnica_Sistema_Ventilacion_Inyeccion_2260CFM_v2.md`): ventilador axial mural (placa mural) Ø560 mm, transmisión directa, con cubierta intemperie que aloja el banco de filtración, estructura de unión pernada al muro y malla de protección interior. Se conservan caudal, ΔP de diseño, filtración MERV 8 + MERV 13-14, rejillas y ausencia de presurización.

**Nota de revisión REV1 — 2026-07-27:** cambio de alcance del cliente — sistema sin presurización, ventilador axial en lugar de centrífugo, sin instrumentación de presión diferencial.

---

## 1. Servicio

1.1. Impulsión de aire exterior filtrado (MERV 8 + MERV 13-14) al laboratorio de análisis industrial para ventilación general a 12 renovaciones/h (3 840 m³/h sobre 320 m³), con exclusión de polvo, insectos y objetos extraños del aire de impulsión. Descarga directa al recinto a través del muro, sin red de ductos de distribución; el aire sale del recinto por rejillas de descarga libre a la atmósfera. El sistema no mantiene consigna de presión interior. Operación continua.

1.2. Ambiente de instalación: exterior o semi-cubierto dentro de planta de hipoclorito de calcio; atmósfera con Cl₂/ClO⁻, polvo de Ca(ClO)₂ y humedad relativa media 84 %. Servicio clasificado como altamente corrosivo.

1.3. Configuración de montaje uniforme con la planta (secuencia de flujo): exterior → cubierta intemperie (aloja prefiltro MERV 8 y filtro final MERV 13-14) → ventilador axial mural → paso por muro con estructura de unión → malla de protección interior → descarga al recinto.

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
| Diámetro del impulsor (uniformidad planta) | 560 mm (22 in) | — |
| Velocidad en boca (Ø560 mm) | 4.33 m/s | — |
| Potencia teórica de aire (η = 0.55) | 0.320 kW = 0.43 HP | — |

3.1. La selección se efectúa sobre catálogo a densidad estándar en el punto 3 840 m³/h @ 225 Pa, aplicando las leyes de los ventiladores (P ∝ ρ, potencia ∝ ρ, Q constante) según [Twin City Fan FE-1600](http://eu.tcf.com/wp-content/uploads/sites/4/2018/06/Temperature-Altitude-Effects-on-Fans-FE-1600-1.pdf) (consulta 2026-07-23). El tamaño comercial queda fijado en Ø560 mm por uniformidad con el montaje típico instalado en la planta; las RPM exactas se confirman con el software de selección del fabricante.

3.2. El ventilador seleccionado entregará en el sitio el mismo caudal a las mismas RPM, con presión y potencia reducidas en el factor 0.733; la eficiencia mínima exigible es 0.55 (dato provisional, a verificar contra la curva de la selección final). El margen sobre la potencia de eje (motor provisional 0.75 HP vs. 0.43 HP teóricos, con margen de servicio 1.5) absorbe el derateo por altitud de NEMA MG-1 (≈9 % a 2 558 msnm) y el factor de servicio; la potencia final del motor se confirma con la curva de catálogo de la selección.

## 4. Tipo y materiales de construcción

**Tabla 3.** Requisitos de construcción.

| Componente | Especificación |
|---|---|
| Tipo | Axial mural (placa mural / wall fan), Ø560 mm, transmisión directa (motor en el cubo del impulsor); montaje en muro mediante estructura de unión |
| Carcasa, placa mural y rodete | PRFV con resina viniléster, laminado según ASTM C582/D4167; alternativa: acero con recubrimiento epóxico anticorrosivo (segunda línea, con inspección programada) |
| Elementos metálicos en la corriente | Mínimos; eje del motor en acero inoxidable con protección anticorrosiva |
| Motor en la corriente de aire | Encapsulado severe duty (ver Tabla 4) — la transmisión directa ubica el motor dentro de la corriente; se exige ejecución anticorrosiva reforzada, criterio ya operado por la planta en sus montajes típicos |
| Construcción contra chispa | AMCA 99 Spark A (dato típico de especificación para PRFV) |
| Certificación de desempeño | AMCA 210/211 (sello AMCA exigible) |
| Descartado | Acero inoxidable en la corriente (picadura por cloruros); acero galvanizado desnudo en la corriente de aire |

Justificación de materiales: las resinas viniléster tipo Derakane se especifican expresamente para cloro e hipoclorito ([INEOS — Derakane Resin Selection Guide](http://www.ineos.com/globalassets/ineos-group/businesses/ineos-composites/markets/corrosion/derakane-resin-selection-guide.pdf), consulta 2026-07-23); el polipropileno ofrece alta resistencia a cloruros e hipoclorito a temperatura ambiente ([Plastec](https://www.plastecventilation.com/collections/plastec-series), consulta 2026-07-23). El montaje típico de la planta usa acero galvanizado y pintura electrostática; para este servicio se eleva la especificación a PRFV o epóxico anticorrosivo por la atmósfera clorada.

**Nota de ingeniería (REV2).** La adopción del montaje mural de transmisión directa deja el motor dentro de la corriente de aire corrosivo, a diferencia de la configuración de transmisión por bandas evaluada en REV1. El riesgo se mitiga con la ejecución encapsulada severe duty de la Tabla 4 y con el programa de inspección semestral de la Tabla de mantenimiento de la descripción técnica de planta; la alternativa de transmisión por bandas queda documentada como opción si la vida del motor en servicio resultara inferior a la esperada.

## 5. Motor

**Tabla 4.** Especificación del motor.

| Parámetro | Valor |
|---|---|
| Potencia instalada | 0.75 HP (provisional; confirmar con la curva de la selección final) |
| Ejecución | TEFC encapsulado, severe duty, pintura epóxica, protección interna anticorrosiva, sellos de eje en ambos extremos, eje inox (referencia IEEE 841 o equivalente) |
| Ubicación | En el cubo del impulsor, dentro de la corriente de aire (transmisión directa) |
| Aislamiento / protección | Clase F (H preferible) / IP56 mínimo (IP66 preferible) |
| Tensión / fases / frecuencia | 440 V, 3φ, 60 Hz (confirmado por el cliente, 2026-07-23) |
| Derateo por altitud | ≈9 % (NEMA MG-1); absorbido por el margen de selección (§3.2) |
| Accesorios | Calentador anticondensación (paradas largas); caja de conexiones sellada, prensaestopas niquelados |

Referencias de especificación: [Leeson/Regal Severe Duty (PDF)](https://www.regalrexnord.com/-/media/documents/brands/literature/industries/leeson_product_catalog_1050.pdf); [Baldor-Reliance IEEE 841XL](https://www.baldor.com/mvc/DownloadCenter/Files/9AKK108319) (consulta 2026-07-23).

## 6. Accesorios

**Tabla 5.** Accesorios del conjunto de montaje (uniformidad con la planta).

| Ítem | Función | Material / especificación |
|---|---|---|
| Cubierta intemperie | Protección contra lluvia, radiación solar e ingreso directo de agua; aloja el banco de filtración (ver HD-FILT-001) | PRFV o acero galvanizado G90 con pintura electrostática epóxica; alternativa inox 316L |
| Estructura de unión | Marco de soporte pernado al muro para fijación segura del ventilador; transmite cargas estáticas, dinámicas y vibraciones | Perfiles ASTM A36 galvanizados en caliente + pintura epóxica; ferretería inox 316 (A4) con aislamiento dieléctrico |
| Malla de protección interior | Jaula de seguridad en la descarga interior; evita contacto accidental con el impulsor | Malla inox 316 o galvanizada con pintura epóxica, marco desmontable |
| Sellado del pasamuros | Evita recirculaciones y filtraciones no controladas en el vano | Silicona RTV neutra (no acetoxi) |
| Guardamotor y tablero | Protección eléctrica conforme a RETIE (ver listado_equipos.md, ítems 11-12) | Gabinete con tratamiento anticorrosivo, prensaestopas niquelados |

6.1. La toma de aire exterior debe ubicarse a sotavento y alejada de las fuentes de cloro de la planta, conforme a la recomendación de la investigación del sistema.

## 7. Candidatos comerciales

**Tabla 6.** Candidatos (consulta 2026-07-23, ajustada 2026-07-27 a tipo mural); RPM final por confirmar con proveedor en el punto 3 840 m³/h @ 225 Pa.

| Fabricante / línea | Material | Canal en Colombia | Fuente |
|---|---|---|---|
| Sodeca HQD/HGT mural anticorrosivo — primera opción por uniformidad y canal local | PRFV / epóxico, mural transmisión directa | Sodeca Colombia (filial, catálogo 60 Hz) | [Sodeca](https://www.sodeca.com); [catálogo Colombia (PDF)](https://www.sodeca.co/files/catalogs/es/SODECA_CT18_catalogo_resumen_CO.pdf) |
| Greenheck mural (línea industrial) | Acero con recubrimiento epóxico | Prime Lines HVAC, Bogotá (representante oficial) | [Greenheck](https://www.greenheck.com); [rep.](https://www.greenheck.com/find-my-rep/2973_southamerica_colombia) |
| Aerovent / Twin City Fan (línea mural FRP) | PRFV | Por confirmar representante/canal local | [Aerovent](https://www.aerovent.com) |
| New York Blower FRP mural | PRFV | Importación (plazo máx. ~3 meses, dato cliente 2026-07-23) | [NYB](https://www.nyb.com/) |
| Plastec | Polipropileno | Importación directa (despacho 48 h declarado) | [Plastec](https://www.plastecventilation.com/collections/plastec-series) |

## 8. Montaje

8.1. El ventilador se instalará en **muro/pasamuros**, con el eje horizontal y a una cota aproximada de **3,0 m sobre el piso terminado** del laboratorio. El sentido de flujo es: aspiración del aire exterior a través de la cubierta intemperie y su banco de filtración, descarga directa al interior del recinto.

8.2. El conjunto se soporta mediante una **estructura de unión** (marco de perfiles ASTM A36 galvanizados) pernada al muro con anclajes inox 316 (A4) y aislamiento dieléctrico frente a estructuras galvanizadas. El vano del muro se sella con silicona RTV neutra para evitar recirculaciones.

8.3. La **cubierta intemperie** se embrida directamente a la placa mural del ventilador por el lado exterior; aloja el banco de filtración (HD-FILT-001) y protege el conjunto contra lluvia y radiación solar. La altura de 3,0 m exige garantizar el acceso para cambio de filtros e inspección del ventilador (plataforma fija o escalera industrial).

8.4. La **malla de protección interior** (jaula) se instala en la descarga del lado interior del muro, desmontable para inspección del impulsor.

8.5. La toma de aire exterior debe ubicarse a sotavento y alejada de las fuentes de cloro de la planta, conforme a la recomendación de la investigación del sistema.

## 9. Normas aplicables

9.1. AMCA 210/211 (desempeño y certificación), AMCA 99 (Spark A), AMCA 300 (nivel sonoro), ASTM C582 y ASTM D4167 (laminados PRFV), NEMA MG-1 / IEC 60034-1 (motores y derateo por altitud), IEEE 841 (ejecución severe duty de referencia), RETIE y NTC 2050 (instalación eléctrica), ISO 12944 / prácticas NACE-AMPP (protección anticorrosiva del entorno de instalación), SMACNA HVAC Duct Construction Standards (referencia de construcción del montaje).

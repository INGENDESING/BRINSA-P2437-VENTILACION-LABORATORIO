# Hoja de datos: etapa de filtración (prefiltro MERV 8 + filtro final MERV 13-14)

| Campo | Valor |
|---|---|
| Código | HD-FILT-001 |
| Revisión | 0 |
| Fecha | 2026-07-27 |
| Proyecto | P2437-HV-INF-001 — BRINSA, laboratorio de análisis industrial, Cajicá |
| Etiqueta de equipo | FILT-001 (banco de filtración de la impulsión, alojado en la cubierta intemperie) |

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

## 7. Integración en la cubierta intemperie del ventilador mural DTS-001

7.1. El ventilador seleccionado es un axial mural (placa mural) Ø560 mm de transmisión directa (HD-VENT-001, DTS-001) con punto de trabajo 3 840 m³/h a 165 Pa en el sitio (equivalente 225 Pa en catálogo a ρ = 1,2 kg/m³). Por uniformidad con el montaje típico de la planta, el banco de filtración FILT-001 se aloja **dentro de la cubierta intemperie** del ventilador, sin caja/housing separado ni transición cuadrado/circular. La secuencia de flujo es: toma exterior (boca de la cubierta) → malla anti-insectos → prefiltro MERV 8 → filtro final MERV 13-14 → ventilador axial mural → paso por muro → malla de protección interior → descarga al recinto (HD-VENT-001 §8.1).

**Tabla 6.** Verificación hidráulica del filtro final en el punto de trabajo del ventilador.

| Parámetro | Valor | Fuente / cálculo |
|---|---|---|
| Caudal de diseño | 3 840 m³/h ≡ 2 260 CFM | Memoria de cálculo, HD-VENT-001 §3 |
| Área facial del filtro 24×24 in | 0,372 m² ≡ 4,00 ft² | 610 mm × 610 mm |
| Velocidad facial en el filtro | 2,87 m/s ≡ 565 fpm | Q / A |
| Velocidad máxima usable (Durafil ES3) | 625 fpm | [Product Sheet Durafil ES3 (PDF)](https://www.camfil.com/dam/files/290/1590002/Product-Sheet-Durafil-ES3-ENG-US.pdf) |
| ΔP inicial catálogo MERV 14 @ 500 fpm | 0,31 in c.a. ≡ 77 Pa | [Drawing Durafil ES3 (PDF)](https://www.camfil.com/dam/files/1165/1676816/Drawing-Durafil-ES3.pdf) |
| ΔP inicial estimado @ 565 fpm (catálogo) | 98 Pa | Escalado cuadrático: 77 Pa × (565/500)² |
| ΔP inicial estimado en el sitio (ρ = 0,88 kg/m³) | 72 Pa | 98 Pa × 0,733 |
| ΔP final de diseño (catálogo) | 210 Pa | Valor congelado de la memoria de cálculo |
| ΔP final estimado en el sitio | 154 Pa | 210 Pa × 0,733 |
| ΔP disponible para filtro + rejillas en el ventilador | 165 Pa sitio | HD-VENT-001 §3 |

7.2. El filtro final opera dentro del rango hidráulico permitido: la velocidad facial (565 fpm) es inferior al límite de 625 fpm del Durafil ES3, y la caída de presión final de diseño (154 Pa en el sitio) deja un margen de 11 Pa para las rejillas de descarga, coincidente con el punto de trabajo declarado del ventilador. El caudal de 2 260 CFM supera el caudal nominal (rated airflow) de 2 000 CFM del Durafil ES3 24×24×12, pero se encuentra dentro del máximo operativo dado por 625 fpm (≈2 500 CFM); por tanto, la selección requiere confirmación del fabricante de que no se excede el límite de uso continuo. El Durafil ES2 (referencia original) tiene caudal nominal 3 000 CFM, por lo que también es técnicamente válido y puede ofrecerse como alternativa equivalente.

7.3. La cubierta intemperie reemplaza funcionalmente a la caja de filtración: protege contra lluvia, radiación solar e ingreso directo de agua, y aloja en su interior el portafiltros con la malla anti-insectos, el prefiltro y el filtro final. Se especifica con acceso frontal o superior para el cambio de filtros desde la plataforma, boca de entrada con área libre suficiente para no añadir pérdida significativa (la pérdida de la boca se consigna como margen menor dentro de los 165 Pa; confirmar en submittal), y embridado directo a la placa mural del ventilador. Material: PRFV con resina viniléster o acero galvanizado G90 con pintura electrostática epóxica; alternativa inox 316L, siguiendo el mismo criterio anticorrosivo del ventilador.

**Tabla 7.** Accesorios y periféricos del banco de filtración en la cubierta.

| Ítem | Función | Material / especificación | Nota de compatibilidad |
|---|---|---|---|
| Portafiltros (holding frame) | Sujeción y sellado del prefiltro y filtro final dentro de la cubierta | Inox 316L, junta de poliuretano continua | Debe aceptar módulo 24×24 in y admitir carga del filtro (≈5 kg) |
| Malla anti-insectos | Protección contra insectos y objetos gruesos en la boca de la cubierta | Inox 316, tejido 18×18, marco desmontable | Aguas arriba del prefiltro (listado_equipos.md ítem 7) |
| Cubierta intemperie | Aloja el banco de filtración; protección de intemperie; embridado a placa mural | PRFV viniléster o galvanizado G90 + pintura epóxica; alternativa inox 316L | Acceso frontal/superior para cambio de filtros; drenaje inferior |
| Clips de prefiltro | Fijar el prefiltro MERV 8 a la cara del filtro final | Plástico o inox 316 (Camfil C-84-2 / C-84-4 para ES3) | El Durafil ES3 incluye ranuras para clips; confirmar si se suministran con el filtro |
| Fijación de la cubierta | Anclaje de la cubierta a la placa mural y/o estructura de unión | Pernos inox 316 (A4) con aislamiento dieléctrico | La estructura de unión del ventilador (HD-VENT-001 §8.2) soporta el conjunto |

7.4. Puntos de verificación en campo. La boca de la cubierta debe tener área libre igual o mayor al área facial del filtro (0,372 m²) para no incrementar la pérdida de entrada; la profundidad interior de la cubierta debe acomodar la profundidad del conjunto (malla 30 mm + prefiltro 50 mm + filtro final 300 mm + holguras). La altura de montaje de 3,0 m sobre el piso exige plataforma o escalera industrial para el cambio de filtros; el peso del conjunto filtro+prefiltro (≈7 kg) es manejable manualmente. El sentido de flujo puede ser en cualquier dirección en el Durafil ES2/ES3; se recomienda orientar la flecha del filtro hacia el ventilador para aprovechar la succión y mantener el elemento asentado contra el portafiltros. Programa de mantenimiento: prefiltro 3-6 meses y filtro final 6-12 meses según ΔP o condición (criterio de la descripción técnica de planta).

## 8. Foto comercial de referencia

8.1. La Figura 1 presenta la imagen comercial del filtro V-bank Camfil Durafil ES (familia que incluye ES2 y ES3). La configuración mostrada corresponde a un filtro de banco tipo V con marco plástico ABS, juntas planas y ranuras para clips de prefiltro, equivalente en forma y dimensiones al especificado.

**Figura 1.** Filtro V-bank Camfil Durafil ES de referencia (24×24×12 in, MERV 13-14). Fuente: Camfil.

![Filtro Camfil Durafil ES V-bank](https://www.camfil.com/dam/images/878/144420/Durafil-ES-V-bank-air-filter.png?width=470&height=470&bgcolor=white)

8.2. Enlace directo a la ficha del distribuidor con especificaciones del SKU 855080-009 (Durafil ES2 24×24×12 in, MERV-14/14A): [Capris — CAMFIL 855080009 Filtro tipo V (4V) con cejilla MERV-14/14A 24"×24"×12" Durafil ES2](https://www.capris.cr/es/camfil-855080009-filtro-tipo-v-4v-con-cejilla-merv-14-14a-24u0022x24u0022x12u0022-durafil-es2-k50086.html).

## 9. Normas aplicables

9.1. ANSI/ASHRAE 52.2-2017 (ensayo y clasificación MERV); ISO 16890 (ePM1, exigible como informe alternativo); EN 779:2012 (referencia heredada F7/F8). El estado de carga del filtro se sigue por programa de mantenimiento basado en la ΔP esperada (59 Pa limpio / 154 Pa cargado en el sitio) y en la carga de polvo observada en operación (dato típico de operación).

# Hoja de datos: instrumentos de presión diferencial y control de presurización

| Campo | Valor |
|---|---|
| Código | HD-INST-001 |
| Revisión | 0 |
| Fecha | 2026-07-23 |
| Proyecto | P2437-HV-INF-001 — BRINSA, laboratorio de análisis industrial, Cajicá |
| Etiquetas | PDT-001 (transmisor), PDI-001 (indicador local), PDSV-001 (damper de alivio barométrico) |

---

## 1. Servicio

1.1. Medición, indicación, alarma y control pasivo de la presurización positiva del laboratorio: set-point +25 Pa, mínimo admisible +12.5 Pa, respecto a la referencia exterior. La referencia exterior queda expuesta a atmósfera clorada y viento; las tomas de impulso requieren protección (§5).

## 2. Arquitectura del lazo

2.1. Secuencia: el transmisor PDT-001 mide el diferencial interior–exterior y entrega 4-20 mA al PLC/BMS del cliente (o a relés autónomos); el indicador local PDI-001 permite verificación visual continua; el elemento final de control es el damper barométrico PDSV-001, cuyo contrapeso se calibra para abrir cuando el diferencial supera +25 Pa, descargando el exceso de caudal y estabilizando la presión de sala. Con filtro limpio (ΔP total 95 Pa en el sitio) el damper trabaja más abierto; con filtro cargado (190 Pa en el sitio) cierra y mantiene la consigna — compensación pasiva que hace al damper obligatorio (informe_investigacion.md §5.2).

2.2. El esquema corresponde al lazo documentado para presurización de edificios: sensor diferencial interior–exterior supervisando el elemento de alivio ([Trane ADM-APN003](https://www.trane.com/content/dam/Trane/Commercial/global/products-systems/education-training/engineers-newsletters/airside-design/admapn003en_0502.pdf), consulta 2026-07-23). Dado que el contrapeso actúa sobre diferencial de presión y no sobre caudal, el ajuste a +25 Pa es válido a la altitud del sitio; la posición de equilibrio cambia con la densidad, por lo que la calibración final se realiza en comisionamiento con micromanómetro (práctica documentada por [Halton BRD](https://www.halton.com/app/uploads/2020/08/Halton-BRD-datasheet-2024.pdf), consulta 2026-07-23).

**Tabla 1.** Puntos de consigna y alarmas.

| Parámetro | Valor | Acción |
|---|---|---|
| Set-point de presurización | +25 Pa | Ajuste del contrapeso del damper PDSV-001 |
| Alarma baja | +12.5 Pa | Pérdida de presurización: riesgo de ingreso de insectos, polvo y cloro |
| Alarma alta | +40 Pa | Damper atascado o falla de exfiltración (dato típico) |
| Retardo de alarmas | 30-60 s | Evita falsas alarmas por apertura de puerta (dato típico) |
| Límite superior absoluto | ≈60 Pa | Fuerza de apertura de puertas (referencia IBC 1009.3; dato típico) |

2.3. El lazo activo (variador de frecuencia o damper motorizado) solo se justifica con aperturas frecuentes de puerta o exigencia de registro BMS ([AIVC airbase_7469 (PDF)](https://www.aivc.org/sites/default/files/airbase_7469.pdf), consulta 2026-07-23); para el set-point fijo de este proyecto se adopta la solución pasiva de máxima confiabilidad.

## 3. Transmisor de presión diferencial (PDT-001)

**Tabla 2.** Especificación y candidatos (consulta 2026-07-23).

| Parámetro | Especificación / candidatos |
|---|---|
| Rango | 0-62.5 Pa (0-0.25 in c.a.); set-point al 40 % de escala |
| Salida | 4-20 mA, 2 hilos |
| Precisión | ±1 % FS o mejor |
| Protección | NEMA 4X (IP66); montaje en interior, toma exterior protegida |
| Constante de tiempo | Ajustable 0.5-15 s (amortigua ráfagas de viento en la referencia) |
| Primera opción | Dwyer MS-121(-LCD) Magnesense: rangos seleccionables 25/62.5/125 Pa, ±1 % FS, NEMA 4X ([catálogo (PDF)](https://www.transcat.com/media/pdf/MS_cat.pdf)) |
| Alternativa premium | Setra 264, rango 0-0.25 in c.a., ±0.25/±0.4/±1 % FS, elemento capacitivo inox ([datasheet (PDF)](https://www.setra.com/hubfs/Product_Data_Sheets/Setra_Model_264_Data_Sheet.pdf)); suministro por importación, por confirmar stock |
| Alternativa BMS Siemens | Siemens QBM2130-1U, 0-100 Pa, 4-20 mA, IP42 (exige gabinete adicional) ([Industry Mall](https://mall.industry.siemens.com/mall/en/WW/Catalog/Products/10510770)) |

## 4. Indicador local (PDI-001)

**Tabla 3.** Especificación del manómetro diferencial (consulta 2026-07-23).

| Parámetro | Especificación |
|---|---|
| Modelo de referencia | Dwyer Magnehelic serie 2000, modelo 2000-00 |
| Rango | 0-62 Pa (0-0.25 in c.a.); división menor 0.005 in c.a. |
| Precisión | ±2 % FS |
| Construcción | Caja aluminio fundido (ensayo niebla salina 168 h); opción bisel inox (-SS); conexiones 1/8 in NPT |
| Montaje | Embutido en panel/puerta del laboratorio (interior) |
| Fuente | [Skilltech — tabla serie 2000](https://skilltech.com.br/produto/manometro-para-pressao-diferencial-magnehelic-serie-2000/) |

4.1. Si el cliente no dispone de PLC, se sustituye/complementa con Dwyer Photohelic 3000MR-00AV (indicador + 2 relés SPDT, rango 0-0.25 in c.a.; [Northeast Controls](https://nciweb.net/pressure1.htm), consulta 2026-07-23), que genera las alarmas de la Tabla 1 de forma autónoma.

## 5. Damper de alivio barométrico (PDSV-001)

**Tabla 4.** Especificación y candidatos (consulta 2026-07-23).

| Parámetro | Especificación / candidatos |
|---|---|
| Tipo | Barométrico de alivio, contrapeso ajustable, cierre por gravedad |
| Rango de ajuste start-open | 12-75 Pa (0.05-0.30 in c.a.), que cubre el set-point de +25 Pa |
| Materiales | Aluminio extruido 6063-T5 o línea severe-environment; galvanizado descartado |
| Dimensionamiento | Caudal de alivio de diseño con velocidad facial ≤ 2.5 m/s (dato típico); tamaño final por confirmar con proveedor |
| Ensayos | AMCA 500-D (caída de presión y fuga) |
| Calibración | En comisionamiento, con micromanómetro, a +25 Pa |
| Primera opción | Greenheck SEBR-10 (severe environment; rango 0.05-0.30 in c.a.) ([submittal (PDF)](https://content.greenheck.com/public/DAMProd/Original/10002/SEBR10Series_submittal.pdf)); canal Greenheck en Bogotá |
| Alternativa | Ruskin CBD6/BD6 (aluminio 6063-T5, control hasta 0.25 in c.a.) ([Ruskin BD6](https://www.ruskin.com/model/bd6)) |
| Alternativa | Nailor 1390CB-EAF (contrapeso 360°, rodamientos de bolas para diferenciales muy bajos, opción aluminio) ([submittal (PDF)](https://nailor.com/sites/default/files/documents/1390CB_B_0_0.pdf)) |

## 6. Tomas de impulso, montaje y accesorios

6.1. Toma de referencia exterior: caja estática de pared (tipo Dwyer A-417 o fabricación local inox 316, dato típico), orientada a sotavento, con purga o filtro de membrana por el ambiente clorado; tubería de impulso y conexiones 1/8 in NPT con sellante compatible.

6.2. Los instrumentos (cuerpos de aluminio fundido) se instalan en el interior de la sala o en gabinete IP66 con prensaestopas niquelados/inox; los herrajes estándar zincados se reemplazan por soportes fabricados en inox 316. Cableado de la señal 4-20 mA apantallado; protecciones y tablero conforme a RETIE/NTC 2050 (listado_equipos.md, ítems 16-17).

## 7. Disponibilidad en Colombia

7.1. Dwyer: Vía Industrial (Bogotá/Cali, [viaindustrial.com](https://www.viaindustrial.com/dwyer/marca/)), RS Importaciones y Suministros (Bogotá, [rsimportacionesysuministros.com.co](https://rsimportacionesysuministros.com.co/producto/transmisor-magnehelic-dwyer-instruments-a/)), SICO Global ([sico.global](https://sico.global/productos/transmisor-medidor-de-presion-diferencial-dwyer-magnehelic-605/)) — consulta 2026-07-23. Setra y los dampers Nailor/Ruskin se gestionan por importación o representante (por confirmar); Greenheck vía Prime Lines HVAC, Bogotá.

## 8. Normas aplicables

8.1. AMCA 500-D (damper), ASHRAE 62.1/170 (niveles de presurización de referencia), OSHA 29 CFR 1910.1450 (buena práctica de laboratorios), RETIE y NTC 2050 (instalación eléctrica e instrumentación), Resolución 0312 de 2019 (Colombia).

# Memoria Descriptiva — Sistema de Ventilación y Presurización del Laboratorio

## 1. Información general del proyecto

| Concepto | Valor |
|----------|-------|
| Ubicación del proyecto | Carpeta `C:\Users\ingen\OneDrive\Escritorio\HVAC\Calculos` |
| Volumen efectivo del laboratorio, \(V\) | 320 m³ |
| Renovaciones de aire requeridas, \(N\) | 12 ren/h (12 ACH) |
| Objetivo de operación | Ventilación por impulsión con presión positiva respecto a zonas adyacentes |
| Estrategia | Ventilador de impulsión directa + rejillas de exfiltración controladas |

La estrategia de presurización positiva consiste en inyectar aire limpio directamente al recinto mediante un ventilador de impulsión (sin ductos), de modo que el flujo neto de aire atraviese las rendijas y aberturas desde el laboratorio hacia el exterior. Las rejillas de exfiltración controladas en las paredes permiten que el aire salga de forma distribuida y mantengan la presión positiva deseada, evitando la entrada de contaminantes, polvo o microorganismos desde áreas menos controladas.

---

## 2. Marco normativo y sustentación de las 12 renovaciones/hora

### 2.1 Referencias normativas aplicables

1. **ASHRAE 170 — Ventilation of Health Care Facilities**  
   Establece caudales de ventilación y presiones diferenciales para instalaciones de salud. Para espacios de laboratorio clínico/procedimiento recomienda entre **6 y 15 renovaciones/hora (ACH)**, dependiendo del nivel de riesgo y del uso.

2. **ASHRAE Standard 62.1 — Ventilation for Acceptable Indoor Air Quality**  
   Proporciona los requisitos mínimos de ventilación exterior y calidad del aire interior para edificios, excepto edificios de baja altura residenciales. Para laboratorios, exige ventilación suficiente para diluir contaminantes generados en el proceso.

3. **OSHA 29 CFR 1910.1450 — Laboratory Standard**  
   Requiere que los empleadores mantengan niveles de exposición por debajo de los límites permisibles (PEL) mediante controles de ingeniería, incluida la ventilación general y local.

4. **NFPA 99 — Health Care Facilities Code**  
   Regula los sistemas de aire y gases en instalaciones de salud, incluyendo requisitos de fiabilidad para sistemas de ventilación críticos.

5. **WHO — Laboratory Biosafety Manual (4ª edición)**  
   Para laboratorios de bioseguridad nivel 2 (BSL-2) recomienda **6–12 ACH**; para BSL-3 se eleva a **12–15 ACH**. El valor de 12 ACH cubre con holgura el rango superior de un laboratorio BSL-2 y el umbral inferior de un BSL-3.

6. **NIH Design Requirements Manual (DRM)**  
   Para laboratorios de investigación biomédica sugiere **10–12 ACH** como punto de diseño para control de contaminación y confort térmico.

### 2.2 Sustentación de las 12 renovaciones/hora

| Norma / Guía | Recomendación ACH | Observación |
|--------------|-------------------|-------------|
| ASHRAE 170 — Laboratory / Procedure room | 15 ACH típico; 6–12 ACH para general | El valor de 12 ACH es adecuado para laboratorio de control medio |
| WHO BSL-2 | 6–12 ACH | 12 ACH = límite superior, cubre mayor riesgo |
| WHO BSL-3 | 12–15 ACH | 12 ACH = umbral inferior, aceptable como punto de partida |
| NIH DRM | 10–12 ACH | Punto de diseño recomendado |
| ASHRAE 62.1 | Según ocupación y contaminantes | Complementa con caudal por persona/m² |

**Conclusión normativa:**  
La selección de **12 renovaciones de aire por hora (12 ACH)** está sustentada por las guías internacionales de bioseguridad (WHO, NIH) y los estándares de ventilación de ASHRAE para instalaciones de salud. Este valor garantiza una dilución rápida de contaminantes internos, soporta el requerimiento de presión positiva y deja margen de seguridad respecto al mínimo de 6 ACH para laboratorios generales.

---

## 3. Cálculo del caudal de aire de impulsión

### 3.1 Fórmula

El caudal de ventilación por renovaciones de aire se calcula como:

\[
Q = \frac{V \times N}{60}
\]

Donde:
- \(Q\) = Caudal de aire, m³/min
- \(V\) = Volumen efectivo del recinto, m³
- \(N\) = Número de renovaciones de aire por hora, ren/h

### 3.2 Desarrollo

\[
Q = \frac{320 \text{ m}^3 \times 12 \text{ ren/h}}{60 \text{ min/h}} = 64.00 \text{ m}^3/\text{min}
\]

Equivalente:

\[
Q = 64.00 \times 60 = 3\,840 \text{ m}^3/\text{h}
\]

### 3.3 Conversión a CFM

\[
1 \text{ m}^3/\text{min} = 35.3147 \text{ CFM}
\]

\[
Q = 64.00 \times 35.3147 = 2\,260.1 \text{ CFM}
\]

**Caudal de diseño del ventilador:** **2 260 CFM (≈ 3 840 m³/h)**

---

## 4. Potencia estimada del ventilador

### 4.1 Fórmula

\[
P = \frac{Q \times \Delta P}{\eta \times 1\,000}
\]

Donde:
- \(P\) = Potencia del ventilador, kW
- \(Q\) = Caudal, m³/s
- \(\Delta P\) = Presión total a vencer, Pa
- \(\eta\) = Eficiencia total del ventilador (típica 0.55–0.70)

### 4.2 Datos de diseño

- \(Q = 64.00 \text{ m}^3/\text{min} = 1.0667 \text{ m}^3/\text{s}\)
- \(\Delta P\) estimada para sistema de impulsión directa con filtración media + rejillas de exfiltración: **150–300 Pa**
- Eficiencia estimada del ventilador, \(\eta = 0.60\)

### 4.3 Desarrollo — escenarios

#### Escenario conservador (\(\Delta P = 150 \text{ Pa}\))

\[
P = \frac{1.0667 \times 150}{0.60 \times 1\,000} = 0.267 \text{ kW}
\]

#### Escenario de diseño (\(\Delta P = 250 \text{ Pa}\))

\[
P = \frac{1.0667 \times 250}{0.60 \times 1\,000} = 0.444 \text{ kW}
\]

#### Escenario alto (\(\Delta P = 350 \text{ Pa}\))

\[
P = \frac{1.0667 \times 350}{0.60 \times 1\,000} = 0.622 \text{ kW}
\]

### 4.4 Selección de motor

Se recomienda seleccionar un ventilador con motor de **0.75 HP (0.56 kW)** o **1.0 HP (0.75 kW)** para dejar margen de sobredimensionamiento, pérdidas adicionales por filtración sucia y variación de eficiencia.

**Potencia de diseño propuesta:** **0.44 kW / 0.60 HP**, motor instalado **1.0 HP**.

---

## 5. Área de impulsión del ventilador (sin ductos)

### 5.1 Criterio de velocidad

Para ventiladores centrífugos o axiales de impulsión directa, una velocidad razonable en la boca de impulsión se sitúa entre **6 y 12 m/s**. Se adopta **8 m/s** como punto de diseño intermedio.

### 5.2 Fórmula

\[
A_{vent} = \frac{Q}{v_{vent}}
\]

\[
D = \sqrt{\frac{4 A_{vent}}{\pi}}
\quad \text{y} \quad
r = \frac{D}{2}
\]

Donde:
- \(A_{vent}\) = Área de boca del ventilador, m²
- \(D\) = Diámetro equivalente, m
- \(r\) = Radio equivalente, m
- \(Q = 1.0667 \text{ m}^3/\text{s}\)
- \(v_{vent}\) = Velocidad en boca del ventilador, m/s

### 5.3 Desarrollo

Con \(v_{vent} = 8 \text{ m/s}\):

\[
A_{vent} = \frac{1.0667}{8} = 0.1333 \text{ m}^2
\]

\[
D = \sqrt{\frac{4 \times 0.1333}{\pi}} = 0.412 \text{ m}
\]

\[
r = \frac{0.412}{2} = 0.206 \text{ m} = 206.0 \text{ mm}
\]

**Área de impulsión del ventilador:** **0.1333 m²**  
**Diámetro equivalente:** **412 mm**  
**Radio equivalente:** **206.0 mm**

Para el modelo CFD se recomienda representar la boca de impulsión como un **círculo de radio 206.0 mm** con el caudal de **1.0667 m³/s** normal a la superficie, equivalente a una velocidad de **8 m/s**.

---

## 6. Rejillas de exfiltración / salida

### 6.1 Criterio de velocidad

Para mantener la presión positiva sin generar ruido excesivo ni corrientes de aire molestas, la velocidad facial en rejillas de exfiltración para laboratorios suele estar entre **2.5 y 4.0 m/s**. Se adopta **3.0 m/s** como punto de diseño.

### 6.2 Fórmula

\[
A_{exfil} = \frac{Q}{v_{salida}}
\]

Donde:
- \(A_{exfil}\) = Área neta total de rejillas de salida, m²
- \(Q = 1.0667 \text{ m}^3/\text{s}\)
- \(v_{salida}\) = Velocidad facial de salida, m/s

### 6.3 Desarrollo

Con \(v_{salida} = 3.0 \text{ m/s}\):

\[
A_{exfil} = \frac{1.0667}{3.0} = 0.3556 \text{ m}^2
\]

Si se instalan **3 rejillas de exfiltración**:

\[
A_{rejilla} = \frac{0.3556}{3} = 0.1185 \text{ m}^2
\]

Para una proporción ancho/alto de 0.95, las dimensiones calculadas son:

\[
h = \sqrt{\frac{A_{rejilla}}{0.95}} = \sqrt{\frac{0.1185}{0.95}} = 0.3532 \text{ m}
\]

\[
w = \frac{A_{rejilla}}{h} = \frac{0.1185}{0.3532} = 0.3355 \text{ m}
\]

### 6.4 Alternativas de configuración

| Velocidad salida (m/s) | Área total (m²) | N° rejillas | Área/rejilla (m²) | Dimensiones propuestas (mm) |
|------------------------|-----------------|-------------|-------------------|-----------------------------|
| 2.5 | 0.427 | 3 | 0.142 | 390 × 365 |
| **3.0** | **0.356** | **3** | **0.119** | **350 × 340** |
| 4.0 | 0.267 | 3 | 0.089 | 300 × 295 |

**Rejillas de salida propuestas:** **3 rejillas de 353 mm × 336 mm cada una** (normalizables a 350 mm × 340 mm), con velocidad de exfiltración de **3.0 m/s**.

---

## 7. Datos para el modelo CFD

| Elemento | Geometría | Dimensiones | Condición de contorno |
|----------|-----------|-------------|----------------------|
| Impulsión del ventilador | Círculo | Radio **206.0 mm** | Velocity inlet, **8 m/s** normal al plano |
| Rejilla de salida 1 | Rectángulo | **353 mm × 336 mm** | Velocity outlet, **3 m/s** normal al plano |
| Rejilla de salida 2 | Rectángulo | **353 mm × 336 mm** | Velocity outlet, **3 m/s** normal al plano |
| Rejilla de salida 3 | Rectángulo | **353 mm × 336 mm** | Velocity outlet, **3 m/s** normal al plano |
| Paredes del laboratorio | Superficies sólidas | Según geometría 3D | Wall, no slip |

**Notas para el CFD:**
- El caudal total de entrada (1.0667 m³/s) debe igualar el caudal total de salida (3 × 0.1185 m² × 3 m/s = 1.0665 m³/s).
- La diferencia mínima se debe al redondeo de dimensiones.
- El campo de presión relativa debe mostrar valores positivos dentro del laboratorio respecto a zonas adyacentes.
- Se recomienda colocar las rejillas de salida en paredes opuestas o perpendiculares a la impulsión para favorecer un flujo cruzado efectivo.

---

## 8. Resumen de resultados de diseño

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| Volumen efectivo | 320 | m³ |
| Renovaciones de aire | 12 | ren/h (ACH) |
| Caudal de diseño | 64.0 | m³/min |
| Caudal de diseño | 3 840 | m³/h |
| Caudal de diseño | **2 260** | **CFM** |
| Potencia estimada del ventilador | 0.444 | kW (a 250 Pa, η=0.6) |
| Potencia instalada recomendada | **1.0** | **HP** |
| Área de impulsión del ventilador | **0.1333** | **m²** |
| Radio de impulsión (CFD) | **206.0** | **mm** |
| Velocidad de impulsión | 8 | m/s |
| Número de rejillas de salida | **3** | unidades |
| Área neta por rejilla de salida | **0.1185** | **m²** |
| Dimensiones de rejillas de salida | **353 × 336** | **mm** |
| Velocidad de exfiltración | 3.0 | m/s |

---

## 9. Consideraciones adicionales para la presurización positiva

1. **Balance de masas:** para mantener presión positiva, el caudal de impulsión debe superar el caudal de extracción (si existe) más las fugas naturales del recinto. Una diferencia del **10–20 %** entre impulsión y extracción es común. En este diseño, las rejillas de salida están dimensionadas para que todo el caudal de impulsión se exfiltre controladamente.

2. **Extracción localizada:** si se requiere campana o puntos de captación, debe compensarse con mayor impulsión para preservar la presión positiva en el volumen general.

3. **Control de presión diferencial:** se recomienda instalar sensor de presión diferencial entre el laboratorio y el corredor/zona adyacente, con set-point típico de **+12.5 Pa a +25 Pa** (+0.05 a +0.10 inH₂O).

4. **Filtración:** el aire de impulsión debe filtrarse al menos con filtros MERV 13–14; para aplicaciones de mayor riesgo, HEPA (H13/H14) según normativa sanitaria local.

5. **Rendijas y estanqueidad:** puertas con burletes, umbras herméticas y sellado de pasos de instalaciones facilitan mantener la presión positiva con menor caudal de fugas.

6. **Modelo CFD:** se sugiere simular el flujo con condiciones de inyección circular (radio 206.0 mm, 8 m/s) y salida por las tres rejillas (353 × 336 mm, 3 m/s), evaluando la distribución de velocidades, edad del aire y presión relativa en el recinto.

---

## 10. Referencias

- ASHRAE. (2021). *ANSI/ASHRAE Standard 170-2021, Ventilation of Health Care Facilities*.
- ASHRAE. (2022). *ANSI/ASHRAE Standard 62.1-2022, Ventilation for Acceptable Indoor Air Quality*.
- NFPA. (2021). *NFPA 99, Health Care Facilities Code*.
- OSHA. (2012). *29 CFR 1910.1450, Occupational Exposure to Hazardous Chemicals in Laboratories*.
- World Health Organization. (2004). *Laboratory Biosafety Manual* (3rd ed.). Geneva: WHO.
- National Institutes of Health. (2023). *NIH Design Requirements Manual*.

---

*Documento generado para el proyecto HVAC — Laboratorio Brinsa.*  
*Fecha: 2026-07-16*

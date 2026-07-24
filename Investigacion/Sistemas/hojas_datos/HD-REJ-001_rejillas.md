# Hoja de datos: rejillas de exfiltración con malla anti-insectos

| Campo | Valor |
|---|---|
| Código | HD-REJ-001 |
| Revisión | 0 |
| Fecha | 2026-07-23 |
| Proyecto | P2437-HV-INF-001 — BRINSA, laboratorio de análisis industrial, Cajicá |
| Etiqueta de equipo | REJ-001 a REJ-003 (rejillas de exfiltración) |

---

## 1. Servicio

1.1. Descarga del caudal de exfiltración del laboratorio presurizado (+25 Pa) hacia el exterior, a través de la envolvente del recinto. Las rejillas son la trayectoria de salida permanente del aire y, con el sistema detenido, una vía potencial de ingreso: por ello incorporan malla anti-insectos. Ambiente exterior corrosivo (atmósfera clorada de planta de hipoclorito de calcio).

## 2. Condiciones de operación y desempeño

**Tabla 1.** Condiciones de diseño (valores congelados de la memoria de cálculo).

| Parámetro | Valor |
|---|---|
| Cantidad | 3 unidades |
| Dimensiones faciales (unitarias) | 353×336 mm (área facial 0.1187 m²) |
| Caudal total de exfiltración | 3 840 m³/h (1.0667 m³/s) |
| Velocidad facial | 3 m/s |
| ΔP unitaria (cierre de orificio, C_d = 0.60, en el sitio) | 11 Pa |
| ΔP equivalente a densidad estándar (ρ = 1.2 kg/m³) | 15 Pa |
| Densidad del aire de diseño | 0.88 kg/m³ (2 558 msnm, 74.1 kPa) |

2.1. Nota de contexto: la configuración sin damper de alivio (rejillas a 4 m/s) solo alcanzaría 19.6 Pa de presurización a esta altitud; cerrar el balance a 25 Pa sin damper requeriría un área total de 0.236 m² (0.079 m² por rejilla ≈ 280×281 mm a 4.5 m/s). El sistema adoptado conserva las tres rejillas de 353×336 mm y cierra el balance con el damper barométrico (componente obligatorio; ver HD-INST-001 e informe_investigacion.md §3.2.4).

## 3. Construcción y áreas netas

**Tabla 2.** Especificación constructiva.

| Característica | Especificación |
|---|---|
| Tipo de núcleo | Eggcrate (panal) ½×½×½ in (12.7 mm), máxima área libre |
| Área libre del núcleo | ≥ 90 % (cifra repetida en catálogos del tipo; [Airfoil RC-FCR5](https://airfoil.com.au/product/removable-core-fixing-clip-eggcrate-grille-rc-fcr5/), consulta 2026-07-23) |
| Malla anti-insectos | Tejido 18×18, abertura ≈1 mm, alambre 0.45 mm, área abierta ≥ 48 % ([tabla Industrial Metal Mesh](https://www.industrialmetalmesh.com/sale-54819921-micron-304-316l-stainless-steel-wire-mesh-screen-filter-mesh.html), consulta 2026-07-23); excluye insectos comunes |
| Área neta combinada (núcleo + malla) | ≈ 45 % del área facial (dato típico: 0.90 × 0.50) |
| Material de la rejilla | Inox 316L (primera opción) o aluminio anodizado 6063-T5 (alternativa) |
| Material de la malla | Inox 316 |
| Montaje de la malla | Marco desmontable para limpieza periódica |
| Par galvánico | Si se combina marco de aluminio con malla inox, aislamiento dieléctrico (dato típico de ingeniería) |
| Ensayo de desempeño | ASHRAE 70 (medición de rejillas) |

3.1. La malla domina la pérdida del conjunto; el dimensionamiento por área neta combinada y la ΔP calculada por cierre de orificio (11 Pa) deben verificarse contra el área efectiva (Ak) del fabricante seleccionado (por confirmar con proveedor).

## 4. Candidatos comerciales

**Tabla 3.** Candidatos (consulta 2026-07-23).

| Producto | Tipo / material | Pros | Contras | Fuente |
|---|---|---|---|---|
| Titus 50F / 50R | Eggcrate ½ in; aluminio, con versión íntegramente inox de fábrica | «Highest free area of any return grille»; única opción inox de catálogo | Importación; tamaño 353×336 por pedido | [Titus 50F (PDF)](https://www.titus-hvac.com/file/1228/50F_50Rrprod_specialized_2017.pdf) |
| Krueger EGC5 | Eggcrate ½ in; aluminio | Amplia gama de tamaños (6×4 in a 96×96 in) | Sin ejecución inox | [Krueger EGC5](https://www.krueger-hvac.com/Catalog%20Home/Grilles/Grilles%20-%20Return/EGC5) |
| ProAire S.A.S (Bogotá) | Fabricación a medida con corte láser, inox 316 | Medida exacta 353×336 y ejecución inox 316L local; vía recomendada | Submittal y Ak por confirmar con proveedor | [proairecolombia.com](https://www.proairecolombia.com/productos/rejillas-y-difusores.html) |
| Laminaire (Colombia) | Rejillas y difusores en aluminio a pedido | Fabricación local con software de selección; marco para malla a pedido | Confirmar ejecución inox | [laminaire.net](https://laminaire.net/) |
| CL Ingeniería (Bogotá) | Rejillas, dampers y accesorios HVAC | Canal local adicional | Catálogo genérico | [clingenieria.co](https://clingenieria.co/) |

## 5. Instalación

5.1. Montaje a ras de muro exterior con marco perimetral sellado con silicona RTV neutra (compatible con hipoclorito; [Chemical Resistance of RTV Silicone Sealants (PDF)](https://irp.cdn-website.com/63168859/files/uploaded/Chemical%20Resistance%20of%20RTV%20Silicone%20Sealants%20Chart.pdf), consulta 2026-07-23) y ferretería inox 316 (A4). 5.2. Las bocas exteriores se orientan preferentemente a sotavento respecto de las fuentes de cloro de la planta. 5.3. Programa de limpieza de la malla según carga de polvo observada en comisionamiento (dato típico de operación).

## 6. Normas aplicables

6.1. ASHRAE 70 (método de ensayo y reporte de desempeño de rejillas); correlación de área libre para transferencia de aire según [Building Science BA-0006](https://buildingscience.com/sites/default/files/migrate/pdf/BA-0006_Discuss_transfer_grilles.pdf) (consulta 2026-07-23); ISO 12944 / NACE-AMPP para la selección de materiales en el ambiente clorado.

---
fecha: 2026-07-23
tags: [codificacion, normalizacion]
---

# Codificación de documentos del proyecto P2437 según GP-N-09

**Proyecto:** P2437 — Diseño del sistema de ventilación y presurización del laboratorio BRINSA
**Cliente:** BRINSA (Cajicá, Cundinamarca)
**Norma aplicada:** GP-N-09 — Normalización de la documentación de los proyectos (DML Ingenieros Consultores S.A.S.)
**Fecha:** 23/07/2026 · Revisión: CERO (0)

## 1. Objetivo

Asignar a cada documento generado en el proyecto P2437 un código conforme a la norma
GP-N-09, de modo que la documentación del proyecto quede clasificada, identificada y
lista para el Listado de Documentos del Proyecto y para entrega al cliente.

## 2. Alcance

Aplica únicamente a la **codificación** (estructura del código, siglas de tipo de
documento, especialidad, consecutivo y revisión). Los demás requisitos de GP-N-09
(tamaños de papel, encabezados, pies de página, rótulos AutoCAD, firmas) quedan
fuera de este informe.

## 3. Esquema de codificación (síntesis de GP-N-09)

El código de un documento se compone de cuatro campos separados por guiones:

```
P<proyecto>-<ESPECIALIDAD>-<TIPO>-<consecutivo>
```

| Campo | Regla | Ejemplo |
| --- | --- | --- |
| Proyecto | Número de la Orden de Proyecto (proceso Ventas) | P2437 |
| Especialidad | Sigla de la especialidad responsable | HV |
| Tipo | Sigla del tipo de documento | INF |
| Consecutivo | Número de tres dígitos por tipo y especialidad | 001 |

Ejemplo de la norma: `P2644-PR-ESP-015` = especificación N° 015 de la especialidad
Procesos del proyecto P2644.

Reglas complementarias: todo documento inicia en **Revisión CERO (0)** y solo la
última revisión es el documento vigente; la fecha se registra en formato corto
dd/mm/aaaa.

### 3.1. Siglas de tipo de documento aplicables a este proyecto

| Sigla | Tipo de documento | Sub-carpeta (GP-N-09) |
| --- | --- | --- |
| INF | Informe | INFORMES |
| DTS | Hoja de datos de equipo o instrumento | HOJAS DE DATOS |
| DOC | Documento técnico | DOCUMENTOS TÉCNICOS |
| CAL | Memoria de cálculo | MEMORIAS DE CÁLCULO |
| LIS | Listado | LISTADOS |
| ESP | Especificación | ESPECIFICACIONES |
| RFQ | Requerimiento de cotización | DOCUMENTOS TÉCNICOS |
| PLN | Plano, LayOut, PFD, P&ID | PLANOS |

### 3.2. Siglas de especialidad aplicables a este proyecto

| Sigla | Especialidad | Uso en P2437 |
| --- | --- | --- |
| HV | Aire acondicionado (HVAC) | Especialidad principal del sistema |
| PR | Proceso | Hoja de datos de proceso del equipo (existente) |
| IC | Instrumentación y control | Instrumentos de presión diferencial |

## 4. Codificación propuesta para los documentos del proyecto

### 4.1. Documentos ya codificados conforme a GP-N-09

| Documento | Archivo actual | Código GP-N-09 | Estado |
| --- | --- | --- | --- |
| Informe técnico del sistema de ventilación y presurización | `Latex/02_informe_tex/P2437-HV-INF-001 REV0.tex/.pdf` | **P2437-HV-INF-001** | Conforme (Rev. 0) |

### 4.2. Documentos por codificar (propuesta)

| Documento | Archivo actual | Código propuesto | Tipo | Especialidad |
| --- | --- | --- | --- | --- |
| Memoria de cálculo del sistema | `memoriadecalculo.xlsx` | **P2437-HV-CAL-001** | CAL | HV |
| Informe de investigación del sistema (componentes, equipos, normativa) | `Investigacion/Sistemas/informe_investigacion.md` | **P2437-HV-INF-002** | INF | HV |
| Listado de equipos y accesorios (BOQ) | `Investigacion/Sistemas/listado_equipos.md` | **P2437-HV-LIS-001** | LIS | HV |
| Hoja de datos del ventilador centrífugo PRFV | `Investigacion/Sistemas/hojas_datos/HD-VENT-001_ventilador.md` | **P2437-HV-DTS-001** | DTS | HV |
| Hoja de datos del filtro MERV 13-14 | `Investigacion/Sistemas/hojas_datos/HD-FILT-001_filtro_merv.md` | **P2437-HV-DTS-002** | DTS | HV |
| Hoja de datos de rejillas de exfiltración | `Investigacion/Sistemas/hojas_datos/HD-REJ-001_rejillas.md` | **P2437-HV-DTS-003** | DTS | HV |
| Hoja de datos de instrumentos de presión diferencial | `Investigacion/Sistemas/hojas_datos/HD-INST-001_instrumentos_presion.md` | **P2437-IC-DTS-001** | DTS | IC |

Las bases de diseño **no** se emiten como documento aparte: van como sección
"Bases de Diseño" del informe **P2437-HV-INF-001** (se retira la propuesta inicial
P2437-HV-DOC-001). El archivo `bases_diseno.yaml` permanece como fuente de datos
para cálculos, no como entregable.

Los códigos internos actuales de las hojas de datos (HD-VENT-001, HD-FILT-001,
HD-REJ-001, HD-INST-001) quedan como alias de trazabilidad interna; el código
oficial para gestión y entrega es el GP-N-09.

### 4.3. Documentos previstos a futuro (reserva de códigos)

| Documento previsto | Código reservado | Nota |
| --- | --- | --- |
| Requerimiento de cotización del paquete de ventilación | P2437-HV-RFQ-001 | Siguiente etapa (compras) |
| Especificación de montaje y puesta en marcha | P2437-HV-ESP-001 | Ingeniería de detalle |
| Planos de instalación (LayOut / P&ID) | P2437-HV-PLN-001… | Cuando se disponga de planos del laboratorio |
| Listado de Documentos del Proyecto | P2437-DI-LIS-001 | Control documental (ver §6) |

### 4.3.1. Estructura de emisión de entregables

Los entregables codificados se publican en la carpeta `Emisiones/`, organizada por
tipo de documento según las sub-carpetas de GP-N-09: `1.0 HV-INFORMES/`,
`2.0 HV-MEMORIAS DE CALCULO/`, `3.0 HV-HOJAS DE DATOS/` y `4.0 HV-LISTADOS/`.
Los archivos de `Emisiones/` son copias generadas automáticamente por
`scripts/emitir.py` (que regenera el Excel, recompila los informes LaTeX y copia
los entregables con sus nombres codificados), con trazabilidad en
`Emisiones/MANIFIESTO_EMISION.md`. Regla: las fuentes se editan, las emisiones se
regeneran; nunca se edita a mano un archivo emitido.

**Excepción de nomenclatura (2026-07-27):** por solicitud del cliente/proyecto,
los nombres de archivo de los entregables emitidos **no incluyen la revisión**
(`REV1`) al final. El código GP-N-09 del documento se conserva sin sufijo de
revisión; la revisión vigente se indica en la portada/metadatos del documento y
en el control de versiones de git. Ejemplo: el informe se emite como
`P2437-HV-INF-001.pdf` (no `P2437-HV-INF-001 REV1.pdf`).

Formatos corporativos obligatorios (carpeta `FormatosDocumentos/`): la memoria
CAL-001 y las hojas de datos DTS se generan como libros Excel de **2 hojas**
(PORTADA + especificación única) desde las plantillas `CAL.xlsx` y `DTS.xlsx`,
mediante `generar_excel.py` y `scripts/generar_dts.py` respectivamente.

### 4.4. Documentos fuera del alcance de GP-N-09

| Documento / carpeta | Motivo |
| --- | --- |
| `AGENTS.md`, `contexto.md`, `task/todo.md`, `vault/`, `.agents/` | Gestión interna del flujo de trabajo con el agente; no son entregables del proyecto |
| `generar_excel.py`, `Latex/scripts/`, `Latex/01_calculos/src/` | Herramientas de software internas, no documentos |
| `docs/` (dashboard web) | Herramienta digital de visualización; no es documento en el sentido de GP-N-09 |
| `resultado simulaciones/` (capturas CFD) | Registros de apoyo; se codificarán como anexos del informe CFD cuando se emita |

## 5. Desviaciones y observaciones detectadas

1. **`HojasDatos/P2437-PR-DT-001.xlsx`**: usa la sigla `DT`, pero GP-N-09 define
   `DTS` para hojas de datos. Si el documento se regenera, debería renombrarse a
   `P2437-PR-DTS-001`. Como puede tratarse de un archivo recibido del cliente, se
   recomienda verificar su origen antes de renombrarlo.
2. **Inconsistencia en la propia norma**: el ejemplo 2 de GP-N-09 usa la sigla
   `LAY` para LayOut, pero la tabla de tipos de documento solo define `PLN`
   ("Plano, LayOut, PFD, PID"). Se adopta `PLN` (la tabla manda sobre el ejemplo);
   conviene elevar la observación al responsable de normalización de DML.
3. **Especialidad de las hojas de datos de instrumentos**: se asignó IC a
   HD-INST-001 por ser instrumentación de medición; las demás DTS quedan en HV por
   ser equipos del sistema de ventilación. Si DML prefiere concentrar todo en la
   especialidad líder (HV), el consecutivo sería P2437-HV-DTS-004.
4. **Excepción de nomenclatura para entregables (2026-07-27):** los archivos
   emitidos en `Emisiones/` no llevan sufijo ` REV1` en el nombre, aunque la
   revisión vigente sea REV1. La revisión se documenta en la portada del archivo
   y en git. Ver §4.3.1.
5. **Revisiones**: todos los documentos del proyecto están en Revisión CERO (0),
   conforme a la norma. Las rutas `Latex/06_entregables/REV0/` ya reflejan este
   criterio.

## 6. Recomendaciones

1. Adoptar este informe como base del **Listado de Documentos del Proyecto**
   (P2437-DI-LIS-001), que GP-N-09 menciona como referencia para el control de
   revisiones vigentes.
2. Insertar el código GP-N-09 en el encabezado de cada documento (las hojas de
   datos ya tienen encabezado propio; basta agregar la línea "Código DML").
3. No renombrar archivos físicos en esta etapa: la bibliografía del informe
   `P2437-HV-INF-001` referencia las rutas actuales de las hojas de datos; el
   renombrado se haría en la emisión de la Rev. 1 junto con la actualización de
   citas.

## 7. Referencias

- GP-N-09 — Normalización de la documentación de los proyectos, DML Ingenieros
  Consultores S.A.S. (`Codificacion/GP-N-09.docx`, consulta 23/07/2026).
- SGI-P-01 — Procedimiento para el control de la información documentada (citado
  por GP-N-09 para el control de revisiones).
- [[estructuraproyecto]] — mapa de archivos del proyecto.

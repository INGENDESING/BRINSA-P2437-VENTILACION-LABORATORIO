---
fecha: 2026-07-28
estado: vigente
tags: [decision]
---

# Decisión: formato Excel corporativo A3 horizontal, TNR 28, verde claro DML

## Decisión

Los 4 libros Excel generados (CAL-001, DTS-001/002/003, LIS-001) usan hoja A3
horizontal con ajuste a una página de ancho, Times New Roman 28 en todo el
contenido, encabezados de tabla en verde claro DML `C6E0B4` con texto verde
oscuro `375623` (sin azul `1F4E78`), exactamente una fila en blanco entre
bloques y alturas de fila ≥ 38 pt. Todo el formato se define en el módulo
único `scripts/estilos_excel.py` y se verifica con
`scripts/verificar_formato_excel.py`. El encabezado corporativo (filas 1-7),
la portada y el PDF alternativo de DTS-001 conservan su formato anterior.

## Motivo

Instrucción explícita del cliente (2026-07-28): los Excel de especificación se
veían mal (celdas pequeñas, texto perdido, demasiadas filas en blanco) y el
formato se perdía en cada regeneración porque el código de estilos estaba
triplicado en los 3 generadores. El módulo único resuelve la causa raíz:
cualquier cambio futuro de formato se edita una sola vez.

## Alternativas consideradas

- Escalar también el encabezado corporativo (filas 1-7) a 28 pt → descartado
  por el usuario: deforma el bloque de plantilla; se conserva intacto.
- Actualizar también el PDF alternativo de DTS-001 → descartado por el usuario
  en este plan (solo Excel).
- Mantener estilos locales en cada generador → descartado: es la causa de la
  divergencia de formato entre regeneraciones.

## Referencias

- `scripts/estilos_excel.py`, `scripts/verificar_formato_excel.py`
- Plan y revisión en `task/todo.md` (sección "Rediseño estético integral de
  los Excel generados", 2026-07-28)
- Bitácora [[2026-07-28]]

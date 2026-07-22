# Plan: Organización de Repositorio y Despliegue de Web Estática

## Contexto
- Objetivo: Preparar el proyecto para control de versiones en GitHub y crear un dashboard web estático para presentar los cálculos de la presurización.
- Cliente / Proyecto DML: Laboratorio Brinsa
- Normas aplicables: Buenas prácticas de versionado (Git) y estándares modernos de UI/UX para la web.

## Supuestos clave
- [ ] La interfaz web será estática (Vanilla HTML/CSS/JS) para permitir su despliegue sencillo a través de GitHub Pages.
- [ ] Los archivos temporales generados por la compilación de LaTeX (.aux, .log, .out, .toc) no tienen valor histórico y deben excluirse mediante `.gitignore`.
- [ ] La página actuará como un resumen técnico e interactivo de los resultados presentes en el archivo Excel y en la memoria de cálculo.

## Tareas
- [ ] T1. **Limpieza y `.gitignore`**: Crear `.gitignore` para excluir archivos innecesarios de LaTeX y Python (`__pycache__`, etc.).
- [ ] T2. **Repositorio Local**: Inicializar Git, agregar los archivos fuente válidos (`.py`, `.tex`, `.md`, `.xlsx`, `.pdf`) y generar el commit inicial.
- [ ] T3. **Estructura Web**: Crear carpeta `docs/` (configuración recomendada para GitHub Pages) conteniendo `index.html`, `styles.css` y `app.js`.
- [ ] T4. **Desarrollo Frontend**: Implementar un diseño "Premium" (paleta de colores curada estilo "dark mode", fuentes modernas, tablas tipo Elsevier adaptadas a web y micro-animaciones) mostrando las entradas y resultados de diseño.

## Riesgos / Puntos de verificación
- [ ] Validación dimensional: Asegurar que los datos numéricos mostrados en la web sean exactamente los mismos que figuran en el documento formal y el Excel.
- [ ] El directorio debe quedar limpio antes del commit (sin dejar rastros de archivos temporales que inflen el repositorio).

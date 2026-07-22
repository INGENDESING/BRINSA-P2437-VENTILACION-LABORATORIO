from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, NamedStyle
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import ColorScaleRule
import os
import math

# Crear libro
wb = Workbook()

# Estilos base
header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(color="FFFFFF", bold=True, size=11)
input_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
input_font = Font(bold=True, color="000000")
result_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
result_font = Font(bold=True, color="006100")
formula_fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
title_font = Font(bold=True, size=14, color="1F4E78")
subtitle_font = Font(bold=True, size=11, color="1F4E78")
thin_border = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin')
)

def apply_border(ws, start_row, start_col, end_row, end_col):
    for row in ws.iter_rows(min_row=start_row, max_row=end_row, min_col=start_col, max_col=end_col):
        for cell in row:
            cell.border = thin_border

def auto_width(ws):
    for column in ws.columns:
        max_length = 0
        column_letter = get_column_letter(column[0].column)
        for cell in column:
            try:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        ws.column_dimensions[column_letter].width = min(max(max_length + 2, 10), 60)

# ===================== HOJA 1: DATOS GENERALES =====================
ws1 = wb.active
ws1.title = "Datos Generales"
ws1['A1'] = "MEMORIA DE CÁLCULO — SISTEMA DE VENTILACIÓN Y PRESURIZACIÓN"
ws1['A1'].font = Font(bold=True, size=16, color="1F4E78")
ws1.merge_cells('A1:D1')

ws1['A3'] = "Información del proyecto"
ws1['A3'].font = title_font
ws1.merge_cells('A3:D3')

info = [
    ["Concepto", "Valor", "Unidad", "Observación"],
    ["Nombre del proyecto", "Laboratorio Brinsa", "-", "Ventilación por impulsión con presión positiva"],
    ["Ubicación", "C:\\Users\\ingen\\OneDrive\\Escritorio\\HVAC\\Calculos", "-", "Carpeta de cálculos del proyecto"],
    ["Volumen efectivo del laboratorio (V)", "320", "m³", "Medición / modelo 3D"],
    ["Renovaciones de aire (N)", "12", "ren/h", "Sustentado normativamente"],
    ["Objetivo", "Presurización positiva", "-", "Evitar ingreso de contaminantes"],
    ["Estrategia", "Ventilador directo + rejillas de exfiltración", "-", "Sin ductos de impulsión"],
]

for i, row in enumerate(info, start=5):
    for j, value in enumerate(row, start=1):
        cell = ws1.cell(row=i, column=j, value=value)
        if i == 5:
            cell.fill = header_fill
            cell.font = header_font
        else:
            cell.border = thin_border
        cell.alignment = Alignment(vertical='center', wrap_text=True)

ws1['A14'] = "Objetivo del documento"
ws1['A14'].font = subtitle_font
ws1.merge_cells('A14:D14')
ws1['A15'] = "Presentar de forma atómica, funcional y verificable el cálculo del caudal de aire, potencia del ventilador, área de impulsión del ventilador (sin ductos) y área/dimensiones de las rejillas de exfiltración para modelado CFD, con sustentación normativa."
ws1['A15'].alignment = Alignment(wrap_text=True)
ws1.merge_cells('A15:D17')

apply_border(ws1, 5, 1, 11, 4)
auto_width(ws1)

# ===================== HOJA 2: ENTRADAS =====================
ws2 = wb.create_sheet("Entradas")
ws2['A1'] = "PARÁMETROS DE ENTRADA"
ws2['A1'].font = title_font
ws2.merge_cells('A1:E1')

headers = ["Parámetro", "Símbolo", "Valor", "Unidad", "Referencia / Nota"]
for j, h in enumerate(headers, start=1):
    cell = ws2.cell(row=3, column=j, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.border = thin_border

entradas = [
    ["Volumen efectivo del laboratorio", "V", 320, "m³", "Medición directa o del modelo"],
    ["Renovaciones de aire", "N", 12, "ren/h", "Ver hoja Normativa"],
    ["Presión total estimada del ventilador", "ΔP", 250, "Pa", "Incluye filtro y rejillas de exfiltración"],
    ["Eficiencia total del ventilador", "η", 0.60, "-", "Centrífugo/axial típico"],
    ["Velocidad en boca del ventilador", "v_vent", 8.0, "m/s", "Para CFD, rango 6–12 m/s"],
    ["Velocidad de exfiltración en rejillas", "v_sal", 3.0, "m/s", "Rango recomendado 2.5–4.0 m/s"],
    ["Número de rejillas de salida", "n_rej", 3, "unid.", "Distribución propuesta"],
    ["Proporción ancho/alto rejilla", "prop", 0.95, "-", "353 mm × 336 mm ≈ 0.95"],
    ["Set-point presión diferencial", "ΔP_pos", 25, "Pa", "Presión positiva vs zona adyacente"],
]

for i, row in enumerate(entradas, start=4):
    for j, value in enumerate(row, start=1):
        cell = ws2.cell(row=i, column=j, value=value)
        cell.border = thin_border
        if j == 3:
            cell.fill = input_fill
            cell.font = input_font
        cell.alignment = Alignment(vertical='center', wrap_text=True)

# Notas
ws2['A15'] = "Notas:"
ws2['A15'].font = subtitle_font
ws2['A16'] = "• Modifique los valores en amarillo; todos los cálculos se actualizan automáticamente."
ws2['A17'] = "• Las fórmulas están visibles en la barra de fórmulas de cada celda."
ws2['A18'] = "• Unidades: 1 m³/min = 35.3147 CFM; 1 kW = 1.341 HP."
ws2.merge_cells('A16:E16')
ws2.merge_cells('A17:E17')
ws2.merge_cells('A18:E18')

apply_border(ws2, 3, 1, 12, 5)
auto_width(ws2)

# ===================== HOJA 3: CÁLCULOS =====================
ws3 = wb.create_sheet("Cálculos")
ws3['A1'] = "DESARROLLO DE CÁLCULOS"
ws3['A1'].font = title_font
ws3.merge_cells('A1:F1')

# Encabezados
headers3 = ["Paso", "Descripción", "Fórmula / Valor", "Resultado", "Unidad", "Referencia celda"]
for j, h in enumerate(headers3, start=1):
    cell = ws3.cell(row=3, column=j, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.border = thin_border

calculos = [
    ["1", "Caudal de aire volumétrico", "Q = V × N / 60", "=Entradas!C4*Entradas!C5/60", "m³/min", "=Cálculos!D4"],
    ["2", "Caudal de aire en m³/h", "Q_h = Q × 60", "=D4*60", "m³/h", "=Cálculos!D5"],
    ["3", "Caudal de aire en CFM", "Q_cfm = Q × 35.3147", "=D4*35.3147", "CFM", "=Cálculos!D6"],
    ["4", "Caudal en m³/s", "Q_s = Q / 60", "=D4/60", "m³/s", "=Cálculos!D7"],
    ["5", "Potencia teórica del ventilador", "P = Q_s × ΔP / (η × 1000)", "=D7*Entradas!C6/(Entradas!C7*1000)", "kW", "=Cálculos!D8"],
    ["6", "Potencia en HP", "HP = P × 1.341", "=D8*1.341", "HP", "=Cálculos!D9"],
    ["7", "Área de impulsión del ventilador", "A_vent = Q_s / v_vent", "=D7/Entradas!C8", "m²", "=Cálculos!D10"],
    ["8", "Diámetro equivalente del ventilador", "D = √(4×A_vent/π)", "=SQRT(4*D10/PI())", "m", "=Cálculos!D11"],
    ["9", "Radio del ventilador", "r = D / 2", "=D11/2", "m", "=Cálculos!D12"],
    ["10", "Radio del ventilador en mm", "r_mm = r × 1000", "=D12*1000", "mm", "=Cálculos!D13"],
    ["11", "Área neta total de rejillas de salida", "A_exfil = Q_s / v_sal", "=D7/Entradas!C9", "m²", "=Cálculos!D14"],
    ["12", "Área neta por rejilla de salida", "A_rej = A_exfil / n_rej", "=D14/Entradas!C10", "m²", "=Cálculos!D15"],
    ["13", "Altura de rejilla (proporción dada)", "h = √(A_rej / prop)", "=SQRT(D15/Entradas!C11)", "m", "=Cálculos!D16"],
    ["14", "Ancho de rejilla", "w = A_rej / h", "=D15/D16", "m", "=Cálculos!D17"],
    ["15", "Altura de rejilla en mm", "h_mm = h × 1000", "=D16*1000", "mm", "=Cálculos!D18"],
    ["16", "Ancho de rejilla en mm", "w_mm = w × 1000", "=D17*1000", "mm", "=Cálculos!D19"],
]

for i, row in enumerate(calculos, start=4):
    for j, value in enumerate(row, start=1):
        cell = ws3.cell(row=i, column=j, value=value)
        cell.border = thin_border
        cell.alignment = Alignment(vertical='center', wrap_text=True)
        if j == 4:
            cell.fill = formula_fill
            cell.font = Font(color="000080", bold=True)
            cell.number_format = '0.0000'

# ===================== HOJA 4: RESULTADOS =====================
ws4 = wb.create_sheet("Resultados")
ws4['A1'] = "RESUMEN DE RESULTADOS DE DISEÑO"
ws4['A1'].font = title_font
ws4.merge_cells('A1:D1')

headers4 = ["Parámetro", "Valor", "Unidad", "Observación"]
for j, h in enumerate(headers4, start=1):
    cell = ws4.cell(row=3, column=j, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.border = thin_border

resultados = [
    ["Caudal de diseño", "='Cálculos'!D4", "m³/min", "Caudal de impulsión requerido"],
    ["Caudal de diseño", "='Cálculos'!D5", "m³/h", "Equivalente en metros cúbicos por hora"],
    ["Caudal de diseño", "='Cálculos'!D6", "CFM", "Equivalente en pies cúbicos por minuto"],
    ["Potencia teórica del ventilador", "='Cálculos'!D8", "kW", "A 250 Pa y η=0.60"],
    ["Potencia teórica del ventilador", "='Cálculos'!D9", "HP", "Unidades imperiales"],
    ["Potencia instalada recomendada", "=ROUNDUP('Cálculos'!D9,0)", "HP", "Motor comercial con margen"],
    ["Área de impulsión del ventilador", "='Cálculos'!D10", "m²", "Boca del ventilador"],
    ["Diámetro equivalente del ventilador", "='Cálculos'!D11", "m", "Para referencia"],
    ["Radio del ventilador (CFD)", "='Cálculos'!D13", "mm", "Círculo de inyección"],
    ["Velocidad de impulsión", "=Entradas!C8", "m/s", "Condición de entrada CFD"],
    ["Área neta total de rejillas de salida", "='Cálculos'!D14", "m²", "A v=3 m/s"],
    ["Número de rejillas de salida", "=Entradas!C10", "unid.", "Distribución propuesta"],
    ["Área neta por rejilla de salida", "='Cálculos'!D15", "m²", "Cada rejilla"],
    ["Altura de rejilla de salida", "='Cálculos'!D18", "mm", "Dimensiones para CFD"],
    ["Ancho de rejilla de salida", "='Cálculos'!D19", "mm", "Dimensiones para CFD"],
    ["Velocidad de exfiltración", "=Entradas!C9", "m/s", "Condición de salida CFD"],
]

for i, row in enumerate(resultados, start=4):
    for j, value in enumerate(row, start=1):
        cell = ws4.cell(row=i, column=j, value=value)
        cell.border = thin_border
        cell.alignment = Alignment(vertical='center', wrap_text=True)
        if j == 2:
            cell.fill = result_fill
            cell.font = result_font
            cell.number_format = '0.00'

# Calcular valores numéricos en Python para Vista Rápida
V = float(entradas[0][2])
N = float(entradas[1][2])
deltaP = float(entradas[2][2])
eta = float(entradas[3][2])
v_vent = float(entradas[4][2])
v_sal = float(entradas[5][2])
n_rej = float(entradas[6][2])
prop = float(entradas[7][2])

Q_m3min = V * N / 60.0
Q_m3h = Q_m3min * 60.0
Q_cfm = Q_m3min * 35.3147
Q_m3s = Q_m3min / 60.0
P_kW = Q_m3s * deltaP / (eta * 1000.0)
P_HP = P_kW * 1.341
A_vent = Q_m3s / v_vent
D_vent = (4 * A_vent / math.pi) ** 0.5
r_vent = D_vent / 2.0
r_vent_mm = r_vent * 1000.0
A_exfil = Q_m3s / v_sal
A_rej = A_exfil / n_rej
h_rej = (A_rej / prop) ** 0.5
w_rej = A_rej / h_rej
h_rej_mm = h_rej * 1000.0
w_rej_mm = w_rej * 1000.0

apply_border(ws4, 3, 1, 19, 4)
auto_width(ws4)

# ===================== HOJA 5: NORMATIVA =====================
ws5 = wb.create_sheet("Normativa")
ws5['A1'] = "SUSTENTACIÓN NORMATIVA — 12 RENOVACIONES/HORA"
ws5['A1'].font = title_font
ws5.merge_cells('A1:E1')

headers5 = ["Norma / Guía", "Año / Edición", "Recomendación ACH", "Observación"]
for j, h in enumerate(headers5, start=1):
    cell = ws5.cell(row=3, column=j, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.border = thin_border

normas = [
    ["ASHRAE 170 — Ventilation of Health Care Facilities", "2021", "6–15 ACH", "Laboratorios clínicos/procedimiento"],
    ["ASHRAE 62.1 — Ventilation for Acceptable IAQ", "2022", "Por ocupación y área", "Caudal mínimo de aire exterior"],
    ["OSHA 29 CFR 1910.1450 — Laboratory Standard", "2012", "Según PEL", "Ventilación para control de exposición"],
    ["NFPA 99 — Health Care Facilities Code", "2021", "Cumplimiento de sistemas", "Fiabilidad de sistemas de aire"],
    ["WHO — Laboratory Biosafety Manual (BSL-2)", "2004", "6–12 ACH", "12 ACH = límite superior BSL-2"],
    ["WHO — Laboratory Biosafety Manual (BSL-3)", "2004", "12–15 ACH", "12 ACH = umbral inferior BSL-3"],
    ["NIH — Design Requirements Manual", "2023", "10–12 ACH", "Punto de diseño para laboratorios biomédicos"],
]

for i, row in enumerate(normas, start=4):
    for j, value in enumerate(row, start=1):
        cell = ws5.cell(row=i, column=j, value=value)
        cell.border = thin_border
        cell.alignment = Alignment(vertical='center', wrap_text=True)

ws5['A13'] = "Conclusión"
ws5['A13'].font = subtitle_font
ws5.merge_cells('A13:E13')
ws5['A14'] = "La selección de 12 renovaciones de aire por hora está sustentada por las guías internacionales de bioseguridad (WHO BSL-2/BSL-3, NIH DRM) y los estándares de ventilación de ASHRAE para instalaciones de salud."
ws5['A14'].alignment = Alignment(wrap_text=True)
ws5.merge_cells('A14:E16')

apply_border(ws5, 3, 1, 10, 4)
auto_width(ws5)

# ===================== HOJA 6: VISTA RÁPIDA (valores precalculados) =====================
ws6 = wb.create_sheet("Vista Rápida")
ws6['A1'] = "VISTA RÁPIDA — RESULTADOS PRECARGADOS"
ws6['A1'].font = title_font
ws6.merge_cells('A1:D1')

headers6 = ["Parámetro", "Valor", "Unidad", "Observación"]
for j, h in enumerate(headers6, start=1):
    cell = ws6.cell(row=3, column=j, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.border = thin_border

vista_rapida = [
    ["Caudal de diseño", Q_m3min, "m³/min", "Caudal de impulsión requerido"],
    ["Caudal de diseño", Q_m3h, "m³/h", "Equivalente en metros cúbicos por hora"],
    ["Caudal de diseño", Q_cfm, "CFM", "Equivalente en pies cúbicos por minuto"],
    ["Potencia teórica del ventilador", P_kW, "kW", "A 250 Pa y η=0.60"],
    ["Potencia teórica del ventilador", P_HP, "HP", "Unidades imperiales"],
    ["Potencia instalada recomendada", int(math.ceil(P_HP)), "HP", "Motor comercial con margen"],
    ["Área de impulsión del ventilador", A_vent, "m²", "Boca del ventilador"],
    ["Diámetro equivalente del ventilador", D_vent, "m", "Para referencia"],
    ["Radio del ventilador (CFD)", r_vent_mm, "mm", "Círculo de inyección"],
    ["Velocidad de impulsión", v_vent, "m/s", "Condición de entrada CFD"],
    ["Área neta total de rejillas de salida", A_exfil, "m²", "A v=3 m/s"],
    ["Número de rejillas de salida", int(n_rej), "unid.", "Distribución propuesta"],
    ["Área neta por rejilla de salida", A_rej, "m²", "Cada rejilla"],
    ["Altura de rejilla de salida", h_rej_mm, "mm", "Dimensiones para CFD"],
    ["Ancho de rejilla de salida", w_rej_mm, "mm", "Dimensiones para CFD"],
    ["Velocidad de exfiltración", v_sal, "m/s", "Condición de salida CFD"],
]

for i, row in enumerate(vista_rapida, start=4):
    for j, value in enumerate(row, start=1):
        cell = ws6.cell(row=i, column=j, value=value)
        cell.border = thin_border
        cell.alignment = Alignment(vertical='center', wrap_text=True)
        if j == 2:
            cell.fill = result_fill
            cell.font = result_font
            if isinstance(value, int):
                cell.number_format = '0'
            else:
                cell.number_format = '0.0000'

ws6['A22'] = "Nota:"
ws6['A22'].font = subtitle_font
ws6.merge_cells('A22:D22')
ws6['A23'] = "Estos valores son el resultado numérico precargado de las fórmulas de la hoja Cálculos. Si modifica las entradas, revise también las hojas Cálculos y Resultados."
ws6['A23'].alignment = Alignment(wrap_text=True)
ws6.merge_cells('A23:D25')

apply_border(ws6, 3, 1, 19, 4)
auto_width(ws6)

# ===================== CONFIGURACIÓN DE CÁLCULO =====================
wb.calculation.calcMode = "auto"
wb.calculation.fullCalcOnLoad = True

# ===================== GUARDAR =====================
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memoriadecalculo.xlsx")
wb.save(output_path)
print(f"Archivo guardado en: {output_path}")

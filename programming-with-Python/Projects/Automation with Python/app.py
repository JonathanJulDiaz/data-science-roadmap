import openpyxl as xl
from openpyxl.chart import BarChart, Reference

wb = xl.load_workbook('transactions.xlsx')

sheet = wb['Sheet1']

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row=row, column=3)
    corrected_price = cell.value * 0.9
    corrected_price_cell = sheet.cell(row=row, column=4)
    corrected_price_cell.value = corrected_price

corrected_price_cell = sheet.cell(row=1, column=4)
corrected_price_cell.value = 'Corrected Price'

values = Reference(sheet, min_col=4, min_row=2, max_col=4, max_row=sheet.max_row)

chart = BarChart()

chart.add_data(values, titles_from_data=True)
chart.title = 'Corrected Price'
chart.x_axis.title = 'Product'
chart.y_axis.title = 'Price'

sheet.add_chart(chart, 'E2')
 
wb.save('transactions2.xlsx')
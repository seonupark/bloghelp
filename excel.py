from openpyxl import load_workbook

wb = load_workbook(filename='function.xlsx')
ws = wb['Sheet1']

for j in range(2,6):
    for i in range(1,11):
        ws.cell(column=j,row=i, value=(ws.cell(column=j-1,row=i).value+3))

wb.save('function.xlsx')
wb.close()









# for row in ws.rows:
#     for cell in row:
#         print(cell.value)
#


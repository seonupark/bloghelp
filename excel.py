from openpyxl import load_workbook

aa = load_workbook(filename='practice.xlsx')
ws = aa['3단']

ws['B1']=4

for j in range(2,6):
    for i in range(1,11):
        ws.cell(column=j,row=i, value=(j+2)*i)

aa.save('practice.xlsx')
aa.close()

# for row in ws.rows:
#     for cell in row:
#         print(cell.value)
#


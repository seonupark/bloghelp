from openpyxl import load_workbook

aa = load_workbook(filename='practice.xlsx', read_only=True)
ws = aa['3단']

for row in ws.rows:
    for cell in row:
        print(cell.value)


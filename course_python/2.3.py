import xlrd
result = {}
rb = xlrd.open_workbook('C:\\Users\\ppirogov\\Desktop\\Паше\\salaries.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

for i in range(10, len(vals)):
    row = vals[i]
    name = row[1]
    grades = row[14:]
    if name is not result:
        result[name] = {}

    print (row)

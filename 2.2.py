import xlrd
from statistics import median , mean

c = []
d = []
wb = xlrd.open_workbook('C:\\Users\\ppirogov\\Desktop\\Паше\\salaries.xlsx')

sheet = wb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#print (wb.sheet_by_index(0).row_values(0)[0])
col_number = sheet.ncols
max = 0
number = 0
max2 = 0
number2 = 0
a = 1
b = 1
while a < 9:
    c.append(median(sheet.row_values(a)[1:]))
    if max < median(sheet.row_values(a)[1:]):
        max = median(sheet.row_values(a)[1:])
        number = a
    a+=1
a = 1
b = 1
print (sheet.row_values(number)[0])
while a < 9:
    b = 1
    max2 = 0
    number2 = 0
    while b < 8:
        if max2 < sheet.row_values(a)[b]:
            max2 = sheet.row_values(a)[b]
            number2 = b
        b+=1
        #print (max2, end = ' ')
    #print ()
    print (sheet.row_values(a)[0], end = ' ')
    print (sheet.row_values(0)[number2])
    a+=1

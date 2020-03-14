import xlrd
from statistics import median
c = []
d=[0,0,0,0,0,0,0]
wb = xlrd.open_workbook('C:\\Users\\ppirogov\\Desktop\\Паше\\salaries.xlsx')
sheet = wb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
max, number,max2,number2 = 0,0,0,0
a,b = 1,1
while a < 9:
    c.append(median(sheet.row_values(a)[1:]))
    if max < median(sheet.row_values(a)[1:]):
        max = median(sheet.row_values(a)[1:])
        number = a
    a+=1
a = 1
b = 1
print (sheet.row_values(number)[0], end = ' ')
#print (vals)
while a < 9:
    b = 1
    while b < 8:
        d[b-1]+=vals[a][b]
        b+=1
    a+=1
i=0
p=0
max3 = 0
while i < 7:
    if d[i] > max3:
        max3=d[i]
        p = i
    i+=1
print (sheet.row_values(0)[p+1])
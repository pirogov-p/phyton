import xlrd
from statistics import median

wb = xlrd.open_workbook('C:\\Users\\ppirogov\\Desktop\\Паше\\salaries.xlsx')

sheet = wb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#print (wb.sheet_by_index(0).row_values(0)[0])
max = 0
a = 1
for a  in vals:
    print (median(a[1:]))
   '''if int(median(a[1:]))> max:
        max=median(a[1:])
    a+=1'''
print (max)
import xlrd

wb = xlrd.open_workbook('C:\\Users\\ppirogov\\Desktop\\Паше\\tab.xlsx')

sheet = wb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#print (wb.sheet_by_index(0).row_values(0)[0])
'''for a in vals:
    print (a)'''
a = print(statistics.median(data1))
print (a)
import xlrd
a = dict()
b = []
#d = [0,0,0,0]
k1,k2,k3,k4 =0,0,0,0
rb = xlrd.open_workbook('C:\\Users\\ppirogov\\Desktop\\Паше\\trekking.xlsx')
sheet = rb.sheet_by_index(0)
sheet2 = rb.sheet_by_index(1)
vals2 =[sheet2.row_values(rownum) for rownum in range(sheet2.nrows)]
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
for i in range(1, len(vals)):
    a[vals[i][0]]=vals[i][1:]
#print (a)
for q in a:
    if a[q][3] == '':
        a[q][3] = 0
    for q1 in range(len(vals2)):
        if q == vals2[q1][0]:
            k1 = k1 + a[q][0] * vals2[q1][1] / 100
            k2 = k2 + a[q][1] * vals2[q1][1] / 100
            k3 = k3 + a[q][2] * vals2[q1][1] / 100
            k4 = k4 + a[q][3] * vals2[q1][1] / 100
print (int(k1),int(k2),int(k3),int(k4))

import xlrd
a = dict()
day = 0
rb = xlrd.open_workbook('C:\\Users\\ppirogov\\Desktop\\Паше\\trekking.xlsx')
sheet = rb.sheet_by_index(0)
sheet2 = rb.sheet_by_index(1)
vals2 =[sheet2.row_values(rownum) for rownum in range(sheet2.nrows)]
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#замена пустых полей нулями
for i in range(1, len(vals)):
    for e in range(1, len(vals[i])):
        if vals[i][e] == '':
            vals[i][e] =0
    a[vals[i][0]] = vals[i][1:]
# кол - во дней - 9
for i in range(1, len(vals2)):
    if day < vals2[i][0]:
        day = vals2[i][0]
#перебор
for i in range(int(day)):
    #print (i)
    k1, k2, k3, k4 = 0, 0, 0, 0
    for e in range(1, len(vals2)):
        #print (e)
        if vals2[e][0]==i+1:
            for r in a:
                if r == vals2[e][1]:
                    #print(a[r][0], vals2[e][2])
                    k1 = k1 + a[r][0] * vals2[e][2] / 100
                    k2 = k2 + a[r][1] * vals2[e][2] / 100
                    k3 = k3 + a[r][2] * vals2[e][2] / 100
                    k4 = k4 + a[r][3] * vals2[e][2] / 100

    print(int(k1), int(k2), int(k3), int(k4))
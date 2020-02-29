import requests, zipfile, io, xlrd, xlwt
r = requests.get('https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
#z.extractall('C:\\Users\\ppirogov\\Desktop\\Паше\\stpik')
z.extractall('C:\\Users\\pirog\\Desktop\\python')
a = dict()
for name in z.namelist():
    aa = xlrd.open_workbook('C:\\Users\\pirog\\Desktop\\python\\' + name)
    sheet = aa.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    #print (vals[1][1], vals[1][3])
    a[vals[1][1]]=vals[1][3]
#for k in sorted(a.keys()):
#    print (k, int(a[k]))

'''x = open('C:\\Users\\ppirogov\\Desktop\\Паше\\text.txt', 'w', encoding='utf-8')
for k in sorted(a.keys()):
    x.write(k +' ' + str(int(a[k])) + '\n')
'''
#rc = xlrd.open_workbook('C:\\Users\\pirog\\Desktop\\python\\test.xlsx', formatting_info=True)
wb = xlwt.Workbook()
ws = wb.add_sheet('Test')
i = 1
for k in sorted(a.keys()):
    ws.write(i,1,k)
    ws.write(i, 2, a[k])
    i += 1
wb.save('C:\\Users\\pirog\\Desktop\\test.xls')


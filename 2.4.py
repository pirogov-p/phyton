import requests, zipfile, io, xlrd, xlwt
r = requests.get('https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall('C:\\Users\\ppirogov\\Desktop\\Паше\\stpik')
a = dict()
for name in z.namelist():
    rb = xlrd.open_workbook(name)
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    #print (vals[1][1], vals[1][3])
    a[vals[1][1]]=vals[1][3]
for k in sorted(a.keys()):
    print (k, int(a[k]))

x = open('C:\\Users\\ppirogov\\Desktop\\Паше\\text.txt', 'w', encoding='utf-8')
for k in sorted(a.keys()):
    x.write(k +' ' + str(int(a[k])) + '\n')



import xlrd
d = set()
a = []
rb = xlrd.open_workbook('C:\\Users\\ppirogov\\Desktop\\Паше\\trekking.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#print (vals)
for i in range(1, len(vals)):
    a.append(vals[i][:2])
s = dict(a)
d = sorted(s.items(), key=lambda item: (-item[1], item[0]))
for b in d:
    print (b[0])

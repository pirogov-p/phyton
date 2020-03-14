from urllib.request import urlopen
html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
ans = []
status = 0
for c in s:
    if c == '<':
        status = 1
    if c == '>':
        status =0
    elif status == 0:
        ans.append(c)
s = ''.join(ans)
print (s)
#print (s.count('C++'))

'''print ('c++ count = ', s.count('C++'))
print ('python count = ', s.count('Python'))
'''
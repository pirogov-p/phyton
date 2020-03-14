from urllib.request import urlopen
import collections
import re
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
ans = set()
status = 0
max = 0
p =[]
regex = '<code>(.*?)</code>'
l = sorted(re.findall(regex, s))
c = collections.Counter()
for word in l:
    c[word] += 1
for word in l:
    if c[word]>max:
        max = c[word]
for word in l:
    if c[word]==max:
        ans.add(word)
p = list(ans)
p.sort()
#print (p)
#print (c)
for a in p:
   print (a, end = ' ')
from urllib.request import urlopen
import re
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
ans = []
status = 0

#regex = '<code>(.*?)</code>'
#l = sorted(re.findall(regex, s))
print (s)
'''for a in l:
    print (a, end = ' ')'''
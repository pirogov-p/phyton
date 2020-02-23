from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
ans = []
status = 0
for c in s:
    ans.append(c)

    #regex = '<code>(.*?)</code>'
    #l = sorted(findall(regex, s))
#print (ans)
print (s)
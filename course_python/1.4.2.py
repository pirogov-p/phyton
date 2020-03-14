from bs4 import BeautifulSoup
import requests
page = requests.get("https://stepik.org/media/attachments/lesson/209723/4.html")
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table')
table_rows = table.find_all('tr')
a=[]
print (soup)
''''for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    a.append(row)
sum = 0
for b in a:
    for c in b:
        sum +=int(c)

print (sum)'''
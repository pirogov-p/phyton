from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import bs4
import collections
import re
page = requests.get("https://stepik.org/media/attachments/lesson/209719/2.html")
soup = BeautifulSoup(page.content, 'html.parser')
for a in soup.find_all('a', href=True):
    print (a['href'])
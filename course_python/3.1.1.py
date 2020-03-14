import xmltodict,requests


f=open(r'C:\\Users\\pirog\\Desktop\\map1.osm',"wb") #открываем файл для записи, в режиме wb
ufr = requests.get("https://stepik.org/media/attachments/lesson/245571/map1.osm") #делаем запрос
f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
f.close()

fin = open('C:\\Users\\pirog\\Desktop\\map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])
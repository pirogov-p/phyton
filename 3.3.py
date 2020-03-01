import xmltodict,requests
f=open(r'C:\\Users\\pirog\\Desktop\\map1.osm',"wb") #открываем файл для записи, в режиме wb
ufr = requests.get("https://stepik.org/media/attachments/lesson/245681/map2.osm") #делаем запрос
f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
f.close()
f = open('C:\\Users\\pirog\\Desktop\\map1.osm', 'r', encoding='utf8')
text = f.read()
f.close()
a = xmltodict.parse(text)
fuel = 0
b = set()
for node in a['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    fuel+=1
        elif isinstance(tags, dict):
            if (tags['@v']) == 'fuel':
                fuel += 1
print(fuel)

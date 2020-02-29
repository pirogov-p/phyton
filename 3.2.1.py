import xmltodict,requests


f=open(r'C:\\Users\\pirog\\Desktop\\map1.osm',"wb") #открываем файл для записи, в режиме wb
ufr = requests.get("https://stepik.org/media/attachments/lesson/245678/map1.osm") #делаем запрос
f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
f.close()

f = open('C:\\Users\\pirog\\Desktop\\map1.osm', 'r', encoding='utf8')
text = f.read()
f.close()
have = 0
dont_have = 0
a = xmltodict.parse(text)
for node in a['osm']['node']:
        if 'tag' in node:
            have+=1
        else :
            dont_have+=1
'''for ways in a['osm']['way']:
    if 'node' in ways:
        nodes = ways['node']
        if 'tag' in node:
            have += 1
        else:
            dont_have += 1
            '''
print (have, dont_have)
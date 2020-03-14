import xmltodict, requests

f=open(r'C:\\Users\\pirog\\Desktop\\map.osm',"r", encoding='utf-8')
text = f.read()
f.close()
shops = 0
a = xmltodict.parse(text)
for node in a['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if tag['@k'] == 'shop':
                    shops+=1
                #print (tag)
print (shops)
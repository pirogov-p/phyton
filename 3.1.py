import xmltodict
a = xmltodict.parse("""<?xml version="1.0" ?>
<person>
  <name>john</name>
  <age>20</age>
</person>""")

print (a['person'])
# {u'person': {u'age': u'20', u'name': u'john'}}
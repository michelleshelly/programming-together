#XML is more generic
#HTML is a special kind of XML
#so all HTML are XMLs but not all XMLs are HTMLs. HTML subset of XML

# add Z at the back or +3h for time etc

import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Chuck</name>
    <name>Sandy</name>
    <phone type ="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>
'''
tree = ET.fromstring(data)
nameValues = tree.findall('name')
for name in nameValues:
    print(name.text)

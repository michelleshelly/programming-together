import xml.etree.ElementTree as ET

xml_string = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
                <password>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

root_stuff = ET.fromstring(xml_string)
user_elements = root_stuff.findall('users/user')
print('user count:', len(user_elements))

for user in user_elements:
    print('name:', user.find('id').text)
    print('id:', user.find('id').text)
    print('attribute(x):', user.get('x'))


# ''' [] is a list 
# ''' () is a dictionary

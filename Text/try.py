import json

text = '''
{
    \"listA\": [123, \"treiwon\"]
}
'''

jObject = json.loads(text)

listA = jObject['listA']
for item in listA:
    print(item)
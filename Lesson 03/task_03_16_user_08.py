import json
ln = input()
jsData = json.loads(ln)
def ancester_count(clName):
    ancesters = set()
    ancesters.add(clName)
    for cl in jsData:
        if clName in cl['parents']:
            ancesters.update(ancester_count(cl['name']))
    return ancesters
for clName in sorted(jsData, key=lambda x: x['name']):
    print(clName['name'] + ' : ' + str(len(ancester_count(clName['name']))))

import json

def count_children(cls):
    res = [cls]
    for d in classes:
        if cls in d['parents']:
            res.extend(count_children(d['name']))
    return list(set(res))

classes = json.loads(input())

for cls in sorted([x['name'] for x in classes]):
    print(cls, len(count_children(cls)), sep=' : ')
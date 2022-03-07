import json

sample = json.loads(input())

parent_dict = {}
for item in sample:
    parent_dict[item["name"]] = item["parents"]

child_dict = {}


def addChild(item, child):
    if item not in child_dict:
        child_dict[item] = set()
        child_dict[item].add(item)
    child_dict[item].add(child)
    for parent in parent_dict[item]:
        addChild(parent, child)


for item in parent_dict:
    addChild(item, item)

for item in sorted(child_dict.items()):
    print('{} : {}'.format(item[0], len(item[1])))

import json
classes = json.loads(input())
classDict = {cls['name']:cls['parents'] for cls in classes}

def total_children(name, children):
    for key, parents in classDict.items():
        if name in parents:
            children.add(key)
            total_children(key, children)
    return children

for name in sorted(classDict.keys()):
    print(name, ':', len(total_children(name, set({name}))))
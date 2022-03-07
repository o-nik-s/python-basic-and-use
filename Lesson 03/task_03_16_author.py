import json

data = json.loads(input())
children = dict()

for cls in data:
    for par in cls["parents"]:
        if par not in children:
            children[par] = []
        children[par].append(cls["name"])

def dfs(v, used):
    size = 1
    used.add(v)
    if v not in children:
        return size

    for child in children[v]:
        if child not in used:
            size += dfs(child, used)

    return size

ans = []

for cls in data:
    ans.append((cls["name"], dfs(cls["name"], set())))

for i in sorted(ans):
    print(i[0], ":", i[1])
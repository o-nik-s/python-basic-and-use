import json

used = []
dict = {}
for node in json.loads(input()):
    for item in node["parents"]:
        dict[item] = (dict[item] if item in dict else []) + [node["name"]]
    if node["name"] not in dict:
        dict[node["name"]] = []
foo = lambda current : (0 if current in used or used.append(current) else 1 + sum([foo(i) for i in dict[current]]))
for i in sorted(dict):
    print(i, ":", foo(i))
    used = []
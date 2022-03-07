import json


def get_childs(parent):
    for cls in par_list:
        if parent in cls['parents']:
            fam_tree.add(cls['name'])
            get_childs(cls['name'])

js_string = input()
par_list = json.loads(js_string)

res_list = []
for cls in par_list:
    fam_tree = set()
    get_childs(cls['name'])
    res_list.append((cls['name'], len(fam_tree)+1))
for key, value in sorted(res_list):
    print(key, value, sep=' : ')
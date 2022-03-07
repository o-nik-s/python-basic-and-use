par_list = {}

def create_tree(child):
    fam_tree.update(par_list[child])
    for sparent in par_list[child]:
        create_tree(sparent)

for i in range(int(input())):
    substructure = input().split(':')
    if len(substructure) > 1:
        par_list[substructure[0].strip()] = substructure[1].split()
    else:
        par_list[substructure[0].strip()] = []
#print(par_list)

for i in range(int(input())):
    parent, child = input().split()
    fam_tree = set()
    create_tree(child)
    if parent == child or parent in fam_tree:
        print('Yes')
    else:
        print('No')

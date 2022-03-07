def foo_yn(cp, c):
    if cp == c: return 'Yes'
    if cp in set((foo_all_parent(c, all_parent = []))):
        return 'Yes'
    else:
        return 'No'

def foo_all_parent(c, all_parent = []):
    if cl_parent[c] != []:
        all_parent.extend(cl_parent[c])
        for i in cl_parent[c]:
            foo_all_parent(i, all_parent)
    return all_parent

cl_parent = {}
for i in range(int(input())):
    com = [j for j in input().split()]
    cl_parent[com[0]] = com[2:len(com)]

for i in range(int(input())):
    cp, c = input().split()
    print(foo_yn(cp,c))
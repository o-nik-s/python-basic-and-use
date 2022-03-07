def findInParents(parentList: None):
    if parentList is not None:
        if parent in parentList:
            return True
        else:
            findSt = False
            for parentChild in parentList:
                if parentChild in classDescrDict:
                    findSt += bool(findInParents(classDescrDict[parentChild]))
                    if findSt:
                        return True


n = int(input())
classDescrDict = dict()
for i in range(n):
    clDescrNow = input().strip()
    if ":" not in clDescrNow:
        classDescrDict[clDescrNow] = None
    else:
        child, parents = tuple(map(lambda x: x.strip(), clDescrNow.split(':')))
        classDescrDict[child] = parents.split()
# print(classDescrDict)
q = int(input())
for i in range(q):
    parent, child = input().split()
    if child not in classDescrDict:
        print("No")
    elif child == parent:
        print("Yes")
    else:
        res = bool(findInParents(classDescrDict[child]))
        print(res * "Yes" + (1 - res) * "No")

n = int(input())
classDefs = {}


def aggregateParents(className, parents):
    parents.extend(classDefs[className])

    for parent in classDefs[className]:
        aggregateParents(parent, parents)


for _ in range(n):
    classDef = input().split(" : ")
    if len(classDef) > 1:
        parents = classDef[1].split()
        classDefs[classDef[0]] = parents
    else:
        classDefs[classDef[0]] = []

q = int(input())
for _ in range(q):
    test = input()
    parentName = test.split()[0]
    className = test.split()[1]
    parents = []
    aggregateParents(className, parents)
    if parentName in parents or parentName == className:
        print("Yes")
    else:
        print("No")

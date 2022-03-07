

n = int(input())
currentNamespace = list()
namespace = currentNamespace
currentNamespace.append("global")
listSpace = list()
for i in range(n):
    request = input().split(" ")
    print(request)
    if request[0] == "create":
        if request[2] == currentNamespace[0]:
            currentNamespace.append(request[1])
            newNamespace = [request[1]]
            currentNamespace.append(newNamespace)
            listSpace.append(newNamespace)
            oldNamespace = currentNamespace
            currentNamespace = newNamespace
        else:
            a = 0
            print("Variant create 2")
            print("listSpace", listSpace)
        print("create")
    elif request[0] == "add":
        if request[1] == currentNamespace[0]:
            currentNamespace.append(request[2])
        else:
            a = 0
            print("Variant add 2")
            # namespace.append(request[2])
            print("listSpace", listSpace)
        print("add")
    elif request[0] == "get":
        print("get")
    print("namespace", namespace)
print('result namespace', namespace)

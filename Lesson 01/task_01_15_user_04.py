classes = {}

def is_parent(A, B):
    if (A == B):
        return 'Yes'
    elif A in classes[B]:
        return 'Yes'
    else:
        for i in classes[B]:
            if is_parent(A, i) == 'Yes':
                return 'Yes'
    return 'No'

for i in range(int(input())):
    line = input().split()
    _class = line[0]
    classes[_class] = []
    if len(line) > 1:
        _parents = line[2:]
        classes[_class].extend(_parents)

for i in range(int(input())):
    A, B = input().split()
    print(is_parent(A, B))

parents = {}
for _ in range(int(input())):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def is_parent(child, parent):
    if child == parent: return True
    for p in parents[child]:
        if is_parent(p, parent ): return True
    return False

exceptions = []
for _ in range(int(input())):
    a = input().strip()
    for i in exceptions:
        if is_parent(a,i):
            print(a)
            break
    exceptions.append(a)

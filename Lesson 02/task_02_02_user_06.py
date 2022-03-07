ex = dict()
for _ in range(int(input())):
    line = input().split()
    ex[line[0]] = line[2:]

def search_and_delete(s):
    global ex
    found = 0
    for k in ex:
        if ex[k] and s in ex[k]:
            ex[k] = None
            found += 1
            search_and_delete(k)
    if ex[s] is not None:
        found += 1
        ex[s] = None
    return found


for _ in range(int(input())):
    line = input()
    if not search_and_delete(line):
        print(line)

def test(parent, child):
    if parent == child or parent in base[child]:
        return True
    for i in base[child]:
        if test(parent, i) == True:
            return True
    return False

base = dict()
commands = set()
for com in [input().split() for i in range(int(input()))]:
    base[com[0]] = com[2:len(com)]
for i in range(int(input())):
    exmp = input()
    for com in commands:
        if test(com, exmp):
            print(exmp)
            break
    commands.add(exmp)

def test(parent, child):
    if parent == child or parent in base[child]:
        return 'Yes'
    for i in base[child]:
        if test(parent, i) == 'Yes':
            return 'Yes'
    return 'No'

base = {}
for com in [input().split(' ') for i in range(int(input()))]:
    base[com[0]] = com[2:len(com)]
for com in [input().split(' ') for i in range(int(input()))]:
    print (test(com[0], com[1]))
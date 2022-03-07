n = int(input())
dicti = {}
for i in range(n):
    Name1, *Names = input().split(':')
    if Names == []:
        k = Names
    else:
        k = list(Names[0].split())
    dicti[Name1.strip()] = k
    for a in k:
        if a not in dicti.keys():
            dicti[a] = []
for key, value in dicti.items():
    for j in value:
        if j in dicti.keys():
            dicti[key] += dicti[j]

for i in range(int(input())):
    A, B = input().split()
    if A == B:
        print('Yes')
    else:
        if A in dicti[B]:
            print('Yes')
        else:
            print('No')
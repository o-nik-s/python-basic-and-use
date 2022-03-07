d = dict()
for i in range(int(input())):
    a = input().split()
    d[a[0]] = a[2:]

for k, v in d.items():
    for k2, v2 in d.items():
        if k in v2:
            v2 += v

for i in range(int(input())):
    a = input().split()
    b = False
    for k, v in d.items():
        if a[1] == k and (a[0] in v or a[0] == k):
            b = True
    if b:
        print('Yes')
    else:
        print('No')
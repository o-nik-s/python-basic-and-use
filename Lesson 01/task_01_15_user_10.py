def foo(a, b):
    tmp = a == b
    for i in d[b]:
        tmp |= foo(a, i)
    return tmp

d = {}

for i in range(int(input())):
    s = input().split()
    d[s[0]] = ([] if len(s) == 1 else s[2:])

for i in range(int(input())):
    a, b = map(str, input().split())
    print("Yes" if foo(a, b) else "No")
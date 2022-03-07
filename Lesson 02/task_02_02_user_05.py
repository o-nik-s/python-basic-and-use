def foo(exep):
    if d[exep] == -1:
        print(exep)
    else:
        k = d[exep]
        d[exep] = -1
        for i in k:
            if d[i] != -1:
                foo(i)
                d[i] = -1


d = {}
for i in range(int(input())):
    s = input().split()
    if len(s) != 1:
        for i in s[2:]:
            d[i] = [s[0]] if i not in d else d[i] + [s[0]]
    if s[0] not in d:
        d[s[0]] = []

for i in range(int(input())):
    foo(input())
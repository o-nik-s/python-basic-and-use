s = input()
a = input()
b = input()

if a not in s:
    print(0)
elif a in b:
    print("Impossible")
else:
    ans = 0
    while a in s:
        s = s.replace(a, b)
        ans += 1

    print(ans)
s, a, b = input(), input(), input()
counter = 0
if (a in b) and (a in s):
    print('Impossible')
else:
    while a in s:
        s = s.replace(a, b)
        counter += 1
    print(counter)
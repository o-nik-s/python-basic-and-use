s, a, b = [input() for i in range(3)]
counter = 0
if (a == b and a in s) or (a in b and a in s):
    counter = 'Impossible'
else:
    while a in s:
        s = s.replace(a, b)
        counter += 1
print(counter) 
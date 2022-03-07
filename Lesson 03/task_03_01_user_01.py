n, (s, a, b) = 0, (input().strip() for _ in range(3))
while a in s:
    n += 1
    s = b.join(s.split(a))
    if a in b and a in s:
        break
print("Impossible" if a in b and a in s else n)
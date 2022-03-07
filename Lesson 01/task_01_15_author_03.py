# Пример решения задачи с использованием алгоритма поиска в глубину

# https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_%D0%B3%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D1%83
# https://en.wikipedia.org/wiki/Depth-first_search

# https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_%D0%B3%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D1%83

# Решение от Константина Зайцева, автора курса

n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]

def dfs(v, used):
    used.add(v)
    for i in parents[v]:
        if i not in used:
            dfs(i, used)

q = int(input())
for _ in range(q):
    a, b = input().split()
    used = set()
    dfs(b, used)
    print("Yes" if a in used else "No")

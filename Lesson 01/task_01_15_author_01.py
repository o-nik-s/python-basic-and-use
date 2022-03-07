# Пример правильного решения:
# Xраним "кто чей родитель" в качестве словаря (обратите в инициализации этого словаря на использование тернарного оператора внутри цикла for).
# Реализуем функцию is_parent, проверяющую, что второй аргумент является предком первого.
# Последовательно запустим нашу функцию на всех парах имён классов из нашего ввода.

# Решение от Константина Зайцева, автора курса

n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]
print(parents)

def is_parent(child, parent):
    if child == parent:
        return True

    for p in parents[child]:
        if is_parent(p, parent):
            return True

    return False

q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")

'''IMHO самое понятное из трёх выложенных решение, но с тем же багом :)
parents[child]
вместо
parents.get(child, [])'''

'''Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa﻿'''

s = input()
t = input()
# print(s.find.__doc__)
i, count = 0, 0
while i <= len(s):
    # print(s[i:])
    f = s[i:].find(t)
    if f >= 0:
        count += 1
        i += f + 1
    else:
        i = len(s) + 1
print(count)


'''
author
s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        ans += 1

print(ans)
'''

'''
s = input()
t = input()

print(sum(1 for i in range(len(s)) if s.startswith(t, i)))
'''

'''
s, t = input(), input()
print(sum(s[i : i + len(t)] == t for i in range(len(s) - len(t) + 1)))
'''

'''
def cross_count(s, t):
    try:
        return 1 + cross_count(s[s.index(t)+1:], t)
    except (ValueError, IndexError):
        return 0

print(cross_count(input(), input()))
'''

'''
a, b = (input().strip() for i in range(2))
count = 0
for i in range(len(a) - len(b) + 1):
    if b == a[i:i + len(b)]:
        count += 1
print(count)
'''


'''
a, b = (input().strip() for i in range(2))
count = 0
for i in range(len(a) - len(b) + 1):
    if b == a[i:i + len(b)]:
        count += 1
print(count)
'''

'''
x, y = str(input()), str(input())
count = 0
while y in x:
    x = x[x.index(y)+1:]
    count += 1
print(count)
'''
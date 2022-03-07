'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
'''

import sys
import re

pattern = "cat"
for line in sys.stdin:
    line = line.rstrip()
    if re.findall(pattern, line).count(pattern) >= 2:
        print(line)


'''
author
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"cat.*cat", line):
        print(line)
'''

'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r"cat", line)) > 1:
        print(line)
'''

'''
import sys, re

text = [line.strip() for line in sys.stdin if re.search(r"cat.*cat", line)]
print("\n".join(text))
'''

'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r'cat', line).count('cat') > 1:
        print(line)
'''

'''
from sys import stdin
import re

pattern = r'cat'

for line in stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) >= 2:
        print(line)
'''

'''
import sys
import re

pattern = r'.*?cat.*?cat'
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern,line) != None:
        print(line)
'''

'''
s, t = input(), input()
print(len(list(filter(lambda x: x == t, (s[i : i + len(t)] for i in range(len(s) - len(t) + 1))))))
'''

'''
def findall(a, b, count=0):
    for i in range(len(a)): count += 1 if a.startswith(b, i) else 0
    return count
print(findall(input(), input()))
'''

'''
'''
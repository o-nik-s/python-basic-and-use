# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    # print(re.findall(pattern, line))
    print(re.sub("human", "computer", line))  # Заменим все вхождения нашего шаблона внутри нашей строки на "computer"


'''
from re import sub
from sys import stdin
print(sub('human', 'computer',stdin.read()))
'''
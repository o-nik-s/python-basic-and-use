# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.

import sys
import re

pattern = r"(\w)\1+"
for line in sys.stdin:
    # print(re.findall(pattern, line))
    print(re.sub(pattern, r"\1", line.rstrip()))


'''
import re
import sys

print(*[re.sub(r"(\w)(\1)+", r"\1", line) for line in sys.stdin], sep='')
'''
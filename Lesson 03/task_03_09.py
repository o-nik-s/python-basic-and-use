'''
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

Примечание:
Обратите внимание на параметр count у функции sub﻿.
'''

import sys
import re

pattern = r"\b[a|A]+\b"
for line in sys.stdin:
    print(re.sub(pattern, "argh", line.rstrip(), count=1))  # Заменим все вхождения нашего шаблона внутри нашей строки на "argh"

'''
import re
import sys

for line in sys.stdin:
    line = line.strip()
    line = re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE)
    print(line)
'''

'''
import sys
import re
[print(re.sub(r'\b[aA]+\b', 'argh', line.rstrip(), 1)) for line in sys.stdin]
'''

'''
import re, sys
exp = re.compile(r"\b[aA]+\b")
print(*map(lambda line: exp.sub('argh', line, 1), sys.stdin), sep='')
'''
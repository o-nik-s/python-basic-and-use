# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
import sys
import re

pattern = r"z.{3}z"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)


'''
author
import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"z...z", line):
        print(line)
'''

'''
import sys, re
exp = re.compile("z...z")
print(*filter(lambda line: exp.search(line), sys.stdin), sep='')
'''

'''
import sys
import re

for line in sys.stdin:
	if re.search(r'z...z', line):
		print(line, end="")
'''

'''
import sys
import re

print('\n'.join([line.rstrip() for line in sys.stdin if re.findall(r'z.{3}z', line)]))
'''

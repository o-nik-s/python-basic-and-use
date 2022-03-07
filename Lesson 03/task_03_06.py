'''
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
'''

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\\", line):
        print(line)


'''
import sys
import re

print('\n'.join([line.rstrip() for line in sys.stdin if re.findall(r'\\', line)]))
'''

'''
import re
import sys

print('\n'.join([line.rstrip() for line in sys.stdin if re.search(r'\\', line.rstrip())]))
'''

'''
import sys
import re

print('\n'.join([line.rstrip() for line in sys.stdin if re.search('.*\\\\.*',line)]))
'''
'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Примечание:
Для работы со словами используйте группы символов \b и \B.
Описание этих групп вы можете найти в документации.
'''

# \b
# Граница слова. Слово определяется как последовательность символов чисел и/или букв, так что границы слова
# представляют пробелы или любые символы, не относящиеся к перечисленным.
'''>>> p = re.compile(r'\bclass\b')
>>> print p.search('no class at all')
<_sre.SRE_Match object at 0x...>
>>> print p.search('the declassified algorithm')
None
>>> print p.search('one subclass is')
None'''
# \B
# Противоположное предыдущему сочетание, соответствующая текущей позиции не на границе слова.
# https://habrahabr.ru/post/115436/


import sys
import re

pattern = r"\bcat\b"
for line in sys.stdin:
    line = line.rstrip()
    if re.findall(pattern, line):
        print(line)


'''
author
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\bcat\b", line):
        print(line)
'''

'''
import sys
import re

print('\n'.join([line.rstrip() for line in sys.stdin if re.search(r'\bcat\b', line)]))
'''

'''
import re
import sys

print(*(line.rstrip() for line in sys.stdin if re.search(r'\bcat\b', line.rstrip())), sep='\n')
'''
'''
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
'''

import sys
import re

pattern = r"\b(\w+)\1\b" # + - один или более раз
for line in sys.stdin:
    line = line.rstrip()
    # print(re.findall(pattern, line))
    if re.findall(pattern, line):
        print(line)


'''
import sys
import re

print('\n'.join([line.rstrip() for line in sys.stdin if re.search(r'\b(\w+)\1\b',line)]))
'''


'''
pattern = r"(\w+)-\1" # \1 - найти такую же группу, какую Ты уже собрал ранее
string = "test-test" # Сможем найти
+ - повторить 1 или более раз
'''

'''А почему (группа){2} не работает как (группа)\1 ? 
(группа){2} это 2 раза описание группы, а это (группа)\1  группа и её копия
'''
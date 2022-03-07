'''
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w﻿.
'''

import sys
import re

pattern = r"\b(\w)(\w)"
for line in sys.stdin:
    # print(re.findall(pattern, line))
    print(re.sub(pattern, r"\2\1", line.rstrip()))



'''----------------------------------------------------------------------------------------------------------------'''

'''
В помощь ещё размышляющим:
начало слова: \b
любая буква-цифра: \w
группировка: ()
шаблон замены, ссылающийся на группировки: r"\2\1"
'''

# https://docs.python.org/3.5/library/re.html

'''
6.2.5.5. Text Munging
sub() replaces every occurrence of a pattern with a string or the result of a function. This example demonstrates 
using sub() with a function to “munge” text, or randomize the order of all the characters in each word of a sentence 
except for the first and last characters:
>>>
>>> def repl(m):
...     inner_word = list(m.group(2))
...     random.shuffle(inner_word)
...     return m.group(1) + "".join(inner_word) + m.group(3)
>>> text = "Professor Abdolmalek, please report your absences promptly."
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
>>> re.sub(r"(\w)(\w+)(\w)", repl, text)
'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'
'''

'''
Группы - это  то что заключено в скобки. Номер группы отсчитывают по количеству открывающих скобок до содержимого. 
Вот тут тонкий момент номера групп начинается с "1", а не с "0".
'''

'''
﻿Как понял я, к примеру, : r'(ab)(bc)' в таком виде и порядке расположения в скобках  (ab) - первая группа или \1, 
(bc) - вторая группа или \2. Т.е. '(ab)' == '\1' и '(bc)' == '\2'. Само решение не показываю - оно, как оказалось в финале, 
проще пареной репы. Для второго задания подсказка, если в выражении  r"(ab)\1" - то это фактически r"abab" что еще нужно 
добавить для решения следующего задания - это не сложно, главное понять почему именно ЭТО туда поставить.  :) 
'''

'''
Делается в одну строку, при помощи re.sub. В строке замены можно использовать переменные (номера) групп. Но чтобы 
обратные слеши работали нормально, их нужно экранировать, либо сделать строку замены "сырой".
'''

'''
Приблизительно так: В re.sub() в шаблоне ловим одну и вторую нужную группу с помощью скобок -(..), 
в подстановке в сыром выражении меняем местами группы с помощью \1 \2
'''

'''
import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r".............", r"......", line))
'''
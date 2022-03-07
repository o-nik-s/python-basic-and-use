# 3.3 Регулярные выражения /РВ/ в Python

# Мы сначала с помощью регулярных выражений описываем шаблом, а потом проверяем, подходит ли наша строка под наш шаблон.

# Обычные строки
# Используем обратный слэш, чтобы заэкранировать символ.
x = "hello\nworld"
print(x)

x = "hello\"world"
print(x)

# Обычные и "сырые" строки
# Однако в регулярных выражениях обратный слэш нужен как обратный слэш.
# ЧТобы указать интерпретатору, что символы надо использовать в том виде, в котором они указаны, можем указать:
x = r"hello\nworld"  # raw  - "Сырые строки"
print(x)

import re # От regular expression - регулярные выражения - модуль стандартной библиотеки Пайтон
print(re.match)  # Берет шаблон и строку, и проверяет, подходит ли строка под данный шаблон
print(re.search)  # Берет строку и находит первую подстроку, которая подходит под наш шаблон
print(re.findall)  # Находит все подстроки строки, которые подходят под шаблон
print(re.sub)  # Заменяет все вхождения подстрок, которые подходят под наш шаблон, чем-нибудь другим

re.split(pattern, string, [maxsplit=0]) # Этот метод разделяет строку по заданному шаблону.
re.compile(pattern, repl, string) # Мы можем собрать регулярное выражение в отдельный объект, 
# который может быть использован для поиска. Это также избавляет от переписывания одного и того же выражения.

# Регулярные выражения и будут выписывать шаблон

pattern = r"abc" # Шаблон
string = "abcd" # Строка, которыую мы хотим проверить, подходит ли она под шаблон
match_object = re.match(pattern, string)
print(match_object)
# Вернулся объект Match object
# У него есть атрибут match, который содержит вхождения шаблона "abc" внутрь нашей строки "abc"
# И у него есть атрибут span, который позволяет понять, с какой по какую позицию в нашей строке string находится
# наше вхождение шаблона в строку

# Функция match берет строку и берет с самого начала нашей строки до тех пор, пока какой-нибуль префикс строки не
# подошел под данное регулярное выражение. А как только оно подходит, она его возвращает в качестве match.

pattern = r"abc"
string = "aсcd"
match_object = re.match(pattern, string)
print(match_object)
# Если строка не подходит под шаблон, то функция match возвращаем None

string = "babc"
match_object = re.match(pattern, string)
print(match_object)
# Не подходит под шаблон, потому что строка начинается с b, а шаблорн начинается с a

# Однако если мы хотим найти вхождения нашего шаблона в строку, мы можем использовать search
match_object = re.search(pattern, string)
print(match_object)

# Те числа, которые вернулись внутри span, - это те же самые числа, которые мы бы использовали в слайсинге


# Метасимволы

# [] - можем указать множество походящих символов
pattern = r"a[abc]c" # В качестве второго символа может подойти a, b или c
string = "abc" # "aac", "acc" - все три True
match_object = re.match(pattern, string)
print(match_object)

# Метасимволы позволяют расширять то множество строк, которое подходит под наш шаблон

string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string) # Хотим найти все вхождения шаблона внутрь нашей большой строки
print(all_inclusions)

# Предположим, что acc и aac - опечатки, и нам нужно использовать строку abc
fixed_typos = re.sub(pattern, "abc", string) # Заменим все вхождения нашего шаблона внутри нашей строки на "abc"
print(fixed_typos) # Исправили все опечатки
# Функция "sub" "на месте" заменяет все подстроки на что-то другое
print()


pattern = r" english\?"
string = "Do you speak english?"
match = re.search(pattern, string)
print(match)
# Вопросительный знак является метасимволом в регулярном выражении, поэтому если мы просто хотим найти символ "?",
# мы должны его экранировать с помощью обратного слэша.
# И так будет с каждым метасимволом. В том числе мы должны экранировать и обратный слэш.
print()

# [] -- можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы

pattern = r"a[a-d]c" # Можно указать диапазон, в котором подходят символы
string = "abc, acc, aac, adc"
all_inclusions = re.findall(pattern, string) # Хотим найти все вхождения шаблона внутрь нашей большой строки
print(all_inclusions)
fixed_typos = re.sub(pattern, "abc", string) # Заменим все вхождения нашего шаблона внутри нашей строки на "abc"
print(fixed_typos) # Исправили все опечатки


pattern = r"a[a-zA-Z]c" # Можно указать все буквы латинского алфавита
string = "abc, acc, aac, adc, aBc, azc"
all_inclusions = re.findall(pattern, string) # Хотим найти все вхождения шаблона внутрь нашей большой строки
print(all_inclusions)
fixed_typos = re.sub(pattern, "abc", string) # Заменим все вхождения нашего шаблона внутри нашей строки на "abc"
print(fixed_typos) # Исправили все опечатки

# Можно использовать символ "^" /"циркумфлекс"/ для того чтобы описать те множества символов, которые не подходят
# "В двух словах, циркумфлекс - это диакритический знак, ﻿а то, что у нас на клавиатурах, - самостоятельный символ, называемый карет."
pattern = r"a[^a-zA-Z]c" # Можно указать все буквы латинского алфавита
string = "abc, a.c, acc, a-c, aac, adc, aBc, azc"
all_inclusions = re.findall(pattern, string) # Хотим найти все вхождения шаблона внутрь нашей большой строки
print(all_inclusions) # В результате найдем только те элементы, которые с небуквенными символами
fixed_typos = re.sub(pattern, "abc", string) # Заменим все вхождения нашего шаблона внутри нашей строки на "abc"
print(fixed_typos)


# Так как некоторые группы символов используются в регулярных выражениях достаточно часто,
# для них уже существует короткая запись
# [] -- можно указать множество подходящих символов
# , ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# \d ~ [0-9] -- цифры
# \D ~ [^0-9] -- что угодно кроме цифр
# \s ~ [ \t\n\r\f\v] -- пробельные символы (\r - перенос каретки, \f - перенос страницы, \v - вертикальная табуляция)
# \S ~ [^ \t\n\r\f\v] -- что угодно кроме пробельных симоволов
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-Z0-9_] -- что угодно кроме \w

pattern = r"a\wc"
string = "abc, a.c, acc, a-c, aac, adc, aBc, azc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
fixed_typos = re.sub(pattern, "abc", string) # Заменим все вхождения нашего шаблона внутри нашей строки на "abc"
print(fixed_typos)

pattern = r"a[\w.]c" # Предыдущее включая точку
string = "abc, a.c, acc, a-c, aac, adc, aBc, azc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
fixed_typos = re.sub(pattern, "abc", string) # Заменим все вхождения нашего шаблона внутри нашей строки на "abc"
print(fixed_typos)

# Метасимвол . - любой символ кроме переноса строки будет подходить под точку
pattern = r"a.c" # Предыдущее включая точку
string = "abc, a.c, acc, a-c, aac, adc, aBc, azc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
fixed_typos = re.sub(pattern, "abc", string) # Заменим все вхождения нашего шаблона внутри нашей строки на "abc"
print(fixed_typos)
print()


# Так же мы можем указывать в регулярных выражениях, что нас интересует некоторое число повторов символов или группы символов.

pattern = r"ab*a" # Нас интересует любое число символов b, включая 0
string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

# Если же нас интересует только положительное число включений, мы можем использовать символ "+"
pattern = r"ab+a" # Нас интересует число символов b > 0
string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r"ab?a" # Нас интересует 0 или 1 вхождение символа b
string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

# Если нас интересует конкретное число вхождений или от какого-то до какого-то количества,
# мы можем использовать метасимвол {}
pattern = r"ab{3}a" # Внутри фигурных скобок - то количество, которое нас интересует, например, 3
string = "aa, aba, abba, abbba, abbbbba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r"ab{2,4}a" # Найдем от 2 до 4 вхождений
string = "aa, aba, abba, abbba, abbbbba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
print()


# В фигурных скобках после запятой можно ничего не ставить и искать больше или равно символов чем n?
# {3,}
# И наоборот тоже работает { , 3} - меньше или равно 3 символов

# По умолчанию метасимволы повторов * или + являюются "жадными", т.е. они пытаются вовлечь в себя как можно больше символов,
# при том, чтобы наше все регулярное выражение удовлетворилось целиком

pattern = r"a[ab]+a"
string = "abaaba"
match_object = re.match(pattern, string)
print(match_object)
all_inclusions = re.findall(pattern, string)
print(all_inclusions)


pattern = r"a[ab]+b"
string = "abaaba"
match_object = re.match(pattern, string)
print(match_object)
all_inclusions = re.findall(pattern, string)
print(all_inclusions)


# Однако можно искать не жадным образом, а наоборот, найти наименьшее число вхождений,
# которое бы удовлетворило наше регулярное выражение
# Для этого можно использовать ? после метасимвола
pattern = r"a[ab]+?a"
string = "abaaba"
match_object = re.match(pattern, string)
print(match_object) # Является строка наименьшей длины
all_inclusions = re.findall(pattern, string)
print(all_inclusions) # Найдем оба вхождени строки aba, aba



# Так же с помощью регулярных выражений мы можем группировать символы
# Это нужно, например, для того, чтобы мы могли использовать метасимвол повтора для какой-либо группы символов,
# а не для одиночного символа
# Так же мы можем использовать группировку для того, чтобы переиспользовать группу целиком
# Для группировки необходимо использовать метасимов (), в который мы заключаем группу символов
pattern = r"(test)*" # Хотим повторить
string = "testtest"
match = re.match(pattern, string)
print(match)

# Метасимвол "или"
pattern = r"(test|text)*" # Или данная группа символов или данная группа символов
string = "testtext" # Подходит
match = re.match(pattern, string)
print(match)

# Метасимвол "или" обладает наименьшим приоритетом в регулярных выражениях
pattern = r"abc|(test|text)*" # Или данная группа символов или данная группа символов
string = "abc" # Подходит
match = re.match(pattern, string)
print(match)

# Однако самое замечательное в группах то, что мы запоминаем, какие символы попали в конкретную группу
pattern = r"((abc)|(test|text)*)"  # Или данная группа символов или данная группа символов
string = "abc"
match = re.match(pattern, string)
print(match)
print(match.groups())  # Вывели на экран значение трех групп. И каждой группе будет соответствовать пара открывающей и закрывающей скобки
# Первая группе соответствует всему нашему РГ /потому что под первую пару скобок попало все наше РГ/
# Второй группе будет соовтетствовать маленькая группа, содержащая строку abc
# А третьей группе, в которую ничего не попало, соответствует группа, содержащая test|text

string = "testtext"
match = re.match(pattern, string)
print(match)
print(match.groups())
# Когда используем группы и метасимвол повторения, то мы запомним последнее вхождение, которое у нас было /text/
string = "testtexttest" # В данном случае - test
match = re.match(pattern, string)
print(match)
print(match.groups())

pattern = r"Hello (abc|test)"
string = "Hello abc"
match = re.match(pattern, string)
print(match)
print(match.group()) # По умолчанию аргумент равен 0 - хотим найти просто совпадение нашему шаблону
print(match.group(0))
print(match.group(1))

# Однако самое замечательное в группировке то, что мы можем использовать уже найденную группу внутри регулярного выражения
pattern = r"(\w+)-\1" # \1 - найти такую же группу, какую Ты уже собрал ранее
string = "test-test" # Сможем найти
match = re.match(pattern, string)
print(match)
string = "test-text" # Не найдем, так как text не совпадает с первой группой, которую мы нашли
match = re.match(pattern, string)
print(match)
# Номер после обратно слэша соответствует номеру группы

pattern = r"(\w+)-\1" # \1 - найти такую же группу, какую Ты уже собрал ранее
string = "test-test chow-chow"
# Мы можем переиспользовать эту группу, в том числе внутри sub
duplicates = re.sub(pattern, r"\1", string) # При этом важно использовать "сырые строки" в строке, которую мы указываем на замену
print(match)
# И тогда вместо изначальной строки оставили лишь одно слово из пары совпадающих слов
# Если findall ранее возвращала ту подстроку, которая подходила под шаблон, то теперь findall будет возвращать кортеж групп
duplicates = re.findall(pattern, string) # При этом важно использовать "сырые строки" в строке, которую мы указываем на замену
print(duplicates)

# Вместо одной группы используем две. Например, хотим поймать все вхождение регулярного выражения целиком
pattern = r"((\w+)-\2)" # 1 заменили на 2 т.к. данная открывающая скобка теперь стала второй /добавили скобки/
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)
print(duplicates) # Теперь мы поймали кортежи по 2 группы: первой группой является все регулярное выражение, а второй группой -
# первое слово, которое через дефис является удвоенным

# Таким образом, с помощью группировок мы можем повторять какие-то группы символов и переиспользовать уже найденные группы
# прямо внутри нашего найденного регулярного выражения


# Так же внутрь каждой из этих функций мы можем передать флажок для того, чтобы сказать, как вести себя с данным регулярным
# выражением

# Например, мы можем сказать, что нас не очень интересует, являются ли буквы заглавными или строчными
# Для этого используется флажок IGNORECASE
x = re.match(r"text", "TEXT", re.IGNORECASE)

# Хотим вывести дополнительную информацию о РГ. Для этого можно использовать фалг DEBUG.
x = re.match(r"(te)*xt", "TEXT", re.IGNORECASE | re.DEBUG) # Чтобы добавить один флаг к другому, можем использовать или
# Мы увидели, что  наша группа (te), отдельно выраженная, выделилась в SUBPATTERN c номером 1 /как раз тот номер, который
# мы указываем после обратного слэша для группы/. Мы увидели, что т.к. мы указали "*", то мы пытаемся найти от 0 до
# очень большого числа MAXREPEAT. И так же каждому буквенному символу в нашем регулярном выражении соответствует его
# код в таблице Юникода (LITERAL 116, LITERAL 101).

# Если поставить ? после *,
x = re.match(r"(te)*?xt", "TEXT", re.IGNORECASE | re.DEBUG)
# то теперь мы ищем не "жадно", мы ищем минимальное вхождение MIN_REPEAT, которому бы удовлетворило наше РВ.


# Таким образом, РВ являются отличным инструментом для поиска нужной информации

# https://regex101.com/#python
# http://www.regexr.com/ - удобный ресурс для тестирования регулярок...

# http://habrahabr.ru/blogs/python/115825/
# https://habrahabr.ru/post/115436/

'''
Библиотека requests позволяет отправлять HTTP-запросы HEAD, GET, POST, PUT, PATCH и DELETE. Все заголовки и параметры 
добавляются очень просто, также и обработка ответов сервера. Разумеется, requests работает на базе urllib2, 
но берёт на себя всю сложную работу.
'''

re.split('[^a-z]', t)  # регулярное выражение, считающее разделителем любой символ, не являющийся буквой


Оператор	Описание
.	Один любой символ, кроме новой строки \n.
?	0 или 1 вхождение шаблона слева
+	1 и более вхождений шаблона слева
*	0 и более вхождений шаблона слева
\w	Любая цифра или буква (\W — все, кроме буквы или цифры)
\d	Любая цифра [0-9] (\D — все, кроме цифры)
\s	Любой пробельный символ (\S — любой непробельнй символ)
\b	Граница слова
[..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
\	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
^ и $	Начало и конец строки соответственно
{n,m}	От n до m вхождений ({,m} — от 0 до m)
a|b	Соответствует a или b
()	Группирует выражение и возвращает найденный текст
\t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно

https://tproger.ru/translations/regular-expression-python/
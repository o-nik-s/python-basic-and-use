# Работа с функциями: functool и лямбда функции


# В рамках уровка функциями будут называться не только функции
# Строго говоря, в Пайтон можно называть только те объекты, которые имеют тип функция

# Функциональный подход

# Метод уточной типизации: если что-то плавает как утка, крякает как утка и похоже на утку,
# вполне вероятно, что это - утка


# Большое внимание в Пайтон уделено работе с последовательностями (списки, итераторы) и работе с функциями.
# Дело в том, что большая часть стадартной библиотеки Пайтон использует их в качестве аргументов


# map
n, k = map(int, input().split())
print(n + k)

x = input().split()
print(x)
n, k = map(int, x) # f [a, b, c, ...] -> f(a), f(b), f(c), ...
print(n + k)

map_obj = map(int, x)
print(map_obj)
n = next(map_obj)
k = next(map_obj)
print(n + k)

# Однако в Пайтон есть механизм распаковки, что позволяет осуществлять множественное присваивание
# Если от знака присваивания слева находится больше чем одна переменная, а справа находится что-нибуль,
# по чему мы можем проитерироваться, будь то список, кортеж или итератор, то интерпретатор пытается
# "распихать" элементы последовательности по нашим переменным. И если элементов там оказалось больше, чем нужно,
# то тогда он упадет с ошибкой, а если меньше, чем нужно, то тоже упадет с ошибкой.

# В том момент, когда мы создаем объект класса map, мы запоминаем две ссылки. Мы запоминаем одну ссылку на функцию и
# одну ссылку на итератор второго аргумента. В тот момент, когда нас спращивают, какой же элемент является следующим next,
# мы считываем следующий элемент из нашего итератора, и затем применяем к нему ту функцию, которую нам передали.

# Мы можем написать то же самое, используя обычный генератор
n, k = (int(i) for i in x)
print(n + k)
print("\n\n")

# Стоит не бояться передавать функции внутрь других функций


# Класс фильтр
# Класс фильтр так же принимает внутрь себя два аргумента. Это - функция и последовательность, элементы которой мы хотим
# отфильтровать. Наша функция должна возвращать логическое значение True в том случае, если элемент последовательности
# нам подходит, и False, если не подходит.

# Считаем список целых чисел и оставим только те, которые являются четными
x = input().split() # Считаем строку, разобьем ее по пробелам
xs = (int(i) for i in x) # Приведем ее к целым числам

def even(x): # Проверяем, является ли число четным
    return x % 2 == 0

evens = filter(even, xs) # Оставляем лишь четные числа
for i in evens: # Для каждого четного числа мы его выведем в терминал
    print(i)

# Конструктор класса filter возвращает нам filter object. Этот filter object является итератором и внутри него реализован
# метод next.
# Однако конструктор класса, которым Вы захотите воспользоваться, если будете пользоваться итераторами,
# - это конструктор класса List. Дело в том, что если в конструктор класса List мы поместим итератор, то он попробует
# собрать все элементы итератора и поместить их внутрь одного листа.
# Однако пользоваться им нужно аккуратно. Во-первых, если Вы уверены, что итератор возвращает конечное число аргументов.
# И, во-вторых, если они разумно умещаются в оперативной памяти.

x = input().split() # Считаем строку, разобьем ее по пробелам
xs = (int(i) for i in x) # Приведем ее к целым числам
evens = list(filter(even, xs))
print(evens)


# В связи с тем, что мы начинаем передавать функции внутри других функций, возникает желание писать функции
# еще более коротко и лаконично. ДЛя этого в языке Пайтон есть лямбда-функции.

# Лямбда-функции - это всего лишь синтаксис в языке Пайтон для создания новых объектов функций.
even = lambda x: x % 2 == 0
# Здесь верны все те же правила, что и для аргументов обычных функций (со *, с **, со значением по умолчанию)
# Выражение должно быть возвращаемым значением
# Таким образом, мы в начале создали объект функции, используя синтаксис lambda, а затем присвоили имени even
# ссылку на данную функцию в оперативной памяти

# Но самое замечательное в синтаксисе lambda состоит в том, что мы можем подставить их внутрь функции
evens = list(filter(lambda x: x % 2 == 0, (int(i) for i in input().split())))
print(evens)

# Синтаксис лямбда-функции:
# lambda; аргументы, которые принимает наша функция; возвращаемое ей значение в одно выражение



# Сортировка
# Когда мы сортируем список, вместо ключа мы можем передать функцию, которая будет высчитана от всех элементов нашего списка
# И затем наш список будет осортирован не по порядку элементов, а по порядку значений данной функции

x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("Johb", "Backus")
]
# Мы бы хотели отсортировать данный список по суммарной длине имени

def length(name):
    return len(" ".join(name)) # Склеиваем по пробелу и возвращаем длину данной строки

name_length = [length(name) for name in x]
print(name_length)

x.sort(key=length) # Сортируем список по возрастанию длины их имени
print(x)

# Таким образом, передав функцию в качестве key, мы вначале вычилисли данную функцию на каждом элементе списка,
# а затем отсортировали наш список именно по этим значениям

# Если мы не хотим писать отдельную функцию length
x.sort(lambda name: len(" ".join(name)))
print(x)

# Иногда возникает желание использовать стандартные операции Пайтон именно в виде функций

# НАпример, мы хотим представить сумму в качестве функции, принимающей два аргумента и возвращающей сумму
# Для всего этого в Пайтон есть библиотека operator

import operator as op
print(op.add(4, 5))
print(op.mul(4, 5))
print(op.contains([1, 2, 3], 4)) # Проверяет, входит ли значение 4 в список [1, 2, 3]

# itemgetter позволяет достать элемент коллекции
x = [1, 2, 3]
f = op.itemgetter(1) # f(x) == x[1] - т.е. по сути функция реализовывает квадратные скобки и взятие элементов из некоторого множества
print(f(x))

x = {"123": 3}
f = op.itemgetter("123") # f(x) == x["123"] - в качестве ключа можем использовать словарь
print(f(x))

# attrgetter позволяет достать атрибут от объекта
f = op.attrgetter("sort")
print(f([]))


x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("Johb", "Backus")
]
# Попробуем отсортировать список по последнему элементу в кортеже
x.sort(key=op.itemgetter(-1))
print(x)

# Иногда для решения задач удобно использовать операторы в качестве функции для того, чтобы передать их аргументом в другую функцию
# Если Вы не хотите писать свою функцию сами, сначала проверьте библиотеку operator, наверняка она уже там реализована


# Еще одной полезной библиотекой для работы с функциями является библиотека functools

# И мы рассмотрим главную функцию от нее - функцию partial
# Функция partial позволяет запомнить нам некоторые аргументы, с которыми мы бы хотели вызвать функцию,
# и возвращает нам функцию, в которую нам эти аргументы передавать больше не нужно

from functools import partial

x = int("1101", base=2)  # Задаем число в двоичной системе счисления
print(x)

# Однако мы хотим написать функцию, которая принимала бы в качестве аргументов одно число, а делала бы то же самое
# Вызываеле бы функцию Int и указывала явным аргументом base = 2

int_2 = partial(int, base=2)
x = int_2("1101")
print(x)

# Таким образом, patrial берет функцию и частично подставляет в нее какие-то из аргументов
# При этмо возвращая нам новую функцию, в которую больше эти аргументы подставлять уже не нужно

# Теперь, применяя данные значния. мы можем написать одну большую функцию


x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("Johb", "Backus")
]

import operator as op
from functools import partial

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)

# Однако наша функция является универсалльной
y = ["abc", "cba", "abb"]
sort_by_last(y)
print(y)
# Так же отсортировали строки по последнему символу
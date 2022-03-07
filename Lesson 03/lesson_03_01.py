# Стандартные методы и функции для строк

# Проверка вхождения подстроки в строку
print("abc" in "abcba")
print("abc" in "abcba")

# Поиск позиции вхождения
print("cabcd".find("abc"))  # Индекс первого вхождения или -1
print("cabcd".find("aec"))  # -1
print()


# Рекомендуется читать документацию. Предже всего, в документации можно найти аргументы, которые
# имеют значение по умолчанию и чаще всего замалчиваются.
print(str.find.__doc__)  # Документация метода find

print("cabcd".find("abc", 1))  # Позиция внутри строки, начиная с 1
print("cabcd"[1:].find("abc"))  # Позиция втнури слайса

# Метод Index делает почти все то же самое, однако когда мы не находим подстроку внутри строки?
# мы бросаем ошибку ValueError
print("cabcd".index("abc"))  # Индекс первого вхождения или ValueError
# print("cabcd".index("aec")) # ValueError
print()

s = "The man in black fled across the desert, and the gunslinger followed"
print(s.startswith("The man in black")) # Проверяем, начинается ли строка с какой-то другой строки
print(s.startswith.__doc__)
# Префиксом так же может быть и кортеж из строк, который мы должны попробовать
print(s.startswith(("The woman", "The dog", "The man in black"))) # Можем проверить, кто именно идет по пустыне

s = "image.png"
print(s.endswith(".png")) # Проверяет, заканчивается ли строка некоторой подстрокой. Удобно использовать для проверки типов файлов.
print()

s = "abacaba"
print(s.count("aba")) # Проверяет число вхождений одной подстроки внутрь другой строки
# Однако нужно понимать, что она находит число непересекающихся вхождений

# У части данных функций есть правосторонние аналоги. Они делают все то же самое, но начинают читать строку справа налево
print(s.rfind("aba"))
print()


# Очень часто тексты строят таким образом, что буквы находятся в разных регистрах
s = "The man in black fled across the desert, and the gunslinger followed"
print(s.lower())  # Текст строки, все буквы которого находятся в верхнем регистре
print(s.upper())  # Текст строки, все буквы которого находятся в нижнем регистре
print(s.count("the"))
print(s.lower().count("the"))

s = "1,2,3,4"
print(s)
print(s.replace(",", ", ")) # Позволяет нацти все вхождения строки, переданной первым аргументом, и заменить ее
# на вхождения строки, которая передана вторым аргументом
print(s.replace.__doc__)
# Принимает еще один дополнительный элемент count - число замен, которое мы должны сделать
print(s.replace(",", ", ", 2))  # Заменим лишь 2 первых вхождения

s = "1 2 3 4"
print(s.split(" ")) # Разбивает строку по заданному разделителю; возвращает список
print(s.split.__doc__)
# maxsplit определяет то количество разбиений, которое мы можем сделать
print(s.split(" ", 2))
# Если не укажем разделитель или он будет равен None, то мы будем использовать в качестве разделителя
# любую последовательность пробельных символов и пустые строки будут удалены из ответа.
s = "1\t\t 2     3  \n  4       "
print(s.split())

s = "   1, 2, 3, 4   "
print(repr(s.rstrip()))
print(repr(s.lstrip()))
print(repr(s.strip()))
# Можно удалять не пробелы, а и другие символып
s = "_*___1, 2, 3, 4__*_"
print(repr(s.rstrip("*_")))
print(repr(s.lstrip("*_")))
print(repr(s.strip("*_")))

numbers = map(str, [1, 2, 3, 4, 5])
print(repr(" ".join(numbers))) # Принимает в качестве аргумента последовательность. Вставляет ту строку,
# от которой его вызвали, между элементами последовательности.
# Важно помнить, что элементы последовательности всегда должны быть строками.
print()

# Функции имеют правосторонние аналоги, с которыми можно ознакомиться в описании методов класса str.


# Форматирование

# Форматированием мы будем называть процесс подстановки какого-то конкретного значения в достаточно общий шаблон.

capital = 'London is the capital of Great Britain' # Общая фраза
template = '{} is capital of {}' # Шаблон
print(template.format("London", "Great Britain")) # Подставит значения, переданные в виде аргументов, на те позиции, которым мы указали
print(template.format("Vaduz", "Liechtenstein"))
print(template.format.__doc__)
# S.format(*args, **kwargs) -> str - принимает неограниченное число позиционных элементов,
# и неограниченное число аргументов, которым мы можем передать по имени

# Мы можем явно указать порядок
template = '{1} is capital of {0}'
print(template.format("London", "Great Britain")) # Подставит значения, переданные в виде аргументов, на те позиции, которым мы указали
print(template.format("Vaduz", "Liechtenstein"))
# По умолчанию по порядку перебираются переданные позиционные элементы

# Так же для форматирования можно использовать и именованные аргументы
template = '{capital} is capital of {country}'
# Тогда порядок не важен
print(template.format(capital="London", country="Great Britain"))
print(template.format(country="Liechtenstein", capital="Vaduz"))
print()


# Благодаря форматированию в Пайтон мы можем так же обращаться к атрибутам объектов, которые мы передали
import requests
template = "Response from {0.url} with code {0.status_code}"
# Мы получили ответ от такого-то адреса с таким-то кодом

res = requests.get("https://test.com")
print(template.format(res))

# res = requests.get("https://dosc.python.org/3.5/")
# print(template.format(res)) # code 200, что существует и доступна

# res = requests.get("https://dosc.python.org/3.5/random")
# print(template.format(res)) # code 404 - не существует
print()


from random import random
x = random()
print(x)
print("{:.3}".format(x))  # Указываем, что нас инетресует только три знака после запятой в нашем числе
# Наподобие того, как мы получали атрибуты нашего шаблона, мы так же можем получать элементы списка или значения словаря


'''
template = "Hello %s from %s"
print(template % ('John', 'London'))
# Hello John from London
-
Он устарел и не рекомендуется к использованию
'''


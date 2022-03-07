# XML, библиотека ElementTree, библиотека lxml

# XML - "расширяемый язык разметки"
# Так же как html является тэговым языком разметки, однако в XML мы придерживаемся более строгих правил,
# но основное отличие от XML в том, что мы сами определяем тэги

# Если XML используется чтобы данные отображать, чаще всего в браузере, то XML используется для того,
# чтобы данные хранить.

# Элементы XML
# Элементы определяются с помощью тэгов:
# <tag> </tag>
# <tag/> - тэг сразу открывается и закрывается

# Содержимое элементов: то, что было заключено между тэгами
# Так же мы храним внутри элемента атрибуты
# Атрибуты - это пара "ключ-значение", которая разделены равно. Значение всегда хранится в кавычках.
# И мы определяем атрибуты в открывающем теге.

# <tag id="1"> текст; элементы </tag>

# В XML-формате мы сами придумываем себе формат, сами придумываем тэги, сами придумывем имена для атрибутов

# Формат XML требует от нас наличие выделенного корня, т.е. такого элемента, который содержал бы в себе
# все остальные элементы.

# Библиотеки, которые раблотают с файлами XML, так или иначе хранят его в виде дерева.


# Для работы с файлами в XML формате в стандартной библиотеке Пайтон есть библиотека для работы с XML ElementTree

from xml.etree import ElementTree

tree = ElementTree.parse("example.xml") # Возрващает дерево
root = tree.getroot() # Спрашиваем корень дерева

print(root)
print(root.tag, root.attrib) # Атрибутов у корня нет, наш словарь пустой

# Если бы мы получили данные с помощью API в формате XML, то можно было бы использовать функцию fromstring
# и тем самым получить корень дерева
# use root = ElementTree.fromstring(string_xml_data) to parse from string

# Мы можем перебрать детей нашего корня используя цикл for
for child in root:
    print(child.tag, child.attrib)

# Для обращения к детям и детям детей можно использовать индексацию через числа
print(root[0][0].text)

# Все элементы нашего дерева будут иметь один класс Element
# Поэтому все имена методов и атрибутов у данных объектов будут одинаковы

# Мы можем найти что-нибудь интересное у нашего поддерева, используя метод iter
# root.iter("scores") вернет итератор, который перебирает все элементы нашего поддерева с данным тэгом

for element in root.iter("scores"):
    print(element)

for element in root.iter("scores"):
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)
# Если с помощью iter мы смогли перебрать все интересующие нас элементы в поддереве, то с помощью .findall мы
# сможем перебрать только лишь через детей.

# Теперь хотим научиться модифицировать деревья, создавать новые и записывать обратно в XML-формат

# from xml.etree import ElementTree
tree = ElementTree.parse("example.xml")
root = tree.getroot()

tree.write("example_copy.xml")

# Нам поступила новыя информация, что Грег заработал новые баллы в новом модуле. Давайте ее добавим.

greg = root[0]
module1 = next(greg.iter("module1"))
print(module1, module1.text)
module1.text = str(float(module1.text) + 30)
tree.write("example_modified.xml")
# Теперь Greg получил 100 баллов в новом модуле

# Теперь нужно изменить сертификат на сертификат с отличием
certificate = greg[2]
certificate.set("type", "with distinction")
tree.write("example_modified.xml")

# Как мы можем добавлять или создавать элементы из другог элемента?
tree = ElementTree.parse("example_modified.xml")
root = tree.getroot()
greg = root[0]

description = ElementTree.Element("description")
description.text = "Showed excellent skills during the course"
greg.append(description)

# Предположим, решили убрать данное описание
description = greg.find("description") # Находим вхождение первого ребенка, который является тегом description
greg.remove(description) # Хотим удалить description из элемента Greg

tree.write("example_modified.xml")
# print(ElementTree.ElementTree.__doc__)


# А вот если бы мы хотели создать дерево с самого начала, то см. creation.py
from xml.etree import ElementTree

# Создали корень дерева, используя конструктор Элемент
root = ElementTree.Element("student")

# Используя конструктор СабЭлемент, можем указать, чьим ребеном является данный элемент, который мы создаем
first_name = ElementTree.SubElement(root, "firstName")
first_name.text = "Greg"

second_name = ElementTree.SubElement(root, "secondName")
second_name.text = "Dean"

scores = ElementTree.SubElement(root, "scores")

# Затем для каждого модуля создаем по элементу и говорим, что они являются детьми нашего элемента scores
module1 = ElementTree.SubElement(scores, "module1")
module1.text = "100"

module2 = ElementTree.SubElement(scores, "module2")
module2.text = "80"

module3 = ElementTree.SubElement(scores, "module3")
module3.text = "90"

# Создаем дерево и в конструктор ElementTree передаем корень, за который будем поддерживать наше дерево
tree = ElementTree.ElementTree(root)

# Записываем все наше дерево внуть одного xml-файла
tree.write("student.xml")
print()

# XML-файд без переноса строк является синтаксически верным XML-файлом


# Здесь мы можем вспоминить про HTML

# Почему мы не можем использовать те же механизмы разбора, которые мы используем для XML, для того, чтобы разбирать данные
# для HTML.
# Реалии таковы, что большая часть траффика дл HTML является плохо сформированной.
# Поэтому для работы с ним используют сторонние библиотеки Beautiful Soup и LXML.


# Рассмотрим библиотеку LXML

from lxml import etree
# Это связано с тем, что библиотека etree пытается вести себя точно так же как встроекнная в Питон библиотека ElementTree.
import requests

res = requests.get("https://docs.python.org/3/")
print(res.status_code)
print(res.headers["Content-Type"])

# Именно этот парсер является той самой "умной" частью библиотеки LXML, которая отличает его от языка Пайтон.
# Он позволит работать с той частью в формате HTML, которая плохо сформирована
parser = etree.HTMLParser()
root = etree.fromstring(res.text, parser) # Вернет корень нашего дерева

# print(root)
# Переберем все элементы в поддереве нашего корня, которые являются атрибутом 'a'
# Мы выведем на экран данные элементы и их атрибуты
for element in root.iter("a"):
    print(element, element.attrib)

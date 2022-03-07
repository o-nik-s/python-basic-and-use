# author
import xml.etree.ElementTree as ET

tree = ET.fromstring(input())
ans = {"red": 0, "green": 0, "blue": 0}

def dfs(cube, res, depth):
    res[cube.attrib["color"]] += depth
    for i in cube.findall("cube"):
        dfs(i, res, depth + 1)

dfs(tree, ans, 1)
print(ans["red"], ans["green"], ans["blue"])


from xml.etree import ElementTree

root = ElementTree.fromstring(input())
colors = {"red": 0, "green": 0, "blue": 0}

def getcubes(root, value):
    colors[root.attrib['color']] += value
    for child in root:
        getcubes(child, value+1)

getcubes(root,1)
print(colors["red"], colors["green"], colors["blue"])


from xml.etree import ElementTree
colors = {"red": 0, "green": 0, "blue": 0}  # словарь ключ=цвет
def finder(root, count=1):
    colors[root.attrib["color"]] += count  # нашли цвет добавили к счётчику
    [finder(child, count + 1) for child in root]  # поиск во вложениях
finder(ElementTree.fromstring(input()))  # считываем xml-строку
print(colors["red"], colors["green"], colors["blue"])  # выдаём ответ


from xml.etree import ElementTree
values = {
    'blue': 0,
    'red': 0,
    'green': 0
}
def func(tree, value=1):
    values[tree.get('color')] += value
    for element in tree:
        func(element, value + 1)
func(ElementTree.fromstring(input()))
print(values['red'], values['green'], values['blue'])


# любой узел, в т.ч. корневой:
#     может отличаться от cube
#     может иметь любой цвет
#     может вообще не иметь цвета
import xml.etree.ElementTree
colors = ('red', 'green', 'blue')  # допустимые цвета
weight = {}  # словарь {цвет: вес}
total = []  # список всех узлов уровня 2+ (вложенных в root)
root = xml.etree.ElementTree.fromstring(input())
if root.tag == 'cube' and 'color' in root.attrib:  # если корневой тэг == cube и у него есть цвет
    weight[root.attrib['color']] = weight.get(root.attrib['color'], 0) + 1  # добавим вес цвета в словарь
for color in colors:  # добавляем в список все узлы каждого цвета
    total.extend(root.findall(".//cube[@color='{color}']".format(color=color)))
level = 2  # уровень, на котором считаем веса цветов
while len(total) > 0:  # будем вести подсчёт повышая уровень, пока не пройдем все элементы
    for color in colors:  # для каждого из цветов
        lst = root.findall("./{level}[@color='{color}']".format(color=color, level='cube/' * (level - 1)))  # добавим во временный список узлы c уровня level и цвета color
        weight[color] = weight.get(color, 0) + len(lst) * level  # добавим в словарь вес цвета color
        for el in lst:  # удалим из общего списка узлов посчитанные цвета
            total.remove(el)
    level += 1  # следующий уровень
[print(weight[c], end=' ') for c in colors]
# решил без рекурсии, ибо надоела :)


from xml.etree import ElementTree
root = ElementTree.fromstring(input())
dict_val = {'red': 0, 'green': 0, 'blue': 0}
def get_value_color(element, depth):
    dict_val[element.attrib['color']] += depth
    for child in element:
        try:
            get_value_color(child, depth + 1)
        except StopIteration:
            return
get_value_color(root, 1)
print('{} {} {}'.format(dict_val['red'], dict_val['green'], dict_val['blue']))


# put your python code here
import xml.etree.ElementTree as etree
import collections
c = collections.Counter()
def deep_find(et, level=1):
    c[et.attrib['color']] += level
    for e in et:
        if e is not None:
            deep_find(e, level + 1)
xm = input()
deep_find(etree.fromstring(xm))
print(c['red'], c['green'], c['blue'])

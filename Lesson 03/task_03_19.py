'''
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>
 
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. 
Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, 
имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
'''

from xml.etree import ElementTree

def getChilds(root, level):
    for child in root:
        cubeList.append((child.attrib['color'], level + 1))
        getChilds(child, level + 1)


'''inputXML = input()
with open("input_task_03_19.xml", "w") as inF:
     inF.write(inputXML)
tree = ElementTree.parse("input_task_03_19.xml") # Возвращает дерево
root = tree.getroot() # Спрашиваем корень дерева'''

root = ElementTree.fromstring(input())

cubeList = list()
cubeList.append((root.attrib['color'], 1))
getChilds(root, 1)
# print(cubeList)
cubeDict = dict()
for cub in cubeList:
    cubeDict[cub[0]] = cubeDict.get(cub[0], 0) + cub[1]
# print(cubeDict)
print(cubeDict.get("red", 0), cubeDict.get("green", 0), cubeDict.get("blue", 0))

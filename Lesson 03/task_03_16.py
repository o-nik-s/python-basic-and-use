'''
Вам дано описание наследования классов в формате JSON. 
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта 
есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:
class A:
    pass
class B(A, C):
    pass
class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется 
явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.
'''

import json


def classParents(name):
    global parents
    for cl in classDict[name]:
        parents.add(cl)
        for p in classDict[cl]:
            parents.add(p)
        classParents(cl)


inpt = json.loads(input())
classDict, parentsDict = {}, {}
for el in inpt:
    classDict[el['name']] = el['parents']
for cl in classDict:
    parents = set(classDict[cl])
    for parent in classDict[cl]:
        classParents(parent)
    parentsDict[cl] = parents
childDict = dict()
for cl in parentsDict:
    childDict[cl] = set()
    # childDict[cl].add(cl)
    for child in parentsDict:
        if cl in parentsDict[child]:
            childDict[cl].add(child)
for parent in sorted(childDict):
    print(parent, ":", len(childDict[parent]) + 1)

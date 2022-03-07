# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

# Или эквивалентно записи:
# class Class1(Class2, Class3 ... ClassK):
#     pass

# Класс A является прямым предком класса B, если B отнаследован от A:
# class B(A):
#     pass

# Класс A является предком класса B, если
# - A = B;
# - A - прямой предок B
# существует такой класс C, что C - прямой предок B и A - предок C

# Например:
# class B(A):
#     pass

# class C(B):
#     pass

# A -- предок С

# Вам необходимо отвечать на запросы, является ли один класс предком другого класса

# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.

# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
# В следующих n строках содержится описание наследования классов. В i-й строке указано, от каких классов
# наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется,
# что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса
# более одного раза.
# В следующей строке содержится число q - количество запросов.
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2,
# и "No", если не является.


def insrtInDescr(dct):
    global stF
    if parent in dct:
        dct[parent][child] = dict()
        stF = True
    else:
        for val in dct.values():
            insrtInDescr(val)


def findElem(elem, dct):
    if elem in dct:
        return dct[elem]
    else:
        for val in dct.values():
            findEl = findElem(elem, val)
            if findEl != None:
                return findEl


n = int(input())
classDescription = dict()
classDescription['object'] = dict()
classDescrList = list()
for i in range(n):
    clDescrNow = input().strip()
    classDescrList.append(clDescrNow)
i = 0
while len(classDescrList) != 0:
    clDescrNow = classDescrList[0].strip()
    if ":" not in clDescrNow:  # Нет родителей
        classDescription['object'][clDescrNow] = dict()
        classDescrList.remove(classDescrList[i])
    else:  # Есть родители
        count  = len(classDescrList)
        sep = clDescrNow.find(':')
        child, parents = tuple(map(lambda x: x.strip(), clDescrNow.split(':')))
        childDict = dict()
        stF = False
        for parent in parents.split():
            insrtInDescr(classDescription['object'])
        if not(stF):
            classDescrList.append(classDescrList[i])
        classDescrList.remove(classDescrList[i])
        if count == len(classDescrList): # Родители отдельно не заданы, надо создавать вручную!
            for parent in parents.split():
                classDescription['object'][parent] = dict()
print("Итого: ", classDescription)
q = int(input())
for i in range(q):
    parent, child = input().split()
    parentDict = findElem(parent, classDescription['object'])
    if parent == child and parentDict != None:
        print("Yes")
    elif parentDict == None:
        print("No")
    else:
        findChild = findElem(child, parentDict)
        print((findChild != None) * "Yes" + (findChild == None) * "No")

# Отладочные тесты:
# https://stepik.org/lesson/24462/step/7?discussion=337590
# https://stepik.org/lesson/24462/step/7?discussion=195450&reply=195488
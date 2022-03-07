import json

def find_children(parents_class, simple_class, already_parents):
    if parents_class == simple_class:#при первом входе добавляем parents_class в словарь
        already_parents[parents_class] = [parents_class]
    for j in res:#проходим по всем элементам списка словарей
        if simple_class in j['parents'] and j["name"] not in already_parents[parents_class]:#проверка на вхождения
            already_parents[parents_class] += [j["name"]]
            find_children(parents_class, j["name"], already_parents)#запуск рекурсии
    return
vvod = input() #считываем строку
already_parents = {}
res = json.loads(vvod)#преобразовываем в список словарей
for i in res:#проверяем все элементы списка
    find_children(i["name"], i["name"], already_parents)#запускаем функцию
l = already_parents.keys() #достаем ключи
l = list(l)#преобразуем в список
l.sort() #сортировка
for i in l: #вывод результата
    print(i, ':', len(already_parents[i])) 
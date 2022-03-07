n = int(input())
classes = {}
for i in range(n):
    line = input()
    parts = line.split(" : ")
    cls = parts[0]
    if len(parts) == 1:
        classes[cls] = []
    else:
        classes[cls] = parts[1].split(" ")


def check(src, dest):
    if src == dest:
        return True
    return any([check(child, dest) for child in classes[src]])


m = int(input())
used = []

for i in range(m):
    cls = input()
    if any([check(cls, used_one) for used_one in used]):
        print(cls)
    used.append(cls)


'''Пример правильного решения.

Идейно задача почти не отличается от задачи с наследованием классов из первого модуля:
Сводить задачи к уже решенным и переиспользовать свой код -- можно и даже нужно.

Храним предков в таком же формате; функция проверки наследования одного класса от другого также может быть переиспользована.

Теперь нужно лишь проверить для каждого исключения в except-списке, не ловили ли мы выше предка этого исключения. 
И если ловили -- то данное исключение можно не ловить и вывести его в терминал.'''
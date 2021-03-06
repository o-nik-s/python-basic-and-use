# # тестовый граф наследования
#     A   X
#    /|\ / \
#   B C Y   Z
#    \|  \ /
#     D   V
#    / \   \
#   E   F   W
#        \
#         G

lst_mro = [  # тестовый граф наследования в ввиде списка "введённых пользователем" строк
    'G : F',  # сначала отнаследуем от F, потом его объявим: корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    'A',
    'B : A',
    'C : A',
    'D : B C',
    'E : D',
    'F : D',
    # а теперь другая ветка наследования
    'X',
    'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    'Z : X',
    'V : Z Y',
    'W : V',
]

lst_q = [  # тестовый список "введённых пользователем" запросов
    'X QWE',    # No    # нет такого класса QWE
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'A X',      # No    # классы есть, но они нет родства :)
    'X W',      # Yes   # X предок W через Y, V
]

lst_mro = [input() for i in range(int(input()))]  # раскомментировать для сдачи задания
lst_q = [input() for i in range(int(input()))]    # раскомментировать для сдачи задания

lst_mro = [el.replace(':', ' ').split() for el in lst_mro]  # список наследования  # [[потомок, родитель1, родитель2, ..., родительN], []]
lst_q = [el.split() for el in lst_q]  # список запросов

lst_otv = []  # список ответов по порядку списка запросов
dct_mro = {}  # словарь наследования  # {'A': [], 'W': ['V'], 'E': ['D'], 'Z': ['X'], 'F': ['D'], 'G': ['F'], 'V': ['Z', 'Y'], 'X': [], 'B': ['A'], 'Y': ['X', 'A'], 'D': ['B', 'C'], 'C': ['A']}

for i in range(len(lst_mro)):  # составим словарь {потомок: [список предков]} по входным данным
    dct_mro[lst_mro[i][0]] = dct_mro.get(lst_mro[i][0], []) + lst_mro[i][1:]


def check_parent_for_child(parent, child):
    if parent not in dct_mro:  # если класс не был объявлен в списке наследования
        return False           # значит это самозванец :)

    if parent == child:  # если поступил запрос вида 'родитель родитель'
        return True      # то нужно ответить 'Yes', т.е. вернуть True

    lst_parents = dct_mro.get(child, [])  # получаем список предков класса child
    if len(lst_parents) > 0:              # если список не пуст - работаем по нему
        for p in lst_parents:             # иначе child не был объявлен в списке наследования (самозванец :) )
            if check_parent_for_child(parent, p):
                return True
    # else:
    #     return False

for prnt, chld in lst_q:
    if check_parent_for_child(prnt, chld):
        print('Yes')
    else:
        print('No')

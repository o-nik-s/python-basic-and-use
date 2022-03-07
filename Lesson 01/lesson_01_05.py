# Введение в классы

# Все данные в Python представлены объектами и отношениями между объектами
# У любого объекта в Python есть тип
# Однако для решения задач не всегда удобно использовать только существующие типы

# Для определения объектов новых типов существуют классы
# Классы в Python позволяют описать поведение объектов данного класса
# Так же классы позволяют создать сами объекты данного класса
# Таким образом, классы в Python - это механизм и синтаксис для описания собственных типов данных

class MyClass:
    # Тело класса
    a = 10

    def func(self):
        print('Hello')

# В отличие от функции тело класса исполняется в момент определения самого класса
# Более того, так же как и в функциях, для тела класса создается отдельный namespace и те имена, которые в этом
# namespace остались, затем закрепляются за объектом класса

# После того, как объявление класса исполнилось, создается объект myClass
# Имена, которые остались в namespace после исполнения, закрепляются за объектом myClass

# Мы можем достучаться до этих объектов, написав:
print(MyClass.a)
print(MyClass.func)

# В таком случае про a и func будет правильно сказать, что они являются атрибутами класса MyClass
# К атрибутам можно обратиться через точку
# Формально атрибут - это какое-то имя внутри пространства имен
# А точка - это некоторый синтаксис, чтобы обратиться к этому имени


# Куда более интересно создание объектов класса
# Поэтому в Python предусмотрен механизм инстанцирования или конструктор

# Чтобы запустить конструктор класса и создать новый объект класса мы должны воспользоваться нашим классом как функцией и вызвать ее
x = MyClass()  # Создание нового объекта x класса MyClass
# Конструкторы так же есть и у встроенных классов
lst = list() # Вызываем конструктор явно
lst = [] # Используем синстксис языка
# При этом конструктор всегда будет запущен, когда мы создаем новый объект класса

# Более того, у любого класса в Python всегда есть конструкторы
# И конструктор - это единственный механизм, которым создаются новые объекты

print(type(x))
print(type(MyClass))

# После создания класса гарантируются всего две вещи
# 1. Мы всегда можем вызвать его конструктор
# 2. Мы можем обращаться к его атрибутам


# Действия с объектами
class Counter:
    pass
# Когда исполнится класс Counter, с именем Counter будет связан объект в оперативной памяти.
# Этот объект будет соответствовать созданному классу.
print(Counter)  # class object

# Теперь воспользуемся конструктором и создадим объект типа Counter()
x = Counter()  # x in instance object - экземпляр класса Counter
# Если для самого класса мы можем вызвать конструктор и использовать его атрибуты
# То для экземпляра класса мы можем работать только с атрибутами
x.count = 0  # Создаем новый атрибут у нашего объекта instance, т.е. объекта экземпляра
x.count += 1

# Важно понимать, что так же как и с классом, с каждым экземпляром класса будет ассоциировано новое пространство имен
# И именно в данном пространстве имен мы будем создавать новые имена и присваивать им какие-то объекты

# Итак
# У нас есть объекты классы
# И у нас есть объекты экземпляры
# Экземпляры имеют тип нашего класса, который мы создаем
# Конструктор позволяет на создавать экземпляры
# И что у объектов классов что у объектом экземпляров есть свое собственное пространство имен
# Атрибуты в данном пространстве имен мы можем изменять и можем создавать


# Конструктор нужен прежде всего для того, чтобы создавать новые объекты нашего класса.
# И в языке Пайтон есть возможность определение поведение конструктора.
# Это нужно для определения некоторых значений атрибутов уже созданных экземпляров по умолчанию.
# Для этого нужно определить функцию __init__ внутри нашего класса.
# def __init__(self, ...):

# Конструктор нужен прежде всего того, чтобы создавать новые объекты нашего класса
# В Пайтон существует возможность определить поведение конструктора
# Это может быть нужно для того, чтобы мы могли определить некоторые значения атрибутов уже созданных экземпляров
# по умолчанию
# Для того, чтобы определить поведение конструктора, необходимо определить функцию init внутри нашего класса


# В начале создается пустой объект класса /нет ни одного атрибута/
# Уже этот объект передается в функцию в качестве self
# Внутри self мы можем присвоить ему какие-то атрибуты
# Функция init не должна возвращать какое-либо значение, т.е. идеалогически возврат функции должен быть None
# Это связано с тем, что идеологически функция init всего лишь устанавливает атрибуты для нашего объекта self

class Counter:
    def __init__(self): # Первый агрумент, который принимается, - это уже какой-то экземпляр нашего класса
        self.count = 0

x = Counter()
# x будет ссылаться на тот же измененный self, который мы передали внутрь конструктора
print(x.count)
# Установленные в конструкторы атрибуты ведут себя так же, как и другие атрибуты
x.count += 1

# Функция init() не обязательно может принимать всего один аргумент self
class Counter: # Пусть хотим, чтобы счетчик начинал счет с некоторого заданного числа
    def __init__(self, start=0): # Аргументы вслед за self инициализируются аргументами, которые мы передали внутрь конструктора
        self.count = 0

x1 = Counter(10)
x = Counter()
print(x.count)
x.count += 1


# Описанный механизм работает ...

# Переменные класса, переменные экземпляра, плохой пример
class Song():
    tags = [] # Аргумент tags

    def __init__(self, artist, song):
        self.artist = artist
        self.song = song

    def add_tags(self, *args): # Метод, который добавляет теги в атрибут tags
        self.tags.extend(args)

# Важно понимать, что в конструкторе и в коде мы явно не определяем tags у каждого из экземпляров
# Поэтому Т.к. конструктор не находит тэги в экземпляре, он находит их в классе

song1 = Song("Neuromonah Feofan", "Holodno v lesu")
song1.add_tags("Russian", "Drum'n'base")

song2 = Song("S G", "R t B")
song2.add_tags("A", "C")

# В конструкторе мы нигде явно не определяем tags у каждого из экземпляров
# Каждый раз когда мы вызываем add_tags(), т.к. tags не найден в экземпляре, он использует song.tags

# Таким образом, наши тэги каждый раз, когда мы вызываем метод, добавяться в один и тот же объект

print(song2.tags) # ['Russian', "Drum'n'base", 'A', 'C'] -  is Song.tags - это имя tags в namespace song
print(song1.tags)

# Две ошибки
# Мы имели в виду, что теги являются атрибутом конкретного экземпляра, потому как тэги ассоциируем с атрибутом, а не с классом
# Метод add_tags не менял никакого объекта, идеологически неправильно использовать метод, потому что он менял класс, а не объект

# Этого всего можно было бы избежать, если бы меняли атрибут tags внутри конструктора

class Song():

    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        self.tags = [] # Аргумент tags

    def add_tags(self, *args): # Метод, который добавляет теги в атрибут tags
        self.tags.extend(args)

song1 = Song("Neuromonah Feofan", "Holodno v lesu")
song1.add_tags("Russian", "Drum'n'base")

song2 = Song("S G", "R t B")
song2.add_tags("A", "C")
print(song2.tags)
print(song1.tags)


# ? Описанный механизм поиска атрибутов работает не только для методов
# ? Если атрибут, который мы не нашли не в экземпляре, но нашли в классе, не является функцией, то мы просто можем его использовать.


# Три новых типа:
# 1. Объекты класса /можем вызвать конструктор; создавть и обращаться к атрибутам/
# 2. Объекты экземпляра /можем создавть и обращаться к атрибутам/
# 3. Связанные методы. Они ссылаются на объект и ссылаются на функцию внутри класса /можем лишь вызывать/

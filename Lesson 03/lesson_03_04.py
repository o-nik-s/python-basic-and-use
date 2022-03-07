# Распространённые форматы текстовых файлов: CSV, JSON

# CSV-формат
# first name,last name,module1,module2,module3
# student,best,100,100,100
# student,good,90,90.2,100
# Таблица описывает имена студентов и сколько баллов они набрали в каждом модуле
# Данный формат идеально подходит для хранения табличных данных

# Для работы с форматом csv есть библиотека csv
import csv
with open("example.csv") as f:
    reader = csv.reader(f) # Конструктор класса reader, он является итерируемым,
    for row in reader: # поэтому мы можем перебирать с помощью итератора строки нашей таблицы
        print(row)

# А зачем нам для этого целая библиотека
# Значение в двойных кавычках и с запятой попадет в отдельный элемент нашей таблицы /например, "90,2"/
# Кроме того, отдельный элемент в кавычках записывается даже если содержал перенос строки

# Мы можем сами указать знак разделителя
import csv
with open("example.tsv") as f:
    reader = csv.reader(f, delimiter="\t") # Конструктор класса reader, он является итерируемым,
    for row in reader: # поэтому мы можем перебирать с помощью итератора строки нашей таблицы
        print(row)

# Данный модуль позволяет не только считывать, а и записывать файлы
students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("example.csv", "a") as f:  # a - хотим дозаписать студентов в файл
    writer = csv.writer(f)
    for student in students:
        writer.writerow(student)

with open("example.csv", "a") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(students) # Сразу передаем список списка без итерации по списку
# quoting=csv.QUOTE_ALL - нужно поместить в кавычки все передаваемые значения
# quoting=csv.QUOTE_NONNUMERIC - поместить внутрь кавычек все нечисловые значения


# Формат json /изанчально - для описания объектов javascript/

# Ключом в json-объекте может быть только строка, true и false пишется с маленькой буквы,
# а значению None будет соответствовать значение null
# Так же строки можно объявить только в двойных кавычках

# Однако помимо всех этих мелочек каждой сущености в json существует аналог в языке Пайтон

# Для работы c json используется библиотека json

import json

student1 = {
    'first_name': 'Greg',
    'last_name': 'Dean',
    'scores': [70, 80, 90],
    'description': "Good job, Greg",
    'certificate': True
}

student2 = {
    'first_name': 'Wirt',
    'last_name': 'Wood',
    'scores': [80, 80.2, 80],
    'description': "Nicely Done",
    'certificate': True
}

data = [student1, student2]
data_json = json.dumps(data, indent=4, sort_keys=True)
# Функция dumps принимает первым аргументом объект языка Пайтон
# и возвращает соответствующее ему строковое представление в формате json
# Аргумент intend - количество отступов, которое нужно использовать в списках и словарях
# sort_keys=True - нужно отсортировать ключи кажлого словаря, который попадается в данном объекта

# print(json.dumps(data, indent=4, sort_keys=True))
# Чтобы записать данные в файле формата json
with open("students.json", "w") as f:
     json.dump(data, f, indent=4, sort_keys=True) # Функция dump вместо dumps

# Чтобы получить объект Пайтон, соответствующий строковому представлению в json, используем функцию loads
data_again = json.loads(data_json)
print(sum(data_again[0]["scores"]))

# Чтобы считать из файла данные в формате json
with open("students.json", "r") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"]))

# Формат удобен, т.к. сущности соответствующие
'''
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго 
с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
'''


import csv

crimesList, maxCrime = {}, ("", 0)
with open("Crimes.csv") as f:
    reader = csv.reader(f, delimiter=",") # Конструктор класса reader, он является итерируемым,
    header = next(reader)
    print(header)
    for row in reader: # поэтому мы можем перебирать с помощью итератора строки нашей таблицы
    #    print(row)
        year = row[header.index("Date")].split()[0].split("/")[2]
        type = row[header.index("Primary Type")]
        if year == "2015":
            crimesList[type] = crimesList.get(type, 0) + 1
print(crimesList)
for key, value in crimesList.items():
    if value > maxCrime[1]:
        maxCrime = (key, value)
print(maxCrime)


'''
Кстати, нашел интересный модуль в стандартной библиотеке коллекций как раз под эту задачу:

https://docs.python.org/3/library/collections.html#collections.Counter

collections.Counter()
И в особенности его метод .most_common()
С их помощью задача вообще в несколько строк кода решается!
'''
# для доступа к колонке по ключу можно использовать csv.DictReader

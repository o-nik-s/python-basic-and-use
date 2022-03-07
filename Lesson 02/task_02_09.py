'''Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab'''

inf = open("dataset_24465_4.txt")
filereadlines = inf.read().splitlines()
# print(filereadlines)
inf.close()
wrf = open("output_20_09.txt", "w")
for line in filereadlines[::-1]:
    print(line, file=wrf)
    # wrf.write(line+"\n")
wrf.close()

# можно ещё функцию reversed() применить к списку строк исходного файла, и получить тот же список в обратном порядке

with open("dataset_24465_4.txt") as inf, open("output_02_09.txt", "w") as outf:
    outf.writelines(reversed(list(inf)))


'''Моё исходное решение было таким:
with open("input") as i, open("output", "w") as o:
    o.writelines(reversed([s for s in i]))
 Но сейчас я на него посмотрел и понял, что можно ещё проще ;-)
with open("input") as i, open("output", "w") as o:
    o.writelines(reversed(list(i)))
 А если не контролировать открытие и закрытие файлов, то вообще можно так ;-)))
open("output", "w").writelines(reversed(list(open("input"))))'''
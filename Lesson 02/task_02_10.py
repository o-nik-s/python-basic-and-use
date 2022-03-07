'''Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, 
в которых есть хотя бы один файл с расширением ".py". 

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных 
в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
Пример архива:  
Пример ответа: '''

import requests # Работа с ссылками
import zipfile # Работа с zip-архивами

import os
import os.path

print(os.getcwd())
dir = "main"
# os.chdir(dir)
print(os.getcwd())


dirList = []
i = 0
outf = open("output_02_10.txt", "w")
for current_dir, dirs, files in os.walk(dir):
    # print(current_dir)
    # print(i, current_dir, files)
    for file in files:
        if file[-3:] == ".py":
            i += 1
            print(i, current_dir, file)
            dirList.append((i, current_dir, file))
            print(current_dir, file=outf)
            break
print(dirList)
outf.close()

# Расширение файла можно выцепить многими способами, но лучший — использовать os.path.splitext.

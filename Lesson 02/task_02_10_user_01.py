import zipfile # Работа с zip-архивами
import os.path

ARC = 'main'  # имя файла-архива, файла-списка

# распаковка архива прямо в рабочую директорию
if zipfile.is_zipfile('{}.zip'.format(ARC)):
    with zipfile.ZipFile('{}.zip'.format(ARC)) as zf:
        zf.extractall()

lst = []  # заполняем список папок
for dirPath, childDirNames, fileNames in os.walk(ARC):
    for name in fileNames:
        if name.endswith('.py'):
            lst.append(dirPath)
            break  # вместо доп. условия if name.endswith('.py') and dirPath not in lst:

# сортировка и выгрузка списка в файл
with open('{}.txt'.format(ARC), 'w') as out:
    out.writelines('\n'.join(sorted(lst)))
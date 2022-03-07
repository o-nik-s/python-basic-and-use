# Стиль программирования: pep8 и документация

# PEP - дословно - предложения по улучшению языка Пайтон

'''
Ссылка на официальную версию документа PEP8: https://www.python.org/dev/peps/pep-0008/﻿

Официальная версия документа PEP8 написана на английском языке, однако в интернете можно найти переводы 
данного документа на русский язык:﻿ 
﻿http://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html или 
﻿http://defpython.ru/pep8﻿.

Однако данные переводы могут быть слегка устаревшими, а официальная версия документа время от времени обновляется. ﻿
'''

# В PyCharm стилистические ошибки подсвечиваются серым цветом.

# Всю эту информацию можно узнать, запустив консольную утилиту pep8, которую можно установить с помощью
# pip install pep8
# на нужном файле.
# pep8 generators.py /в консоли/

# Ошибки с E являются критическими. Ошибки с W являются предупреждениями.

# https://www.python.org/dev/peps/pep-0008/


# Кроме стиля программирования сделать код более понятным могут документирующие строки.

# Можно использовать строку в начале функции, метода и класса для описания их работы
# При этом данная строка будет доступна в качестве атрибута doc
# ИмяКласса.__doс__

# Таким образом можно смотреть документацию большинства стандартных модулей
import sys
print(sys.__doc__)
print(sys.getrefcount.__doc__)

'''Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять,
какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей 
служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.
# https://stepik.org/media/attachments/lesson/24466/encrypted.bin
# https://stepik.org/media/attachments/lesson/24466/passwords.txt

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
'''

from urllib import request
import simplecrypt

encrypted = request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()
passwords = request.urlopen('https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip().split()
# print(encrypted.decode("utf-8"))

print(encrypted)
for passw in passwords:
    passw = passw.decode()
    print(passw)
    try:
        print(simplecrypt.decrypt(passw, encrypted))
    except Exception:
        print("Bad password or corrupt / modified data")

print()


'''#with open("encrypted.bin", "rb") as encrf, open("passwords.txt", "r") as passf:
    encrypted = encrf.read().strip()[2:]
    passwords = passf.read().strip().split()
    print(passwords)
    for passw in passwords:
        print(passw)
        print(simplecrypt.decrypt(passw, encrypted))
    for encr in encrypted:
        print(encr)

print(encrypted)

with open("passwords.txt", "r") as inp:
    pass
'''

'''Чтобы получить фразу в тексте нужно еще перевести бинарник в текст с помощью
str.decode('utf8')'''

'''
Вот так можно скачать файл по url:

﻿import urllib
from urllib import request﻿

﻿﻿encrypted = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()
passwords = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip().split()﻿
'''

'''- а что за b' появляется в каждой строке при таком способе считывания
- бинарные данные. В примере написан вариант считывания с указанием 'rb', у меня не указано = 'r' по умолчанию. 
А принт просто преобразует бинарные данные в такой вид.
'''

'''Ребята! Надо же подчеркнуть, что если пароль неправильный, то выбрасывается исключение. 
По идее - должна получаться бессмысленная фраза при неправильном пароле.'''

'''
может кому будет полезно, решал так:
- прочитал оба файла
- преобразовал пароли в список из строк (перед первым паролем нужно убрать  b' )
- создал цикл в котором проверял пароли методом decrypt

Важно(!) внутри цикла отлавливать ошибки, так как при неправильном пароле модуль райзит - 
DecryptionException('Bad password or corrupt / modified data.')
и печатал результат декрипта, там все видно сразу.
Всем успехов!'''
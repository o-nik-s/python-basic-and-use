'''Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, 
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти 
за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.'''

import re
import requests


def reqLinks(url):
    req = requests.get(url)
    # if res.status_code == 200:
    if req.status_code == requests.codes.ok:
        return re.findall(pattern, req.text)
    else:
        return []


pattern = r"<a href=\"(\w*:[/|\w|\.]*)\">"
# pattern = r"(?<=href\=\")(.*?)(?=\")"
# print(re.findall(pattern, line))

url1 = input().strip()
url2 = input().strip()
linkList = reqLinks(url1)
print(linkList)
st = False
# if res.status_code == 200:
if url2.split() in linkList:
    st = True
else:
    for link in linkList:
        linkList2 = reqLinks(link)
        print(linkList2)
        if url2 in linkList2:
            st = True
print("Yes" if st else "No")

'''
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, 
выведите их имена в лексикографическом порядке.

Работа с API Artsy

Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа 
к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), 
и в дальнейшем все запросы к API осуществляются при помощи этого ключа.

Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API 
https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, 
и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.

После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, 
как можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.

import requests
import json

client_id = '...'
client_secret = '...'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]


Теперь все готово для получения информации о художниках. На стартовой странице документации есть пример того, 
как осуществляется запрос и как выглядит ответ сервера. Пример запроса на Python.
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)

Пример входных данных:
4d8b92b34eb68a1b2c0003f4
537def3c139b21353f0006a6
4e2ed576477cc70001006f99

Пример выходных данных:
Abbott Mary
Warhol Andy
Abbas Hamra

Примечание:
﻿В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

Примечание для пользователей Windows
При открытии файла для записи на Windows по умолчанию используется кодировка CP1251, 
в то время как для записи имен на сайте используется кодировка UTF-8, что может привести к ошибке при попытке 
записать в файл имя с необычными символами. Вы можете использовать print, или аргумент encoding функции open.
'''

'''
Name	App Artsy
Client Id	ceae42bfc83436ff8dc1
Client Secret	c87eb4fbf6398075deaeab360a855a9e
'''

import requests
import json

client_id = 'ceae42bfc83436ff8dc1'
client_secret = 'c87eb4fbf6398075deaeab360a855a9e'
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
headers = {"X-Xapp-Token": json.loads(r.text)["token"]}

id = '4d8b92b34eb68a1b2c0003f4'
artInf = open("dataset_24476_4 (1).txt").read().splitlines()
outF = open("output.txt", "w", encoding="UTF-8")
# artList = open("input_task_03_18.txt").read().splitlines()
artList = []
for id in artInf:
    req = requests.get(r'https://api.artsy.net/api/artists/{}'.format(id), headers=headers).json()
    artList.append((int(req["birthday"]), req["sortable_name"]))
    print(artList[-1])
    # print(requests.get(r'https://api.artsy.net/api/artists/{}'.format(id), headers=headers).json()["sortable_name"], file=outF)
outF.close()
print("------------------")
print(*(art[1] for art in sorted(artList)), sep="\n")



'''
token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTUwNTY4NDUxMywiaWF0IjoxNTA1MDc5NzEzLCJhdWQiOiI1OWI1YjFhMTI3NWIyNDE5YzM2NzNlMTYiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNTliNWIxYTE4YjNiODE1NmIwOTgwMzAzIn0.2yBP3_wfpBhvOsdlWHmmHI-PJ15NndWjlSmpBagigUo
'''

'''
{
  "id": "4d8b92b34eb68a1b2c0003f4",
  "slug": "andy-warhol",
  "created_at": "2010-08-23T14:15:30+00:00",
  "updated_at": "2017-09-10T21:42:09+00:00",
  "name": "Andy Warhol",
  "sortable_name": "Warhol Andy",
  "gender": "male",
  "birthday": "1928",
  "hometown": "Pittsburgh, Pennsylvania",
  "location": "New York, New York",
  "nationality": "American",
  "image_versions": [
    "four_thirds",
    "large",
    "square",
    "tall"
  ],
  "_links": {
    "thumbnail": {
      "href": "https://d32dm0rphc51dk.cloudfront.net/PFufT6nMKNwLOpPEezf4Ww/four_thirds.jpg"
    },
    "image": {
      "href": "https://d32dm0rphc51dk.cloudfront.net/PFufT6nMKNwLOpPEezf4Ww/{image_version}.jpg",
      "templated": true
    },
    "self": {
      "href": "https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4"
    },
    "permalink": {
      "href": "http://www.artsy.net/artist/andy-warhol"
    },
    "artworks": {
      "href": "https://api.artsy.net/api/artworks?artist_id=4d8b92b34eb68a1b2c0003f4"
    },
    "published_artworks": {
      "href": "https://api.artsy.net/api/artworks?artist_id=4d8b92b34eb68a1b2c0003f4&published=true"
    },
    "similar_artists": {
      "href": "https://api.artsy.net/api/artists?similar_to_artist_id=4d8b92b34eb68a1b2c0003f4"
    },
    "similar_contemporary_artists": {
      "href": "https://api.artsy.net/api/artists?similar_to_artist_id=4d8b92b34eb68a1b2c0003f4&similarity_type=contemporary"
    },
    "genes": {
      "href": "https://api.artsy.net/api/genes?artist_id=4d8b92b34eb68a1b2c0003f4"
    }
  }
}
'''

'''
Если вы делаете запрос при помощи requests, то подключать библиотеку json не обязательно. requests умеет представлять данные в json.
Например:
response = requests.get('site.com/well/return/response/in/json').json()
Если при этом запросе возвращаются данные в json, то в response они корректно запишутся.
'''

'''
import requests
list_art = []  # список будущих ответов
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",  # инициируем запрос на получение токена
                  data={
                      "client_id": '...........',   # наш client_id
                      "client_secret": '.........'  # наш client_secret
                  })
headers = {"X-Xapp-Token": r.json()["token"]}  # создаем заголовок, содержащий наш токен
with open("dataset_24476_4.txt") as f:  # открываем файл
    for art in f:  # считываем id художников построчно с файла
        r = requests.get("https://api.artsy.net/api/artists/"+art.strip(), headers=headers)  # инициируем запрос
        list_art.append((r.json()["birthday"] + r.json()["sortable_name"]))  #вытягиваем в список то что нам ﻿надо
[print(i[4:])for i in sorted(list_art)]
'''

'''
output = {}
with open('dataset_24476_4.txt', 'r') as f:
    data = f.read().strip().split()
for i in data:
    r = requests.get("https://api.artsy.net/api/artists/{}".format(i), headers=headers)
    output[r.json()['sortable_name']] = r.json()["birthday"]

with open('artists_out.txt', 'w+', encoding='utf-8') as fw:
    for i in sorted(output.items(), key=lambda x: x[1]):
        fw.write(i[0]+'\n')
'''
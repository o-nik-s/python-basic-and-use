# API

# API будет описывать предоставляемую нам функциональность.

# Например, мы знаем, что стандартная библиотека Пайтон предоставляет нам функциональность для работы с файлами.

# Например, есть функция open. Мы знаем, как она работает.
# Таким образом Пацтон предлагает нам API для работы с файлами.

# Так же API предлагает нам возможность абстрагироваться от реализации. Мы можем не знать отличия файловых систем,
# как работает Виндовс и Линукс, однако API все равно откроет файл для работы.

# Таким образом, API какого-нибудь модуля или сервиса - это набор функций, констант, методов, которые мы можем использовать,
# и при этом про каждую из них прежде всего известно, что она принимает, что она возвращает, что она должна делать,
# но при этом может быть неизвестно, как она это делает.

# Мы будет рассматривать Web API


# Мы рассмотрим Open API на примере OpenWeatherMap, предоставляюшего информацию о погоде в разных точнках планеты.
# openweathermap.org/api

# Почти все сервисы, предоставляющие API, запрашивают API-ключ

# Ключ: 11c0d3dc6093f7442898ee49d2430d20

# Хотим, чтобы программа считывала из стандартного ввода город, и затем программа выводила погоду в данном городе.

import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("City? ")

params = {
    'q': city,
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
print(res.status_code)
print(res.headers["Content-Type"])
print(res.json())  # returns json.loads(res.text) :)

data = res.json()
template = 'Current temperature in {} is {}'
print(template.format(city, data["main"]["temp"]))

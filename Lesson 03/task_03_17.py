'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true
'''

import requests

params = {
    'json': 'true'
}

with open("input_task_03_17.txt", 'r') as inpF, open("output_task_03_17.txt", 'w') as outF:
# with open("dataset_24476_3.txt", 'r') as inpF, open("output_task_03_17.txt", 'w') as outF:
    for line in inpF:
        number = int(line.strip())
        api_url = "http://numbersapi.com/" + str(number) + "/math"

        res = requests.get(api_url, params=params)
        # print(res.url)
        # print(res.status_code)
        # print(res.headers["Content-Type"])
        # print(res.text)
        # print(res.json())  # returns json.loads(res.text) :)

        data = res.json()
        # print(data)
        print('Interesting' if data['found'] else 'Boring', file=outF)
        print('Interesting' if data['found'] else 'Boring')

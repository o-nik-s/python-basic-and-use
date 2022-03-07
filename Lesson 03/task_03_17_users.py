# author

import requests
import json

def is_interesting(x):
    url = "http://numbersapi.com/"; + str(x) + "/math?json=true"
    resp = requests.get(url).text
    js = json.loads(resp)
    return js["found"]

with open("input.txt") as fi:
    for line in fi:
        print("Interesting" if is_interesting(line.rstrip()) else "Boring")



import requests as re

with open('dataset_24476_3.txt') as file:
    for num in file:
        response = re.get('http://numbersapi.com/{number}/math?json=true'.format( number=num.rstrip() )).json()
        print('Interesting') if response['found'] else print('Boring')


import requests

with open("dataset_24476_3.txt", "r") as rf:
    for line in rf:
        print("Interesting" if requests.get("http://numbersapi.com/{}/math?json=true".format(line.strip())).json()[
            "found"] else "Boring")


import requests

with open('dataset_24476_3.txt') as f:
    for line in f:
        r = requests.get('http://numbersapi.com/' + line.strip() + '/math?json=true')
        print('Interesting' if r.json()['found'] else 'Boring')


import requests
import json

url = "http://numbersapi.com/{}/math"
with open("input.txt") as f:
    for row in f:
        data = requests.get(url.format(row.rstrip()), params={'json': True}).text
        print("Interesting" if json.loads(data)['found'] else "Boring")


url = "http://numbersapi.com/%s/math?json=true"

with open("in.txt") as f, open("out.txt","w") as outf:
    for line in f:
        data = requests.get(url % line.strip()).json()
        outf.write("Interesting\n" if data["found"] else "Boring\n")


import requests, json

lst = open('dataset_24476_3.txt').read().splitlines()
for digit in lst:
    text = requests.get(r'http://numbersapi.com/{}/math'.format(digit), {'json': True}).text
    print('Interesting' if bool(json.loads(text)['found']) else 'Boring')

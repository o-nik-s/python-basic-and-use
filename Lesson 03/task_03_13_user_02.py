import requests
import re

def test(a, b):
    for f in re.findall(r'<a href="(.*)">', requests.get(a).text):
        if b in re.findall(r'<a href="(.*)">', requests.get(f).text):
            return 'Yes'
    return 'No'

print(test(input(), input()))

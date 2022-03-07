import requests
import re


def finder(texts):  # поиск интернет адресов
    result_url = re.findall(r".*<a href=\"(.*)\"\>[\d]</a>", requests.get(texts).text)
    return result_url


def listing(list_url):  # перебор адресов по списку
    for line in list_url:
        find_requests = finder(line)
        for line2 in find_requests:
            if line2 == reference_B:
                return "Yes"
    return "No"
reference_A, reference_B = input(), input()  # стандартный ввод двух интернет адресов
print(listing(finder(reference_A)))  # результат поиска

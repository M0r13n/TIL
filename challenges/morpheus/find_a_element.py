import json
import requests

LINK_UNSORTED = 'https://cc.the-morpheus.de/challenges/2/'
LINK_SORTED = 'https://cc.the-morpheus.de/challenges/2/sorted/'
SOLUTION = 'https://cc.the-morpheus.de/solutions/2/'


def get(link):
    content = requests.get(link).json()
    return content['k'], content['list']


def post(link, index):
    r = requests.post(link, json.dumps({'token': index}))
    print(r.status_code, r.reason, r.text)


def find_unsorted():
    element, data = get(LINK_UNSORTED)
    # find searched element
    for i in range(len(data)):
        if data[i] == element:
            return i


def find_sorted():
    element, data = get(LINK_SORTED)
    return binary_search(data, element, 0, len(data))


def binary_search(data, searched, lower, upper):
    if upper < lower:
        return -1
    middle = int((lower + upper) / 2)
    if data[middle] == searched:
        return middle
    elif data[middle] < searched:
        return binary_search(data, searched, middle + 1, upper)
    else:
        return binary_search(data, searched, lower, middle - 1)


post(SOLUTION, find_unsorted())
post(SOLUTION, find_sorted())

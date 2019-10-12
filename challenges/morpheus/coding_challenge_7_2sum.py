import json
import requests

Q_LINK = 'https://cc.the-morpheus.de/challenges/7/'
S_LINK = 'https://cc.the-morpheus.de/solutions/7/'


def get() -> str:
    content = requests.get(Q_LINK).json()
    return content


def post(a, b):
    r = requests.post(S_LINK, json={'token': [a, b]})
    print([a, b], r.status_code, r.reason, r.text)


def solution_2sum(k, numbers):
    # lookup time in dict is O(1)
    table = {}
    i = 0
    l = len(numbers)
    # max O(n) iterations
    while i < l:
        n = numbers[i]
        diff = k - n

        if diff in table:
            return table[diff], i
        if n not in table:
            table.update({n: i})
        i += 1


task = get()
post(*solution_2sum(task['k'], task['list']))

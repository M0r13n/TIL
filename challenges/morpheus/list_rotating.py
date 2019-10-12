import json
import requests

LINK = 'https://cc.the-morpheus.de/challenges/4/'
LINK_POST = 'https://cc.the-morpheus.de/solutions/4/'


def get():
    content = requests.get(LINK).json()
    return content


def post(data):
    r = requests.post(LINK_POST, json.dumps({'token': data}))
    print(r.status_code, r.reason, r.text)


def rotate(list, k):
    length = len(list)
    k = k % length
    rotated_list = [0] * length

    for i in range(length):
        new_index = (i + k) % length
        rotated_list[new_index] = list[i]
    return rotated_list


content = get()
list = content['list']
k = content['k']
post(rotate(list, k))

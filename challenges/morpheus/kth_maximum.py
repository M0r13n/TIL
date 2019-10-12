import json
import requests

LINK = 'https://cc.the-morpheus.de/challenges/3/'
LINK_POST = 'https://cc.the-morpheus.de/solutions/3/'


def get():
    content = requests.get(LINK).json()
    return content['k'], content['list']


def post(kth_item):
    r = requests.post(LINK_POST, json.dumps({'token': kth_item}))
    print(r.status_code, r.reason, r.text)


def kth_maximum():
    k, data = get()
    data = mergesort(data)
    post(data[len(data)-k])


def mergesort(array):
    if len(array) <= 1:
        return array

    middle = int(len(array) // 2)
    left_array = mergesort(array[0:middle])
    right_array = mergesort(array[middle::])
    return merge(left_array, right_array)


def merge(left_array, right_array):
    array = []
    left_array_length = len(left_array)
    right_array_length = len(right_array)

    left_pointer = 0
    right_pointer = 0

    # iterate over both lists until either one of both lists is empty
    while left_pointer < left_array_length and right_pointer < right_array_length:
        # append smallest item to final array
        if left_array[left_pointer] <= right_array[right_pointer]:
            array.append(left_array[left_pointer])
            left_pointer += 1
        else:
            array.append(right_array[right_pointer])
            right_pointer += 1

    # add remaining items of either left_array or right_array
    for item in left_array[left_pointer::]:
        array.append(item)

    for item in right_array[right_pointer::]:
        array.append(item)

    return array


kth_maximum()

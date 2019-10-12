import requests

LINK = 'https://cc.the-morpheus.de/challenges/6/'
LINK_POST = 'https://cc.the-morpheus.de/solutions/6/'


def get() -> str:
    content = requests.get(LINK).text
    return content


def post(solution):
    r = requests.post(LINK_POST, json={'token': solution})
    print(solution, r.status_code, r.reason, r.text)


def dec2bin(decimal):
    """
    convert decimal to binary
    :param decimal: decimal number
    :return: binary representation if provided decimal
    """
    decimal = int(decimal)
    binary = ""

    while decimal > 1:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2  # floor dívision

    if decimal % 2 == 1:
        binary = str(1) + binary

    return binary


post(dec2bin(get()))

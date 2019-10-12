import json
import requests

LINK = 'https://cc.the-morpheus.de/challenges/5/'
LINK_POST = 'https://cc.the-morpheus.de/solutions/5/'


def get() -> str:
    content = requests.get(LINK).text
    return content


def post(solution):
    r = requests.post(LINK_POST, json.dumps({'token': int(solution)}))
    print(r.status_code, r.reason, r.text)


def is_operand(k: str) -> bool:
    return k.isdigit()


def is_operator(k: str) -> bool:
    return k in ('+', '-', '*', '/')


def calc(x, y, op) -> int:
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    # assert op is an valid operator
    return x / y


def evaluate_postfix(postfix_notation: str):
    """my idea is to push every operand to a stack until we hit a operator.
    in this case we start to evaluate the term backwards"""

    operand_stack = []

    postfix_notation = postfix_notation.split()

    for k in postfix_notation:
        if is_operand(k):
            operand_stack.append(k)
        elif is_operator(k):
            x = float(operand_stack.pop())
            y = float(operand_stack.pop())
            operator = k
            r = calc(y, x, operator)  # swap
            operand_stack.append(r)

        else:
            raise ValueError('invalid element')

    return operand_stack[0]


for i in range(20):
    post(evaluate_postfix(get()))

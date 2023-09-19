# https://contest.yandex.ru/contest/27393/enter/

import re

def prepare_number(number: str):
    number = re.sub(r"[-()]", "", number)
    city_code = "495"; num_len = len(number)

    if number[0] == "+": number = number[2:]
    elif number[0] == "8" and (num_len == 11 or num_len == 8):
        number = number[1:]

    if len(number) > 7:
        city_code = number[:3]; number = number[3:]

    return city_code, number

def decision(code, number, wish_code, wish_num):
    return "NO" if code != wish_code or number != wish_num else "YES"


wish_code, wish_num = prepare_number(input())

for _ in range(3):
    code, number = prepare_number(input())
    print(decision(code, number, wish_code, wish_num))

# https://contest.yandex.ru/contest/50668/enter
#Volozh,Arcady,Yurievich,11,2,1964

from string import ascii_uppercase

def solve(people):
    res = []

    for person in people:
        last_name, first_name, middle_name, *birthday = person
        count_different_chr_FIO = len({*last_name, *first_name, *middle_name})
        sum_digit_birthday = sum(map(int, birthday[0]+birthday[1])) * 64
        number_in_alphabet = (ascii_uppercase.find(last_name[0].upper()) + 1) * 256
        sums = count_different_chr_FIO + sum_digit_birthday + number_in_alphabet
        result = hex(sums).upper(); n = len(result)

        if n == 1: res.append(f'00{result}')
        elif n == 2: res.append(f'0{result}')
        else: result = res.append(result[-3:])

    return res


people = [input().split(',') for _ in range(int(input()))]

print(*solve(people))

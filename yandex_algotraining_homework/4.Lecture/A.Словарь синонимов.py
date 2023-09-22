# https://contest.yandex.ru/contest/27665/enter/

def solve(n):
    d = {}

    for _ in range(n):
        key, val = input().split(); d[key] = val; d[val] = key

    return d[input()]

n = int(input())

print(solve(n))

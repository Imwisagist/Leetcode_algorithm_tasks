# https://contest.yandex.ru/contest/27472/enter/

def solve(n, numbers, target):
    if target in numbers: return target

    min_ = abs(numbers[0] - target)
    res = numbers[0]

    for num in numbers:
        if abs(num - target) < min_:
            min_ = abs(num - target)
            res = num

    return res


n = input()
numbers = list(map(int, input().split()))
target = int(input())

print(solve(n, numbers, target))

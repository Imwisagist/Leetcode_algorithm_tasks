# https://contest.yandex.ru/contest/27472/enter/

def solve(numbers):
    cnt = 0; prev = prev_prev = None

    for num in numbers:
        if not prev_prev is None:
            if prev_prev < prev > num: cnt += 1

        prev_prev = prev; prev = num

    return cnt


numbers = list(map(int, input().split()))

print(solve(numbers))

# https://contest.yandex.ru/contest/8458/

cur = best = 0

for i in range(int(input())):
    num = int(input())

    if num: cur += 1; best = max(cur,best)
    else: cur = 0

print(best)

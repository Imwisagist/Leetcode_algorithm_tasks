# https://contest.yandex.ru/contest/8458/

jewelry = set(input())

print(sum(1 for i in input() if i in jewelry))

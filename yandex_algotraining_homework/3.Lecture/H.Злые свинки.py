# https://contest.yandex.ru/contest/27663/enter/

def solve(birds): return len(set(birds))


birds = [int(input().split()[0]) for _ in range(int(input()))]

print(solve(birds))

# https://contest.yandex.ru/contest/27663/enter/

def solve(scoolboys):
    almost_one_known = set().union(*scoolboys)
    all_known = set(scoolboys[0]).intersection(*scoolboys)

    return len(all_known), *all_known, len(almost_one_known), *almost_one_known


n = int(input())
scoolboys = [set(input() for _ in range(int(input()))) for _ in range(n)]

print(*solve(scoolboys), sep="\n")

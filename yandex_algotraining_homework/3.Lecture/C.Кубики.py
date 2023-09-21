# https://contest.yandex.ru/contest/27663/enter/

def solve(anya, borya): 
    intersection = anya & borya
    length = len(intersection)
    print(length); print(*sorted(intersection))
    print(len(anya) - length)
    print(*sorted(anya - intersection))
    print(len(borya) - length)
    print(*sorted(borya - intersection))


n, m = map(int,input().split())
anya = set(int(input()) for _ in range(n))
borya = set(int(input()) for _ in range(m))

solve(anya, borya)

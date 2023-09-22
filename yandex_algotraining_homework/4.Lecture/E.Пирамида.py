# https://contest.yandex.ru/contest/27665/enter/

def solve(n):
    d = {}; d_get = d.get

    for _ in range(n):
        block_w, block_h = map(int, input().split())

        if d_get(block_w,0) < block_h: d[block_w] = block_h

    return sum(d.values())


print(solve(int(input())))

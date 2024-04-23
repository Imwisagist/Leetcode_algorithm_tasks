# https://contest.yandex.ru/contest/60243/problems/B/

from collections import deque


def solution():
    n, k = map(int, input().split())
    c = map(int, input().split())
    r, dq, cnt = 0, deque(), [0]*n

    for i, v in enumerate(c):
        while dq and dq[0][1] <= i - k: dq.popleft()
        while dq and dq[-1][0] >= v: dq.pop()

        dq.append((v, i))
        r += dq[0][0]
        cnt[dq[0][1]] += 1

    return r, " ".join(map(str, cnt))


print(*solution(), sep="\n")

# https://contest.yandex.ru/contest/60243/problems/A/


def check_continuity(arr: list) -> bool:
    cnt: int = 0

    for v in arr:
        if v == 1: cnt += 1
        else: cnt = 0
        if cnt == 5: return True

    return False


def check_win(x: int, y: int, p: dict) -> bool:
    l1, l2, l3, l4 = [], [], [], []

    for i in range(-4, 5):
        if (x, y + i) in p and p[x, y + i] == p[x, y]: l1.append(1)
        else: l1.append(0)
        if (x + i, y) in p and p[x + i, y] == p[x, y]: l2.append(1)
        else: l2.append(0)
        if (x + i, y + i) in p and p[x + i, y + i] == p[x, y]: l3.append(1)
        else: l3.append(0)
        if (x - i, y + i) in p and p[x - i, y + i] == p[x, y]: l4.append(1)
        else: l4.append(0)

    if check_continuity(l1) or check_continuity(l2) or check_continuity(l3) or check_continuity(l4): return True
    else: return False


def solution(n: int) -> str:
    p: dict = {}

    for i in range(n):
        x, y = map(int, input().split())
        p[x, y] = i % 2

        if check_win(x, y, p) and i == n - 1:
            if i % 2 == 0: return "First"
            else: return "Second"

        elif check_win(x, y, p): return "Inattention"

    return "Draw"


print(solution(int(input())))

# https://contest.yandex.ru/contest/27665/enter/

def solve(endurances, pushes):
    d = {}; d_get = d.get

    for btn_push_num in pushes:
        d[btn_push_num] = d_get(btn_push_num,0) + 1

    for idx, endurance in enumerate(endurances,1):
        print("YES" if d[idx] > endurance else "NO")
    

n = int(input()); endurances = map(int, input().split())
k = int(input()); pushes = map(int, input().split())

solve(endurances, pushes)

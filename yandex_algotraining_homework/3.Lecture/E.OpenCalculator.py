# https://contest.yandex.ru/contest/27663/enter/

def solve(buttons, target): 
    return len(set(map(int, str(target))) - buttons)


buttons = set(map(int,input().split()))
target = int(input())

print(solve(buttons, target))

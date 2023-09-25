# https://contest.yandex.ru/contest/27472/enter/

def solve(arr):
    prev = ""

    for i in arr:
        if i <= prev: return "NO"
        
        prev = i

    return "YES"


arr = input().split()

print(solve(arr))

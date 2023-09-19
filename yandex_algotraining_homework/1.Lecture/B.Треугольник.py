# https://contest.yandex.ru/contest/27393/enter/

def decision(x,y,z,m):
    return "YES" if (sum((x, y, z)) - m) > m else "NO"

x, y, z = int(input()), int(input()), int(input())
m = max(x, y, z)

print(decision(x,y,z,m))

# https://contest.yandex.ru/contest/27393/enter/

def decision(a, b, c, d, e):
    if a > b: a, b = b, a
    
    if b > c:
        b, c = c, b

        if a > b: a, b, = b, a

    if d > e: d, e = e, d

    return "YES" if a <= d and b <= e else "NO"


a, b, c, d, e = (int(input()) for _ in range(5))

print(decision(a, b, c, d, e))

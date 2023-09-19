# https://contest.yandex.ru/contest/27393/enter/

def decision(a, b, n, m):
    min1 = a * (n - 1) + n; max1 = min1 + 2*a
    min2 = b * (m - 1) + m; max2 = min2 + 2*b
    min_time, max_time = max(min1,min2), min(max1,max2)

    if min_time > max_time: return "-1"

    return f"{min_time} {max_time}"


a, b, n, m = (int(input()) for _ in range(4))

print(decision(a, b, n, m))

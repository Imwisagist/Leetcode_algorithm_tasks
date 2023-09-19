# https://contest.yandex.ru/contest/27393/enter/

def decision(x1, y1, x2, y2):
    variants = (
        max(x1, x2) * (y1 + y2), max(x1, y2) * (y1 + x2),
        max(y1, x2) * (x1 + y2), max(y1, y2) * (x1 + x2),
    )

    min_area = min(variants)

    if min_area == variants[0]: return max(x1, x2), y1 + y2
    elif min_area == variants[1]: return max(x1, y2), y1 + x2
    elif min_area == variants[2]: return max(y1, x2), x1 + y2
    else: return max(y1, y2), x1 + x2


x1, y1, x2, y2 = map(int, input().split())

print(*decision(x1, y1, x2, y2))

# https://contest.yandex.ru/contest/27663/enter/

def extend(rect, d):
    min_add, max_add, min_sub, max_sub = rect

    return [min_add - d, max_add + d, min_sub - d, max_sub + d]

def intersect(r1, r2):
    return [
        max(r1[0], r2[0]), min(r1[1], r2[1]),
        max(r1[2], r2[2]), min(r1[3], r2[3]),
    ]

def solve(t, d, n):
    pos_rect = (0,0,0,0)

    for _ in range(n):
        pos_rect = extend(pos_rect, t); nav_x, nav_y = map(int, input().split())
        nav_rect = extend((nav_x + nav_y,nav_x + nav_y,nav_x - nav_y,nav_x - nav_y), d)
        pos_rect = intersect(pos_rect, nav_rect)
    
    return [
        ((x_add_y + x_sub_y) // 2, x_add_y - (x_add_y + x_sub_y) // 2) 
        for x_add_y in range(pos_rect[0], pos_rect[1] + 1) 
        for x_sub_y in range(pos_rect[2], pos_rect[3] + 1) 
        if (x_add_y + x_sub_y) % 2 == 0
    ]


t, d, n = map(int, input().split())
result = solve(t, d, n)

print(len(result))
for coords in result: print(*coords)

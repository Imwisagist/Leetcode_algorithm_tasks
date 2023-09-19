# https://contest.yandex.ru/contest/27393/enter/

def decision(n, k, m):
    if k < m: return 0

    cnt = 0
    parts_from_wp, parts_metall_remain = divmod(k, m)

    while n >= k:
        workpiece, wp_metall_remain = divmod(n,k)
        cnt += parts_from_wp * workpiece
        n = wp_metall_remain + (workpiece * parts_metall_remain)

    return cnt


n, k, m = map(int, input().split())

print(decision(n, k, m))

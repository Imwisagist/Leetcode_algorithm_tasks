# https://contest.yandex.ru/contest/60243/problems/C/


distances = [[0] * 100 for _ in range(100)]
query_u, query_v, query_t, query_price = [], [], [], []
condition_a, condition_b, condition_t = [], [], []


def check_reachability(max_price: int) -> bool:
    floyd = [[0] * 100 for _ in range(100)]

    for i in range(nodes):
        for j in range(nodes): floyd[i][j] = distances[i][j]

    for i in range(queries):
        if query_price[i] <= max_price:
            floyd[query_u[i]][query_v[i]] = query_t[i]
            floyd[query_v[i]][query_u[i]] = query_t[i]

    for t in range(nodes):
        for i in range(nodes):
            for j in range(nodes): floyd[i][j] = min(floyd[i][j], floyd[i][t] + floyd[t][j])

    for i in range(conditions):
        if floyd[condition_a[i]][condition_b[i]] > condition_t[i]: return False

    return True


def solution():
    global nodes, edges, queries, conditions
    nodes, edges = map(int, input().split())

    for i in range(nodes):
        for j in range(nodes):
            if i == j: continue

            distances[i][j] = float("inf")

    for _ in range(edges):
        u, v, t = map(int, input().split())
        u -= 1; v -= 1; distances[u][v] = distances[v][u] = t

    queries = int(input())

    for _ in range(queries):
        u, v, t, c = map(int, input().split())
        u -= 1; v -= 1; query_u.append(u); query_v.append(v); query_t.append(t); query_price.append(c)

    conditions = int(input())

    for _ in range(conditions):
        a, b, t = map(int, input().split())
        a -= 1; b -= 1; condition_a.append(a); condition_b.append(b); condition_t.append(t)

    l, h, ans = 0, int(1e9), -1

    while l <= h:
        m = (l + h) // 2

        if check_reachability(m):
            h = m - 1; ans = m
        else: l = m + 1

    proposals = [i + 1 for i in range(queries) if query_price[i] <= ans]

    return ans if ans == -1 else len(proposals), " ".join(map(str, proposals))


print(*solution(), sep="\n")

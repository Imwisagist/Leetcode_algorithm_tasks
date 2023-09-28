# https://contest.yandex.ru/contest/51022/enter/

n,m,q = map(int, input().split())
d = {}; s = input().split()
table = [tuple(map(int,input().split())) for _ in range(n)]

for i in range(m): d[s[i]] = [i,-float('inf'),float('inf')]

for _ in range(q):
    chr,operator,val = input().split(); val = int(val)

    if operator == '>':
        if d[chr][1] < val: d[chr][1] = val
    else:
        if d[chr][2] > val: d[chr][2] = val

print(
    sum(sum(table[i]) 
    for i in range(n) 
    if all(
        d[s[j]][1] < table[i][j] < d[s[j]][2] 
        for j in range(m)
    ))
)

# https://contest.yandex.ru/contest/27665/enter/

from collections import Counter

def modif_counter(cur, target, chr, count):
    cnt = 0

    if cur.get(chr, 0) == target.get(chr, None): cnt = -1
    
    cur[chr] += count

    if cur[chr] == target.get(chr, None): cnt = 1

    return cnt

def solve(g, ls, sub_s, s):
    cur,target = Counter(s[:len(sub_s)]),Counter(sub_s); c,n = 0,len(target)
    matching_letters = sum(1 for chr in target if target[chr] == cur.get(chr, None))

    if cur == target: c += 1

    for i in range(g, ls):
        matching_letters += modif_counter(cur, target, s[i - g], -1)
        matching_letters += modif_counter(cur, target, s[i], 1)

        if matching_letters == n: c += 1

    return c


g, ls = map(int, input().split()); sub_s, s = input(), input()

print(solve(g, ls, sub_s, s))

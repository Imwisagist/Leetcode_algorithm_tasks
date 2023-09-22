# https://contest.yandex.ru/contest/27665/enter/

import sys

def solve(words):
    d, res = {}, []

    for word in words.split(): 
        if word in d: d[word] += 1; res.append(d[word])
        else: d[word] = 0; res.append(0)

    return res
    

words = sys.stdin.read()

print(*solve(words))

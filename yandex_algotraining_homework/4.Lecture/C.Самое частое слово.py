# https://contest.yandex.ru/contest/27665/enter/

import sys

def solve(words):
    d, m, res = {}, 0, "ÿ"; d_get = d.get

    for word in words.split():
        val = d_get(word,0) + 1; d[word] = val

        if val > m: m = val

    for word, count in d.items():
        if count == m: res = min(res, word)

    return res
    

words = sys.stdin.read()

print(solve(words))

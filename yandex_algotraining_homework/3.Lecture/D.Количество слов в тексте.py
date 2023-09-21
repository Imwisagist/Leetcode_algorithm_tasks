# https://contest.yandex.ru/contest/27663/enter/

import sys

def solve(words): return len(set(words.split()))


words = sys.stdin.read()

print(solve(words))

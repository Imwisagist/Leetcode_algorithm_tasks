# https://leetcode.com/problems/minimum-window-substring/description/
from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    n, needcnt = len(s), len(t)

    if n < needcnt: return ""

    d, res, start = defaultdict(int), (0, float('inf')), 0

    for ch in t: d[ch] += 1

    for end, ch in enumerate(s):
        if d[ch] > 0: needcnt -= 1

        d[ch] -= 1

        if needcnt == 0:
            while True:
                tmp = s[start]

                if d[tmp] == 0: break

                d[tmp] += 1; start += 1

            if end - start < res[1] - res[0]: res = (start, end)

            d[s[start]] += 1; needcnt += 1; start += 1

    return '' if res[1] > n else s[res[0]:res[1] + 1]


assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert minWindow("a", "a") == "a"
assert minWindow("a", "aa") == ""

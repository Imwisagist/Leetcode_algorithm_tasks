# https://leetcode.com/problems/minimum-window-substring/description/
from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    n, needcnt = len(s), len(t)

    if n < needcnt: return ""

    d, res, left = defaultdict(int), (0, float('inf')), 0

    for ch in t: d[ch] += 1

    for right, ch in enumerate(s):
        if d.get(ch, 0) > 0: needcnt -= 1

        d[ch] -= 1

        if not needcnt:
            while True:
                tmp = s[left]

                if d[tmp] == 0: break

                d[tmp] += 1; left += 1

            if right - left < res[1] - res[0]: res = (left, right)

            d[s[left]] += 1; needcnt += 1; left += 1

    return '' if res[1] > n else s[res[0]:res[1] + 1]


assert minWindow("FDOBECODEBANC", "ABC") == "BANC"
assert minWindow("a", "a") == "a"
assert minWindow("a", "aa") == ""

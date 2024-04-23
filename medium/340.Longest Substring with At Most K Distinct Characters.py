# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
from collections import defaultdict


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    l, r, d, n, res = 0, 1, defaultdict(int), len(s), 0

    if k == 0: return 0
    if n == 1: return 1

    d[s[l]] += 1

    while r < n:
        d[s[r]] += 1

        while len(d.keys()) > k:
            if d[s[l]] == 1: d.pop(s[l])
            else: d[s[l]] -= 1
            l += 1

        r += 1
        res = max(res, r - l)

    return res


assert lengthOfLongestSubstringKDistinct("eceba", 2) == 3
assert lengthOfLongestSubstringKDistinct("aa", 1) == 2
# https://leetcode.com/problems/permutation-in-string/description/
from collections import defaultdict


def checkInclusion(s1: str, s2: str) -> bool:
    d1, d2, n1, n2 = defaultdict(int), defaultdict(int), len(s1), len(s2)
    l, r = 0, n1 - 1

    if n1 > n2: return False

    for char in s1: d1[char] += 1
    for char in s2[:r]: d2[char] += 1

    while r < n2:
        d2[s2[r]] += 1
        char = s2[l]

        if d1 == d2: return True
        if d2[char] == 1: d2.pop(char)
        else: d2[char] -= 1

        l += 1
        r += 1

    return False


assert checkInclusion("a", "a") is True
assert checkInclusion("ab", "eidbaooo") is True
assert checkInclusion("ab", "eidboaoo") is False
assert checkInclusion("abc", "ab") is False

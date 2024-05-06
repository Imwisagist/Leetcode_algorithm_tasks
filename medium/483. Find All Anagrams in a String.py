# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
from typing import List
from collections import defaultdict


def findAnagrams(s: str, p: str) -> List[int]:
    l, r, n, res, d1, d2 = 0, len(p)-1, len(s), [], defaultdict(int), defaultdict(int)

    for i in s[:r]: d1[i] += 1
    for i in p: d2[i] += 1

    for j in range(r, n):
        d1[s[j]] += 1

        if d1 == d2: res.append(l)

        left_chr = s[l]

        if d1[left_chr] == 1: del d1[left_chr]
        else: d1[left_chr] -= 1

        l += 1

    return res


assert findAnagrams("cbaebabacd", "abc") == [0, 6]
assert findAnagrams("abab", "ab") == [0, 1, 2]

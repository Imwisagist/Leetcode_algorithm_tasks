# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/

from typing import List


def findArray(pref: List[int]) -> List[int]:
    return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]


assert findArray([5, 2, 0, 3, 1]) == [5, 7, 2, 3, 2]
assert findArray([13]) == [13]

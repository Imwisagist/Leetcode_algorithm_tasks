# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
from collections import Counter
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    d1, d2, res = Counter(), Counter(), []

    for i in nums1: d1[i] += 1
    for i in nums2: d2[i] += 1
    for key in d1 & d2: res += [key] * min(d1[key], d2[key])

    return res


assert intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
assert intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]

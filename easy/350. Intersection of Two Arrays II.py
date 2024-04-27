# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
from collections import defaultdict, Counter
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    d1, d2, res = Counter(), Counter(), []

    for i in nums1: d1[i] += 1
    for i in nums2: d2[i] += 1
    for key in d1 & d2: res += [key] * min(d1[key], d2[key])

    return res
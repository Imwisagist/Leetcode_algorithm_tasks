# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/description/

from typing import List

def minNumber(nums1: List[int], nums2: List[int]) -> int:
    s1, s2 = set(nums1), set(nums2)
    m1, m2 = min(s1), min(s2); intersect = s1 & s2

    if intersect: min_inter = min(intersect)
    else:
        if m1 < m2: return m1*10 + m2
        else: return m2*10 + m1

    if m1 < m2: smallest = m1*10 + m2
    else: smallest = m2*10 + m1

    return min_inter if min_inter < smallest else smallest


assert minNumber([4,1,3],[5,7]) == 15
assert minNumber([3,5,2,6],[3,1,7]) == 3

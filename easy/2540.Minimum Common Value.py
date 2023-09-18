# https://leetcode.com/problems/minimum-common-value/

from typing import List

def getCommon(nums1: List[int], nums2: List[int]) -> int:
    n1, n2, l, r = len(nums1), len(nums2), 0, 0

    while l < n1 and r < n2:
        left, right = nums1[l], nums2[r]
        
        if left == right: return left
        elif left > right: r += 1
        else: l += 1
    
    return -1


assert getCommon([1,2,3],[2,4]) == 2
assert getCommon([1,2,3,6],[2,3,4,5]) == 2

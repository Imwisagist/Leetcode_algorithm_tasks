# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

from typing import List

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    nums1, nums2 = set(nums1), set(nums2)

    return [list(nums1 - nums2), list(nums2 - nums1)]

assert findDifference([1,2,3], [2,4,6]) == [[1,3],[4,6]]
assert findDifference([1,2,3,3], [1,1,2,2]) == [[3],[]]

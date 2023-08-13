# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))


assert intersection([1,2,2,1],[2,2]) == [2]
assert intersection([4,9,5],[9,4,9,8,4]) == [9,4]

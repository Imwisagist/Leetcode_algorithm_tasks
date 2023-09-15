# https://leetcode.com/problems/two-out-of-three/description/

from typing import List

def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    s1, s2, s3 = set(nums1), set(nums2), set(nums3)

    return s1 & s2 | s1 & s3 | s2 & s3


assert twoOutOfThree([1,1,3,2],[2,3],[3]) == [3,2] or {2,3}
assert twoOutOfThree([3,1],[2,3],[1,2]) == [2,3,1] or {1,2,3}

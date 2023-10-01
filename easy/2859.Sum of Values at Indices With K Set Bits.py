# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/

from typing import List

def sumIndicesWithKSetBits(nums: List[int], k: int) -> int:
    return sum(nums[i] for i in range(len(nums)) if i.bit_count() == k)


assert sumIndicesWithKSetBits([5,10,1,5,2],1) == 13
assert sumIndicesWithKSetBits([4,3,2,1],2) == 1

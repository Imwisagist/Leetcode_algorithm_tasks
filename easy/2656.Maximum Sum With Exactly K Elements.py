# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

from typing import List

def maximizeSum(nums: List[int], k: int) -> int:
    return k * (2*max(nums)+k-1) // 2


assert maximizeSum([1,2,3,4,5],3) == 18
assert maximizeSum([5,5,5],2) == 11

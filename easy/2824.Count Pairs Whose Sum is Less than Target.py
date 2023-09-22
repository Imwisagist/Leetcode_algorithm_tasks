# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

from typing import List

def countPairs(nums: List[int], target: int) -> int:
    return sum(
        1
        for i in range(len(nums)) 
        for j in range(i+1, len(nums)) 
        if nums[i] + nums[j] < target
    )


assert countPairs([-1,1,2,3,1],2) == 3
assert countPairs([-6,2,5,-2,-7,-1,3],-2) == 10

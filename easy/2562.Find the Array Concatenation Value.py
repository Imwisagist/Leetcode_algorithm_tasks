# https://leetcode.com/problems/find-the-array-concatenation-value/description/

from typing import List

def findTheArrayConcVal(nums: List[int]) -> int:
    l, r, m, res = 0, len(nums) - 1, 0, 0

    if r % 2 == 0: m = r // 2
    
    if r == 0: return nums[0]

    while l < r: res += int(str(nums[l]) + str(nums[r])); l += 1; r -= 1

    if m: res += nums[m]

    return res


assert findTheArrayConcVal([7,52,2,4]) == 596
assert findTheArrayConcVal([5,14,13,8,12]) == 673

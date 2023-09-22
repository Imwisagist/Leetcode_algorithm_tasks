# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

from typing import List

def specialArray(nums: List[int]) -> int:
    nums.sort(); length = len(nums); l, r = 0, length

    if length <= nums[0]: return length

    while l <= r:
        m = (l + r) // 2; count = 0

        for idx, num in enumerate(nums):
            if num >= m: count = length - idx; break
    
        if count == m: return count
        elif count < m: r = m - 1
        else: l = m + 1            
    
    return -1


assert specialArray([3,6,7,7,0]) == -1
assert specialArray([3,5]) == 2
assert specialArray([0,0]) == -1
assert specialArray([0,4,3,0,4]) == 3

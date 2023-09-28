# https://leetcode.com/problems/find-the-middle-index-in-array/description/

from typing import List

def findMiddleIndex(nums: List[int]) -> int:
    left_sum, right_sum = 0, sum(nums)

    for idx, num in enumerate(nums):
        right_sum -= num

        if left_sum == right_sum: return idx

        left_sum += num

    return -1


assert findMiddleIndex([2,3,-1,8,4]) == 3
assert findMiddleIndex([1,-1,4]) == 2
assert findMiddleIndex([2,5]) == -1

# https://github.com/Imwisagist/Leetcode_algorithm_tasks

from typing import List

def pivotIndex(nums: List[int]) -> int:
    left_sum, right_sum = 0, sum(nums)

    for idx, num in enumerate(nums):
        right_sum -= num

        if left_sum == right_sum: return idx

        left_sum += num
    
    return -1


assert pivotIndex([-1,-1,0,1,1,0]) == 5
assert pivotIndex([1,7,3,6,5,6]) == 3
assert pivotIndex([1,2,3]) == -1
assert pivotIndex([2,1,-1]) == 0

# https://leetcode.com/problems/squares-of-a-sorted-array/

from collections import deque
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    answer = deque()
    left_index, right_index = 0, len(nums) - 1
    left, right = abs(nums[left_index]), abs(nums[right_index])
    
    while left_index <= right_index:
        if left > right:
            answer.appendleft(left * left)
            left_index += 1
            left = abs(nums[left_index])
        else:
            answer.appendleft(right * right)
            right_index -= 1
            right = abs(nums[right_index])

    return list(answer)


assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

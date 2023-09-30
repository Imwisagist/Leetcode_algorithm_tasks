# https://leetcode.com/problems/132-pattern/description/

from typing import List

def find132pattern(nums: List[int]) -> bool:
    stack,third = [],float('-inf')

    for n in reversed(nums):
        if n < third: return True

        while stack and stack[-1] < n:
            third = stack.pop()

        stack.append(n)

    return False


assert find132pattern([1,2,3,4]) is False
assert find132pattern([3,1,4,2]) is True
assert find132pattern([-1,3,2,0]) is True

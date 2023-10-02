# https://leetcode.com/problems/sum-of-squares-of-special-elements/description/

from typing import List

def sumOfSquares(nums: List[int]) -> int:
    n = len(nums)

    return nums[n-1]**2 + sum(
        nums[i-1]**2
        for i in range(1,(n//2)+1)
        if n % i == 0
    )


assert sumOfSquares([1,2,3,4]) == 21
assert sumOfSquares([2,7,1,19,18,3]) == 63

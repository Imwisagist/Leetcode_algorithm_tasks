# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/

from typing import List

def minStartValue(nums: List[int]) -> int:
    res = sum = 0

    for i in nums:
        sum += i

        if sum < 0: res = min(res, sum)

    return abs(res) + 1


assert minStartValue([-3,2,-3,4,2]) == 5
assert minStartValue([1,2]) == 1
assert minStartValue([1,-2,-3]) == 5

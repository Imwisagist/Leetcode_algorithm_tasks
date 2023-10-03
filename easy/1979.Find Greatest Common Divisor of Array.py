# https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/

from typing import List

def findGCD(nums: List[int]) -> int:
    min,max = float("inf"),float("-inf")

    for n in nums:
        if n > max: max = n

        if n < min: min = n

    while min: max, min = min, max % min

    return max


assert findGCD([2,5,6,9,10]) == 2
assert findGCD([7,5,6,8,3]) == 1
assert findGCD([3,3]) == 3

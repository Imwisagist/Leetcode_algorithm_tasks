# https://leetcode.com/problems/number-of-arithmetic-triplets/description/

from typing import List

def arithmeticTriplets(nums: List[int], diff: int) -> int:
    seen = set(nums)

    return sum(num - diff in seen and num - diff * 2 in seen for num in seen)
    

assert arithmeticTriplets([0,1,4,6,7,10], 3) == 2
assert arithmeticTriplets([4,5,6,7,8,9], 2) == 2

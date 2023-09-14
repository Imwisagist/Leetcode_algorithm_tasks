# https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

from typing import List

def numberOfPairs(nums: List[int]) -> List[int]:
    counter: dict = {}

    for num in nums:
        counter[num] = counter.get(num,0) + 1

    pairs: int = sum(cnt // 2 for cnt in counter.values())

    return [pairs, len(nums) - 2 * pairs]


assert numberOfPairs([1,3,2,1,3,2,2]) == [3,1]
assert numberOfPairs([1,1]) == [1,0]

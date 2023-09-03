# https://leetcode.com/problems/distribute-candies/

from typing import List

def distributeCandies(candyType: List[int]) -> int:
    return min(len(set(candyType)), len(candyType) // 2)

assert distributeCandies([1,1,2,2,3,3]) == 3
assert distributeCandies([1,1,2,3]) == 2
assert distributeCandies([6,6,6,6]) == 1

# https://leetcode.com/problems/number-of-distinct-averages/description/

from typing import List

def distinctAverages(nums: List[int]) -> int:
    avg, arr = set(), sorted(nums)

    while arr: avg.add((arr.pop(0) + arr.pop(-1)) / 2)

    return len(avg)


assert distinctAverages([4,1,4,0,3,5]) == 2
assert distinctAverages([1,100]) == 1

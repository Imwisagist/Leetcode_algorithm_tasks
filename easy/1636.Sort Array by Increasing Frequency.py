# https://leetcode.com/problems/sort-array-by-increasing-frequency/

from typing import List

def frequencySort(nums: List[int]) -> List[int]:
    d: dict = {}
    d_get = d.get

    for i in nums: d[i] = d_get(i,0) + 1

    return sorted(nums, key=lambda x: (d[x], -x))

assert frequencySort([1,1,2,2,2,3]) == [3,1,1,2,2,2]
assert frequencySort([2,3,1,3,2]) == [1,3,3,2,2]
assert frequencySort([-1,1,-6,4,5,-6,1,4,1]) == [5,-1,4,4,-6,-6,1,1,1]

# https://leetcode.com/problems/degree-of-an-array/

from typing import List

def findShortestSubArray(nums: List[int]) -> int:
    numbers_count, left_idxs, right_idxs = {}, {}, {}
    degree, shortest = 0, len(nums)
    
    for idx, num in enumerate(nums):
        numbers_count[num] = numbers_count.get(num, 0) + 1
        degree = max(degree, numbers_count[num])
        
        if num not in left_idxs:
            left_idxs[num] = idx
        right_idxs[num] = idx
            
    for num, freq in numbers_count.items():
        if freq == degree:
            shortest = min(shortest, right_idxs[num] - left_idxs[num] + 1)
    
    return shortest


assert findShortestSubArray([1,2,2,3,1]) == 2
assert findShortestSubArray([1,2,2,3,1,4,2]) == 6

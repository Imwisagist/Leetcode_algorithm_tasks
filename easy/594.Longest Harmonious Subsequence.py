# https://leetcode.com/problems/longest-harmonious-subsequence/

from typing import List

def findLHS(nums: List[int]) -> int:
    hashmap, result = {}, 0

    for i in nums:
        hashmap[i] = hashmap.get(i, 0) + 1

    for i in hashmap.keys():
        if i+1 in hashmap:
            result = max(result, hashmap[i] + hashmap[i+1])

    return result


assert findLHS([1,3,2,2,5,2,3,7]) == 5
assert findLHS([1,2,3,4]) == 2
assert findLHS([1,1,1,1]) == 0

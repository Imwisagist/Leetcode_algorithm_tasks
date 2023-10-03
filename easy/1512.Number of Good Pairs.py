# https://leetcode.com/problems/number-of-good-pairs/

from collections import defaultdict
from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
    d,res = defaultdict(int),0

    for n in nums:            
        if n in d: res += d[n]

        d[n] += 1

    return res

assert numIdenticalPairs([1,2,3,1,1,3]) == 4
assert numIdenticalPairs([1,1,1,1]) == 6
assert numIdenticalPairs([1,2,3]) == 0

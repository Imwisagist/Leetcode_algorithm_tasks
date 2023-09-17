# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/description/

from collections import Counter
from typing import List

def mostFrequent(nums: List[int], key: int) -> int:
    c, prev = Counter(), 0

    for num in nums:
        if prev == key: c[num] += 1
        prev = num

    return c.most_common(1)[0][0]


assert mostFrequent([1,100,200,1,100],1) == 100
assert mostFrequent([2,2,2,2,3],2) == 2

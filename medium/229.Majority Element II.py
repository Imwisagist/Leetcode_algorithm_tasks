# https://leetcode.com/problems/majority-element-ii/description/?envType=daily-question&envId=2023-10-05
from collections import defaultdict
from typing import List

def majorityElement(nums: List[int]) -> List[int]:
    n,d = len(nums) / 3, defaultdict(int)

    for i in nums: d[i] += 1

    return [i for i in d if d[i] > n]
        

assert majorityElement([3,2,3]) == [3]
assert majorityElement([1]) == [1]
assert majorityElement([1,2]) == [1,2]

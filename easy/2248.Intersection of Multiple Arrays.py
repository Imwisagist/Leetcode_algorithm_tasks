# https://leetcode.com/problems/intersection-of-multiple-arrays/description/ 

from typing import List
from functools import reduce

def intersection(nums: List[List[int]]) -> List[int]:
    return sorted(reduce(lambda x,y:x&y,map(set,nums)))


assert intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]) == [3,4]
assert intersection([[1,2,3],[4,5,6]]) == []

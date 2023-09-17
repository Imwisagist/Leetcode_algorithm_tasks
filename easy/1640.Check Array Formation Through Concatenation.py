# https://leetcode.com/problems/check-array-formation-through-concatenation/description/

from typing import List

def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
    d: dict = {x[0]:x for x in pieces}; d_get = d.get

    return sum((d_get(x,[]) for x in arr),[]) == arr


assert canFormArray([15,88],[[88],[15]]) is True
assert canFormArray([49,18,16],[[16,18,49]]) is False
assert canFormArray([91,4,64,78],[[78],[4,64],[91]]) is True

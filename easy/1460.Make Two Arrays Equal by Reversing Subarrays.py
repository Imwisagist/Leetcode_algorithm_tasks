# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/

from typing import List

def canBeEqual(target: List[int], arr: List[int]) -> bool:
    d: dict = {}
    d_get = d.get

    for i in target: d[i] = d_get(i,0) + 1

    for i in arr:
        if d_get(i,0) > 0:
            d[i] -= 1
        else: return False
        
    return True


assert canBeEqual([1,2,3,4],[2,4,1,3]) is True
assert canBeEqual([7],[7]) is True
assert canBeEqual([3,7,9],[3,7,11]) is True
assert canBeEqual([1,1,1,1,1],[1,1,1,1,1]) is True
assert canBeEqual([1,2,2,3],[1,1,2,3]) is False

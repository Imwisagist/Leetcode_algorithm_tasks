# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/

from typing import List

def findLucky(arr: List[int]) -> int:
    d: dict = {}
    d_get = d.get

    for num in arr: d[num] = d_get(num,0) + 1
    
    for k, v in sorted(d.items(), reverse=True):
        if k == v: return k

    return -1


assert findLucky([2,2,3,4]) == 2
assert findLucky([1,2,2,3,3,3]) == 3
assert findLucky([2,2,2,3,3]) == -1

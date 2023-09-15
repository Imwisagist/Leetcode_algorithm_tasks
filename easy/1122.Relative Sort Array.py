# https://leetcode.com/problems/relative-sort-array/description/

from typing import List

def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    d: dict = {}

    for i, v in enumerate(arr2): d[v] = i

    return sorted(arr1, key=lambda x: (d.get(x,float('inf')), x))


assert relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
assert relativeSortArray([28,6,22,8,44,17],[22,28,8,6]) == [22,28,8,6,17,44]

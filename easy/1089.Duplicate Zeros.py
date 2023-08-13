# https://leetcode.com/problems/duplicate-zeros/description/

from typing import List

def duplicateZeros(arr: List[int]) -> None:
    l,r, shift = 0, len(arr), 0

    while l < r:
        if arr[l] == 0:
            arr.insert(l,0)
            shift += 1
            l +=1
        l +=1

    for _ in range(shift):
        arr.pop()


arr1: list = [1,0,2,3,0,4,5,0]
duplicateZeros(arr1)
assert arr1 == [1,0,0,2,3,0,0,4]

arr2: list = [1,2,3]
duplicateZeros(arr2)
assert arr2 == [1,2,3]

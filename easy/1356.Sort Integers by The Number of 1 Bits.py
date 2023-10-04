# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/

from typing import List

def sortByBits(arr: List[int]) -> List[int]:
    arr.sort(key=lambda x:[x.bit_count(),x])

    return arr


assert sortByBits([1024,512,256,128,64,32,16,8,4,2,1]) == [1,2,4,8,16,32,64,128,256,512,1024]
assert sortByBits([0,1,2,3,4,5,6,7,8]) == [0,1,2,4,8,3,5,6,7]
assert sortByBits([1024,512,256,128,64,32,16,8,4,2,1]) == [1024,512,256,128,64,32,16,8,4,2,1]

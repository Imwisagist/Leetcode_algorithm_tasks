# https://leetcode.com/problems/count-good-triplets/description/

from typing import List

def countGoodTriplets(arr: List[int], a: int, b: int, c: int) -> int:
    return sum(
        1
        for i,v1 in enumerate(arr)
        for j,v2 in enumerate(arr[i+1:],i+1)
        for v3 in arr[j+1:]
        if (
            abs(v1-v2) <= a and
            abs(v2-v3) <= b and
            abs(v1-v3) <= c
        )
    )


assert countGoodTriplets([3,0,1,1,9,7],7,2,3) == 4
assert countGoodTriplets([1,1,2,2,3],0,0,1) == 0

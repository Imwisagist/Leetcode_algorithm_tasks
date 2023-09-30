# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/

from math import isqrt
from typing import List
from heapq import heappop, heappush, heappushpop

def pickGifts(gifts: List[int], k: int) -> int:
    heap = []
    
    for g in gifts: heappush(heap,-g)

    g = -heappop(heap)

    for _ in range(k): g = -heappushpop(heap,-isqrt(g))

    return g - sum(heap)


assert pickGifts([25,64,9,4,100],4) == 29
assert pickGifts([1,1,1,1],4) == 4

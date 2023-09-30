# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/

from typing import List
from heapq import heappop, heappush

def fillCups(amount: List[int]) -> int:
    heap,res = [],0

    for n in amount: heappush(heap,-n) if n != 0 else None
    
    while len(heap) > 1:
        first,second = heappop(heap),heappop(heap)
        first += 1; second += 1; res += 1

        if first: heappush(heap, first)

        if second: heappush(heap, second)

    if heap: return res - heap[0]
    else: return res


assert fillCups([1,4,2]) == 4
assert fillCups([5,4,4]) == 7
assert fillCups([5,0,0]) == 5

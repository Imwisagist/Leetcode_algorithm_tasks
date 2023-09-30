# https://leetcode.com/problems/last-stone-weight/description/

from typing import List
from heapq import heappop, heappush

def lastStoneWeight(stones: List[int]) -> int:
    heap = []

    for s in stones: heappush(heap,-s)

    while len(heap) > 1:
        x,y = -heappop(heap),-heappop(heap)

        if x != y: heappush(heap,-(x-y))

    if heap: return abs(heap[0])
    else: return 0


assert lastStoneWeight([2,7,4,1,8,1]) == 1
assert lastStoneWeight([1]) == 1

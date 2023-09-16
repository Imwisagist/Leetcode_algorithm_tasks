# https://leetcode.com/problems/fair-candy-swap/description/

from typing import List

def fairCandySwap(aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
    diff = (sum(bobSizes) - sum(aliceSizes)) // 2

    alice = set(aliceSizes)

    for box in bobSizes:
        if box - diff in alice:
            return [box - diff, box]


assert fairCandySwap([1,1],[2,2]) == [1,2]
assert fairCandySwap([1,2],[2,3]) == [1,2]
assert fairCandySwap([2],[1,3]) == [2,3]

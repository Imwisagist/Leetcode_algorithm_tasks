# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/description/

from typing import List

def minCostToMoveChips(position: List[int]) -> int:
    odd = even = 0

    for p in position:
        if p % 2: odd += 1
        else: even += 1

    return even if even < odd else odd


assert minCostToMoveChips([1,2,3]) == 1
assert minCostToMoveChips([2,2,2,3,3]) == 2
assert minCostToMoveChips([1,1000000000]) == 1

# https://leetcode.com/problems/find-the-losers-of-the-circular-game/description/

from itertools import accumulate
from typing import List

def circularGameLosers(n: int, k: int) -> List[int]:
    losers = set(i for i in range(1, n+1))

    for mul in accumulate(i for i in range(n)):
        who_catch_ball = k * mul % n + 1

        if who_catch_ball not in losers: break

        losers.remove(who_catch_ball)

    return losers


assert circularGameLosers(5,2) == [4,5]
assert circularGameLosers(4,4) == [2,3,4]
assert circularGameLosers(8,1) == []

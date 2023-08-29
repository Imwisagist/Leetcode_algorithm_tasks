# https://leetcode.com/problems/arranging-coins/

from math import sqrt

def arrangeCoins(n: int) -> int:
    return int(sqrt(2 * n + 0.25) - 0.50)


assert arrangeCoins(5) == 2
assert arrangeCoins(8) == 3
assert arrangeCoins(81) == 12

# https://leetcode.com/problems/power-of-four/

from math import log

def isPowerOfFour(n: int) -> bool:
    return n > 0 and log(n, 4).is_integer()


assert isPowerOfFour(16) is True
assert isPowerOfFour(5) is False
assert isPowerOfFour(1) is True

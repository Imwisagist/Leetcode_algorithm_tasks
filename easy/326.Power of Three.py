# https://leetcode.com/problems/power-of-three/

from math import log

def isPowerOfThree(n: int) -> bool:
    
    return n > 0 and 3**round(log(n, 3)) == n


assert isPowerOfThree(27) is True
assert isPowerOfThree(0) is False
assert isPowerOfThree(-1) is False

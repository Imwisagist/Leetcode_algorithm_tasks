# https://leetcode.com/problems/power-of-two/

def isPowerOfTwo(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0

assert isPowerOfTwo(1) is True
assert isPowerOfTwo(16) is True
assert isPowerOfTwo(3) is False

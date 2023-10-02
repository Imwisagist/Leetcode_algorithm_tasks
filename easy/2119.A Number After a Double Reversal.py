# https://leetcode.com/problems/a-number-after-a-double-reversal/description/

def isSameAfterReversals(num: int) -> bool:
    return not num or num % 10


assert isSameAfterReversals(526) is True
assert isSameAfterReversals(1800) is False
assert isSameAfterReversals(0) is True

# https://leetcode.com/problems/add-digits/

def addDigits(num: int) -> int:
    return 1 + (num - 1) % 9 if num else 0


assert addDigits(38) == 2
assert addDigits(0) == 0

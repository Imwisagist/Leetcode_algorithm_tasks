# https://leetcode.com/problems/check-if-the-number-is-fascinating/description/

def isFascinating(n: int) -> bool:
    return (n == 192 or 
            n == 219 or 
            n == 273 or 
            n == 327)


assert isFascinating(192) is True
assert isFascinating(100) is False

# https://leetcode.com/problems/count-distinct-numbers-on-board/description/

def distinctIntegers(n: int) -> int:
    return n - 1 if n > 1 else 1


assert distinctIntegers(5) == 4
assert distinctIntegers(3) == 2

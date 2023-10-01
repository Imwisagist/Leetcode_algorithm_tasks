# https://leetcode.com/problems/smallest-even-multiple/description/

def smallestEvenMultiple(n: int) -> int:
    return n if n % 2 == 0 else n * 2


assert smallestEvenMultiple(5) == 10
assert smallestEvenMultiple(6) == 6

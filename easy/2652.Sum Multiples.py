# https://leetcode.com/problems/sum-multiples/description/

def sumOfMultiples(n: int) -> int:
    return sum(i for i in range(3,n+1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)


assert sumOfMultiples(7) == 21
assert sumOfMultiples(10) == 40
assert sumOfMultiples(9) == 30

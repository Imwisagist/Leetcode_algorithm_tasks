# https://leetcode.com/problems/climbing-stairs/

def climbStairs(n: int) -> int:
    one, two = 1, 1

    for i in range(n-1): temp = one; one = one + two; two = temp

    return one


assert climbStairs(2) == 2
assert climbStairs(5) == 8

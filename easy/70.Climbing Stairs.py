# https://leetcode.com/problems/climbing-stairs/

def climbStairs(n: int) -> int:
    if 0 <= n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


assert climbStairs(2) == 2
assert climbStairs(5) == 8

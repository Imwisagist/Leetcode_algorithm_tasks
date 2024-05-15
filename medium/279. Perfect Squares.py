# https://leetcode.com/problems/perfect-squares/


def numSquares(n: int) -> int:
    while n % 4 == 0: n >>= 2

    if n % 8 == 7: return 4
    if int(n ** 0.5) == n ** 0.5: return 1

    for i in range(1, int(n ** 0.5) + 1):
        diff = n - i * i

        if int(diff ** 0.5) == diff ** 0.5: return 2

    return 3


assert numSquares(12) == 3
assert numSquares(13) == 2

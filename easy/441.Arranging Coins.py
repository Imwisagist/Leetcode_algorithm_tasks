# https://leetcode.com/problems/arranging-coins/

def arrangeCoins(n: int) -> int:
    left, right = 0, n

    while left <= right:
        middle = (right + left) // 2
        curr = middle * (middle + 1) // 2
        if curr == n:
            return middle
        if n < curr:
            right = middle - 1
        else:
            left = middle + 1

    return right


assert arrangeCoins(5) == 2
assert arrangeCoins(8) == 3
assert arrangeCoins(81) == 12

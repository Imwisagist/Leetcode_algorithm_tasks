# https://leetcode.com/problems/sqrtx/

def mySqrt(x: int) -> int:
    if x == 0:
        return x

    left, right = 1, x

    while left <= right:
        mid = left + (right - left) // 2
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            right = mid - 1
        else:
            left = mid + 1

    return right


assert mySqrt(4) == 2
assert mySqrt(8) == 2

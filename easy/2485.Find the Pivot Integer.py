# https://leetcode.com/problems/find-the-pivot-integer/description/

def pivotInteger(n: int) -> int:
    left_sum, right_sum = 0, (n+1) * n // 2

    for i in range(1, n+1):
        right_sum -= i

        if left_sum == right_sum: return i

        left_sum += i

    return -1


assert pivotInteger(8) == 6
assert pivotInteger(1) == 1
assert pivotInteger(4) == -1

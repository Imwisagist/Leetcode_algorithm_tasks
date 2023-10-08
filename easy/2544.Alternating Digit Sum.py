# https://leetcode.com/problems/alternating-digit-sum/description/

def alternateDigitSum(n: int) -> int:
    res,sign = 0,1

    while n:
        sign ^= -2
        res += sign * (n%10)
        n //= 10

    return res * sign


assert alternateDigitSum(10) == 1
assert alternateDigitSum(521) == 4
assert alternateDigitSum(111) == 1
assert alternateDigitSum(886996) == 0

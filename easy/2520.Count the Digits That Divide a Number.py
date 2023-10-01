# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/

def countDigits(num: int) -> int:
    res,digit = 0,num

    while digit:
        if num % (digit % 10) == 0: res += 1
        digit //= 10

    return res


assert countDigits(7) == 1
assert countDigits(121) == 2
assert countDigits(1248) == 4

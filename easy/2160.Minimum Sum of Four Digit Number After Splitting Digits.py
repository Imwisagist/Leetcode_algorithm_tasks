# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

def minimumSum(num: int) -> int:
    d = sorted((num % 10,num // 10 % 10,num // 100 % 10,num // 1000))

    return d[0]*10+d[2] + d[1]*10+d[3]


assert minimumSum(2932) == 52
assert minimumSum(4009) == 13

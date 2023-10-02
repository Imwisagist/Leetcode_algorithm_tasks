# https://leetcode.com/problems/number-of-common-factors/description/

from math import gcd

def commonFactors(a: int, b: int) -> int:
    limit,res = gcd(a,b),0

    for i in range(1,int(limit**0.5)+1):
        if limit % i == 0: res += 2

    return res if i*i != limit else res - 1


assert commonFactors(12,6) == 4
assert commonFactors(25,30) == 2

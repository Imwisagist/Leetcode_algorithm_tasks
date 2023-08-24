# https://leetcode.com/problems/ugly-number/

def isUgly(n: int) -> bool:
    if n == 0: return 0
            
    for i in 2,3,5:
        while n % i == 0:
            n //= i

    return n == 1


assert isUgly(6) is True
assert isUgly(1) is True
assert isUgly(14) is False

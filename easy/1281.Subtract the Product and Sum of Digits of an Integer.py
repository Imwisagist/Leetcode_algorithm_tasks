# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

def subtractProductAndSum(n: int) -> int:
    product = sum = 1

    while n:
        digit = n % 10; n //= 10
        product *= digit; sum += digit
        
    return product - sum + 1


assert subtractProductAndSum(234) == 15
assert subtractProductAndSum(4421) == 21

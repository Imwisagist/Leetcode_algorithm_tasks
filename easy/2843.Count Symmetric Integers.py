# https://leetcode.com/problems/count-symmetric-integers/description/

def countSymmetricIntegers(low: int, high: int) -> int:
    return sum(
        1
        for n in range(11,100,11)
        if low <= n <= high
    ) + sum(
        1
        for n in range(max(1001,low),min(high+1,10000))
        if n%10 + n//10%10 == n//100%10 + n//1000
    ) 


assert countSymmetricIntegers(2,11) == 1
assert countSymmetricIntegers(1,100) == 9
assert countSymmetricIntegers(1200,1230) == 4

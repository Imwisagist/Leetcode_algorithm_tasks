# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

def countPrimeSetBits(left: int, right: int) -> int:
    return sum(
        1
        for i in range(left,right+1)
        if i.bit_count() in {2,3,5,7,11,13,17,19}
    )


assert countPrimeSetBits(6,10) == 4
assert countPrimeSetBits(10,15) == 5

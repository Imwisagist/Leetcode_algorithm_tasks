# https://leetcode.com/problems/number-of-1-bits/

def hammingWeight(n: int) -> int:
    return n.bit_count()


assert hammingWeight(0b00000000000000000000000000001011) == 3
assert hammingWeight(0b00000000000000000000000010000000) == 1
assert hammingWeight(0b11111111111111111111111111111101) == 31

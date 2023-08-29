# https://leetcode.com/problems/hamming-distance/

def hammingDistance(x: int, y: int) -> int:
    return (x ^ y).bit_count()


assert hammingDistance(1, 4) == 2
assert hammingDistance(3, 1) == 1

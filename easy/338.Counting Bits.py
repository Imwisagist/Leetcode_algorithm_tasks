# https://leetcode.com/problems/counting-bits/

from typing import List

def countBits(n: int) -> List[int]:
    
    return [i.bit_count() for i in range(n + 1)]

assert countBits(2) == [0, 1, 1]
assert countBits(5) == [0, 1, 1, 2, 1, 2]

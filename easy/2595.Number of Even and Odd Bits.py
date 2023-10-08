# https://leetcode.com/problems/number-of-even-and-odd-bits/description/

from typing import List

def evenOddBit(n: int) -> List[int]:                
    return [
        (int('0101010101',2)&n).bit_count(),
        (int('1010101010',2)&n).bit_count(),
    ]


assert evenOddBit(17) == [2,0]
assert evenOddBit(2) == [0,1]

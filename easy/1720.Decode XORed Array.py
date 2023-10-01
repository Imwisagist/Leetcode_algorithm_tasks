# https://leetcode.com/problems/decode-xored-array/description/

from functools import reduce
from typing import List

def decode(encoded: List[int], first: int) -> List[int]:
    res = [first]

    for i in range(len(encoded)):
        res.append(res[i] ^ encoded[i])

    return res


assert decode([1,2,3],1) == [1,0,2,1]
assert decode([6,2,7,3],4) == [4,2,0,7,4]

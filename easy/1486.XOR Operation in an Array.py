# https://leetcode.com/problems/xor-operation-in-an-array/description/

def xorOperation(n: int, start: int) -> int:
    res = 0

    for i in range(n): res ^= start+2*i

    return res


assert xorOperation(5,0) == 8
assert xorOperation(4,3) == 8

# https://leetcode.com/problems/reverse-bits/

def reverseBits(n: int) -> int:
    n = bin(n)[2:]
    n = '0'*( 32-len(n) ) + n
    
    return int(n[::-1], 2)


assert reverseBits(0b10100101000001111010011100) == 964176192
assert reverseBits(0b11111111111111111111111111111101) == 3221225471

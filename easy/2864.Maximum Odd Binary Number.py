# https://leetcode.com/problems/maximum-odd-binary-number/description/

def maximumOddBinaryNumber(s: str) -> str:
    bits = s.count("1") - 1

    return f'{"1"*bits}{"0"*(len(s)-bits-1)}1'


assert maximumOddBinaryNumber("010") == "001"
assert maximumOddBinaryNumber("0101") == "1001"

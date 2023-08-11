# https://leetcode.com/problems/add-binary/

def addBinary(a: str, b: str) -> str:
    return bin(int(a,2) + int(b,2))[2:]

assert addBinary("11", "1") == "100"
assert addBinary("1010", "1011") == "10101"

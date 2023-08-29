# https://leetcode.com/problems/number-complement/

def findComplement(num: int) -> int:
    inverted_num, mask = ~num, (1 << num.bit_length()) - 1

    return inverted_num & mask


assert findComplement(5) == 2
assert findComplement(1) == 0

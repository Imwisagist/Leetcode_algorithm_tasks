# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

def toHex(num: int) -> str:
    if num == 0: return "0"
    if num < 0: num += 2 ** 32

    map, result = "0123456789abcdef", ""

    while num > 0:
        digit = num % 16
        num = (num - digit) // 16
        result += map[digit]

    return result[::-1]


assert toHex(26) == "1a"
assert toHex(-1) == "ffffffff"

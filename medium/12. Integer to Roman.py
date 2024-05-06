# https://leetcode.com/problems/integer-to-roman/


def intToRoman(num: int) -> str:
    d = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    s = ""

    for digit, symbol in d.items():
        count, remainder = divmod(num, digit)
        s += symbol*count
        num = remainder

    return s


assert intToRoman(3749) == "MMMDCCXLIX"
assert intToRoman(58) == "LVIII"
assert intToRoman(1994) == "MCMXCIV"

# https://leetcode.com/problems/roman-to-integer/

def romanToInt(s: str) -> int:
    roman, result = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}, 0

    for i in range(len(s) - 1):
        num = roman[s[i]]

        if num < roman[s[(i + 1)]]: result -= num
        else: result += num

    return result + roman[s[-1]]


assert romanToInt("I") == 1
assert romanToInt("II") == 2
assert romanToInt("LVIII") == 58
assert romanToInt("MCMXCIV") == 1994

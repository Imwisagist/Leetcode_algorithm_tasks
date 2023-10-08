# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/

def checkString(s: str) -> bool:
    return "ba" not in s


assert checkString("aaabbb") is True
assert checkString("abab") is False
assert checkString("bbb") is True

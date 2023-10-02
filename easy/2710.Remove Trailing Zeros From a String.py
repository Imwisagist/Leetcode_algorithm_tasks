# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/

def removeTrailingZeros(num: str) -> str:
    return num.rstrip("0")


assert removeTrailingZeros("51230100") == "512301"
assert removeTrailingZeros("123") == "123"

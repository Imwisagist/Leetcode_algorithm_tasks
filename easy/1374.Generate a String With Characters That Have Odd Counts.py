# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/description/

def generateTheString(n: int) -> str:
    return "a" * n if n % 2 == 1 else "a" * (n-1) + "b"


assert generateTheString(4) == "aaab"
assert generateTheString(2) == "ab"
assert generateTheString(7) == "aaaaaaa"

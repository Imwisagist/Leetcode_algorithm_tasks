# https://leetcode.com/problems/remove-palindromic-subsequences/description/

def removePalindromeSub(s: str) -> int:
    return int(s == s[::-1]) or 2


assert removePalindromeSub("ababa") == 1
assert removePalindromeSub("abb") == 2
assert removePalindromeSub("baabb") == 2

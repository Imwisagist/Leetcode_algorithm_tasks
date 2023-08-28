# https://leetcode.com/problems/longest-palindrome/

def longestPalindrome(s: str) -> int:
    d, sum = {}, 0

    for i in s:
        d[i] = d.get(i, 0) + 1

    for i in d.values():
        sum += (i // 2) * 2

    return sum if sum == len(s) else sum + 1


assert longestPalindrome("abccccdd") == 7
assert longestPalindrome("a") == 1

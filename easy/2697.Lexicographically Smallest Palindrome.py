# https://leetcode.com/problems/lexicographically-smallest-palindrome/description/

def makeSmallestPalindrome(s: str) -> str:
    l, r, res = 0, len(s) - 1, list(s)

    while l < r:
        left, right = s[l], s[r]

        if left < right: res[l] = left; res[r] = left
        else: res[l] = right; res[r] = right

        l += 1; r -= 1

    return "".join(res)


assert makeSmallestPalindrome("egcfe") == "efcfe"
assert makeSmallestPalindrome("abcd") == "abba"
assert makeSmallestPalindrome("seven") == "neven"

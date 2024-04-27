# https://leetcode.com/problems/longest-palindromic-substring/


def longestPalindrome(s: str) -> str:
    if len(s) < 2: return s

    max_len, max_str = 1, s[0]; center = right = 0
    s = '#' + '#'.join(s) + '#'; n = len(s); dp = [0 for _ in range(n)]

    for i in range(n):
        if i < right: dp[i] = min(right - i, dp[2 * center - i])
        while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < n and s[i - dp[i] - 1] == s[i + dp[i] + 1]: dp[i] += 1
        if i + dp[i] > right: center = i; right = i + dp[i]
        if dp[i] > max_len: max_len = dp[i]; max_str = s[i - dp[i]:i + dp[i] + 1].replace('#', '')

    return max_str


assert longestPalindrome("babad") == "bab"
assert longestPalindrome("cbbd") == "bb"

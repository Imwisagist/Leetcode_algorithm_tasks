# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def lengthOfLongestSubstring(s: str) -> int:
    n, se = len(s), set(); res = left = 0

    for right in range(n):
        r_chr = s[right]

        if r_chr not in se:
            se.add(r_chr)
            res = max(res, right - left + 1)
        else:
            while r_chr in se:
                se.remove(s[left])
                left += 1

            se.add(r_chr)

    return res


assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3

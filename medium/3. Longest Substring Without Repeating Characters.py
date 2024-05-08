# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def lengthOfLongestSubstring(s: str) -> int:
    se = set(); res = l_idx = 0

    for r_idx, r_chr in enumerate(s):
        if r_chr not in se:
            se.add(r_chr)
            res = max(res, r_idx - l_idx + 1)
        else:
            while r_chr in se:
                se.remove(s[l_idx])
                l_idx += 1

            se.add(r_chr)

    return res


assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3

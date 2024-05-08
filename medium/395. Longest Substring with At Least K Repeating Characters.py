# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
from collections import Counter


def longestSubstring(s: str, k: int) -> int:
    count = Counter(s)

    for char in count.keys():
        if count[char] < k:
            return max(longestSubstring(sub, k) for sub in s.split(char))

    return len(s)


assert longestSubstring("ababbc", 2) == 5
assert longestSubstring("ababacb", 3) == 0

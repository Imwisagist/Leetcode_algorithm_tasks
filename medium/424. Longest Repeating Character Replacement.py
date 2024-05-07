# https://leetcode.com/problems/longest-repeating-character-replacement/description/
from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    freq = defaultdict(int)
    left = max_freq = 0

    for right, r_val in enumerate(s):
        freq[r_val] += 1
        max_freq = max(max_freq, freq[r_val])

        if right - left + 1 - max_freq > k:
            freq[s[left]] -= 1
            left += 1

    return len(s) - left


assert characterReplacement("ABAB", 2) == 4
assert characterReplacement("AABABBA", 1) == 4

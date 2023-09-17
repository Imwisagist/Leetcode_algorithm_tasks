# https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/

from collections import Counter

def rearrangeCharacters(s: str, target: str) -> int:
    c, t, r = Counter(s), Counter(target), 0

    while t <= c: c -= t; r += 1

    return r


assert rearrangeCharacters("ilovecodingonleetcode","code") == 2
assert rearrangeCharacters("abcba","abc") == 1
assert rearrangeCharacters("abbaccaddaeea", "aaaaa") == 1

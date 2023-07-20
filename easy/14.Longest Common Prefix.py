# https://leetcode.com/problems/longest-common-prefix/
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    strs.sort()
    first_word, last_word, result = strs[0], strs[-1], []

    for i in range(len(first_word)):
        if first_word[i] != last_word[i]:
            return "".join(result)
        result.append(first_word[i])

    return "".join(result)


assert longestCommonPrefix(["ab", "a"]) == "a"
assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert longestCommonPrefix(["dog", "racecar", "car"]) == ""

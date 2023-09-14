# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

def areOccurrencesEqual(s: str) -> bool:
    chars: dict = {}

    for i in s:
        chars[i] = chars.get(i, 0) + 1

    prev_count = chars[s[0]]

    for count in chars.values():
        if prev_count != count:
            return False

    return True


assert areOccurrencesEqual("abacbc") is True
assert areOccurrencesEqual("aaabb") is False

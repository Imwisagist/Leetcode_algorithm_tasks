# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/description/

def checkAlmostEquivalent(word1: str, word2: str) -> bool:
    for i in set(word1)|set(word2):
        if abs(word1.count(i) - word2.count(i)) > 3: return False

    return True


assert checkAlmostEquivalent("aaaa", "bccb") is False
assert checkAlmostEquivalent("abcdeef", "abaaacc") is True
assert checkAlmostEquivalent("cccddabba","babababab") is True
assert checkAlmostEquivalent("zzzyyy","iiiiii") is False

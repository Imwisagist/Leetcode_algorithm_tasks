# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


assert strStr("sadbutsad", "sad") == 0
assert strStr("leetcode", "leeto") == -1
assert strStr("leeleeto", "leeto") == 3

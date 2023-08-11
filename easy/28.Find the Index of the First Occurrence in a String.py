# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(haystack: str, needle: str) -> int:
    needle_len: int = len(needle)

    for i in range(0, len(haystack) - needle_len + 1):
        if haystack[i] == needle[0]:
            if haystack[i:i + needle_len] == needle:
                return i
            
    return -1

assert strStr("sadbutsad", "sad") == 0
assert strStr("leetcode", "leeto") == -1
assert strStr("leeleeto", "leeto") == 3

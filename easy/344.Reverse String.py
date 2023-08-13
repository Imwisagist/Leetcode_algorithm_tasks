# https://leetcode.com/problems/reverse-string/

from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        s[i], s[(i + 1) * -1] = s[(i + 1) * -1], s[i]


reversed: list = ["o","l","l","e","h"]
s: list = ["h","e","l","l","o"]
reverseString(s)

assert s == reversed

reversed: list = ["h","a","n","n","a","H"]
s: list = ["H","a","n","n","a","h"]
reverseString(s)

assert s == reversed

# # My solution has been created on leetcode

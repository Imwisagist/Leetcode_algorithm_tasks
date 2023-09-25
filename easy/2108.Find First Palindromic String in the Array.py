# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

from typing import List

def firstPalindrome(words: List[str]) -> str:
    for word in words:
        if word == word[::-1]: return word

    return ""


assert firstPalindrome(["abc","car","ada","racecar","cool"]) == "ada"
assert firstPalindrome(["notapalindrome","racecar"]) == "racecar"
assert firstPalindrome(["def","ghi"]) == ""

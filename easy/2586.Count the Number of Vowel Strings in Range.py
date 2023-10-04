# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/

from typing import List

def vowelStrings(words: List[str], left: int, right: int) -> int:
    vowels = {"a","e","i","o","u"}

    return sum(
        1
        for w in words[left:right+1]
        if w[0] in vowels and w[-1] in vowels
    )


assert vowelStrings(["vo","j","i","s","i"],0,3) == 1
assert vowelStrings(["are","amy","u"],0,2) == 2
assert vowelStrings(["hey","aeo","mu","ooo","artro"],1,4) == 3

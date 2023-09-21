# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

from typing import List

def nextGreatestLetter(letters: List[str], target: str) -> str:
    l, r = 0, len(letters) - 1

    if target < letters[l] or target >= letters[r]:
        return letters[l]

    while l < r:
        m = (l + r) // 2

        if letters[m]>target: r = m
        else: l = m + 1

    return letters[l]


assert nextGreatestLetter(["c","f","j"], "a") == "c"
assert nextGreatestLetter(["c","f","j"], "c") == "f"
assert nextGreatestLetter(["x","x","y","y"], "z") == "x"

# https://leetcode.com/problems/sort-the-people/description/

from typing import List

def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    return [name for _, name in sorted(zip(heights, names), reverse=True)]


assert sortPeople(["Mary","John","Emma"], [180,165,170]) == ["Mary","Emma","John"]
assert sortPeople(["Alice","Bob","Bob"], [155,185,150]) == ["Bob","Alice","Bob"]

# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/

from typing import List
from string import ascii_uppercase as au

def cellsInRange(s: str) -> List[str]:
    return [
        i+str(j)
        for i in au[au.index(s[0]):au.index(s[3])+1]
        for j in range(int(s[1]),int(s[4])+1)
    ]


assert cellsInRange("K1:L2") == ["K1","K2","L1","L2"]
assert cellsInRange("A1:F1") == ["A1","B1","C1","D1","E1","F1"]

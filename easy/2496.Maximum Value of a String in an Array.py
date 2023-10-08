# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/

from typing import List

def maximumValue(strs: List[str]) -> int:
    return max(int(s) if s.isdigit() else len(s) for s in strs)


assert maximumValue(["alic3","bob","3","4","00000"]) == 5
assert maximumValue(["1","01","001","0001"]) == 1

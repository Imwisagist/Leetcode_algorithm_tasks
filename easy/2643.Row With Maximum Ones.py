# https://leetcode.com/problems/row-with-maximum-ones/description/

from typing import List

def rowAndMaximumOnes(mat: List[List[int]]) -> List[int]:
    idx = max = 0

    for i,m in enumerate(mat): 
        if sum(m) > max: max = sum(m); idx = i

    return [idx,max]


assert rowAndMaximumOnes([[0,1],[1,0]]) == [0,1]
assert rowAndMaximumOnes([[0,0,0],[0,1,1]]) == [1,2]
assert rowAndMaximumOnes([[0,0],[1,1],[0,0]]) == [1,2]

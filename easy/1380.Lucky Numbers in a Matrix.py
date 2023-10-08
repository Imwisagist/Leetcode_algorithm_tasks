# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/

from typing import List

def luckyNumbers (matrix: List[List[int]]) -> List[int]:
    mrows = [min(row) for row in matrix]
    
    for col in zip(*matrix):
        mc = max(col)

        for mr in mrows:
            if mc == mr: return [mc]


assert luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]) == [15]
assert luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]) == [12]
assert luckyNumbers([[7,8],[1,2]]) == [7]

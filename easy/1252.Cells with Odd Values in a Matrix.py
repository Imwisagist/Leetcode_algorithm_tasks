# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/

from typing import List

def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
    rows,cols = [0]*m,[0]*n
    
    for r,c in indices: rows[r] += 1; cols[c] += 1
    
    return sum(
        1
        for r in rows
        for c in cols
        if (r + c) % 2
    )


assert oddCells(2,3,[[0,1],[1,1]]) == 6
assert oddCells(2,2,[[1,1],[0,0]]) == 0

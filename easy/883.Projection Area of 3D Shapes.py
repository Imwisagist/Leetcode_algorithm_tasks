# https://leetcode.com/problems/projection-area-of-3d-shapes/description/

from typing import List

def projectionArea(grid: List[List[int]]) -> int:
        xy = sum(1 for i in sum(grid, []) if i)
        yz = sum(map(max, zip(*grid)))
        zx = sum(map(max, grid))
        
        return xy + yz + zx 


assert projectionArea([[1,2],[3,4]]) == 17
assert projectionArea([[2]]) == 5
assert projectionArea([[1,0],[0,2]]) == 8

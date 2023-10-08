# https://leetcode.com/problems/shift-2d-grid/description/

from typing import List

def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    n,m = len(grid),len(grid[0]); k %= n*m
    new_grid = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            idx = i*m+j+k
            new_grid[(idx//m)%n][idx%m]=grid[i][j]

    return new_grid

assert shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]],4) == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
assert shiftGrid([[1,2,3],[4,5,6],[7,8,9]],1) == [[9,1,2],[3,4,5],[6,7,8]]
assert shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]],4) == [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
assert shiftGrid([[1,2,3],[4,5,6],[7,8,9]],9) == [[1,2,3],[4,5,6],[7,8,9]]

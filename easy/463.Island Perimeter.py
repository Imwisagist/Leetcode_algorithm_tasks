# https://leetcode.com/problems/island-perimeter/

from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    result: int = 0

    for row in range(len(grid)):
        for column in range(len(grid[0])):
                if grid[row][column]:
                    result += 4
                    if row and grid[row-1][column]:
                        result -= 2                        
                    if column and grid[row][column-1]:
                        result -= 2
                        
    return result


assert islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
assert islandPerimeter([[1]]) == 4
assert islandPerimeter([[1,0]]) == 4

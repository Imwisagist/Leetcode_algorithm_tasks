# https://leetcode.com/problems/largest-local-values-in-a-matrix/description/

from typing import List

def largestLocal(grid: List[List[int]]) -> List[List[int]]:
    offsets = (
        (0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1),(2,2),
    )
    n,res = len(grid),[]

    for i in range(n-2):
        arr = []

        for j in range(n-2): 
            max = 0

            for x,y in offsets:
                cur = grid[i+x][j+y]

                if cur > max: max = cur
                
            arr.append(max)

        res.append(arr)

    return res


assert largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]) == [[9,9],[8,6]]
assert largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == [[2,2,2],[2,2,2],[2,2,2]]

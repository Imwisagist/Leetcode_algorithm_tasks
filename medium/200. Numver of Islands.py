# https://leetcode.com/problems/number-of-islands/
from typing import List


def numIslands(grid: List[List[str]]) -> int:

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0":
            return

        grid[i][j] = "0"

        for off_x, off_y in offsets:
            dfs(i + off_x, j + off_y)

    res = 0
    n = len(grid)
    m = len(grid[0])
    offsets = ((-1, 0), (0, -1), (1, 0), (0, 1))

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "1":
                res += 1
                dfs(row, col)

    return res

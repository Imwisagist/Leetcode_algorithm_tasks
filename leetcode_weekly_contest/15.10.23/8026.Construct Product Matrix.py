from typing import List


def constructProductMatrix(grid: List[List[int]]) -> List[List[int]]:
    mod,prod = 12345,1

    for g in grid:
        for i in g: prod *= i

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = (prod//grid[i][j]) % mod

    return grid


assert constructProductMatrix([[1,2],[3,4]]) == [[24,12],[8,6]]
assert constructProductMatrix([[12345],[2],[1]]) == [[2],[0],[0]]

# TL
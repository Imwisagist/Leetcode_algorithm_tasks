# https://leetcode.com/problems/matrix-cells-in-distance-order/description/

from typing import List

def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
    return sorted(
        [
            (i,j)
            for i in range(rows)
            for j in range(cols)
        ],
            key=lambda p: abs(p[0]-rCenter)+abs(p[1]-cCenter)
    )


assert allCellsDistOrder(1,2,0,0) == [[0,0],[0,1]]
assert allCellsDistOrder(2,2,0,1) == [[0,1],[0,0],[1,1],[1,0]]
assert allCellsDistOrder(2,3,1,2) == [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]

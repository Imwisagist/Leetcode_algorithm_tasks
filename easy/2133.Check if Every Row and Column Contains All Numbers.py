# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

from typing import List

def checkValid(matrix: List[List[int]]) -> bool:
    n: int = len(matrix)

    for row, col in zip(matrix, zip(*matrix)):
        if len(set(row)) != n or len(set(col)) != n:
            return False
        
    return True


assert checkValid([[1,2,3],[3,1,2],[2,3,1]]) is True
assert checkValid([[1,1,1],[1,2,3],[1,2,3]]) is False

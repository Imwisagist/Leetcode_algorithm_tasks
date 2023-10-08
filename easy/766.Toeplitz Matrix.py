# https://leetcode.com/problems/toeplitz-matrix/description/

from collections import deque
from typing import List

def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    if not matrix or not matrix[0]: return False                

    expected = deque(matrix[0])
    
    for row_i in range(1, len(matrix)):
        row = matrix[row_i]; expected.pop()
        expected.appendleft(row[0])

        for col_i in range(1, len(row)):
            if row[col_i] != expected[col_i]: return False

    return True


assert isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]) is True
assert isToeplitzMatrix([[1,2],[2,2]]) is False

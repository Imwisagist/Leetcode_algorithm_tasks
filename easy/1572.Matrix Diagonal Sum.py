# https://leetcode.com/problems/matrix-diagonal-sum/description/
from typing import List


def diagonalSum(mat: List[List[int]]) -> int:
    res, n = 0, len(mat)
    m = n // 2
    res = sum(mat[i][i] + mat[n - 1 - i][i] for i in range(n))

    if n % 2: res -= mat[m][m]

    return res


assert diagonalSum([[7, 3, 1, 9], [3, 4, 6, 9], [6, 9, 6, 6], [9, 5, 8, 5]]) == 55
assert diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
assert diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 8
assert diagonalSum([[5]]) == 5
